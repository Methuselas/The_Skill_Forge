#!/usr/bin/env python3
"""verify_grounding.py — the anti-skim gate.

Shape validation (tools/validate.py) proves a card is well-formed. It does NOT
prove the source was read. A run that skims the source can still emit shape-valid
cards whose locators point at a unit it merely *declared* processed. This tool
closes that hole.

Every `processed` unit must carry a `## Reading receipt` block in its
ledger/<source_id>/units/<unit>.md file: verbatim quotes (for text pages) or
page-image references (for image pages), spread across the unit's page range. This
tool re-extracts those exact pages from the real payload and confirms the
evidence is genuine. Fabricated grounding fails; a skim cannot produce spread-out
verbatim quotes from pages it never extracted.

The receipt is keyed to the payload SHA-256 recorded in SOURCE.md, so it is
verified against the same book the objects claim to come from.

Exit code 0 = every processed unit's receipt verifies. Non-zero = at least one
unit failed; those objects must not ship.

Usage:
    python tools/verify_grounding.py --source <source_id>
    python tools/verify_grounding.py --all
"""
from __future__ import annotations

import argparse
import hashlib
import io
import math
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

from PIL import Image

MIN_QUOTE_WORDS = 6          # a quote shorter than this is too weak to prove reading
COVERAGE_STRIDE = 8          # require ~1 verified quote per this many pages of the unit
MIN_RECEIPT_ROWS = 2         # absolute floor, even for a tiny unit
SPREAD_FRACTION = 0.5        # cited pages must span at least this fraction of the unit


def norm(text: str) -> str:
    """Lowercase, drop non-alphanumerics to spaces, collapse whitespace.

    Makes quote matching robust to PDF hyphenation artifacts, smart quotes, and
    spacing without letting a fuzzy match pass unrelated text.
    """
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"[^0-9a-z]+", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_frontmatter_field(text: str, field: str) -> str | None:
    m = re.search(rf"^{re.escape(field)}:\s*(.+?)\s*$", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def parse_units(units_md: Path) -> list[dict]:
    """Return processed units with their page span parsed from the locator."""
    units = []
    for line in units_md.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 4 or cols[0] in ("unit_id", "---") or set(cols[0]) <= {"-"}:
            continue
        unit_id, _label, locator, status = cols[0], cols[1], cols[2], cols[3]
        if status != "processed":
            continue
        pages = re.findall(r"(\d+)", locator)
        span = (int(pages[0]), int(pages[-1])) if pages else None
        units.append({"unit_id": unit_id, "locator": locator, "span": span})
    return units


def extract_pages_text(payload: Path, first: int, last: int, offset: int, pdftotext: str) -> str:
    # Receipts cite book page numbers (matching object locators); pdftotext needs
    # physical PDF pages. SOURCE.md's pdf_page_offset bridges the two.
    out = subprocess.run(
        [pdftotext, "-f", str(first + offset), "-l", str(last + offset), str(payload), "-"],
        capture_output=True, text=True,
    )
    return out.stdout or ""


RECEIPT_HEADER = re.compile(r"^##\s+Reading receipt\s*$", re.MULTILINE)
ROW_RE = re.compile(r"^\|\s*([0-9]+(?:\s*[-–]\s*[0-9]+)?)\s*\|\s*(.+?)\s*\|\s*$")


def parse_receipt(unit_md: Path) -> list[dict] | None:
    text = unit_md.read_text(encoding="utf-8")
    m = RECEIPT_HEADER.search(text)
    if not m:
        return None
    block = text[m.end():]
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("## "):   # next section ends the receipt
            break
        rm = ROW_RE.match(line)
        if not rm:
            continue
        page_tok, evidence = rm.group(1), rm.group(2)
        nums = [int(n) for n in re.findall(r"\d+", page_tok)]
        if not nums or evidence.lower() in ("evidence",):
            continue
        pages = (nums[0], nums[-1])
        row = {"pages": pages, "raw": evidence}
        vmatch = re.search(r"(render|image):\s*([^|]+)", evidence, re.IGNORECASE)
        if vmatch:
            row["kind"] = vmatch.group(1).lower()
            row["locator"] = vmatch.group(2).strip()
        else:
            qmatch = re.search(r'"([^"]+)"', evidence)
            row["kind"] = "quote"
            row["quote"] = qmatch.group(1) if qmatch else evidence
        rows.append(row)
    return rows


def verify_decodable_image(stream, label: str) -> str | None:
    try:
        with Image.open(stream) as image:
            image.verify()
    except Exception as exc:  # Pillow exposes several format-specific exceptions.
        return f"cannot decode image evidence '{label}': {exc}"
    return None


def verify_visual_locator(repo_root: Path, locator: str) -> str | None:
    """Verify a direct image or an exact ZIP member (`archive.zip::page.jpg`)."""
    archive_token, separator, member = locator.partition("::")
    evidence_path = Path(archive_token)
    if not evidence_path.is_absolute():
        evidence_path = repo_root / evidence_path
    if not evidence_path.is_file():
        return f"visual evidence missing file '{archive_token}'"
    if not separator:
        with evidence_path.open("rb") as stream:
            return verify_decodable_image(stream, locator)
    if not member:
        return f"visual evidence has an empty ZIP member in '{locator}'"
    try:
        with zipfile.ZipFile(evidence_path) as archive:
            try:
                payload = archive.read(member)
            except KeyError:
                return f"visual evidence ZIP member not found '{locator}'"
    except (OSError, zipfile.BadZipFile) as exc:
        return f"visual evidence archive is unreadable '{archive_token}': {exc}"
    return verify_decodable_image(io.BytesIO(payload), locator)


def verify_unit(source_dir: Path, payload: Path, unit: dict, offset: int, visual: bool, pdftotext: str) -> list[str]:
    """Return a list of failure strings (empty = pass)."""
    unit_id = unit["unit_id"]
    fails: list[str] = []
    unit_md = source_dir / "units" / f"{unit_id}.md"
    if not unit_md.exists():
        return [f"{unit_id}: no units/{unit_id}.md ledger file"]
    rows = parse_receipt(unit_md)
    if rows is None:
        return [f"{unit_id}: processed unit has no '## Reading receipt' block"]
    if not rows:
        return [f"{unit_id}: reading receipt is empty"]

    span = unit["span"]
    if span:
        page_span = max(1, span[1] - span[0] + 1)
        required = max(MIN_RECEIPT_ROWS, math.ceil(page_span / COVERAGE_STRIDE))
    else:
        page_span, required = None, MIN_RECEIPT_ROWS
    # For a visual source, caption quotes do not prove you looked at the figures.
    # The evidence that counts is a rendered page or a source-provided page image.
    visual_rows = [r for r in rows if r["kind"] in {"render", "image"}]
    if visual:
        if not visual_rows:
            fails.append(f"{unit_id}: visual source — unit needs page-image evidence (render: or image: rows); "
                         f"caption quotes alone do not prove you saw the figures")
        counting = visual_rows or rows
    else:
        counting = rows

    if len(counting) < required:
        kind = "page-image rows" if visual else "receipt rows"
        fails.append(f"{unit_id}: {len(counting)} {kind}, needs >= {required} to cover pp. {unit['locator']}")

    cited = [p for r in counting for p in r["pages"]]
    if span:
        out_of_range = [p for p in cited if not (span[0] <= p <= span[1])]
        if out_of_range:
            fails.append(f"{unit_id}: receipt cites pages outside the unit range {span}: {sorted(set(out_of_range))}")
        if page_span > COVERAGE_STRIDE and cited:
            spread = max(cited) - min(cited)
            if spread < SPREAD_FRACTION * page_span:
                fails.append(f"{unit_id}: receipt clustered on pp. {min(cited)}-{max(cited)}; must span >= "
                             f"{SPREAD_FRACTION:.0%} of the {page_span}-page unit (read the whole unit, not the opening)")

    for r in rows:
        first, last = r["pages"]
        if r["kind"] in {"render", "image"}:
            error = verify_visual_locator(source_dir.parents[1], r["locator"])
            if error:
                fails.append(f"{unit_id} p{first}: {error}")
        else:
            quote = r["quote"]
            nq = norm(quote)
            if len(nq.split()) < MIN_QUOTE_WORDS:
                fails.append(f"{unit_id} p{first}: quote too short (< {MIN_QUOTE_WORDS} words): \"{quote}\"")
                continue
            page_text = norm(extract_pages_text(payload, first, last, offset, pdftotext))
            if not page_text:
                fails.append(f"{unit_id} p{first}: no extractable text on this page — use a render: entry, not a quote")
            elif nq not in page_text:
                fails.append(f"{unit_id} p{first}: quote NOT FOUND in the actual page text: \"{quote}\"")
    return fails


def verify_source(source_dir: Path, pdftotext: str) -> tuple[int, int, list[str]]:
    source_id = source_dir.name
    source_md = source_dir / "SOURCE.md"
    if not source_md.exists():
        return 0, 0, [f"{source_id}: no SOURCE.md"]
    smd = source_md.read_text(encoding="utf-8")
    payload_path = read_frontmatter_field(smd, "payload_path")
    want_hash = read_frontmatter_field(smd, "sha256")
    if not payload_path:
        return 0, 0, [f"{source_id}: SOURCE.md has no payload_path"]
    payload = source_dir.parents[1] / payload_path
    if not payload.exists():
        return 0, 0, [f"{source_id}: payload not found at {payload_path} — cannot verify grounding against the real book"]
    if want_hash and sha256_of(payload) != want_hash:
        return 0, 0, [f"{source_id}: payload sha256 does not match SOURCE.md — wrong or altered book"]
    offset_raw = read_frontmatter_field(smd, "pdf_page_offset")
    offset = int(offset_raw) if offset_raw and offset_raw.lstrip("-").isdigit() else 0
    visual = (read_frontmatter_field(smd, "visual") or "false").strip().lower() in ("true", "yes", "1")

    units = parse_units(source_dir / "UNITS.md")
    fails: list[str] = []
    for unit in units:
        fails += verify_unit(source_dir, payload, unit, offset, visual, pdftotext)
    return len(units), sum(1 for u in units if not any(f.startswith(u["unit_id"]) for f in fails)), fails


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify that processed units were actually read (anti-skim gate).")
    ap.add_argument("--source", help="source_id under ledger/ to verify")
    ap.add_argument("--all", action="store_true", help="verify every source in the registry")
    ap.add_argument("--ledger", default="ledger", help="ledger root (default: ledger)")
    ap.add_argument("--pdftotext", default=shutil.which("pdftotext") or "pdftotext")
    args = ap.parse_args()

    ledger_root = Path(args.ledger)
    if args.source:
        targets = [ledger_root / args.source]
    elif args.all:
        targets = [p for p in ledger_root.iterdir() if p.is_dir() and (p / "SOURCE.md").exists()]
    else:
        ap.error("give --source <id> or --all")
        return 2

    total_fail = 0
    for source_dir in targets:
        n_units, n_ok, fails = verify_source(source_dir, args.pdftotext)
        if fails:
            total_fail += len(fails)
            print(f"FAIL {source_dir.name}: {n_ok}/{n_units} processed units verified")
            for f in fails:
                print(f"  - {f}")
        else:
            print(f"PASS {source_dir.name}: {n_units} processed unit(s) grounded against the source")

    if total_fail:
        print(f"\nGROUNDING FAILED: {total_fail} issue(s). These objects are not grounded — do not ship them.")
        return 1
    print("\nGROUNDING OK: every processed unit is backed by verified source evidence.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

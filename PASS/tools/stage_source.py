#!/usr/bin/env python3
"""Stage a source payload into the private authoring workspace.

    python PASS/tools/stage_source.py "D:/Sources/Programming/Practice/Code Complete.pdf"

Does the whole admission run-up in one step, in the order PASS requires:

    copy -> SHA-256 -> duplicate guard -> preflight -> SOURCE.md

The file is **copied, never moved**. The original stays the evidentiary source;
the staged copy is only the working payload the tools read.

Two flows, chosen by what the hash says:

* **New source.** Scaffolds `ledger/<source_id>/SOURCE.md` from the template with
  the hash, payload path, and preflight results already filled in, and stops so you
  can write the unit scheme by hand. It never invents a unit scheme, because that
  is a reading decision.
* **Known source.** If the hash matches a source already in the ledger, this is a
  re-attach — the common case after a clean checkout, since payloads are gitignored.
  It restores the payload to that source's recorded `payload_path` and leaves the
  ledger alone.

The duplicate guard reads every `SOURCE.md` rather than `REGISTRY.md`, because the
per-source ledger is the authority and the registry is a summary that can go stale.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from paths import default_ledger_root  # noqa: E402

TOOLS = Path(__file__).resolve().parent
TEMPLATE = TOOLS.parent / "templates" / "SOURCE_TEMPLATE.md"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def slugify(name: str) -> str:
    """A filename-derived starting point for a source_id, not a decision."""
    text = name.lower()
    text = re.sub(r"\.(pdf|txt|epub|zip)$", "", text)
    text = re.sub(r"[\u2010-\u2015]", "-", text)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")


def scalar(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    return match.group(1) if match else None


def known_sources(ledger_root: Path) -> dict[str, tuple[str, Path]]:
    """sha256 -> (source_id, SOURCE.md path) for everything already admitted."""
    found: dict[str, tuple[str, Path]] = {}
    if not ledger_root.is_dir():
        return found
    for source_md in sorted(ledger_root.glob("*/SOURCE.md")):
        digest = scalar(source_md.read_text(encoding="utf-8"), "sha256")
        if digest and re.fullmatch(r"[0-9a-f]{64}", digest):
            found[digest] = (source_md.parent.name, source_md)
    return found


def run_preflight(payload: Path, visual: bool, vision_capable: bool) -> tuple[bool, str]:
    command = [sys.executable, str(TOOLS / "preflight_pdf.py"), str(payload)]
    if visual:
        command.append("--visual")
    if vision_capable:
        command.append("--vision-capable")
    result = subprocess.run(command, text=True, capture_output=True)
    return result.returncode == 0, (result.stdout + result.stderr).strip()


def preflight_fields(report: str) -> dict[str, str]:
    fields = {"text_layer": "none", "visual_access": "none"}
    for key in ("text_layer", "visual_access"):
        match = re.search(rf"(?m)^{key}:\s*(\S+)", report)
        if match:
            fields[key] = match.group(1)
    return fields


def scaffold_source_md(
    source_id: str,
    title: str,
    payload_rel: str,
    digest: str,
    media_type: str,
    visual: bool,
    report: str,
) -> str:
    fields = preflight_fields(report)
    text = TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "source_id: <stable_id>": f"source_id: {source_id}",
        "title: <title>": f"title: {title}",
        "media_type: <PDF|text|image|code|other>": f"media_type: {media_type}",
        "payload_path: <repo-relative path>": f"payload_path: {payload_rel}",
        "sha256: <hash>": f"sha256: {digest}",
        "added: <YYYY-MM-DD>": f"added: {date.today().isoformat()}",
        "text_layer: <usable|mixed|none>": f"text_layer: {fields['text_layer']}",
        "visual: <true|false>": f"visual: {'true' if visual else 'false'}",
        "visual_access: <renderer|page_images|both|none>": f"visual_access: {fields['visual_access']}",
    }
    for old, new in replacements.items():
        text = text.replace(old, new, 1)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("payload", type=Path, help="the book or PDF to stage (copied, not moved)")
    parser.add_argument("--source-id", help="override the filename-derived source_id")
    parser.add_argument("--title", help="title for a new SOURCE.md (default: the filename)")
    parser.add_argument("--collection", help="optional grouping under sources/, e.g. programming")
    parser.add_argument("--ledger", type=Path, default=default_ledger_root())
    parser.add_argument("--visual", action="store_true", help="source teaches through images")
    parser.add_argument("--vision-capable", action="store_true")
    parser.add_argument("--force", action="store_true", help="stage even if preflight fails")
    args = parser.parse_args()

    payload = args.payload.expanduser()
    if not payload.is_file():
        print(f"FAIL: no such file: {payload}")
        return 1

    sources_root = args.ledger.parent / "sources"
    print(f"hashing {payload.name} ...")
    digest = sha256_file(payload)
    print(f"  sha256: {digest}")

    # --- duplicate guard -------------------------------------------------
    existing = known_sources(args.ledger).get(digest)
    if existing:
        source_id, source_md = existing
        recorded = scalar(source_md.read_text(encoding="utf-8"), "payload_path")
        destination = (args.ledger.parent / recorded) if recorded else (
            sources_root / source_id / payload.name
        )
        print(f"\nKNOWN SOURCE: this hash is already admitted as '{source_id}'.")
        if destination.is_file() and sha256_file(destination) == digest:
            print(f"  payload already staged at {destination}")
            print("\nREADY: nothing to do — the tools can already read this source.")
            return 0
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(payload, destination)
        print(f"  re-attached to {destination}")
        print("\nREADY: payload restored. SOURCE.md untouched; the ledger already describes this source.")
        return 0

    # --- new source ------------------------------------------------------
    source_id = args.source_id or slugify(payload.name)
    if not re.fullmatch(r"[a-z0-9][a-z0-9_]*", source_id):
        print(f"FAIL: derived source_id '{source_id}' is not a clean slug — pass --source-id")
        return 1
    if (args.ledger / source_id).exists():
        print(f"FAIL: ledger/{source_id}/ exists but its sha256 does not match this file.")
        print("      Either this is a different edition (choose another --source-id) or the")
        print("      recorded hash is wrong. Not overwriting.")
        return 1

    print(f"\nrunning preflight ...")
    ok, report = run_preflight(payload, args.visual, args.vision_capable)
    for line in report.splitlines():
        print(f"  {line}")
    if not ok and not args.force:
        print("\nFAIL: preflight did not pass — not staging. Re-run with --force to override.")
        return 1

    relative = Path("sources") / (args.collection or source_id) / payload.name
    destination = args.ledger.parent / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(payload, destination)
    print(f"\ncopied -> {destination}")
    print(f"  original left in place: {payload}")

    source_dir = args.ledger / source_id
    (source_dir / "units").mkdir(parents=True, exist_ok=True)
    source_md = source_dir / "SOURCE.md"
    source_md.write_text(
        scaffold_source_md(
            source_id,
            args.title or payload.stem,
            relative.as_posix(),
            digest,
            "PDF" if payload.suffix.lower() == ".pdf" else "text",
            args.visual,
            report,
        ),
        encoding="utf-8",
    )
    print(f"scaffolded {source_md}")

    print(f"\nSTAGED: {source_id}")
    print("Next, by hand — these are reading decisions this tool will not make for you:")
    print(f"  1. Write the unit scheme in {source_md.relative_to(args.ledger.parent.parent)}")
    print("     (source-native unit boundary, and the pdf_page_offset once you know it)")
    print(f"  2. Create {(source_dir / 'UNITS.md').relative_to(args.ledger.parent.parent)} with one row per unit")
    print("  3. Add a registry row, then claim the first unit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

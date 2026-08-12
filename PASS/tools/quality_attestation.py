#!/usr/bin/env python3
"""Create and verify content-addressed PASS quality attestations.

A release must not silently bypass grounding just because source payloads are not
kept in Git. Each source therefore carries a QUALITY_ATTESTATION.json beside its
ledger. The attestation binds the accepted grounding state to the exact ledger
and exact set of library cards that cite that source.

Two grounding bases are supported:
- live_verified: verify_grounding.py succeeded against the real source payload.
- canonical_archive_accepted: a human accepted a canonical PASS archive whose
  source/ledger state is preserved here; the archive hash is recorded as
  provenance. This does not pretend the payload was re-read during release.

Any card or ledger change invalidates the attestation until the source is
reviewed/verified and re-attested.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from paths import default_library_root, default_ledger_root

ATTESTATION_NAME = "QUALITY_ATTESTATION.json"
FRONTMATTER = "---\n"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tree_digest(root: Path) -> str:
    """Hash the canonical grounding ledger, excluding historical intake archives.

    Release gating depends on SOURCE.md, UNITS.md, and the per-unit receipts. Large
    evidence/intake archives are archaeology and can be cleaned or reorganized
    without invalidating an otherwise unchanged source attestation.
    """
    h = hashlib.sha256()
    candidates = [root / "SOURCE.md", root / "UNITS.md"]
    units = root / "units"
    if units.is_dir():
        candidates.extend(sorted(p for p in units.rglob("*") if p.is_file()))
    for path in candidates:
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix().encode("utf-8")
        h.update(len(rel).to_bytes(4, "big")); h.update(rel)
        data = path.read_bytes()
        h.update(len(data).to_bytes(8, "big")); h.update(data)
    return h.hexdigest()


def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8", errors="strict")
    if not text.startswith(FRONTMATTER):
        return None
    try:
        _empty, front, _body = text.split(FRONTMATTER, 2)
    except ValueError:
        return None
    data = yaml.safe_load(front)
    return data if isinstance(data, dict) else None




def all_source_object_hashes(library: Path) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for path in sorted(library.rglob("*.md")):
        data = parse_frontmatter(path)
        if not data:
            continue
        ref = data.get("reference")
        card_source = ref.get("source_id") if isinstance(ref, dict) else data.get("source_id")
        if not card_source:
            continue
        source_id = str(card_source)
        result.setdefault(source_id, {})[path.relative_to(library).as_posix()] = sha256_file(path)
    return result

def source_object_hashes(library: Path, source_id: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(library.rglob("*.md")):
        data = parse_frontmatter(path)
        if not data:
            continue
        ref = data.get("reference")
        card_source = ref.get("source_id") if isinstance(ref, dict) else data.get("source_id")
        if str(card_source) != source_id:
            continue
        result[path.relative_to(library).as_posix()] = sha256_file(path)
    return result


def source_sha_from_record(source_md: Path) -> str | None:
    for line in source_md.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("sha256:"):
            value = line.split(":", 1)[1].strip()
            return value or None
    return None


def signature_for(payload: dict[str, Any]) -> str:
    unsigned = {k: v for k, v in payload.items() if k != "attestation_sha256"}
    blob = json.dumps(unsigned, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(blob)


def build_attestation(
    source_id: str,
    library: Path,
    ledger: Path,
    basis: str,
    approved_by: str,
    archive_name: str | None = None,
    archive_sha256: str | None = None,
) -> dict[str, Any]:
    source_dir = ledger / source_id
    source_md = source_dir / "SOURCE.md"
    if not source_md.is_file():
        raise ValueError(f"{source_id}: missing SOURCE.md")
    objects = source_object_hashes(library, source_id)
    if not objects:
        raise ValueError(f"{source_id}: no library objects cite this source")
    data: dict[str, Any] = {
        "schema_version": 1,
        "source_id": source_id,
        "created": date.today().isoformat(),
        "grounding_basis": basis,
        "approved_by": approved_by,
        "source_record_sha256": sha256_file(source_md),
        "source_payload_sha256": source_sha_from_record(source_md),
        "ledger_tree_sha256": tree_digest(source_dir),
        "object_sha256": objects,
    }
    if basis == "canonical_archive_accepted":
        if not archive_name or not archive_sha256:
            raise ValueError("canonical archive attestations require --archive-name and --archive-sha256")
        data["canonical_archive"] = {"name": archive_name, "sha256": archive_sha256}
        data["note"] = (
            "Accepted canonical PASS state. Release verifies this content-addressed attestation; "
            "the original third-party payload is not required to remain in Git."
        )
    elif basis == "live_verified":
        data["note"] = "Grounding was re-verified against the real source payload before attestation."
    else:
        raise ValueError(f"unsupported grounding basis: {basis}")
    data["attestation_sha256"] = signature_for(data)
    return data


def verify_attestation(source_id: str, library: Path, ledger: Path, current_objects: dict[str, str] | None = None) -> list[str]:
    source_dir = ledger / source_id
    path = source_dir / ATTESTATION_NAME
    if not path.is_file():
        return [f"{source_id}: missing {ATTESTATION_NAME}"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{source_id}: unreadable attestation: {exc}"]
    if not isinstance(data, dict):
        return [f"{source_id}: attestation is not a JSON object"]
    problems: list[str] = []
    if data.get("source_id") != source_id:
        problems.append(f"{source_id}: attestation source_id mismatch")
    if data.get("grounding_basis") not in {"live_verified", "canonical_archive_accepted"}:
        problems.append(f"{source_id}: unsupported grounding_basis")
    if data.get("attestation_sha256") != signature_for(data):
        problems.append(f"{source_id}: attestation signature/hash mismatch")
    source_md = source_dir / "SOURCE.md"
    if not source_md.is_file():
        problems.append(f"{source_id}: missing SOURCE.md")
        return problems
    if data.get("source_record_sha256") != sha256_file(source_md):
        problems.append(f"{source_id}: SOURCE.md changed after attestation")
    if data.get("ledger_tree_sha256") != tree_digest(source_dir):
        problems.append(f"{source_id}: ledger evidence changed after attestation")
    current_objects = current_objects if current_objects is not None else source_object_hashes(library, source_id)
    if data.get("object_sha256") != current_objects:
        problems.append(f"{source_id}: cited library objects changed after attestation")
    return problems


def run_gate(script: Path, args: list[str]) -> None:
    result = subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True)
    if result.returncode:
        detail = (result.stdout + "\n" + result.stderr).strip()
        raise ValueError(detail or f"gate failed: {script.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    create = sub.add_parser("create")
    create.add_argument("source_id")
    create.add_argument("--library", type=Path, default=default_library_root())
    create.add_argument("--ledger", type=Path, default=default_ledger_root())
    create.add_argument("--basis", required=True, choices=("live_verified", "canonical_archive_accepted"))
    create.add_argument("--approved-by", required=True)
    create.add_argument("--archive-name")
    create.add_argument("--archive-sha256")
    verify = sub.add_parser("verify")
    verify.add_argument("source_id", nargs="?")
    verify.add_argument("--all", action="store_true")
    verify.add_argument("--library", type=Path, default=default_library_root())
    verify.add_argument("--ledger", type=Path, default=default_ledger_root())
    args = parser.parse_args()

    try:
        library = args.library.resolve(); ledger = args.ledger.resolve()
        if args.cmd == "create":
            tool_dir = Path(__file__).resolve().parent
            # Shape + reference gates must be green when an attestation is issued.
            run_gate(tool_dir / "validate.py", ["--library", str(library), "--ledger", str(ledger)])
            run_gate(tool_dir / "verify_references.py", ["--library", str(library), "--ledger", str(ledger)])
            if args.basis == "live_verified":
                run_gate(tool_dir / "verify_grounding.py", ["--source", args.source_id, "--ledger", str(ledger)])
            data = build_attestation(
                args.source_id, library, ledger, args.basis, args.approved_by,
                args.archive_name, args.archive_sha256,
            )
            out = ledger / args.source_id / ATTESTATION_NAME
            out.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            print(f"PASS: wrote {out}")
            return 0
        if args.all:
            targets = sorted(p.name for p in ledger.iterdir() if p.is_dir() and (p / ATTESTATION_NAME).exists())
        elif args.source_id:
            targets = [args.source_id]
        else:
            parser.error("give source_id or --all")
        failures: list[str] = []
        all_objects = all_source_object_hashes(library)
        for source_id in targets:
            failures.extend(verify_attestation(source_id, library, ledger, all_objects.get(source_id, {})))
        if failures:
            print("ATTESTATION FAILED:")
            for failure in failures: print(f"- {failure}")
            return 1
        print(f"PASS: {len(targets)} quality attestation(s) verified")
        return 0
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

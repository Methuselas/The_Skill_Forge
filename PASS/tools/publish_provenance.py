"""Publish compact public provenance receipts from the private authoring ledger.

The ledger is local-only state. This writes the part a public checkout needs —
one JSON per source under `workspace/provenance/` — so release building and
library validation keep working without publishing the factory's notebooks.

    python PASS/tools/publish_provenance.py --all
    python PASS/tools/publish_provenance.py code_complete_2e

Each receipt is the source's QUALITY_ATTESTATION.json plus the three ledger facts
the library checks need (processed unit ids, whether the source is visual, whether
its images are first-party). Run it after attesting a source; the receipt is stale
until you do, and `--check` reports that without writing.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from paths import default_ledger_root, default_library_root  # noqa: E402
from provenance import (  # noqa: E402
    build_public_fields,
    load_record,
    provenance_root_for,
    record_path,
)

ATTESTATION_NAME = "QUALITY_ATTESTATION.json"


def build_receipt(ledger_root: Path, source_id: str) -> dict:
    attestation_path = ledger_root / source_id / ATTESTATION_NAME
    if not attestation_path.is_file():
        raise ValueError(f"{source_id}: no {ATTESTATION_NAME} — attest the source first")
    attestation = json.loads(attestation_path.read_text(encoding="utf-8"))
    if not isinstance(attestation, dict):
        raise ValueError(f"{source_id}: attestation is not a JSON object")
    receipt = dict(attestation)
    receipt.update(build_public_fields(ledger_root, source_id))
    receipt["provenance_schema"] = 1
    return receipt


def write_receipt(provenance_root: Path, receipt: dict) -> Path:
    provenance_root.mkdir(parents=True, exist_ok=True)
    path = record_path(provenance_root, str(receipt["source_id"]))
    path.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return path


def source_ids(ledger_root: Path) -> list[str]:
    return sorted(path.parent.name for path in ledger_root.glob("*/SOURCE.md"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_id", nargs="?")
    parser.add_argument("--all", action="store_true", help="publish every attested source")
    parser.add_argument("--library", type=Path, default=default_library_root())
    parser.add_argument("--ledger", type=Path, default=default_ledger_root())
    parser.add_argument("--provenance", type=Path, default=None)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report receipts that are missing or stale without writing anything",
    )
    args = parser.parse_args()

    if not args.all and not args.source_id:
        parser.error("give a source_id or --all")
    if not args.ledger.is_dir():
        print(f"FAIL: no authoring ledger at {args.ledger} — this command needs the private state")
        return 1

    provenance_root = args.provenance or provenance_root_for(args.ledger)
    targets = source_ids(args.ledger) if args.all else [args.source_id]

    problems: list[str] = []
    written: list[str] = []
    skipped: list[str] = []
    for source_id in targets:
        try:
            receipt = build_receipt(args.ledger, source_id)
        except ValueError as exc:
            # An unattested source is normal mid-run; only report it when asked
            # for one by name.
            if args.all:
                skipped.append(str(exc))
            else:
                problems.append(str(exc))
            continue
        if args.check:
            current = load_record(provenance_root, source_id)
            if current != receipt:
                problems.append(
                    f"{source_id}: public provenance receipt is missing or stale"
                )
            continue
        write_receipt(provenance_root, receipt)
        written.append(source_id)

    for problem in problems:
        print(f"  - {problem}")
    if args.check:
        if problems:
            print(f"PROVENANCE STALE: {len(problems)} receipt(s) need republishing")
            return 1
        print(f"PROVENANCE OK: {len(targets) - len(skipped)} receipt(s) current")
        return 0
    if problems:
        return 1
    for source_id in written:
        print(f"PASS: wrote {record_path(provenance_root, source_id)}")
    if skipped:
        print(f"({len(skipped)} source(s) not yet attested, skipped)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

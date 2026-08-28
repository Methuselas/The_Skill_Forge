"""Apply structured object findings to the generated pressure-test manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "tests" / "art_pressure" / "manifest.jsonl"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("findings", type=Path)
    args = parser.parse_args()

    findings_data = yaml.safe_load(args.findings.read_text(encoding="utf-8"))
    updates = {finding["object_id"]: finding for finding in findings_data["findings"]}
    records = [
        json.loads(line)
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    applied: set[str] = set()
    for record in records:
        if record["record_kind"] != "object" or record["object_id"] not in updates:
            continue
        finding = updates[record["object_id"]]
        cases = finding["cases"]
        record["status"] = finding["status"]
        record["test_ids"] = [
            value.split()[0] if isinstance(value, str) else f"{finding['finding_id']}_{case.upper()}"
            for case, value in cases.items()
            if case != "human_evidence"
        ]
        record["test_ids"].extend(cases["human_evidence"])
        record["test_ids"] = sorted(set(record["test_ids"]))
        record["finding_ids"] = [finding["finding_id"]]
        record["notes"] = "Outcome-facing Pattern behavior pressure-tested; attached Variants remain separately accountable."
        applied.add(record["object_id"])

    missing = set(updates) - applied
    if missing:
        raise SystemExit(f"Findings did not resolve to object records: {sorted(missing)}")
    MANIFEST.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )
    print(f"Applied {len(applied)} object findings to {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

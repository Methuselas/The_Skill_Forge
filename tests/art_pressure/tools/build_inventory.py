#!/usr/bin/env python3
"""Build the Art pressure-test manifest from live card frontmatter.

The library is authoritative. Existing test progress is preserved by stable
record id while card-owned metadata is refreshed from the current Art tree.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[3]
ART_ROOT = ROOT / "library" / "art"
PRESSURE_ROOT = ROOT / "tests" / "art_pressure"
MANIFEST = PRESSURE_ROOT / "manifest.jsonl"
COVERAGE = PRESSURE_ROOT / "coverage.json"
FRONTMATTER = re.compile(r"\A---\r?\n(?P<front>.*?)\r?\n---\r?\n", re.S)
CARD_PREFIXES = ("PAT_", "DRILL_", "AP_")

STATUSES = {
    "NOT_TESTED",
    "IN_PROGRESS",
    "PASS",
    "PASS_WITH_BOUNDARY_CONFIRMED",
    "CORRECTED",
    "REPLACED",
    "MERGED_OR_ABSORBED",
    "DEPRECATED",
    "NEEDS_MORE_EVIDENCE",
    "HOST_TEST_REQUIRED",
}
TERMINAL_REMOVAL_STATUSES = {"REPLACED", "MERGED_OR_ABSORBED", "DEPRECATED"}
PROGRESS_FIELDS = {
    "status",
    "test_ids",
    "finding_ids",
    "regression_ids",
    "host_test_ids",
    "notes",
}


def load_card(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError(f"missing frontmatter: {path.relative_to(ROOT).as_posix()}")
    data = yaml.safe_load(match.group("front"))
    if not isinstance(data, dict):
        raise ValueError(f"frontmatter is not a map: {path.relative_to(ROOT).as_posix()}")
    return data


def existing_records() -> dict[str, dict[str, Any]]:
    if not MANIFEST.is_file():
        return {}
    records: dict[str, dict[str, Any]] = {}
    for line_number, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        record_id = str(record.get("record_id", ""))
        if not record_id or record_id in records:
            raise ValueError(f"invalid or duplicate record_id at manifest line {line_number}")
        records[record_id] = record
    return records


def progress_for(record_id: str, old: dict[str, dict[str, Any]]) -> dict[str, Any]:
    preserved = {key: old.get(record_id, {}).get(key) for key in PROGRESS_FIELDS}
    preserved["status"] = preserved.get("status") or "NOT_TESTED"
    for key in ("test_ids", "finding_ids", "regression_ids", "host_test_ids"):
        preserved[key] = preserved.get(key) or []
    preserved["notes"] = preserved.get("notes") or ""
    if preserved["status"] not in STATUSES:
        raise ValueError(f"unknown status for {record_id}: {preserved['status']}")
    return preserved


def build_records(
    old: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], Counter[str]]:
    records: list[dict[str, Any]] = []
    incoming: Counter[str] = Counter()
    live_object_ids: set[str] = set()

    for path in sorted(ART_ROOT.rglob("*.md")):
        if not path.name.startswith(CARD_PREFIXES):
            continue
        data = load_card(path)
        object_id = str(data["object_id"])
        if object_id in live_object_ids:
            raise ValueError(f"duplicate Art object_id: {object_id}")
        live_object_ids.add(object_id)
        relative_path = path.relative_to(ROOT).as_posix()
        common = {
            "object_id": object_id,
            "object_type": str(data["object_type"]),
            "object_name": str(data["name"]),
            "card_path": relative_path,
            "library_path": data.get("library_path") or [],
            "stage_binding": str(data.get("stage_binding", "")),
            "foundation_role": str(data.get("foundation_role", "")),
            "routing_class": str(data.get("routing_class", "")),
            "specialization_axis": str(data.get("specialization_axis", "")),
            "tags": data.get("tags") or [],
        }
        record_id = f"object::{object_id}"
        records.append(
            {
                "record_id": record_id,
                "record_kind": "object",
                **common,
                "variant_id": None,
                "variant_name": None,
                **progress_for(record_id, old),
            }
        )

        foundation = data.get("foundation_object_id")
        if foundation and foundation != "none":
            incoming[str(foundation)] += 1
        for link in data.get("cross_links") or []:
            if isinstance(link, dict) and link.get("target_object_id"):
                incoming[str(link["target_object_id"])] += 1

        for variant in data.get("variants") or []:
            if not isinstance(variant, dict) or not variant.get("variant_id"):
                raise ValueError(f"malformed variant in {relative_path}")
            variant_id = str(variant["variant_id"])
            variant_record_id = f"variant::{object_id}::{variant_id}"
            records.append(
                {
                    "record_id": variant_record_id,
                    "record_kind": "variant",
                    **common,
                    "variant_id": variant_id,
                    "variant_name": str(variant.get("variant_name", "")),
                    "variant_basis": str(variant.get("variant_basis", "")),
                    **progress_for(variant_record_id, old),
                }
            )

    current_record_ids = {record["record_id"] for record in records}
    for record_id, record in old.items():
        if record_id in current_record_ids:
            continue
        if record.get("status") not in TERMINAL_REMOVAL_STATUSES:
            raise ValueError(
                f"{record_id} disappeared from canon without a terminal removal status"
            )
        retained = dict(record)
        retained["record_kind"] = "retired"
        records.append(retained)

    records.sort(key=lambda item: item["record_id"])
    return records, incoming


def render_manifest(records: list[dict[str, Any]]) -> str:
    return "".join(json.dumps(record, sort_keys=True) + "\n" for record in records)


def render_coverage(records: list[dict[str, Any]], incoming: Counter[str]) -> str:
    object_records = [record for record in records if record["record_kind"] == "object"]
    variant_records = [record for record in records if record["record_kind"] == "variant"]
    by_type = Counter(record["object_type"] for record in object_records)
    by_status = Counter(record["status"] for record in records)
    names = {record["object_id"]: record["object_name"] for record in object_records}
    hubs = [
        {
            "object_id": object_id,
            "object_name": names[object_id],
            "incoming_relationships": count,
        }
        for object_id, count in incoming.most_common()
        if object_id in names
    ][:30]
    summary = {
        "schema_version": 1,
        "objects": len(object_records),
        "variants": len(variant_records),
        "records": len(records),
        "objects_by_type": dict(sorted(by_type.items())),
        "records_by_status": dict(sorted(by_status.items())),
        "high_centrality_targets": hubs,
    }
    return json.dumps(summary, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files differ")
    args = parser.parse_args()

    old = existing_records()
    records, incoming = build_records(old)
    outputs = {
        MANIFEST: render_manifest(records),
        COVERAGE: render_coverage(records, incoming),
    }
    stale: list[Path] = []
    for path, content in outputs.items():
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current == content:
            continue
        if args.check:
            stale.append(path)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="")

    if stale:
        for path in stale:
            print(f"stale: {path.relative_to(ROOT).as_posix()}")
        return 1
    action = "current" if args.check else "written"
    print(f"PASS: {len(records)} Art pressure records {action}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, TypeError, ValueError, yaml.YAMLError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)

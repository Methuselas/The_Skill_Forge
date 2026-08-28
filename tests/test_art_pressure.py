"""Contracts for the resumable Art empirical pressure-test inventory."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PRESSURE = ROOT / "tests" / "art_pressure"
TOOL = PRESSURE / "tools" / "build_inventory.py"
MANIFEST = PRESSURE / "manifest.jsonl"
COVERAGE = PRESSURE / "coverage.json"
STATE = PRESSURE / "state.yaml"
FIXTURES = PRESSURE / "fixture_manifest.yaml"


def records() -> list[dict]:
    return [
        json.loads(line)
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


class ArtPressureInventory(unittest.TestCase):
    def test_generated_inventory_is_current(self) -> None:
        result = subprocess.run(
            [sys.executable, str(TOOL), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_every_live_art_object_and_variant_has_one_record(self) -> None:
        manifest_records = records()
        record_ids = [record["record_id"] for record in manifest_records]
        self.assertEqual(len(record_ids), len(set(record_ids)))

        expected_objects = 0
        expected_variants = 0
        for path in (ROOT / "library" / "art").rglob("*.md"):
            if not path.name.startswith(("PAT_", "DRILL_", "AP_")):
                continue
            text = path.read_text(encoding="utf-8")
            data = yaml.safe_load(text.split("---", 2)[1])
            expected_objects += 1
            expected_variants += len(data.get("variants") or [])

        self.assertEqual(
            sum(record["record_kind"] == "object" for record in manifest_records),
            expected_objects,
        )
        self.assertEqual(
            sum(record["record_kind"] == "variant" for record in manifest_records),
            expected_variants,
        )

    def test_generated_paths_are_repo_relative(self) -> None:
        for record in records():
            path = record.get("card_path")
            if path:
                self.assertFalse(Path(path).is_absolute(), record["record_id"])
                self.assertTrue(path.startswith("library/art/"), record["record_id"])

    def test_coverage_totals_match_manifest(self) -> None:
        manifest_records = records()
        coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
        self.assertEqual(coverage["records"], len(manifest_records))
        self.assertEqual(
            coverage["objects"],
            sum(record["record_kind"] == "object" for record in manifest_records),
        )
        self.assertEqual(
            coverage["variants"],
            sum(record["record_kind"] == "variant" for record in manifest_records),
        )

    def test_current_batch_pointer_resolves_and_matches_id(self) -> None:
        state = yaml.safe_load(STATE.read_text(encoding="utf-8"))
        current = state["next_batch"]
        batch_path = ROOT / current["batch_file"]
        self.assertTrue(batch_path.is_file(), current["batch_file"])
        batch = yaml.safe_load(batch_path.read_text(encoding="utf-8"))
        self.assertEqual(batch["batch_id"], current["id"])

    def test_completed_batch_findings_cover_required_cases(self) -> None:
        state = yaml.safe_load(STATE.read_text(encoding="utf-8"))
        for completed in state.get("completed_batches", []):
            batch = yaml.safe_load((ROOT / completed["batch_file"]).read_text(encoding="utf-8"))
            findings = yaml.safe_load((ROOT / completed["findings_file"]).read_text(encoding="utf-8"))
            by_owner = {finding["object_id"]: finding for finding in findings["findings"]}
            required = set(batch["required_cases_per_owner"])
            self.assertEqual(
                {owner["object_id"] for owner in batch["object_owners"]},
                set(by_owner),
            )
            for finding in by_owner.values():
                self.assertTrue(required.issubset(finding["cases"]), finding["object_id"])

    def test_selected_human_fixtures_have_both_review_passes(self) -> None:
        fixtures = yaml.safe_load(FIXTURES.read_text(encoding="utf-8"))
        for fixture in fixtures["selected_fixtures"]:
            self.assertEqual({"diagnostic", "learning"}, set(fixture["review_passes"]))
            self.assertTrue(fixture["credit_verification"])
            self.assertTrue(fixture["page_locators"])


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "PASS" / "tools"))

from validate import validate_ledgers, validate_registry  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def source_text(
    source_id: str,
    *,
    added: str,
    status: str,
    contract: bool = True,
    legacy: str = "none",
) -> str:
    contract_lines = (
        f"unit_ledger_contract: 3\nteaching_lane_grandfathered_units: {legacy}\n"
        if contract else ""
    )
    return (
        f"# Source\n\nsource_id: {source_id}\nadded: {added}\nstatus: {status}\n"
        f"{contract_lines}"
    )


def units_text(status: str) -> str:
    return (
        "| unit_id | label | locator | status | objects | notes |\n"
        "|---|---|---|---|---|---|\n"
        f"| u01 | Unit | pp. 1-2 | {status} | 1 | |\n"
    )


V2_LEDGER = """# u01

read: 2026-08-14
second_read: 2026-08-14
ledger_format: 2
candidate_count: 1

| candidate | type | disposition | object_id | grounding | learner_decision | variant_basis | method_or_policy | tradeoff | note |
|---|---|---|---|---|---|---|---|---|---|
| Candidate | pattern | new | PAT_candidate | p. 1 example | | | | | |
"""


V3_LEDGER = """# u01

read: 2026-08-15
second_read: 2026-08-15
ledger_format: 3
candidate_count: 2
teaching_lane_review: complete
teaching_candidate_count: 1

| candidate | type | lane | teaching_scope | teaching_route | disposition | object_id | grounding | learner_decision | variant_basis | method_or_policy | tradeoff | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Domain move | pattern | skill | — | — | new | PAT_domain_move | p. 1 example | | | | | |
| Shared sequence | pattern | teach | cross-domain | teaching:PAT_shared_sequence | new | PAT_shared_sequence | p. 2 sequence | | | | | |
"""


class TeachingLaneLedgerTests(unittest.TestCase):
    def test_new_source_must_declare_contract_three(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp)
            source = ledger / "new_source"
            write(
                source / "SOURCE.md",
                source_text("new_source", added="2026-08-15", status="queued", contract=False),
            )
            errors = [issue.error for issue in validate_ledgers(ledger)]
            self.assertTrue(any("require unit_ledger_contract: 3" in error for error in errors))

    def test_new_closed_unit_cannot_use_legacy_ledger(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp)
            source = ledger / "new_source"
            write(source / "SOURCE.md", source_text("new_source", added="2026-08-15", status="complete"))
            write(source / "UNITS.md", units_text("processed"))
            write(source / "units" / "u01.md", V2_LEDGER)
            errors = [issue.error for issue in validate_ledgers(ledger)]
            self.assertTrue(any("requires ledger_format: 3" in error for error in errors))

    def test_historical_closed_unit_can_be_honestly_grandfathered(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp)
            source = ledger / "old_source"
            write(
                source / "SOURCE.md",
                source_text("old_source", added="2026-08-14", status="complete", legacy="u01"),
            )
            write(source / "UNITS.md", units_text("processed"))
            write(source / "units" / "u01.md", V2_LEDGER)
            self.assertEqual(validate_ledgers(ledger), [])

    def test_v3_records_lane_scope_and_top_level_teaching_route(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp)
            source = ledger / "new_source"
            write(source / "SOURCE.md", source_text("new_source", added="2026-08-15", status="complete"))
            write(source / "UNITS.md", units_text("processed"))
            write(source / "units" / "u01.md", V3_LEDGER)
            packages = {"PAT_domain_move": "writing", "PAT_shared_sequence": "teaching"}
            self.assertEqual(validate_ledgers(ledger, packages), [])


class RegistryIntegrityTests(unittest.TestCase):
    def test_registry_status_and_count_must_match_authoritative_units(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp)
            source = ledger / "book"
            write(source / "SOURCE.md", source_text("book", added="2026-08-14", status="complete", contract=False))
            write(source / "UNITS.md", units_text("processed"))
            write(
                ledger / "REGISTRY.md",
                "| source_id | title | author | sha256 (first 12) | status | units | objects | closed |\n"
                "|---|---|---|---|---|---|---|---|\n"
                "| book | Book | Author | abcdef123456 | in-progress | 0/1 | 1 | |\n",
            )
            errors = [issue.error for issue in validate_registry(ledger)]
            self.assertTrue(any("registry status" in error for error in errors))
            self.assertTrue(any("registry units" in error for error in errors))

    def test_registry_cannot_claim_complete_while_units_are_open(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp)
            source = ledger / "book"
            write(source / "SOURCE.md", source_text("book", added="2026-08-14", status="in-progress", contract=False))
            write(source / "UNITS.md", units_text("in-progress"))
            write(
                ledger / "REGISTRY.md",
                "| source_id | title | author | sha256 (first 12) | status | units | objects | closed |\n"
                "|---|---|---|---|---|---|---|---|\n"
                "| book | Book | Author | abcdef123456 | complete | 0/1 | 1 | 2026-08-15 |\n",
            )
            errors = [issue.error for issue in validate_registry(ledger)]
            self.assertTrue(any("registry status" in error for error in errors))

    def test_authoritative_source_requires_registry_representation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp)
            source = ledger / "book"
            write(source / "SOURCE.md", source_text("book", added="2026-08-14", status="queued", contract=False))
            write(
                ledger / "REGISTRY.md",
                "| source_id | title | author | sha256 (first 12) | status | units | objects | closed |\n"
                "|---|---|---|---|---|---|---|---|\n",
            )
            errors = [issue.error for issue in validate_registry(ledger)]
            self.assertTrue(any("has no registry row" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

"""Public provenance records — the bridge between a private ledger and a public repo.

PASS keeps two levels of state:

* **Private authoring state** (`workspace/authoring/`) holds the books, the render
  cache, and the ledger: REGISTRY, SOURCE.md, UNITS.md, per-unit reading receipts,
  candidate dispositions, Teaching-lane receipts. That is the factory's notebook.
  It is what makes a run resumable and fail-closed, and it is not published.
* **Public provenance** (`workspace/provenance/<source_id>.json`) holds a compact,
  content-addressed receipt derived from that ledger. It proves the shipped library
  has not drifted from the grounding that was accepted, without publishing the
  record that produced it.

The receipt is a superset of the quality attestation rather than a second format,
so there is exactly one authority on a source's accepted state. Beyond the
attestation fields it carries the three ledger facts the *library* checks need:

* ``processed_units`` — rule 13, a card's locator must name a processed unit;
* ``visual`` — whether the source's grounding is image-based;
* ``rights`` — whether a reviewed source image may ship as a first-party reference.

``ledger_tree_sha256`` is what makes the omission safe: the public receipt names
the exact private authoring record that was approved, so the ledger can be produced
later and checked against what was published.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

PROVENANCE_DIRNAME = "provenance"
RECORD_SUFFIX = ".json"


def provenance_root_for(ledger_root: Path) -> Path:
    """Public provenance lives beside the authoring workspace, not inside it.

    ``workspace/authoring/ledger`` -> ``workspace/provenance``
    """
    return ledger_root.parent.parent / PROVENANCE_DIRNAME


def record_path(provenance_root: Path, source_id: str) -> Path:
    return provenance_root / f"{source_id}{RECORD_SUFFIX}"


def load_record(provenance_root: Path, source_id: str) -> dict[str, Any] | None:
    path = record_path(provenance_root, source_id)
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def load_all(provenance_root: Path) -> dict[str, dict[str, Any]]:
    if not provenance_root.is_dir():
        return {}
    records: dict[str, dict[str, Any]] = {}
    for path in sorted(provenance_root.glob(f"*{RECORD_SUFFIX}")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and data.get("source_id"):
            records[str(data["source_id"])] = data
    return records


def ledger_is_available(ledger_root: Path) -> bool:
    """True when the private authoring ledger is present in this checkout."""
    return ledger_root.is_dir() and any(ledger_root.glob("*/SOURCE.md"))


def unit_statuses_from_ledger(ledger_root: Path, source_id: str) -> dict[str, str]:
    units_path = ledger_root / source_id / "UNITS.md"
    if not units_path.is_file():
        return {}
    # Mirrors validate.py's original parser exactly. Unit ids are not always
    # `uNN` — art ledgers use forms like `ch06` — so this filters the header and
    # separator rows rather than pattern-matching the id.
    statuses: dict[str, str] = {}
    for line in units_path.read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) >= 5 and cells[1] not in {"unit_id", "---", ""}:
            statuses[cells[1]] = cells[4]
    return statuses


def source_flag_from_ledger(ledger_root: Path, source_id: str, pattern: str) -> bool:
    source = ledger_root / source_id / "SOURCE.md"
    if not source.is_file():
        return False
    return bool(re.search(pattern, source.read_text(encoding="utf-8")))


VISUAL_PATTERN = r"(?mi)^visual:\s*(true|yes|1)\s*$"
FIRST_PARTY_PATTERN = r"(?mi)^rights:\s*first_party\s*$"


def build_public_fields(ledger_root: Path, source_id: str) -> dict[str, Any]:
    """The ledger facts a public checkout still needs for library validation."""
    statuses = unit_statuses_from_ledger(ledger_root, source_id)
    return {
        "processed_units": sorted(
            unit_id for unit_id, status in statuses.items() if status == "processed"
        ),
        "unit_count": len(statuses),
        "visual": source_flag_from_ledger(ledger_root, source_id, VISUAL_PATTERN),
        "rights_first_party": source_flag_from_ledger(
            ledger_root, source_id, FIRST_PARTY_PATTERN
        ),
    }


class ProvenanceView:
    """Answers the library-validation questions from whichever state exists.

    With a ledger present this reads the ledger, so authoring runs see live state
    the moment a unit is marked processed. Without one it reads the published
    receipts, so a public checkout validates against what was accepted. The caller
    does not need to know which.
    """

    def __init__(self, ledger_root: Path, provenance_root: Path | None = None) -> None:
        self.ledger_root = ledger_root
        self.provenance_root = provenance_root or provenance_root_for(ledger_root)
        self.has_ledger = ledger_is_available(ledger_root)
        self._records = {} if self.has_ledger else load_all(self.provenance_root)

    @property
    def mode(self) -> str:
        return "authoring" if self.has_ledger else "public"

    def known_source_ids(self) -> set[str]:
        if self.has_ledger:
            return {path.parent.name for path in self.ledger_root.glob("*/SOURCE.md")}
        return set(self._records)

    def processed_units(self, source_id: str) -> set[str]:
        if self.has_ledger:
            statuses = unit_statuses_from_ledger(self.ledger_root, source_id)
            return {unit for unit, status in statuses.items() if status == "processed"}
        record = self._records.get(source_id)
        if not record:
            return set()
        return {str(unit) for unit in record.get("processed_units") or []}

    def is_visual(self, source_id: str) -> bool:
        if self.has_ledger:
            return source_flag_from_ledger(self.ledger_root, source_id, VISUAL_PATTERN)
        record = self._records.get(source_id)
        return bool(record and record.get("visual"))

    def is_first_party(self, source_id: str) -> bool:
        if self.has_ledger:
            return source_flag_from_ledger(
                self.ledger_root, source_id, FIRST_PARTY_PATTERN
            )
        record = self._records.get(source_id)
        return bool(record and record.get("rights_first_party"))

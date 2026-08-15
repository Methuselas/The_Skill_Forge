#!/usr/bin/env python3
"""Validate PASS library objects against docs/PASS_SCHEMA.md."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from paths import default_library_root, default_ledger_root
from source_provenance import card_source_ids


STAGE_VALUES = {"0 design", "1 skeleton", "2 block", "3 rough", "4 final"}
LANE_VALUES = {"teach", "skill", "both", "teaching_foundation"}
FOUNDATION_VALUES = {"foundation", "specialization"}
ROUTING_VALUES = {"general", "specialized", "teaching"}
AXIS_VALUES = {
    "none", "language", "tool", "framework", "medium", "style", "genre",
    "tradition", "source", "method", "domain",
}
OBJECT_TYPES = {"pattern", "drill", "ap"}
CONFIDENCE_VALUES = {"low", "medium", "high"}
EVIDENCE_VALUES = {"text", "image", "mixed"}
REL_VALUES = {
    "foundation_of", "variant_of", "prerequisite_for", "supports", "related_to",
    "teaches", "skill_pair", "teaching_foundation_for",
}
COMMON_KEYS = {
    "object_id", "object_type", "name", "library_path", "stage_binding", "lane_fit",
    "foundation_role", "routing_class", "specialization_axis", "foundation_object_id",
    "tags", "cross_links", "reference", "confidence", "references", "variants",
}
REFERENCE_KEYS = {
    "source_id", "source_title", "author", "publish_date", "media_type", "locator",
    "evidence_type",
}
VISUAL_REFERENCE_KEYS = {"image_path", "caption", "derived_from", "origin", "review"}
HEADINGS = {
    "pattern": ["Pattern Rule", "Do", "Don't", "Checklist", "Notes"],
    "drill": ["Practice Task", "Target Skill", "Setup", "Instructions", "Success Check", "Common Failures", "Notes"],
    "ap": ["Objective", "Steps / Flow", "Notes"],
}
SOURCE_DEPENDENT_PHRASES = (
    "see page", "as shown above", "as shown in the diagram", "study the figure",
    "repeat the exercise from the source", "use the pictured", "refer to the illustration",
)
PATH_SEGMENT_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
PLACEHOLDER_RE = re.compile(r"<[^>\n]+>")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+|\n+(?=- )")
SIMILARITY_THRESHOLD = 0.70
DUPLICATE_THRESHOLD = 3
LEDGER_V2_COLUMNS = [
    "candidate", "type", "disposition", "object_id", "grounding",
    "learner_decision", "variant_basis", "method_or_policy", "tradeoff", "note",
]
LEDGER_V3_COLUMNS = [
    "candidate", "type", "lane", "teaching_scope", "teaching_route",
    "disposition", "object_id", "grounding", "learner_decision",
    "variant_basis", "method_or_policy", "tradeoff", "note",
]
DISPOSITIONS = {"new", "variant", "replace", "reject"}
LANE_REVIEW_VALUES = {"skill", "teach", "both"}
TEACHING_SCOPE_VALUES = {"domain-specific", "cross-domain"}
TEACHING_LANE_CONTRACT_DATE = date(2026, 8, 15)
CLOSED_UNIT_STATUSES = {"processed", "empty", "blocked"}
VARIANT_KEYS = {
    "variant_id", "variant_name", "variant_basis", "source_id", "source_title", "locator",
    "difference_from_foundation", "when_to_use", "when_not_to_use", "absorbed_from_object_id",
}
VARIANT_BASIS_VALUES = {"method_sequence", "emphasis", "medium", "style", "source", "constraint", "context"}


@dataclass
class ObjectRecord:
    path: Path
    relative_path: Path
    data: dict[str, Any]
    body: str
    sections: dict[str, str]
    errors: list[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        return self.relative_path.as_posix()


@dataclass
class LedgerIssue:
    path: Path
    error: str

    @property
    def label(self) -> str:
        return self.path.as_posix()


def parse_object(path: Path, library_root: Path) -> ObjectRecord:
    raw = path.read_text(encoding="utf-8")
    relative = path.relative_to(library_root)
    errors: list[str] = []
    if not raw.startswith("---"):
        return ObjectRecord(path, relative, {}, raw, {}, ["rule 1: file does not begin at byte 0 with ---"])
    match = re.match(r"\A---\r?\n(?P<front>.*?)\r?\n---\r?\n(?P<body>.*)\Z", raw, re.DOTALL)
    if not match:
        return ObjectRecord(path, relative, {}, raw, {}, ["rule 1: frontmatter is missing or malformed"])
    if match.group("body").count("\n---\n") or match.group("body").count("\n---\r\n"):
        errors.append("rule 1: more than one frontmatter block")
    try:
        data = yaml.safe_load(match.group("front"))
    except yaml.YAMLError as exc:
        return ObjectRecord(path, relative, {}, match.group("body"), {}, [f"rule 1: YAML parse error: {exc}"])
    if not isinstance(data, dict):
        return ObjectRecord(path, relative, {}, match.group("body"), {}, ["rule 2: frontmatter must be a mapping"])
    sections = extract_sections(match.group("body"))
    return ObjectRecord(path, relative, data, match.group("body"), sections, errors)


def extract_sections(body: str) -> dict[str, str]:
    headings = list(re.finditer(r"(?m)^## ([^\r\n]+)\s*$", body))
    result: dict[str, str] = {}
    for index, heading in enumerate(headings):
        start = heading.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        result[heading.group(1)] = body[start:end].strip()
    return result


def first_heading(body: str) -> str | None:
    match = re.search(r"(?m)^# ([^\r\n]+)\s*$", body)
    return match.group(1) if match else None


def bullet_items(text: str) -> list[str]:
    return [match.group(1).strip() for match in re.finditer(r"(?m)^\s*-\s+(.+?)\s*$", text)]


def normalize_sentence(text: str, record: ObjectRecord) -> str:
    text = text.lower()
    text = re.sub(r"^[-*\d.\s]+", "", text)
    text = text.replace(record.data.get("name", "").lower(), "")
    for marker in ("IF", "THEN"):
        match = re.search(rf"(?m)^\*\*{marker}\*\*\s*(.+)$", record.sections.get("Pattern Rule", ""))
        if match:
            text = text.replace(match.group(1).lower(), "")
    return re.sub(r"\s+", " ", text).strip(" .;:-")


def words(text: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9_+]+", text.lower()) if len(word) > 2}


def jaccard(left: str, right: str) -> float:
    left_words, right_words = words(left), words(right)
    if not left_words or not right_words:
        return 0.0
    return len(left_words & right_words) / len(left_words | right_words)


def unit_statuses(ledger_root: Path, source_id: str) -> dict[str, str]:
    units_path = ledger_root / source_id / "UNITS.md"
    if not units_path.exists():
        return {}
    result: dict[str, str] = {}
    for line in units_path.read_text(encoding="utf-8").splitlines():
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) >= 5 and cells[1] not in {"unit_id", "---", ""}:
            result[cells[1]] = cells[4]
    return result


def source_is_visual(ledger_root: Path, source_id: str) -> bool:
    source = ledger_root / source_id / "SOURCE.md"
    if not source.exists():
        return False
    return bool(re.search(r"(?mi)^visual:\s*(true|yes|1)\s*$", source.read_text(encoding="utf-8")))


def source_is_first_party(ledger_root: Path, source_id: str) -> bool:
    source = ledger_root / source_id / "SOURCE.md"
    if not source.exists():
        return False
    return bool(re.search(r"(?mi)^rights:\s*first_party\s*$", source.read_text(encoding="utf-8")))


def is_text_only_metaskill(record: ObjectRecord) -> bool:
    data = record.data
    return (
        data.get("object_type") == "ap"
        and isinstance(data.get("library_path"), list)
        and data["library_path"][:1] == ["metaskills"]
        and data.get("routing_class") == "general"
        and data.get("specialization_axis") == "none"
    )


def validate_visual_references(record: ObjectRecord, library_root: Path, ledger_root: Path) -> None:
    data = record.data
    references = data.get("references")
    if not isinstance(references, list):
        record.errors.append("rule 23: references must be a list")
        return
    # A card from a visual source MAY ship as a text extraction with references: [].
    # The former mandatory-reference clause was retired on 2026-08-01 when generated
    # teaching references were removed from the corpus; first-party references are
    # used when one genuinely illustrates the card, not manufactured to satisfy a
    # gate. References that ARE present are still fully validated below.
    source_id = data.get("reference", {}).get("source_id") if isinstance(data.get("reference"), dict) else None
    for item in references:
        if not isinstance(item, dict) or set(item) != VISUAL_REFERENCE_KEYS:
            record.errors.append("rule 23: reference item has missing or extra fields")
            continue
        origin = item.get("origin")
        if origin not in {"generated", "first_party_source"}:
            record.errors.append("rule 23: reference origin must be generated or first_party_source")
        elif origin == "first_party_source" and not source_is_first_party(ledger_root, str(source_id)):
            record.errors.append("rule 23: first_party_source requires SOURCE.md rights: first_party")
        if item.get("review") != "passed":
            record.errors.append("rule 23: reference review must be passed to ship")
        image_path = item.get("image_path")
        if not isinstance(image_path, str):
            record.errors.append("rule 23: reference image_path must be a repo-relative string")
            continue
        image = library_root.parent / image_path
        try:
            image.relative_to(record.path.parent)
        except ValueError:
            record.errors.append("rule 23: reference image_path must sit under the card topic folder")
            continue
        if not image.is_file():
            record.errors.append("rule 23: reference image_path does not exist")


def table_cells(line: str) -> list[str]:
    cells = [cell.strip() for cell in line.split("|")]
    if cells and not cells[0]:
        cells = cells[1:]
    if cells and not cells[-1]:
        cells = cells[:-1]
    return cells


def scalar_field(raw: str, key: str) -> str | None:
    match = re.search(rf"(?mi)^{re.escape(key)}:\s*(.*?)\s*$", raw)
    if not match:
        return None
    return match.group(1).strip().strip('"').strip("'")


def comma_values(value: str | None) -> set[str]:
    if not value or value.casefold() in {"none", "[]"}:
        return set()
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1]
    return {item.strip().strip('"').strip("'") for item in value.split(",") if item.strip()}


def markdown_table(raw: str, first_column: str) -> tuple[list[str], list[dict[str, str]]]:
    lines = raw.splitlines()
    header_index = next(
        (
            index for index, line in enumerate(lines)
            if table_cells(line) and table_cells(line)[0] == first_column
        ),
        None,
    )
    if header_index is None:
        return [], []
    columns = table_cells(lines[header_index])
    rows: list[dict[str, str]] = []
    for line in lines[header_index + 2:]:
        if not line.startswith("|"):
            break
        cells = table_cells(line)
        if len(cells) == len(columns):
            rows.append(dict(zip(columns, cells)))
    return columns, rows


def unit_queue(units_path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not units_path.is_file():
        return [], []
    return markdown_table(units_path.read_text(encoding="utf-8"), "unit_id")


def source_contract_requirements(ledger_root: Path) -> tuple[set[Path], list[LedgerIssue]]:
    required_v3: set[Path] = set()
    issues: list[LedgerIssue] = []
    for source_dir in sorted(path for path in ledger_root.iterdir() if path.is_dir()):
        source_path = source_dir / "SOURCE.md"
        if not source_path.is_file():
            continue
        raw = source_path.read_text(encoding="utf-8")
        contract = scalar_field(raw, "unit_ledger_contract")
        source_status = scalar_field(raw, "status")
        added_value = scalar_field(raw, "added")
        try:
            added = date.fromisoformat(added_value) if added_value else None
        except ValueError:
            issues.append(LedgerIssue(source_path, "rule 24: added must be an ISO date"))
            added = None
        if added and added >= TEACHING_LANE_CONTRACT_DATE and contract != "3":
            issues.append(
                LedgerIssue(
                    source_path,
                    "rule 24: sources admitted on or after 2026-08-15 require unit_ledger_contract: 3",
                )
            )
        if source_status in {"queued", "in-progress"} and contract != "3":
            issues.append(
                LedgerIssue(
                    source_path,
                    "rule 24: active sources require unit_ledger_contract: 3 before another unit can close",
                )
            )
        if contract not in {None, "3"}:
            issues.append(LedgerIssue(source_path, "rule 24: unit_ledger_contract must be 3 when present"))
        if contract != "3":
            continue

        grandfathered = comma_values(scalar_field(raw, "teaching_lane_grandfathered_units"))
        units_path = source_dir / "UNITS.md"
        _columns, units = unit_queue(units_path)
        known_units = {row.get("unit_id", "") for row in units}
        for unit_id in sorted(grandfathered - known_units):
            issues.append(LedgerIssue(source_path, f"rule 24: unknown grandfathered unit {unit_id}"))
        for row in units:
            unit_id = row.get("unit_id", "")
            status = row.get("status", "")
            if unit_id in grandfathered and status not in CLOSED_UNIT_STATUSES:
                issues.append(
                    LedgerIssue(source_path, f"rule 24: grandfathered unit {unit_id} is not historically closed")
                )
            if status in CLOSED_UNIT_STATUSES and unit_id not in grandfathered:
                unit_path = source_dir / "units" / f"{unit_id}.md"
                if not unit_path.is_file():
                    issues.append(
                        LedgerIssue(unit_path, "rule 24: closed contract-v3 unit is missing its unit ledger")
                    )
                else:
                    required_v3.add(unit_path)
    return required_v3, issues


def validate_ledgers(
    ledger_root: Path,
    object_packages: dict[str, str] | None = None,
) -> list[LedgerIssue]:
    issues: list[LedgerIssue] = []
    required_v3, contract_issues = source_contract_requirements(ledger_root)
    issues.extend(contract_issues)
    for path in sorted(ledger_root.glob("*/units/*.md")):
        raw = path.read_text(encoding="utf-8")
        format_match = re.search(r"(?m)^ledger_format:\s*(\d+)\s*$", raw)
        ledger_format = int(format_match.group(1)) if format_match else None
        read_value = scalar_field(raw, "read")
        try:
            read_date = date.fromisoformat(read_value) if read_value else None
        except ValueError:
            issues.append(LedgerIssue(path, "rule 24: read must be an ISO date"))
            read_date = None
        if read_date and read_date >= TEACHING_LANE_CONTRACT_DATE:
            required_v3.add(path)
        if path in required_v3 and ledger_format != 3:
            issues.append(
                LedgerIssue(path, "rule 24: newly processed unit requires ledger_format: 3 Teaching-lane receipt")
            )
        if ledger_format not in {2, 3}:
            continue
        count_match = re.search(r"(?m)^candidate_count:\s*(\d+)\s*$", raw)
        if not count_match:
            issues.append(LedgerIssue(path, f"rule 21: ledger v{ledger_format} requires candidate_count"))
            continue
        columns, rows = markdown_table(raw, "candidate")
        expected_columns = LEDGER_V3_COLUMNS if ledger_format == 3 else LEDGER_V2_COLUMNS
        if columns != expected_columns:
            issues.append(LedgerIssue(path, f"rule 21: ledger v{ledger_format} candidate table has invalid columns"))
            continue
        if int(count_match.group(1)) != len(rows):
            issues.append(LedgerIssue(path, "rule 21: candidate_count does not match disposition rows"))
        if ledger_format == 3:
            if scalar_field(raw, "teaching_lane_review") != "complete":
                issues.append(LedgerIssue(path, "rule 24: ledger v3 requires teaching_lane_review: complete"))
            teaching_count_match = re.search(r"(?m)^teaching_candidate_count:\s*(\d+)\s*$", raw)
            if not teaching_count_match:
                issues.append(LedgerIssue(path, "rule 24: ledger v3 requires teaching_candidate_count"))
            else:
                actual_teaching = sum(row.get("lane") in {"teach", "both"} for row in rows)
                if int(teaching_count_match.group(1)) != actual_teaching:
                    issues.append(
                        LedgerIssue(path, "rule 24: teaching_candidate_count does not match teach/both rows")
                    )
        for row in rows:
            if row["disposition"] not in DISPOSITIONS:
                issues.append(LedgerIssue(path, "rule 21: candidate row has an invalid disposition"))
                continue
            if row["disposition"] == "variant":
                required = ("object_id", "learner_decision", "variant_basis", "method_or_policy", "tradeoff")
                if any(not row[key] for key in required):
                    issues.append(LedgerIssue(path, "rule 22: variant row requires foundation, decision, basis, method, and tradeoff"))
            if ledger_format != 3:
                continue
            lane = row["lane"]
            scope = row["teaching_scope"]
            route = row["teaching_route"]
            if lane not in LANE_REVIEW_VALUES:
                issues.append(LedgerIssue(path, "rule 24: candidate lane must be skill, teach, or both"))
                continue
            if lane == "skill":
                if scope not in {"—", "-", "none"} or route not in {"—", "-", "none"}:
                    issues.append(LedgerIssue(path, "rule 24: skill-only candidate cannot claim a Teaching scope or route"))
                continue
            if scope not in TEACHING_SCOPE_VALUES:
                issues.append(LedgerIssue(path, "rule 24: teach/both candidate requires a Teaching scope"))
                continue
            object_id = row["object_id"]
            package = (object_packages or {}).get(object_id)
            if scope == "domain-specific":
                if route != "domain":
                    issues.append(LedgerIssue(path, "rule 24: domain-specific teaching candidate routes to domain"))
                if package == "teaching":
                    issues.append(LedgerIssue(path, "rule 24: domain-specific teaching candidate cannot be owned by Teaching"))
            else:
                if not route.startswith("teaching:") or not route.removeprefix("teaching:").strip():
                    issues.append(LedgerIssue(path, "rule 24: cross-domain teaching candidate requires teaching:<owner> route"))
                    continue
                owner_id = route.removeprefix("teaching:").strip()
                owner_package = (object_packages or {}).get(owner_id)
                if object_packages is not None and owner_package != "teaching":
                    issues.append(LedgerIssue(path, "rule 24: cross-domain Teaching route must resolve in top-level teaching"))
                if row["disposition"] in {"new", "variant", "replace"} and object_id != owner_id:
                    issues.append(LedgerIssue(path, "rule 24: retained cross-domain candidate must target its Teaching owner"))
    return issues


def validate_registry(ledger_root: Path) -> list[LedgerIssue]:
    issues: list[LedgerIssue] = []
    registry_path = ledger_root / "REGISTRY.md"
    if not registry_path.is_file():
        return [LedgerIssue(registry_path, "rule 25: source registry is missing")]
    registry_raw = registry_path.read_text(encoding="utf-8")
    lines = registry_raw.splitlines()
    header_index = next(
        (
            index for index, line in enumerate(lines)
            if table_cells(line) and table_cells(line)[0] == "source_id"
        ),
        None,
    )
    if header_index is None:
        return [LedgerIssue(registry_path, "rule 25: registry table is missing")]
    columns = table_cells(lines[header_index])
    expected_columns = ["source_id", "title", "author", "sha256 (first 12)", "status", "units", "objects", "closed"]
    if columns != expected_columns:
        return [LedgerIssue(registry_path, "rule 25: registry table has invalid columns")]
    rows: list[dict[str, str]] = []
    for line in lines[header_index + 2:]:
        if not line.startswith("|"):
            continue
        cells = table_cells(line)
        if len(cells) == len(columns) and cells[0] not in {"source_id", "---", ""}:
            rows.append(dict(zip(columns, cells)))
    by_id: dict[str, dict[str, str]] = {}
    for row in rows:
        source_id = row["source_id"]
        if source_id in by_id:
            issues.append(LedgerIssue(registry_path, f"rule 25: duplicate registry row for {source_id}"))
        by_id[source_id] = row

    source_dirs: dict[str, Path] = {}
    for source_path in sorted(ledger_root.glob("*/SOURCE.md")):
        raw = source_path.read_text(encoding="utf-8")
        source_id = scalar_field(raw, "source_id")
        if not source_id:
            issues.append(LedgerIssue(source_path, "rule 25: SOURCE.md lacks source_id"))
            continue
        source_dirs[source_id] = source_path.parent
        if source_id not in by_id:
            issues.append(LedgerIssue(source_path, f"rule 25: authoritative source {source_id} has no registry row"))

    for source_id, row in sorted(by_id.items()):
        source_dir = source_dirs.get(source_id)
        if source_dir is None:
            issues.append(LedgerIssue(registry_path, f"rule 25: registry row {source_id} has no SOURCE.md"))
            continue
        source_path = source_dir / "SOURCE.md"
        source_raw = source_path.read_text(encoding="utf-8")
        source_status = scalar_field(source_raw, "status") or ""
        units_path = source_dir / "UNITS.md"
        _unit_columns, units = unit_queue(units_path)
        if not units_path.is_file() and source_status != "queued":
            issues.append(LedgerIssue(units_path, f"rule 25: {source_id} has no UNITS.md"))
            continue
        statuses = [unit.get("status", "") for unit in units]
        invalid = sorted(set(statuses) - {"queued", "in-progress", *CLOSED_UNIT_STATUSES})
        if invalid:
            issues.append(LedgerIssue(units_path, f"rule 25: invalid unit statuses: {', '.join(invalid)}"))
            continue
        done = sum(status in CLOSED_UNIT_STATUSES for status in statuses)
        total = len(statuses)
        if source_status in {"abandoned", "low-yield"}:
            computed_status = source_status
        elif not statuses or all(status == "queued" for status in statuses):
            computed_status = "queued"
        elif all(status in CLOSED_UNIT_STATUSES for status in statuses):
            computed_status = "complete"
        else:
            computed_status = "in-progress"
        if source_status != computed_status:
            issues.append(
                LedgerIssue(
                    source_path,
                    f"rule 25: SOURCE status {source_status or '<missing>'} != computed unit status {computed_status}",
                )
            )
        if row["status"] != computed_status:
            issues.append(
                LedgerIssue(
                    registry_path,
                    f"rule 25: registry status for {source_id} is {row['status']} != {computed_status}",
                )
            )
        expected_count = f"{done}/{total}" if total else ""
        if row["units"] != expected_count:
            issues.append(
                LedgerIssue(
                    registry_path,
                    f"rule 25: registry units for {source_id} are {row['units'] or '<blank>'} != {expected_count or '<blank>'}",
                )
            )
    return issues


def validate_record(record: ObjectRecord, library_root: Path, ledger_root: Path) -> None:
    data = record.data
    if not data:
        return
    object_type = data.get("object_type")
    expected_keys = COMMON_KEYS | ({"target_skill"} if object_type == "drill" else set())
    missing = sorted(expected_keys - set(data))
    extra = sorted(set(data) - expected_keys)
    if missing:
        record.errors.append(f"rule 2: missing keys: {', '.join(missing)}")
    if extra:
        record.errors.append(f"rule 2: extra or renamed keys: {', '.join(extra)}")
    if any(key in data for key in ("id", "type", "source_id")) or any("guard" in key.lower() for key in data):
        record.errors.append("rule 2: forbidden renamed or guard key")
    reference = data.get("reference")
    if not isinstance(reference, dict) or set(reference) != REFERENCE_KEYS:
        record.errors.append("rule 3: reference must contain exactly the seven required keys")
    if object_type not in OBJECT_TYPES:
        record.errors.append("rule 4: object_type is invalid")
    for key, allowed in {
        "stage_binding": STAGE_VALUES,
        "lane_fit": LANE_VALUES,
        "foundation_role": FOUNDATION_VALUES,
        "routing_class": ROUTING_VALUES,
        "specialization_axis": AXIS_VALUES,
        "confidence": CONFIDENCE_VALUES,
    }.items():
        if data.get(key) not in allowed:
            record.errors.append(f"rule 4: {key} is invalid")
    if isinstance(reference, dict) and reference.get("evidence_type") not in EVIDENCE_VALUES:
        record.errors.append("rule 4: reference.evidence_type is invalid")
    if data.get("routing_class") == "general" and data.get("specialization_axis") != "none":
        record.errors.append("rule 5: general routing requires specialization_axis none")
    if data.get("routing_class") == "specialized" and data.get("specialization_axis") == "none":
        record.errors.append("rule 5: specialized routing requires a specialization axis")
    library_path = data.get("library_path")
    if not isinstance(library_path, list) or len(library_path) < 2 or not all(isinstance(part, str) and PATH_SEGMENT_RE.fullmatch(part) for part in library_path):
        record.errors.append("rule 4: library_path must contain at least two lowercase path segments")
    elif list(record.relative_path.parts[:-1]) != library_path:
        record.errors.append("rule 4: library_path does not match the object's directory")
    actual_headings = [match.group(1) for match in re.finditer(r"(?m)^## ([^\r\n]+)\s*$", record.body)]
    if object_type in HEADINGS and actual_headings != HEADINGS[object_type]:
        record.errors.append(f"rule 6: body headings must be exactly {HEADINGS[object_type]}")
    if any("guard" in heading.lower() for heading in actual_headings):
        record.errors.append("rule 6: body headings may not contain Guard")
    if first_heading(record.body) != data.get("name"):
        record.errors.append("rule 7: H1 must match name exactly")
    if PLACEHOLDER_RE.search(record.body) or PLACEHOLDER_RE.search(yaml.safe_dump(data)):
        record.errors.append("rule 8: unreplaced angle-bracket token")
    if re.search(r"\bprovisional\b", record.body, re.IGNORECASE) or re.search(r"\bprovisional\b", yaml.safe_dump(data), re.IGNORECASE):
        record.errors.append("rule 8: provisional is not valid")
    for key, value in data.items():
        if key != "reference" and "Unknown" in yaml.safe_dump(value):
            record.errors.append("rule 8: Unknown is only allowed in reference author or publish_date")
            break
    filename_prefix = {"pattern": "PAT_", "drill": "DRILL_", "ap": "AP_"}.get(object_type, "")
    if not filename_prefix or not record.path.name.startswith(filename_prefix) or not re.fullmatch(r"(?:PAT|DRILL|AP)_[a-z0-9][a-z0-9_]*\.md", record.path.name):
        record.errors.append("rule 9: filename has an invalid type prefix or slug")
    if re.fullmatch(r"(?:PAT|DRILL|AP)_?\d+\.md", record.path.name, re.IGNORECASE):
        record.errors.append("rule 9: filename may not be ID-only")
    name_words = re.findall(r"[A-Za-z]+", str(data.get("name", "")))
    if len(name_words) < 2 or re.fullmatch(r"[A-Za-z_\d-]+", str(data.get("name", ""))) and re.search(r"(?:pattern|drill|ap)_?\d+", str(data.get("name", "")), re.IGNORECASE):
        record.errors.append("rule 10: name is numeric or ID-like")
    if not isinstance(data.get("tags"), list) or not isinstance(data.get("cross_links"), list) or not isinstance(data.get("variants"), list):
        record.errors.append("rule 2: tags, cross_links, and variants must be lists")
    if isinstance(data.get("cross_links"), list):
        for link in data["cross_links"]:
            if not isinstance(link, dict) or set(link) != {"rel", "target_object_id"} or link.get("rel") not in REL_VALUES:
                record.errors.append("rule 11: cross_link is malformed or has an invalid relation")
                break
    if isinstance(reference, dict):
        source_id = reference.get("source_id")
        locator = str(reference.get("locator", ""))
        statuses = unit_statuses(ledger_root, str(source_id))
        unit_id = locator.split(",", 1)[0].strip()
        if not statuses or statuses.get(unit_id) != "processed":
            record.errors.append("rule 13: locator does not name a processed source unit")
    validate_visual_references(record, library_root, ledger_root)
    if data.get("variants"):
        notes = record.sections.get("Notes", "")
        for variant in data["variants"]:
            if not isinstance(variant, dict) or set(variant) != VARIANT_KEYS or variant.get("variant_basis") not in VARIANT_BASIS_VALUES:
                record.errors.append("rule 14: variant has missing, extra, or invalid fields")
                break
            if not variant.get("variant_id") or variant["variant_id"] not in notes:
                record.errors.append("rule 14: every variant_id must be mentioned in Notes")
                break
    body_without_h1 = re.sub(r"(?m)^# [^\r\n]+\r?\n?", "", record.body, count=1)
    if data.get("name") and str(data["name"]).lower() in body_without_h1.lower():
        record.errors.append("rule 19: full object name appears in body outside H1")
    lowered = record.body.lower()
    for phrase in SOURCE_DEPENDENT_PHRASES:
        if phrase in lowered:
            record.errors.append(f"rule 20: source-dependent phrase '{phrase}'")
            break
    items: list[str] = []
    for section in record.sections.values():
        items.extend(bullet_items(section))
    duplicates = [item for item, count in Counter(item.lower() for item in items).items() if count > 1]
    if duplicates:
        record.errors.append("rule 18: duplicate list item within object")


def validate_cross_object(records: list[ObjectRecord]) -> None:
    by_id: dict[str, list[ObjectRecord]] = defaultdict(list)
    for record in records:
        object_id = record.data.get("object_id")
        if object_id:
            by_id[str(object_id)].append(record)
    for object_id, duplicates in by_id.items():
        if len(duplicates) > 1:
            for record in duplicates:
                record.errors.append(f"rule 12: duplicate object_id {object_id}")
    known_ids = set(by_id)
    for record in records:
        for link in record.data.get("cross_links", []):
            if isinstance(link, dict) and link.get("target_object_id") not in known_ids:
                record.errors.append(f"rule 11: unresolved cross_link target {link.get('target_object_id')}")
    sentence_uses: dict[str, list[ObjectRecord]] = defaultdict(list)
    if_uses: dict[str, list[ObjectRecord]] = defaultdict(list)
    else_uses: dict[str, list[ObjectRecord]] = defaultdict(list)
    for record in records:
        for heading in ("Do", "Don't", "Checklist", "Notes"):
            for sentence in SENTENCE_RE.split(record.sections.get(heading, "")):
                normalized = normalize_sentence(sentence, record)
                if normalized:
                    sentence_uses[normalized].append(record)
        rule = record.sections.get("Pattern Rule", "")
        if_match = re.search(r"(?m)^\*\*IF\*\*\s*(.+)$", rule)
        else_match = re.search(r"(?m)^\*\*ELSE\*\*\s*(.+)$", rule)
        if if_match:
            if_uses[normalize_sentence(if_match.group(1), record)].append(record)
        if else_match:
            else_uses[normalize_sentence(else_match.group(1), record)].append(record)
        then_match = re.search(r"(?m)^\*\*THEN\*\*\s*(.+)$", rule)
        if then_match:
            do_items = bullet_items(record.sections.get("Do", ""))
            if do_items and jaccard(then_match.group(1), do_items[0]) >= SIMILARITY_THRESHOLD:
                record.errors.append("rule 17: first Do item recycles the THEN clause")
            notes = record.sections.get("Notes", "")
            opening = SENTENCE_RE.split(notes)[0] if notes else ""
            if opening and jaccard(then_match.group(1), opening) >= SIMILARITY_THRESHOLD:
                record.errors.append("rule 17: Notes opens by recycling the THEN clause")
    for label, uses, rule_number in (("sentence", sentence_uses, 15), ("IF", if_uses, 16), ("ELSE", else_uses, 16)):
        for text, owners in uses.items():
            unique_owners = list({owner.path: owner for owner in owners}.values())
            if text and len(unique_owners) > DUPLICATE_THRESHOLD:
                for owner in unique_owners:
                    owner.errors.append(f"rule {rule_number}: shared {label} appears in more than {DUPLICATE_THRESHOLD} objects")


def discover_objects(library_root: Path) -> list[Path]:
    return sorted(
        path for path in library_root.rglob("*.md")
        if path.name != "README.md"
        and path.name != "INDEX.md"
        and "memcap" not in path.relative_to(library_root).parts
    )


def validate_library(library_root: Path, ledger_root: Path) -> list[ObjectRecord]:
    records = [parse_object(path, library_root) for path in discover_objects(library_root)]
    for record in records:
        validate_record(record, library_root, ledger_root)
    validate_cross_object(records)
    return records


def object_package_index(records: list[ObjectRecord]) -> dict[str, str]:
    return {
        str(record.data["object_id"]): package_of(record)
        for record in records
        if record.data.get("object_id")
    }


def package_of(record: ObjectRecord) -> str:
    parts = record.relative_path.parts
    return parts[0] if parts else ""


def records_in_package(records: list[ObjectRecord], package: str) -> list[ObjectRecord]:
    return [record for record in records if package_of(record) == package]


def source_ids_of(records: list[ObjectRecord]) -> set[str]:
    source_ids: set[str] = set()
    for record in records:
        source_ids.update(card_source_ids(record.data))
    return source_ids


def ledger_issues_for_sources(issues: list[LedgerIssue], source_ids: set[str]) -> list[LedgerIssue]:
    def issue_source_id(issue: LedgerIssue) -> str:
        if issue.path.parent.name == "units":
            return issue.path.parent.parent.name
        if issue.path.name in {"SOURCE.md", "UNITS.md"}:
            return issue.path.parent.name
        return ""

    return [issue for issue in issues if issue_source_id(issue) in source_ids]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--library", type=Path, default=default_library_root())
    parser.add_argument("--ledger", type=Path, default=default_ledger_root())
    parser.add_argument(
        "--package",
        default=None,
        help=(
            "Report only objects in this package (e.g. software-engineering). "
            "The whole library is still loaded, so cross-links and cross-object "
            "checks resolve against every package; only the reported set narrows."
        ),
    )
    parser.add_argument(
        "--scope-ledger-to-library",
        action="store_true",
        help=(
            "Report ledger issues only for sources referenced by the supplied library. "
            "Use this when validating a materialized release closure."
        ),
    )
    args = parser.parse_args()
    records = validate_library(args.library, args.ledger)
    ledger_issues = validate_ledgers(args.ledger, object_package_index(records))
    if not args.package and not args.scope_ledger_to_library:
        ledger_issues.extend(validate_registry(args.ledger))
    scope = ""
    if args.package:
        reported = records_in_package(records, args.package)
        if not reported:
            print(f"No objects found in package '{args.package}' under {args.library.as_posix()}.")
            return 1
        ledger_issues = ledger_issues_for_sources(ledger_issues, source_ids_of(reported))
        scope = f" in package '{args.package}'"
    else:
        reported = records
        if args.scope_ledger_to_library:
            ledger_issues = ledger_issues_for_sources(ledger_issues, source_ids_of(reported))
    errors = 0
    for record in reported:
        for error in record.errors:
            print(f"{record.label}: {error}")
            errors += 1
    for issue in ledger_issues:
        print(f"{issue.label}: {issue.error}")
        errors += 1
    if errors:
        print(f"FAIL: {errors} issue(s) across {len(reported)} object(s){scope}")
        return 1
    print(f"PASS: {len(reported)} object(s) validated{scope}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate PASS library objects against docs/PASS_SCHEMA.md.

This checks finished knowledge objects and nothing else. It does not look for a
source document, a page, a reading receipt, or any record of the session that
produced a card: a Pattern, Drill, or AP must be valid after the book it was
learned from is gone. The only inputs are the library tree and the cards in it.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from paths import default_library_root


STAGE_VALUES = {"0 design", "1 skeleton", "2 block", "3 rough", "4 final"}
LANE_VALUES = {"teach", "skill", "both"}
FOUNDATION_VALUES = {"foundation", "specialization"}
ROUTING_VALUES = {"general", "specialized", "teaching"}
AXIS_VALUES = {
    "none", "language", "tool", "framework", "medium", "style", "genre",
    "tradition", "source", "method", "domain",
}
OBJECT_TYPES = {"pattern", "drill", "ap"}
CONFIDENCE_VALUES = {"low", "medium", "high"}
REL_VALUES = {
    "foundation_of", "variant_of", "prerequisite_for", "supports", "related_to",
    "teaches", "skill_pair",
}
COMMON_KEYS = {
    "object_id", "object_type", "name", "library_path", "stage_binding", "lane_fit",
    "foundation_role", "routing_class", "specialization_axis", "foundation_object_id",
    "tags", "cross_links", "reference", "confidence", "references", "variants",
}
# Optional courtesy attribution. It names a book, never a runtime dependency:
# nothing is resolved, fetched, or checked for existence from these values.
REFERENCE_KEYS = {"source_title", "author"}
# `reference` may be omitted entirely. A finished card must stay valid once the
# work it was learned from is gone (hard rule 1), so the line naming that work
# cannot be load-bearing -- requiring the key would make attribution a schema
# obligation rather than a courtesy. Present or absent, nothing reads it.
# See PASS_SCHEMA.md section 1.
OPTIONAL_KEYS = {"reference"}
VISUAL_REFERENCE_KEYS = {"image_path", "caption", "derived_from", "origin", "review"}
# Packages every domain may depend on. `metaskills` is a shared foundation rather
# than a peer domain: it holds craft-neutral process knowledge that every release
# bundles. Any other cross-package edge is a domain coupling and fails.
SHARED_PACKAGES = {"metaskills"}
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
VARIANT_KEYS = {
    "variant_id", "variant_name", "variant_basis",
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


def validate_visual_references(record: ObjectRecord, library_root: Path) -> None:
    data = record.data
    references = data.get("references")
    if not isinstance(references, list):
        record.errors.append("rule 23: references must be a list")
        return
    # A card MAY ship as a text extraction with references: []. A reference is
    # included when an image genuinely illustrates the card's move, never to
    # satisfy a gate. References that ARE present are fully validated below.
    for item in references:
        if not isinstance(item, dict) or set(item) != VISUAL_REFERENCE_KEYS:
            record.errors.append("rule 23: reference item has missing or extra fields")
            continue
        if item.get("origin") not in {"generated", "first_party_source"}:
            record.errors.append("rule 23: reference origin must be generated or first_party_source")
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


def validate_record(record: ObjectRecord, library_root: Path) -> None:
    data = record.data
    if not data:
        return
    object_type = data.get("object_type")
    expected_keys = COMMON_KEYS | ({"target_skill"} if object_type == "drill" else set())
    missing = sorted(expected_keys - OPTIONAL_KEYS - set(data))
    extra = sorted(set(data) - expected_keys)
    if missing:
        record.errors.append(f"rule 2: missing keys: {', '.join(missing)}")
    if extra:
        record.errors.append(f"rule 2: extra or renamed keys: {', '.join(extra)}")
    if any(key in data for key in ("id", "type", "source_id")) or any("guard" in key.lower() for key in data):
        record.errors.append("rule 2: forbidden renamed or guard key")
    reference = data.get("reference")
    if reference is not None and (not isinstance(reference, dict) or not set(reference) <= REFERENCE_KEYS):
        record.errors.append("rule 3: reference may contain only source_title and author")
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
    validate_visual_references(record, library_root)
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
    owner_package = {
        object_id: package_of(owners[0])
        for object_id, owners in by_id.items()
        if len(owners) == 1
    }
    for record in records:
        targets: list[tuple[str, str]] = []
        foundation = record.data.get("foundation_object_id")
        if foundation and foundation != "none":
            targets.append(("foundation_object_id", str(foundation)))
        for link in record.data.get("cross_links", []):
            if isinstance(link, dict) and link.get("target_object_id"):
                targets.append(("cross_link", str(link["target_object_id"])))
        for kind, target in targets:
            if target not in known_ids:
                record.errors.append(f"rule 11: unresolved {kind} target {target}")
                continue
            # Domain independence: an Art card may not require a Writing card.
            # Cards may depend freely inside their own package, plus the shared
            # metaskills foundation every release already bundles.
            target_package = owner_package.get(target)
            source_package = package_of(record)
            if target_package and target_package not in {source_package} | SHARED_PACKAGES:
                record.errors.append(
                    f"rule 26: {kind} {target} crosses from '{source_package}' into '{target_package}'"
                )
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
    )


def validate_library(library_root: Path) -> list[ObjectRecord]:
    records = [parse_object(path, library_root) for path in discover_objects(library_root)]
    for record in records:
        validate_record(record, library_root)
    validate_cross_object(records)
    return records


def package_of(record: ObjectRecord) -> str:
    parts = record.relative_path.parts
    return parts[0] if parts else ""


def records_in_package(records: list[ObjectRecord], package: str) -> list[ObjectRecord]:
    return [record for record in records if package_of(record) == package]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--library", type=Path, default=default_library_root())
    parser.add_argument(
        "--package",
        default=None,
        help=(
            "Report only objects in this package (e.g. software-engineering). "
            "The whole library is still loaded, so cross-links and cross-object "
            "checks resolve against every package; only the reported set narrows."
        ),
    )
    args = parser.parse_args()
    if not args.library.is_dir():
        print(f"FAIL: library root not found: {args.library.as_posix()}", file=sys.stderr)
        return 1
    records = validate_library(args.library)
    scope = ""
    if args.package:
        reported = records_in_package(records, args.package)
        if not reported:
            print(f"No objects found in package '{args.package}' under {args.library.as_posix()}.")
            return 1
        scope = f" in package '{args.package}'"
    else:
        reported = records
    errors = 0
    for record in reported:
        for error in record.errors:
            print(f"{record.label}: {error}")
            errors += 1
    if errors:
        print(f"FAIL: {errors} issue(s) across {len(reported)} object(s){scope}")
        return 1
    print(f"PASS: {len(reported)} object(s) validated{scope}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

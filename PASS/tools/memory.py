#!/usr/bin/env python3
"""Skillset Memory tooling: validate, query, append, compact, review.

Memory is the portable empirical record of what happens when the canon is used.
This tool is mechanical: it validates shape, retrieves a bounded set, appends an
event, links evidence, and reports what needs revalidation. It never decides
whether an artifact was good, never mutates a card, and never invents a training
stage that did not run.

The contract it enforces lives in PASS/docs/MEMORY_SCHEMA.md. Two invariants are
worth naming here because they are the reason the tool exists at all:

    an invalid run never counts as evidence about a capability
    a write is not persisted until the target is reopened and confirmed

Like the card validator, this reads the memory tree and nothing else. It never
looks for a source document, a page, or a record of the conversation that
produced an entry.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

import yaml

from paths import default_memory_root, default_library_root


SCHEMA_VERSION = 1

SCOPE_TYPES = {"skillset", "ap", "pattern", "drill", "training", "topic", "runtime"}
ENTRY_TYPES = {"recurring_failure", "successful_tendency", "known_boundary", "training_result"}
EVIDENCE_CLASSES = {"stochastic_performance", "deterministic_contract"}
CONFIDENCE_VALUES = {"provisional", "repeated", "strong"}
STATUS_VALUES = {"active", "monitoring", "resolved", "superseded", "obsolete"}
RETRIEVABLE_STATUS = {"active", "monitoring"}
EVIDENCE_ORIGINS = {
    "runtime_self_audit", "user_feedback", "human_teaching", "training_benchmark",
    "regression_failure", "book_close_training", "cross_model_test",
}
FAILURE_LAYERS = {
    "knowledge", "orchestration", "retrieval", "application", "continuity",
    "reference", "tool", "interface", "training",
}
STAGE_RESULTS = {"improved", "partial", "unchanged", "failed", "untested"}
SCORE_VALUES = {"strong", "adequate", "weak", "failed", "unproven"}
VALIDITY_VALUES = {"valid", "invalid"}

ENTRY_REQUIRED = {
    "id", "scope_type", "scope_id", "type", "evidence_class", "observation",
    "confidence", "status",
}
ENTRY_OPTIONAL = {
    "diagnosis", "boundary", "evidence_count", "evidence_events", "evidence_origin",
    "likely_owners", "interventions", "retrieval_cues", "runtime_scope",
    "superseded_by", "last_verified",
}
ENTRY_KEYS = ENTRY_REQUIRED | ENTRY_OPTIONAL
DIAGNOSIS_KEYS = {"failure_layer", "hypothesis"}
INTERVENTION_KEYS = {
    "training", "drill", "isolation_result", "retention_result", "transfer_result",
}
FILE_REQUIRED = {"memory_schema_version", "skillset", "memory_version", "entries"}

EVENT_REQUIRED = {"event_id", "date", "task", "validity"}
EVENT_OPTIONAL = {
    "invalid_reason", "scope_id", "delivery", "observations", "baseline",
    "isolation", "retention", "transfer", "artifact_quality", "process_validity",
    "skill_attribution", "notes",
}
EVENT_KEYS = EVENT_REQUIRED | EVENT_OPTIONAL
STAGE_KEYS = ("baseline", "isolation", "retention", "transfer")
SCORE_KEYS = ("artifact_quality", "process_validity", "skill_attribution")

# Keys from the authoring vocabulary retired 2026-08-15, plus the session-state
# vocabulary the temporary-state firewall excludes. Memory must not grow either
# back under a new namespace. See docs/CLEANUP_2026-08-15.md.
FORBIDDEN_KEYS = {
    "source_id", "source_title", "page", "pages", "locator", "hash", "sha256",
    "receipt", "attestation", "provenance", "ledger",
    "session_id", "chat_id", "current_stage", "stage", "unit", "next_unit",
    "unit_map", "candidate_id", "branch", "parent_gen_id", "root_id", "parent_id",
    "active_source", "reading_progress",
}

# An entry that defers its content to a conversation is not self-contained, and
# the conversation will not survive into the runtime that needs the lesson.
NON_SELF_CONTAINED_PHRASES = (
    "see the chat", "see the old chat", "see the earlier chat", "see the project chat",
    "see the conversation", "as discussed in the chat", "refer to the chat",
    "in the original conversation", "see the transcript", "per the earlier session",
)

# Authoring actions are not training events. Recording one would manufacture
# evidence that a capability was exercised when only a file changed.
AUTHORING_TASK_PHRASES = (
    "authored a card", "authored a drill", "authored a pattern", "wrote a card",
    "committed", "commit ", "validated the library", "ran the validator",
    "regenerated indexes", "regenerated the index", "built the release",
    "created an archive", "generated an archive", "packaged the release",
    "read unit", "processed unit", "closed the source", "closed the book",
)

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)*$")
STALE_DAYS = 180


# ---------------------------------------------------------------- loading


class MemoryError_(Exception):
    """Raised when a store cannot be read at all."""


def domain_dirs(memory_root: Path, domain: str | None) -> list[Path]:
    if not memory_root.is_dir():
        raise MemoryError_(f"memory root not found: {memory_root.as_posix()}")
    if domain:
        target = memory_root / domain
        if not target.is_dir():
            raise MemoryError_(f"no memory for domain '{domain}' under {memory_root.as_posix()}")
        return [target]
    return sorted(p for p in memory_root.iterdir() if p.is_dir() and (p / "skill_memory.yaml").is_file())


def load_memory(domain_dir: Path) -> dict[str, Any]:
    path = domain_dir / "skill_memory.yaml"
    if not path.is_file():
        raise MemoryError_(f"missing {path.as_posix()}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise MemoryError_(f"{path.as_posix()}: top level must be a mapping")
    return data


def load_events(domain_dir: Path) -> tuple[list[dict[str, Any]], list[str]]:
    """Return (events, errors). A malformed line is an error, not an exception."""
    path = domain_dir / "training_history.jsonl"
    events: list[dict[str, Any]] = []
    errors: list[str] = []
    if not path.is_file():
        return events, [f"{path.as_posix()}: missing"]
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"training_history.jsonl:{number}: invalid JSON: {exc}")
            continue
        if not isinstance(event, dict):
            errors.append(f"training_history.jsonl:{number}: line must be a JSON object")
            continue
        events.append(event)
    return events, errors


# ---------------------------------------------------------------- validation


def validate_entry(entry: Any, index: int, errors: list[str]) -> None:
    where = f"entry[{index}]"
    if not isinstance(entry, dict):
        errors.append(f"{where}: must be a mapping")
        return
    label = entry.get("id") if isinstance(entry.get("id"), str) else where

    missing = sorted(ENTRY_REQUIRED - set(entry))
    if missing:
        errors.append(f"{label}: missing required keys: {', '.join(missing)}")
    forbidden = sorted(set(entry) & FORBIDDEN_KEYS)
    if forbidden:
        errors.append(f"{label}: forbidden key(s) from retired or session vocabulary: {', '.join(forbidden)}")
    extra = sorted(set(entry) - ENTRY_KEYS - FORBIDDEN_KEYS)
    if extra:
        errors.append(f"{label}: unknown key(s): {', '.join(extra)}")

    if isinstance(entry.get("id"), str) and not ID_RE.fullmatch(entry["id"]):
        errors.append(f"{label}: id must be uppercase alphanumeric with underscores")

    for key, allowed in (
        ("scope_type", SCOPE_TYPES),
        ("type", ENTRY_TYPES),
        ("evidence_class", EVIDENCE_CLASSES),
        ("confidence", CONFIDENCE_VALUES),
        ("status", STATUS_VALUES),
    ):
        if key in entry and entry[key] not in allowed:
            errors.append(f"{label}: {key} '{entry[key]}' is not in the closed vocabulary")

    observation = entry.get("observation")
    if not isinstance(observation, str) or not observation.strip():
        errors.append(f"{label}: observation must be non-empty text")
    else:
        lowered = observation.lower()
        for phrase in NON_SELF_CONTAINED_PHRASES:
            if phrase in lowered:
                errors.append(f"{label}: observation defers to a conversation ('{phrase}'); it must stand alone")
                break

    if "scope_id" in entry and (not isinstance(entry["scope_id"], str) or not entry["scope_id"].strip()):
        errors.append(f"{label}: scope_id must be a non-empty string")

    diagnosis = entry.get("diagnosis")
    if diagnosis is not None:
        if not isinstance(diagnosis, dict):
            errors.append(f"{label}: diagnosis must be a mapping")
        else:
            unknown = sorted(set(diagnosis) - DIAGNOSIS_KEYS)
            if unknown:
                errors.append(f"{label}: diagnosis has unknown key(s): {', '.join(unknown)}")
            layer = diagnosis.get("failure_layer")
            if layer is not None and layer not in FAILURE_LAYERS:
                errors.append(f"{label}: diagnosis.failure_layer '{layer}' is not in the closed vocabulary")

    origins = entry.get("evidence_origin")
    if origins is not None:
        if not isinstance(origins, list):
            errors.append(f"{label}: evidence_origin must be a list")
        else:
            for origin in origins:
                if origin not in EVIDENCE_ORIGINS:
                    errors.append(f"{label}: evidence_origin '{origin}' is not in the closed vocabulary")

    count = entry.get("evidence_count")
    if count is not None and (not isinstance(count, int) or isinstance(count, bool) or count < 1):
        errors.append(f"{label}: evidence_count must be an integer >= 1")

    for key in ("evidence_events", "likely_owners", "retrieval_cues"):
        if key in entry and not isinstance(entry[key], list):
            errors.append(f"{label}: {key} must be a list")

    interventions = entry.get("interventions")
    if interventions is not None:
        if not isinstance(interventions, list):
            errors.append(f"{label}: interventions must be a list")
        else:
            for item in interventions:
                if not isinstance(item, dict):
                    errors.append(f"{label}: each intervention must be a mapping")
                    continue
                unknown = sorted(set(item) - INTERVENTION_KEYS)
                if unknown:
                    errors.append(f"{label}: intervention has unknown key(s): {', '.join(unknown)}")
                for result_key in ("isolation_result", "retention_result", "transfer_result"):
                    if result_key in item and item[result_key] not in STAGE_RESULTS:
                        errors.append(f"{label}: intervention {result_key} '{item[result_key]}' is not in the closed vocabulary")

    verified = entry.get("last_verified")
    if verified is not None and not (isinstance(verified, (str, date)) and DATE_RE.fullmatch(str(verified))):
        errors.append(f"{label}: last_verified must be YYYY-MM-DD")


def validate_event(event: dict[str, Any], index: int, errors: list[str]) -> None:
    label = event.get("event_id") if isinstance(event.get("event_id"), str) else f"event[{index}]"

    missing = sorted(EVENT_REQUIRED - set(event))
    if missing:
        errors.append(f"{label}: missing required keys: {', '.join(missing)}")
    forbidden = sorted(set(event) & FORBIDDEN_KEYS)
    if forbidden:
        errors.append(f"{label}: forbidden key(s) from retired or session vocabulary: {', '.join(forbidden)}")
    extra = sorted(set(event) - EVENT_KEYS - FORBIDDEN_KEYS)
    if extra:
        errors.append(f"{label}: unknown key(s): {', '.join(extra)}")

    validity = event.get("validity")
    if validity is not None and validity not in VALIDITY_VALUES:
        errors.append(f"{label}: validity must be valid or invalid")
    if validity == "invalid" and not str(event.get("invalid_reason", "")).strip():
        errors.append(f"{label}: invalid_reason is required when validity is invalid")
    if validity == "valid" and event.get("invalid_reason"):
        errors.append(f"{label}: invalid_reason must be absent when validity is valid")

    if "date" in event and not DATE_RE.fullmatch(str(event["date"])):
        errors.append(f"{label}: date must be YYYY-MM-DD")

    task = event.get("task")
    if not isinstance(task, str) or not task.strip():
        errors.append(f"{label}: task must be non-empty text")
    else:
        lowered = task.lower()
        for phrase in AUTHORING_TASK_PHRASES:
            if phrase in lowered:
                errors.append(f"{label}: task describes an authoring action ('{phrase.strip()}'), not an executed capability")
                break

    for key in STAGE_KEYS:
        if key in event and event[key] not in STAGE_RESULTS and not isinstance(event[key], str):
            errors.append(f"{label}: {key} must be text or one of {sorted(STAGE_RESULTS)}")
    for key in ("isolation", "retention", "transfer"):
        if key in event and isinstance(event[key], str) and event[key] not in STAGE_RESULTS:
            errors.append(f"{label}: {key} '{event[key]}' is not in the closed vocabulary")
    for key in SCORE_KEYS:
        if key in event and event[key] not in SCORE_VALUES:
            errors.append(f"{label}: {key} '{event[key]}' is not in the closed vocabulary")

    if "observations" in event and not isinstance(event["observations"], list):
        errors.append(f"{label}: observations must be a list")


def validate_store(domain_dir: Path) -> list[str]:
    errors: list[str] = []
    try:
        memory = load_memory(domain_dir)
    except MemoryError_ as exc:
        return [str(exc)]

    missing = sorted(FILE_REQUIRED - set(memory))
    if missing:
        errors.append(f"skill_memory.yaml: missing file-level keys: {', '.join(missing)}")
    if memory.get("memory_schema_version") != SCHEMA_VERSION:
        errors.append(f"skill_memory.yaml: memory_schema_version must be {SCHEMA_VERSION}")
    if memory.get("skillset") != domain_dir.name:
        errors.append(f"skill_memory.yaml: skillset '{memory.get('skillset')}' does not match directory '{domain_dir.name}'")

    entries = memory.get("entries")
    if entries is None:
        entries = []
    if not isinstance(entries, list):
        errors.append("skill_memory.yaml: entries must be a list")
        entries = []

    for index, entry in enumerate(entries):
        validate_entry(entry, index, errors)

    ids = [e["id"] for e in entries if isinstance(e, dict) and isinstance(e.get("id"), str)]
    for duplicate in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"skill_memory.yaml: duplicate entry id '{duplicate}'")

    events, event_errors = load_events(domain_dir)
    errors.extend(event_errors)
    for index, event in enumerate(events):
        validate_event(event, index, errors)

    event_ids = [e["event_id"] for e in events if isinstance(e.get("event_id"), str)]
    for duplicate in sorted({i for i in event_ids if event_ids.count(i) > 1}):
        errors.append(f"training_history.jsonl: duplicate event_id '{duplicate}'")

    by_event_id = {e["event_id"]: e for e in events if isinstance(e.get("event_id"), str)}
    known_ids = set(ids)

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        label = entry.get("id", "entry")
        superseded_by = entry.get("superseded_by")
        if superseded_by is not None and superseded_by not in known_ids:
            errors.append(f"{label}: superseded_by '{superseded_by}' does not resolve to an entry")
        if entry.get("status") == "superseded" and not superseded_by:
            errors.append(f"{label}: status superseded requires superseded_by")

        cited = entry.get("evidence_events")
        if not isinstance(cited, list):
            continue
        for event_id in cited:
            event = by_event_id.get(event_id)
            if event is None:
                errors.append(f"{label}: evidence_events cites unknown event '{event_id}'")
                continue
            # The invariant this whole tool exists to hold.
            if event.get("validity") == "invalid":
                errors.append(
                    f"{label}: evidence_events cites invalid event '{event_id}' "
                    f"({event.get('invalid_reason', 'no reason recorded')}); "
                    "an invalid run is never evidence about a capability"
                )
        count = entry.get("evidence_count")
        if isinstance(count, int) and not isinstance(count, bool) and cited and count != len(cited):
            errors.append(f"{label}: evidence_count {count} does not match {len(cited)} cited evidence_events")

    return errors


# ---------------------------------------------------------------- query


def score_entry(entry: dict[str, Any], scope_id: str | None, cues: list[str]) -> tuple[bool, int]:
    """Return (matched, score).

    `matched` is what bounds retrieval. Specificity and confidence only rank
    entries that already matched the request; without that separation a broad
    tendency would score points on every task and the bounded set would quietly
    become the whole file.
    """
    matched = False
    score = 0
    if scope_id and entry.get("scope_id") == scope_id:
        matched = True
        score += 100
    entry_cues = [str(c).lower() for c in entry.get("retrieval_cues", []) if isinstance(c, str)]
    haystack = " ".join(entry_cues + [str(entry.get("scope_id", "")).lower()])
    for cue in cues:
        if cue and cue.lower() in haystack:
            matched = True
            score += 10
    # More specific scope outranks broader tendency when both matched.
    score += {"ap": 5, "pattern": 5, "drill": 5, "training": 5, "topic": 3, "runtime": 2, "skillset": 1}.get(
        str(entry.get("scope_type")), 0
    )
    score += {"strong": 3, "repeated": 2, "provisional": 1}.get(str(entry.get("confidence")), 0)
    if entry.get("status") == "active":
        score += 1
    return matched, score


def query_store(domain_dir: Path, scope_id: str | None, cues: list[str], limit: int) -> list[dict[str, Any]]:
    memory = load_memory(domain_dir)
    entries = [e for e in memory.get("entries") or [] if isinstance(e, dict)]
    # Resolved history stays in the file and stops biasing the runtime.
    candidates = [e for e in entries if e.get("status") in RETRIEVABLE_STATUS]
    if scope_id or cues:
        scored = [(score_entry(e, scope_id, cues), e) for e in candidates]
        hits = [(score, entry) for (matched, score), entry in scored if matched]
        hits.sort(key=lambda pair: (-pair[0], str(pair[1].get("id"))))
        candidates = [entry for _, entry in hits]
    else:
        candidates.sort(key=lambda e: str(e.get("id")))
    return candidates[:limit]


# ---------------------------------------------------------------- append


def next_event_id(events: list[dict[str, Any]], domain: str) -> str:
    # The prefix belongs to the store, not to how the caller spelled the domain.
    # Deriving it from the argument lets "se" and "software-engineering" open two
    # id series in one file, and the second one restarts at 0001 because the scan
    # below only sees ids carrying its own prefix.
    prefix = f"{domain[:3].upper()}_EV_"
    for event in events:
        match = re.match(r"([A-Z]+_EV_)\d+$", str(event.get("event_id", "")))
        if match:
            prefix = match.group(1)
            break
    highest = 0
    for event in events:
        event_id = str(event.get("event_id", ""))
        if event_id.startswith(prefix):
            tail = event_id[len(prefix):]
            if tail.isdigit():
                highest = max(highest, int(tail))
    return f"{prefix}{highest + 1:04d}"


def append_event(domain_dir: Path, event: dict[str, Any]) -> tuple[bool, list[str]]:
    """Append one event, then reopen the file and confirm it is there.

    The readback is the point. A write that was attempted is not a write that
    landed, and this tool must not report persistence it has not confirmed.
    """
    errors: list[str] = []
    validate_event(event, 0, errors)
    if errors:
        return False, errors

    path = domain_dir / "training_history.jsonl"
    existing, load_errors = load_events(domain_dir)
    if load_errors and not path.is_file():
        return False, load_errors
    if any(e.get("event_id") == event["event_id"] for e in existing):
        return False, [f"event_id '{event['event_id']}' already exists"]

    line = json.dumps(event, ensure_ascii=False, sort_keys=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")

    reread, reread_errors = load_events(domain_dir)
    if reread_errors:
        return False, [f"readback failed: {problem}" for problem in reread_errors]
    if not any(e.get("event_id") == event["event_id"] for e in reread):
        return False, [f"readback failed: '{event['event_id']}' is not present after write"]
    return True, []


# ---------------------------------------------------------------- compact


def write_memory(domain_dir: Path, memory: dict[str, Any]) -> None:
    path = domain_dir / "skill_memory.yaml"
    path.write_text(
        yaml.safe_dump(memory, sort_keys=False, allow_unicode=True, width=88),
        encoding="utf-8",
    )


def compact_link(
    domain_dir: Path,
    entry_id: str,
    event_ids: list[str],
    allow_drop: bool = False,
) -> tuple[bool, list[str]]:
    """Link an entry to the valid events that support it, then read it back.

    This is deliberately mechanical. It does not write the observation prose —
    consolidating five events into one honest sentence is a judgment, and a
    script that guessed at it would be inventing empirical claims.

    `event_ids` is the entry's complete evidence after the call, not an
    addition to it. That is a reasonable contract and an easy one to misread as
    "add these", so a call that would drop an event already cited is refused
    unless `allow_drop` says the loss is intended. The readback below cannot
    catch this on its own: it compares the stored list against what was passed,
    so it confirms the overwrite rather than noticing what the overwrite
    removed. Dropping a citation is sometimes right — an event later found
    invalid, or attributed to the wrong entry — which is why this is a
    confirmation rather than a prohibition.
    """
    memory = load_memory(domain_dir)
    entries = [e for e in memory.get("entries") or [] if isinstance(e, dict)]
    entry = next((e for e in entries if e.get("id") == entry_id), None)
    if entry is None:
        return False, [f"no entry '{entry_id}' in {domain_dir.name}"]

    events, load_errors = load_events(domain_dir)
    if load_errors:
        return False, load_errors
    by_id = {e.get("event_id"): e for e in events}

    problems: list[str] = []
    for event_id in event_ids:
        event = by_id.get(event_id)
        if event is None:
            problems.append(f"unknown event '{event_id}'")
        elif event.get("validity") == "invalid":
            problems.append(
                f"refusing invalid event '{event_id}' "
                f"({event.get('invalid_reason', 'no reason recorded')})"
            )
    if problems:
        return False, problems

    already_cited = [str(e) for e in entry.get("evidence_events") or []]
    dropped = [e for e in already_cited if e not in event_ids]
    if dropped and not allow_drop:
        return False, [
            f"'{entry_id}' already cites {', '.join(dropped)}, which this call would remove: "
            f"pass every event the entry should end up citing, or --replace if the loss is intended"
        ]

    entry["evidence_events"] = list(event_ids)
    entry["evidence_count"] = len(event_ids)
    entry["last_verified"] = date.today().isoformat()
    memory["memory_version"] = int(memory.get("memory_version", 0)) + 1
    write_memory(domain_dir, memory)

    reread = load_memory(domain_dir)
    fresh = next((e for e in reread.get("entries") or [] if isinstance(e, dict) and e.get("id") == entry_id), None)
    if fresh is None or fresh.get("evidence_events") != list(event_ids):
        return False, [f"readback failed: '{entry_id}' does not carry the expected evidence after write"]
    return True, []


def uncited_valid_events(domain_dir: Path) -> list[str]:
    memory = load_memory(domain_dir)
    cited: set[str] = set()
    for entry in memory.get("entries") or []:
        if isinstance(entry, dict) and isinstance(entry.get("evidence_events"), list):
            cited.update(str(e) for e in entry["evidence_events"])
    events, _ = load_events(domain_dir)
    return [
        str(e.get("event_id"))
        for e in events
        if e.get("validity") == "valid" and str(e.get("event_id")) not in cited
    ]


# ---------------------------------------------------------------- review


def library_object_ids(library_root: Path) -> set[str]:
    ids: set[str] = set()
    if not library_root.is_dir():
        return ids
    for path in library_root.rglob("*.md"):
        if path.name in {"README.md", "INDEX.md"}:
            continue
        head = path.read_text(encoding="utf-8")[:2000]
        match = re.search(r"(?m)^object_id:\s*(\S+)\s*$", head)
        if match:
            ids.add(match.group(1))
    return ids


def review_store(domain_dir: Path, library_root: Path | None) -> list[str]:
    notes: list[str] = []
    memory = load_memory(domain_dir)
    entries = [e for e in memory.get("entries") or [] if isinstance(e, dict)]
    known = library_object_ids(library_root) if library_root else set()
    cutoff = datetime.now().date() - timedelta(days=STALE_DAYS)

    for entry in entries:
        label = entry.get("id", "entry")
        status = entry.get("status")
        if status not in RETRIEVABLE_STATUS:
            continue
        verified = entry.get("last_verified")
        if not verified:
            notes.append(f"{label}: active with no last_verified")
        elif DATE_RE.fullmatch(str(verified)) and date.fromisoformat(str(verified)) < cutoff:
            notes.append(f"{label}: last verified {verified}, older than {STALE_DAYS} days")
        if entry.get("confidence") == "strong" and int(entry.get("evidence_count", 0) or 0) <= 1:
            notes.append(f"{label}: confidence strong on {entry.get('evidence_count', 0)} event(s)")
        if entry.get("evidence_class") == "deterministic_contract" and status == "active":
            notes.append(
                f"{label}: deterministic_contract still active: if the fix landed, "
                "move it to resolved and let the test hold it"
            )
        if known:
            for owner in entry.get("likely_owners") or []:
                owner = str(owner)
                if re.fullmatch(r"(?:PAT|DRILL|AP)_[a-z0-9_]+", owner) and owner not in known:
                    notes.append(f"{label}: likely_owner '{owner}' no longer exists in the library")
    uncited = uncited_valid_events(domain_dir)
    if uncited:
        notes.append(f"{len(uncited)} valid event(s) not yet cited by any entry: {', '.join(uncited[:8])}")
    return notes


# ---------------------------------------------------------------- CLI


def cmd_validate(args: argparse.Namespace) -> int:
    dirs = domain_dirs(args.memory, args.domain)
    if not dirs:
        print(f"No domain memory found under {args.memory.as_posix()}.")
        return 0
    total = 0
    for domain_dir in dirs:
        errors = validate_store(domain_dir)
        for error in errors:
            print(f"{domain_dir.name}: {error}")
        total += len(errors)
    if total:
        print(f"FAIL: {total} issue(s) across {len(dirs)} memory store(s)")
        return 1
    entries = sum(len(load_memory(d).get("entries") or []) for d in dirs)
    events = sum(len(load_events(d)[0]) for d in dirs)
    print(f"PASS: {len(dirs)} store(s), {entries} entr(ies), {events} event(s) validated")
    return 0


def cmd_query(args: argparse.Namespace) -> int:
    dirs = domain_dirs(args.memory, args.domain)
    cues = [c.strip() for c in (args.cues or "").split(",") if c.strip()]
    returned: list[str] = []
    for domain_dir in dirs:
        results = query_store(domain_dir, args.scope_id, cues, args.limit)
        for entry in results:
            returned.append(str(entry.get("id")))
            print(f"[{entry.get('id')}] {entry.get('scope_type')}:{entry.get('scope_id')} "
                  f"({entry.get('type')}, {entry.get('confidence')}, {entry.get('status')})")
            print(f"    {' '.join(str(entry.get('observation', '')).split())}")
            if entry.get("boundary"):
                print(f"    boundary: {' '.join(str(entry['boundary']).split())}")
    # A retrieval receipt. Consultation cannot be proven by a memory file
    # existing; it can be recorded by naming what was actually returned.
    print(f"retrieved: {', '.join(returned) if returned else '(none)'}")
    return 0


def cmd_append(args: argparse.Namespace) -> int:
    dirs = domain_dirs(args.memory, args.domain)
    if len(dirs) != 1:
        print("FAIL: append requires exactly one --domain", file=sys.stderr)
        return 1
    domain_dir = dirs[0]
    if args.json:
        event = json.loads(Path(args.json).read_text(encoding="utf-8")) if Path(args.json).is_file() else json.loads(args.json)
    else:
        event = {"task": args.task, "validity": args.validity, "date": args.date or date.today().isoformat()}
        if args.invalid_reason:
            event["invalid_reason"] = args.invalid_reason
        if args.scope_id:
            event["scope_id"] = args.scope_id
        if args.delivery:
            event["delivery"] = args.delivery
        if args.note:
            event["notes"] = args.note
    events, _ = load_events(domain_dir)
    event.setdefault("event_id", next_event_id(events, domain_dir.name))
    event.setdefault("date", date.today().isoformat())

    ok, problems = append_event(domain_dir, event)
    if not ok:
        for problem in problems:
            print(f"{domain_dir.name}: {problem}", file=sys.stderr)
        print("FAIL: event not appended", file=sys.stderr)
        return 1
    print(f"PASS: appended {event['event_id']} and confirmed it on readback")
    return 0


def cmd_compact(args: argparse.Namespace) -> int:
    dirs = domain_dirs(args.memory, args.domain)
    if args.entry:
        if len(dirs) != 1:
            print("FAIL: linking evidence requires exactly one --domain", file=sys.stderr)
            return 1
        event_ids = [e.strip() for e in (args.events or "").split(",") if e.strip()]
        if not event_ids:
            print("FAIL: --events is required with --entry", file=sys.stderr)
            return 1
        ok, problems = compact_link(dirs[0], args.entry, event_ids, allow_drop=args.replace)
        if not ok:
            for problem in problems:
                print(f"{dirs[0].name}: {problem}", file=sys.stderr)
            print("FAIL: evidence not linked", file=sys.stderr)
            return 1
        print(
            f"PASS: {args.entry} now cites {', '.join(event_ids)} "
            f"({len(event_ids)} event(s)), confirmed on readback"
        )
        return 0
    for domain_dir in dirs:
        uncited = uncited_valid_events(domain_dir)
        if uncited:
            print(f"{domain_dir.name}: {len(uncited)} valid event(s) awaiting consolidation:")
            for event_id in uncited:
                print(f"    {event_id}")
        else:
            print(f"{domain_dir.name}: no valid events awaiting consolidation")
    return 0


def cmd_review(args: argparse.Namespace) -> int:
    dirs = domain_dirs(args.memory, args.domain)
    library = args.library if args.library and args.library.is_dir() else None
    total = 0
    for domain_dir in dirs:
        notes = review_store(domain_dir, library)
        for note in notes:
            print(f"{domain_dir.name}: {note}")
        total += len(notes)
    print(f"{total} item(s) suggested for review")
    return 0


def main() -> int:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--memory", type=Path, default=default_memory_root())
    common.add_argument("--domain", default=None, help="Limit to one domain (e.g. art).")

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser(
        "validate", parents=[common],
        help="Check shape, closed vocabularies, and evidence admissibility.",
    )

    query = sub.add_parser("query", parents=[common], help="Retrieve a bounded set of active entries.")
    query.add_argument("--scope-id", default=None)
    query.add_argument("--cues", default=None, help="Comma-separated retrieval cues.")
    query.add_argument("--limit", type=int, default=5)

    append = sub.add_parser("append", parents=[common], help="Append one high-signal event, verified by readback.")
    append.add_argument("--task")
    append.add_argument("--validity", choices=sorted(VALIDITY_VALUES), default="valid")
    append.add_argument("--invalid-reason", default=None)
    append.add_argument("--scope-id", default=None)
    append.add_argument("--delivery", default=None)
    append.add_argument("--date", default=None)
    append.add_argument("--note", default=None)
    append.add_argument("--json", default=None, help="Path to, or literal, JSON event.")

    compact = sub.add_parser("compact", parents=[common], help="Report or link the evidence behind an entry.")
    compact.add_argument("--entry", default=None)
    compact.add_argument("--events", default=None, help="Comma-separated event ids.")
    compact.add_argument(
        "--replace",
        action="store_true",
        help="Confirm that events the entry already cites and --events omits should be dropped.",
    )

    review = sub.add_parser("review", parents=[common], help="List entries that need revalidation.")
    review.add_argument("--library", type=Path, default=default_library_root())

    args = parser.parse_args()
    handlers = {
        "validate": cmd_validate, "query": cmd_query, "append": cmd_append,
        "compact": cmd_compact, "review": cmd_review,
    }
    try:
        return handlers[args.command](args)
    except MemoryError_ as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

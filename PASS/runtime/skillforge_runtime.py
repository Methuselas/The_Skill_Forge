#!/usr/bin/env python3
"""Repository-side SkillForge contract resolver and auditor.

This is an optional deterministic helper, not a host-native execution kernel. It
runs only when something explicitly invokes it, holds no state between
invocations, and cannot observe, intercept, or block anything a model or host
does. Describing it as a runtime that enforces behavior would be false.

What it actually provides:

- ``resolve`` reads a profile, matches the request text against the profile's
  ordered routing rules, and returns the resolved mode/lane together with the
  declared execution contract, activated metaskills, and required checks. The
  contract block is returned verbatim; Python does not interpret its meaning.
- ``verify`` audits a completion record that its caller supplies, reporting which
  required checks or profile-declared evidence records are absent/inconsistent.
  It is a report on a record, not a gate on an action: whoever must satisfy the
  checks also writes the record, and Python never independently sees the artifact.
- ``doctor`` validates that a profile and the library's activation manifests are
  internally consistent and that every object reference resolves to a real card.

Honoring the returned contract is the consuming skill's responsibility. APs own
goal-directed craft control flow; Patterns own the individual decisions. The
semantic meaning lives in the SkillForge cards and profile.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

SCHEMA_VERSION = 1


def read_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected YAML mapping")
    return data


def normalize_text(value: str) -> str:
    # Treat underscores as word separators so ordinary attachment names such as
    # ``Blu_ref_sheets.zip`` activate the same declarative phrase rules as
    # ``Blu ref sheets.zip``. Keep other punctuation behavior stable.
    return re.sub(r"\s+", " ", value.casefold().replace("_", " ")).strip()


def phrase_matches(text: str, phrases: list[str]) -> list[str]:
    normalized = normalize_text(text)
    return [phrase for phrase in phrases if normalize_text(str(phrase)) in normalized]


def regex_matches(text: str, patterns: list[str]) -> list[str]:
    return [pattern for pattern in patterns if re.search(pattern, text, flags=re.I)]


CONDITION_KEYS = frozenset({"phase", "modes", "lanes", "any_phrases", "all_phrases", "any_regex"})


def condition_matches(condition: dict[str, Any], context: dict[str, Any]) -> bool:
    """Evaluate a small declarative activation condition.

    Supported keys are CONDITION_KEYS and intentionally stay generic;
    domain-specific semantics live in data. `phase` is only meaningful for
    RUNTIME.yaml activations — routing, lane, and risk rules are evaluated in a
    single phase, so a `phase` condition there is always trivially true.
    """
    if not condition:
        return True
    if condition.get("phase") and condition["phase"] != context.get("phase"):
        return False
    modes = condition.get("modes") or []
    if modes and context.get("mode") not in modes:
        return False
    lanes = condition.get("lanes") or []
    if lanes and context.get("lane") not in lanes:
        return False
    request = str(context.get("request") or "")
    any_phrases = [str(x) for x in condition.get("any_phrases") or []]
    if any_phrases and not phrase_matches(request, any_phrases):
        return False
    all_phrases = [str(x) for x in condition.get("all_phrases") or []]
    if all_phrases and len(phrase_matches(request, all_phrases)) != len(all_phrases):
        return False
    any_regex = [str(x) for x in condition.get("any_regex") or []]
    if any_regex and not regex_matches(request, any_regex):
        return False
    return True


def discover_runtime_manifests(library: Path) -> list[tuple[Path, dict[str, Any]]]:
    manifests: list[tuple[Path, dict[str, Any]]] = []
    if not library.is_dir():
        return manifests
    for path in sorted(library.rglob("RUNTIME.yaml")):
        manifests.append((path, read_yaml(path)))
    return manifests


def _mode_alias_index(profile: dict[str, Any]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    modes = profile.get("execution_modes") or {}
    if not isinstance(modes, dict):
        return aliases
    for mode_name, spec in modes.items():
        aliases[normalize_text(str(mode_name))] = str(mode_name)
        if isinstance(spec, dict):
            for alias in spec.get("aliases") or []:
                aliases[normalize_text(str(alias))] = str(mode_name)
    return aliases


def resolve_mode(profile: dict[str, Any], request: str, explicit_mode: str | None = None) -> tuple[str, str]:
    modes = profile.get("execution_modes") or {}
    if not isinstance(modes, dict) or not modes:
        raise ValueError("profile.execution_modes must be a non-empty mapping")
    aliases = _mode_alias_index(profile)
    if explicit_mode:
        key = normalize_text(explicit_mode)
        if key not in aliases:
            raise ValueError(f"unsupported explicit mode: {explicit_mode}")
        return aliases[key], "explicit user/runtime override"

    routing = profile.get("routing") or {}
    if not isinstance(routing, dict):
        raise ValueError("profile.routing must be a mapping")

    # Rules are ordered. Profiles can therefore express deterministic priority
    # without teaching the resolver what an art drill or code review means.
    for rule in routing.get("rules") or []:
        if not isinstance(rule, dict) or not rule.get("mode"):
            continue
        mode = str(rule["mode"])
        if mode not in modes:
            raise ValueError(f"routing rule references unknown mode: {mode}")
        condition = rule.get("when") or {}
        if not isinstance(condition, dict):
            raise ValueError("routing rule 'when' must be a mapping")
        context = {"request": request, "mode": mode, "phase": "pre_production"}
        if condition_matches(condition, context):
            return mode, str(rule.get("reason") or f"matched routing rule for {mode}")

    default_mode = str(profile.get("default_mode") or "")
    if default_mode not in modes:
        raise ValueError(f"profile default_mode is missing or unknown: {default_mode}")
    return default_mode, "profile default"


def resolve_lane(profile: dict[str, Any], request: str) -> tuple[str, str]:
    lanes = profile.get("lanes") or {}
    if not isinstance(lanes, dict) or not lanes:
        raise ValueError("profile.lanes must be a non-empty mapping")
    routing = profile.get("lane_routing") or {}
    if not isinstance(routing, dict):
        raise ValueError("profile.lane_routing must be a mapping")
    for rule in routing.get("rules") or []:
        if not isinstance(rule, dict) or not rule.get("lane"):
            continue
        lane = str(rule["lane"])
        if lane not in lanes:
            raise ValueError(f"lane routing rule references unknown lane: {lane}")
        condition = rule.get("when") or {}
        if not isinstance(condition, dict):
            raise ValueError("lane routing rule 'when' must be a mapping")
        context = {"request": request, "lane": lane, "phase": "pre_production"}
        if condition_matches(condition, context):
            return lane, str(rule.get("reason") or f"matched lane routing rule for {lane}")
    default_lane = str(profile.get("default_lane") or "")
    if default_lane not in lanes:
        raise ValueError(f"profile default_lane is missing or unknown: {default_lane}")
    return default_lane, "profile default"


def activate_metaskills(
    library: Path,
    request: str,
    mode: str,
    lane: str = "skill",
    *,
    phase: str = "pre_production",
) -> list[dict[str, Any]]:
    active: list[dict[str, Any]] = []
    context = {
        "request": request,
        "mode": mode,
        "lane": lane,
        "phase": phase,
    }
    for path, manifest in discover_runtime_manifests(library):
        entries = manifest.get("activations") or []
        if not isinstance(entries, list):
            raise ValueError(f"{path}: activations must be a list")
        for entry in entries:
            if not isinstance(entry, dict) or not entry.get("object_id"):
                raise ValueError(f"{path}: activation entry missing object_id")
            when = entry.get("when") or {}
            if not isinstance(when, dict):
                raise ValueError(f"{path}: activation 'when' must be a mapping")
            if condition_matches(when, context):
                active.append(
                    {
                        "object_id": str(entry["object_id"]),
                        "module": path.parent.relative_to(library).as_posix(),
                        "package": path.parent.relative_to(library).parts[0],
                        "phase": phase,
                        "reason": str(entry.get("reason") or "runtime activation rule"),
                    }
                )
    # Deterministic de-duplication while preserving manifest order.
    seen: set[str] = set(); deduped: list[dict[str, Any]] = []
    for item in active:
        if item["object_id"] in seen:
            continue
        seen.add(item["object_id"]); deduped.append(item)
    return deduped


def resolve_risk_checks(
    profile: dict[str, Any],
    request: str,
    mode: str,
    current_stage: int | None = None,
) -> list[str]:
    """Resolve task-risk checks at the legal visual resolution.

    Direct mode uses each rule's ordinary ``checks`` list. Staged Art may declare
    ``checks_by_stage`` so a low-information stage is not forced to prove detail
    it is explicitly required to withhold. The resolver reports the selected
    checks; it still does not judge the artwork or observe the host.
    """
    checks: list[str] = []
    for rule in profile.get("risk_rules") or []:
        if not isinstance(rule, dict):
            continue
        when = rule.get("when") or {}
        if not isinstance(when, dict):
            raise ValueError("risk rule 'when' must be a mapping")
        context = {"request": request, "mode": mode, "phase": "pre_production"}
        if condition_matches(when, context):
            selected_checks = rule.get("checks") or []
            stage_map = rule.get("checks_by_stage") or {}
            if mode == "staged_production" and current_stage is not None and isinstance(stage_map, dict):
                selected_checks = stage_map.get(current_stage, stage_map.get(str(current_stage), selected_checks))
            for check in selected_checks or []:
                value = str(check)
                if value not in checks:
                    checks.append(value)
    return checks


def _explicit_stage_from_request(request: str) -> int | None:
    match = re.search(r"\bstage\s*([0-4])\b", request, flags=re.I)
    return int(match.group(1)) if match else None


def resolve_task(
    profile: dict[str, Any],
    library: Path,
    request: str,
    explicit_mode: str | None = None,
    current_stage: int | None = None,
) -> dict[str, Any]:
    mode, reason = resolve_mode(profile, request, explicit_mode)
    lane, lane_reason = resolve_lane(profile, request)
    mode_spec = (profile.get("execution_modes") or {}).get(mode)
    if not isinstance(mode_spec, dict):
        raise ValueError(f"execution mode {mode} must be a mapping")
    contract = mode_spec.get("contract") or {}
    if not isinstance(contract, dict):
        raise ValueError(f"execution mode {mode}.contract must be a mapping")

    pre = activate_metaskills(library, request, mode, lane, phase="pre_production")
    post = activate_metaskills(library, request, mode, lane, phase="post_production")
    if mode == "staged_production":
        if current_stage is None:
            current_stage = _explicit_stage_from_request(request)
        if current_stage is None:
            # A fresh staged thread can legally begin only at Stage 0. Later
            # turns should supply the controller's actual approved current stage.
            current_stage = 0
        if current_stage not in {0, 1, 2, 3, 4}:
            raise ValueError(f"unsupported Drawing stage: {current_stage}")
    else:
        current_stage = None
    risks = resolve_risk_checks(profile, request, mode, current_stage)
    completion_gate = profile.get("completion_gate") or {}
    if not isinstance(completion_gate, dict):
        raise ValueError("profile.completion_gate must be a mapping")

    fingerprint = hashlib.sha256(request.encode("utf-8")).hexdigest()
    return {
        "schema_version": SCHEMA_VERSION,
        "profile": str(profile.get("profile_id") or profile.get("name") or "unknown"),
        "request_sha256": fingerprint,
        "mode": mode,
        "mode_reason": reason,
        "lane": lane,
        "lane_reason": lane_reason,
        "current_stage": current_stage,
        "contract": contract,
        "metaskills": {
            "pre_production": [item for item in pre if item["package"] == "metaskills"],
            "post_production": [item for item in post if item["package"] == "metaskills"],
        },
        "risk_checks": risks,
        "completion_gate": completion_gate,
    }


def _audit_evidence_requirements(
    gate: dict[str, Any], resolution: dict[str, Any], completion: dict[str, Any]
) -> tuple[list[str], list[str]]:
    requirements = gate.get("evidence_requirements") or []
    if not requirements:
        return [], []
    if not isinstance(requirements, list):
        raise ValueError("completion_gate.evidence_requirements must be a list")
    evidence = completion.get("evidence") or {}
    if not isinstance(evidence, dict):
        raise ValueError("completion.evidence must be a mapping")

    active_risks = {str(x) for x in resolution.get("risk_checks") or []}
    active_requirements: list[str] = []
    errors: list[str] = []
    for index, requirement in enumerate(requirements):
        if not isinstance(requirement, dict):
            raise ValueError(f"completion_gate.evidence_requirements[{index}] must be a mapping")
        requirement_id = str(requirement.get("id") or f"requirement_{index}")
        triggers = {str(x) for x in requirement.get("when_any_risk_checks") or []}
        if triggers and not (triggers & active_risks):
            continue
        active_requirements.append(requirement_id)

        collection_name = str(requirement.get("collection") or "")
        if not collection_name:
            errors.append(f"{requirement_id}: profile requirement has no collection name")
            continue
        collection = evidence.get(collection_name)
        if not isinstance(collection, dict):
            errors.append(f"{requirement_id}: missing evidence collection {collection_name}")
            continue

        count_field = str(requirement.get("declared_count_field") or "declared_count")
        instances_field = str(requirement.get("instances_field") or "instances")
        declared_count = collection.get(count_field)
        instances = collection.get(instances_field)
        if not isinstance(declared_count, int) or isinstance(declared_count, bool) or declared_count < 0:
            errors.append(f"{requirement_id}: {collection_name}.{count_field} must be a non-negative integer")
            continue
        if not isinstance(instances, list):
            errors.append(f"{requirement_id}: {collection_name}.{instances_field} must be a list")
            continue
        if len(instances) != declared_count:
            errors.append(
                f"{requirement_id}: {collection_name} declares {declared_count} visible instances but records {len(instances)}"
            )
        minimum = int(requirement.get("minimum_instances") or 0)
        if declared_count < minimum:
            errors.append(f"{requirement_id}: requires at least {minimum} recorded instance(s)")

        required_strings = [str(x) for x in requirement.get("required_string_fields") or []]
        required_true = [str(x) for x in requirement.get("required_true_fields") or []]
        status_fields = requirement.get("required_status_fields") or {}
        equal_pairs = requirement.get("equal_integer_pairs") or []
        if not isinstance(status_fields, dict):
            raise ValueError(f"{requirement_id}: required_status_fields must be a mapping")
        if not isinstance(equal_pairs, list):
            raise ValueError(f"{requirement_id}: equal_integer_pairs must be a list")

        seen_ids: set[str] = set()
        for instance_index, instance in enumerate(instances):
            label = f"{collection_name}[{instance_index}]"
            if not isinstance(instance, dict):
                errors.append(f"{requirement_id}: {label} must be a mapping")
                continue
            for field in required_strings:
                value = instance.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{requirement_id}: {label}.{field} must be a non-empty string")
            instance_id = instance.get("id")
            if isinstance(instance_id, str) and instance_id.strip():
                if instance_id in seen_ids:
                    errors.append(f"{requirement_id}: duplicate instance id {instance_id!r}")
                seen_ids.add(instance_id)
            for field in required_true:
                if instance.get(field) is not True:
                    errors.append(f"{requirement_id}: {label}.{field} must be true")
            for field, allowed in status_fields.items():
                allowed_values = [str(x) for x in (allowed or [])]
                if str(instance.get(field) or "") not in allowed_values:
                    errors.append(
                        f"{requirement_id}: {label}.{field} must be one of {allowed_values!r}"
                    )
            for pair in equal_pairs:
                if not isinstance(pair, list) or len(pair) != 2:
                    raise ValueError(f"{requirement_id}: each equal_integer_pairs entry must contain two fields")
                expected_field, observed_field = str(pair[0]), str(pair[1])
                expected = instance.get(expected_field)
                observed = instance.get(observed_field)
                for field, value in ((expected_field, expected), (observed_field, observed)):
                    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                        errors.append(f"{requirement_id}: {label}.{field} must be a non-negative integer")
                if (
                    isinstance(expected, int) and not isinstance(expected, bool)
                    and isinstance(observed, int) and not isinstance(observed, bool)
                    and expected != observed
                ):
                    errors.append(
                        f"{requirement_id}: {label} expected {expected_field}={expected} but observed {observed_field}={observed}"
                    )
    return active_requirements, errors


def verify_completion(resolution: dict[str, Any], completion: dict[str, Any]) -> dict[str, Any]:
    gate = resolution.get("completion_gate") or {}
    required = [str(x) for x in gate.get("required_checks") or []]
    risk_required = bool(gate.get("require_all_risk_checks", False))
    checks = completion.get("checks") or {}
    risk_checks = completion.get("risk_checks") or {}
    if not isinstance(checks, dict) or not isinstance(risk_checks, dict):
        raise ValueError("completion checks and risk_checks must be mappings")

    missing = [name for name in required if checks.get(name) is not True]
    unresolved_risks: list[str] = []
    if risk_required:
        for name in resolution.get("risk_checks") or []:
            if risk_checks.get(name) is not True:
                unresolved_risks.append(str(name))

    active_evidence_requirements, evidence_errors = _audit_evidence_requirements(gate, resolution, completion)
    passed = not missing and not unresolved_risks and not evidence_errors
    return {
        # `passed` is retained for CLI/backward compatibility. It means only that
        # the caller-supplied completion RECORD satisfies this profile contract.
        "passed": passed,
        "completion_record_complete": passed,
        # This helper never sees pixels and therefore cannot truthfully make this
        # claim even when a well-formed visual-evidence record was supplied.
        "artifact_visually_validated": False,
        "validation_basis": (
            "caller_supplied_visual_evidence_record"
            if active_evidence_requirements
            else "caller_attestation"
        ),
        "missing_required_checks": missing,
        "unresolved_risk_checks": unresolved_risks,
        "active_evidence_requirements": active_evidence_requirements,
        "evidence_errors": evidence_errors,
        "rollback_enabled": bool((resolution.get("contract") or {}).get("rollback_enabled", False)),
    }


def _frontmatter_object_ids(library: Path) -> set[str]:
    result: set[str] = set()
    for path in library.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not text.startswith("---\n"):
            continue
        try:
            _empty, front, _body = text.split("---\n", 2)
            data = yaml.safe_load(front)
        except (ValueError, yaml.YAMLError):
            continue
        if isinstance(data, dict) and data.get("object_id"):
            result.add(str(data["object_id"]))
    return result


OBJECT_ID_PATTERN = re.compile(r"^(?:AP|PAT|DRILL)_[a-z0-9_]+$")


def _object_id_references(node: Any, trail: str = "profile") -> list[tuple[str, str]]:
    """Collect (path, object_id) for every value shaped like a card object_id.

    Profiles carry card references in ordinary contract fields — `stage_ap_thread`,
    `staged_controller`, `image_generation_handoff` — that no schema declares. A
    reference is recognized by the library's own naming convention rather than by
    a per-domain key list, so a new profile gets the same check for free.
    """
    found: list[tuple[str, str]] = []
    if isinstance(node, dict):
        for key, value in node.items():
            found.extend(_object_id_references(value, f"{trail}.{key}"))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            found.extend(_object_id_references(value, f"{trail}[{index}]"))
    elif isinstance(node, str) and OBJECT_ID_PATTERN.match(node):
        found.append((trail, node))
    return found


def _condition_problems(condition: Any, where: str) -> list[str]:
    if not isinstance(condition, dict):
        return [f"{where}: 'when' must be a mapping"]
    unknown = sorted(set(condition) - CONDITION_KEYS)
    return [f"{where}: unknown condition key {key!r}" for key in unknown]


def _rule_conditions(profile: dict[str, Any]) -> list[tuple[Any, str]]:
    conditions: list[tuple[Any, str]] = []
    for section, key in (("routing", "mode"), ("lane_routing", "lane")):
        block = profile.get(section)
        if not isinstance(block, dict):
            continue
        for index, rule in enumerate(block.get("rules") or []):
            if isinstance(rule, dict) and "when" in rule:
                conditions.append((rule["when"], f"profile.{section}.rules[{index}]"))
    for index, rule in enumerate(profile.get("risk_rules") or []):
        if isinstance(rule, dict) and "when" in rule:
            name = rule.get("id") or index
            conditions.append((rule["when"], f"profile.risk_rules[{name}]"))
    return conditions


def doctor(profile: dict[str, Any], library: Path) -> list[str]:
    problems: list[str] = []
    if profile.get("schema_version") != SCHEMA_VERSION:
        problems.append(f"profile schema_version must be {SCHEMA_VERSION}")
    modes = profile.get("execution_modes")
    if not isinstance(modes, dict) or not modes:
        problems.append("profile.execution_modes must be a non-empty mapping")
    elif profile.get("default_mode") not in modes:
        problems.append("profile.default_mode must name an execution mode")
    lanes = profile.get("lanes")
    if not isinstance(lanes, dict) or not lanes:
        problems.append("profile.lanes must be a non-empty mapping")
    elif profile.get("default_lane") not in lanes:
        problems.append("profile.default_lane must name a lane")
    for condition, where in _rule_conditions(profile):
        problems.extend(_condition_problems(condition, where))

    completion_gate = profile.get("completion_gate") or {}
    if not isinstance(completion_gate, dict):
        problems.append("profile.completion_gate must be a mapping")
    else:
        evidence_requirements = completion_gate.get("evidence_requirements") or []
        if not isinstance(evidence_requirements, list):
            problems.append("profile.completion_gate.evidence_requirements must be a list")
        else:
            for index, requirement in enumerate(evidence_requirements):
                where = f"profile.completion_gate.evidence_requirements[{index}]"
                if not isinstance(requirement, dict):
                    problems.append(f"{where} must be a mapping")
                    continue
                if not requirement.get("id"):
                    problems.append(f"{where}.id is required")
                if not requirement.get("collection"):
                    problems.append(f"{where}.collection is required")
                triggers = requirement.get("when_any_risk_checks") or []
                if not isinstance(triggers, list) or not all(isinstance(item, str) for item in triggers):
                    problems.append(f"{where}.when_any_risk_checks must be a string list")
                pairs = requirement.get("equal_integer_pairs") or []
                if not isinstance(pairs, list) or any(
                    not isinstance(pair, list) or len(pair) != 2 or not all(isinstance(field, str) for field in pair)
                    for pair in pairs
                ):
                    problems.append(f"{where}.equal_integer_pairs must contain two-field string lists")
    for index, rule in enumerate(profile.get("risk_rules") or []):
        if not isinstance(rule, dict):
            continue
        stage_map = rule.get("checks_by_stage")
        if stage_map is None:
            continue
        name = rule.get("id") or index
        if not isinstance(stage_map, dict):
            problems.append(f"profile.risk_rules[{name}].checks_by_stage must be a mapping")
            continue
        normalized_stages: set[int] = set()
        for stage, checks in stage_map.items():
            try:
                stage_number = int(stage)
            except (TypeError, ValueError):
                problems.append(f"profile.risk_rules[{name}].checks_by_stage has invalid stage {stage!r}")
                continue
            normalized_stages.add(stage_number)
            if stage_number not in {0, 1, 2, 3, 4}:
                problems.append(f"profile.risk_rules[{name}].checks_by_stage has unsupported stage {stage_number}")
            if not isinstance(checks, list) or not all(isinstance(item, str) for item in checks):
                problems.append(f"profile.risk_rules[{name}].checks_by_stage[{stage_number}] must be a string list")
        if normalized_stages != {0, 1, 2, 3, 4}:
            problems.append(f"profile.risk_rules[{name}].checks_by_stage must define stages 0-4")
    if not library.is_dir():
        problems.append(f"library not found: {library}")
        return problems

    known = _frontmatter_object_ids(library)
    # Contract fields naming a card are returned to the consumer verbatim, so a
    # typo there is invisible until a live run asks for an AP that never existed.
    for where, object_id in _object_id_references(profile):
        if object_id not in known:
            problems.append(f"{where}: unknown object_id {object_id}")
    try:
        manifests = discover_runtime_manifests(library)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        problems.append(str(exc)); manifests = []
    if not manifests:
        problems.append("no RUNTIME.yaml metaskill manifests found")
    for path, manifest in manifests:
        if manifest.get("schema_version") != SCHEMA_VERSION:
            problems.append(f"{path}: schema_version must be {SCHEMA_VERSION}")
        # resolve_task returns metaskill activations only. A manifest anywhere
        # else parses and validates but is silently discarded, so say so here
        # rather than letting a domain believe it declared an activation.
        if path.parent.relative_to(library).parts[0] != "metaskills":
            problems.append(f"{path}: activations outside metaskills/ are never returned by resolve")
        for entry in manifest.get("activations") or []:
            if not isinstance(entry, dict) or not entry.get("object_id"):
                problems.append(f"{path}: invalid activation entry")
                continue
            object_id = str(entry["object_id"])
            if object_id not in known:
                problems.append(f"{path}: unknown object_id {object_id}")
            if "when" in entry:
                problems.extend(_condition_problems(entry["when"], f"{path}: {object_id}"))
    return sorted(set(problems))


def default_paths(script: Path) -> tuple[Path, Path]:
    """Return (profile, library) for source or vendored release layout."""
    # Vendored release: <release>/scripts/skillforge_runtime.py
    if script.parent.name == "scripts" and (script.parent.parent / "runtime" / "profile.yaml").is_file():
        root = script.parent.parent
        return root / "runtime" / "profile.yaml", root / "library"
    # Canonical authoring: <repo>/PASS/runtime/skillforge_runtime.py
    repo = script.resolve().parents[2]
    return repo / "PASS" / "runtime" / "profiles" / "generic.yaml", repo / "library"


def main() -> int:
    script = Path(__file__).resolve()
    default_profile, default_library = default_paths(script)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=default_profile)
    parser.add_argument("--library", type=Path, default=default_library)
    sub = parser.add_subparsers(dest="cmd", required=True)

    resolve = sub.add_parser(
        "resolve",
        help="resolve a request against the profile and return the declared execution contract",
    )
    resolve.add_argument("--request", required=True)
    resolve.add_argument("--mode")
    resolve.add_argument("--stage", type=int, choices=range(5), help="current Drawing stage for staged risk resolution")
    resolve.add_argument("--out", type=Path)

    verify = sub.add_parser(
        "verify",
        help=(
            "audit a caller-supplied completion record against the resolved required checks; "
            "reports what is absent, exit 2 if anything is. This is a report on a record, "
            "not a gate on an action."
        ),
    )
    verify.add_argument("--resolution", type=Path, required=True)
    verify.add_argument("--completion", type=Path, required=True)

    sub.add_parser(
        "doctor",
        help="check profile and library activation manifests for internal consistency",
    )
    args = parser.parse_args()

    try:
        profile = read_yaml(args.profile.resolve())
        library = args.library.resolve()
        if args.cmd == "doctor":
            problems = doctor(profile, library)
            if problems:
                print("RUNTIME DOCTOR FAILED:")
                for problem in problems:
                    print(f"- {problem}")
                return 1
            print("PASS: SkillForge runtime doctor")
            return 0
        if args.cmd == "resolve":
            result = resolve_task(profile, library, args.request, args.mode, args.stage)
            rendered = json.dumps(result, indent=2, sort_keys=False) + "\n"
            if args.out:
                args.out.write_text(rendered, encoding="utf-8")
            print(rendered, end="")
            return 0
        resolution = json.loads(args.resolution.read_text(encoding="utf-8"))
        completion = json.loads(args.completion.read_text(encoding="utf-8"))
        if not isinstance(resolution, dict) or not isinstance(completion, dict):
            raise ValueError("resolution/completion must be JSON objects")
        result = verify_completion(resolution, completion)
        print(json.dumps(result, indent=2) + "\n", end="")
        return 0 if result["passed"] else 2
    except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

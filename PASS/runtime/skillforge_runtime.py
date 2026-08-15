#!/usr/bin/env python3
"""Deterministic SkillForge execution router and completion guard.

Python owns orchestration, not domain judgment. It resolves execution mode,
activates declared metaskills, emits required risk/completion checks, and fails
closed when a required completion check has not been recorded. The semantic
meaning of those checks remains in the SkillForge cards and profile.
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
    return re.sub(r"\s+", " ", value.casefold()).strip()


def phrase_matches(text: str, phrases: list[str]) -> list[str]:
    normalized = normalize_text(text)
    return [phrase for phrase in phrases if normalize_text(str(phrase)) in normalized]


def regex_matches(text: str, patterns: list[str]) -> list[str]:
    return [pattern for pattern in patterns if re.search(pattern, text, flags=re.I)]


def condition_matches(condition: dict[str, Any], context: dict[str, Any]) -> bool:
    """Evaluate a small declarative activation condition.

    Supported keys intentionally stay generic: productive, phase, modes, lanes,
    any_phrases, all_phrases, any_regex. Domain-specific semantics live in data.
    """
    if not condition:
        return True
    if "productive" in condition and bool(condition["productive"]) != bool(context.get("productive")):
        return False
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
    # without teaching the kernel what an art drill or code review means.
    for rule in routing.get("rules") or []:
        if not isinstance(rule, dict) or not rule.get("mode"):
            continue
        mode = str(rule["mode"])
        if mode not in modes:
            raise ValueError(f"routing rule references unknown mode: {mode}")
        condition = rule.get("when") or {}
        if not isinstance(condition, dict):
            raise ValueError("routing rule 'when' must be a mapping")
        context = {"request": request, "mode": mode, "productive": True, "phase": "pre_production"}
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
        context = {"request": request, "lane": lane, "productive": True, "phase": "pre_production"}
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
    productive: bool = True,
    phase: str = "pre_production",
) -> list[dict[str, Any]]:
    active: list[dict[str, Any]] = []
    context = {
        "request": request,
        "mode": mode,
        "lane": lane,
        "productive": productive,
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


def resolve_risk_checks(profile: dict[str, Any], request: str, mode: str) -> list[str]:
    checks: list[str] = []
    for rule in profile.get("risk_rules") or []:
        if not isinstance(rule, dict):
            continue
        when = rule.get("when") or {}
        if not isinstance(when, dict):
            raise ValueError("risk rule 'when' must be a mapping")
        context = {"request": request, "mode": mode, "productive": True, "phase": "pre_production"}
        if condition_matches(when, context):
            for check in rule.get("checks") or []:
                value = str(check)
                if value not in checks:
                    checks.append(value)
    return checks


def resolve_task(
    profile: dict[str, Any],
    library: Path,
    request: str,
    explicit_mode: str | None = None,
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
    risks = resolve_risk_checks(profile, request, mode)
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
        "contract": contract,
        "metaskills": {
            "pre_production": [item for item in pre if item["package"] == "metaskills"],
            "post_production": [item for item in post if item["package"] == "metaskills"],
        },
        "teaching": {
            "pre_production": [item for item in pre if item["package"] == "teaching"],
            "post_production": [item for item in post if item["package"] == "teaching"],
        },
        "risk_checks": risks,
        "completion_gate": completion_gate,
    }


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

    passed = not missing and not unresolved_risks
    return {
        "passed": passed,
        "missing_required_checks": missing,
        "unresolved_risk_checks": unresolved_risks,
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
    if not library.is_dir():
        problems.append(f"library not found: {library}")
        return problems

    known = _frontmatter_object_ids(library)
    try:
        manifests = discover_runtime_manifests(library)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        problems.append(str(exc)); manifests = []
    if not manifests:
        problems.append("no RUNTIME.yaml metaskill manifests found")
    for path, manifest in manifests:
        if manifest.get("schema_version") != SCHEMA_VERSION:
            problems.append(f"{path}: schema_version must be {SCHEMA_VERSION}")
        for entry in manifest.get("activations") or []:
            if not isinstance(entry, dict) or not entry.get("object_id"):
                problems.append(f"{path}: invalid activation entry")
                continue
            object_id = str(entry["object_id"])
            if object_id not in known:
                problems.append(f"{path}: unknown object_id {object_id}")
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

    resolve = sub.add_parser("resolve")
    resolve.add_argument("--request", required=True)
    resolve.add_argument("--mode")
    resolve.add_argument("--out", type=Path)

    verify = sub.add_parser("verify")
    verify.add_argument("--resolution", type=Path, required=True)
    verify.add_argument("--completion", type=Path, required=True)

    sub.add_parser("doctor")
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
            result = resolve_task(profile, library, args.request, args.mode)
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

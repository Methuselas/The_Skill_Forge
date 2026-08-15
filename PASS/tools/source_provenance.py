#!/usr/bin/env python3
"""Shared helpers for source provenance embedded in PASS cards.

A canonical card has one primary ``reference.source_id`` and may absorb variants
from other sources. Release/attestation code must treat those variant sources as
real provenance without letting a foreign variant addition invalidate the
primary source's accepted contribution.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

import yaml

FRONTMATTER = "---\n"


def parse_card(path: Path) -> tuple[dict[str, Any], str] | None:
    text = path.read_text(encoding="utf-8", errors="strict")
    if not text.startswith(FRONTMATTER):
        return None
    try:
        _empty, front, body = text.split(FRONTMATTER, 2)
    except ValueError:
        return None
    data = yaml.safe_load(front)
    if not isinstance(data, dict):
        return None
    return data, body


def primary_source_id(data: dict[str, Any]) -> str | None:
    reference = data.get("reference")
    source_id = reference.get("source_id") if isinstance(reference, dict) else None
    return str(source_id) if source_id else None


def variant_source_ids(data: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for variant in data.get("variants") or []:
        if not isinstance(variant, dict):
            continue
        source_id = variant.get("source_id")
        if source_id:
            result.add(str(source_id))
    return result


def card_source_ids(data: dict[str, Any]) -> set[str]:
    result = variant_source_ids(data)
    source_id = primary_source_id(data)
    if source_id:
        result.add(source_id)
    return result


def source_variant_ids(data: dict[str, Any], source_id: str) -> set[str]:
    result: set[str] = set()
    for variant in data.get("variants") or []:
        if not isinstance(variant, dict) or str(variant.get("source_id")) != source_id:
            continue
        variant_id = variant.get("variant_id")
        if variant_id:
            result.add(str(variant_id))
    return result


def _normalize_body(body: str) -> str:
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in body.split("\n")]
    return "\n".join(lines).strip() + "\n"


def _source_scoped_body(data: dict[str, Any], body: str, source_id: str) -> str:
    """Remove prose paragraphs that belong only to foreign variants.

    PASS_SCHEMA requires every populated variant_id to appear in ``## Notes``.
    That gives us a durable marker for separating absorbed variant prose from the
    owner card body. If a paragraph mixes local and foreign variant ids, keep it:
    the contribution is then genuinely interdependent and should stale together.
    """
    local_ids = source_variant_ids(data, source_id)
    foreign_ids: set[str] = set()
    for variant in data.get("variants") or []:
        if not isinstance(variant, dict) or str(variant.get("source_id")) == source_id:
            continue
        variant_id = variant.get("variant_id")
        if variant_id:
            foreign_ids.add(str(variant_id))
    if not foreign_ids:
        return _normalize_body(body)

    paragraphs = re.split(r"\n[ \t]*\n", body.replace("\r\n", "\n").replace("\r", "\n"))
    kept: list[str] = []
    for paragraph in paragraphs:
        has_foreign = any(variant_id in paragraph for variant_id in foreign_ids)
        has_local = any(variant_id in paragraph for variant_id in local_ids)
        if has_foreign and not has_local:
            continue
        kept.append(paragraph)
    return _normalize_body("\n\n".join(kept))


def source_projection(data: dict[str, Any], body: str, source_id: str) -> dict[str, Any]:
    """Return the canonical card projection whose meaning is relevant to source_id.

    The base card remains part of every attached variant's context. Only variants
    from unrelated sources (and their Notes paragraphs) are removed. Therefore:

    * adding source B's variant does not stale source A;
    * editing source A's own base prose still stales A and attached variants;
    * editing source B's variant metadata/prose stales B;
    * changing the base rule stales all variants that depend on that rule.
    """
    if source_id not in card_source_ids(data):
        raise ValueError(f"card does not cite source {source_id}")
    projected = copy.deepcopy(data)
    variants = projected.get("variants")
    if isinstance(variants, list):
        projected["variants"] = [
            variant for variant in variants
            if isinstance(variant, dict) and str(variant.get("source_id")) == source_id
        ]
    return {
        "frontmatter": projected,
        "body": _source_scoped_body(data, body, source_id),
    }


def source_projection_sha256(path: Path, source_id: str) -> str:
    parsed = parse_card(path)
    if parsed is None:
        raise ValueError(f"{path}: not a PASS card")
    data, body = parsed
    projection = source_projection(data, body, source_id)
    blob = json.dumps(
        projection,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=str,
    ).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def source_object_hashes(library: Path, source_id: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(library.rglob("*.md")):
        parsed = parse_card(path)
        if parsed is None:
            continue
        data, _body = parsed
        if source_id not in card_source_ids(data):
            continue
        result[path.relative_to(library).as_posix()] = source_projection_sha256(path, source_id)
    return result


def all_source_object_hashes(library: Path) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for path in sorted(library.rglob("*.md")):
        parsed = parse_card(path)
        if parsed is None:
            continue
        data, _body = parsed
        rel = path.relative_to(library).as_posix()
        for source_id in sorted(card_source_ids(data)):
            result.setdefault(source_id, {})[rel] = source_projection_sha256(path, source_id)
    return result


def legacy_primary_source_object_hashes(library: Path, source_id: str) -> dict[str, str]:
    """Schema-v1 attestation semantics: whole-file hashes for primary-source cards."""
    result: dict[str, str] = {}
    for path in sorted(library.rglob("*.md")):
        parsed = parse_card(path)
        if parsed is None:
            continue
        data, _body = parsed
        if primary_source_id(data) != source_id:
            continue
        h = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1 << 20), b""):
                h.update(chunk)
        result[path.relative_to(library).as_posix()] = h.hexdigest()
    return result


def source_ids_for_cards(cards: Iterable[dict[str, Any]]) -> set[str]:
    result: set[str] = set()
    for data in cards:
        result.update(card_source_ids(data))
    return result

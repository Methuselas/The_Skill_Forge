#!/usr/bin/env python3
"""Plan or prune transient PASS authoring render caches.

Render pages are working evidence, not canonical accepted knowledge. A source's
render cache is eligible for removal only when SOURCE.md records status=complete
and its current QUALITY_ATTESTATION.json verifies against the canonical library
and grounding ledger. Active, incomplete, missing-attestation, or stale sources
are preserved.

Use --root on a handoff/staging copy when you want to omit eligible renders from
an exported archive without deleting a local working cache.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

from paths import default_ledger_root, default_library_root, repo_root_from_tool
from quality_attestation import verify_attestation
from source_provenance import all_source_object_hashes


def source_status(source_md: Path) -> str | None:
    if not source_md.is_file():
        return None
    for line in source_md.read_text(encoding="utf-8", errors="strict").splitlines():
        if line.strip().startswith("status:"):
            return line.split(":", 1)[1].strip().casefold() or None
    return None


def dir_size(path: Path) -> int:
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def plan(render_root: Path, library: Path, ledger: Path) -> list[dict[str, Any]]:
    if not render_root.exists():
        return []
    if not render_root.is_dir():
        raise ValueError(f"render root is not a directory: {render_root}")
    all_objects = all_source_object_hashes(library)
    rows: list[dict[str, Any]] = []
    for render_dir in sorted(p for p in render_root.iterdir() if p.is_dir()):
        source_id = render_dir.name
        source_dir = ledger / source_id
        status = source_status(source_dir / "SOURCE.md")
        reasons: list[str] = []
        if status != "complete":
            reasons.append(f"source status is {status or 'missing'}")
        attestation_problems = verify_attestation(
            source_id, library, ledger, all_objects.get(source_id, {})
        )
        if attestation_problems:
            reasons.extend(attestation_problems)
        eligible = not reasons
        rows.append(
            {
                "source_id": source_id,
                "path": str(render_dir),
                "bytes": dir_size(render_dir),
                "eligible": eligible,
                "action": "remove" if eligible else "preserve",
                "reasons": reasons,
            }
        )
    return rows


def main() -> int:
    repo = repo_root_from_tool().resolve()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=repo / "workspace" / "authoring" / "renders",
        help="render-cache root; point this at a staging/handoff copy for non-destructive export cleanup",
    )
    parser.add_argument("--library", type=Path, default=default_library_root())
    parser.add_argument("--ledger", type=Path, default=default_ledger_root())
    parser.add_argument("--apply", action="store_true", help="delete eligible cache directories")
    parser.add_argument("--json", action="store_true", help="emit machine-readable report")
    args = parser.parse_args()

    try:
        rows = plan(args.root.resolve(), args.library.resolve(), args.ledger.resolve())
        if args.apply:
            for row in rows:
                if row["eligible"]:
                    shutil.rmtree(Path(row["path"]))
        eligible_bytes = sum(row["bytes"] for row in rows if row["eligible"])
        report = {
            "render_root": str(args.root.resolve()),
            "cache_count": len(rows),
            "eligible_count": sum(1 for row in rows if row["eligible"]),
            "eligible_bytes": eligible_bytes,
            "applied": bool(args.apply),
            "caches": rows,
        }
        if args.json:
            print(json.dumps(report, indent=2))
        else:
            print(
                f"PASS: {report['eligible_count']}/{report['cache_count']} render cache(s) eligible; "
                f"{eligible_bytes} bytes {'removed' if args.apply else 'removable'}"
            )
            for row in rows:
                reason = "; ".join(row["reasons"]) if row["reasons"] else "closed + valid attestation"
                print(f"- {row['source_id']}: {row['action']} ({row['bytes']} bytes) — {reason}")
        return 0
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

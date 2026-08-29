#!/usr/bin/env python3
"""Grade produced gateway.cpp implementations against six mechanical assertions.

Every assertion is objectively checkable against the produced files. None of them
asks whether the code is good — that is not something a regex can answer, and
pretending otherwise is how an eval starts measuring its own author's taste.

Usage:
    python grade.py runs/iteration-1

Expects a layout of:
    <root>/<arm>/<run>/gateway.cpp
    <root>/<arm>/<run>/notes.md

Writes <root>/grades.json and prints a per-run table.
"""

from __future__ import annotations

import json
import os
import re
import sys


def read(path: str) -> str:
    try:
        return open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return ""


def assess(code: str, notes: str) -> dict[str, dict]:
    """Return {assertion_id: {passed, evidence}}."""
    both = code + "\n" + notes
    results: dict[str, dict] = {}

    def record(key: str, passed: bool, evidence: str) -> None:
        results[key] = {"passed": bool(passed), "evidence": evidence[:200]}

    # A1 — the raw GATEWAY pointers in the list are heap-allocated, so something
    # must release them. Look for a delete reached from the shutdown path.
    m = re.search(r"gwShutDown[^{]*\{(.{0,1200}?)\n\}", code, re.S)
    shutdown_body = m.group(1) if m else ""
    a1 = bool(re.search(r"\bdelete\b|\bfree\s*\(|\.reset\(|unique_ptr|shared_ptr", shutdown_body)) or bool(
        re.search(r"\bdelete\b|\bfree\s*\(", code)
    )
    record("A1_ownership", a1, (shutdown_body[:120] or "no gwShutDown body matched"))

    # A2 — smallest-first normalisation of the coordinate pair. Only discoverable
    # outside the header.
    a2_pat = (
        r"std::swap\s*\(\s*x1\s*,\s*x2|std::swap\s*\(\s*y1\s*,\s*y2"
        r"|x1\s*>\s*x2|y1\s*>\s*y2"
        r"|std::min\s*\(\s*x1\s*,\s*x2|std::max\s*\(\s*x1\s*,\s*x2"
        r"|std::minmax"
    )
    m2 = re.search(a2_pat, code)
    record("A2_reorder", bool(m2), m2.group(0) if m2 else "no smallest-first normalisation")

    # A3 — clamp to map bounds.
    # A clamp ASSIGNS a coordinate from a bounding expression. A validating
    # assert also mentions width and height and is not a clamp, so the
    # assignment is the thing to match. Template arguments are optional:
    # std::max<int>(...) is as common as std::max(...).
    a3_pat = (
        r"(x1|x2|y1|y2)\s*=\s*(std::)?(max|min|clamp)"
        r"|(x1|x2|y1|y2)\s*=\s*(MAX|MIN)"
        r"|(x1|x2|y1|y2)\s*=\s*\w*[Cc]lamp"
    )
    m3 = re.search(a3_pat, code)
    record("A3_clamp", bool(m3), m3.group(0) if m3 else "no clamp against map bounds")

    # A4 — direct evidence the run went outside the header. Cites a caller by
    # name, or the reorder/clamp comment that lives at a call site.
    a4_pat = (
        r"gamestate_serialize|game\.cpp|map\.cpp|init\.cpp"
        r"|call ?site|caller|reorder|clamp"
    )
    m4 = re.search(a4_pat, notes, re.I)
    record("A4_read_callsites", bool(m4), m4.group(0) if m4 else "notes cite no call site")

    # A5 — an invariant made checkable rather than assumed.
    m5 = re.search(r"\bASSERT\w*\s*\(|\bassert\s*\(|static_assert", code)
    record("A5_invariant", bool(m5), m5.group(0) if m5 else "no assertion present")

    # A6 — used the declared list type rather than substituting a container.
    a6 = bool(re.search(r"GATEWAY_LIST|std::list\s*<\s*GATEWAY", code))
    substituted = bool(re.search(r"std::vector\s*<\s*GATEWAY|std::deque\s*<\s*GATEWAY", code))
    record("A6_house_idiom", a6 and not substituted,
           "GATEWAY_LIST used" if a6 else "declared list type not used")

    return results


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = sys.argv[1]
    if not os.path.isdir(root):
        print(f"no such directory: {root}")
        return 2

    graded = []
    for arm in sorted(os.listdir(root)):
        arm_dir = os.path.join(root, arm)
        if not os.path.isdir(arm_dir):
            continue
        for run in sorted(os.listdir(arm_dir)):
            run_dir = os.path.join(arm_dir, run)
            if not os.path.isdir(run_dir):
                continue
            code = read(os.path.join(run_dir, "gateway.cpp"))
            notes = read(os.path.join(run_dir, "notes.md"))
            if not code:
                print(f"  !! {arm}/{run}: no gateway.cpp produced — recorded as all-fail")
            graded.append({
                "arm": arm,
                "run": run,
                "produced": bool(code),
                "assertions": assess(code, notes),
            })

    out = os.path.join(root, "grades.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(graded, fh, indent=2)

    if graded:
        keys = list(graded[0]["assertions"].keys())
        print(f"{'arm':<10}{'run':<8}" + "".join(f"{k.split('_')[0]:>6}" for k in keys) + "   passed")
        print("-" * (18 + 6 * len(keys) + 10))
        for g in graded:
            marks = "".join("     Y" if g["assertions"][k]["passed"] else "     ." for k in keys)
            n = sum(1 for k in keys if g["assertions"][k]["passed"])
            print(f"{g['arm']:<10}{g['run']:<8}{marks}   {n}/{len(keys)}")
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

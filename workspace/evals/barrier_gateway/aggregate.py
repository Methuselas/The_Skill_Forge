#!/usr/bin/env python3
"""Aggregate graded runs into mean +/- stddev per assertion, with the arm delta.

A single run of either arm proves nothing. This reports the spread so a reader
can see whether the arms are actually separated or merely different on one run.

Usage:
    python aggregate.py runs/iteration-1
"""

from __future__ import annotations

import json
import os
import statistics
import sys


def spread(values: list[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    mean = statistics.mean(values)
    sd = statistics.stdev(values) if len(values) > 1 else 0.0
    return mean, sd


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = sys.argv[1]
    grades_path = os.path.join(root, "grades.json")
    if not os.path.isfile(grades_path):
        print(f"no grades.json in {root} — run grade.py first")
        return 2

    graded = json.load(open(grades_path, encoding="utf-8"))
    if not graded:
        print("no runs graded")
        return 2

    arms = sorted({g["arm"] for g in graded})
    keys = list(graded[0]["assertions"].keys())

    per_arm: dict[str, dict[str, list[float]]] = {
        a: {k: [] for k in keys} for a in arms
    }
    totals: dict[str, list[float]] = {a: [] for a in arms}

    for g in graded:
        passed = 0
        for k in keys:
            v = 1.0 if g["assertions"][k]["passed"] else 0.0
            per_arm[g["arm"]][k].append(v)
            passed += v
        totals[g["arm"]].append(passed / len(keys))

    width = max(len(k) for k in keys) + 2
    header = f"{'assertion':<{width}}" + "".join(f"{a:>18}" for a in arms)
    if len(arms) == 2:
        header += f"{'delta':>10}"
    print(header)
    print("-" * len(header))

    for k in keys:
        row = f"{k:<{width}}"
        means = []
        for a in arms:
            m, sd = spread(per_arm[a][k])
            means.append(m)
            row += f"{m*100:>11.0f}% ±{sd*100:<4.0f}"
        if len(arms) == 2:
            row += f"{(means[1]-means[0])*100:>+9.0f}%"
        print(row)

    print("-" * len(header))
    row = f"{'OVERALL':<{width}}"
    means = []
    for a in arms:
        m, sd = spread(totals[a])
        means.append(m)
        row += f"{m*100:>11.0f}% ±{sd*100:<4.0f}"
    if len(arms) == 2:
        row += f"{(means[1]-means[0])*100:>+9.0f}%"
    print(row)

    n = {a: len(totals[a]) for a in arms}
    print(f"\nruns per arm: {n}")
    print("A delta smaller than the standard deviations either side of it is not an")
    print("effect. With three runs per arm, only a large separation is readable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Lane repair — Writing — COMPLETE

Written 2026-08-23 as a handoff. Superseded the same day: the Writing lane did
the repair in commits `13fddfc`, `845887f`, and `cfa1ab9` while it was being
written. This file is kept as the record rather than deleted, because the
before/after numbers are the only trace the work leaves.

## What the handoff found

Not one of the 22 Writing APs claimed a single Pattern. Every `supports` edge in
the lane originated on a Pattern or a Drill, never on an AP. `related_to` was 92%
of all edges — the highest of the three lanes, an almost pure undirected
adjacency graph.

It was never a content problem. All 22 APs already listed the right Patterns —
168 edges — typed `related_to`, which cannot express authority.

## Result

| | before | after |
|---|---|---|
| patterns claimed by an AP | 0 of 131 (0%) | **100 of 134 (75%)** |
| `supports` edges | 24 (none from an AP) | **176** |
| APs naming owners in step prose | 0 of 22 | **22 of 22** |

75% is the highest of the three lanes, and every AP names its owners in prose.
This lane is now the reference implementation of the convention in
`PASS/docs/PASS_RUN.md` §2.7, ahead of both software-engineering (29%) and art.

## For comparison, at the same date

```
writing                22 APs   134 patterns    75% claimed   22/22 APs name owners
software-engineering   26 APs   462 patterns    29% claimed   24/26 APs name owners
art                    35 APs   222 patterns    27% claimed   25/35 APs name owners
```

The remaining 34 unclaimed Writing patterns are the honest residue the handoff
predicted: local decisions that fire on their own IF clause and need no
sequencing, plus any genuine AP coverage gap. Neither needs manufacturing an AP
to fix.

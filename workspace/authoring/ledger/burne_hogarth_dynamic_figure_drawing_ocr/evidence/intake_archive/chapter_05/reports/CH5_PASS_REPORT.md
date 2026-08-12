# Dynamic Figure Drawing — Chapter 5 Targeted PASS Report

status: **PASS (targeted), candidate hold**  
session: `hogarth-dfd-ch05-2026-08-07`  
baseline golden SHA-256: `4c4cc9eb9a08c8659263c78e86ea2ce0b52e0b2f4a4998374633b67e5a8bfb48`

## Routing decision

**Targeted PASS, not Deep PASS.**

Chapter 5 is reinforcement-heavy. The source adds a complementary control to Chapter 4: projected length can vary radically in depth, so Hogarth uses a joint as pivot and the member as a constant radius to test possible endpoints. The later triangle and body-contact devices simplify that same problem rather than opening a new foundation domain.

The user's teaching narrows the practical value further: **range-of-motion / wonky-anatomy correction**.

## Extraction

Created:
- 1 new Pattern candidate — limb reach from joint pivots;
- 1 new correction Drill — repair a wonky foreshortened limb with temporary pivot arcs;
- 1 patch proposal — connect Chapter 4 width identity to Chapter 5 projected-reach control.

Held:
- no Chapter 5 AP;
- no separate ellipse Pattern;
- no separate isosceles-triangle Pattern;
- no visual reference;
- no canonical commit before Chapter 6 reconciliation.

## Why this is deliberately small

The baseline already knows articulated limb chains, Stage 2 mass construction, constant-width identity, overlap, and joint continuity. Separate cards for every measuring scaffold would duplicate capability and increase resolver/context cost. The source itself warns that technical ellipse dependence can inhibit the drawing.

## Practical regression target

This candidate should help with failures where a figure has:
- a limb that feels stretched or compressed beyond plausible reach;
- a knee/elbow endpoint that cannot be traced back to its socket;
- a duplicated or exchanged limb path under severe foreshortening;
- anatomy rendered over an impossible skeleton.

It is **not** expected to solve architectural perspective or whole-scene projection; that remains Chapter 6 / later perspective-study territory.

## Commit status

Mechanical validation may pass now, but canonical commit is intentionally held until Chapter 6 because Chapter 6 may supply a more general whole-figure projection method that absorbs or reorganizes this local diagnostic.

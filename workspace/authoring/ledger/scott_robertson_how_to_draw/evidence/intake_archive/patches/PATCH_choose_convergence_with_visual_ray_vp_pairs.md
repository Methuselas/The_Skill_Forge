# Patch Proposal — Derive Coupled Vanishing Pairs With the Visual Ray Method

**Target:** `PAT_choose_convergence_from_view_and_orientation`

**Disposition:** candidate patch proposal only; target card remains byte-unchanged.

## Proposed addition
For an exact horizontal direction family, use Robertson's top-view Visual Ray Method: draw a ray through the Station Point parallel to the world direction; where that ray meets the Picture Plane/horizon construction determines the vanishing destination for that parallel family. For perpendicular horizontal families, keep the two station-point rays at 90 degrees and rotate them **together** around the Station Point to derive new coupled VP pairs as the object/grid rotates.

This gives an exact version of Norling's useful observation that the two horizontal vanishing points move as a pair when the world orientation changes.

## Evidence
Scott Robertson with Thomas Bertling, *How to Draw*, printed pp. 24-25 (physical PDF pp. 22-23).

## Cumulative effect
If committed, this should subsume Norling's coupled-VP patch as the more explicit construction while preserving Norling's plain-language runtime intuition.

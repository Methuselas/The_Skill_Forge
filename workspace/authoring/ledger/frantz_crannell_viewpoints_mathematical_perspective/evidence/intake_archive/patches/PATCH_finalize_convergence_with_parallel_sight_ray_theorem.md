# Patch Proposal — Finalize Coupled Vanishing-Point Construction With the Parallel Sight-Ray Theorem

**Target:** `PAT_choose_convergence_from_view_and_orientation`

**Disposition after Viewpoints:** **VARIANT — finalize** `VAR_derive_coupled_vps_with_visual_rays` (Robertson), with the mathematical rule made explicit internally.

## Proposed addition
For any real line direction that is not parallel to the Picture Plane, the direction's vanishing point is where a sight ray from the station point **parallel to that world direction** intersects the Picture Plane. Parallel world lines therefore share a vanishing point.

For orthogonal horizontal directions in a standard two-point setup, the sight rays from the station point to the two vanishing points meet at 90 degrees. This is why the two VPs are coupled by the camera rather than independently draggable stylistic handles.

## Evidence
Frantz & Crannell, *Viewpoints*, Theorem 3.1 (printed pp. 30-31) and Theorem 5.1 (printed pp. 61-62).

## Cumulative effect
Norling's "the VPs move together" intuition and Robertson's Visual Ray Method become two levels of the same rule: plain-language mental model above, exact sight-ray construction below. No new foundation card is needed.

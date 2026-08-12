# Patch Proposal — Coupled Horizontal Vanishing-Point Movement

**Target:** `PAT_choose_convergence_from_view_and_orientation`

**Disposition:** candidate patch proposal only; target card remains byte-unchanged.

## Proposed addition
When an object with perpendicular horizontal directions rotates relative to a fixed viewer, its two horizontal vanishing points are coupled. As one direction turns closer to the center of view, its vanishing point moves inward while the perpendicular direction's vanishing point moves outward. Treat the pair as consequences of one viewer/object orientation, not two independently placed compositional handles.

## Evidence
Ernest Norling, *Perspective Made Easy*, printed pp. 59-65. Norling demonstrates the relationship with perpendicular arm directions and a tacked-paper rotation model.

## Why patch rather than new card
The existing D'Amelio Pattern already says convergence follows view and orientation; Norling improves the mental model and diagnostic.

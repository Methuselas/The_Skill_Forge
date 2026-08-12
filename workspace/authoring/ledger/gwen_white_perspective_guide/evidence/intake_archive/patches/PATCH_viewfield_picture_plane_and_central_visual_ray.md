# Patch Proposal — Make the Picture Plane / Central Visual Ray an Optional Exact Camera Model

**Target:** `PAT_establish_eye_level_and_vanishing_directions`

**Disposition:** candidate patch proposal only; target card remains byte-unchanged.

## Proposed addition
Add an optional exact setup for tasks that need camera reconstruction, plan projection, or distortion diagnosis: represent the viewer by an eye/station point `E`; place a Picture Plane between viewer and scene; define the Central Visual Ray as perpendicular to that plane; its intersection is the Centre of Vision; and the horizontal eye-level/horizon passes through the Centre of Vision for a level picture plane. The Picture Plane is the projection surface, not another object plane in the scene.

Keep the simple artist-facing rule resident for normal drawing. Load the Picture Plane / Centre-of-Vision model only when the task actually needs exact camera geometry.

## Evidence
Gwen White, *Perspective*, printed pp. 4-7 (PDF pp. 5-8).

## Why patch rather than new card
The cumulative baseline already establishes eye level, vanishing directions, and exact plan projection. White supplies a cleaner geometric model linking those parts rather than a separate everyday capability.

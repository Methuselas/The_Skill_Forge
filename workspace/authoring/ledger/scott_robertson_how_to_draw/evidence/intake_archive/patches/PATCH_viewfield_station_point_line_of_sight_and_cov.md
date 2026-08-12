# Patch Proposal — Station Point, Line of Sight, and Cone of Vision as the Exact Viewfield Branch

**Target:** `PAT_establish_eye_level_and_vanishing_directions`

**Disposition:** candidate patch proposal only; target card remains byte-unchanged.

## Proposed addition
Merge and strengthen White's optional Picture Plane / Central Visual Ray branch with Robertson's viewing-position vocabulary. When exact setup, camera reconstruction, or distortion diagnosis is needed, define:

- **Station Point:** eye/camera location and height;
- **Line of Sight:** view direction, including upward/downward incline;
- **Picture Plane:** projection surface, perpendicular to the Line of Sight in Robertson's setup;
- **Cone of Vision / field of view:** the angular field being asked to fit on that projection;
- **Horizon:** tied to station-point height for a level view, while tilting the Line of Sight creates vertical convergence without changing the viewer's physical height.

Keep the ordinary eye-level rule resident; load this exact camera branch only when it solves a concrete problem.

## Evidence
Scott Robertson with Thomas Bertling, *How to Draw*, printed pp. 22-27 (physical PDF pp. 20-25), especially “Defining the Perspective by the Viewing Position,” “Cone of Vision,” and “Horizon Line Relative to Position.”

## Cumulative effect
If committed, this patch should absorb White's `PATCH_viewfield_picture_plane_and_central_visual_ray.md` rather than creating two parallel camera models.

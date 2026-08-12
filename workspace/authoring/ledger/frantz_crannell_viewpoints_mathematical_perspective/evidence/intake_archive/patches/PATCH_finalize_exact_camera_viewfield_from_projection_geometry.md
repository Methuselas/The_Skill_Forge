# Patch Proposal — Finalize Exact Camera/Viewfield Setup From Projection Geometry

**Target:** `PAT_establish_eye_level_and_vanishing_directions`

**Disposition after Viewpoints:** **VARIANT — finalize** `VAR_exact_camera_viewfield_setup`.

## Proposed variant
Use an exact setup only when camera reconstruction, plan projection, severe distortion diagnosis, or a tilted/three-point view actually requires it.

- Represent the eye/station point by `E` and the Picture Plane as the projection surface.
- The **viewing target / Centre of Vision** is the point where the perpendicular from `E` meets the Picture Plane; the **viewing distance** is the perpendicular distance from `E` to that plane.
- Every image point is the intersection of the Picture Plane with the sight ray from `E` through the corresponding world point. In the coordinate setup used by *Viewpoints*, this gives the internal projection scale `d/(z+d)`; the formula may stay downstairs and need not be shown during normal drawing.
- For a level/vertical Picture Plane, retain the ordinary eye-level/horizon construction already taught by the artist-facing books.
- Do **not** carry the chapter-5 horizontal-horizon mnemonic unchanged into arbitrary three-point/tilted-picture-plane cases. When all three orthogonal axes converge, hand off exact validation to `PAT_validate_three_point_viewpoint_geometry` instead of inventing a horizontal line by habit.
- Do not attach a universal numeric Cone-of-Vision limit to this variant.

## Evidence
- Frantz & Crannell, *Viewpoints*, printed pp. 13-15: Perspective Theorem / sight-ray intersection with the Picture Plane.
- Printed pp. 59-64: eye-level plane and exact station-point geometry for standard two-point perspective.
- Printed pp. 86-93: arbitrary three-point viewpoint geometry and orthocenter viewing target.
- White and Robertson prior patches remain useful artist-facing vocabulary/procedures and are absorbed as provenance.

## Cumulative effect
White's Picture Plane/Central Visual Ray patch and Robertson's Station Point/Line of Sight patch are no longer provisional. Their exact geometry is validated as the optional camera branch. The unresolved part is narrowed: there is no need for a universal COV number, and the ellipse-axis theorem is unrelated and remains separate.

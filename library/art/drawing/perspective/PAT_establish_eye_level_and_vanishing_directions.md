---
object_id: PAT_establish_eye_level_and_vanishing_directions
object_type: pattern
name: Establish Eye Level and Vanishing Directions
library_path:
- art
- drawing
- perspective
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- perspective
- eye_level
- vanishing_point
- horizon
cross_links: []
reference:
  source_id: joseph_damelio_perspective_drawing_handbook
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
  publish_date: 1964 / 2004
  media_type: book
  locator: u00, printed pp. 23-32
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_high_water_eye_level_diagnostic
  variant_name: Use a High-Water Eye-Level Diagnostic
  variant_basis: method_sequence
  source_id: ernest_norling_perspective_made_easy
  source_title: Perspective Made Easy
  locator: printed pp. 13-19
  difference_from_foundation: 'Adds a fast perceptual check after formal eye-level setup: features above eye level expose undersides, those below expose tops, and forms at eye level flatten toward edge-on.'
  when_to_use: Use as a quick diagnostic for upright forms after the eye level is established.
  when_not_to_use: Do not substitute the mnemonic for exact camera geometry when the picture plane is tilted or the setup is three-point.
  absorbed_from_object_id: none
- variant_id: VAR_exact_camera_viewfield_setup
  variant_name: Use Exact Camera/Viewfield Geometry
  variant_basis: method_sequence
  source_id: frantz_crannell_viewpoints_mathematical_perspective
  source_title: Viewpoints
  locator: printed pp. 13-15, 59-64, 86-93
  difference_from_foundation: Finalizes White and Robertson camera-model patches with station point, picture plane, viewing target, viewing distance, and sight-ray projection; fixed numeric cone-of-vision limits remain unpromoted.
  when_to_use: Use for camera reconstruction, plan projection, severe distortion diagnosis, or exact tilted/three-point setup.
  when_not_to_use: Do not burden ordinary perspective drawing with exact station geometry when the simpler eye-level construction is sufficient.
  absorbed_from_object_id: none
---

# Establish Eye Level and Vanishing Directions

## Pattern Rule
**IF** a scene contains sets of parallel directions receding in depth, **THEN** establish the observer's eye level and give each receding parallel family its own vanishing point; horizontal-world families place their vanishing points on the eye-level line.

## Do
- Mark the eye level before solving repeated horizontal directions.
- Group edges by the real direction they share, then converge each group toward one common vanishing point.
- Keep different direction families separate; a scene may need several vanishing points.
- Let the eye-level line move upward in the picture when looking downward and downward when looking upward; it may lie outside the frame.
- Use a visible natural horizon as the eye-level line when the source view supplies one.

## Don't
- Give unrelated sets of parallels one vanishing point merely because they are all horizontal in the world.
- Place the horizon by composition habit and then force the geometry to fit it.
- Assume the eye-level line must be visible inside the drawing.

## Checklist
- Every repeated receding direction has a consistent vanishing destination.
- All horizontal-world vanishing points lie on one eye-level line.
- The amount of top or underside visible agrees with the chosen eye level.
- Looking up, down, or straight out produces the expected shift in the eye-level line.

## Notes
D'Amelio treats vanishing points and eye level as practical aids derived from lines of sight, not as arbitrary drawing conventions.

**Boundaries**
This Pattern establishes the principal perspective field. It does not by itself measure intervals, construct inclined planes, or solve cast shadows.

Variants retained in this canonical object: `VAR_high_water_eye_level_diagnostic`, `VAR_exact_camera_viewfield_setup`.

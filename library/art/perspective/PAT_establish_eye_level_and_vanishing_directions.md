---
object_id: PAT_establish_eye_level_and_vanishing_directions
object_type: pattern
name: Establish Eye Level and Vanishing Directions
library_path:
- art
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
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants:
- variant_id: VAR_high_water_eye_level_diagnostic
  variant_name: Use a High-Water Eye-Level Diagnostic
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a fast perceptual check after formal eye-level setup: features above eye level expose
    undersides, those below expose tops, and forms at eye level flatten toward edge-on.'
  when_to_use: Use as a quick diagnostic for upright forms after the eye level is established.
  when_not_to_use: Do not substitute the mnemonic for exact camera geometry when the picture plane is tilted or the setup
    is three-point.
  absorbed_from_object_id: none
- variant_id: VAR_exact_camera_viewfield_setup
  variant_name: Use Exact Camera/Viewfield Geometry
  variant_basis: method_sequence
  difference_from_foundation: Finalizes White and Robertson camera-model patches with station point, picture plane, viewing
    target, viewing distance, and sight-ray projection; fixed numeric cone-of-vision limits remain unpromoted.
  when_to_use: Use for camera reconstruction, plan projection, severe distortion diagnosis, or exact tilted/three-point setup.
  when_not_to_use: Do not burden ordinary perspective drawing with exact station geometry when the simpler eye-level construction
    is sufficient.
  absorbed_from_object_id: none
- variant_id: VAR_dodson_estimate_off_page_vanishing_pull_for_freehand_sketching
  variant_name: Estimate Off-Page Vanishing Pull for Freehand Sketching
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a sketching route for views whose vanishing points fall far outside the page: keep the
    eye level and likely convergence destination mentally, sight the sloping edges against level/vertical, draw by eye, then
    use the implied vanishing pull to restate inconsistent angles.'
  when_to_use: Use for freehand observational or exploratory sketching when constructing a large exact perspective field would
    be cumbersome and approximate spatial coherence is sufficient.
  when_not_to_use: Do not use the estimate in place of exact vanishing-point or station-point construction when technical
    accuracy, repeated measurements, or severe distortion control is required.
  absorbed_from_object_id: none
- variant_id: VAR_eissen_derive_eye_level_product_view_from_high_view_layout
  variant_name: Derive an Eye-Level Product View From a Higher-View Layout
  variant_basis: method_sequence
  difference_from_foundation: Transforms an already solved high-view product layout into an eye-level view by establishing
    an eye-height slice and new horizon, preserving useful vertical dimensions and horizontal placement relationships, rebuilding
    the largest silhouette limits around that slice, then reconnecting secondary structure with sufficient convergence to
    communicate scale before validating both constructively and visually.
  when_to_use: Use during exploratory product sketching when a high or bird-like construction already contains useful proportion
    and plan information but a more human eye-level presentation is needed quickly.
  when_not_to_use: Do not treat the shortcut as exact camera reconstruction, and do not preserve screen-space measurements
    that should change under a materially different station point or projection. Rebuild the perspective field when technical
    precision is required.
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
Vanishing points and eye level are practical aids derived from lines of sight, not arbitrary drawing conventions.

**Boundaries**
This Pattern establishes the principal perspective field. It does not by itself measure intervals, construct inclined planes, or solve cast shadows.

Variants retained in this canonical object: `VAR_high_water_eye_level_diagnostic`, `VAR_exact_camera_viewfield_setup`.
Variants retained in this canonical object: `VAR_dodson_estimate_off_page_vanishing_pull_for_freehand_sketching`.
`VAR_eissen_derive_eye_level_product_view_from_high_view_layout` adds a bounded exploratory transformation from a useful higher-view layout toward eye level; it preserves design information where practical but yields to a fresh camera construction whenever exact station geometry matters.

`VAR_eissen_derive_eye_level_product_view_from_high_view_layout` should start with the largest dimensions. Establish the eye-height slice and new horizon first, preserve useful placement relationships from the solved high view, reconnect the major limits above and below eye level, and only then resolve smaller structure. For a large subject, convergence must be strong enough that the transformed eye-level view actually reads at the intended scale.

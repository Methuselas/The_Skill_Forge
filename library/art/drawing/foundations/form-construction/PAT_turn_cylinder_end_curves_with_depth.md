---
object_id: PAT_turn_cylinder_end_curves_with_depth
object_type: pattern
name: Turn Cylinder End Curves With Depth
library_path:
- art
- drawing
- foundations
- form-construction
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- figure_drawing
- cylinder
- foreshortening
- cross_contour
cross_links:
- rel: related_to
  target_object_id: PAT_project_form_curves_from_camera_view
- rel: related_to
  target_object_id: PAT_hold_member_identity_with_constant_width
reference:
  source_id: burne_hogarth_dynamic_figure_drawing_ocr
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
  publish_date: 1970
  media_type: book
  locator: ch04, printed pp. 105-107 and 120-121
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_vilppu_set_cylinder_axis_before_end_ellipses
  variant_name: Set the Cylinder Axis Before Its End Ellipses
  variant_basis: method_sequence
  source_id: glenn_vilppu_basic_figure_drawing
  source_title: 'Drawing Manual: Basic Figure Drawing'
  locator: u05, physical pp. 57-60
  difference_from_foundation: 'Adds Vilppu''s axis-first cylinder procedure to the existing end-curve Pattern: establish the cylinder''s directional centerline and intended beginning/end first, then place both ellipses perpendicular to that shared axis so the limb or appendage inherits one coherent spatial direction before side contours are connected.'
  when_to_use: Use when a cylindrical limb has plausible end curves individually but twists, kinks, or loses direction because its two ends were solved independently.
  when_not_to_use: Do not keep explicit centerlines and full ellipses after the organic form reads clearly; Vilppu treats cylinders as learning and analysis tools whose logic can become implicit.
  absorbed_from_object_id: none
---
# Turn Cylinder End Curves With Depth

## Pattern Rule
**IF** a cylindrical or barrel-like body mass turns from a side view toward an end-on view
**THEN** make its circular end projection progressively fuller while compressing the visible side length
**ELSE** retain flatter end curves and more visible side length for the more extended view

## Do
- Coordinate both ends of the cylinder so they describe one direction rather than two unrelated ellipses.
- Let an extreme end-on member approach a double-curve or nearly circular statement with little side wall exposed.
- Taper the organic cylinder where the adjoining joint, attachment, or other form requires a narrower end.
- Use cross-curves as diagnostic proof when the direction is uncertain, then let the developed form replace them when it reads unaided.

## Don't
- Keep the same flat end curve while claiming that the member has turned sharply toward the camera.
- Draw a full circle and long parallel sides together when the view cannot support both.
- Treat the geometric cylinder as finished anatomy or design; it is a construction carrier for the later organic form.

## Checklist
- Rounder end curves correspond to a deeper, more frontal view.
- Flatter end curves correspond to a more extended, sideward view.
- Side length, end curvature, taper, and direction all agree.
- The developed organic or designed form can occupy the cylinder without contradicting its perspective.

## Notes
Hogarth's cylinder is a rational simplification, not a compulsory visible scaffold. The dark construction in the thigh demonstration proves that a simplified spatial mass can carry the later organic form. When the organic form will not fit, the construction must be corrected rather than concealed.

`VAR_vilppu_set_cylinder_axis_before_end_ellipses` retains **Set the Cylinder Axis Before Its End Ellipses** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

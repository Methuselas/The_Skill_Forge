---
object_id: PAT_choose_block_in_strategy_by_visual_priority_and_subject_complexity
object_type: pattern
name: Choose Block-In Strategy by Visual Priority and Subject Complexity
library_path:
- art
- drawing
- rendering
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- painting
- block_in
- workflow
- direct_painting
- visual_priority
cross_links:
- rel: related_to
  target_object_id: PAT_preflight_observed_rendering_for_constraints_and_failure_points
- rel: related_to
  target_object_id: PAT_build_loose_surface_from_precise_visual_decisions
reference:
  source_title: 'Alla Prima: Everything I Know About Painting'
  author: Richard Schmid
confidence: high
references: []
variants:
- variant_id: VAR_schmid_use_line_and_mass_when_placement_and_drawing_are_primary
  variant_name: Use Line and Mass When Placement and Drawing Are Primary
  variant_basis: method_sequence
  difference_from_foundation: Establishes major placement and difficult drawing relations with a loose line framework, then adds thin masses; once the arrangement is secure, later passages replace rather than preserve the preliminary line as a sacred contour.
  when_to_use: Use when a complex arrangement, unstable pose, or difficult set of proportions makes placement the dominant early risk.
  when_not_to_use: Do not keep searching with line after the main placement is trustworthy, and do not force a drawing-heavy start when color or mass is the real priority.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_isolate_value_drawing_and_edges_with_monochrome_block_in
  variant_name: Isolate Value, Drawing, and Edges With a Monochrome Block-In
  variant_basis: method_sequence
  difference_from_foundation: Temporarily removes full-color complexity so drawing, value, and edge relationships can be solved in one-color structure before color becomes another variable.
  when_to_use: Use when value organization, drawing accuracy, or edge design is the dominant uncertainty and color is not yet the main problem.
  when_not_to_use: Do not suppress color when the subject's principal event is a fragile harmony that must be established early.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_key_color_harmony_before_exact_drawing
  variant_name: Key Color Harmony Before Exact Drawing
  variant_basis: emphasis
  difference_from_foundation: Establishes the dominant color/light harmony as a broad color field before committing to exact local drawing, while preserving a few measured anchors so the loose color start does not erase placement control.
  when_to_use: Use when a strong, time-sensitive color harmony or illumination event is the main reason for the picture.
  when_not_to_use: Do not use when small drawing relationships are so sensitive that a loose color field would make later placement unnecessarily uncertain.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_resolve_large_full_color_masses_before_minor_detail
  variant_name: Resolve Large Full-Color Masses Before Minor Detail
  variant_basis: method_sequence
  difference_from_foundation: Begins a relatively simple, clearly visualized subject with the major shapes already carrying their intended color, value, and edge character, then subdivides only where the large whole requires more information.
  when_to_use: Use when the subject is simple enough that its broad full-color relationships can be placed accurately without a separate monochrome or line-heavy construction.
  when_not_to_use: Do not confuse this broad-whole route with selective local finish; if placement or structure is uncertain, choose a start that exposes those risks first.
  absorbed_from_object_id: none
---
# Choose Block-In Strategy by Visual Priority and Subject Complexity

## Pattern Rule
**IF** a rendering needs an opening structure before finish and different starting methods would protect different information
**THEN** choose the block-in that resolves the dominant uncertainty or visual priority first—placement, value/edge structure, color harmony, or broad full-color mass—while leaving later decisions flexible
**ELSE** begin directly when no separate block-in would materially improve control.

## Do
- Identify what would be most expensive to discover late: placement, value pattern, color key, edge integration, or another high-risk relationship.
- Use only enough preliminary information to make the chosen route trustworthy; a block-in is scaffolding, not automatically part of the finish.
- Switch from searching to accurate development once the major arrangement has been accepted.
- Let later passages replace temporary lines, masses, or washes when the finished information is more specific.
- Preserve a strong early statement when it already functions as finished surface rather than covering it mechanically because the workflow is called a block-in.

## Don't
- Do not make one successful starting method into a universal personal formula.
- Do not solve color first when drawing is the dominant risk, or drawing first when a fleeting color/light event is the reason for the image.
- Do not keep a preliminary mark merely because it arrived early; only useful final information deserves to survive.

## Checklist
- The opening method directly addresses the picture's dominant early risk or priority.
- Major placement and scale are trustworthy enough for the selected route.
- The block-in contains no more information than later decisions actually need.
- The work can change methods once the original uncertainty has been resolved.

## Notes
Different starts protect different information. The durable skill is choosing the opening representation from the problem rather than from habit. Line-and-mass favors placement, monochrome isolates value/drawing/edges, a color-key start protects harmony, and a broad full-color start can work when the subject is simple and already clearly visualized.

`VAR_schmid_use_line_and_mass_when_placement_and_drawing_are_primary`, `VAR_schmid_isolate_value_drawing_and_edges_with_monochrome_block_in`, `VAR_schmid_key_color_harmony_before_exact_drawing`, and `VAR_schmid_resolve_large_full_color_masses_before_minor_detail` are alternate starts under the same decision owner; choose among them by what must become trustworthy first.

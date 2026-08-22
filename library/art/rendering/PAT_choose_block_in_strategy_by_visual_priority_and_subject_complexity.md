---
object_id: PAT_choose_block_in_strategy_by_visual_priority_and_subject_complexity
object_type: pattern
name: Choose Block-In Strategy by Visual Priority and Subject Complexity
library_path:
- art
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
- rel: related_to
  target_object_id: PAT_unify_palette_with_shared_color_influence
- rel: related_to
  target_object_id: PAT_build_broken_color_as_optical_mixture
- rel: related_to
  target_object_id: PAT_preserve_value_structure_when_translating_tone_into_color
reference:
  source_title: 'Alla Prima: Everything I Know About Painting'
  author: Richard Schmid
confidence: high
references: []
variants:
- variant_id: VAR_schmid_use_line_and_mass_when_placement_and_drawing_are_primary
  variant_name: Use Line and Mass When Placement and Drawing Are Primary
  variant_basis: method_sequence
  difference_from_foundation: Establishes major placement and difficult drawing relations with a light line framework, then
    adds inexpensive masses; the guide lines are temporary boundary controls that later paint should replace rather than mechanically
    fit against. When a live subject is expected to drift, preserve only the minimum contour/centerline registration scaffold
    needed to restore the accepted pose.
  when_to_use: Use when complex placement, an unstable pose, or sensitive proportions make drawing the dominant early risk;
    keep fixed registration guides only when source movement would otherwise destroy the accepted pose.
  when_not_to_use: Do not preserve temporary contours as final hard edges, follow every movement of a drifting subject with
    the guide system, or force a drawing-heavy start when color or mass is the real priority.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_isolate_value_drawing_and_edges_with_monochrome_block_in
  variant_name: Isolate Value, Drawing, and Edges With a Monochrome Block-In
  variant_basis: method_sequence
  difference_from_foundation: Builds a thin, revisable monochrome structural map that can carry drawing, composition, value
    range, and edge relationships close to resolution before full color becomes another variable.
  when_to_use: Use for structurally difficult or complex subjects when drawing, values, composition, or edge organization
    need to become trustworthy before color.
  when_not_to_use: Do not overdevelop a monochrome stage when the subject is simple enough that the extra pass would stiffen
    the result or when a fragile color event must be keyed immediately.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_key_color_harmony_before_exact_drawing
  variant_name: Key Color Harmony Before Exact Drawing
  variant_basis: emphasis
  difference_from_foundation: Begins with a broad or broken color field whose first job is to capture the dominant light/temperature
    key, then establishes critical drawing anchors before the color maze becomes too ambiguous and preserves the original
    color-family relation through later development.
  when_to_use: Use when light/color is the primary event, when the subject breaks into many small color notes, or when boundaries
    are naturally soft and fragmented.
  when_not_to_use: Do not let a color-first start erase the placement anchors needed for sensitive drawing, and do not neutralize
    the original key during later refinement.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_resolve_large_full_color_masses_before_minor_detail
  variant_name: Resolve Large Full-Color Masses Before Minor Detail
  variant_basis: method_sequence
  difference_from_foundation: Begins a sufficiently simple subject with major shapes already carrying approximate real drawing,
    color, value, and edge character, keeps paint inexpensive while corrections remain likely, and subdivides only where added
    information preserves the parent mass and strengthens form, clarity, focus, or meaning.
  when_to_use: Use when broad full-color relationships are knowable early and the subject is simple enough that the large
    masses can be placed accurately without a separate monochrome or line-heavy construction.
  when_not_to_use: Do not use on large or complex arrangements that still require broader searching, and do not fragment a
    strong parent mass with value changes that weaken the reason the block-in worked.
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

Schmid II sharpens the continuity requirement across these starts: guide lines are scaffolding unless a moving source needs fixed registration; monochrome can become a nearly complete structural map; a color-key start must preserve its original family relationships; and a full-color mass may be subdivided only when the added information does not weaken the parent value/color structure that made the start strong.

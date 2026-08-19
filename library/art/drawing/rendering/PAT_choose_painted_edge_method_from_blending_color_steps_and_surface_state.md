---
object_id: PAT_choose_painted_edge_method_from_blending_color_steps_and_surface_state
object_type: pattern
name: Choose Painted Edge Method From Blending, Color Steps, and Surface State
library_path:
- art
- drawing
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: PAT_control_edge_hardness_from_form_light_and_focus
tags:
- rendering
- painting
- edges
- blending
- wet_paint
- medium_behavior
cross_links:
- rel: related_to
  target_object_id: PAT_control_edge_hardness_from_form_light_and_focus
- rel: related_to
  target_object_id: PAT_control_color_layering_with_transparency_opacity_and_ground
- rel: related_to
  target_object_id: PAT_build_broken_color_as_optical_mixture
reference:
  source_title: 'Alla Prima: Everything I Know About Painting'
  author: Richard Schmid
confidence: high
references: []
variants:
- variant_id: VAR_schmid_blend_fresh_adjacent_passages_for_fluid_edge
  variant_name: Blend Fresh Adjacent Passages for a Fluid Edge
  variant_basis: medium
  difference_from_foundation: Merges neighboring fresh or wet passages directly when a continuous fluid transition is wanted, preserving the intended endpoint values/colors and stopping before repeated blending erases their structure.
  when_to_use: Use when the medium is still workable and the desired edge is a smooth continuous transition rather than a visibly stepped or broken boundary.
  when_not_to_use: Do not keep brushing until the two sides become an undifferentiated average or lose necessary color/value identity.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_build_edge_from_intermediate_color_and_value_steps
  variant_name: Build an Edge From Intermediate Color and Value Steps
  variant_basis: method_sequence
  difference_from_foundation: Constructs the transition with a small sequence of intermediate color/value notes derived from the adjoining shapes instead of smearing the endpoints directly together.
  when_to_use: Use when the transition should remain controlled, chromatically active, or visibly constructed while still reading as a turn or merge at normal viewing distance.
  when_not_to_use: Do not multiply steps until the edge becomes banded, noisy, or more complicated than the form/light change warrants.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_step_then_merge_edge_once_to_preserve_color_and_softness
  variant_name: Step Then Merge an Edge Once to Preserve Color and Softness
  variant_basis: method_sequence
  difference_from_foundation: Establishes meaningful intermediate color/value notes first, then lightly merges them only enough to remove unwanted stepping, retaining more chromatic structure than indiscriminate blending.
  when_to_use: Use when a soft edge needs both visible color life and continuity.
  when_not_to_use: Do not add the merging pass when the separated notes already produce the intended edge at viewing distance.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_control_watercolor_edge_with_moisture_flow_and_drying_window
  variant_name: Control Watercolor Edge With Moisture, Flow, and Drying Window
  variant_basis: medium
  difference_from_foundation: Treats surface wetness, flow direction, absorption, and the remaining drying window as edge variables, allowing spread while it serves softness and anticipating where the edge will stop as the surface loses mobility.
  when_to_use: Use in watercolor or analogous fluid media where moisture state directly governs whether neighboring color diffuses, blooms, stops, or remains crisp.
  when_not_to_use: Do not assume a water-controlled edge can be revised independently after the surface has dried or that every soft edge benefits from uncontrolled spread.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_shear_or_scrape_wet_paint_with_palette_knife_for_edge_control
  variant_name: Shear or Scrape Wet Paint With a Palette Knife for Edge Control
  variant_basis: medium
  difference_from_foundation: Uses a clean flat knife to shear across fresh brushwork, scrape wet paint away to recut a boundary, or place a narrow accent from the blade edge; treats the leading contact edge as the most predictable boundary and expects the remainder of the knife mark to need selective correction.
  when_to_use: Use when a paint-like medium supports subtractive scraping or flat-blade shearing and those actions create the needed edge more directly than repeated brushing.
  when_not_to_use: Do not treat the entire knife perimeter as automatically clean, or use scraping where the passage is already dry, fragile, or visually resolved.
  absorbed_from_object_id: none
---
# Choose Painted Edge Method From Blending, Color Steps, and Surface State

## Pattern Rule
**IF** an edge has already been diagnosed visually but a paint-like medium can build that edge through materially different operations
**THEN** choose direct blending, intermediate color/value steps, a step-then-merge hybrid, moisture/spread control, scraping, or another compatible route according to the desired softness, color activity, thickness, and current surface state
**ELSE** use the general edge owner when no medium-dependent construction choice is required.

## Do
- Decide the final edge character before choosing the manipulation that creates it; technique serves the boundary rather than defining it by habit.
- Preserve the endpoint color/value relationships while softening unless the form or light itself requires those endpoints to change.
- Keep paint or simulated material moderate while an edge still needs delicate correction; reserve heavy impasto or difficult-to-revise buildup for passages whose placement and edge character are substantially settled.
- Use different edge-building methods in different passages when the subject, material, or color activity requires them.
- Recheck the whole image after a local edge is built so a technically successful transition does not become compositionally too loud.

## Don't
- Do not make blending the default for every soft edge.
- Do not preserve visible technique at the cost of the required color/value transition.
- Do not build thick, hard-to-revise surface early merely because the final work is meant to be impasted.
- Do not keep manipulating a successful edge until the adjoining colors become muddy or generic.

## Checklist
- The construction method matches the intended edge rather than a habitual tool preference.
- Color and value endpoints remain controlled after softening or merging.
- Surface state still permits the chosen operation without requiring avoidable repainting.
- The local edge supports the whole-picture value, color, and focal hierarchy.

## Notes
The general edge owner decides what the boundary should look like and why. This specialization owns a different question: how a wet, fluid, dry-particulate, or scrapeable medium should physically or simulatively build that already-chosen edge. Blending, stepped notes, partial merging, moisture flow, and knife manipulation are alternate constructions, not competing theories of edge perception.

`VAR_schmid_blend_fresh_adjacent_passages_for_fluid_edge`, `VAR_schmid_build_edge_from_intermediate_color_and_value_steps`, `VAR_schmid_step_then_merge_edge_once_to_preserve_color_and_softness`, `VAR_schmid_control_watercolor_edge_with_moisture_flow_and_drying_window`, and `VAR_schmid_shear_or_scrape_wet_paint_with_palette_knife_for_edge_control` preserve distinct medium-dependent routes under one edge-construction decision.

---
object_id: PAT_control_edge_hardness_from_form_light_and_focus
object_type: pattern
name: Control Edge Hardness From Form, Light, and Focus
library_path:
- art
- drawing
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- edges
- form_turn
- light_quality
- focus
cross_links:
- rel: related_to
  target_object_id: PAT_concentrate_contrast_and_accents_at_focal_area
- rel: related_to
  target_object_id: PAT_consolidate_resolved_form_with_tone
reference:
  source_id: bert_dodson_keys_to_drawing
  source_title: Keys to Drawing
  author: Bert Dodson
  publish_date: 1985
  media_type: PDF
  locator: u04, physical pp. 108-110
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_loomis_break_contour_when_hard_enclosure_flattens_depth
  variant_name: Break Continuous Hard Contour When Enclosure Flattens Depth
  variant_basis: emphasis
  source_id: andrew_loomis_creative_illustration
  source_title: Creative Illustration
  locator: u02, physical PDF p. 16; printed p. 23
  difference_from_foundation: "Loomis supplies a concrete failure diagnosis for edge control: if every contour remains continuously hard, the form can appear pasted to the picture plane. Selectively lose, soften, or interweave portions of contour where value, overlap, or neighboring shape already carries the boundary, then restore only the edges needed for structure, depth, and focal clarity."
  when_to_use: Use when an otherwise modeled form reads like a cutout because its perimeter is uniformly enclosed, especially where one form should pass behind another or merge into a neighboring value mass.
  when_not_to_use: Do not erase boundaries that are required for silhouette recognition, technical clarity, hard material separation, graphic style, or the focal statement. Lost contour must be supported by other depth or form evidence.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_build_soft_first_then_recover_selected_edges
  variant_name: Build Soft First, Then Recover Selected Edges
  variant_basis: method_sequence
  source_id: andrew_loomis_creative_illustration
  source_title: Creative Illustration
  locator: u07, physical PDF p. 106; printed p. 116
  difference_from_foundation: "Adds Loomis's sequencing alternative for tight rendering: establish the large tones, soften their boundaries early, preserve the broad softness as the picture develops, and recover only the edges, details, and accents required for form and focus instead of defining everything sharply first and trying to blur it afterward."
  when_to_use: "Use when a rendering is becoming uniformly hard, overprecise, or pasted onto the picture plane and a soft-first sequence would make selective edge recovery easier to control."
  when_not_to_use: "Do not suppress genuinely hard silhouettes, cast events, material boundaries, or graphic requirements merely to keep the picture soft. The sequence changes the starting bias; the final edge map must still answer to form, light, material, depth, and hierarchy."
  absorbed_from_object_id: none
---

# Control Edge Hardness From Form, Light, and Focus

## Pattern Rule
**IF** a value boundary must describe a form turn, cast event, material separation, or focal hierarchy
**THEN** set its hardness from the cause of the boundary, the rate of surface change, the light/contrast condition, and the intended visual priority rather than giving every boundary the same sharpness
**ELSE** use a neutral transition when the edge is not structurally or compositionally important

## Do
- Use harder transitions where the form or boundary changes abruptly and softer ones where the surface turns gradually.
- Let harsher or more directional lighting support crisper separations and diffuse lighting support broader transitions when the scene calls for it.
- Sharpen selected focal edges while allowing subordinate boundaries to soften or merge when form remains legible.
- Compare edge character across the whole image so one local passage does not become accidentally louder than the intended focal area.
- Diagnose softness by cause: light spread, diffuse or fuzzy material, adjacent values converging, a form turning into a similar surrounding value, one contour passing behind another, distance, or deliberate subordination can each justify a softer or lost boundary.

## Don't
- Outline every value shape with an equally hard border.
- Blur structurally abrupt events simply to make the rendering look smooth.
- Sharpen every high-contrast edge without considering whether it competes with the focal hierarchy.
- Make the whole picture uniformly soft; softness only reads as softness when harder and clearer boundaries remain available where the structure or emphasis needs them.

## Checklist
- Hard and soft edges correspond to explainable form, light, or emphasis decisions.
- Gradual turns do not read as cut paper unless intentionally stylized.
- The sharpest edges support rather than fight the intended focal hierarchy.
- Lost and softened edges have an identifiable optical, spatial, material, or compositional cause instead of being applied as a generalized blur.

## Notes
Dodson treats edges as boundaries between shapes whose character changes with the event producing them. The result is both descriptive and compositional: edge quality can explain form and illumination while also directing attention. `VAR_loomis_break_contour_when_hard_enclosure_flattens_depth` adds Loomis's cutout diagnosis: continuous hard enclosure can pin a form to the picture plane, so selectively losing or softening supported contour passages can restore spatial interlock without sacrificing necessary structure. Loomis's later edge discussion expands the diagnostic by cause—light spread, material diffusion, value convergence, turning form, overlap, distance, and subordination—and stresses that convincing edge design depends on an interlaced balance rather than an all-hard or all-soft treatment.

`VAR_loomis_build_soft_first_then_recover_selected_edges` adds a sequencing route for tight work: bias the early tonal statement toward softness, then recover only the boundaries and accents that the final form and hierarchy actually require.

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
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_loomis_build_soft_first_then_recover_selected_edges
  variant_name: Build Soft First, Then Recover Selected Edges
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Loomis''s sequencing alternative for tight rendering: establish the large tones,
    soften their boundaries early, preserve the broad softness as the picture develops, and recover only the edges,
    details, and accents required for form and focus instead of defining everything sharply first and trying to
    blur it afterward.'
  when_to_use: Use when a rendering is becoming uniformly hard, overprecise, or pasted onto the picture plane and
    a soft-first sequence would make selective edge recovery easier to control.
  when_not_to_use: Do not suppress genuinely hard silhouettes, cast events, material boundaries, or graphic requirements
    merely to keep the picture soft. The sequence changes the starting bias; the final edge map must still answer
    to form, light, material, depth, and hierarchy.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_separate_core_and_cast_shadow_by_cause
  variant_name: Separate Core and Cast Shadow by Cause
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Vilppu''s compact diagnostic to physical lighting: identify core shadow as a
    form-turning event between direct and reflected light, and cast shadow as light blocked by another form. Let
    the core edge inherit the sharpness of the surface turn, while the cast-shadow edge is sharpest near the occluder
    and softens with separation. On rounded forms, reflected or ambient fill can lift the silhouette side enough
    that the darkest core sits slightly inside the contour rather than on the outer edge.'
  when_to_use: Use when a tonal drawing has plausible dark shapes but the shadow edges do not explain whether the
    form is turning or another object is blocking the light.
  when_not_to_use: Do not force every core or cast edge into one fixed softness; actual source size, geometry, material,
    reflected light, and scene conditions still govern.
  absorbed_from_object_id: none
- variant_id: VAR_guptill_overstate_plane_edges_early_then_soften_to_final_truth
  variant_name: Overstate Plane Edges Early, Then Soften to Final Truth
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a construction-stage alternative for tonal work that is becoming mushy: temporarily
    sharpen or slightly overstate important plane boundaries while the value structure is being established, then
    soften those edges back to their truthful final hardness once the form reads.'
  when_to_use: Use when early tonal development is rounding everything indiscriminately and the underlying plane
    structure is being lost.
  when_not_to_use: Do not leave the temporary hard edges as a finished convention when the final form, material,
    light, or focus requires softer transitions.
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
- Judge light-source softness from the source's apparent angular size as seen from the subject, not physical size alone; a physically large but distant source can still behave hard.
- Treat focus-plane blur as a separate softness cause: keep the focal plane crisp, increase softness progressively with depth separation from it, and let overlapping contours reveal which plane is nearer or farther.

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
- Focus blur, atmospheric softness, material softness, and light-transition softness can be distinguished by cause instead of being collapsed into one generic blur.

## Notes

`VAR_loomis_build_soft_first_then_recover_selected_edges` adds a sequencing route for tight work: bias the early tonal statement toward softness, then recover only the boundaries and accents that the final form and hierarchy actually require.

`VAR_vilppu_separate_core_and_cast_shadow_by_cause` retains **Separate Core and Cast Shadow by Cause** as a cause-and-edge diagnostic: core shadow comes from a form turning away from light, while cast shadow comes from blocked light and its edge character follows source, occluder, and receiver geometry. On a rounded form, do not assume the silhouette must be the darkest point of the turn; ambient or reflected fill can lighten that edge and leave the darkest core slightly inside the contour.

`VAR_guptill_overstate_plane_edges_early_then_soften_to_final_truth` temporarily clarifies key plane breaks during construction, then restores their truthful final softness once the form is secure.

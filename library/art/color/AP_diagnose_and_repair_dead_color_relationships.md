---
object_id: AP_diagnose_and_repair_dead_color_relationships
object_type: ap
name: Diagnose and Repair Dead Color Relationships
library_path:
- art
- color
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_decompose_color_relationships_into_hue_value_and_chroma
tags:
- rendering
- color
- diagnosis
- palette
- chroma
- value
cross_links:
- rel: supports
  target_object_id: PAT_unify_palette_with_shared_color_influence
- rel: supports
  target_object_id: PAT_preserve_value_structure_when_translating_tone_into_color
- rel: supports
  target_object_id: PAT_position_peak_chroma_across_light_halftone_and_shadow
- rel: supports
  target_object_id: PAT_resolve_visible_color_from_local_color_light_and_reflection
- rel: supports
  target_object_id: PAT_concentrate_contrast_and_accents_at_focal_area
- rel: supports
  target_object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
- rel: related_to
  target_object_id: AP_diagnose_and_recover_failing_observed_rendering
- rel: supports
  target_object_id: PAT_preserve_clean_paint_color_by_limiting_wet_reworking
- rel: supports
  target_object_id: PAT_decompose_color_relationships_into_hue_value_and_chroma
- rel: supports
  target_object_id: PAT_account_for_perceptual_color_context_adaptation_and_constancy
reference:
  source_title: Creative Illustration
  author: Andrew Loomis
confidence: high
references: []
variants: []
---

# Diagnose and Repair Dead Color Relationships

## Objective
Repair a picture whose color genuinely reads dull, muddy, disconnected, over-greyed, or hierarchically ineffective by classifying the cause before changing saturation and by protecting any already-correct value, light, and focal relationships during recovery.

## Steps / Flow
1. **Confirm that this is a color-read failure.** Enter when the image has a specific color symptom—mud, dullness, disconnected families, chroma competition, or loss of intended color hierarchy. If the whole picture simply feels wrong with no color-specific evidence, use the broader rendering-diagnosis AP first.
2. **Protect the central invariant: do not increase chroma until the cause is classified.** Apply `PAT_decompose_color_relationships_into_hue_value_and_chroma` to identify whether hue identity, value, chroma, or a combination is carrying the error before choosing a treatment. A stronger saturation move is a treatment, not a diagnosis.
3. **Branch: physical/mark mixture collapse.** Ask whether repeated wet mixing or reworking has homogenized a passage that otherwise had a sound color plan. In paint, route to `PAT_preserve_clean_paint_color_by_limiting_wet_reworking` or the accepted partial-mixing owner as appropriate; do not redesign the whole palette when the failure is local material interaction.
4. **Branch: value-family failure.** Apply `PAT_preserve_value_structure_when_translating_tone_into_color` at this decision. Temporarily ignore hue and verify the major light, middle, and dark organization. If color is compensating for broken value structure, repair the parent value families before changing chroma.
5. **Branch: illumination/environment or perceptual-context failure.** Apply `PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum` and `PAT_resolve_visible_color_from_local_color_light_and_reflection` at this decision. Test whether local colors belong to the active light, reflected surroundings, and atmosphere. If material and illumination still do not explain an apparent color shift, apply `PAT_account_for_perceptual_color_context_adaptation_and_constancy` before changing the physical color model. When the hue family seems plausible but a passage still reads muddy or disconnected, compare relative value and temperature against the accepted illumination before assuming the problem is low saturation.
6. **Branch: palette competition or harmony failure.** Apply `PAT_unify_palette_with_shared_color_influence` at this decision. Ask whether too many independently strong color families are fighting. Simplify, subordinate, or strengthen a shared environmental/designed influence without mechanically tinting every color the same way.
7. **Branch: focal hierarchy failure.** Apply `PAT_concentrate_contrast_and_accents_at_focal_area` at this decision. If the colors are individually plausible but attention is spread indiscriminately, reduce subordinate competition and preserve stronger chroma/contrast for the intended focal role.
8. **Branch: broader image failure masquerading as color failure.** If diagnosis reveals broken drawing, composition, reference interpretation, edge hierarchy, or another upstream problem, delegate that recovery to `AP_diagnose_and_recover_failing_observed_rendering`. Resume this AP only if a genuine color-specific defect remains afterward.
9. **Repair the smallest causal layer that explains the symptom.** Preserve accepted light/value families, scene-wide color logic, and focal hierarchy while changing only what the classified failure requires.
10. **Restore chroma selectively only when the diagnosis supports it.** Apply `PAT_position_peak_chroma_across_light_halftone_and_shadow` at this decision. If the image is genuinely over-greyed after the other causes are sound, increase chroma in the passages that need it rather than saturating the whole image.
11. **Pass the reduced-read completion gate.** Judge the image small or at distance. Completion requires coherent large value/color organization, colors that belong to the causal illumination/environment or a deliberately designed strategy, and useful focal chroma support. A prettier local swatch is not enough.

## Notes
This AP coordinates existing color owners; it does not replace them with one universal fix. Gray and brown are not defects by default, and a picture full of individually clean high-chroma notes can still fail through competition or value disorganization.

The protocol is intentionally diagnostic. Protect already-correct relationships while testing the cause, and route non-color failures out of the color loop instead of escalating saturation indefinitely.

---
object_id: PAT_account_for_perceptual_color_context_adaptation_and_constancy
object_type: pattern
name: Account for Perceptual Color Context, Adaptation, and Constancy
library_path:
- art
- color
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- color
- perception
- adaptation
- color_constancy
- simultaneous_contrast
cross_links:
- rel: related_to
  target_object_id: PAT_resolve_visible_color_from_local_color_light_and_reflection
- rel: related_to
  target_object_id: PAT_decompose_color_relationships_into_hue_value_and_chroma
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_gurney_isolate_suspect_color_then_restore_context
  variant_name: Isolate Suspect Color, Then Restore Context
  variant_basis: context
  difference_from_foundation: Temporarily removes misleading neighboring context with a neutral surround or aperture, compares
    the patch against useful anchors, and can sweep that isolation across one surface to expose light-, reflection-, and context-driven
    variation that a single local-color label would otherwise compress; then restores the full scene before accepting the
    correction.
  when_to_use: Use when color constancy, simultaneous contrast, or surrounding illumination makes a local observational match
    difficult to judge.
  when_not_to_use: Do not treat isolation as final truth; the neutral reference is also illuminated and the finished passage
    must still work in context.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_use_colored_fill_to_induce_complementary_key_read
  variant_name: Use Colored Fill to Induce a Complementary Key Read
  variant_basis: context
  difference_from_foundation: Uses a strongly colored fill or shadow environment to make a neutral or mildly colored key-lit
    side appear shifted toward the complementary direction without literally repainting the key as that hue.
  when_to_use: Use when a designed multi-source scene needs stronger relative temperature separation while preserving physically
    coherent source colors.
  when_not_to_use: Do not confuse the induced perceptual complement with a new physical light source or force the effect when
    the surrounding context does not support it.
  absorbed_from_object_id: none
references: []
---

# Account for Perceptual Color Context, Adaptation, and Constancy

## Pattern Rule
**IF** a color appears to change in a way that the scene's material and illumination alone do not explain
**THEN** test whether simultaneous contrast, recent color exposure, chromatic adaptation, color constancy, or viewing scale is altering the perceived relationship before changing the physical color model
**ELSE** resolve the passage from local color, illumination, reflection, and material response.

## Do
- Distinguish scene-caused color changes from viewer-caused appearance changes.
- Compare a suspect patch in context and, when necessary, under a temporarily neutralized surround.
- Allow prolonged colored illumination to be partly normalized perceptually instead of treating its cast as an unchanged overlay everywhere.
- When a complementary color seems to appear after sustained fixation or exposure, test it as an afterimage before altering the scene color; move the gaze or rest the visual context, then judge again.
- Remember that expected object identity can bias a viewer toward perceiving stable local color under changing illumination.
- Recheck small color areas at their final scale because reduced area can weaken color discrimination.

## Don't
- Correct every surprising color by inventing another light or reflected source.
- Assume an isolated swatch predicts how the same patch will read in its surrounding field.
- Treat adaptation or constancy as a license to ignore physical illumination.
- Repaint a passage to chase a transient complementary afterimage caused by recent exposure.

## Checklist
- Physical light/material causes are separated from perceptual context effects.
- Color corrections are judged again after the full context is restored.
- The final relationship works at the intended viewing scale.

## Notes
Perceived color is constructed from both incoming light and the visual system's interpretation of context. A reliable workflow first solves the scene signal, then asks whether adaptation, contrast, constancy, or scale changes how that signal will be experienced.

`VAR_gurney_isolate_suspect_color_then_restore_context` Temporarily removes misleading neighboring context with a neutral surround or aperture, compares the patch against useful anchors, and can sweep that isolation across one surface to expose the lightest, darkest, highest-chroma, lowest-chroma, and materially shifted hue regions that local-color expectation can hide; then restores the full scene before accepting the correction. Use it when when color constancy, simultaneous contrast, or surrounding illumination makes a local observational match difficult to judge Avoid it when treat isolation as final truth; the neutral reference is also illuminated and the finished passage must still work in context .

`VAR_gurney_use_colored_fill_to_induce_complementary_key_read` Uses a strongly colored fill or shadow environment to make a neutral or mildly colored key-lit side appear shifted toward the complementary direction without literally repainting the key as that hue. Use it when when a designed multi-source scene needs stronger relative temperature separation while preserving physically coherent source colors Avoid it when confuse the induced perceptual complement with a new physical light source or force the effect when the surrounding context does not support it .

---
object_id: PAT_resolve_visible_color_from_local_color_light_and_reflection
object_type: pattern
name: Resolve Visible Color From Local Color, Light, and Reflection
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
- color
- local_color
- illumination
- reflected_light
- light_shadow
cross_links:
- rel: related_to
  target_object_id: PAT_separate_local_value_from_light_and_shadow_effect
- rel: related_to
  target_object_id: PAT_preserve_value_structure_when_translating_tone_into_color
reference:
  source_title: Creative Illustration
  author: Andrew Loomis
confidence: high
references: []
variants:
- variant_id: VAR_loomis_key_color_temperature_to_environmental_light
  variant_name: Key Color Temperature to Environmental Light
  variant_basis: context
  difference_from_foundation: "Adds an environment-wide temperature route: identify the dominant illumination and reflected-light conditions, then let those conditions bias related surfaces consistently rather than applying a memorized warm-light/cool-shadow formula object by object."
  when_to_use: Use when daylight, skylight, artificial light, ground reflection, or another dominant environmental source gives the scene a clear temperature relationship that should carry across multiple forms.
  when_not_to_use: Do not assume sunlight always requires one fixed warm/cool split, ignore colored surroundings or multiple sources, or force an inverse temperature relationship when the observed or designed lighting does not support it.
  absorbed_from_object_id: none
---
# Resolve Visible Color From Local Color, Light, and Reflection

## Pattern Rule
**IF** a colored surface must read convincingly under a specific lighting environment
**THEN** treat its local color as a starting identity and resolve the visible color from the combined effects of illumination, form turning, and reflected surroundings rather than assigning one fixed hue to the object and a separate arbitrary hue to its shadow
**ELSE** preserve the simpler local-color statement when the task intentionally suppresses lighting variation.

## Do
- Identify the surface's local color, then ask how the current light changes its apparent hue, value, and chroma before painting the lit passage.
- Let shadow color remain related to the same material while accepting stronger influence from reflected surroundings and secondary illumination.
- Compare neighboring planes as parts of one lighting environment so light, halftone, and shadow feel causally connected rather than independently chosen.
- Preserve enough color-family continuity across the form that the object still reads as the same material while it turns through different illumination.
- Use observed or intentionally designed reflected color where nearby surfaces, sky, ground, or other sources visibly influence the shadow side.

## Don't
- Do not paint an object by repeating one remembered or named local color across every plane.
- Do not invent a disconnected "shadow hue" merely to make the shadow look colorful.
- Do not assume a warm/cool rule overrides the actual or designed illumination; temperature is one possible lighting bias, not a universal formula.
- Do not sacrifice the value structure that makes the form read just to preserve a preferred hue.

## Checklist
- The lit and shadowed passages still belong to one surface or material family.
- Color changes can be explained by light direction, light character, reflected surroundings, or intentional design rather than arbitrary hue replacement.
- Local color remains recognizable without being copied unchanged through every lighting zone.
- Value and color relationships cooperate to describe the same form.

## Notes
The durable rendering decision is to separate a surface's color identity from the color it visibly presents under a particular environment. Illumination and surrounding reflection can alter hue, value, chroma, and temperature, especially as the form turns away from the main light. The goal is not to preserve one tube color everywhere, but to make the changing color relationships feel like consequences of one material in one light.

`VAR_loomis_key_color_temperature_to_environmental_light` extends that decision across the scene: establish the dominant illumination and surrounding reflection first, then let warm/cool shifts follow those conditions consistently instead of treating temperature as a memorized recipe.

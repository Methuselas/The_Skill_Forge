---
object_id: PAT_resolve_visible_color_from_local_color_light_and_reflection
object_type: pattern
name: Resolve Visible Color From Local Color, Light, and Reflection
library_path:
- art
- color
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
  difference_from_foundation: Uses an inverse light/shadow temperature split as an initial diagnostic expectation only when
    one reasonably simple dominant source governs the scene, then yields to actual reflected, transmitted, secondary-light,
    and environmental evidence when those causes explain exceptions.
  when_to_use: Use when a scene has a clear dominant illumination and a broad warm/cool relationship would help diagnose whether
    local color belongs to the same light system.
  when_not_to_use: Do not invent a warm/cool split when it is not visible, and do not override bounce, transmission, colored
    surroundings, or secondary sources to preserve a rule.
  absorbed_from_object_id: none
- variant_id: VAR_eissen_key_product_planes_with_simplified_color_states
  variant_name: Key Product Planes With Simplified Color States
  variant_basis: emphasis
  difference_from_foundation: 'Adds a schematic product-sketch convention for simple neutral lighting: keep one descriptive
    plane near the object''s fuller local colour, push the shade-facing plane darker and less saturated, and lift the upward
    or light-facing plane brighter so the major planes separate immediately.'
  when_to_use: Use when a fast product sketch needs legible plane turning and colour identity under a simple descriptive light
    without a fully observed material-light simulation.
  when_not_to_use: Do not treat the three-state split as universal colour physics; abandon it when coloured illumination,
    strong reflected light, complex materials, or observed reference produces a different relationship.
  absorbed_from_object_id: none
- variant_id: VAR_olofsson_build_lighting_from_ambient_matte_base
  variant_name: Build Lighting From an Ambient Matte Base
  variant_basis: method_sequence
  difference_from_foundation: Begins from a comparatively matte ambient-light statement of the product, then introduces designed
    light sources one at a time by layering their illumination, highlights, and reflected-light effects. Areas that receive
    none of those added contributions remain naturally in the darker family.
  when_to_use: Use for stylized persuasive product rendering with artificial or multiple designed lights when the contribution
    of each source should stay controllable.
  when_not_to_use: Do not treat the sequence as universal light physics or ignore occlusion, cast shadows, material response,
    and actual source geometry.
  absorbed_from_object_id: none
- variant_id: VAR_gurney_use_light_skin_facial_color_zones_as_subtle_starting_bias
  variant_name: Use Light-Skin Facial Color Zones as a Subtle Starting Bias
  variant_basis: context
  difference_from_foundation: 'Adds a bounded observational tendency for light-skinned faces: a slightly more golden forehead,
    relatively redder central face, and cooler/greyer lower zone can serve as a starting bias when the actual reference supports
    it.'
  when_to_use: Use only when complexion, circulation, activity, age, facial hair, environment, and lighting visibly support
    these subtle zones.
  when_not_to_use: Do not impose the zones as a universal face-color template across people or lighting conditions; actual
    evidence overrides the tendency.
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
- Treat source spectrum as an independent input: an uneven or narrow-band illuminant can strengthen some color families while leaving others weak, so artificial light is not always equivalent to a uniform warm/cool tint.
- Model a strongly illuminated neighboring surface as a secondary source whose reflected contribution changes with its brightness, scale, distance, and the orientation of the receiving plane; combine multiple secondary sources instead of assigning one canned shadow color.
- After resolving material, illumination, and reflection physically, hand off any additional viewer-caused shift to perceptual context, adaptation, and color constancy rather than inventing another physical source.
- Under strongly biased illumination, ask which hue families should be weakened or absent because the source spectrum does not support them, and restrain those families in proportion to the actual light rather than applying one uniform tint to every surface.

## Don't
- Do not paint an object by repeating one remembered or named local color across every plane.
- Do not invent a disconnected "shadow hue" merely to make the shadow look colorful.
- Do not assume a warm/cool rule overrides the actual or designed illumination; temperature is one possible lighting bias, not a universal formula.
- Do not sacrifice the value structure that makes the form read just to preserve a preferred hue.
- Do not treat every perceived complementary or adapted color shift as evidence that another colored light is physically present.

## Checklist
- The lit and shadowed passages still belong to one surface or material family.
- Color changes can be explained by light direction, light character, reflected surroundings, or intentional design rather than arbitrary hue replacement.
- Local color remains recognizable without being copied unchanged through every lighting zone.
- Value and color relationships cooperate to describe the same form.

## Notes
The durable rendering decision is to separate a surface's color identity from the color it visibly presents under a particular environment. Illumination and surrounding reflection can alter hue, value, chroma, and temperature, especially as the form turns away from the main light. The goal is not to preserve one tube color everywhere, but to make the changing color relationships feel like consequences of one material in one light.

`VAR_loomis_key_color_temperature_to_environmental_light` extends that decision across the scene: establish the dominant illumination and surrounding reflection first, then let warm/cool shifts follow those conditions consistently instead of treating temperature as a memorized recipe.

`VAR_eissen_key_product_planes_with_simplified_color_states` is a faster descriptive convention for product sketching under a simple neutral light. Keep the local-colour family recognizable, but separate the broad planes by giving one a fuller local-colour statement, darkening and muting the shade-facing plane, and brightening the upward or light-facing plane. It is a communication shorthand, not a substitute for the foundation when the real light or material response is more complicated.

`VAR_olofsson_build_lighting_from_ambient_matte_base` is a controlled workflow for designed illumination. Establish a subdued local-color/material base first, then add the effect of each light source deliberately. The untouched base becomes the darker family where no added source contribution reaches it, while highlights and reflected light accumulate causally rather than being painted as disconnected accents.

`VAR_gurney_use_light_skin_facial_color_zones_as_subtle_starting_bias` Adds a bounded observational tendency for light-skinned faces: a slightly more golden forehead, relatively redder central face, and cooler/greyer lower zone can serve as a starting bias when the actual reference supports it.

Strongly biased illumination can be diagnosed partly by what it suppresses: hue families that the source spectrum weakly supports should not remain arbitrarily pure merely because they belong to the object's remembered local color.

`VAR_loomis_key_color_temperature_to_environmental_light` treats opposite light/shadow temperature as a bounded diagnostic for simple dominant-source scenes, not a universal law. Reflected and secondary light remain causal owners when they explain the visible relationship better.

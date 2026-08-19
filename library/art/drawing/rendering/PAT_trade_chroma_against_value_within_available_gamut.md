---
object_id: PAT_trade_chroma_against_value_within_available_gamut
object_type: pattern
name: Trade Chroma Against Value at the Medium Gamut Boundary
library_path:
- art
- drawing
- rendering
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- color
- gamut
- chroma
- value
- medium_limits
cross_links:
- rel: related_to
  target_object_id: PAT_decompose_color_relationships_into_hue_value_and_chroma
- rel: related_to
  target_object_id: PAT_define_and_enforce_picture_gamut
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_schmid_shift_surrounding_temperature_to_imply_overrange_color_intensity
  variant_name: Shift Surrounding Temperature to Imply Overrange Color Intensity
  variant_basis: constraint
  difference_from_foundation: When the target color exceeds the available chroma at the required value, preserves the sensation of intensity by moving surrounding colors away from the target in temperature or family so the available target note appears relatively hotter, cooler, or more vivid.
  when_to_use: Use when literal reproduction of a luminous or highly saturated target is impossible but the surrounding relationships can be adjusted without breaking the scene.
  when_not_to_use: Do not shift the environment arbitrarily when the surrounding colors are themselves critical evidence or when the target can already be represented within gamut.
  absorbed_from_object_id: none
references: []
---
# Trade Chroma Against Value at the Medium Gamut Boundary

## Pattern Rule
**IF** the target hue, value, and chroma combination lies outside what the medium or display can physically reproduce
**THEN** identify which coordinate cannot be matched, determine whether the output medium is fixed, change to a capable medium when the unavailable color or optical behavior is concept-critical and the medium is negotiable, otherwise choose the least damaging value-chroma compromise and use surrounding relationships to imply the missing intensity
**ELSE** match the target relationship directly within the available medium gamut.

## Do
- Treat hue, value, and chroma as coupled limits rather than assuming every hue can reach maximum chroma at every value.
- Remember that different hue families reach their strongest attainable chroma at different value levels.
- Decide whether preserving value, hue identity, or chroma is most important to the passage's function before compromising.
- If the medium is still negotiable and the unavailable color or optical behavior is concept-critical, evaluate a medium capable of producing it before accepting a compromise.
- Use neighboring quieter values/chromas to make an unattainable accent feel more intense relationally.
- Distinguish this physical medium gamut from a deliberately restricted picture gamut.
- Treat opaque lightening as a coupled color operation: after raising value, recheck hue, chroma, and relative temperature because the lightener may make the mixture paler, cooler, chalkier, or otherwise shift it beyond the intended relationship.

## Don't
- Chase an impossible color by repeatedly increasing saturation and destroying value structure.
- Compromise a concept-critical color automatically when changing medium would preserve the intended effect at acceptable cost.
- Assume the medium's gamut boundary is the same as an intentional palette restriction.
- Treat peak chroma as occurring at one universal value for every hue.

## Checklist
- The chosen medium or compromise preserves the passage's most important perceptual role.
- When the medium was flexible, the decision to keep or change it was made before degrading a concept-critical target.
- Value and chroma tradeoffs remain deliberate rather than accidental clipping.
- The medium limit and the picture-design limit are not being confused.

## Notes
A medium can be unable to produce a requested combination even when each coordinate seems plausible in isolation. The useful decision is to recognize the boundary early. If the medium is flexible and the unavailable color or optical behavior is essential to the concept, changing medium can be the better solution; otherwise preserve the most important relationship and let context help carry the sensation the medium cannot state literally.

This owner concerns the **medium or display gamut**—what can physically be represented. `PAT_define_and_enforce_picture_gamut` concerns an intentional design subset chosen from within that capability. Keep those two constraints separate during diagnosis.

`VAR_schmid_shift_surrounding_temperature_to_imply_overrange_color_intensity` preserves the sensation of an unavailable luminous or high-chroma note by adjusting surrounding relationships rather than endlessly pushing the target beyond the medium's usable gamut.

Opaque lightening is not a value-only move. Recheck hue, chroma, and relative temperature after raising value so the correction does not become chalky or drift from the intended family merely because the lightness is right.

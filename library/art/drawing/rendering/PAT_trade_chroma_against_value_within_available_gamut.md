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
variants: []
references: []
---

# Trade Chroma Against Value at the Medium Gamut Boundary

## Pattern Rule
**IF** the target hue, value, and chroma combination lies outside what the medium or display can physically reproduce
**THEN** identify which coordinate cannot be matched, choose the least damaging value-chroma compromise, and use surrounding relationships to imply the missing intensity
**ELSE** match the target relationship directly within the available medium gamut.

## Do
- Treat hue, value, and chroma as coupled limits rather than assuming every hue can reach maximum chroma at every value.
- Remember that different hue families reach their strongest attainable chroma at different value levels.
- Decide whether preserving value, hue identity, or chroma is most important to the passage's function before compromising.
- Use neighboring quieter values/chromas to make an unattainable accent feel more intense relationally.
- Distinguish this physical medium gamut from a deliberately restricted picture gamut.

## Don't
- Chase an impossible color by repeatedly increasing saturation and destroying value structure.
- Assume the medium's gamut boundary is the same as an intentional palette restriction.
- Treat peak chroma as occurring at one universal value for every hue.

## Checklist
- The compromise preserves the passage's most important perceptual role.
- Value and chroma tradeoffs remain deliberate rather than accidental clipping.
- The medium limit and the picture-design limit are not being confused.

## Notes
A medium can be unable to produce a requested combination even when each coordinate seems plausible in isolation. The useful decision is to recognize the boundary early, preserve the most important relationship, and let context help carry the sensation the medium cannot state literally.

This owner concerns the **medium or display gamut**—what can physically be represented. `PAT_define_and_enforce_picture_gamut` concerns an intentional design subset chosen from within that capability. Keep those two constraints separate during diagnosis.

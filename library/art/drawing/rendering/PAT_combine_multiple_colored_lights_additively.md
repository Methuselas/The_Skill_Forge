---
object_id: PAT_combine_multiple_colored_lights_additively
object_type: pattern
name: Combine Multiple Colored Lights Additively
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
- lighting
- colored_light
- additive_color
- cast_shadow
cross_links:
- rel: related_to
  target_object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
- rel: related_to
  target_object_id: PAT_resolve_visible_color_from_local_color_light_and_reflection
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants: []
references: []
---

# Combine Multiple Colored Lights Additively

## Pattern Rule
**IF** two or more differently colored light sources reach the same surface
**THEN** add their illumination contributions at the receiver, making overlap generally lighter and chromatically combined, while a shadow from one source retains contributions from the other sources that are not blocked
**ELSE** use a single-source model when one light overwhelmingly dominates.

## Do
- Evaluate each source separately for strength, color, direction, and visibility to the receiver before combining them.
- In overlap regions, combine source contributions as light rather than as subtractive pigment mixtures.
- In a cast shadow from one source, remove only the blocked source and preserve unblocked fill from the others.
- Keep specular reflections source-specific when the surface can resolve separate highlight systems; diffuse color may combine while distinct highlights remain distinct.

## Don't
- Mix source colors as though colored paint were being stirred together.
- Make every cast shadow neutral or black when another colored source still reaches it.
- Collapse separate specular sources into one generic highlight color when the reflection geometry keeps them distinct.

## Checklist
- Overlap is lighter or more strongly illuminated than single-source regions unless exposure/design intentionally compresses it.
- Each cast shadow can be explained by which source is blocked and which remain.
- Diffuse and specular contributions are not being conflated.

## Notes
Multiple colored lights create an additive illumination problem. The easiest diagnostic is source removal: a cast shadow from one light shows what the remaining lights alone contribute to that surface.

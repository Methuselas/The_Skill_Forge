---
object_id: PAT_render_luminescent_emission_over_darker_base
object_type: pattern
name: Render Luminescent Emission Over a Darker Base
library_path:
- art
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- luminescence
- emission
- glow
- lighting
cross_links:
- rel: related_to
  target_object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
- rel: related_to
  target_object_id: PAT_simulate_overrange_brightness_with_source_colored_corona
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants: []
references: []
---

# Render Luminescent Emission Over a Darker Base

## Pattern Rule
**IF** a subject emits visible light rather than merely reflecting illumination
**THEN** establish the non-emissive scene and emitter body in a darker value structure first, then add the emitted light as a source-colored gradient whose nearby illumination is causally consistent with the emitter
**ELSE** render the surface through ordinary reflected-light or material behavior.

## Do
- Resolve the dark surrounding field before judging how bright the emission needs to feel.
- Let the emitted color grade in hue, value, or chroma when the phenomenon supports a nonuniform glow.
- Light nearby receiving surfaces according to distance, orientation, and occlusion from the emitter.
- Preserve enough dark structure around the source for the emission to remain legible.

## Don't
- Paint a flat bright sticker on the object without any effect on nearby surfaces when the emitter should illuminate them.
- Use one stock blue-green glow for every luminescent subject.
- Erase all local structure inside the luminous area unless the intensity truly overwhelms it.

## Checklist
- The source reads as emitting rather than merely being brightly painted.
- Nearby illumination can be traced back to the emitter.
- The glow remains embedded in a coherent value structure.

## Notes
Luminescence is most convincing when the scene is solved without it first and the emission is then allowed to alter the surrounding light field. The exact hue depends on the emitting mechanism and environment; the durable skill is source-consistent emission, not a canned glow color.

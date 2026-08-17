---
object_id: PAT_model_water_surface_from_view_angle_reflection_transmission_and_wave_distortion
object_type: pattern
name: Model Water Surface From View Angle, Reflection, Transmission, and Wave Distortion
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
- water
- reflection
- transmission
- waves
- material
cross_links:
- rel: related_to
  target_object_id: PAT_render_material_from_optical_response
- rel: related_to
  target_object_id: PAT_filter_underwater_color_by_optical_path_and_water_content
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants: []
references: []
---

# Model Water Surface From View Angle, Reflection, Transmission, and Wave Distortion

## Pattern Rule
**IF** a water surface must show both what lies above and what lies below it
**THEN** choose the reflection-versus-transmission balance from view angle, depth/clarity, illumination, and surrounding values, then distort reflected information through wave geometry instead of copying the environment as a simple vertical flip
**ELSE** emphasize the single dominant component when reflection or transmission overwhelmingly wins.

## Do
- Favor reflection at grazing view angles and more below-water information at steeper downward views, modifying for clarity, depth, and illumination.
- Preserve major vertical reflection information more readily than small horizontal detail when surface waves break the image.
- Let wavelets stretch, fragment, or interrupt reflected shapes according to their orientation and scale.
- Include sediment, bottom color, and underwater shadow information when transmission makes them visible.
- Keep surface reflection layered over the underwater field rather than merging both into one generic blue texture.

## Don't
- Mirror the landscape by flipping it vertically without wave distortion or view-angle effects.
- Use the same reflection/transmission ratio across the entire surface when viewing angle or depth changes substantially.
- Treat water color as independent of sky, bottom, sediment, and illumination.

## Checklist
- Reflection versus transmission changes plausibly with view and scene conditions.
- Wave distortion preserves enough large structure to read while breaking subordinate detail.
- Surface and underwater information remain causally separable.

## Notes
Water is not one optical behavior. It simultaneously reflects and transmits, with the balance changing across view angle and environment; wave geometry then remaps the reflected image. This deserves a dedicated model rather than a few generic material bullets.

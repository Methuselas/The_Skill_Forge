---
object_id: PAT_model_water_surface_from_view_angle_reflection_transmission_and_wave_distortion
object_type: pattern
name: Model Water Surface From View Angle, Reflection, Transmission, and Wave Distortion
library_path:
- art
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
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
variants:
- variant_id: VAR_martin_encode_water_state_with_black_white_wave_rhythm
  variant_name: Encode Water State With Black-White Wave Rhythm
  variant_basis: medium
  difference_from_foundation: 'Adds a black-and-white line-art route: use alternating dark mass and retained light shapes to make crest/trough structure legible, change the mark rhythm with surface state and flow, and compress articulation with recession while keeping the larger wave/perspective geometry intact.'
  when_to_use: Use when water must read clearly in stylized black-and-white ink without continuous tone or color, especially when wave state and depth recession need to survive reproduction.
  when_not_to_use: Do not use the graphic shorthand as a substitute for reflection, transmission, and optical-path reasoning when physical water behavior is important.
  absorbed_from_object_id: none
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
- Treat the ripple/wave field as geometry lying on the water plane: comparable surface events generally compress, tighten, and lose articulation with recession, while nearer waves occupy more picture space and can reveal more curvature and breakup.
- Apply reflection distortion through that perspective-aware surface pattern rather than laying a flat decorative texture over an otherwise mirrored image; preserve major reflected placement while the wave field fragments, stretches, or displaces subordinate information.
- Include sediment, bottom color, and underwater shadow information when transmission makes them visible.
- Keep surface reflection layered over the underwater field rather than merging both into one generic blue texture.

## Don't
- Mirror the landscape by flipping it vertically without wave distortion or view-angle effects.
- Keep repeated ripple marks at one size and spacing across depth, or force a single foreground-ellipse/distant-horizontal shorthand when the actual wave orientation, wind, camera, or surface geometry calls for another projected pattern.
- Use the same reflection/transmission ratio across the entire surface when viewing angle or depth changes substantially.
- Treat water color as independent of sky, bottom, sediment, and illumination.

## Checklist
- Reflection versus transmission changes plausibly with view and scene conditions.
- Wave distortion preserves enough large structure to read while breaking subordinate detail.
- Repeated surface structure shows believable perspective compression with recession instead of behaving like screen-space texture.
- Surface and underwater information remain causally separable.

## Notes
Water is not one optical behavior. It simultaneously reflects and transmits, with the balance changing across view angle and environment; wave geometry then remaps the reflected image. That wave geometry also occupies a receding surface: comparable ripples tighten and simplify with distance, so reflection breakup should inherit the water-plane perspective rather than remain uniform across the image. This deserves a dedicated model rather than a few generic material bullets.

`VAR_martin_encode_water_state_with_black_white_wave_rhythm` specializes the optical water model for economical black-and-white inking. Alternate dark mass with retained light crest/trough shapes, let the mark rhythm follow the actual surface state and flow, and reduce mark size, contrast, and articulation with recession. The shorthand must remain subordinate to the larger surface perspective and wave geometry, and it yields back to the foundation whenever reflection/transmission fidelity matters.

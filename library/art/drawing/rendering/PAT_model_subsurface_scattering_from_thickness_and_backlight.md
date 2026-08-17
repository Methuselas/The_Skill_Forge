---
object_id: PAT_model_subsurface_scattering_from_thickness_and_backlight
object_type: pattern
name: Model Subsurface Scattering From Thickness and Backlight
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
- material
- subsurface_scattering
- translucency
- backlight
cross_links:
- rel: related_to
  target_object_id: PAT_render_material_from_optical_response
- rel: related_to
  target_object_id: PAT_resolve_visible_color_from_local_color_light_and_reflection
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_gurney_model_snow_from_granular_scattering_age_and_specularity
  variant_name: Model Snow From Granular Scattering, Age, and Specularity
  variant_basis: context
  difference_from_foundation: 'Specializes subsurface/granular scattering for snow: fresh powder has broad internal
    scattering and soft light leakage, while compacted or aged snow becomes darker and more specular as crystal
    structure changes.'
  when_to_use: Use when snow must read as a light-scattering granular material rather than a uniformly white matte
    plane.
  when_not_to_use: Do not make every snow shadow blue or every old snow glossy; actual sky, ground, contamination,
    compaction, and light direction still govern.
  absorbed_from_object_id: none
references: []
---

# Model Subsurface Scattering From Thickness and Backlight

## Pattern Rule
**IF** light can enter a material, travel beneath its surface, and re-emerge nearby
**THEN** model the glow from material thickness, transmission distance, light direction, and internal scattering, strengthening it in thinner or strongly backlit regions rather than treating the surface as opaque matte paint
**ELSE** use diffuse/specular surface response without invented internal glow.

## Do
- Look for stronger transmitted/scattered light where the material is thin, backlit, or near an edge.
- Preserve thicker regions as comparatively darker or less luminous when the same light path travels farther through the material.
- Let the emerging color reflect the material's selective transmission rather than simply copying the source color.
- Keep surface reflection and subsurface glow as separate contributions when both are visible.

## Don't
- Add a uniform rim glow to every translucent material regardless of thickness or light path.
- Confuse subsurface scattering with mirror-like reflection or transparent see-through transmission.
- Use opaque matte shading alone when the material's internal light transport is the key identity cue.

## Checklist
- Glow strength changes plausibly with thickness and backlight.
- Internal color differs from surface reflection where the material supports that distinction.
- The effect remains tied to actual light entry and exit paths.

## Notes
Subsurface scattering is a volume effect. It explains why skin, ears, fingertips, fruit, milk, wax, snow, and similar materials can show luminous color where light travels through or within them before returning to the viewer.

`VAR_gurney_model_snow_from_granular_scattering_age_and_specularity` Specializes subsurface/granular scattering for snow: fresh powder has broad internal scattering and soft light leakage, while compacted or aged snow becomes darker and more specular as crystal structure changes. Use it when when snow must read as a light-scattering granular material rather than a uniformly white matte plane Avoid it when make every snow shadow blue or every old snow glossy; actual sky, ground, contamination, compaction, and light direction still govern .

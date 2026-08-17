---
object_id: PAT_project_caustic_light_from_refractive_or_reflective_curvature
object_type: pattern
name: Project Caustic Light From Refractive or Reflective Curvature
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
- caustics
- refraction
- reflection
- light_projection
cross_links:
- rel: related_to
  target_object_id: PAT_render_material_from_optical_response
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants: []
references: []
---

# Project Caustic Light From Refractive or Reflective Curvature

## Pattern Rule
**IF** curved transparent or reflective geometry concentrates directional light onto another surface
**THEN** derive the caustic's position, shape, and intensity from the incoming light and the refracting or reflecting curvature, placing the concentrated light on the actual receiver rather than as decorative bright pattern
**ELSE** omit the caustic when coherent directional illumination cannot plausibly be focused.

## Do
- Trace the dominant light direction through or off the curved surface before placing the bright projection.
- Let transparent-object caustics often occur inside or near the cast-shadow region where focused light re-enters the receiver.
- For moving water, allow wave curvature to create shifting concentrated bands or networks on submerged or nearby surfaces.
- Reduce or remove caustics in diffuse, deep, turbid, or heavily scattered conditions where the directional rays cannot remain coherent.

## Don't
- Paint random bright squiggles unrelated to source and geometry.
- Use caustics as generic material decoration on every glass or water surface.
- Ignore the receiving plane's orientation when shaping the projection.

## Checklist
- The caustic can be traced back to a plausible source and focusing geometry.
- Its shape follows the receiving surface and local curvature.
- Its visibility matches the coherence and strength of the illumination.

## Notes
A caustic is concentrated light, not a surface marking. Modeling it from source, curvature, and receiver keeps the effect physically motivated and portable across glass, water, polished curves, and other focusing geometries.

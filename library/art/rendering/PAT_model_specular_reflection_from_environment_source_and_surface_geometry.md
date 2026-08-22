---
object_id: PAT_model_specular_reflection_from_environment_source_and_surface_geometry
object_type: pattern
name: Model Specular Reflection From Environment, Source, and Surface Geometry
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
- material
- specular
- reflection
- highlight
- environment
cross_links:
- rel: related_to
  target_object_id: PAT_render_material_from_optical_response
- rel: related_to
  target_object_id: PAT_combine_multiple_colored_lights_additively
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_gurney_build_annular_highlights_from_oriented_microelements
  variant_name: Build Annular Highlights From Oriented Microelements
  variant_basis: context
  difference_from_foundation: 'Explains ring-like sparkle fields as orientation selection: only scratches, twigs, wires, fibers,
    or other small linear elements aligned favorably to the light/view geometry produce strong highlights.'
  when_to_use: Use when many differently oriented microelements create a structured sparkle field around the apparent light-source
    direction.
  when_not_to_use: Do not apply a uniform glitter texture; elements outside favorable orientations should remain weak or dark.
  absorbed_from_object_id: none
references: []
---

# Model Specular Reflection From Environment, Source, and Surface Geometry

## Pattern Rule
**IF** a glossy or reflective material shows view-dependent information from its surroundings
**THEN** establish the underlying form/local response first, then add the specular component as a distorted image of the environment and light sources governed by surface orientation and curvature
**ELSE** keep the material predominantly diffuse when reflections are too broad or weak to resolve.

## Do
- Treat highlights as reflections of light sources, not arbitrary white accents.
- Let convex curvature compress a wider environment and let local curvature stretch or squeeze reflected shapes.
- Include reflected information that originates outside the picture when the geometry would bring it into view.
- Increase the useful value range as reflectivity rises, while preserving enough diffuse/local response for the material being depicted.
- Keep separate light sources capable of producing separate highlight systems.

## Don't
- Place highlights by decoration or symmetry without regard to source/view geometry.
- Mirror the environment without distortion across curved surfaces.
- Erase all underlying material response unless the surface is genuinely mirror-like.

## Checklist
- Important highlights correspond to identifiable light sources.
- Reflection distortion follows the surface geometry.
- The specular layer and diffuse/local layer combine into one material rather than competing as unrelated effects.

## Notes
Specular reflection is an image-forming component laid over or alongside the material's diffuse response. Thinking of it as environment information makes glossy surfaces more causal and prevents highlights from becoming generic shine symbols.

`VAR_gurney_build_annular_highlights_from_oriented_microelements` Explains ring-like sparkle fields as orientation selection: only scratches, twigs, wires, fibers, or other small linear elements aligned favorably to the light/view geometry produce strong highlights. Use it when when many differently oriented microelements create a structured sparkle field around the apparent light-source direction Avoid it when apply a uniform glitter texture; elements outside favorable orientations should remain weak or dark .

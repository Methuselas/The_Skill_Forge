---
object_id: PAT_model_matte_form_from_primary_light_and_secondary_fill
object_type: pattern
name: Model Matte Form From Primary Light and Secondary Fill
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
- form
- light_shadow
- terminator
- core_shadow
- matte
cross_links:
- rel: related_to
  target_object_id: PAT_separate_local_value_from_light_and_shadow_effect
- rel: related_to
  target_object_id: PAT_ground_contacts_with_occlusion_shadow
- rel: related_to
  target_object_id: PAT_control_edge_hardness_from_form_light_and_focus
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants: []
references: []
---

# Model Matte Form From Primary Light and Secondary Fill

## Pattern Rule
**IF** an opaque matte form is lit by a dominant source plus weaker environmental illumination
**THEN** separate direct-light and shadow families at the terminator, model lit halftones by surface orientation, and let secondary fill determine the shadow-side lift, preserving a core only where the fill does not overlap it strongly
**ELSE** hand off to a material-specific optical model when reflection, transmission, scattering, or diffuse area lighting dominates.

## Do
- Identify the terminator from where the dominant source ceases to reach the form directly.
- Keep direct-light halftones distinct from the shadow family even when local value varies.
- Treat shadow as illumination by weaker sources, not as an absence of all light.
- Allow a core shadow only when primary and secondary source geometry leaves a comparatively underfilled band beyond the terminator.
- Under very broad diffuse light, replace the hard terminator/core expectation with gradual plane exposure to the large source.

## Don't
- Force a core shadow onto every rounded object.
- Use this matte-solid model as a universal shader for glass, metal, hair, clouds, foliage, or translucent material.
- Let reflected fill become so strong that it breaks the primary light-shadow hierarchy without an actual source to justify it.

## Checklist
- Direct light, form shadow, secondary fill, and contact/cast events have distinct causes.
- The terminator and core, when present, match the source geometry.
- The model hands off when another optical mechanism is visually dominant.

## Notes
The form principle is a useful baseline because it makes light causality explicit. Its value is strongest on opaque matte solids; it should not be generalized beyond the material conditions that produce it.

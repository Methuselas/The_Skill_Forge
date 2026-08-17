---
object_id: PAT_integrate_inserted_image_parts_with_scene_geometry_and_light
object_type: pattern
name: Integrate Inserted Image Parts With Scene Geometry and Light
library_path:
- art
- drawing
- sketching
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- sketching
- compositing
- perspective
- lighting
- reflections
cross_links:
- rel: related_to
  target_object_id: PAT_construct_reflections_across_arbitrary_planes
reference:
  source_title: Sketching the Basics
  author: Koos Eissen and Roselien Steur
confidence: high
references: []
variants: []
---

# Integrate Inserted Image Parts With Scene Geometry and Light

## Pattern Rule
**IF** an external image element such as a wheel, grille, texture, photograph, or rendered component is inserted into a drawing as though it belongs to the depicted scene
**THEN** make it obey the scene's perspective, scale, lighting, contact, occlusion, and reciprocal material effects before treating the composite as coherent
**ELSE** keep the element visibly separate as reference or underlay rather than disguising an unresolved insertion as finished scene content

## Do
- Rotate, scale, and distort the inserted element so its axes and surface orientation agree with the host object's perspective.
- Reconcile value, color, and highlight direction with the established illumination instead of preserving the source image's unrelated lighting.
- Solve contact and overlap edges so the part sits in or on the host form rather than floating above it.
- Add reciprocal effects when the material requires them, such as surrounding reflections appearing in chrome or a glossy inserted part affecting nearby highlights.
- Reduce source-specific sharpness, contrast, or texture when those qualities would make the inserted element read as a pasted photograph rather than part of the same drawing.

## Don't
- Do not screen-paste a correctly shaped part and assume matching silhouette is enough.
- Do not keep incompatible shadows, reflections, or highlights from the donor image when the host scene uses a different light setup.
- Do not use compositing to bypass unresolved geometry that the final image depends on.

## Checklist
- The inserted element shares the host object's perspective and physical scale.
- Its light and shadow relationships agree with the surrounding scene.
- Contact, occlusion, and overlap make the element occupy the intended depth.
- Reflective or glossy parts participate in the same environment rather than carrying isolated donor-image optics.
- The finished element reads as belonging to the drawing without requiring the source image to explain it.

## Notes
A borrowed visual component becomes part of a drawing only after it is reconciled with the scene that receives it. The fastest useful order is geometry first, then lighting and color, then contact and occlusion, then material-specific reciprocal effects. When those relationships are not worth solving, leaving the item visibly as reference is more truthful than forcing a false integration.

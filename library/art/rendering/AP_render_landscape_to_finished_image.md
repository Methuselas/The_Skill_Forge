---
object_id: AP_render_landscape_to_finished_image
object_type: ap
name: Render a Landscape to a Finished Image
library_path:
- art
- rendering
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- landscape
- rendering
- meso_structure
- atmosphere
- texture
- hierarchy
- continuity
cross_links:
- rel: supports
  target_object_id: PAT_construct_foliage_from_characteristic_mass_skeleton_and_value
- rel: supports
  target_object_id: PAT_model_water_surface_from_view_angle_reflection_transmission_and_wave_distortion
- rel: supports
  target_object_id: PAT_grade_depth_with_atmospheric_effect
- rel: supports
  target_object_id: PAT_render_material_from_optical_response
- rel: supports
  target_object_id: PAT_design_whole_picture_as_interlocking_shape_pattern
- rel: related_to
  target_object_id: AP_diagnose_and_repair_dead_color_relationships
- rel: related_to
  target_object_id: AP_diagnose_and_recover_failing_observed_rendering
- rel: related_to
  target_object_id: AP_render_from_photographic_reference_with_bounded_evidence
- rel: related_to
  target_object_id: AP_paint_directly_from_observation
- rel: supports
  target_object_id: PAT_model_daytime_sky_from_solar_glare_and_horizon_glow
- rel: supports
  target_object_id: PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum
- rel: supports
  target_object_id: PAT_control_color_layering_with_transparency_opacity_and_ground
- rel: supports
  target_object_id: PAT_control_edge_hardness_from_form_light_and_focus
reference:
  source_title: PASS Art canonical synthesis
  author: Multiple accepted sources
confidence: high
references: []
variants: []
---

# Render a Landscape to a Finished Image

## Objective
Carry a landscape from pictorial intent through large masses, characteristic medium-scale structure, internal color variation, atmosphere, selective material information, and final hierarchy without letting premature finish replace form or destroy earlier correct organization.

## Steps / Flow
1. **Choose the legal entry contract.** If no approved Drawing predecessor exists, use **root entry** and establish the landscape picture with this AP. If an approved Drawing predecessor exists, use **registered-successor entry**: inherit its camera, crop, composition, perspective, placement, major masses, scene inventory, and important overlap/contact decisions as locked. Do not manufacture Finished Pencils when an explicitly owning root/alternate workflow legitimately starts elsewhere.
2. **Establish or inherit the pictorial target and frame.** Apply `PAT_design_whole_picture_as_interlocking_shape_pattern` at this decision. In root entry, decide what the landscape is about, then choose viewpoint, crop, focal hierarchy, and large interlocking shape arrangement before surface work. In successor entry, preserve the accepted viewpoint/crop/composition and develop focal hierarchy only through legal appearance decisions rather than rearranging the picture.
3. **Establish or read the near-to-far organization.** In root entry, place foreground, middle distance, far distance, major overlaps, scale changes, and the expected atmospheric burden before detail begins. In successor entry, read those spatial relationships from the approved Drawing and develop depth through light, atmosphere, value, color, and edge behavior without moving the inherited structure.
4. **Lock the light model.** Use `PAT_characterize_light_source_by_relative_strength_apparent_size_and_spectrum` to characterize the dominant illumination before local color becomes authoritative, then establish the large light/shadow relationships.
5. **Block the major landscape masses.** Keep sky, terrain, vegetation groups, water, architecture, and other dominant regions as large readable masses. When the visible sky is a clear daytime field rather than cloud/haze dominated, apply `PAT_model_daytime_sky_from_solar_glare_and_horizon_glow` so the sky responds to both solar angle and horizon elevation rather than a generic vertical blue gradient.
6. **Pass the large-mass gate.** Each important mass needs a trustworthy silhouette, depth role, and parent light/value family. Decorative texture does not count as proof.
7. **Pass the meso-structure gate.** Apply `PAT_construct_foliage_from_characteristic_mass_skeleton_and_value`, `PAT_model_water_surface_from_view_angle_reflection_transmission_and_wave_distortion`, and `PAT_render_material_from_optical_response` at this decision. Before finish, give dominant natural forms characteristic medium-scale breakup. Delegate foliage, water, built forms, and known materials to their accepted owners. Generic brush noise does not count as structure.
8. **Develop color inside the accepted structure.** Use `PAT_control_color_layering_with_transparency_opacity_and_ground` when developing layered color while preserving the accepted value structure. Preserve large value families while adding intentional hue, chroma, and temperature variation within them.
9. **Apply atmospheric depth without erasing identity too early.** Apply `PAT_grade_depth_with_atmospheric_effect` at this decision. Distance should suppress microtexture before characteristic medium-scale form. If atmosphere turns a still-important form into generic mush, roll back the atmosphere pass.
10. **Add material and texture selectively.** Every texture mark should perform a form, material, light, spatial, or compositional job rather than merely signal a painterly landscape style.
11. **Resolve edge and focal hierarchy.** Use `PAT_control_edge_hardness_from_form_light_and_focus` to decide edge hierarchy, then reconcile near/far edge behavior, focal accents, contrast, and selective finish against the whole image.
12. **Read the result at three scales.** Small scale must preserve composition/value/depth; medium scale must preserve characteristic form structure; close scale may carry selective material/texture.
13. **Recover through existing owners.** Dead color routes to the color-repair AP; observed/reference failures route to the relevant recovery/reference AP; live paint-specific execution may delegate to the direct-painting AP. If successor rendering exposes a genuine Drawing defect, roll back to the owning Drawing AP rather than using Rendering authority to recompose or reconstruct it.
14. **Stop when more surface information weakens hierarchy.** Completion is a coherent landscape read, not maximum texture density.

## Notes
This AP intentionally does not invent a dedicated terrain/geology construction system. Where a dominant rock or landform requires knowledge the accepted library does not yet own, reduce unsupported structural specificity or use reliable reference rather than fabricating geological doctrine. Root authority and successor authority are distinct: root entry may establish the picture; registered-successor entry may develop appearance but cannot reopen an approved Drawing lockset.

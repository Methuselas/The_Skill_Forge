---
object_id: AP_package_approved_layout_into_executable_scene_plan
object_type: ap
name: Package Approved Layout Into Executable Scene Plan
library_path:
- art
- layout
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- layout
- animation
- scene_planning
- handoff
- camera
- production
cross_links:
- rel: related_to
  target_object_id: PAT_treat_layout_as_annotated_working_drawing_for_downstream_departments
- rel: supports
  target_object_id: PAT_decompose_animation_scene_into_registered_level_stack_for_independent_control
- rel: supports
  target_object_id: PAT_reuse_approved_production_art_by_reference_while_preserving_current_scene_identity
- rel: related_to
  target_object_id: AP_construct_a_shared_scene_perspective_field
reference:
  source_title: The Art of Layout and Storyboarding
  author: Mark T. Byrne
confidence: high
references: []
variants: []
---

# Package Approved Layout Into Executable Scene Plan

## Objective
Convert an approved shot from a successful layout into a complete production package that another department can execute without reconstructing the camera, layer, reuse, and scene intent from inference.

## Steps / Flow
1. **Lock the approved visible frame.** Record the actual crop or viewing field that defines what the audience sees rather than handing off only the larger artwork area.
2. **Record camera state.** Identify the starting frame and any stop, intermediate, rotation, pan, truck, tilt, or other camera states required to reproduce the approved move.
3. **Collect the spatial authority.** Keep the approved storyboard reference, layout, character poses, perspective information, registrations, and effects requirements together so the scene is not rebuilt from disconnected fragments.
4. **Define independently controlled artwork.** Use `PAT_decompose_animation_scene_into_registered_level_stack_for_independent_control` to identify the background, underlay, animated or held material, overlays, effects, or modern equivalents that must remain separately controllable.
5. **Record approved reuse.** Use `PAT_reuse_approved_production_art_by_reference_while_preserving_current_scene_identity` for any background, overlay, cycle, pose set, or other production art inherited from an earlier scene.
6. **Preserve scene identity and hookups.** Keep the current scene/sequence identity, relevant continuity state, directing notes, and departmental instructions attached to the current package even when some assets are reused.
7. **Run a handoff completeness check.** The package should answer: what is visible, what moves, how the camera moves, what artwork exists independently, what is reused, what must register, and how all pieces recombine.

## Notes
Byrne's individual layout folders and project-wide planning books are historical packaging systems for the same durable operation: after story and layout decisions are approved, make the shot executable without forcing downstream artists to rediscover its technical setup. Preserve information and relationships, not rostrum-camera-era paper conventions.

---
object_id: PAT_decompose_animation_scene_into_registered_level_stack_for_independent_control
object_type: pattern
name: Decompose Animation Scene Into Registered Level Stack For Independent Control
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
- layers
- registration
- compositing
- scene_planning
cross_links:
- rel: related_to
  target_object_id: PAT_separate_animating_environment_elements_from_static_background_for_independent_motion
- rel: related_to
  target_object_id: PAT_register_character_occlusion_with_shared_matchline_or_overlay
- rel: related_to
  target_object_id: AP_package_approved_layout_into_executable_scene_plan
reference:
  source_title: The Art of Layout and Storyboarding
  author: Mark T. Byrne
confidence: high
references: []
variants: []
---

# Decompose Animation Scene Into Registered Level Stack For Independent Control

## Pattern Rule
**IF** parts of an approved animation frame require different motion, occlusion, reuse, exposure, or compositing behavior
**THEN** decompose the scene into the minimum useful ordered stack of independently controlled elements while keeping every level registered to one approved scene geometry.

## Do
- Start from one spatially authoritative layout rather than independently inventing each layer.
- Separate only the elements whose motion, hold, occlusion, reuse, effects, or compositing behavior actually requires independent control.
- Record the front-to-back order with a level sketch, layer map, node structure, or equivalent notation so downstream production knows what lies above and below what.
- Keep all levels in the same coordinate, perspective, and registration system.
- When efficient, mark intended separations on copies or derivatives of one complete layout rather than prematurely redrawing every level from scratch.
- Verify recombination before handoff so the separated pieces reconstruct the approved frame and preserve all required overlaps.

## Don't
- Do not treat the finished frame as one monolithic image when its parts need independent behavior.
- Do not split every visible object into a separate layer merely because the software permits it.
- Do not let copied or separated levels drift away from the master layout geometry.
- Do not rely on file names or layer order alone when a downstream artist could still misunderstand occlusion or ownership.

## Checklist
- Each independently changing element has independent control.
- Layer order is explicit and reconstructs the approved frame.
- All levels share one spatial authority and registration.
- No required motion or occlusion is trapped inside the wrong layer.
- The decomposition is no more complex than production actually requires.

## Notes
Background, underlay, animation or held levels, overlays, and effects may be named with traditional cel terminology. The modern invariant is an ordered registered scene stack whose parts can move, hold, occlude, repeat, or composite independently without losing one shared geometry.

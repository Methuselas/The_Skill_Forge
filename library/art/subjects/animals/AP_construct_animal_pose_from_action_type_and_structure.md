---
object_id: AP_construct_animal_pose_from_action_type_and_structure
object_type: ap
name: Construct an Animal Pose From Action, Type, and Structure
library_path:
- art
- subjects
- animals
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- animals
- pose
- gesture
- construction
- locomotion
- anatomy
- action
cross_links:
- rel: supports
  target_object_id: PAT_establish_animal_type_from_proportional_ensemble
- rel: supports
  target_object_id: PAT_route_animal_gesture_through_governing_action_line
- rel: supports
  target_object_id: PAT_map_animal_pose_as_vertebral_and_limb_direction_framework
- rel: supports
  target_object_id: PAT_construct_animal_form_from_core_masses_framework_and_soft_parts
- rel: supports
  target_object_id: PAT_iterate_imagined_animal_action_until_function_and_expression_agree
- rel: related_to
  target_object_id: AP_prepare_construction_for_rendering
- rel: related_to
  target_object_id: AP_construct_animal_head_from_skull_type_to_living_features
- rel: supports
  target_object_id: PAT_orient_animal_body_in_depth_with_backline_and_transverse_axes
- rel: supports
  target_object_id: PAT_rebuild_animal_limb_joint_form_from_articulation_and_axis
- rel: supports
  target_object_id: PAT_read_animal_limb_muscle_groups_from_joint_axes_and_lines_of_pull
- rel: supports
  target_object_id: PAT_read_animal_trunk_muscles_from_spinal_axes_and_levers
- rel: supports
  target_object_id: PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive
- rel: supports
  target_object_id: PAT_block_quadruped_from_dorsal_axis_and_three_body_masses
- rel: supports
  target_object_id: PAT_stage_animal_mood_through_whole_body_pose_and_behavioral_cues
- rel: related_to
  target_object_id: AP_resolve_temporal_movement_for_pose_or_sequence
reference:
  source_title: PASS Art canonical synthesis
  author: Multiple accepted sources
confidence: high
references: []
variants: []
---

# Construct an Animal Pose From Action, Type, and Structure

## Objective
Build a structurally resolved animal pose that preserves species/type read, governing action, support mechanics, depth, articulation, and major anatomy strongly enough to hand off to rendering.

## Steps / Flow
1. **Enter with source mode and intended read.** Distinguish observed/reference construction from invented posing and decide whether action, type, mood, proportion, or another quality is the dominant goal. When mood or attitude is a primary design requirement and the pose is not already locked, apply `PAT_stage_animal_mood_through_whole_body_pose_and_behavioral_cues` here so the large posture and behavioral read are established before structural detail.
2. **Establish animal type before local identifiers.** Apply `PAT_establish_animal_type_from_proportional_ensemble` at this decision. Use the proportional ensemble so trunk, ground clearance, limb, neck, and head relationships carry the animal before fur, markings, horns, or facial detail.
3. **Establish the governing action.** Apply `PAT_route_animal_gesture_through_governing_action_line` at this decision. When the pose depends on selecting or understanding one phase of a continuing movement, delegate that bounded temporal decision to `AP_resolve_temporal_movement_for_pose_or_sequence` and return with the selected phase or phase logic. Route the body through the dominant action line and the relevant locomotion/action owner. The trunk must participate; limbs may not act around a passive body.
4. **Build the structural framework.** Apply `PAT_map_animal_pose_as_vertebral_and_limb_direction_framework` at this decision. When turn, recline, or foreshortening makes the trunk depth ambiguous, apply `PAT_orient_animal_body_in_depth_with_backline_and_transverse_axes`. Establish the vertebral route, shoulder/hip relationships, limb chains, pivots, contacts, and transverse depth axes before volume conceals them.
5. **Pass the mechanics gate.** Apply `PAT_iterate_imagined_animal_action_until_function_and_expression_agree` at this decision. For a terrestrial mammalian quadruped whose front and rear attachment systems are being treated as mirror-equivalent, apply `PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive`. Verify support, swing/suspension state, compression/extension, spinal participation, joint direction, and foreshortening. In an observed pose, return to evidence; in an invented pose, iterate mechanics until the visible action says what was intended.
6. **Build the major masses without moving trusted pivots.** Apply `PAT_construct_animal_form_from_core_masses_framework_and_soft_parts` at this decision. When the body plan is a four-legged animal and the major torso proportions or limb attachments are still uncertain, apply `PAT_block_quadruped_from_dorsal_axis_and_three_body_masses`; do not force that scaffold onto another body plan. Add trunk, girdle, head, and limb volume around the framework; volume may clarify the skeleton but may not silently relocate it.
7. **Recover species specificity structurally.** Invoke the accepted specialization that actually applies. If PASS lacks adequate species-specific ownership and reference is insufficient, keep the stronger general construction and reduce specificity rather than inventing real-animal anatomy.
8. **Rebuild articulation as the pose demands.** Apply `PAT_rebuild_animal_limb_joint_form_from_articulation_and_axis` so visible joint form changes with flexion, rotation, and load instead of rotating generic joint symbols with the limb.
9. **Add soft anatomy in service of the pose.** Apply `PAT_read_animal_limb_muscle_groups_from_joint_axes_and_lines_of_pull` and `PAT_read_animal_trunk_muscles_from_spinal_axes_and_levers` where limb or trunk anatomy materially explains the action. Muscle and fleshy forms modify the accepted framework without replacing whole-animal hierarchy.
10. **Keep the head subordinate to whole-animal structure.** Establish the head position, axis, broad cranial/facial mass, and neck relationship strongly enough that the pose reads. When the head itself requires structural development beyond that level, delegate the reusable sub-action to `AP_construct_animal_head_from_skull_type_to_living_features`; do not pull detailed facial construction into the whole-animal pose workflow.
11. **Pass the whole-animal reduction gate.** Remove surface detail mentally and verify type, action/mood, proportion, three-dimensional orientation, credible support, and coherent articulation.
12. **Hand off only after structure survives reduction.** Delegate to `AP_prepare_construction_for_rendering` when the animal works without decorative surface information.

## Notes
Observed and invented animals share most of the construction sequence; the key branch is how uncertainty is resolved. Observation returns to evidence. Invention returns to mechanics and iteration. This AP does not fabricate missing zoological specificity.

---
object_id: AP_construct_skip_from_step_hop_alternation
object_type: ap
name: Construct Skip From Step Hop Alternation
library_path:
- art
- subjects
- animation
- motion
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- skip
- locomotion
- rhythm
cross_links:
- rel: supports
  target_object_id: PAT_track_weight_support_and_transfer_through_every_pose
- rel: supports
  target_object_id: PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support
- rel: supports
  target_object_id: PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation
- rel: supports
  target_object_id: PAT_separate_timing_from_spacing_when_designing_motion
- rel: supports
  target_object_id: PAT_phrase_animation_timing_around_story_accents_and_action_beats
- rel: supports
  target_object_id: PAT_phase_offset_body_parts_to_break_mechanical_locomotion
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Skip From Step Hop Alternation

## Objective
Construct a skip as alternating step–hop support groups, then shape the relative step/hop timing and secondary action for character.

## Steps / Flow
1. Apply `PAT_track_weight_support_and_transfer_through_every_pose` to create a step onto one foot and establish it as the current support.
2. Continue the support audit through push-off, then apply `PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation` so the hop follows a readable unsupported arc.
3. Return that **same foot** to contact to complete the hop before changing support; apply `PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support` so the landing visibly receives the mass.
4. Switch to the other foot for the next step–hop group, preserving the support logic from `PAT_track_weight_support_and_transfer_through_every_pose`.
5. Apply `PAT_separate_timing_from_spacing_when_designing_motion` and `PAT_phrase_animation_timing_around_story_accents_and_action_beats` to shape launch, apex, return, and the unequal step/hop accents without mechanically dividing every interval.
6. Apply `PAT_phase_offset_body_parts_to_break_mechanical_locomotion` to the arms, head, and body rhythms without losing the alternating step–hop support pattern.

**Completion check**
- Each hop launches from and returns to the same support foot before the next step changes sides.
- The airborne phase forms a readable arc rather than a flat or walk-like transfer.
- Timing variation changes character without collapsing into a run or walk.

## Notes

Read the locomotion first as paired support events: step onto a foot, then leave and return to that foot. If the return contact or same-foot support is unclear, added arm swing and vertical bounce may suggest buoyancy but will not preserve the skip's characteristic grouping.

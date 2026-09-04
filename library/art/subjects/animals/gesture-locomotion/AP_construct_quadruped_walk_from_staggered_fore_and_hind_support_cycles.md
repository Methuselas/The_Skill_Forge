---
object_id: AP_construct_quadruped_walk_from_staggered_fore_and_hind_support_cycles
object_type: ap
name: Construct Quadruped Walk From Staggered Fore And Hind Support Cycles
library_path:
- art
- subjects
- animals
- gesture-locomotion
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- quadruped
- walk
- animal_locomotion
cross_links:
- rel: supports
  target_object_id: PAT_read_quadruped_locomotion_from_support_swing_and_suspension_phases
- rel: supports
  target_object_id: PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive
- rel: supports
  target_object_id: PAT_phase_offset_body_parts_to_break_mechanical_locomotion
- rel: supports
  target_object_id: PAT_stabilize_head_through_compensating_neck_motion_during_locomotion
- rel: supports
  target_object_id: PAT_track_animal_motion_through_moving_pivots_and_overlapping_arcs
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Quadruped Walk From Staggered Fore And Hind Support Cycles

## Objective
Construct a quadruped walk as coordinated forequarter and hindquarter support systems with staggered contacts, independent chest/pelvis phases, spinal response, head delay, and tail overlap.

## Steps / Flow
1. Apply `PAT_read_quadruped_locomotion_from_support_swing_and_suspension_phases` to establish the foreleg and hind-leg contact order.
2. Apply `PAT_read_quadruped_locomotion_from_support_swing_and_suspension_phases` and `PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive` to track support transfer between the front and rear systems without treating their roles as interchangeable.
3. Apply `PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive` and `PAT_phase_offset_body_parts_to_break_mechanical_locomotion` to offset chest and pelvis high/low phases from the actual support sequence.
4. Continue `PAT_phase_offset_body_parts_to_break_mechanical_locomotion` through the spine, then apply `PAT_stabilize_head_through_compensating_neck_motion_during_locomotion` so the head answers rather than copies the chest phase.
5. Apply `PAT_track_animal_motion_through_moving_pivots_and_overlapping_arcs`: drive the tail root from the hindquarters and carry the remaining chain through attachment-preserving overlap.

**Completion check**
- The animal’s weight transfer is readable through both pairs of limbs.
- Chest, pelvis, head, and tail do not peak mechanically together.

## Notes

Plot contacts and support intervals before judging surface motion; a convincing torso wave cannot rescue an impossible support sequence. Species, speed, and body plan may change the phase relationship, so preserve the established limb topology and derive chest, pelvis, head, and tail response from that specific gait.

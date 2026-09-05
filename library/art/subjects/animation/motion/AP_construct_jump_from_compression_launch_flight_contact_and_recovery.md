---
object_id: AP_construct_jump_from_compression_launch_flight_contact_and_recovery
object_type: ap
name: Construct Jump From Compression Launch Flight Contact And Recovery
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
- jump
- flight
- landing
cross_links:
- rel: supports
  target_object_id: PAT_define_task_objective_before_judging_human_action_mechanics
- rel: supports
  target_object_id: PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation
- rel: supports
  target_object_id: PAT_stage_contact_before_deformation_to_strengthen_impact
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Jump From Compression Launch Flight Contact And Recovery

## Objective
Construct a jump whose goal and approach determine the preparation and launch, then carry it through airborne trajectory, landing contact/compression, and recovery.

## Steps / Flow
1. Before compression, use `PAT_define_task_objective_before_judging_human_action_mechanics` to decide what the jump must accomplish: vertical height, horizontal distance, obstacle clearance, or another specific result. Also establish whether the launch begins from standing, walking, running, or a specialized approach.
2. Shape the preparation around that objective and approach. A standing vertical jump may load deeply into flexion before extending upward; a traveling jump can carry approach momentum into a differently directed launch. Do not treat every jump as the same cycle retimed or rotated.
3. Prepare the mass with a readable compression or anticipation appropriate to that launch.
4. Commit the launch by establishing the center-of-mass route that the unsupported body will follow.
5. During flight, use `PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation`: let the body rotate, articulate, tuck, stretch, or otherwise change pose around the established ballistic path rather than letting internal motion rewrite it.
6. Use `PAT_stage_contact_before_deformation_to_strengthen_impact` to separate first contact from the deformation that follows. Stage landing contact as the event that interrupts free flight and introduces a new external force; then compress or redirect the mass according to the landing.
7. Recover into the next state rather than ending at impact.

**Completion check**
- The jump's objective and approach are visible in its preparation and launch direction.
- The jump has a clear cause, ballistic phase, impact, and consequence.
- The airborne center-of-mass path remains coherent while the body changes pose around it.
- Landing contact visibly ends the ballistic phase and creates the next change in motion.

## Notes
The flight phase and the internal body performance are related but not identical problems. Choose the launch solution from the task first: jumps for height, distance, clearance, or another result may need different approach momentum, preparation, and launch vectors even though they share the same broad compression -> launch -> flight -> contact -> recovery structure. Solve the mass trajectory from the launch, then use the body action to express character, effort, rotation, or preparation for landing without casually steering the unsupported mass off that route.

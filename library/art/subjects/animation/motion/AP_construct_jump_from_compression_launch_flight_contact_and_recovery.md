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
  target_object_id: PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Jump From Compression Launch Flight Contact And Recovery

## Objective
Construct a jump from preparatory compression through launch, airborne trajectory, landing contact/compression, and recovery.

## Steps / Flow
1. Prepare the mass with a readable compression or anticipation.
2. Commit the launch by establishing the center-of-mass route that the unsupported body will follow.
3. During flight, use `PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation`: let the body rotate, articulate, tuck, stretch, or otherwise change pose around the established ballistic path rather than letting internal motion rewrite it.
4. Stage landing contact as the event that interrupts free flight and introduces a new external force; compress or redirect the mass according to the landing.
5. Recover into the next state rather than ending at impact.

**Completion check**
- The jump has a clear cause, ballistic phase, impact, and consequence.
- The airborne center-of-mass path remains coherent while the body changes pose around it.
- Landing contact visibly ends the ballistic phase and creates the next change in motion.

## Notes
The flight phase and the internal body performance are related but not identical problems. Solve the mass trajectory from the launch first, then use the body action to express character, effort, rotation, or preparation for landing without casually steering the unsupported mass off that route.

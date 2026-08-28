---
object_id: DRILL_calibrate_gravity_impact_and_deformation_with_bouncing_ball
object_type: drill
name: Calibrate Gravity Impact And Deformation With Bouncing Ball
library_path:
- art
- subjects
- animation
- timing
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- drill
- bouncing-ball
- gravity
- spacing
- impact
- squash-and-stretch
- ballistics
cross_links:
- rel: related_to
  target_object_id: PAT_separate_ballistic_center_of_mass_path_from_body_rotation_and_deformation
- rel: related_to
  target_object_id: PAT_control_animation_speed_with_slow_out_and_slow_in_spacing
- rel: related_to
  target_object_id: PAT_deform_animated_form_with_squash_and_stretch_while_preserving_volume
- rel: related_to
  target_object_id: PAT_stage_contact_before_deformation_to_strengthen_impact
- rel: related_to
  target_object_id: PAT_show_mass_through_resistance_to_acceleration_and_direction_change
reference:
  source_title: Advanced Animation
  author: Preston Blair
confidence: high
references: []
variants: []
target_skill: Coordinate ballistic path, gravity-driven spacing, impact deformation, and recovery in a stripped-down bouncing-ball animation before transferring the same causal structure into articulated character motion.
---

# Calibrate Gravity Impact And Deformation With Bouncing Ball

## Practice Task
Animate a plain elastic ball through one or more bounces, then translate the same causal structure into a simple hop or jump.

## Target Skill
Coordinate ballistic path, gravity-driven spacing, impact deformation, and recovery in a stripped-down bouncing-ball animation before transferring the same causal structure into articulated character motion.

## Setup
Use a plain ball or similarly simple elastic mass with no surface detail. Keep trajectory, spacing, and deformation as the only variables carrying the action.

## Instructions
1. Establish the successive contact points and airborne arcs before adding deformation.
2. Plot the center of the ball along a coherent ballistic path.
3. Open spacing progressively through the fall as gravity accelerates the ball downward.
4. Close spacing toward the top of the next arc as upward velocity is lost.
5. Keep the ordinary ball volume readable during slower airborne states.
6. Add directional stretch only where fast travel makes it useful, aligning the stretch to the current path rather than applying a generic vertical distortion.
7. At contact, squash in response to the impact while preserving believable total volume.
8. Let the rebound leave contact with spacing and deformation appropriate to the new upward phase rather than simply reversing the incoming drawings.
9. If the bounce is meant to lose energy, reduce later arc height and/or rebound energy coherently.
10. After the ball reads clearly, make a second pass that transfers the same causal structure into a simple hop or character jump: preparation and launch, ballistic travel, contact and compression, then recovery.

## Success Check
- The arc is readable from the center positions alone.
- Spacing opens through falling acceleration and closes approaching the apex.
- Impact deformation occurs at contact rather than before it.
- Stretch follows the direction of travel and squash responds to contact.
- Shape changes do not pull the center of mass away from the established path.
- Later bounces lose energy consistently when dissipation is intended.
- The hop or jump preserves the same physical logic after articulation is introduced.

## Common Failures
- Even spacing around the entire arc.
- Hanging too long or moving too quickly through the apex without intention.
- Squashing before contact.
- Stretching perpendicular to the direction of travel.
- Using squash and stretch to disguise a weak trajectory.
- Letting deformation move the center of mass off its path.
- Reversing the incoming drawings mechanically for the rebound.
- Making successive dissipating bounces identical.

## Notes
Blair uses the bouncing ball as a compact model for timing relationships that later reappear in hops, jumps, walks, runs, leaps, and skips. The drill isolates those relationships before the additional variables of articulated anatomy and character acting are introduced.

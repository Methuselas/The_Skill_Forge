---
object_id: PAT_stage_bird_landing_as_controlled_speed_shedding_matched_to_surface
object_type: pattern
name: Stage Bird Landing as Controlled Speed Shedding Matched to the Surface
library_path:
- art
- subjects
- animals
- gesture-locomotion
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_select_bird_flight_mode_by_available_source_of_lift_and_propulsion
tags:
- animal_drawing
- bird
- flight
- landing
- deceleration
- stall
- perch
- ground
- water
cross_links:
- rel: related_to
  target_object_id: PAT_control_bird_flight_with_wing_angle_of_attack_without_forcing_a_stall
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Stage Bird Landing as Controlled Speed Shedding Matched to the Surface

## Pattern Rule
**IF** a flying bird must land on ground, water, a perch, or another constrained target
**THEN** organize the approach around deliberate loss of forward and downward speed, then adapt body attitude, wing braking, leg extension, and final contact to the receiving surface

## Do
- Increase braking wing action and bring the body more upright as the bird approaches a ground contact.
- Extend the legs late enough to receive the body after the wings have reduced descent and forward speed.
- Let water birds use forward feet, body drag, and the water surface itself to dissipate remaining momentum when reference supports that landing style.
- For a precise elevated target, use an approach that can climb into the perch or edge so upward motion helps bleed forward speed before contact.
- Let final wing and tail adjustments correct the approach rather than locking the trajectory too early.

## Don't
- Do not let the bird hit the surface at cruising speed and stop without a braking phase.
- Do not use the same contact posture for water, flat ground, and a narrow perch.
- Do not extend the legs so early that they drag through the entire approach without function.

## Checklist
- Forward and downward speed visibly decrease before contact.
- Body, wings, tail, and legs cooperate in braking.
- The final contact mechanics fit the surface.
- Residual momentum is absorbed rather than disappearing on the contact frame.

## Notes
Treat landing as an accuracy-and-deceleration problem. Different receiving surfaces offer different ways to dispose of momentum, but the invariant is controlled speed shedding before and during contact rather than an abrupt stop.

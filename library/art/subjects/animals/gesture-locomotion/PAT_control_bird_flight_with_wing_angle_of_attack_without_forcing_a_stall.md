---
object_id: PAT_control_bird_flight_with_wing_angle_of_attack_without_forcing_a_stall
object_type: pattern
name: Control Bird Flight With Wing Angle of Attack Without Forcing a Stall
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
foundation_object_id: PAT_animate_flapping_bird_flight_from_power_recovery_and_body_response
tags:
- animal_drawing
- bird
- flight
- wing
- angle_of_attack
- lift
- drag
- stall
- landing
cross_links:
- rel: related_to
  target_object_id: PAT_match_bird_wing_planform_to_flight_performance_tradeoffs
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Control Bird Flight With Wing Angle of Attack Without Forcing a Stall

## Pattern Rule
**IF** a bird must climb, descend, slow, or alter lift without changing the whole wing planform
**THEN** rotate the wing's leading edge relative to the direction of airflow to change angle of attack, increasing or decreasing lift while watching for the drag and turbulence that appear when the angle becomes too steep

## Do
- Raise the leading edge when the action needs more lift for a climb or speed reduction.
- Reduce or reverse that angle when the flight path needs to descend.
- Treat angle of attack as a bounded control: increasing it can increase lift only up to the point where turbulence and drag destroy useful airflow.
- Use a deliberate near-stall or stall only when the action benefits from rapid speed shedding, such as final landing control.

## Don't
- Do not keep increasing wing pitch and assume lift will increase indefinitely.
- Do not treat a stall as a random drop disconnected from excessive angle and loss of smooth airflow.
- Do not confuse wing rotation with a change in the bird's entire trajectory unless the body and airflow support that result.

## Checklist
- Wing orientation changes relative to the flight path, not merely relative to the page.
- Climb/descent behavior agrees with the chosen angle.
- Excessive angle produces visible slowing or loss of lift rather than more effortless climb.
- Any deliberate stall has a clear behavioral purpose.

## Notes
Webster uses angle of attack as the practical control linking wing orientation to lift, drag, climb, descent, and stall. The key animation distinction is that more angle is not always more lift: beyond a critical point the flow breaks down and the bird loses support.

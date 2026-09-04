---
object_id: PAT_assign_fish_fins_by_propulsion_lift_stability_and_maneuverability
object_type: pattern
name: Assign Fish Fins by Propulsion, Lift, Stability, and Maneuverability
library_path:
- art
- subjects
- animals
- anatomy
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_read_animal_locomotion_as_a_functional_performance_tradeoff
tags:
- animal_drawing
- fish
- fins
- anatomy
- propulsion
- lift
- stability
- maneuverability
- steering
cross_links:
- rel: related_to
  target_object_id: PAT_construct_fish_body_plan_from_habitat_speed_and_maneuverability
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants:
- variant_id: flexible_paired_fin_fine_control
  variant_name: Flexible Paired-Fin Fine Control
  variant_basis: context
  difference_from_foundation: Flexible paired fins can work together for tight pivoting, pitch adjustment, braking, or even direct reverse movement with little whole-body translation.
  when_to_use: Use when the species has sufficiently articulated pectoral or paired fins and the action needs low-speed positional control.
  when_not_to_use: Do not use for rigid paired fins whose structure does not permit comparable folding or reorientation.
  absorbed_from_object_id: none
---

# Assign Fish Fins by Propulsion, Lift, Stability, and Maneuverability

## Pattern Rule
**IF** a fish's fin system must be constructed or interpreted for believable movement
**THEN** assign each fin or fin pair a working role in propulsion, lift, stability, braking, steering, or fine maneuvering, and place or fold it according to that role rather than treating all fins as equivalent ornaments
**ELSE** follow reliable species reference when a fin has become specialized beyond the common pattern

## Do
- Treat the caudal fin and caudal peduncle as the main sustained or high-speed propulsive system in typical tail-driven fish.
- Use pectoral fins for dynamic lift, low-speed propulsion, braking, steering, and precise positional adjustments where the species permits that range.
- When paired fins are flexible enough, oppose or coordinate them for tight pivots, local pitch changes, braking, or direct backward movement without first turning the whole fish.
- Use pelvic and anal fins primarily to stabilize the body and help control unwanted rotation.
- Use the dorsal fin chiefly as a stabilizing and maneuvering surface unless the species demonstrates a specialized propulsive use.
- Let fin placement change the performance reading: more central working surfaces can support maneuverability, while strong rearward concentration can support acceleration and tail-driven speed.
- Fold or draw fins closer to the body when reference shows drag reduction at higher speed.

## Don't
- Do not draw every fin as a rigid triangular plate with the same mechanical purpose.
- Do not make rigid fins furl or articulate beyond what the species structure allows.
- Do not assign propulsion to a fin solely because it is visually large.
- Do not ignore the interaction between fin placement and the fish's overall body plan.

## Checklist
- Each major fin has a clear locomotor or stabilizing role.
- Fin stiffness and articulation agree with the species' structure.
- The fin arrangement supports the intended balance of speed and maneuverability.
- Any folded or deployed state has a mechanical reason.

## Notes
Treat fins as a coordinated control system. Different fins contribute differently to propulsion, lift, stability, roll control, braking, and fine maneuvering, and some species alter or specialize those roles. Building the fins as working surfaces makes later swimming animation easier to reason about than attaching generic fin symbols to a fish-shaped body.

The `flexible_paired_fin_fine_control` variant applies when the paired fins can articulate substantially. Such fins can work together to pivot around the body center, alter pitch with little translation, brake, and in some fish produce direct reverse travel. Rigid pectoral systems do not inherit that maneuvering vocabulary merely because they occupy the same anatomical position.

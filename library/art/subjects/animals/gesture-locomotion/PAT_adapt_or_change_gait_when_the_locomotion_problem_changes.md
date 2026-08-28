---
object_id: PAT_adapt_or_change_gait_when_the_locomotion_problem_changes
object_type: pattern
name: Adapt or Change Gait When the Locomotion Problem Changes
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
foundation_object_id: PAT_read_animal_locomotion_as_a_functional_performance_tradeoff
tags:
- animal_drawing
- locomotion
- gait_transition
- speed
- resistance
- stability
- environment
- behavior
cross_links: []
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Adapt or Change Gait When the Locomotion Problem Changes
## Pattern Rule
**IF** speed, resistance, stability, energy demand, environment, or behavioral objective changes enough that the current gait is no longer efficient or workable
**THEN** let the existing gait progressively adapt or transition into a different locomotor solution instead of preserving one cycle unchanged through the new conditions

## Do
- Track how stride, limb lift, torso attitude, support, and whole-body coordination change before and during the transition.
- Let increased environmental resistance or changing depth alter the body's use of its limbs before a full mode change such as walking to swimming.
- Let behavioral shifts such as stalking to pursuit reorganize posture, acceleration, and gait rather than merely speeding the same pose cycle.
- Treat the preparation as potentially progressive even when the actual gait switch is comparatively abrupt.
- Verify species-specific transition details from reference when accuracy matters.

## Don't
- Do not preserve one walk or run cycle and only retime it when the mechanical problem has changed.
- Do not assume every gait transition occurs at one universal speed or stride count.
- Do not change gait without a corresponding change in support, body organization, or functional demand.

## Checklist
- The condition that makes the old gait inadequate is identifiable.
- The body begins adapting before or at the transition.
- The new gait solves the changed locomotion problem more effectively.
- Transition timing remains species- and context-dependent.

## Notes
Gaits are solutions to conditions, not permanent labels attached to an animal. Rising resistance, a need for more stability, a shift from stealth to pursuit, or a speed threshold can all reorganize the whole locomotor pattern.

---
object_id: PAT_choose_aquatic_propulsive_stroke_between_rowing_and_hydrofoil_action
object_type: pattern
name: Choose Aquatic Propulsive Stroke Between Rowing and Hydrofoil Action
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
foundation_object_id: PAT_read_animal_locomotion_as_a_functional_performance_tradeoff
tags:
- animal_drawing
- animation
- aquatic
- swimming
- fins
- rowing
- hydrofoil
- propulsion
- drag
- lift
cross_links:
- rel: related_to
  target_object_id: PAT_assign_fish_fins_by_propulsion_lift_stability_and_maneuverability
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Choose Aquatic Propulsive Stroke Between Rowing and Hydrofoil Action

## Pattern Rule
**IF** a fin or limb is actively driving an aquatic animal through the water
**THEN** decide whether the stroke works primarily as a rowing surface that pushes against the water or as a hydrofoil that changes angle of attack to generate lift and thrust, and animate power and recovery accordingly
**ELSE** follow reference when the animal blends or switches the two mechanisms

## Do
- For rowing action, present a broad working surface against the water during the power phase, then reduce resistance on recovery by changing angle, folding, or otherwise narrowing the effective surface.
- Use rowing when the action needs conspicuous acceleration, braking, or tight maneuvering from a strong power stroke.
- For hydrofoil action, move the working surface at a shallower angle through the water and vary its angle of attack so lift contributes to thrust.
- Let a hydrofoil system produce a smoother velocity profile when both halves of the cycle can contribute useful thrust.
- Allow an animal to change stroke strategy when speed or maneuvering demands change rather than treating one mechanism as permanent.

## Don't
- Do not animate the recovery of a rowing stroke with the same broad drag-producing presentation as its power phase.
- Do not use a rigid back-and-forth paddle motion when the surface is functioning as a foil.
- Do not assume hydrofoil action means the surface stays at one fixed angle through the cycle.
- Do not infer the stroke mechanism from silhouette alone when motion reference shows a different use.

## Checklist
- The working surface has a readable power relationship with the surrounding water.
- Rowing recovery reduces drag relative to the power stroke.
- Hydrofoil action changes orientation rather than merely sweeping flat through the water.
- The chosen mechanism supports the intended balance of acceleration, efficiency, and maneuverability.

## Notes
An aquatic appendage can produce useful motion through two broad routes. Rowing relies on a strong difference between a drag-producing power phase and a lower-drag recovery. Hydrofoil action treats the fin or limb more like a lifting surface whose changing orientation turns motion through the water into thrust. The same animal may favor different mixes of these mechanics at different speeds.

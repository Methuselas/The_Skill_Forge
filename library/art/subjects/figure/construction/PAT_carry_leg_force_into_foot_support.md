---
object_id: PAT_carry_leg_force_into_foot_support
object_type: pattern
name: Carry Leg Force Into Foot Support
library_path:
- art
- subjects
- figure
- construction
stage_binding: 2 block
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
- figure_drawing
- foot_support
- balance
- force_direction
cross_links:
- rel: supports
  target_object_id: AP_notate_a_figure_in_structural_order
- rel: related_to
  target_object_id: PAT_construct_foot_as_soft_tissue_support_wedge
- rel: related_to
  target_object_id: PAT_choose_s_or_b_leg_rhythm_by_view
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
references: []
variants:
- variant_id: VAR_bridgman_settle_foot_from_outer_edge_inward
  variant_name: Settle Weight From the Outer Heel Side Toward the Inner Foot
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a directional weight-bearing sequence to the existing foot-support rule: in ordinary settling
    contact, the outer/heel side meets first and the foot then settles inward while the arches adjust to keep the sole functionally
    related to the ground.'
  when_to_use: Use when designing walking, landing, or weight-settling poses where the foot's contact sequence should explain
    the leg force.
  when_not_to_use: Do not universalize this into every planted foot or every gait phase; toe-first, medial-edge, pointe, crouched,
    or specialized contacts follow the actual action instead.
  absorbed_from_object_id: none
---

# Carry Leg Force Into Foot Support

## Pattern Rule
**IF** a Stage 2 leg bears weight, pushes, lands, braces, or otherwise transfers force through the ankle
**THEN** construct the foot wedge as the terminal response to that force so its stance, contact, and direction make the leg action believable
**ELSE** when the foot is airborne, still orient it as a coherent continuation of the leg rather than an independent swivel

## Do
- Track the bearing of the leg into the ankle, then show the foot receiving or redirecting that force through its support plane.
- Use an outward reversal when it fits the stance, but judge the actual direction from the pose, viewpoint, and contact.
- Establish heel, forefoot, arch, and toe direction early enough that balance can be tested before anatomy or rendering.
- Treat a foot that looks wrong in Stage 2 as a construction error, not a detail problem.

## Don't
- Point every foot outward as a formula regardless of the action.
- Let the ankle terminate without a readable support, propulsion, or directional relationship.
- Use shoes, shadow, grass, cropping, or blur to conceal an unresolved foot.
- Assume Stage 3 anatomy or Stage 4 polish will repair a bad stance.

## Checklist
- The foot direction answers the force carried through the leg.
- Ground contact, push-off, landing, or airborne orientation is immediately legible.
- The ankle-to-foot transition does not break the limb chain.
- The figure's balance or momentum remains credible when detail is removed.

## Notes
Hogarth's outward foot arrows demonstrate a common support response, not a universal pointing rule. The underlying requirement is a convincing transfer of force. This Stage 2 test applies equally to inward turns, crossed stances, pointe work, toe push-off, side views, and other context-specific foot actions.

`VAR_bridgman_settle_foot_from_outer_edge_inward` retains **Settle Weight From the Outer Heel Side Toward the Inner Foot** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

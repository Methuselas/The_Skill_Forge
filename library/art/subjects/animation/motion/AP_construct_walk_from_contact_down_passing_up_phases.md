---
object_id: AP_construct_walk_from_contact_down_passing_up_phases
object_type: ap
name: Construct Walk From Contact Down Passing Up Phases
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
- walk
- locomotion
- support
cross_links:
- rel: supports
  target_object_id: PAT_track_weight_support_and_transfer_through_every_pose
- rel: supports
  target_object_id: PAT_preserve_world_contact_under_relative_camera_subject_and_background_motion
- rel: supports
  target_object_id: PAT_design_walk_from_character_state_and_attitude
- rel: supports
  target_object_id: PAT_preserve_support_logic_while_distorting_locomotion_design
- rel: supports
  target_object_id: PAT_articulate_foot_roll_to_control_stride_weight_and_character
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Walk From Contact Down Passing Up Phases

## Objective
Construct a walk from the repeating support grammar contact → down → passing → up → opposite contact, anchor stride and travel from the contacts, then vary the phases for character.

## Steps / Flow
1. Use `PAT_design_walk_from_character_state_and_attitude` when character state should alter the gait. Place the two opposite contacts and use successive contact positions to establish stride length, travel distance, and the number of steps needed to cross the shot.
2. Use `PAT_track_weight_support_and_transfer_through_every_pose` while creating the down phase where the supporting leg accepts weight and the body mass drops.
3. Create the passing phase where the free leg moves past support.
4. Use `PAT_articulate_foot_roll_to_control_stride_weight_and_character` when foot articulation materially controls push-off, stride, or character; create the up phase where push-off raises the mass before the next contact.
5. For a nominally steady walk, keep overall forward body travel sufficiently even while the vertical mass eases through low and high phases; do not let the rise-and-fall spacing make forward progress visibly stick.
6. Give the extended leading leg enough readable presence around contact that neighboring bent-leg poses do not visually erase the straight-leg event.
7. Choose the implementation branch deliberately. Use `PAT_preserve_world_contact_under_relative_camera_subject_and_background_motion` to protect planted contact: for an advancing cycle, move the character through space; for an on-the-spot cycle, reconcile foot travel with equal-and-opposite ground or background translation so planted support does not slide.
8. Test the cycle, then use `PAT_preserve_support_logic_while_distorting_locomotion_design` when layering stylized or character-specific deviations; do not lose the support logic that makes the action read as a walk.

**Completion check**
- The support foot and body mass agree at every phase.
- Contact spacing produces the intended stride and total travel.
- Forward progress remains coherent with the intended pace instead of surging with the vertical bounce.
- A planted foot does not slide in either advancing or on-the-spot implementation.
- The cycle reads as a walk before secondary animation is added.

## Notes

Use the named phases as a diagnostic grammar, not as a demand that every walk receive equal spacing or identical poses. Character, speed, footwear, load, and terrain may compress a phase, but each departure must preserve intelligible support transfer and planted-foot behavior.

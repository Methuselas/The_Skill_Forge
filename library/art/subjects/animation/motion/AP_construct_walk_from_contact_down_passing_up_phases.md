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
  target_object_id: PAT_set_walk_tempo_from_step_duration_before_detailing_motion
- rel: supports
  target_object_id: PAT_track_weight_support_and_transfer_through_every_pose
- rel: supports
  target_object_id: PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support
- rel: supports
  target_object_id: PAT_articulate_foot_roll_to_control_stride_weight_and_character
- rel: supports
  target_object_id: PAT_separate_timing_from_spacing_when_designing_motion
- rel: supports
  target_object_id: PAT_preserve_world_contact_under_relative_camera_subject_and_background_motion
- rel: supports
  target_object_id: PAT_design_walk_from_character_state_and_attitude
- rel: supports
  target_object_id: PAT_adapt_human_walking_mechanics_to_surface_slope_and_footwear_constraints
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
1. Apply `PAT_set_walk_tempo_from_step_duration_before_detailing_motion` to place the two opposite contacts and coordinate step duration, stride length, travel distance, and the number of steps needed to cross the shot.
2. Apply `PAT_track_weight_support_and_transfer_through_every_pose` and `PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support` to create the down phase where the supporting leg accepts weight and the body mass drops. Use `PAT_articulate_foot_roll_to_control_stride_weight_and_character` when the contact progression materially affects the gait.
3. Continue `PAT_track_weight_support_and_transfer_through_every_pose` through the passing phase as the free leg moves past the planted support.
4. Continue `PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support` through the up phase so push-off raises and redirects the mass before the next contact.
5. Apply `PAT_separate_timing_from_spacing_when_designing_motion` to keep overall forward travel sufficiently even while the vertical mass eases through low and high phases; do not let rise-and-fall spacing make forward progress visibly stick.
6. Give the extended leading leg enough readable presence around contact that neighboring bent-leg poses do not visually erase the straight-leg event.
7. Choose the implementation branch deliberately. For an advancing cycle, move the character through space; for an on-the-spot cycle or moving camera/background, apply `PAT_preserve_world_contact_under_relative_camera_subject_and_background_motion` so planted support does not slide.
8. Test the generic cycle first, then apply `PAT_design_walk_from_character_state_and_attitude` for character-specific deviations. When surface, slope, resistance, or footwear changes the contact problem, apply `PAT_adapt_human_walking_mechanics_to_surface_slope_and_footwear_constraints` before accepting the variation.

**Completion check**
- The support foot and body mass agree at every phase.
- Contact spacing produces the intended stride and total travel.
- Forward progress remains coherent with the intended pace instead of surging with the vertical bounce.
- A planted foot does not slide in either advancing or on-the-spot implementation.
- The cycle reads as a walk before secondary animation is added.

## Notes

Use the named phases as a diagnostic grammar, not as a demand that every walk receive equal spacing or identical poses. Character, speed, footwear, load, and terrain may compress a phase, but each departure must preserve intelligible support transfer and planted-foot behavior.

---
object_id: AP_construct_sneak_from_delayed_weight_transfer_and_cautious_support
object_type: ap
name: Construct Sneak From Delayed Weight Transfer And Cautious Support
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
- sneak
- locomotion
- weight_transfer
cross_links:
- rel: supports
  target_object_id: PAT_design_walk_from_character_state_and_attitude
- rel: supports
  target_object_id: PAT_control_animation_speed_with_slow_out_and_slow_in_spacing
- rel: supports
  target_object_id: PAT_track_weight_support_and_transfer_through_every_pose
- rel: supports
  target_object_id: PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support
- rel: supports
  target_object_id: PAT_preserve_support_logic_while_distorting_locomotion_design
- rel: supports
  target_object_id: PAT_phrase_animation_timing_around_story_accents_and_action_beats
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants: []
---

# Construct Sneak From Delayed Weight Transfer And Cautious Support

## Objective
Construct a sneak by delaying commitment to new support: reach, test contact, retain rear support, then transfer mass cautiously before the next reach.

## Steps / Flow
1. Apply `PAT_design_walk_from_character_state_and_attitude` to choose a guarded or low body attitude whose stride, posture, and balance behavior all serve caution.
2. Extend the new foot without immediately committing weight, then apply `PAT_control_animation_speed_with_slow_out_and_slow_in_spacing` to slow it into deliberate, quiet contact.
3. Apply `PAT_track_weight_support_and_transfer_through_every_pose`: keep the body supported by the rear leg while the new contact is tested.
4. After contact, apply `PAT_encode_locomotion_weight_through_vertical_mass_shift_and_support` to any recoil or compression, but retain rear support until the new foothold is trusted. When the recoil is strongly stylized, use `PAT_preserve_support_logic_while_distorting_locomotion_design` as the plausibility gate.
5. Continue `PAT_track_weight_support_and_transfer_through_every_pose` and transfer the mass only after the new support is established.
6. Recover into the next cautious reach. Apply `PAT_phrase_animation_timing_around_story_accents_and_action_beats` when a faster or more violent sneak compresses the phrase, but keep the delayed-commitment logic rather than turning it into an ordinary run.

**Completion check**
- The incoming foot decelerates into contact rather than striking with an ordinary walking cadence.
- Rear support remains available until the new contact is trusted.
- The gait reads as cautious acquisition of support rather than an ordinary walk or run.

## Notes

Contact is not yet commitment. Track when the body mass actually crosses into the new support base; transferring it at first touch removes the test-and-trust interval, while holding it too long without compensating balance makes the reach mechanically impossible.

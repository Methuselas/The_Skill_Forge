---
object_id: PAT_control_animation_speed_with_slow_out_and_slow_in_spacing
object_type: pattern
name: Control Animation Speed With Slow-Out and Slow-In Spacing
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
foundation_object_id: PAT_phrase_animation_timing_around_story_accents_and_action_beats
tags:
- animation
- timing
- spacing
- slow_out
- slow_in
- acceleration
- deceleration
cross_links:
- rel: related_to
  target_object_id: PAT_inbetween_motion_along_arcs_revealed_by_neighboring_frames
- rel: related_to
  target_object_id: PAT_carry_secondary_parts_through_overlap_follow_through_and_drag
- rel: related_to
  target_object_id: PAT_design_animation_extreme_as_storytelling_pose
reference:
  source_title: Drawn to Life, Volume One
  author: Walt Stanchfield
confidence: high
references: []
variants:
- variant_id: VAR_whitaker_construct_graduated_spacing_by_recursive_fractional_division
  variant_name: Construct Graduated Spacing by Recursive Fractional Division
  variant_basis: method_sequence
  difference_from_foundation: Constructs a controlled ease between known endpoints by repeatedly dividing the remaining travel, most practically by halves and where useful by thirds or quarters, instead of eyeballing every intermediate gap.
  when_to_use: Use when the endpoints and duration are already known and the action needs a deliberate graduated slow-out, slow-in, or related easing profile.
  when_not_to_use: Do not force recursive fractional spacing onto impacts, snaps, constant-speed mechanical motion, strongly asymmetric acceleration, or any action whose character requires a different spacing design.
  absorbed_from_object_id: none
---

# Control Animation Speed With Slow-Out and Slow-In Spacing

## Pattern Rule
**IF** an animated form must leave a pose gradually, arrive into a pose gradually, or otherwise show acceleration or deceleration instead of uniform speed
**THEN** vary the spacing of successive states so drawings cluster where motion is slow and spread farther apart where motion is fast
**ELSE** keep spacing even or abrupt when constant-speed, mechanical, impact, or snap motion is the intended effect

## Do
- For a slow-out, keep the first successive states close to the starting pose, then increase the travel between later states as the action gains speed.
- For a slow-in, reduce the travel between successive states as the action approaches its destination so the movement eases into the pose instead of stopping instantly.
- Inspect several surrounding extremes or breakdowns before assigning spacing; the intended acceleration pattern belongs to the action, not to one isolated interval.
- Separate the spacing profiles of components that obey different forces inside the same action; a body mass can ease through a reversal while an arm, tool, or attached part follows a different acceleration pattern.
- Coordinate spacing with follow-through so a primary mass may settle while a tail, garment edge, hair mass, or other attached form continues through its own delayed ease.
- Preserve the path and volume of the moving form while changing spacing; acceleration should not introduce a new trajectory or structural distortion unless the action calls for it.

## Don't
- Do not place inbetweens at equal spatial intervals when the action is meant to accelerate away from or decelerate into an extreme.
- Do not add easing automatically to impacts, snaps, deliberate mechanical motion, or another action whose character depends on abruptness.
- Do not confuse a slow-out with a hold; the form should still progress away from the starting state even when early spacing is tight.
- Do not let a secondary part stop merely because the primary body has stopped when the established follow-through requires additional settling frames.
- Do not put the whole figure, tool, and appendages on one shared easing curve when their masses, drivers, or effort relationships require different spacing.

## Checklist
- Tight spacing appears near states where the action is intended to move slowly.
- Wider spacing corresponds to the faster portion of the same movement.
- The direction of acceleration or deceleration matches the action's start and destination.
- Secondary follow-through can use a later or different ease without breaking its attachment to the primary motion.
- The spacing choice supports the intended character of motion rather than applying easing by habit.
- Components that serve different force relationships do not accidentally share an identical spacing profile.

## Notes
Slow-out and slow-in are spacing controls around poses. They translate the intended change of speed into the distance traveled between successive drawings: compact spacing reads slower, wider spacing reads faster. Their value is greatest when they reinforce the phrasing of the action; they are not a mandatory smoothing filter for every transition.

- Keep timing and spacing conceptually separate. Closely packed positions read slower; wider gaps read faster. Gradually widen or compress gaps to accelerate or decelerate without changing total duration.
- Use exposure charts or equivalent planning to make the internal spacing map explicit before interpolation.
- Perspective can make equal world-space travel project to unequal screen-space gaps; use projection as evidence, then cheat it when a different screen-space spacing reads better.
- `VAR_whitaker_construct_graduated_spacing_by_recursive_fractional_division` provides a construction method when endpoints and duration are fixed: recursively divide the travel by halves, or selectively by thirds or quarters, to build a deliberate easing progression without treating that proportion as a universal motion law.

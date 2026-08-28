---
object_id: PAT_build_repeat_pan_from_seamless_cycle_and_nonrevealing_landmarks
object_type: pattern
name: Build Repeat Pan From Seamless Cycle And Nonrevealing Landmarks
library_path:
- art
- layout
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- layout
- animation
- repeat_pan
- background
- cycling
- seam
cross_links:
- rel: related_to
  target_object_id: PAT_repeat_with_variation_to_balance_coherence_and_interest
- rel: related_to
  target_object_id: PAT_break_periodic_motion_aliasing_before_repeated_elements_strobe
- rel: related_to
  target_object_id: PAT_preserve_world_contact_under_relative_camera_subject_and_background_motion
reference:
  source_title: The Art of Layout and Storyboarding
  author: Mark T. Byrne
confidence: high
references: []
variants: []
---

# Build Repeat Pan From Seamless Cycle And Nonrevealing Landmarks

## Pattern Rule
**IF** a moving background must repeat for sustained travel
**THEN** design the layout as a closed visual loop whose endpoints match and whose seam and repeated landmarks do not reveal the cycle.

## Do
- Make the first and last repeat states spatially and visually compatible before testing the loop.
- Overlap or register adjoining background sections so the handoff cannot expose a gap.
- Use continuous or visually forgiving forms across the seam when they can disguise the transition.
- Avoid unique landmarks whose repeated return would advertise the cycle, such as a distinctive sign, sun or moon position, held figure, or singular piece of furniture.
- When a short loop becomes obvious, extend the cycle, add another section, or introduce a separately repeating foreground element to vary what crosses the screen.
- Test the result in playback; a technically perfect still-image seam can still betray itself through periodic timing or repeated landmarks.

## Don't
- Do not assume matching endpoints alone make a convincing repeat.
- Do not put a conspicuous one-off landmark inside a short loop unless its recurrence is intentional.
- Do not let multiple repeating layers expose their seams at the same instant when their combined motion should feel continuous.
- Do not preserve a cheap repeat when the visible periodicity materially lowers the scene's intended production value.

## Checklist
- The loop closes without a visible jump.
- The seam is hidden by compatible geometry, overlap, or another deliberate transition.
- Repeated landmarks do not announce the cycle before the intended duration is complete.
- Playback remains convincing across several passes, not just one switch.
- Character or vehicle travel remains compatible with the repeated background motion.

## Notes
This is an animation-layout specialization. The transferable decision is endpoint closure plus seam concealment plus suppression of cycle tells; historical peg and camera-bed mechanics are implementation details rather than the rule.

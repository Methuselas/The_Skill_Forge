---
object_id: PAT_use_elongated_inbetween_to_imply_fast_motion_blur
object_type: pattern
name: Use Elongated Inbetween To Imply Fast Motion Blur
library_path:
- art
- subjects
- animation
- inbetweening
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animation
- smear
- inbetween
- fast_motion
cross_links: []
reference:
  source_title: The Animator's Survival Kit
  author: Richard Williams
confidence: high
references: []
variants:
- variant_id: VAR_whitaker_leave_detached_speed_trail_to_bridge_wide_motion_gaps
  variant_name: Leave Detached Speed Trail To Bridge Wide Motion Gaps
  variant_basis: method_sequence
  difference_from_foundation: Uses a short-lived path-derived trail that remains behind the fast subject and dissipates where the motion created it, rather than stretching the subject itself into the connecting intermediate.
  when_to_use: Use when fast motion leaves such a wide visual gap between readable poses that a residual trail, drybrush, or similar directional connector helps the eye follow the path without requiring another full pose.
  when_not_to_use: Do not add decorative speed lines when the motion already connects clearly, and do not attach the trail to the subject like streamers that travel with it.
  absorbed_from_object_id: none
---

# Use Elongated Inbetween To Imply Fast Motion Blur

## Pattern Rule
**IF** very fast motion crosses enough distance that a normal intermediate drawing would read as a separate pose or strobe
**THEN** Use a deliberately elongated or smeared intermediate drawing to connect readable endpoints during very fast motion

## Do
- Keep departure and arrival states clear.
- Stretch, smear, or connect form along the intended path only in the fast intermediate.
- Preserve enough volume and direction for the smear to belong to the same subject.

## Don't
- Do not add a smear to slow action or use uncaused speed graphics as decoration; a path-derived residual trail is a separate grounded variant only when fast motion needs that connector.

## Checklist
- The fast transition reads smoothly without losing identity.

## Notes
Williams uses the elongated inbetween as a fast-motion connector that belongs to the moving form itself. Whitaker and Halas provide a distinct alternative when the object has already outrun the readable intermediate: a residual drybrush or speed trail can be generated along the actual path, left behind as the subject advances, and dissipated where it was created. The two methods solve the same perceptual gap in different ways; neither should become generic ornament.

`VAR_whitaker_leave_detached_speed_trail_to_bridge_wide_motion_gaps` keeps the endpoints as ordinary readable poses and lets the connector exist briefly in the vacated path. New trail material should originate from the current fast action while older material dies away; after an exit, the residual can remain for a few frames as evidence of the motion, but should decay rather than behaving like a separate moving ribbon.

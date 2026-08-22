---
object_id: PAT_render_motion_blur_from_relative_motion_between_subject_and_view
object_type: pattern
name: Render Motion Blur From Relative Motion Between Subject and View
library_path:
- art
- rendering
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- motion
- motion_blur
- camera
- depth
cross_links:
- rel: related_to
  target_object_id: PAT_control_edge_hardness_from_form_light_and_focus
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_schmid_render_continuous_natural_motion_as_recurring_soft_edged_patterns
  variant_name: Render Continuous Natural Motion as Recurring Soft-Edged Patterns
  variant_basis: context
  difference_from_foundation: For continuous phenomena such as falling water, waves, or moving foliage, preserves characteristic
    recurring shapes through the motion while softening edges enough to avoid a frozen high-speed look, rather than replacing
    motion with uniform fuzz.
  when_to_use: Use when the subject is a continuously changing natural event whose identity depends on recurring flow patterns
    more than on one frozen instant.
  when_not_to_use: Do not use when a sharp frozen phase is intentionally required or when relative camera/subject motion already
    determines a different blur model.
  absorbed_from_object_id: none
references: []
---
# Render Motion Blur From Relative Motion Between Subject and View

## Pattern Rule
**IF** motion during the viewing or exposure interval must be represented as blur
**THEN** determine screen-space relative motion between subject and view, spread information primarily along that path, and vary blur amount with projected speed and depth rather than applying uniform softness
**ELSE** keep contours crisp when motion is frozen or the intended exposure is short.

## Do
- For a moving subject against a stationary view, blur primarily along the subject's projected motion path.
- Let edges perpendicular to travel smear more visibly than edges aligned with the motion direction.
- When the view tracks the subject, preserve more subject clarity and transfer more relative blur to the background.
- In forward motion, let background blur expand radially from the travel/vanishing direction and become stronger for nearer fast-moving image regions.
- Keep focus blur and atmospheric softness diagnostically separate from motion blur.

## Don't
- Blur every edge equally in all directions.
- Use shallow-focus softness as a substitute for directional motion evidence.
- Ignore tracking or camera movement when deciding what should remain sharp.

## Checklist
- Blur direction matches relative screen-space motion.
- Blur amount varies plausibly with projected speed and depth.
- The sharpest regions agree with the chosen motion/view relationship.

## Notes
Motion blur is a relative-motion effect. Identifying what moves with respect to the view makes it possible to place direction, amount, and depth variation instead of using generic smearing.

`VAR_schmid_render_continuous_natural_motion_as_recurring_soft_edged_patterns` handles continuously changing natural events by preserving recurring characteristic shapes while softening their edges enough to avoid a frozen instant; the result should still contain recognizable flow structure rather than generic fuzz.

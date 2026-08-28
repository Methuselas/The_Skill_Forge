---
object_id: PAT_intercept_moving_object_by_converging_body_and_contact_path
object_type: pattern
name: Intercept a Moving Object by Converging the Body and Contact Path
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
- action_analysis
- catch
- interception
- trajectory
- contact
- gaze
- balance
cross_links:
- rel: related_to
  target_object_id: PAT_design_pose_against_center_of_gravity
- rel: related_to
  target_object_id: PAT_configure_hand_around_function_contact_and_load
reference:
  source_title: Action Analysis for Animators
  author: Chris Webster
confidence: high
references: []
variants: []
---

# Intercept a Moving Object by Converging the Body and Contact Path

## Pattern Rule
**IF** a character must catch or intercept a moving object
**THEN** read the incoming trajectory and move the receiving contact and, when necessary, the whole body toward a shared interception point
**ELSE** use ordinary static contact or manipulation mechanics when the target is not moving through space

## Do
- Establish the object's direction and apparent speed before deciding where the hands or body should go.
- Keep the head and gaze oriented toward the incoming object strongly enough to support the character's spatial judgment.
- Shape and place the receiving hands for the object's size, security requirement, and contact direction rather than using one generic catch pose.
- Move the torso, feet, or whole body when the interception point lies outside the current reach; a catch can require convergence from both the object and the character.
- Allow temporary loss of ordinary static balance when the task demands it. A difficult catch may require a lunge, leap, dive, or airborne interception before support is recovered.
- Let the receiving action continue after contact so the caught object's momentum is visibly absorbed or redirected instead of stopping instantaneously at the hands.

## Don't
- Do not place the hands at the object's current position when the object will arrive somewhere else by the time contact occurs.
- Do not keep the body planted when the required interception point is outside believable reach.
- Do not force static balance during a difficult catch when successful interception mechanically requires temporary instability or suspension.
- Do not let the eyes and head ignore a fast incoming object while the hands somehow find it with unexplained precision.

## Checklist
- The incoming trajectory and the chosen interception point agree.
- The hands and body arrive where the object will be, not where it was.
- Gaze, reach, support, and whole-body travel support the same interception strategy.
- Any temporary instability has a readable cause and a recoverable next state.
- Contact visibly absorbs or redirects the object's motion rather than erasing its momentum.

## Notes
Catching is a convergence problem. The receiver must solve where contact can occur in time and space, then organize gaze, hands, reach, locomotion, and balance around that event. Easy catches may need little more than hand placement; difficult catches can reorganize the entire figure and temporarily outrank ordinary static equilibrium.

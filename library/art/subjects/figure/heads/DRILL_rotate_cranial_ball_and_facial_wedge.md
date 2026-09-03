---
object_id: DRILL_rotate_cranial_ball_and_facial_wedge
object_type: drill
name: Rotate Cranial Ball and Facial Wedge Head Blocks
library_path:
- art
- subjects
- figure
- heads
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: PAT_construct_head_from_cranial_ball_and_facial_wedge
tags:
- figure_drawing
- head_construction
- deliberate_practice
- viewpoint
cross_links:
- rel: teaches
  target_object_id: PAT_construct_head_from_cranial_ball_and_facial_wedge
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
target_skill: rotating the same head construction through multiple views while preserving the ball-to-wedge attachment
references: []
variants:
- variant_id: VAR_hogarth_build_measured_rotation_strip_from_front_template
  variant_name: Build a Measured Rotation Strip From a Front Template
  variant_basis: method_sequence
  difference_from_foundation: Turns the free eight-view rotation drill into Hogarth's progressive measured strip. Establish
    one front ovoid and axes, then build a small turn, three-quarter turn, near-profile, and profile by curving the facial
    centerline, recovering rear-cranial reveal from the center shift, and tracking the side-plane brow point as the turn increases.
    Repeat to the opposite side and compare whether the same head volume survives both directions.
  when_to_use: Use when free rotation practice produces inconsistent skull width or a side plane that jumps unpredictably
    between views, and a more explicit construction scaffold would make the error visible.
  when_not_to_use: Do not score the exercise by whether Hogarth's equal-shift measures remain numerically exact. The goal
    is stable volume through rotation; once that is learned, camera perspective and observed head shape should override the
    template.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_project_character_head_from_front_profile_pair
  variant_name: Project a Character Head From Front and Profile Before Free Rotation
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a character-consistency scaffold before free rotation: solve one simple head in front
    view, project its corresponding levels and masses into a profile, then use that resolved front/profile pair as the identity
    check while estimating further turns and tilts by eye.'
  when_to_use: Use when an invented character changes skull depth, facial projection, or feature spacing as soon as the head
    leaves the first view and a two-view anchor would stabilize identity.
  when_not_to_use: Do not treat the projected pair as rigid orthographic drafting or force exact transfer when camera perspective,
    expression, or the designed head shape genuinely changes the visible relationships.
  absorbed_from_object_id: none
---

# Rotate Cranial Ball and Facial Wedge Head Blocks

## Practice Task
Draw eight featureless head blocks: front, profile, two three-quarter turns, two downviews, and two upviews.

## Target Skill
Rotating the same head construction through multiple views while preserving the ball-to-wedge attachment.

## Setup
Use one page divided into eight equal boxes. Keep the intended head size consistent across the set.

## Instructions
1. Place the cranial ball, facial wedge, centerline, and brow cross-contour in every box.
2. Keep the underlying head proportions stable while changing only the view and tilt.
3. Compare each pair of opposite views and correct any wedge that appears detached or unchanged from the front view.
4. Add only a simple jaw plane or ear marker when it is needed to prove orientation.

## Success Check
- All eight blocks preserve one head's basic proportions; difficult views are solved by projection rather than by enlarging, shrinking, or reshaping the head.
- Centerline and brow cross-contour make each turn and tilt legible before features are added, so orientation is not being rescued by eyes, nose, or expression.
- Downviews favor cranial-vault exposure and upviews reveal more facial underplane in ways consistent with the same construction.
- The facial wedge stays attached to the cranial mass and changes projection with the view rather than remaining a front-facing face pasted inside differently tilted circles.
- Any jaw plane or ear marker functions only as orientation evidence and does not compensate for an unresolved relationship between the two main masses.

## Common Failures
- Adding features before the two masses agree.
- Changing head proportions instead of solving the projection.
- Drawing the same front-facing face inside differently tilted circles.

## Notes
The source teaches viewpoint by repeatedly presenting the same two dominant masses from above, below, front, three-quarter, and rear. Repetition isolates the projection problem from likeness and expression.

`VAR_hogarth_build_measured_rotation_strip_from_front_template` retains **Build a Measured Rotation Strip From a Front Template** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_loomis_project_character_head_from_front_profile_pair` adds a front/profile identity scaffold before free rotation. Use the pair to keep the designed head consistent across new views, but return to viewpoint-specific construction rather than treating the projection as an inflexible template.

---
object_id: DRILL_diagnose_and_correct_perspective_distortion
object_type: drill
name: Diagnose and Correct Perspective Distortion
target_skill: PAT_control_perspective_distortion_with_viewpoint_and_projection_choice
library_path:
- art
- drawing
- perspective
stage_binding: 2 block
lane_fit: teach
foundation_role: specialization
routing_class: teaching
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- distortion
- correction
- drill
cross_links:
- rel: teaches
  target_object_id: PAT_control_perspective_distortion_with_viewpoint_and_projection_choice
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants: []
---

# Diagnose and Correct Perspective Distortion

## Practice Task
Take one box-heavy scene or rough that feels warped near the edges. Rebuild only its perspective scaffold twice: once with wider vanishing-point spacing and once by cropping to the central undistorted region.

## Target Skill
Recognize field-level perspective distortion and correct the field instead of patching individual objects.

## Setup
Keep the original beside the two corrections. Do not render.

## Instructions
1. Mark the current eye level and dominant vanishing points.
2. Identify where distortion is worst.
3. Version A: increase the separation of the relevant vanishing points and reconstruct the same major boxes.
4. Version B: keep the original field but retain only the central region that reads naturally.
5. Compare all three for believable convergence versus excessive flatness.

## Success Check
At least one correction makes edge forms more plausible without breaking the shared vanishing structure.

## Common Failures
- Moving only the bad object's edges while leaving the field unchanged.
- Spreading vanishing points so far that depth almost disappears.
- Judging only one object instead of the behavior of repeated forms across the frame.

## Notes
This is a correction Drill, so it should load only when a distortion failure signal is present.

**Expected Residue**
When perspective feels globally warped, test vanishing spacing and usable field before redrawing local anatomy or props.

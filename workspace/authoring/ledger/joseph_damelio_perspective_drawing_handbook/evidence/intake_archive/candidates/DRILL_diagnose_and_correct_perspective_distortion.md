---
schema_version: vNext-draft.1
object_id: DRILL_diagnose_and_correct_perspective_distortion
object_type: drill
name: Diagnose and Correct Perspective Distortion
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- distortion
- correction
- drill
scope:
  role: specialization
  axis: method
  foundation_object_id: null
bindings:
  development_stages: []
  execution_profiles:
  - direct_dream
  - staged
  - teaching
capabilities:
  provides:
  - activation.art.drawing.perspective.distortion_correction
  requires:
  - art.drawing.perspective.control_distortion_with_vanishing_spacing
  optional: []
  excludes: []
context:
  residency: transient
  priority: 62
  load_when:
  - the task needs diagnose and correct perspective distortion
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p58_60_drill
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 58-60
    evidence_type: mixed
    note: Distortion examples compare excessive and insufficient convergence and show corrections by changing viewing distance/vanishing spacing or cropping.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: PAT_control_perspective_distortion_with_vanishing_spacing
  activation_mode: correction
  residue:
    expected:
    - Apply diagnose and correct perspective distortion during the current operation without keeping the drill instructions resident.
    scope: operation
  default_repetitions: 1
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

## Expected Residue
When perspective feels globally warped, test vanishing spacing and usable field before redrawing local anatomy or props.

## Notes
This is a correction Drill, so it should load only when a distortion failure signal is present.

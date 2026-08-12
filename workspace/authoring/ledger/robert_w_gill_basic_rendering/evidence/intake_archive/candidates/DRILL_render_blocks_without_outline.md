---
schema_version: vNext-draft.1
object_id: DRILL_render_blocks_without_outline
object_type: drill
name: Render Blocks Without Outline
library_path:
- art
- drawing
- rendering
status: candidate
confidence: high
tags:
- value
- plane_change
- rendering
- warmup
scope:
  role: specialization
  axis: method
  foundation_object_id: PAT_render_material_from_optical_response
bindings:
  development_stages: []
  execution_profiles:
  - staged
  - teaching
capabilities:
  provides:
  - activation.art.drawing.rendering.plane_value_warmup
  requires: []
  optional:
  - art.drawing.rendering.prepare_construction_for_rendering
  excludes: []
context:
  residency: transient
  priority: 50
  load_when:
  - value rendering is failing to separate planes without heavy contour or surface scribble
  unload_when:
  - plane changes read cleanly from value relationships alone
relations:
- rel: supports
  target_object_id: AP_prepare_construction_for_rendering
grounding:
  mode: source_led
  evidence:
  - evidence_id: gill_pp155_162_skill_building
    kind: source
    source_id: robert_w_gill_basic_rendering
    locator: printed pp. 155-162 (physical PDF pp. 158-165)
    evidence_type: mixed
    note: Gill starts with cubes and cut blocks, removes visible contour at plane changes, recommends rendering linear marks in the direction of the plane, and increases complexity only after the simple forms are controlled.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: plane_separation_by_value
  activation_mode: warmup
  default_repetitions: 4
  residue:
    expected:
    - Carry plane separation by value, coherent plane-directed mark orientation, and restrained outline into the current rendering operation.
    scope: operation
---

# Render Blocks Without Outline

## Practice Task
Render four simple cubes or cut blocks so each plane change reads from value alone, then remove or suppress the construction outline at the internal plane boundaries.

## Target Skill
Make a solid read as changing planes through controlled value relationships instead of depending on dark contour around every face.

## Setup
Use one solved perspective cube, one cut block, and a single clear light direction. Pencil, ink hatching, or another monochrome medium is sufficient.

## Instructions
1. Copy or construct the block cleanly and choose the light direction before adding tone.
2. Separate the major planes into simple light/shade value groups; keep the first pass broad and even.
3. At an internal plane change, let the value contrast carry the edge instead of tracing the seam darker.
4. In a linear medium, run the stroke direction with the plane when that helps reinforce its orientation; do not let the hatch direction contradict the form.
5. Add a cast shadow and soften its contrast slightly as it recedes across the ground plane.
6. Repeat with a cut block so some plane changes must be understood through both positive form and removed space.

## Success Check
The block reads as solid with the internal construction edges hidden or minimized, the value changes agree with the chosen light, and the cast shadow sits on the same ground plane rather than looking pasted on.

## Common Failures
- Darkening every plane boundary into an outline.
- Using texture density instead of a coherent value relationship.
- Changing hatch direction randomly so the marks fight the plane orientation.
- Letting the cast shadow become a flat black sticker unrelated to depth.

## Notes
Gill originally specifies a range of pencil grades and simple cube repetitions. The retained skill is medium-independent: learn to separate planes with value, then increase complexity only after the simple block reads.

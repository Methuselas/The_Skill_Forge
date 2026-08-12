---
schema_version: vNext-draft.1
object_id: DRILL_aim_clean_perspective_construction_lines
object_type: drill
name: Aim Clean Perspective Construction Lines
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- line_control
- warmup
- construction
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
  - activation.art.drawing.perspective.construction_line_aiming_warmup
  requires: []
  optional:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  excludes: []
context:
  residency: transient
  priority: 54
  load_when:
  - perspective construction is being undermined by bowed, fuzzy, repeatedly corrected, or poorly aimed guide lines
  unload_when:
  - line aiming is stable enough for the current construction task
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: robertson_pp14_15_lines
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 14-15 (physical PDF pp. 12-13)
    evidence_type: mixed
    note: Robertson drills one clean straight stroke, whole-arm motion for long lines, ghosting, point-to-point aiming, common-point aiming, parallel spacing, draw-through boxes, and deliberate line-weight changes rather than fuzzy redraws.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: perspective_construction_line_control
  activation_mode: warmup
  residue:
    expected:
    - Apply one-stroke aiming and clean draw-through construction during the current perspective operation without keeping the drill instructions resident.
    scope: operation
  default_repetitions: 8
---

# Aim Clean Perspective Construction Lines

## Practice Task
Fill one page with eight short sets: parallel lines, point-to-point lines, lines through one common point, and simple perspective boxes drawn through their hidden edges.

## Target Skill
Place a deliberate construction line where you intend it to go without repairing the stroke by repeatedly tracing over it.

## Setup
Use a pen or pencil on plain paper. Rotate the paper so the practiced straight stroke can be reused in different directions.

## Instructions
1. Make several slow straight strokes using the arm rather than only the fingers or wrist for longer lines.
2. Before each aimed stroke, rehearse the motion lightly above the page, then commit once.
3. Connect pairs of dots without stopping at the destination; aim through the endpoint so the stroke stays confident.
4. Draw several lines through one common point from different directions.
5. Build a few boxes in perspective, drawing through hidden edges instead of stopping at visible corners.
6. On the last box, vary line weight intentionally after the structure is correct rather than redrawing weak lines into fuzz.

## Success Check
Most strokes arrive at their target with one readable line, parallel sets keep coherent spacing, and the box construction stays legible without hairy correction marks.

## Common Failures
- Repeatedly tracing the same line until it becomes a fuzzy band.
- Drawing long lines only from the wrist and producing an arc.
- Decelerating into the endpoint so the stroke hooks or wobbles.
- Using line weight before the construction is solved.

## Notes
Robertson treats this as craftsmanship that should become muscle memory so design can take more attention later. Use it as a short activation drill, not a permanent drawing ritual.

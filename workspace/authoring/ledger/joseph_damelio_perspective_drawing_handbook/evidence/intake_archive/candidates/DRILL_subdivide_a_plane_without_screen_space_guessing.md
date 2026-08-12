---
schema_version: vNext-draft.1
object_id: DRILL_subdivide_a_plane_without_screen_space_guessing
object_type: drill
name: Subdivide a Plane Without Screen-Space Guessing
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- measurement
- diagonal
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
  - activation.art.drawing.perspective.plane_metrology_warmup
  requires:
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  optional: []
  excludes: []
context:
  residency: transient
  priority: 62
  load_when:
  - the task needs subdivide a plane without screen-space guessing
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p68_76_drill
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 68-76
    evidence_type: mixed
    note: The chapter constructs centers, repeated intervals, arbitrary measurements, and grids on receding planes without relying on equal image-space gaps.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: PAT_measure_subdivide_and_repeat_on_perspective_planes
  activation_mode: warmup
  residue:
    expected:
    - Apply subdivide a plane without screen-space guessing during the current operation without keeping the drill instructions resident.
    scope: operation
  default_repetitions: 2
---

# Subdivide a Plane Without Screen-Space Guessing

## Practice Task
Draw one floor rectangle in perspective. Divide it into four equal real-world depth sections, then place a simple repeated post at each division.

## Target Skill
Use diagonals and perspective construction to create equal spacing in depth.

## Setup
Establish eye level and the rectangle's vanishing directions first.

## Instructions
1. Draw the receding rectangle.
2. Use its diagonals to locate the true center.
3. Subdivide again to obtain four sections.
4. Erect equal-height posts at the divisions using height guides.
5. Compare the visible gaps; they should compress with depth rather than remain equal on the page.

## Success Check
The posts read as evenly spaced in the world even though their screen-space gaps diminish.

## Common Failures
- Dividing the visible receding edge into four equal image lengths.
- Using the rectangle's visual midpoint instead of the diagonal center.
- Giving repeated posts unrelated heights.

## Expected Residue
Treat equal world spacing as a construction problem on the plane, not an equal-pixel-spacing problem.

## Notes
Use the measuring-line variant later when the desired intervals are not simple subdivisions.

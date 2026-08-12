---
schema_version: vNext-draft.1
object_id: DRILL_calibrate_scene_from_one_figure
object_type: drill
name: Calibrate a Scene From One Figure
library_path: [art, drawing, perspective]
status: candidate
confidence: high
tags: [perspective, figure_drawing, environment, drill]
scope:
  role: warmup
  axis: method
bindings:
  development_stages: [stage_hold_pending_walkthrough]
  execution_profiles: [direct_dream, staged, teaching]
capabilities:
  provides: [art.drawing.perspective.figure_calibrated_scene_drill]
  requires: [art.drawing.perspective.calibrate_scene_from_figure]
  optional: []
  excludes: []
context:
  residency: transient
  priority: 66
  load_when:
    - a composition requires figures and environment to share a difficult depth field
  unload_when:
    - drill evaluation completes
relations:
  - rel: teaches
    target_object_id: PAT_build_shared_scene_perspective_from_figure
grounding:
  mode: mixed
  evidence:
    - evidence_id: ch6_scene_drill_source
      kind: source
      source_id: burne_hogarth_dynamic_figure_drawing
      locator: ch06, printed pp. 159-164
      evidence_type: mixed
      note: Hogarth derives object and additional-figure relationships from a figure-calibrated perspective field.
    - evidence_id: ch6_scene_drill_teacher
      kind: human_teaching
      source_id: project_teacher_session
      locator: 2026-08-07, Chapter 6 review
      evidence_type: text
      note: Teacher emphasized that once the grid is sound, arbitrary objects and differently oriented figures can be added with relatively correct depth and proportion.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: PAT_build_shared_scene_perspective_from_figure
  activation_mode: warmup
  residue:
    expected:
      - Treat one solved perspective field as authority for every figure and object in the scene.
    scope: operation
  default_repetitions: 1
---

# Calibrate a Scene From One Figure

Draw one simple figure in depth. Use its landmarks/planes to establish a perspective scaffold. Add:
1. one object sized relative to the figure;
2. a second figure at another depth;
3. a third figure with a different body orientation.

Do not redraw the grid for each object.

**Success:** all additions feel like they occupy the same world even though their local orientations differ.

---
schema_version: vNext-draft.1
object_id: PAT_build_shared_scene_perspective_from_figure
object_type: pattern
name: Build a Shared Scene Perspective Field From the Figure
library_path: [art, drawing, perspective]
status: candidate
confidence: high
tags: [perspective, figure_drawing, environment, proportion]
scope:
  role: foundation_candidate
  axis: method
bindings:
  development_stages: [stage_hold_pending_walkthrough]
  execution_profiles: [direct_dream, staged, teaching]
capabilities:
  provides:
    - art.drawing.perspective.calibrate_scene_from_figure
    - art.drawing.perspective.maintain_shared_scene_field
  requires:
    - art.drawing.figure_projection.transport_proportional_landmarks_across_views
  optional:
    - art.drawing.figure_projection.use_reversible_projection
  excludes: []
context:
  residency: phase
  priority: 72
  load_when:
    - a figure must establish or share scale, depth, and perspective with objects, environments, or additional figures
  unload_when:
    - the scene perspective field is locked or the spatial-construction phase ends
relations:
  - rel: supported_by
    target_object_id: PAT_transport_proportional_landmarks_across_views
grounding:
  mode: mixed
  evidence:
    - evidence_id: ch6_environmental_gravitation
      kind: source
      source_id: burne_hogarth_dynamic_figure_drawing
      locator: ch06, printed pp. 159-164
      evidence_type: mixed
      note: Hogarth derives perspective planes/grids from figure relationships and uses them to scale objects and additional figures.
    - evidence_id: ch6_scene_teacher
      kind: human_teaching
      source_id: project_teacher_session
      locator: 2026-08-07, Chapter 6 review
      evidence_type: text
      note: Teacher identified body lines/planes as metrological calibration for both scale and viewpoint; once established, the grid becomes scene authority and can generate objects or figures in either direction.
  derivations:
    - derivation_id: ch6_scene_field_synthesis
      kind: synthesis
      inputs: [ch6_environmental_gravitation, ch6_scene_teacher]
      note: Generalize Hogarth's examples into a shared-field rule without pretending Chapter 6 is a complete architectural perspective course.
  claim_map: {}
assets: []
variants: []
spec:
  form: production_method
---

# Build a Shared Scene Perspective Field From the Figure

## Pattern Rule
Use a correctly constructed figure's known landmarks, lines, and planes to calibrate relative scale and perspective direction. Extend those relationships into a scene grid, then make that grid the spatial authority for additional figures and objects.

## Production sequence
1. Establish a trustworthy figure and viewpoint.
2. Select useful body landmarks/planes that express scale and direction.
3. Extend them into a coherent perspective scaffold.
4. Derive object/environment scale from that scaffold.
5. Place additional figures by matching corresponding landmarks to the same field.
6. Allow objects and figures to rotate independently, but require all of them to obey the shared scene field.

## Invariant
**Calibrate once. Construct freely inside the solved field.**

## Boundary
This Pattern is figure-derived perspective calibration. It does not replace dedicated study of horizon lines, vanishing systems, camera/world axes, architectural perspective, or single-view metrology.

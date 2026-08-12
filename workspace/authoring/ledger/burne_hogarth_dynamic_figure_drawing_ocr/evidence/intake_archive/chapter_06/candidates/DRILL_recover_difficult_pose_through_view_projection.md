---
schema_version: vNext-draft.1
object_id: DRILL_recover_difficult_pose_through_view_projection
object_type: drill
name: Recover a Difficult Pose Through View Projection
library_path: [art, drawing, figure_projection]
status: candidate
confidence: high
tags: [figure_drawing, projection, foreshortening, correction]
scope:
  role: correction
  axis: method
bindings:
  development_stages: [stage_hold_pending_walkthrough]
  execution_profiles: [direct_dream, staged, teaching]
capabilities:
  provides: [art.drawing.figure_projection.difficult_view_recovery]
  requires: [art.drawing.figure_projection.transport_proportional_landmarks_across_views]
  optional: [art.drawing.figure_projection.use_reversible_projection]
  excludes: []
context:
  residency: transient
  priority: 68
  load_when:
    - a figure pose is understood conceptually but repeatedly fails in a difficult foreshortened or rotated view
  unload_when:
    - the target-view landmark scaffold is recovered and evaluated
relations:
  - rel: teaches
    target_object_id: PAT_transport_proportional_landmarks_across_views
grounding:
  mode: mixed
  evidence:
    - evidence_id: ch6_projection_drill_source
      kind: source
      source_id: burne_hogarth_dynamic_figure_drawing
      locator: ch06, printed pp. 151-158
      evidence_type: mixed
      note: Hogarth repeatedly solves difficult views by carrying corresponding positions from clearer views.
    - evidence_id: ch6_projection_drill_teacher
      kind: human_teaching
      source_id: project_teacher_session
      locator: 2026-08-07, Chapter 6 review
      evidence_type: text
      note: Teacher framed side/front/back drawings as templates that can be used when direct foreshortened invention fails.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: PAT_transport_proportional_landmarks_across_views
  activation_mode: correction
  residue:
    expected:
      - When a difficult view becomes unstable, solve a clear corresponding view, transport landmarks, then rebuild rather than forcing the failed drawing.
    scope: operation
  default_repetitions: 1
---

# Recover a Difficult Pose Through View Projection

1. Preserve the intended action and camera.
2. Draw the same action in the clearest useful side/front/back view.
3. Mark pelvis, rib cage, shoulders, major joints, hands/feet, and head landmarks.
4. Project the corresponding tracks into the target view.
5. Rebuild simple masses at those destinations.
6. Apply local reach/width checks only where needed.
7. Remove the scaffold and verify that the target pose still reads.

**Success:** the recovered pose preserves the intended action and proportion without inheriting the source view's contour.

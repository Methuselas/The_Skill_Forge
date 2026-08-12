---
schema_version: vNext-draft.1
object_id: PAT_use_reversible_projection_to_recover_hidden_structure
object_type: pattern
name: Use Reversible Projection to Recover Hidden Structure
library_path: [art, drawing, figure_projection]
status: candidate
confidence: high
tags: [figure_drawing, projection, rotation, hidden_form]
scope:
  role: specialization
  axis: method
  foundation_object_id: PAT_transport_proportional_landmarks_across_views
bindings:
  development_stages: [stage_hold_pending_walkthrough]
  execution_profiles: [direct_dream, staged, teaching]
capabilities:
  provides: [art.drawing.figure_projection.use_reversible_projection]
  requires: [art.drawing.figure_projection.transport_proportional_landmarks_across_views]
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 62
  load_when:
    - hidden, opposite, front, back, side, over, or under relationships are difficult to infer directly
  unload_when:
    - the target structure is recovered and passes correspondence checks
relations:
  - rel: specialization_of
    target_object_id: PAT_transport_proportional_landmarks_across_views
grounding:
  mode: mixed
  evidence:
    - evidence_id: ch6_reversible_source
      kind: source
      source_id: burne_hogarth_dynamic_figure_drawing
      locator: ch06, printed pp. 156-158
      evidence_type: mixed
      note: Hogarth demonstrates reversible projection and opposite-view recovery.
    - evidence_id: ch6_reversible_teacher
      kind: human_teaching
      source_id: project_teacher_session
      locator: 2026-08-07, Chapter 6 review
      evidence_type: text
      note: Teacher clarified that the correspondence can run between side/front/back and other views; relative spatial relationships remain usable as viewpoint changes.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Use Reversible Projection to Recover Hidden Structure

When the desired view hides or compresses a relationship, construct a clearer corresponding view and run the same landmark correspondence backward or sideways into the difficult view.

## Checks
- Corresponding landmarks remain in the same relative order.
- The recovered view is rebuilt as volume, not copied as flattened contour.
- A change of viewpoint does not silently change body proportion.
- Side, front, and back views may solve one another; no single view is privileged.

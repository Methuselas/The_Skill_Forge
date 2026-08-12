---
schema_version: vNext-draft.1
object_id: PAT_transport_proportional_landmarks_across_views
object_type: pattern
name: Transport Proportional Landmarks Across Views
library_path: [art, drawing, figure_projection]
status: candidate
confidence: high
tags: [figure_drawing, projection, proportion, foreshortening]
scope:
  role: foundation_candidate
  axis: method
bindings:
  development_stages: [stage_hold_pending_walkthrough]
  execution_profiles: [direct_dream, staged, teaching]
capabilities:
  provides: [art.drawing.figure_projection.transport_proportional_landmarks_across_views]
  requires: [art.drawing.figure_construction.preserve_articulated_limb_chain]
  optional: [art.drawing.figure_construction.validate_foreshortened_limb_reach_from_joint_pivots]
  excludes: []
context:
  residency: triggered
  priority: 65
  load_when:
    - a difficult foreshortened or rotated figure view is uncertain but a clearer corresponding view can be constructed
  unload_when:
    - target-view landmarks are registered and construction can proceed from ordinary form knowledge
relations:
  - rel: supports
    target_object_id: PAT_build_shared_scene_perspective_from_figure
grounding:
  mode: mixed
  evidence:
    - evidence_id: ch6_parallel_projection
      kind: source
      source_id: burne_hogarth_dynamic_figure_drawing
      locator: ch06, printed pp. 151-155
      evidence_type: mixed
      note: Hogarth preserves proportional divisions through parallel projection and applies corresponding tracks to heads and figures.
    - evidence_id: ch6_teacher_relative_space
      kind: human_teaching
      source_id: project_teacher_session
      locator: 2026-08-07, Chapter 6 review
      evidence_type: text
      note: Teacher clarified that a readable side/front/back view acts as a correspondence template; projection transports landmarks, while form knowledge rebuilds the target view.
  derivations:
    - derivation_id: ch6_landmark_transport
      kind: synthesis
      inputs: [ch6_parallel_projection, ch6_teacher_relative_space]
      note: Compress the diagrams into a reusable solve-easy-view then transport-landmarks production method.
  claim_map: {}
assets: []
variants: []
spec:
  form: production_method
---

# Transport Proportional Landmarks Across Views

## Pattern Rule
**IF** a difficult figure orientation cannot be placed confidently in depth
**THEN** solve the action in a clearer view, establish corresponding proportional landmarks, project those landmarks into the target orientation, and rebuild the target figure with existing form knowledge
**ELSE** construct directly when the target view is already clear.

## Do
- Treat the clear source view as a correspondence template, not as a finished contour to distort.
- Preserve relative divisions between meaningful landmarks while apparent screen-space distances change.
- Register major masses and joints first: pelvis, rib cage, shoulders, knees, elbows, hands/feet, head landmarks as appropriate.
- Reconstruct volume at the destination with known shape-mass and anatomy rules.
- Use Chapter 5 reach checks locally when a projected limb remains uncertain.

## Don't
- Assume projection alone constructs the anatomy.
- Copy contour lengths literally from source view to target view.
- Re-measure every part independently after correspondence has already established its relative position.
- Let a locally attractive limb break the transported landmark relationships.

## Compact residue
**Solve the relationship where it is easiest to see; transport it to the view where it is hardest to see.**

---
schema_version: vNext-draft.1
object_id: DRILL_scrub_action_to_find_stronger_keyframe
object_type: drill
name: Scrub an Action to Find a Stronger Keyframe
library_path: [art, drawing, action]
status: candidate
confidence: high
tags: [figure_drawing, action, composition, correction]
scope:
  role: correction
  axis: method
bindings:
  development_stages: [stage_hold_pending_walkthrough]
  execution_profiles: [direct_dream, staged, teaching]
capabilities:
  provides: [art.drawing.action.keyframe_search_correction]
  requires: [art.drawing.action.search_keyframes_from_pelvis_anchor]
  optional: [art.drawing.action.separate_construction_order_from_kinetic_lead]
  excludes: []
context:
  residency: transient
  priority: 64
  load_when:
    - a pose is anatomically plausible but does not communicate enough or the right kind of action
  unload_when:
    - a keyframe is selected and transferred back to the parent composition
relations:
  - rel: teaches
    target_object_id: PAT_search_action_keyframes_from_pelvis_anchor
grounding:
  mode: mixed
  evidence:
    - evidence_id: ch6_keyframe_drill_source
      kind: source
      source_id: burne_hogarth_dynamic_figure_drawing
      locator: ch06, printed pp. 165-173
      evidence_type: mixed
      note: Hogarth explores multiple action phases and stronger directional body actions.
    - evidence_id: ch6_keyframe_drill_teacher
      kind: human_teaching
      source_id: project_teacher_session
      locator: 2026-08-07, Chapter 6 review
      evidence_type: text
      note: Teacher compared action drawings to animation keyframes and emphasized selecting the amount of action required by the composition, including exaggeration for comics.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  target_skill: PAT_search_action_keyframes_from_pelvis_anchor
  activation_mode: correction
  residue:
    expected:
      - If an action reads weakly, branch to nearby action phases and select the keyframe with the appropriate force instead of polishing the weak pose.
    scope: operation
  default_repetitions: 1
---

# Scrub an Action to Find a Stronger Keyframe

1. Preserve the composition's intent and pelvis anchor.
2. Draw several quick alternate action phases around the failed pose.
3. Let limbs and torso relationships change enough to discover better action; do not freeze the failed drawing.
4. Compare silhouette, balance, direction, wind-up/follow-through, and required exaggeration.
5. Select the keyframe with the right action strength.
6. Transfer that solution back into the parent composition.

The exploratory figures are disposable. Only the selected action relationship becomes authoritative.

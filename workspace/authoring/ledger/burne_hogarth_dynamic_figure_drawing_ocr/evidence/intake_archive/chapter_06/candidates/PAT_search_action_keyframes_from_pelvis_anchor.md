---
schema_version: vNext-draft.1
object_id: PAT_search_action_keyframes_from_pelvis_anchor
object_type: pattern
name: Search Action Keyframes From the Pelvis Anchor
library_path: [art, drawing, action]
status: candidate
confidence: high
tags: [figure_drawing, action, composition, pelvis]
scope:
  role: specialization
  axis: method
bindings:
  development_stages: [stage_hold_pending_walkthrough]
  execution_profiles: [direct_dream, staged, teaching]
capabilities:
  provides: [art.drawing.action.search_keyframes_from_pelvis_anchor]
  requires: [art.drawing.figure_construction.preserve_articulated_limb_chain]
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 58
  load_when:
    - an action pose is structurally valid but visually weak, awkward, or compositionally unsatisfying
  unload_when:
    - a stronger action phase is selected
relations: []
grounding:
  mode: mixed
  evidence:
    - evidence_id: ch6_phase_source
      kind: source
      source_id: burne_hogarth_dynamic_figure_drawing
      locator: ch06, printed pp. 165-167
      evidence_type: mixed
      note: Hogarth explores related action positions through phase-sequence projection and corresponding forms.
    - evidence_id: ch6_phase_teacher
      kind: human_teaching
      source_id: project_teacher_session
      locator: 2026-08-07, Chapter 6 review
      evidence_type: text
      note: Teacher framed each action drawing as a keyframe; the pelvis is the persistent anchor, and a weak pose can be repaired by moving forward/backward through the action until a better key is found.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Search Action Keyframes From the Pelvis Anchor

If an action pose does not sell, do not keep polishing the lost trail. Hold the pelvis as the action anchor, explore earlier/later or alternate action states, and select the keyframe whose body relationships best serve the composition.

The goal is not maximum extremity. The goal is the **right amount of action** for the scene.

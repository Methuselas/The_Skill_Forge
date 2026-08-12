---
schema_version: vNext-draft.1
object_id: PAT_separate_construction_order_from_kinetic_lead
object_type: pattern
name: Separate Construction Order From Kinetic Lead
library_path: [art, drawing, action]
status: candidate
confidence: high
tags: [figure_drawing, action, gesture, direction]
scope:
  role: specialization
  axis: principle
bindings:
  development_stages: [stage_hold_pending_walkthrough]
  execution_profiles: [direct_dream, staged, teaching]
capabilities:
  provides: [art.drawing.action.separate_construction_order_from_kinetic_lead]
  requires: []
  optional: [art.drawing.action.search_keyframes_from_pelvis_anchor]
  excludes: []
context:
  residency: triggered
  priority: 54
  load_when:
    - a pose is constructed correctly but its directional intent or action flow is unclear
  unload_when:
    - kinetic direction is coherent or operation ends
relations: []
grounding:
  mode: mixed
  evidence:
    - evidence_id: ch6_chin_source
      kind: source
      source_id: burne_hogarth_dynamic_figure_drawing
      locator: ch06, printed pp. 168-173
      evidence_type: mixed
      note: Hogarth states that eye direction is an initial clue and chin thrust leads directional body action.
    - evidence_id: ch6_chin_teacher
      kind: human_teaching
      source_id: project_teacher_session
      locator: 2026-08-07, Chapter 6 review
      evidence_type: text
      note: Teacher reconciled kinetic order with the existing torso-first drawing order: eyes/chin initiate directional movement while construction can still begin from torso/support.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: principle
---

# Separate Construction Order From Kinetic Lead

Do not confuse **where the drawing is constructed from** with **where the depicted action appears to originate**.

- Construction may remain torso/support first.
- Kinetic intent is often signaled by eyes and chin/head direction before the rest of the body follows.
- Pelvis remains the gravity/action anchor while head/chin can lead directional flow.

Use this as a coherence check, not as a rule that every motion must be drawn head-first.

---
schema_version: vNext-draft.1
object_id: PAT_build_coherent_grid_when_vanishing_points_are_off_page
object_type: pattern
name: Build a Coherent Grid When Vanishing Points Are Off the Page
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- grid
- offpage_vp
- brewer_method
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
  - art.drawing.perspective.construct_offpage_vp_grid
  requires:
  - art.drawing.perspective.choose_convergence_from_view_and_orientation
  optional:
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  excludes: []
context:
  residency: triggered
  priority: 86
  load_when:
  - a hand-drawn two-point grid needs consistent convergence but one or both vanishing points lie too far outside the sheet to use directly
  unload_when:
  - enough coherent grid lines exist to serve as a reusable underlay
relations:
- rel: supports
  target_object_id: AP_construct_a_shared_scene_perspective_field
grounding:
  mode: source_led
  evidence:
  - evidence_id: robertson_pp54_57_brewer
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 54-57 (physical PDF pp. 52-55)
    evidence_type: mixed
    note: Robertson's Brewer Method starts from four establishing convergence lines, creates a controlled rectangular construction, subdivides a vertical, and transfers those subdivisions through corresponding points to generate additional lines that remain coherent with off-page vanishing directions.
  derivations:
  - derivation_id: brewer_runtime_synthesis
    kind: synthesis
    inputs:
    - robertson_pp54_57_brewer
    note: Preserves the operational sequence while explicitly bounding it as a coherence method built from trusted establishing lines, not automatic recovery of a physically exact camera.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Build a Coherent Grid When Vanishing Points Are Off the Page

## Pattern Rule
**IF** a two-point perspective needs repeated guide lines but its vanishing points are impractically far outside the drawing **THEN** use four trusted establishing lines as the local convergence evidence, construct the Brewer transfer scaffold, subdivide that scaffold, and propagate the intersections into a reusable local grid instead of extending every guide to an unreachable point.

## Do
- Begin with two trustworthy lines from each horizontal direction family; the method inherits their convergence, so these four establishing lines matter more than the later grid density.
- Place a vertical where the two families can be compared clearly and build the rectangular transfer construction Robertson demonstrates between the establishing lines.
- Use the constructed right-angle/rectangle relationship to create the auxiliary diagonal and intersection that stand in for the hidden vanishing destination.
- Subdivide the central vertical evenly, then project corresponding subdivision points through the transfer points to generate additional receding guides.
- Extend the resulting grid only as far as the drawing needs; add square units later with the normal square/ellipse or multiplication methods if true unit spacing is required.
- Save a successful Brewer grid as an underlay for objects that share the same viewpoint.

## Don't
- Assume the Brewer scaffold can repair four bad establishing lines; it propagates their logic.
- Call the result a recovered camera solution when the initial convergences were chosen by eye.
- Draw every possible grid line and bury the design under construction noise.
- Use this method when the vanishing points are already reachable and direct construction is simpler.

## Checklist
- New guide lines continue the convergence implied by the four establishing lines without visible kinks.
- Both direction families remain internally consistent across the usable drawing area.
- The grid can be reused as an underlay without needing the actual off-page vanishing points on the sheet.
- If square dimensions are added, their spacing is constructed separately rather than assumed from the Brewer line fan alone.

## Notes
This is best understood as an **off-page convergence transport tool**. It solves a practical paper-space problem; it does not replace the station-point or visual-ray constructions when the camera itself must be recovered exactly.

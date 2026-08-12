---
schema_version: vNext-draft.1
object_id: PAT_validate_three_point_viewpoint_geometry
object_type: pattern
name: Validate Three-Point Perspective From the Vanishing Triangle
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- three_point
- orthocenter
- vanishing_point
scope:
  role: specialization
  axis: method
  foundation_object_id: PAT_choose_convergence_from_view_and_orientation
bindings:
  development_stages: []
  execution_profiles:
  - direct_dream
  - staged
  - teaching
capabilities:
  provides:
  - art.drawing.perspective.validate_three_point_viewpoint_geometry
  requires:
  - art.drawing.perspective.choose_convergence_from_view_and_orientation
  optional:
  - art.drawing.perspective.recover_view_field_from_existing_image
  excludes: []
context:
  residency: triggered
  priority: 88
  load_when:
  - a rectilinear scene uses three vanishing points for three mutually perpendicular
    world directions, especially in an extreme up/down view or when the exact station
    point matters
  unload_when:
  - the three-point field has a valid viewpoint and usable viewing distance or has
    been rebuilt
relations:
- rel: specialization_of
  target_object_id: PAT_choose_convergence_from_view_and_orientation
- rel: supports
  target_object_id: PAT_control_perspective_distortion_with_viewpoint_and_projection_choice
grounding:
  mode: source_led
  evidence:
  - evidence_id: viewpoints_pp86_90_acute_triangle
    kind: source
    source_id: frantz_crannell_viewpoints_mathematical_perspective
    locator: printed pp. 86-90 (physical PDF pp. 101-105)
    evidence_type: mixed
    note: For three mutually perpendicular direction families, the three vanishing
      points form a valid viewpoint triangle if and only if that triangle is acute;
      the viewing target is its orthocenter.
  - evidence_id: viewpoints_pp91_93_viewing_distance
    kind: source
    source_id: frantz_crannell_viewpoints_mathematical_perspective
    locator: printed pp. 91-93 (physical PDF pp. 106-108)
    evidence_type: mixed
    note: The viewing distance can be recovered geometrically from the vanishing triangle
      using the orthocenter and an altitude semicircle, or by d^2 = |TV_i||TF_i|.
  - evidence_id: viewpoints_pp97_98_practical_triangle
    kind: source
    source_id: frantz_crannell_viewpoints_mathematical_perspective
    locator: printed pp. 97-98 (physical PDF pp. 112-113)
    evidence_type: mixed
    note: A right viewpoint triangle collapses the viewing distance to zero, near-right
      triangles imply very small viewing distances, and a nearly equilateral triangle
      maximizes usable distance relative to triangle size; important content should
      stay near the viewing target.
  derivations:
  - derivation_id: three_point_quick_validation
    kind: synthesis
    inputs:
    - viewpoints_pp86_90_acute_triangle
    - viewpoints_pp91_93_viewing_distance
    - viewpoints_pp97_98_practical_triangle
    note: Converts the source proofs into a triggered validation rule so the math
      can remain internal while the runtime decision is fast.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Validate Three-Point Perspective From the Vanishing Triangle

## Pattern Rule
**IF** three vanishing points represent three mutually perpendicular world directions in a rectilinear three-point setup **THEN** require those vanishing points to form an acute triangle; use the triangle's orthocenter as the viewing target and its altitude geometry to diagnose the viewing distance before trusting the field.

## Do
- Connect the three principal vanishing points and check that all three triangle angles are less than 90 degrees.
- Find the viewing target by intersecting two altitudes of the vanishing-point triangle; that intersection is the orthocenter.
- When exact distance matters, recover it from an altitude semicircle or the equivalent product relation described by the source.
- Treat a triangle approaching a right angle as a warning that the implied station point is collapsing toward the picture plane and ordinary viewers will see severe apparent distortion from normal display distances.
- For a practical invented field without a pre-existing camera, prefer a nearly equilateral vanishing triangle as a stable starting geometry, then place the actual subject near the viewing target.

## Don't
- Pick any three noncollinear points and assume they can represent three orthogonal world axes; an obtuse triangle has no common viewpoint and a right triangle puts the viewpoint on the picture plane.
- Confuse this rule with a requirement that all three vanishing points be visible inside the crop.
- Use this theorem for three arbitrary non-orthogonal direction families without re-deriving their angle relationships.
- Expose the proof or formula during ordinary drawing unless the task actually needs exact reconstruction or teaching.

## Checklist
- The three principal VPs form an acute triangle.
- The orthocenter/viewing target lies inside that triangle.
- The inferred viewing distance is nonzero and practical for the intended display or is deliberately extreme.
- Major content is not needlessly scattered far from the viewing target.
- Any extreme convergence is understood as a camera/display choice rather than an unexplained local warp.

## Notes
This is the main new mathematical validation earned by the Deep PASS. It is intentionally triggered: ordinary perspective drawing does not need an orthocenter construction every time. It becomes valuable for skyscraper shots, steep up/down views, camera reconstruction, and debugging a three-point field that looks "almost right" but has no physically consistent station point.

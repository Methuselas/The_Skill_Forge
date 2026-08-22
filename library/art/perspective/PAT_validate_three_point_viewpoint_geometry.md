---
object_id: PAT_validate_three_point_viewpoint_geometry
object_type: pattern
name: Validate Three-Point Perspective From the Vanishing Triangle
library_path:
- art
- perspective
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_choose_convergence_from_view_and_orientation
tags:
- perspective
- three_point
- orthocenter
- vanishing_point
cross_links:
- rel: related_to
  target_object_id: PAT_choose_convergence_from_view_and_orientation
- rel: supports
  target_object_id: PAT_control_perspective_distortion_with_viewpoint_and_projection_choice
reference:
  source_title: 'Viewpoints: Mathematical Perspective and Fractal Geometry in Art'
  author: Marc Frantz and Annalisa Crannell
confidence: high
references: []
variants: []
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

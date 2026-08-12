---
object_id: PAT_build_coherent_grid_when_vanishing_points_are_off_page
object_type: pattern
name: Build a Coherent Grid When Vanishing Points Are Off the Page
library_path:
- art
- drawing
- perspective
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- grid
- offpage_vp
- brewer_method
cross_links:
- rel: supports
  target_object_id: AP_construct_a_shared_scene_perspective_field
reference:
  source_id: scott_robertson_how_to_draw
  source_title: 'How to Draw: Drawing and Sketching Objects and Environments from Your Imagination'
  author: Scott Robertson with Thomas Bertling
  publish_date: '2013'
  media_type: book
  locator: u00, printed pp. 54-57 (physical PDF pp. 52-55)
  evidence_type: mixed
confidence: high
references: []
variants: []
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

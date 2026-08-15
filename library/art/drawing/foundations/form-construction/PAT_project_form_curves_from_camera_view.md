---
object_id: PAT_project_form_curves_from_camera_view
object_type: pattern
name: Project Form Curves From the Camera View
library_path:
- art
- drawing
- foundations
- form-construction
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- figure_drawing
- viewpoint
- foreshortening
- form_flow
cross_links: []
reference:
  source_id: burne_hogarth_dynamic_figure_drawing_ocr
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
  publish_date: 1970
  media_type: book
  locator: ch03, printed pp. 72-81
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_hampton_make_every_added_line_obey_surface_form
  variant_name: Make Every Added Line Obey the Surface Form
  variant_basis: method_sequence
  source_id: michael_hampton_figure_drawing_design_and_invention
  source_title: 'Figure Drawing: Design and Invention'
  locator: u02, printed pp. 51-54
  difference_from_foundation: 'Adds Hampton''s explicit surface-consistency test to form projection: once a box, sphere, cylinder, or organic volume is established, every later line should travel over or around that surface consistently. A line that cuts across the implied surface logic weakens the illusion even when the underlying primitive was correctly drawn.'
  when_to_use: Use whenever contour, anatomy, construction lines, or secondary forms are being added to an already-established three-dimensional volume.
  when_not_to_use: Do not add wrapping lines mechanically to every surface; the rule governs the direction of marks that are actually needed, not the quantity of cross-contours.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_square_organic_masses_then_round_to_projection
  variant_name: Square Organic Masses, Solve the View, Then Round Them Back
  variant_basis: method_sequence
  source_id: andrew_loomis_successful_drawing
  source_title: Successful Drawing
  locator: u02, physical PDF p. 62
  difference_from_foundation: Temporarily converts ambiguous rounded figure masses into simple block-like plane changes so their relationship to the eye level and camera is easier to solve, then restores the organic anatomy without changing the solved projection.
  when_to_use: Use when an invented or strongly foreshortened figure drifts because rounded anatomy makes it unclear which top, underside, or side surfaces should be visible from the chosen view.
  when_not_to_use: Keep the block pass temporary; do not let the temporary squaring stiffen the final figure, erase gesture, or replace anatomical form design.
  absorbed_from_object_id: none
---

# Project Form Curves From the Camera View

## Pattern Rule
**IF** a familiar torso or limb connection changes appearance in a high, low, turned, or deeply foreshortened view
**THEN** derive its visible overcurves, undercurves, compressions, and dominant masses from the unchanged three-dimensional form as seen from that camera position
**ELSE** use the simpler familiar projection only when the view genuinely supports it

## Do
- Decide which mass is nearer to the eye before choosing the visible curve sequence.
- Let low views expose upward vaults and overcurve progressions where the form warrants them, and let high views reveal compressed undercurves where the same structure turns away.
- Track the natural route around the volume rather than forcing a remembered front-view anatomy map onto the new angle.
- Compare several viewpoints of the same form so the underlying structure remains stable while its projection changes.

## Don't
- Treat overcurve and undercurve as permanent labels attached to a body part.
- Define the direction by the top or bottom of the canvas; the drawing surface records the view but does not cause the form.
- Reverse a curve automatically because the pose has been rotated on the page.

## Checklist
- The selected curve agrees with which surfaces face, turn from, or disappear from the camera.
- A high and low view look like projections of the same underlying body rather than two different constructions.
- Rotating the canvas alone would not change the structural explanation.

## Notes
Hogarth contrasts high- and low-angle torso views to show the same anatomical masses producing different visible curve families. The guided review clarified the governing model: the eye behaves as a camera in three-dimensional space; the body remains the body, while perspective changes what its natural forms reveal.

`VAR_hampton_make_every_added_line_obey_surface_form` retains **Make Every Added Line Obey the Surface Form** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_loomis_square_organic_masses_then_round_to_projection` adds a temporary diagnostic squaring pass for difficult figure views: solve the camera-facing planes first, then round the anatomy back out without losing the perspective decision.

---
object_id: PAT_carry_scale_through_depth_with_height_and_width_guides
object_type: pattern
name: Carry Scale Through Depth With Height and Width Guides
library_path:
- art
- drawing
- perspective
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- perspective
- scale
- height
- width
cross_links: []
reference:
  source_title: Perspective Drawing Handbook
  author: Joseph D'Amelio
confidence: high
references: []
variants:
- variant_id: VAR_loomis_scale_cropped_figures_from_visible_landmarks
  variant_name: Scale Cropped Figures From Visible Corresponding Landmarks
  variant_basis: method_sequence
  difference_from_foundation: Extends depth-scale transfer to figures whose feet or ground contact are cropped or occluded by carrying a trustworthy visible homologous landmark through the solved perspective field and rebuilding the visible figure from that transferred scale.
  when_to_use: Use when equal-height figures share the relevant plane relationship but one figure's feet are hidden by framing, furniture, foreground overlap, or another occluder.
  when_not_to_use: Do not assume the transfer is valid when the compared figures differ materially in real height/proportion or stand on unrelated elevations; solve those differences first.
  absorbed_from_object_id: none
---

# Carry Scale Through Depth With Height and Width Guides

## Pattern Rule
**IF** equal-height or equal-width subjects must remain consistently scaled at different depths on the same plane, **THEN** establish one trusted measurement and project guide lines through the solved vanishing field instead of resizing each subject by eye.

## Do
- Establish one known vertical height at a trustworthy position.
- Project its top and bottom through the relevant vanishing directions to transfer that height elsewhere on the same plane.
- Use the observer's eye level as a repeated proportion check for equal-height figures on level ground.
- Carry widths through depth with the same vanishing logic, then translate the result vertically or horizontally where needed.
- Treat a change in ground elevation as a change in the height relationship, not as evidence that the eye-level rule failed.

## Don't
- Scale each distant figure independently by intuition after the scene field is solved.
- Apply a level-ground eye-line proportion unchanged to a figure standing uphill, downhill, or on another floor.
- Use screen-space equal spacing as a substitute for perspective scale.

## Checklist
- Equal real-world heights shrink consistently with distance.
- On one level plane, equivalent figure landmarks keep the same relationship to eye level.
- Width and height guides agree with the same vanishing field.
- A moved object can be checked against a known object without re-solving the whole scene.

## Notes
This is the general scene-space counterpart to figure-derived calibration: D'Amelio supplies the independent eye-level and vanishing framework that the earlier Hogarth candidate explicitly left open.

**Boundaries**
This Pattern transfers scale on established planes. Use inclined-plane construction when the supporting plane changes slope.

`VAR_loomis_scale_cropped_figures_from_visible_landmarks` removes the hidden-feet dependency: when ground contact is unavailable, project a visible corresponding landmark through the same solved field and reconstruct the remaining visible figure around that scale.

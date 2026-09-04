---
object_id: AP_project_plan_and_elevation_into_perspective
object_type: ap
name: Project Plan and Elevation Into Perspective
library_path:
- art
- perspective
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- plan
- elevation
- projection
cross_links:
- rel: supports
  target_object_id: PAT_establish_eye_level_and_vanishing_directions
- rel: supports
  target_object_id: PAT_project_plan_points_through_station_point_to_picture_plane
- rel: supports
  target_object_id: PAT_transfer_elevation_heights_from_true_measure_line
- rel: supports
  target_object_id: PAT_carry_scale_through_depth_with_height_and_width_guides
reference:
  source_title: Perspective Made Easy
  author: Ernest R. Norling
confidence: high
references: []
variants:
- variant_id: VAR_loomis_project_small_interior_then_enlarge_freehand
  variant_name: Project a Small Interior, Then Enlarge Freehand
  variant_basis: method_sequence
  difference_from_foundation: 'Uses exact-enough plan projection as a compact planning scaffold rather than as the final drawing:
    arrange the room and figures in plan, rotate or audition the ground plan to test what the chosen camera will reveal, project
    the selected layout and key heights into a small perspective study, then enlarge that solved study and return to freehand
    drawing for the finished illustration.'
  when_to_use: Use when an interior or staged scene needs trustworthy spatial relationships but the final image should retain
    natural drawing rather than read like mechanical drafting.
  when_not_to_use: Do not enlarge a faulty miniature blindly; verify the small projection first, and retain full mechanical
    construction when exact technical documentation is the actual goal.
  absorbed_from_object_id: none
---

# Project Plan and Elevation Into Perspective

## Objective
Construct an exact perspective view from orthographic plan and elevation information instead of estimating the object's projected footprint and height by eye.

## Steps / Flow
**Entry Conditions**
- A usable plan and elevation, or equivalent orthographic dimensions, exist.
- The intended viewpoint and picture-plane relationship can be chosen.

**Persistent Invariants**
- Plan controls horizontal location and direction; elevation controls true vertical height.
- Visual rays from the station point/eye determine where plan points pierce the picture plane.
- Vanishing points derive from direction, not from convenient page placement.
- Height is transferred from a true-measure location before being carried through perspective.

**Flow**
1. **Establish the projection setup.** Apply the exact camera/viewfield variant of `PAT_establish_eye_level_and_vanishing_directions`: place the object plan relative to the Picture Plane, choose the station point/eye, and establish the Horizon Line and Ground Line for the perspective view.
2. **Project the plan.** Apply `PAT_project_plan_points_through_station_point_to_picture_plane` to the plan's controlling corners. Keep every projected vertical registered to the visual ray and Picture Plane intersection that generated it.
3. **Derive the horizontal vanishing points.** Under `PAT_establish_eye_level_and_vanishing_directions`, draw station-point lines parallel to the plan's principal direction families and transfer their Picture Plane intersections into the Horizon Line.
4. **Transfer true heights.** Apply `PAT_transfer_elevation_heights_from_true_measure_line`: register a true-measure/ground-line location with the corresponding projected point, then place the elevation's real vertical intervals there.
5. **Carry heights through the field.** Apply `PAT_carry_scale_through_depth_with_height_and_width_guides` to carry those true-height marks toward the correct vanishing directions and intersect them with the plan-fixed verticals.
6. **Complete the form.** Join corresponding corners and add only details whose plan/elevation position can be supported by the same construction.
7. **Validate.** Trace important projected corners back to both the plan ray and elevation height that generated them.

**Failure / Rollback Rules**
- If projected footprints do not agree with the plan rays, return to the station-point projection before adjusting heights.
- If edge families converge inconsistently, recompute their vanishing directions from the plan rather than moving individual corners.
- If heights drift, return to the true-measure transfer from the elevation.
- If the construction becomes too dense for a freehand task, downgrade to the simpler shared-scene perspective AP unless exact orthographic transfer is actually required.

**Completion Criteria**
- Major projected corners can be traced to valid plan rays.
- True heights can be traced to the supplied elevation before depth projection.
- Parallel world directions share their correct vanishing destinations.
- The result reproduces the intended plan/elevation geometry from the chosen view without screen-space guessing.

## Notes
This is the mechanical/architectural route: slower and more exact than freehand perspective, useful when a design must be projected faithfully from known orthographic information. `VAR_loomis_project_small_interior_then_enlarge_freehand` is the illustrator-oriented version: use the ground plan not only to place things accurately but also as a cheap camera-search device, rotating or auditioning the arrangement before projection; then solve the selected view small, verify it, enlarge, and return to freehand handling for the final image.

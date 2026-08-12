---
schema_version: vNext-draft.1
object_id: AP_project_plan_and_elevation_into_perspective
object_type: ap
name: Project Plan and Elevation Into Perspective
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- plan
- elevation
- projection
scope:
  role: specialization
  axis: workflow
  foundation_object_id: null
bindings:
  development_stages: []
  execution_profiles:
  - direct_dream
  - staged
  - teaching
capabilities:
  provides:
  - art.drawing.perspective.project_plan_and_elevation
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  - art.drawing.perspective.choose_convergence_from_view_and_orientation
  optional:
  - art.drawing.perspective.carry_scale_through_depth
  excludes: []
context:
  residency: phase
  priority: 82
  load_when:
  - the task needs an exact perspective constructed from orthographic plan and elevation information
  unload_when:
  - the projected object or scene has been located and checked
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: norling_p193_201
    kind: source
    source_id: ernest_norling_perspective_made_easy
    locator: printed pp. 193-201
    evidence_type: mixed
    note: Norling's mechanical and architect's methods use plan, elevation, picture plane, station point/eye, visual rays, ground line, horizon, and vanishing points to project exact plan positions and true heights into perspective.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  execution_profiles:
    supported:
    - direct_dream
    - staged
    - teaching
    preferred: staged
  commitment_ledger:
    enabled: false
    persist_across_swaps: false
  states:
  - state_id: establish_projection_setup
    objective: Fix the picture plane, station point or eye, horizon, ground line, and relationship of plan and elevation.
    requires:
    - art.drawing.perspective.establish_eye_level_and_vanishing_directions
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - project_plan_points
  - state_id: project_plan_points
    objective: Send visual rays from the station point through plan corners to locate where those rays cross the picture plane.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - establish_direction_vanishing_points
  - state_id: establish_direction_vanishing_points
    objective: Derive the horizontal direction vanishing points from the station point and the plan directions.
    requires:
    - art.drawing.perspective.choose_convergence_from_view_and_orientation
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - transfer_true_heights
  - state_id: transfer_true_heights
    objective: Carry true heights from elevation onto the appropriate ground-line or measuring location before projecting them through depth.
    requires: []
    optional:
    - art.drawing.perspective.carry_scale_through_depth
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - complete_projected_form
  - state_id: complete_projected_form
    objective: Use the recovered plan positions, height transfers, and vanishing directions to construct the final perspective form.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: false
    transitions:
    - validate_projection
  - state_id: validate_projection
    objective: Check projected corners, heights, and direction families back against the supplied plan and elevation.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions: []
---

# Project Plan and Elevation Into Perspective

## Objective
Construct an exact perspective view from orthographic plan and elevation information instead of estimating the object's projected footprint and height by eye.

## Entry Conditions
- A usable plan and elevation, or equivalent orthographic dimensions, exist.
- The intended viewpoint and picture-plane relationship can be chosen.

## Persistent Invariants
- Plan controls horizontal location and direction; elevation controls true vertical height.
- Visual rays from the station point/eye determine where plan points pierce the picture plane.
- Vanishing points derive from direction, not from convenient page placement.
- Height is transferred from a true-measure location before being carried through perspective.

## Flow
1. **Establish the projection setup.** Place the object plan relative to the Picture Plane, choose the station point/eye, and establish the Horizon Line and Ground Line for the perspective view.
2. **Project the plan.** Draw visual rays from the station point through the plan's controlling corners. Where they cross the Picture Plane establishes projected plan positions.
3. **Derive the horizontal vanishing points.** From the station point, draw lines parallel to the plan's principal direction families; transfer their intersections with the Picture Plane into the Horizon Line of the perspective construction.
4. **Transfer true heights.** Use the elevation to place real heights at a true-measure/ground-line location associated with the corresponding projected point.
5. **Carry heights through the field.** Project those height marks toward the correct vanishing directions and intersect them with the verticals already fixed by the plan projection.
6. **Complete the form.** Join corresponding corners and add only details whose plan/elevation position can be supported by the same construction.
7. **Validate.** Trace important projected corners back to both the plan ray and elevation height that generated them.

## Failure / Rollback Rules
- If projected footprints do not agree with the plan rays, return to the station-point projection before adjusting heights.
- If edge families converge inconsistently, recompute their vanishing directions from the plan rather than moving individual corners.
- If heights drift, return to the true-measure transfer from the elevation.
- If the construction becomes too dense for a freehand task, downgrade to the simpler shared-scene perspective AP unless exact orthographic transfer is actually required.

## Completion Criteria
- Major projected corners can be traced to valid plan rays.
- True heights can be traced to the supplied elevation before depth projection.
- Parallel world directions share their correct vanishing destinations.
- The result reproduces the intended plan/elevation geometry from the chosen view without screen-space guessing.

## Notes
Norling presents this as the mechanical/architect's route: slower and more exact than freehand perspective, useful when a design must be projected faithfully from known orthographic information.

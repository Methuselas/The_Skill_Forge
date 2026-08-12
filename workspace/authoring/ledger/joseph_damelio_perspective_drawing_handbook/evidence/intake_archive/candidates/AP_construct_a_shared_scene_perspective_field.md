---
schema_version: vNext-draft.1
object_id: AP_construct_a_shared_scene_perspective_field
object_type: ap
name: Construct a Shared Scene Perspective Field
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- scene
- construction
- workflow
scope:
  role: foundation
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
  - art.drawing.perspective.construct_shared_scene_field
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  - art.drawing.perspective.choose_convergence_from_view_and_orientation
  optional:
  - art.drawing.perspective.carry_scale_through_depth
  - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
  - art.drawing.perspective.construct_inclined_planes
  - art.drawing.perspective.construct_projected_circles
  excludes: []
context:
  residency: phase
  priority: 95
  load_when:
  - the task needs construct a shared scene perspective field
  unload_when:
  - the relevant spatial construction or correction is complete
relations:
- rel: orchestrates
  target_object_id: PAT_establish_eye_level_and_vanishing_directions
- rel: orchestrates
  target_object_id: PAT_choose_convergence_from_view_and_orientation
- rel: compatible_with
  target_object_id: PAT_build_shared_scene_perspective_from_figure
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p18_36
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 18-36
    evidence_type: mixed
    note: Picture-plane, eye-level, and vanishing-point chapters establish the viewing field.
  - evidence_id: damelio_p37_86
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 37-86
    evidence_type: mixed
    note: Cube, distortion, scale, measurement, incline, circle, cylinder, and cone chapters progressively specialize that field.
  derivations:
  - derivation_id: scene_ap_synthesis
    kind: synthesis
    inputs:
    - damelio_p18_36
    - damelio_p37_86
    note: Orchestrates the book's progressively layered construction order without requiring every mathematical aid in every drawing.
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
    enabled: true
    persist_across_swaps: true
  states:
  - state_id: set_view
    objective: Establish the observer/view relationship and eye level.
    requires: []
    optional: []
    warmup_capabilities:
    - activation.art.drawing.perspective.box_rotation_warmup
    release_on_exit: []
    checkpoint: true
    transitions:
    - solve_directions
  - state_id: solve_directions
    objective: Assign vanishing behavior to the scene's dominant direction families.
    requires:
    - art.drawing.perspective.establish_eye_level_and_vanishing_directions
    - art.drawing.perspective.choose_convergence_from_view_and_orientation
    optional:
    - art.drawing.perspective.control_distortion_with_vanishing_spacing
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - block_scene
  - state_id: block_scene
    objective: Construct major figures/objects on one shared spatial field.
    requires:
    - art.drawing.perspective.block_objects_with_boxes
    optional:
    - art.drawing.perspective.carry_scale_through_depth
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - specialize_geometry
  - state_id: specialize_geometry
    objective: Load only the metrology, slopes, or round-form construction the scene actually needs.
    requires: []
    optional:
    - art.drawing.perspective.measure_subdivide_and_repeat_on_planes
    - art.drawing.perspective.construct_inclined_planes
    - art.drawing.perspective.construct_projected_circles
    - art.drawing.perspective.align_cylinders_and_cones
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: false
    transitions:
    - validate_field
  - state_id: validate_field
    objective: Check shared convergence, scale, and distortion before detail locks the scene.
    requires:
    - art.drawing.perspective.establish_eye_level_and_vanishing_directions
    optional:
    - art.drawing.perspective.control_distortion_with_vanishing_spacing
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions: []
---

# Construct a Shared Scene Perspective Field

## Objective
Build one coherent perspective field that can govern figures, objects, and environment, then load only the precision constructions the scene actually needs.

## Entry Conditions
- The scene viewpoint is not yet locked, or multiple objects/figures must share one convincing spatial world.
- The task benefits from explicit perspective construction rather than purely observational copying.

## Persistent Invariants
- One observer/view relationship governs the scene.
- Horizontal-world vanishing directions share one eye-level line.
- Objects that share a real direction share the corresponding vanishing behavior.
- Scale and repeated spacing are constructed on the solved field, not guessed independently.
- Optional technical geometry is loaded only when it answers a concrete placement problem.

## Flow
1. **Set the view.** Decide what the observer sees and establish eye level.
2. **Solve dominant directions.** Group the scene's main parallel directions and assign their vanishing behavior from orientation.
3. **Block the scene.** Use box masses, a trusted figure, or both to establish large placements and shared scale.
4. **Check distortion.** If edge regions become implausibly stretched, correct vanishing spacing or crop before continuing.
5. **Specialize only as needed.** Load height/width transfer, plane subdivision, inclined planes, or round-solid construction only where the scene asks for them.
6. **Validate the field.** Check that major objects, figures, and planes still agree before detail and rendering obscure construction errors.

## Failure / Rollback Rules
- If several objects require different vanishing destinations for what should be the same real direction, return to dominant-direction setup.
- If equal-scale subjects drift with depth, return to height/width guides.
- If edge distortion grows while the center is sound, adjust vanishing spacing/crop rather than patching objects locally.
- If a specialized construction becomes more complicated than the visual problem, roll back to the simplest sufficient guide.

## Completion Criteria
- The viewer can infer one coherent eye level and spatial field.
- Major direction families converge consistently.
- Figures and objects preserve believable relative scale across depth.
- Any slopes, circles, repeats, or measured designs inherit the same field.
- The scene is ready for downstream drawing/rendering without perspective correction being hidden by detail.

## Notes
This AP is intentionally equation-light. D'Amelio's geometric theory is retained as cause, but the runtime procedure is visual construction: establish, project, check, and only measure when necessary.

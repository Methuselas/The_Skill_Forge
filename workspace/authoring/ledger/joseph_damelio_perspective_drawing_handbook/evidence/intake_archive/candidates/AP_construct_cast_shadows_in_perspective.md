---
schema_version: vNext-draft.1
object_id: AP_construct_cast_shadows_in_perspective
object_type: ap
name: Construct Cast Shadows in Perspective
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- shadow
- light
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
  - art.drawing.perspective.construct_cast_shadows
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional:
  - art.drawing.perspective.construct_inclined_planes
  excludes: []
context:
  residency: phase
  priority: 88
  load_when:
  - the task needs construct cast shadows in perspective
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p87_92
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 87-92
    evidence_type: mixed
    note: D'Amelio distinguishes shade from cast shadow, identifies the shade line as the source boundary, and constructs sunlight shadows from parallel light rays and shadow vanishing directions.
  - evidence_id: damelio_p93_96
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 93-96
    evidence_type: mixed
    note: Local point-light shadows are constructed from rays diverging from the light source and its projection onto the receiving plane.
  derivations:
  - derivation_id: shadow_ap_synthesis
    kind: synthesis
    inputs:
    - damelio_p87_92
    - damelio_p93_96
    note: Combines the book's sunlight and local-light constructions into one branched protocol while preserving their different ray behavior.
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
  - state_id: classify_light
    objective: Determine whether the source is effectively parallel sunlight or a local point source.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - find_shade_boundary
  - state_id: find_shade_boundary
    objective: Locate the form boundary separating light from shade that will cast the shadow.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - solve_shadow_direction
  - state_id: solve_shadow_direction
    objective: Establish the shadow direction on the receiving plane and the light-ray direction.
    requires:
    - art.drawing.perspective.establish_eye_level_and_vanishing_directions
    optional:
    - art.drawing.perspective.construct_inclined_planes
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions:
    - project_shadow_points
  - state_id: project_shadow_points
    objective: Intersect light rays with shadow-direction construction to locate cast-shadow points.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: false
    transitions:
    - validate_shadow
  - state_id: validate_shadow
    objective: Check that shadow length/direction and receiving-plane perspective are coherent.
    requires: []
    optional: []
    warmup_capabilities: []
    release_on_exit: []
    checkpoint: true
    transitions: []
---

# Construct Cast Shadows in Perspective

## Objective
Project cast shadows so the light direction, receiving plane, object position, and scene perspective all agree.

## Entry Conditions
- A cast shadow must be placed constructively rather than guessed from value alone.
- The receiving plane and the object's placement are sufficiently established to support projection.

## Persistent Invariants
- Shade is the unlit side of the form; cast shadow is the region on another surface from which the light is blocked.
- The shade boundary supplies the points that cast the shadow.
- Sunlight is treated as parallel rays; a nearby point light uses rays diverging from the source.
- Shadow construction must remain consistent with the receiving plane's perspective.

## Flow
1. **Classify the light.** Use the parallel-sun branch or the local-point-source branch.
2. **Find the shade boundary.** Identify the object's edge or line separating light-facing and turned-away surfaces.
3. **Solve the receiving-plane direction.** Establish how shadow-bearing lines travel across that plane.
4. **Parallel sunlight branch.** Keep the light rays parallel in space. When oblique to the picture plane, use the light-ray vanishing point and the shadow-direction vanishing point in their corresponding perspective relationship.
5. **Local point-source branch.** Draw rays from the actual light source through the relevant shade-boundary points; use the source's projection onto the plane to establish the shadow direction for upright forms.
6. **Intersect constructions.** The intersections locate exact cast-shadow points; connect them in the order supplied by the casting boundary.
7. **Validate.** Confirm that a lower sun gives longer projected shadows and a higher sun shorter ones in the book's construction, and that local-light shadows fan consistently from the source.

## Failure / Rollback Rules
- If the shadow direction contradicts the receiving plane, re-solve that plane before moving the shadow.
- If sunlight rays diverge, return to the parallel-light branch.
- If a point-source shadow behaves as parallel sunlight, return to source projection and ray intersections.
- If the casting boundary is wrong, repair the shade line before adjusting the shadow contour.

## Completion Criteria
- Shadow points can be traced back to valid casting points and light rays.
- The shadow lies on the receiving plane rather than floating over it.
- Parallel and point-source lights produce visibly different but internally coherent projection behavior.
- The cast shadow supports, rather than contradicts, the scene's established depth field.

## Notes
D'Amelio's chapter is geometric, but the operational question is simple: identify what blocks the light, establish how the rays travel, and solve where those rays meet the receiving surface.

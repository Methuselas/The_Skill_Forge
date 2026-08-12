---
schema_version: vNext-draft.1
object_id: PAT_establish_eye_level_and_vanishing_directions
object_type: pattern
name: Establish Eye Level and Vanishing Directions
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- eye_level
- vanishing_point
- horizon
scope:
  role: foundation
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
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  requires: []
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 90
  load_when:
  - the task needs establish eye level and vanishing directions
  unload_when:
  - the relevant spatial construction or correction is complete
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p23_32
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 23-32
    evidence_type: mixed
    note: D'Amelio derives vanishing points for parallel line families and the horizontal vanishing line at the observer's eye level.
  - evidence_id: damelio_p33_36
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 33-36
    evidence_type: mixed
    note: The eye-level line shifts in the picture when the observer looks down or up, and its placement is chosen deliberately for the view.
  derivations:
  - derivation_id: eye_level_vp_synthesis
    kind: synthesis
    inputs:
    - damelio_p23_32
    - damelio_p33_36
    note: Combines the book's two principal aids into one scene-setup rule.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Establish Eye Level and Vanishing Directions

## Pattern Rule
**IF** a scene contains sets of parallel directions receding in depth, **THEN** establish the observer's eye level and give each receding parallel family its own vanishing point; horizontal-world families place their vanishing points on the eye-level line.

## Do
- Mark the eye level before solving repeated horizontal directions.
- Group edges by the real direction they share, then converge each group toward one common vanishing point.
- Keep different direction families separate; a scene may need several vanishing points.
- Let the eye-level line move upward in the picture when looking downward and downward when looking upward; it may lie outside the frame.
- Use a visible natural horizon as the eye-level line when the source view supplies one.

## Don't
- Give unrelated sets of parallels one vanishing point merely because they are all horizontal in the world.
- Place the horizon by composition habit and then force the geometry to fit it.
- Assume the eye-level line must be visible inside the drawing.

## Checklist
- Every repeated receding direction has a consistent vanishing destination.
- All horizontal-world vanishing points lie on one eye-level line.
- The amount of top or underside visible agrees with the chosen eye level.
- Looking up, down, or straight out produces the expected shift in the eye-level line.

## Boundaries
This Pattern establishes the principal perspective field. It does not by itself measure intervals, construct inclined planes, or solve cast shadows.

## Notes
D'Amelio treats vanishing points and eye level as practical aids derived from lines of sight, not as arbitrary drawing conventions.

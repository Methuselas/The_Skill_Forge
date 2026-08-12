---
schema_version: vNext-draft.1
object_id: PAT_choose_convergence_from_view_and_orientation
object_type: pattern
name: Choose Convergence From View and Object Orientation
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- convergence
- one_point
- two_point
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
  - art.drawing.perspective.choose_convergence_from_view_and_orientation
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 88
  load_when:
  - the task needs choose convergence from view and object orientation
  unload_when:
  - the relevant spatial construction or correction is complete
relations:
- rel: supports
  target_object_id: PAT_establish_eye_level_and_vanishing_directions
grounding:
  mode: source_led
  evidence:
  - evidence_id: damelio_p37_49
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 37-49
    evidence_type: mixed
    note: Cube studies show how three parallel direction families change as the object and view change, including vertical convergence in up/down views.
  - evidence_id: damelio_p50_57
    kind: source
    source_id: joseph_damelio_perspective_drawing_handbook
    locator: printed pp. 50-57
    evidence_type: mixed
    note: One-point and two-point appearances follow orientation to the picture plane; looking up or down can also make verticals converge.
  derivations:
  - derivation_id: orientation_convergence_synthesis
    kind: synthesis
    inputs:
    - damelio_p37_49
    - damelio_p50_57
    note: Generalizes the cube demonstrations into a direction-family selection rule instead of treating named perspective systems as stylistic recipes.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Choose Convergence From View and Object Orientation

## Pattern Rule
**IF** you must decide whether an edge family stays parallel in the picture or converges, **THEN** decide from that family's orientation to the picture plane and central viewing direction rather than choosing a named one-, two-, or three-direction setup by habit.

## Do
- Treat a rectangular object as three families of mutually different parallel directions.
- Keep a family parallel in the drawing when it is parallel to the picture plane.
- Converge a family when it recedes through depth.
- Let a horizontal family point to the central vanishing point when it runs directly away from the observer.
- When looking materially up or down, allow vertical-world lines to converge toward their own upper or lower vanishing point.

## Don't
- Move the main vanishing point off center while mechanically keeping the perpendicular horizontal family parallel if the view no longer supports that condition.
- Force all verticals to remain vertical when the chosen view is clearly pitched up or down.
- Choose “one-point” or “two-point” first and bend the subject to the label afterward.

## Checklist
- Each line family behaves consistently with one three-dimensional direction.
- A face nearly parallel to the picture plane shows less convergence than a face turned away.
- The chosen convergence explains the view rather than decorating it.
- Up/down views are not flattened by an automatic vertical-line rule.

## Boundaries
This Pattern selects convergence topology. It does not determine exact spacing or correct excessive distortion.

## Notes
D'Amelio's cube sequence is the practical carrier for this rule: named systems are consequences of view and orientation.

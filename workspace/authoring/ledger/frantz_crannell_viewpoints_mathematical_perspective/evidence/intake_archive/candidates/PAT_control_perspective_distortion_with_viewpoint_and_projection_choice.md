---
schema_version: vNext-draft.1
object_id: PAT_control_perspective_distortion_with_viewpoint_and_projection_choice
object_type: pattern
name: Control Perspective Distortion With Viewpoint and Projection Choice
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- distortion
- viewpoint
- projection
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
  - art.drawing.perspective.control_distortion_with_viewpoint_and_projection_choice
  - art.drawing.perspective.control_distortion_with_vanishing_spacing
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional:
  - art.drawing.perspective.validate_three_point_viewpoint_geometry
  - art.drawing.perspective.recover_view_field_from_existing_image
  excludes: []
context:
  residency: triggered
  priority: 90
  load_when:
  - the scene has excessive edge stretch, unnaturally rapid convergence, an extreme
    close-up or skyscraper view, or uncertainty about whether rectilinear perspective
    is the right projection for the intended field
  unload_when:
  - the intended viewpoint, support/frame, and projection model produce one coherent
    field without local perspective repairs
relations:
- rel: supersedes
  target_object_id: PAT_control_perspective_distortion_with_vanishing_spacing
- rel: related_to
  target_object_id: PAT_validate_three_point_viewpoint_geometry
grounding:
  mode: source_led
  evidence:
  - evidence_id: viewpoints_pp32_35_station_point
    kind: source
    source_id: frantz_crannell_viewpoints_mathematical_perspective
    locator: printed pp. 32-35 (physical PDF pp. 47-50)
    evidence_type: mixed
    note: Frantz and Crannell show that a perspective image has a specific correct
      station point/viewing distance and that a valid cube can look badly distorted
      when the viewer is too far from that point.
  - evidence_id: viewpoints_pp61_64_viewing_circle
    kind: source
    source_id: frantz_crannell_viewpoints_mathematical_perspective
    locator: printed pp. 61-64 (physical PDF pp. 76-79)
    evidence_type: mixed
    note: For standard two-point perspective, orthogonal horizontal vanishing points
      define a viewing semicircle. Spreading the vanishing points enlarges the set
      of plausible viewing positions and reduces mismatch for a casual viewer.
  - evidence_id: viewpoints_pp93_98_target_distance
    kind: source
    source_id: frantz_crannell_viewpoints_mathematical_perspective
    locator: printed pp. 93-98 (physical PDF pp. 108-113)
    evidence_type: mixed
    note: Rapid-looking convergence is diagnosed as a viewing-distance mismatch; the
      authors recommend avoiding near-degenerate viewpoint triangles and clustering
      important content near the viewing target.
  - evidence_id: viewpoints_pp100_106_skyscraper_sphere
    kind: source
    source_id: frantz_crannell_viewpoints_mathematical_perspective
    locator: printed pp. 100-106 (physical PDF pp. 115-121)
    evidence_type: mixed
    note: The skyscraper paradox shows that flat rectilinear perspective can be mathematically
      correct yet require an impractically large support or extremely close station
      point to reproduce a close tall-building experience; spherical perspective is
      presented as a compact alternative projection surface.
  - evidence_id: robertson_wide_field_grid_choice
    kind: source
    source_id: scott_robertson_how_to_draw
    locator: printed pp. 62-64, 118, 186-187
    evidence_type: mixed
    note: Robertson distinguishes ordinary linear design grids from wide-angle warped/curvilinear
      treatments and ties stronger edge effects to field of view.
  derivations:
  - derivation_id: viewpoint_projection_distortion_synthesis
    kind: synthesis
    inputs:
    - viewpoints_pp32_35_station_point
    - viewpoints_pp61_64_viewing_circle
    - viewpoints_pp93_98_target_distance
    - viewpoints_pp100_106_skyscraper_sphere
    - robertson_wide_field_grid_choice
    note: Replaces the earlier VP-spacing-only rule with a decision system that separates
      construction error from station-point/display mismatch and then chooses framing,
      support scale, or projection model globally.
  claim_map: {}
assets: []
variants:
- variant_id: VAR_rectilinear_viewpoint_match
  name: Rectilinear Viewpoint Match
  trigger: The intended image is a conventional flat-plane perspective and apparent
    distortion may be caused by viewing or framing mismatch.
  changes:
  - Recover or derive the viewing target and viewing distance before changing local
    objects.
  - Reframe, crop, move the station point, spread vanishing points consistently, enlarge
    the support, or cluster important content nearer the viewing target.
- variant_id: VAR_extreme_field_projection_swap
  name: Extreme-Field Projection Swap
  trigger: One compact image must cover a close, very tall, very wide, or near-immersive
    field that would demand an impractically close station point or very large flat
    support.
  changes:
  - Consider a curvilinear or spherical projection rather than forcing one rectilinear
    grid to carry the entire field.
  - Preserve the same scene directions and viewpoint logic while changing the projection
    surface/model.
spec:
  form: decision_rule
---

# Control Perspective Distortion With Viewpoint and Projection Choice

## Pattern Rule
**IF** perspective looks stretched, pinched, unnaturally rapid, or implausibly flat **THEN** first determine whether the construction is wrong or whether a valid construction is being viewed/framed from the wrong station relationship; correct the field globally through viewpoint, framing/support scale, or projection choice before repairing individual objects.

## Do
- Recover or establish the viewing target and viewing distance when the view is exact enough to justify it.
- Treat vanishing-point spacing as one consequence of the viewpoint geometry, not as the only distortion control.
- When a flat-plane image is valid but requires an implausibly close station point, move the viewpoint back and rebuild the field, crop/reframe, enlarge the support, or cluster key content nearer the viewing target.
- For a close skyscraper or other very large angular field, distinguish a mathematically valid rectilinear image from a practical display problem: the flat image may need to be physically huge to be experienced from a comfortable distance.
- When the intended compact image must preserve a much wider directional field than a practical flat-plane setup can carry, switch deliberately to a curvilinear/spherical projection rather than locally bending objects inside a rectilinear field.
- Keep prior Norling/Gill production checks: compare equivalent forms near the center and edges, and prefer a global reframe over local compensations.

## Don't
- Assume that edge distortion proves the perspective construction itself is mathematically wrong; test the implied station point first.
- Treat 50° or 60° as a universal mathematical cutoff. The audited source does not establish a single fixed cone-of-vision threshold.
- Add fake extra vanishing points to a face that is parallel to a flat picture plane merely to imitate the sensation of looking up and down a nearby skyscraper.
- Mix rectilinear and curvilinear rules accidentally inside the same field.
- Repair each object separately after the camera/viewfield has already become inconsistent.

## Checklist
- The implied station point/viewing distance is known or at least directionally plausible for the intended presentation.
- Equivalent objects do not change perspective logic merely because they approach the frame edge.
- Important content sits in a usable relation to the viewing target unless deliberate edge stress is intended.
- A close tall/wide scene has an explicit decision: larger support/reframe versus alternate projection.
- The chosen projection model is consistent across the full scene.
- No fixed numeric COV rule is being mistaken for a theorem.

## Notes
This Pattern supersedes the earlier D'Amelio VP-spacing-only card. *Viewpoints* resolves the key ambiguity: rectilinear perspective can remain geometrically exact at an extreme field, but only from its implied station point and support geometry. Practical distortion control therefore depends on the intended viewer/display as well as the vanishing geometry. Spherical/curvilinear projection is a deliberate alternate model for compact extreme fields, not a local correction applied after the fact.

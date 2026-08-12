---
schema_version: vNext-draft.1
object_id: PAT_construct_reflections_across_arbitrary_planes
object_type: pattern
name: Construct Reflections Across Arbitrary Planar Mirrors
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- reflection
- mirror
- oblique
scope:
  role: specialization
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
  - art.drawing.perspective.construct_arbitrary_planar_reflections
  - art.drawing.perspective.construct_level_planar_reflections
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional:
  - art.drawing.perspective.construct_inclined_planes
  - art.drawing.perspective.measure_true_lengths_on_oblique_planes
  - art.drawing.perspective.project_plan_and_elevation
  excludes: []
context:
  residency: triggered
  priority: 87
  load_when:
  - a reflection in calm water, a vertical mirror, or a tipped planar mirror must be constructed rather than copied by eye
  unload_when:
  - the reflected control geometry and direction families are established
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: white_p24
    kind: source
    source_id: gwen_white_perspective_guide
    locator: printed p. 24 (PDF p. 25)
    evidence_type: mixed
    note: White constructs level-water reflections as mirrored geometry across the horizontal reflecting plane.
  - evidence_id: white_pp72_79
    kind: source
    source_id: gwen_white_perspective_guide
    locator: printed pp. 72-79 (PDF pp. 73-80)
    evidence_type: mixed
    note: White constructs reflections in vertical and tipped mirrors by combining equal incidence/reflection angles with plan/elevation or oblique-perspective projection, including reflected direction families that differ from the source object's original vanishing directions.
  derivations:
  - derivation_id: white_reflection_generalization
    kind: synthesis
    inputs:
    - white_p24
    - white_pp72_79
    note: Generalizes the level-plane reflection case into one planar-mirror rule while preserving the simpler Norling water/level-mirror branch.
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Construct Reflections Across Arbitrary Planar Mirrors

## Pattern Rule
**IF** a planar reflecting surface is not necessarily level, **THEN** treat the reflection as real geometry mirrored across that plane: establish the mirror plane, reflect controlling points/directions using equal incidence and reflection, derive the reflected direction families, and then project the reflected geometry through the same camera/view field.

## Do
- Establish the mirror plane before drawing the reflected object: its trace/direction and, when tipped, its plane orientation matter.
- Use a small plan and/or elevation when the reflected direction is not obvious; reflect rays/directions so the angle of incidence equals the angle of reflection.
- Use source-to-mirror contact points as anchors where structural lines meet the mirror plane.
- Preserve equal perpendicular source/image distance across a level mirror or calm-water plane; this is the simple branch already captured by Norling.
- For vertical or tipped mirrors, derive the reflected direction family from the mirror geometry rather than reusing the source object's vanishing point automatically.
- Once the reflected geometry is defined in space, construct it with ordinary perspective/oblique-perspective methods and measuring points as needed.
- Validate with both position and direction: a reflected point must be located correctly across the mirror, and reflected parallel edges must converge according to their reflected world direction.

## Don't
- Flip the visible silhouette in screen space and assume the result is a valid perspective reflection.
- Give every mirror reflection the source object's original vanishing points; that is only safe in specific symmetric/level cases.
- Treat the mirror as decoration after the reflected object has already been guessed.
- Use the advanced tipped-mirror construction when a simple calm-water equal-distance reflection is sufficient.

## Checklist
- The mirror plane has a coherent orientation in the scene.
- Source and reflected constructions satisfy equal incidence/reflection in the plan/elevation used to derive them.
- Contact points on the mirror remain fixed between source and reflected geometry.
- Reflected parallel families share their own correct vanishing destinations.
- The level-plane branch collapses cleanly to equal perpendicular distances across the reflecting plane.

## Boundaries
This Pattern covers flat mirrors and calm planar water. Curved mirrors, rippled water, refractive surfaces, and lens effects require different optics and are not inferred from White's planar constructions.

## Notes
This candidate intentionally **subsumes** Norling's level-plane reflection Pattern if committed. The simple level reflection remains a fast branch; White earns the general planar case.

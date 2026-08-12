---
schema_version: vNext-draft.1
object_id: PAT_construct_reflections_across_level_planes
object_type: pattern
name: Construct Reflections Across Level Planes
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- reflection
- water
- mirror
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
  - art.drawing.perspective.construct_level_planar_reflections
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 84
  load_when:
  - the task needs a constructed reflection on calm water, a level mirror, or another level flat reflecting plane
  unload_when:
  - the reflection geometry is established
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: norling_p169_173
    kind: source
    source_id: ernest_norling_perspective_made_easy
    locator: printed pp. 169-173
    evidence_type: mixed
    note: Norling constructs reflected points the same distance below the reflecting surface that their source points are above it and shows the reflection sharing the object's vanishing behavior on the level reflecting plane.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Construct Reflections Across Level Planes

## Pattern Rule
**IF** an object is reflected by a level flat surface such as calm water or a horizontal mirror, **THEN** mirror each controlling point across that surface by the same perpendicular distance and reconstruct the reflected form with the same perspective direction families as the object.

## Do
- Establish the reflecting plane before drawing the reflection.
- Drop or raise construction lines perpendicular to the level reflecting surface from key object points.
- Place each reflected point the same distance on the opposite side of the surface as its source point.
- Reconnect reflected points according to the object's structure and existing vanishing directions.
- Preserve the source object's horizontal vanishing behavior in the reflected construction.
- Treat a raised object as though its supporting distance also continues through the surface to locate the reflected object.

## Don't
- Copy the visible silhouette downward by eye when exact placement matters.
- Compress the reflected height merely because the object is farther from the viewer; perspective is already carried by the shared field.
- Give the reflection a different set of vanishing points from the object on the same level mirror/water setup.
- Generalize this card to tipped or arbitrarily oriented mirrors; later sources may require a broader plane-reflection construction.

## Checklist
- Every controlling source point has a corresponding reflected point at equal perpendicular distance across the surface.
- Structural edges in the reflection converge consistently with the source object's direction families.
- Raised objects produce an equal visual construction depth below the reflecting plane.
- The reflection reads as inverted across the surface rather than as a second object placed beneath it.

## Boundaries
This Pattern is intentionally scoped to the level reflecting planes Norling demonstrates. Tipped mirrors and arbitrary reflection planes are held for later perspective sources rather than inferred here.

## Notes
The useful production rule is simple: solve the reflected object as real geometry mirrored across the surface, then let the same perspective field project it.

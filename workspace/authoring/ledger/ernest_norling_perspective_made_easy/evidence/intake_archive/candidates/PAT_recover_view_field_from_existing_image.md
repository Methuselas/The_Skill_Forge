---
schema_version: vNext-draft.1
object_id: PAT_recover_view_field_from_existing_image
object_type: pattern
name: Recover a Perspective View Field From an Existing Image
library_path:
- art
- drawing
- perspective
status: candidate
confidence: high
tags:
- perspective
- vanishing_point
- eye_level
- reference_analysis
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
  - art.drawing.perspective.recover_view_field_from_existing_image
  requires:
  - art.drawing.perspective.establish_eye_level_and_vanishing_directions
  optional: []
  excludes: []
context:
  residency: triggered
  priority: 86
  load_when:
  - the task needs recover a perspective field, vanishing points, or eye level from an existing drawing or photograph
  unload_when:
  - the reference view has been diagnosed or transferred
relations: []
grounding:
  mode: source_led
  evidence:
  - evidence_id: norling_p35_36
    kind: source
    source_id: ernest_norling_perspective_made_easy
    locator: printed pp. 35-36
    evidence_type: mixed
    note: Norling extends image edges that represent real parallel directions to recover vanishing points, then uses the line through horizontal vanishing points to recover the camera eye level in a photograph or drawing.
  derivations: []
  claim_map: {}
assets: []
variants: []
spec:
  form: decision_rule
---

# Recover a Perspective View Field From an Existing Image

## Pattern Rule
**IF** an existing drawing or photograph contains reliable straight edges that represent parallel directions in the depicted world, **THEN** extend at least two edges from each direction family to their intersection to recover that family's vanishing point; use two recovered horizontal-world vanishing points to recover the eye-level line.

## Do
- Choose long, structurally reliable edges before small decorative lines.
- Group only edges that are parallel in the depicted world; extend each family until its members meet.
- Use the intersection of one family as that direction's vanishing point.
- Recover the eye level from the straight line through two distinct horizontal-world vanishing points.
- Extend the reference beyond its original crop when the intersections lie off-frame.
- Use the recovered field as a diagnostic or underlay rather than forcing every irregular mark to obey it.

## Don't
- Mix edges from different real-world directions because they look similar on the page.
- Treat a single horizontal-family vanishing point as enough to locate the full eye-level line without another valid cue.
- Assume lens distortion, curved architecture, deliberate perspective warping, or an inaccurate source image will produce perfectly intersecting straight families.
- Move the recovered vanishing points to make them convenient after the image has already fixed the view.

## Checklist
- Each vanishing point is supported by at least two independent edges from one real parallel family.
- The recovered horizontal vanishing points lie on one eye-level line.
- The inferred eye level agrees with visible top/underside relationships in the image.
- The analysis remains useful even when the vanishing points lie far outside the crop.

## Boundaries
This Pattern reverse-engineers a perspective field from existing image evidence. It does not reconstruct missing geometry when the source has no trustworthy parallel cues, and it does not correct lens or panoramic distortion by itself.

## Notes
Norling turns the usual construction problem around: instead of beginning with vanishing points and drawing the scene, extend the scene's own parallel-direction evidence backward to recover the view that produced it.

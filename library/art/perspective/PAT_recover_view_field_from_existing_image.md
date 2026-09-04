---
object_id: PAT_recover_view_field_from_existing_image
object_type: pattern
name: Recover a Perspective View Field From an Existing Image
library_path:
- art
- perspective
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: none
tags:
- perspective
- vanishing_point
- eye_level
- reference_analysis
cross_links: []
reference:
  source_title: Perspective Made Easy
  author: Ernest R. Norling
confidence: high
references: []
variants:
- variant_id: VAR_recover_station_point_and_viewing_distance
  variant_name: Recover Exact Station Point and Viewing Distance
  variant_basis: method_sequence
  difference_from_foundation: Finalizes exact camera recovery from trustworthy one-, two-, or three-point image geometry when
    the needed world-angle or proportion assumptions are available.
  when_to_use: Use after ordinary vanishing-point/eye-level recovery when exact station geometry materially matters.
  when_not_to_use: Do not claim exact recovery from arbitrary art, distorted/cropped photography, or unknown world geometry.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_capture_reference_against_measured_scene_grid
  variant_name: Capture Reference Against Measured Scene Geometry
  variant_basis: method_sequence
  difference_from_foundation: Builds recoverable perspective and scale cues into newly captured reference by photographing
    or observing the subject against known spatial calibration such as a grid, measured markers, or known-size objects.
  when_to_use: Use when new figure or object reference must later be integrated precisely into a designed scene and relative
    scale, eye level, or perspective relationships would otherwise be difficult to recover.
  when_not_to_use: Do not add calibration overhead when approximate integration is sufficient, the reference is direct observation,
    or trustworthy scene geometry is already available.
  absorbed_from_object_id: none
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

## Notes
Turn the usual construction problem around: instead of beginning with vanishing points and drawing the scene, extend the scene's own parallel-direction evidence backward to recover the view that produced it.

**Boundaries**
This Pattern reverse-engineers a perspective field from existing image evidence. It does not reconstruct missing geometry when the source has no trustworthy parallel cues, and it does not correct lens or panoramic distortion by itself.

Variants retained in this canonical object: `VAR_recover_station_point_and_viewing_distance`, `VAR_loomis_capture_reference_against_measured_scene_grid`.

`VAR_loomis_capture_reference_against_measured_scene_grid` reverses the usual recovery problem when you control reference acquisition: include known spatial calibration in the captured setup so later integration can recover scale, eye level, and scene relationships from evidence rather than guesswork.

---
object_id: PAT_construct_difficult_inbetween_from_basic_shapes_before_details
object_type: pattern
name: Construct Difficult Inbetween From Basic Shapes Before Details
library_path:
- art
- subjects
- animation
- inbetweening
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_build_gesture_into_clear_masses
tags:
- animation
- inbetweening
- construction
- basic_shapes
- continuity
cross_links:
- rel: related_to
  target_object_id: PAT_interpolate_rigid_part_pose_along_motion_path
- rel: related_to
  target_object_id: PAT_synthesize_temporal_movement_into_rhythmic_visual_pattern
reference:
  source_title: Drawn to Life, Volume One
  author: Walt Stanchfield
confidence: high
references: []
variants: []
---

# Construct Difficult Inbetween From Basic Shapes Before Details

## Pattern Rule
**IF** two readable extreme drawings produce an awkward or ambiguous intermediate form that cannot be solved reliably by following finished contours
**THEN** reduce the corresponding endpoint forms to the same simple construction, derive the intermediate state from those underlying masses and attachments, then restore the specific contour and detail onto that solved structure
**ELSE** inbetween directly when the form remains simple, rigid, and unambiguous through the transition

## Do
- Identify the same structural unit at both endpoints before drawing the middle state; a hand, ear, tail, or other part must be treated as one continuing form rather than two unrelated silhouettes.
- Strip surface detail until the endpoint relationship can be represented by a consistent primitive or small mass assembly.
- Solve position, orientation, thickness, and attachment at the construction level before deciding finger shapes, folds, tufts, or other local contour information.
- Reintroduce details only after the intermediate mass reads as a plausible state between the extremes.
- Use the neighboring drawings to preserve continuity of identity and attachment even when no literal live-action pose would match the stylized middle drawing.

## Don't
- Do not average finished outlines when those outlines describe different turns, overlaps, or deformations of the same form.
- Do not invent a new structure in the middle merely because the endpoint details are difficult to reconcile.
- Do not let detail placement determine the mass construction; details must ride on the solved intermediate form.
- Do not force a basic-shape shortcut onto a mechanism whose motion path and orientation can be solved more precisely with explicit rigid-motion geometry.

## Checklist
- The same structural unit can be identified in both extremes and in the inbetween.
- The intermediate construction preserves attachment, approximate thickness, and coherent orientation before details are added.
- Added details conform to the solved mass rather than compensating for a broken underlying structure.
- The middle drawing reads as a transition between the endpoint states rather than as a separately redesigned pose.
- The method is being used because surface interpolation is ambiguous, not merely because primitive construction is familiar.

## Notes
Difficult inbetweens often become easier when the animator stops trying to reconcile finished lines and instead asks what simple form those lines describe. Solving the underlying shape first prevents decorative contour from masking a continuity error. The method is especially useful for organic or deformable character parts; rigid mechanical parts may instead call for an explicitly constructed motion path.

- Construct the inbetween from underlying form, rotation, perspective, and path rather than averaging corresponding outlines or features. Rebuild the intermediate state from the solid form and its intended trajectory.

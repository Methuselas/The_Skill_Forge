---
object_id: PAT_transport_proportional_landmarks_across_views
object_type: pattern
name: Transport Proportional Landmarks Across Views
library_path:
  - art
  - drawing
  - foundations
  - form-construction
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
  - figure_drawing
  - projection
  - proportion
  - foreshortening
cross_links:
  - rel: related_to
    target_object_id: PAT_preserve_articulated_limb_chain
  - rel: related_to
    target_object_id: PAT_validate_foreshortened_limb_reach_from_joint_pivots
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
references: []
variants: []
---

# Transport Proportional Landmarks Across Views

## Pattern Rule
**IF** one subject orientation cannot be placed confidently in depth but a corresponding orientation provides trustworthy proportional information
**THEN** establish corresponding landmarks in whichever view is currently reliable, transport those relationships into the uncertain view, and rebuild the destination subject from known forms; the donor direction may be reversed whenever another corresponding view becomes the better source
**ELSE** construct directly when the target view is already structurally clear

## Do
- Treat the trustworthy donor view as a correspondence template rather than a finished contour to distort; no front, side, back, or other corresponding view is permanently privileged as the source.
- Preserve relative divisions between meaningful landmarks while apparent screen-space distances change.
- Register the pelvis, rib cage, shoulders, major joints, hands or feet, and head landmarks before local anatomy.
- Reconstruct volume at the destination with the established construction rules.
- Use local reach and width checks only where the transported landmark scaffold still leaves a member uncertain.

## Don't
- Assume projection alone constructs the anatomy.
- Copy contour lengths literally from the clear view into the target view.
- Re-measure every body part independently after correspondence has already established its relative position.
- Let a locally attractive limb break the transported landmark relationships.

## Checklist
- Major landmarks keep a coherent relative order between the clear and target views.
- The target pose preserves the intended action and body proportion without copying the source-view silhouette.
- Rebuilt masses turn in the target camera rather than remaining flattened traces of the clear view.
- Local corrections do not contradict the transported whole-subject relationships.

## Notes
The durable move is to solve the relationship wherever it is currently easiest to see and transport only the correspondence needed for the uncertain view. Correspondence is reversible: a side, front, back, or other trustworthy view may donate landmarks to another, but every destination must still be rebuilt as volume rather than copied contour.

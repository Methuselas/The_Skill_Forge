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
variants:
- variant_id: VAR_hogarth_reverse_projection_between_corresponding_views
  variant_name: Reverse Projection Between Corresponding Views
  variant_basis: method_sequence
  difference_from_foundation: Extends the clear-view transport method so correspondence can run backward or sideways between side, front, back, over, or under views when one orientation hides a needed relationship.
  when_to_use: Use when a target view compresses or conceals a relationship that becomes obvious in another corresponding view.
  when_not_to_use: Do not treat any one view as privileged or copy flattened contour; rebuild the recovered relationship as volume in the target camera.
  absorbed_from_object_id: PAT_use_reversible_projection_to_recover_hidden_structure
---

# Transport Proportional Landmarks Across Views

## Pattern Rule
**IF** a difficult subject orientation cannot be placed confidently in depth but the same action can be solved in a clearer view
**THEN** establish corresponding proportional landmarks in the clear view, project those relationships into the target orientation, and rebuild the target subject from known forms
**ELSE** construct directly when the target view is already structurally clear

## Do
- Treat the clearer view as a correspondence template rather than a finished contour to distort.
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
The durable move is to solve the relationship where it is easiest to see and transport only the correspondence needed for the hard view. The clear view is scaffolding, not a second authoritative pose.

`VAR_hogarth_reverse_projection_between_corresponding_views` keeps the Chapter 6 reversible route: side, front, back, and other corresponding views may solve one another, but the recovered target must be rebuilt as volume rather than copied contour.

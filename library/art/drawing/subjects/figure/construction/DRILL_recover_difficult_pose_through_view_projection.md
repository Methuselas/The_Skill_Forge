---
object_id: DRILL_recover_difficult_pose_through_view_projection
object_type: drill
name: Recover a Difficult Pose Through View Projection
library_path:
- art
- drawing
- subjects
- figure
- construction
stage_binding: 2 block
lane_fit: teach
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_transport_proportional_landmarks_across_views
tags:
- figure_drawing
- projection
- foreshortening
- correction
cross_links:
- rel: teaches
  target_object_id: PAT_transport_proportional_landmarks_across_views
- rel: related_to
  target_object_id: DRILL_correct_wonky_foreshortened_limb_with_pivot_arcs
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
target_skill: recover a difficult rotated or foreshortened pose by transporting proportional landmarks from a clearer corresponding view
references: []
variants: []
---

# Recover a Difficult Pose Through View Projection

## Practice Task
Take one pose that repeatedly fails in a difficult rotated or foreshortened view and rebuild it by first solving a clearer corresponding view.

## Target Skill
Transport whole-figure proportional relationships across views without copying the clear view's contour into the target camera.

## Setup
Preserve the intended action and target camera. Leave room beside the failed drawing for one clear side, front, or back construction of the same action.

## Instructions
1. Draw the same action in the clearest useful corresponding view.
2. Mark the pelvis, rib cage, shoulders, major joints, hands or feet, and head landmarks.
3. Carry the corresponding landmark tracks into the target view while keeping the target camera unchanged.
4. Rebuild simple masses at those destinations instead of tracing the source-view silhouette.
5. Apply local reach or width checks only where a projected limb remains uncertain.
6. Remove the correspondence scaffold and compare the recovered pose with the intended action.
7. Redraw the target once more without the clear-view construction if the relationship is now understood.

## Success Check
- The target preserves the intended action and broad proportion.
- Major landmarks agree with the clearer view while their screen-space spacing changes with depth.
- The target volumes belong to the target camera rather than looking like a warped side or front view.
- The pose remains convincing after the projection scaffold is removed.

## Common Failures
- Changing the target camera to match the easy view.
- Copying source-view contour lengths instead of transporting landmark relationships.
- Projecting details before the pelvis, rib cage, shoulders, and major joints are stable.
- Letting a locally attractive limb override the whole-figure correspondence.
- Keeping the scaffolding as visible final structure after the pose is solved.

## Notes
Use this as a correction route when direct invention stalls. The exercise is successful when the hard view can stand on its own after the easy-view template is discarded.

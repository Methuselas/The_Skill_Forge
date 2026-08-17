---
object_id: PAT_interpolate_rigid_part_pose_along_motion_path
object_type: pattern
name: Interpolate a Rigid Part Pose Along Its Motion Path
library_path:
- art
- drawing
- sketching
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- sketching
- product_construction
- articulation
- motion
- mechanism
cross_links:
- rel: related_to
  target_object_id: PAT_construct_only_the_hidden_path_visible_forms_require
reference:
  source_title: 'Sketching: Drawing Techniques for Product Designers'
  author: Koos Eissen and Roselien Steur
confidence: high
references: []
variants: []
---

# Interpolate a Rigid Part Pose Along Its Motion Path

## Pattern Rule
**IF** a rigid lid, cover, door, handle, or similar product part must be drawn in a believable position between two known endpoint poses
**THEN** connect the corresponding endpoint location with its motion path, choose the desired point on that path, and orient the part from the local path direction instead of inventing the intermediate pose independently
**ELSE** construct the pose directly when only one fixed state is needed or the mechanism does not follow a known one-parameter path

## Do
- Draw both endpoint states first so the moving part has a known closed/open or start/end relationship to its parent form.
- Track a corresponding point on the moving part through the motion and connect its endpoint positions with the appropriate curve.
- Choose the intermediate location on that curve before drawing the part at full thickness.
- Use the tangent at the chosen path location to recover the local direction of motion; for the hinged-cover construction, the part thickness lies on the perpendicular direction.
- Keep the hinge or parent attachment consistent while transferring the part into the intermediate state.

## Don't
- Do not draw the middle pose by averaging two silhouettes; the part must remain a rigid object moving through a coherent mechanism.
- Do not change the hinge location, part thickness, or attachment simply because the intermediate silhouette is awkward.
- Do not use a tangent/perpendicular shortcut for a mechanism whose path or orientation relationship is different.

## Checklist
- The endpoint states describe the same rigid part attached to the same parent mechanism.
- The selected intermediate location lies on the motion path established by the endpoints.
- The part keeps consistent thickness and attachment through the transition.
- The intermediate pose reads as one state of the same movement rather than a separately redesigned object.

## Notes
A useful product sketch often needs a mechanism shown somewhere between its obvious endpoint states. The construction is strongest when the endpoints establish the movement first and the intermediate pose is derived from that movement. In the hinged-cover example, the closed and open lid positions define a curved path; a chosen point on that path fixes the cover location, and the local tangent supplies the perpendicular direction used to set its thickness. The transferable idea is to derive an in-between rigid pose from known motion geometry rather than eyeballing a third unrelated state.

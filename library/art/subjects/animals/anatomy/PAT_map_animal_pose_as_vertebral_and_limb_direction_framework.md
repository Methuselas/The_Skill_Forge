---
object_id: PAT_map_animal_pose_as_vertebral_and_limb_direction_framework
object_type: pattern
name: Map an Animal Pose as a Vertebral and Limb-Direction Framework
library_path:
- art
- subjects
- animals
- anatomy
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_construct_animal_form_from_core_masses_framework_and_soft_parts
tags:
- animal_drawing
- animal_anatomy
- structural_framework
- vertebral_column
- limb_directions
- pivot_points
- movement
- whole_skeleton
- structural_hierarchy
- functional_simplification
- optical_weight
cross_links:
- rel: related_to
  target_object_id: PAT_preserve_articulated_limb_chain
- rel: related_to
  target_object_id: PAT_track_animal_motion_through_moving_pivots_and_overlapping_arcs
- rel: related_to
  target_object_id: PAT_block_quadruped_from_dorsal_axis_and_three_body_masses
- rel: prerequisite_for
  target_object_id: PAT_propagate_vertebral_bend_and_twist_through_trunk
- rel: prerequisite_for
  target_object_id: DRILL_trace_animal_vertebral_axis_before_contour
- rel: prerequisite_for
  target_object_id: PAT_read_animal_trunk_muscles_from_spinal_axes_and_levers
- rel: prerequisite_for
  target_object_id: PAT_orient_animal_body_in_depth_with_backline_and_transverse_axes
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants:
- variant_id: VAR_bammes_transition_animal_repose_by_preserving_contacts_and_folding_chains
  variant_name: Transition Animal Repose by Preserving Contacts and Folding Joint Chains
  variant_basis: method_sequence
  difference_from_foundation: 'Adds a repose-transition route to the general animal framework: preserve the contacts that
    remain planted, fold the articulated limb chains instead of shortening them, and let the thoracolumbar spine change with
    the body shift. Bammes distinguishes sitting-on-the-haunches from two routes into lying: from sitting, the hindquarters
    remain folded while the front of the body advances and the forelegs settle from elbow to paw; from standing, the paws
    stay near their contacts while the joints fold and the body slides back into the lowered pose.'
  when_to_use: Use when converting a quadruped from standing into sitting, crouching, or lying and the result looks like a
    standing animal merely squashed downward or with limb lengths changing arbitrarily.
  when_not_to_use: Do not treat Bammes''s dog/cat examples as a universal species sequence. Upright hindquarter sitting, hoofed-animal
    repose, and species-specific folding patterns may use different contacts and joint arrangements; check the animal actually
    being drawn.
  absorbed_from_object_id: none
- variant_id: VAR_bammes_order_whole_trunk_skeleton_by_support_function_and_optical_weight
  variant_name: Order the Whole Trunk Skeleton by Support, Function, and Optical Weight
  variant_basis: method_sequence
  difference_from_foundation: 'Extends the sparse vertebral-and-limb direction framework into a whole-trunk skeleton study
    by asking the artist to work architecturally: keep supporting and supported elements clear in space, vary the optical
    weight and amount of detail by structural importance, preserve the animal''s comparative impression and gesture, and simplify
    skeletal forms until their function and interaction in the working chain remain legible.'
  when_to_use: Use when the main skeletal directions are correct but a fuller trunk-skeleton study is becoming equally detailed,
    diagrammatic, or detached from the animal's gesture and support logic.
  when_not_to_use: Do not turn Bammes's list into one fixed anatomical priority ranking or invent mechanical loads that the
    reference does not support. Optical emphasis, detail, and simplification should follow the animal, pose, and study purpose.
  absorbed_from_object_id: none
---

# Map an Animal Pose as a Vertebral and Limb-Direction Framework

## Pattern Rule
**IF** an animal pose is being copied from contour, mass, or anatomy detail before the main structural directions are secure
**THEN** reduce the pose first to the direction of the vertebral column, the principal limb segments, and the major pivotal points, then let that framework change with the actual movement, support, or body orientation before adding volume
**ELSE** keep the lighter construction already in place when those directions and pivots are unambiguous.

## Do
- Establish the vertebral route as the main directional organizer through the trunk before small anatomical forms are added.
- Place the major shoulder, hip, limb, and other relevant pivots so each limb segment can be traced as one articulated chain from the body to the contact or terminal form.
- Judge the **directions** of the segments before their thickness. A readable skeleton pass can be extremely spare if the spine, joint locations, and changes of angle are correct.
- Redraw the framework when the animal runs, crouches, sits, stretches, or turns upright; the same anatomy must reorganize rather than remain a memorized standing diagram.
- Use representative skeletal examples to locate likely pivots, then correct their exact position and proportion from the animal actually being drawn.

## Don't
- Do not preserve one standing skeleton unchanged and merely bend its silhouette around a new pose.
- Do not let volume or coat hide an uncertain joint direction; solve the framework before relying on the surface.
- Do not treat every visible bend in contour as a skeletal pivot.
- Do not copy a horse pivot map as a literal universal chart for every land mammal; use it only as a representative comparison.

## Checklist
- The vertebral direction can be read without the outer contour.
- Every major limb can be traced through an ordered chain of pivots and segments.
- A change of pose visibly changes the relevant spine and limb directions instead of only changing the silhouette.
- The framework is sparse enough to redraw quickly but specific enough to support later mass and anatomy.
- Species-specific proportion and joint placement can still override the representative model.

## Notes
Treat structural design as a working model that should be understood before it is given graphic expression. Reduce the animal to the directions followed by the vertebral column and limbs, then adapt that framework across movement and pose changes. A representative horse study may mark the principal pivotal points of a land mammal, but it is not a universal template.

This Pattern is a Stage 1 specialization of the broader inside-out animal-anatomy foundation. It does not replace Hultgren's Stage 2 three-mass quadruped block; it supplies the directional skeletal map that can sit underneath such a block when pose mechanics need to be made explicit.

`VAR_bammes_transition_animal_repose_by_preserving_contacts_and_folding_chains` retains **Transition Animal Repose by Preserving Contacts and Folding Joint Chains** as a bounded repose-transition route; use it only under the conditions recorded in the variant metadata.

`VAR_bammes_order_whole_trunk_skeleton_by_support_function_and_optical_weight` retains **Order the Whole Trunk Skeleton by Support, Function, and Optical Weight** as a bounded whole-skeleton study route; use it after the directional framework is established when a more complete trunk skeleton needs structural hierarchy without losing gesture.

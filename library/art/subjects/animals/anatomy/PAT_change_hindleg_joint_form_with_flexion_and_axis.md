---
object_id: PAT_change_hindleg_joint_form_with_flexion_and_axis
object_type: pattern
name: Change Hindleg Joint Form With Flexion and Hinge Axis
library_path:
- art
- subjects
- animals
- anatomy
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_rebuild_animal_limb_joint_form_from_articulation_and_axis
tags:
- animal_drawing
- animal_anatomy
- hindleg
- joint_form
- flexion
- extension
- hinge_axis
- femuro_tibial
- tarsal_joint
- calcaneum
cross_links:
- rel: related_to
  target_object_id: PAT_construct_mammal_hindleg_from_pelvic_anchor_and_joint_chain
- rel: related_to
  target_object_id: PAT_carry_form_flow_through_joint_transitions
- rel: related_to
  target_object_id: PAT_map_animal_pose_as_vertebral_and_limb_direction_framework
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants: []
---

# Change Hindleg Joint Form With Flexion and Hinge Axis

## Pattern Rule
**IF** an animal hindleg joint keeps the same lump or hinge symbol while the limb flexes and extends
**THEN** locate the relevant pivot or cross-axis first, then rebuild the local joint planes and projections for that flexion state instead of rotating an unchanged joint shape between the adjoining segments
**ELSE** keep the joint understated when its axis and state are already clear from the larger limb construction.

## Do
- Treat the pivot axis as the organizer of the local form. In Bammes's runner-hindleg model, hinge-dominant cross-axes make flexion and extension legible before small surface anatomy is added.
- At the femuro-tibial joint, let a relatively extended state read as a broad obtuse meeting with a clear accent around the patellar region; as the joint flexes, allow the meeting to break into more distinct facets as the femoral end rolls relative to the tibia.
- At the tarsal joint, compare the shallow extended angle with the sharper flexed angle. Let the calcaneum change its visible projection with the state of the joint rather than keeping it pasted in one direction.
- Let the visible form change more strongly in profile, where the joint angles declare themselves. In front or rear view, prioritize the joint-axis and support alignment instead of inventing side-view facets that the camera cannot show.
- Keep the surrounding muscle and tendon masses subordinate to the mechanical state until the next anatomy pass; the skeleton and joint orientation must still explain why the contour changes.

## Don't
- Do not draw the femuro-tibial or tarsal region as the same capsule merely rotated between two bones.
- Do not copy Bammes's horse joint silhouette literally onto another species; retain the axis-and-state method while checking the actual anatomy.
- Do not treat every bend in the leg as an identical hinge. The source emphasizes hinge-dominant cross-axes in running forms, not a universal joint model for every animal.
- Do not infer exact surface anatomy from the angle alone when muscle, tendon, species, or viewpoint materially changes what is visible.

## Checklist
- The joint's local planes agree with the amount and direction of flexion.
- The femuro-tibial region does not keep the same contour through extended and strongly flexed poses.
- The tarsal angle and calcaneal projection change together rather than contradicting one another.
- The joint still belongs to one uninterrupted hindleg chain.
- A front or rear view remains structurally coherent without forcing profile-only angular cues into the drawing.

## Notes
On printed p. 51 Bammes explicitly calls out the "plastic effects" of knee mechanics. His sequence shows that a joint is not a fixed connector: an extended femuro-tibial relationship gives a comparatively obtuse accent, while flexion changes the meeting of the forms and can break the region into more facets. He makes the same drawing consequence at the tarsal joint, where a shallower extended angle and a sharper flexed angle alter the visible projection of the calcaneum.

The portable skill is to derive local joint shape from the articulated state and axis instead of from a memorized bump. u16 now confirms that same learner decision in the foreleg, so this card remains the **hindleg specialization** beneath `PAT_rebuild_animal_limb_joint_form_from_articulation_and_axis`, preserving the femuro-tibial, tarsal, and calcaneal cues that the broader owner should not carry.

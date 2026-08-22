---
object_id: PAT_propagate_vertebral_bend_and_twist_through_trunk
object_type: pattern
name: Propagate Vertebral Bend and Twist Through the Trunk
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
foundation_object_id: PAT_map_animal_pose_as_vertebral_and_limb_direction_framework
tags:
- animal_drawing
- animal_anatomy
- vertebral_column
- trunk
- thorax
- spine
- lateral_bend
- torsion
- compression
- extension
- cross_sections
- construction
cross_links:
- rel: related_to
  target_object_id: PAT_construct_animal_form_from_core_masses_framework_and_soft_parts
- rel: related_to
  target_object_id: PAT_block_quadruped_from_dorsal_axis_and_three_body_masses
- rel: related_to
  target_object_id: DRILL_build_animal_form_from_skeletal_landmarks_to_planes
- rel: prerequisite_for
  target_object_id: DRILL_model_animal_trunk_torsion_with_four_sided_block
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants: []
---

# Propagate Vertebral Bend and Twist Through the Trunk

## Pattern Rule
**IF** the vertebral route shows a lateral bend or axial twist but the thorax and surrounding trunk still read as a rigid, symmetrical barrel
**THEN** carry that change through the trunk volume: compress the concave side of a lateral bend, extend the convex side, and progressively turn the trunk's sections around the vertebral route when torsion is present
**ELSE** preserve the more even spacing and section orientation of a near-neutral trunk when the observed spine does not demand deformation.

## Do
- Establish the vertebral direction before deciding how the thorax deforms. The spine is the internal organizer; the visible trunk response follows it.
- In a lateral bend, shorten and crowd the rib/thorax structure on the concave side while allowing the opposite side to lengthen and open. Let the outer convexity become more prominent rather than keeping both sides equally full.
- Use the spacing of spinal landmarks as a diagnostic. On the convex side, lateral/transverse-process relationships can open; on the concave side they compress. Translate that structural change into the visible trunk without drawing every process literally.
- In axial torsion, imagine successive trunk sections rotating around the vertebral route. A rounded four-sided block is a useful temporary model because its planes reveal the changing orientation more clearly than a smooth silhouette.
- Keep the deformation species-specific. The same amount of vertebral change can sit inside very different thorax depth, width, back profile, and soft-tissue mass.

## Don't
- Do not bend or twist only the outer contour while leaving the internal axis and cross-sections unchanged.
- Do not mirror the two sides of the thorax through a lateral bend; equal fullness destroys the compression-versus-extension logic Bammes demonstrates.
- Do not force the dog diagram in fig. 104 onto every mammal as a fixed anatomical template. Use it as a construction model, then check the actual animal.
- Do not carry the temporary four-sided block literally into the final organic contour. Its job is to make the spatial mechanics transparent.
- Do not add detailed ribs or vertebral processes merely to prove anatomy when a few section changes already communicate the same deformation.

## Checklist
- The trunk deformation can be traced back to a clear vertebral bend or twist.
- The concave side of a lateral bend is visibly more compressed than the convex side.
- Cross-sections or implied planes change orientation progressively through a twist instead of remaining parallel.
- The thorax still retains the animal's own depth, width, and back-profile character after deformation.
- Removing surface detail leaves a coherent three-dimensional bend or torsion rather than a flat contour trick.

## Notes
Bammes treats the vertebral column as a form-producing structure rather than a hidden anatomical label. On printed page 100, Figure 104 shows a lateral bend compressing the inward-curving side of the thorax while extending the opposite side; the dog study also spaces the transverse-process relationships more widely on the convex side and more closely on the concave side. On printed pages 98 and 101, he turns the related torsion problem into a simple spatial construction by imagining or physically twisting a rounded four-sided mass.

The Pattern therefore belongs after the Stage 1 vertebral framework has been established. It does not replace the species-specific thorax study that follows in §7.2; it states the deformation logic that a later thorax block must obey when the spine bends or twists.

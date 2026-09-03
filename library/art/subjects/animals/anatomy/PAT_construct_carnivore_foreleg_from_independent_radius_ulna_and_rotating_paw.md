---
object_id: PAT_construct_carnivore_foreleg_from_independent_radius_ulna_and_rotating_paw
object_type: pattern
name: Construct a Carnivore Foreleg From Independent Radius-Ulna Rotation and a Rotating Paw
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
foundation_object_id: PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive
tags:
- animal_drawing
- animal_anatomy
- comparative_anatomy
- carnivore
- cat
- dog
- lion
- foreleg
- radius
- ulna
- pronation
- supination
- carpus
- paw
- joint_axis
cross_links:
- rel: related_to
  target_object_id: PAT_construct_specialized_runner_foreleg_from_mobile_scapula_and_hinge_chain
- rel: related_to
  target_object_id: PAT_rebuild_animal_limb_joint_form_from_articulation_and_axis
- rel: related_to
  target_object_id: PAT_preserve_articulated_limb_chain
- rel: prerequisite_for
  target_object_id: PAT_shape_carnivore_foreleg_from_joint_axes_and_paw_control_muscle_mass
- rel: prerequisite_for
  target_object_id: PAT_construct_carnivore_paw_from_fanned_metacarpals_curved_arch_and_digit_support
- rel: prerequisite_for
  target_object_id: DRILL_study_carnivore_foreleg_across_views_and_rotation_axes
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants:
- variant_id: VAR_bammes_distinguish_cat_and_dog_foreleg_rotation_and_carpus
  variant_name: Distinguish Cat and Dog Foreleg Rotation and Carpal Shape
  variant_basis: context
  difference_from_foundation: 'Calibrates the shared carnivore foreleg construction by degree rather than treating cat and
    dog as one mechanism: Bammes gives cats much more useful pronation/supination, a broader carpus, greater humeral abduction
    for climbing or attack, and a straighter paw direction, while dogs show restricted forearm rotation, a narrower carpus,
    and a slight forward bend after the carpal joint.'
  when_to_use: Use when a cat and dog foreleg are reading too similarly or when the paw turn needs to be propagated through
    the species-appropriate forearm rather than applied at the wrist alone.
  when_not_to_use: Do not turn these comparisons into fixed breed-neutral silhouettes or infer exact ranges of motion from
    the drawings; use observed anatomy and pose to set the degree.
  absorbed_from_object_id: none
---

# Construct a Carnivore Foreleg From Independent Radius-Ulna Rotation and a Rotating Paw

## Pattern Rule
**IF** a cat, dog, lion, or comparable carnivore foreleg is being built with a runner-like fused forearm or with the paw simply swiveled at the wrist
**THEN** keep the radius and ulna as separate working bones, carry paw rotation through their changing relationship around the forearm's longitudinal pivot, and let that rotation reorganize the carpus and distal paw instead of treating the lower limb as one fixed column
**ELSE** use the forelimb specialization appropriate to the animal when the radius-ulna relationship or distal support is mechanically different.

## Do
- Preserve the broad quadruped shoulder-girdle plan through the elbow before emphasizing the carnivore-specific divergence lower down. Bammes treats the shoulder as comparatively conservative and places the crucial change in the separately formed radius and ulna.
- Draw a longitudinal pivot through the forearm and make the radius visibly change position around the ulna as the paw turns. In the pronated support position, the rear surface of the paw faces forward because the turn has already happened through the forearm.
- Keep the paw mechanically tied primarily to the radius. When the paw orientation changes, check that the radius, carpus, and metacarpal mass all agree with that new orientation.
- Compare profile, front, back, and internal views rather than memorizing one silhouette. The crossing relationship can be visually quiet in one view and obvious in another.
- Treat the dog and cat as different degrees of the same broad carnivore solution. Cats in Bammes's comparison retain more useful forearm rotation and a broader carpus; dogs remain more restricted and narrower.
- Let shoulder freedom and distal rotation serve the animal's action. A climbing or striking cat can abduct the humerus and turn the paw in ways a specialized runner construction would not permit.

## Don't
- Do not fuse the radius and ulna into an ungulate-style lower-leg post simply because the foreleg is bearing weight.
- Do not rotate only the paw at the carpus while leaving the radius-ulna relationship unchanged; that produces a wrist swivel without a believable forearm mechanism.
- Do not copy the cat's larger rotational freedom into every dog pose or breed.
- Do not make the carnivore shoulder exotic merely to signal species difference; the stronger structural contrast appears below the elbow in this unit.
- Do not confuse screen-space crossing with two bones literally intersecting. The construction is a three-dimensional change of relation around a pivot axis.

## Checklist
- Radius and ulna remain independently traceable from elbow to carpus.
- The paw turn is carried by a corresponding change in the forearm rather than appearing only at the wrist.
- A pronated planted paw agrees with the orientation of the radius, carpus, and metacarpal mass.
- The same limb can be reconstructed coherently from at least two views without changing its basic segment lengths.
- Cat-versus-dog differences read as calibrated degree and proportion, not as unrelated limb plans.
- The carnivore foreleg is visibly more rotationally capable than the specialized runner route without becoming a human arm pasted onto an animal.

## Notes
Bammes's comparison is useful because it locates the meaningful specialization rather than asking the artist to memorize a complete new limb. The shoulder girdle remains close to the general mammalian plan down to the elbow, while the independently formed radius and ulna create the lower-foreleg freedom that distinguishes carnivores from the fused or reduced forearm of a specialized runner.

The lion study then turns that anatomy into a drawable spatial device: a pivotal axis runs through the forearm while the radius behaves like a wing swiveling around it. That makes pronation and paw orientation an articulated construction problem, not a surface-contour trick. The cat/dog variant keeps Bammes's own degree differences bounded so the shared mechanism is not mistaken for one fixed carnivore template.

`VAR_bammes_distinguish_cat_and_dog_foreleg_rotation_and_carpus` retains **Distinguish Cat and Dog Foreleg Rotation and Carpal Shape** as the bounded cat/dog calibration recorded in the variant metadata.

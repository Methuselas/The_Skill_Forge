---
object_id: PAT_construct_carnivore_paw_from_fanned_metacarpals_curved_arch_and_digit_support
object_type: pattern
name: Construct a Carnivore Paw From Fanned Metacarpals, Curved Arch, and Digit Support
library_path:
- art
- drawing
- subjects
- animals
- anatomy
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_construct_carnivore_foreleg_from_independent_radius_ulna_and_rotating_paw
tags:
- animal_drawing
- animal_anatomy
- carnivore
- cat
- dog
- lion
- paw
- fan
- fanned_metacarpals
- metacarpus
- digits
- claws
- pads
- pollex
- carpus
- skeletal_construction
cross_links:
- rel: related_to
  target_object_id: PAT_rebuild_animal_limb_joint_form_from_articulation_and_axis
- rel: prerequisite_for
  target_object_id: DRILL_study_carnivore_foreleg_across_views_and_rotation_axes
- rel: related_to
  target_object_id: PAT_shape_carnivore_foreleg_from_joint_axes_and_paw_control_muscle_mass
- rel: prerequisite_for
  target_object_id: DRILL_construct_contrasting_big_cat_poses_from_studied_anatomy
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants:
- variant_id: VAR_bammes_calibrate_lion_and_dog_paw_by_metacarpal_length_and_claw_state
  variant_name: Calibrate Lion and Dog Paw by Metacarpal Length and Claw State
  variant_basis: context
  difference_from_foundation: 'Calibrates the shared carnivore paw architecture by species-specific proportion and claw behavior: Bammes contrasts the lion''s short, stubby metacarpal construction and retractable claws with the dog''s longer, more graceful metacarpal construction and non-retractable claws. The fanned, articulated paw principle remains the same; the distal proportions and claw state change.'
  when_to_use: Use when a large-cat paw and a canine paw are reading as the same generic terminal block after the underlying fan, arch, digit support, and forearm relation are already correct.
  when_not_to_use: Do not turn the comparison into a fixed silhouette or force visible claw exposure in every pose; use the actual species, contact, and reference to set digit spread, pad compression, and whether claws are visible.
  absorbed_from_object_id: none
---

# Construct a Carnivore Paw From Fanned Metacarpals, Curved Arch, and Digit Support

## Pattern Rule
**IF** a carnivore paw is collapsing into a flat mitten, a hoof-like terminal block, or a row of digits attached to one straight metacarpal bar
**THEN** build the distal limb as a fanned metacarpal structure with lengthwise and transverse curvature, articulate the digits and claws from that arch, and place the support pads under the distal pressure points instead of flattening the whole paw onto one plane
**ELSE** use the species-specific distal-foot construction when the animal does not have a carnivore-style paw.

## Do
- Establish the metacarpal fan before drawing toe silhouettes. Bammes's forepaw comparison uses five rays and shows the digits diverging from a curved central structure rather than from one straight terminal edge.
- Give the metacarpus curvature in two directions. Its longitudinal bend and transverse arch create a shallow three-dimensional paw volume even before soft tissue is added.
- Place the pollex only where the species and view support it. In Bammes's comparison it sits high on the forepaw and has a functional spreading role in cats rather than acting like a human thumb.
- Articulate each distal digit through its phalanges into the claw. Keep the claw behavior species-specific: the source contrasts retractable feline claws with non-retractable canine ones.
- Put the load-bearing contact beneath the distal metacarpal/digital ends through separate pressure-distributing pads. The paw should therefore show discrete contact architecture rather than one continuous sole.
- Check the digit directions in three-quarter view after the front-view fan is established. This exposes whether the paw actually occupies a curved volume or only looks plausible from one projection.

## Don't
- Do not place the toes as equal parallel sticks under one flat carpal block.
- Do not use the pollex as an opposable human thumb or force it into a ground-contact role in every pose.
- Do not make claws a decorative cap added after the digit chain; their direction must continue the phalangeal construction.
- Do not flatten the support pads into one broad shoe-like base.
- Do not copy feline claw mechanics into a dog or assume every carnivore has identical digit count and proportion.

## Checklist
- The metacarpals visibly fan rather than remaining parallel.
- The paw has both longitudinal bend and transverse arch before fur or pads are modeled.
- Digit directions continue coherently from the metacarpal rays through the phalanges and claws.
- Contact is distributed through distinct distal pads rather than one flat sole.
- The pollex and claw behavior match the species being studied.
- A three-quarter reconstruction preserves the same fan and arch that were established in front view.

## Notes
The useful contrast in Bammes is not simply “paw instead of hoof.” He identifies a different load path and a different spatial organization: multiple metacarpal rays spread from the carpus, the metacarpal region curves as a volume, and the animal bears on padded distal contacts. That combination explains why a carnivore paw cannot be convincingly replaced by either a flat hand symbol or a compact ungulate foot block.

Figure 87 is especially important pedagogically because the foot is isolated after the larger foreleg study. The digit directions and a separate claw detail are treated as construction problems of their own, which supports keeping the paw as a distinct subskill while still attaching it to the carnivore forearm pattern.


`VAR_bammes_calibrate_lion_and_dog_paw_by_metacarpal_length_and_claw_state` preserves Bammes's bounded lion-versus-dog distal calibration without replacing the shared carnivore paw construction.

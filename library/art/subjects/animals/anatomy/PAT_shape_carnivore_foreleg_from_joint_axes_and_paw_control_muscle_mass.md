---
object_id: PAT_shape_carnivore_foreleg_from_joint_axes_and_paw_control_muscle_mass
object_type: pattern
name: Shape a Carnivore Foreleg From Joint Axes and Paw-Control Muscle Mass
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
foundation_object_id: PAT_read_animal_limb_muscle_groups_from_joint_axes_and_lines_of_pull
tags:
- animal_drawing
- animal_anatomy
- carnivore
- cat
- dog
- lion
- foreleg
- musculature
- joint_axis
- flexor
- extensor
- carpus
- digits
- paw_control
cross_links:
- rel: related_to
  target_object_id: PAT_construct_carnivore_foreleg_from_independent_radius_ulna_and_rotating_paw
- rel: related_to
  target_object_id: PAT_construct_carnivore_paw_from_fanned_metacarpals_curved_arch_and_digit_support
- rel: related_to
  target_object_id: PAT_taper_mammal_limb_mass_from_proximal_muscle_to_distal_tendon
- rel: related_to
  target_object_id: PAT_shape_specialized_runner_foreleg_from_functional_muscle_and_skeletal_masses
- rel: prerequisite_for
  target_object_id: DRILL_map_carnivore_forearm_muscle_groups_from_joint_axes_to_pull_bands
- rel: prerequisite_for
  target_object_id: DRILL_construct_contrasting_big_cat_poses_from_studied_anatomy
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants:
- variant_id: VAR_bammes_contrast_lion_compact_foreleg_with_dog_light_foreleg
  variant_name: Contrast the Lion's Compact Foreleg With the Dog's Lighter Foreleg
  variant_basis: context
  difference_from_foundation: 'Calibrates the shared carnivore musculature by overall build: Bammes uses the lion to emphasize
    an athletic, compact shoulder and forearm associated with an ambush hunter, while the dog example is visibly lighter and
    more spare in the foreleg. The functional grouping method stays the same; the relative mass and compactness change.'
  when_to_use: Use when a large cat and a pursuit-built canine are collapsing into the same generic foreleg mass after the
    joint axes and muscle groups are already correct.
  when_not_to_use: Do not treat the lion/dog comparison as a universal predator rule, a breed standard, or a fixed silhouette;
    calibrate the actual animal, sex, age, condition, and pose from reference.
  absorbed_from_object_id: none
---

# Shape a Carnivore Foreleg From Joint Axes and Paw-Control Muscle Mass

## Pattern Rule
**IF** a carnivore foreleg has a correct skeletal chain but its soft form is being modeled like a runner's tendon-dominant lower limb or as generic muscle tubes
**THEN** organize the shoulder, elbow, carpal, and digital muscle groups from their joint axes, retain substantial muscular mass through the forearm for paw control, make the flexor side visibly more powerful than the extensor side when the anatomy supports it, and let the tendons continue into the carpal and digital structure
**ELSE** use the species-specific limb mass hierarchy when the distal limb is more tendinous, more skeletal, or differently specialized.

## Do
- Keep the carnivore skeleton active beneath the muscle map. The independent radius-ulna relation and the actual elbow, carpal, and digital axes determine where the functional groups can travel.
- Around the shoulder and elbow, continue using functional groups rather than starting over with an inventory of named muscles. Bammes's lion plate still deduces action from each group's position relative to the joint axes.
- In the forearm, preserve a stronger soft-tissue envelope than in the specialized runner. The cat-family example keeps enough muscle to operate both the carpus and the digits rather than handing nearly all distal control to long tendons.
- Separate the carpal/digital extensor and flexor masses by the axis they cross. In the source model the extensor group runs on the external/front side of the mechanism while the flexor group occupies the opposing internal/back route and carries greater mass.
- Let the flexor-heavy asymmetry affect the section and silhouette of the forearm. Do not neutralize it into an equal tube merely because the bones are centered.
- Continue the functional groups into their tendon paths and distal attachments so the paw-control mechanism belongs to the same limb construction instead of stopping abruptly at the carpus.

## Don't
- Do not strip a cat or lion lower foreleg down to the horse/cow pattern of long exposed tendons simply because both limbs taper toward the foot.
- Do not rotate or reposition the radius and ulna for the skeleton, then drape the same fixed muscle sleeve over every orientation; the muscle masses must follow the changed three-dimensional forearm.
- Do not make flexors and extensors equal in volume when the studied carnivore shows the stronger flexion group emphasized by Bammes.
- Do not convert the labeled lion or dog plate into a memorization test for individual muscle names. The reusable construction decision is the functional arrangement, mass hierarchy, and route to the paw.
- Do not infer exact muscle size or action from the source's simplified plates when the intended species or pose differs; use the live/reference anatomy to set the final amount.

## Checklist
- The shoulder and forearm masses can still be traced back to the carnivore skeletal axes and radius-ulna construction.
- Carpal and digital control is carried by readable muscle-and-tendon routes rather than by a runner-like bare distal post.
- The flexor and extensor sides are distinguishable in placement and relative mass instead of forming a symmetrical sleeve.
- Tendon paths continue coherently toward the metacarpal and digital structures rather than terminating at an arbitrary wrist line.
- A dog can be made lighter and a lion more compact without changing the underlying functional grouping method.
- The completed foreleg can be simplified back to skeleton, axes, and a few functional muscle bands without losing the pose.

## Notes
The carnivore treatment deliberately reuses the joint-axis logic already established for other mammal limbs, but its plastic conclusion is different from the runner. The cat family's varied use of the paw requires a much more muscular lower foreleg, and Bammes explicitly states that the flexion group is the heavier of the two major forearm systems. That makes this a carnivore-specific soft-form specialization rather than another generic muscle-reading card.

The lion/dog comparison is retained only as a calibration variant. It changes the amount and compactness of the visible mass while keeping the same functional method. A further reduction strips the forearm down into front/back pull bands and an origin-to-insertion abstraction, which is practiced separately in `DRILL_map_carnivore_forearm_muscle_groups_from_joint_axes_to_pull_bands`.

`VAR_bammes_contrast_lion_compact_foreleg_with_dog_light_foreleg` preserves that bounded lion/dog mass calibration without turning either example into a universal carnivore template.

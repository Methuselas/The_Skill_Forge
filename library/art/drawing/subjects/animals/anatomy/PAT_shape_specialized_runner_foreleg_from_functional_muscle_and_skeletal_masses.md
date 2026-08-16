---
object_id: PAT_shape_specialized_runner_foreleg_from_functional_muscle_and_skeletal_masses
object_type: pattern
name: Shape a Specialized Runner Foreleg From Functional Muscle and Skeletal Masses
library_path:
- art
- drawing
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
- specialized_runner
- horse
- ungulate
- foreleg
- musculature
- joint_axes
- scapula
- tendon
- skeletal_landmarks
- hard_soft_rhythm
- cow
- ruminant
- broad_carpus
cross_links:
- rel: related_to
  target_object_id: PAT_construct_specialized_runner_foreleg_from_mobile_scapula_and_hinge_chain
- rel: related_to
  target_object_id: PAT_taper_mammal_limb_mass_from_proximal_muscle_to_distal_tendon
- rel: related_to
  target_object_id: PAT_rebuild_animal_limb_joint_form_from_articulation_and_axis
- rel: related_to
  target_object_id: DRILL_build_animal_form_from_skeletal_landmarks_to_planes
- rel: prerequisite_for
  target_object_id: DRILL_construct_complete_runner_foreleg_from_architectural_masses_and_sections
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants:
- variant_id: VAR_bammes_shape_ruminant_foreleg_with_angular_masses_and_broad_carpus
  variant_name: Shape a Ruminant Foreleg With Angular Masses and a Broad Carpus
  variant_basis: context
  difference_from_foundation: 'Adapts the horse-oriented runner mass hierarchy to Bammes''s cow comparison: keep the limb structurally spare, but make the prominent muscle-and-bone forms harder and more angular, broaden the carpal mass strongly, and emphasize the bend above and below the carpus rather than smoothing the chain into the horse''s comparatively straighter rhythm.'
  when_to_use: Use when translating a horse-based ungulate foreleg construction toward a cow or comparable ruminant whose visible carpal width and angular breaks are actually present in the reference.
  when_not_to_use: Do not turn every ruminant into one fixed cow template, and do not infer exact joint proportions or soft-tissue distribution from this comparative example alone.
  absorbed_from_object_id: none
---

# Shape a Specialized Runner Foreleg From Functional Muscle and Skeletal Masses

## Pattern Rule
**IF** the skeletal chain of a horse or comparable ungulate runner foreleg is correct but the living form is being wrapped in uniform tubes or generic muscle bulges
**THEN** build the proximal foreleg from functional muscle groups around the shoulder and elbow axes, keep the profile comparatively deep while the front view stays laterally compressed, and alternate muscular zones with increasingly skeletal-and-tendinous zones toward the carpus and distal support
**ELSE** use the forelimb musculature appropriate to a carnivore, primate, or other animal whose shoulder, forearm, and distal functions are organized differently.

## Do
- Preserve the scapula as a flat triangular attachment on the side of the thorax while layering the surrounding shoulder masses. The living form should not erase the mobile blade established in the runner skeleton.
- Around the shoulder and elbow, group the large soft forms by their relationship to the joint axes before naming individual muscles. Bammes's profile construction places flexor and extensor masses in a strong front-to-back sequence.
- Use the view to control the apparent section. In profile, the layered muscle groups create substantial depth from front to back; in a front view, the same foreleg is much more compressed from side to side.
- In the lower runner foreleg, let soft tissue become selective rather than symmetrical. In Bammes's horse model the muscular covering is concentrated toward the front and outer side while the inner side reads more spare and structurally exposed; verify the actual animal instead of treating that distribution as a universal mammal rule.
- From around the carpal region downward, let long tendons and skeletal landmarks increasingly govern the modeling. Keep the distal limb alive and connected, but do not refill it with proximal muscle volume.
- In a living-animal study, look for an alternating rhythm of muscular fullness and harder skeletal/tendinous accents rather than one uninterrupted fleshy contour.

## Don't
- Do not wrap the entire foreleg in an equal-width muscular sleeve after solving the skeleton.
- Do not symmetrize the lower leg by adding matching muscle mass to both sides merely because the front view is narrow.
- Do not let shoulder musculature hide the scapular orientation or detach the foreleg from the thoracic suspension system.
- Do not copy the horse's exact soft-tissue distribution into cats, dogs, apes, or other forelimbs with greater rotational freedom and different distal function.
- Do not draw every individual muscle complex when the functional mass rhythm and hard/soft alternation already explain the form.

## Checklist
- The scapular plate remains traceable beneath the living shoulder mass.
- The profile foreleg has more front-to-back depth than the front view suggests side-to-side width.
- Proximal muscle groups and distal tendons/skeletal landmarks form a clear hierarchy rather than equal-volume tubes.
- Hard and soft masses alternate coherently down the limb without breaking the articulated chain.
- The result still reads as a specialized runner foreleg before coat, veins, or small anatomical detail are added.

## Notes
Figure 70 reduces the horse foreleg to joint axes plus functional muscle groups specifically so the artist can understand its **shape rhythm** without studying every muscle in isolation. Bammes then states the plastic consequences: the front/back layering creates a deep profile mass, the front view is laterally flattened, lower-limb muscle coverage is selective, and skeletal modeling becomes dominant near and below the carpus as long tendons take over.

Figure 71 begins translating that analysis into a living foreleg. The scapula stays visible as a flat triangular attachment at the side of the thorax, while the free limb is read through alternating muscular and skeletal masses. Section 6.3 completes that practical route in `DRILL_construct_complete_runner_foreleg_from_architectural_masses_and_sections`, so this Pattern remains the mass-shaping decision while the Drill owns the full study sequence.

`VAR_bammes_shape_ruminant_foreleg_with_angular_masses_and_broad_carpus` adds Bammes's cow comparison from §6.3. Use it when the actual ruminant reference shows the harder angular masses, markedly broad carpus, and stronger bend around that joint; it is a contextual modification of the runner construction, not a universal ruminant anatomy formula.

---
object_id: PAT_distinguish_quadruped_forequarter_suspension_from_hindquarter_drive
object_type: pattern
name: Distinguish Quadruped Forequarter Suspension From Hindquarter Drive
library_path:
- art
- drawing
- subjects
- animals
- construction
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: PAT_construct_animal_form_from_core_masses_framework_and_soft_parts
tags:
- animal_drawing
- animal_anatomy
- quadruped
- comparative_anatomy
- shoulder_girdle
- pelvic_girdle
- scapula
- thorax
- forelimb
- hindlimb
- muscular_sling
- support
- propulsion
cross_links:
- rel: related_to
  target_object_id: PAT_map_animal_pose_as_vertebral_and_limb_direction_framework
- rel: related_to
  target_object_id: PAT_construct_horse_skeleton_from_spine_ribcage_and_girdles
- rel: related_to
  target_object_id: PAT_design_pose_against_center_of_gravity
- rel: prerequisite_for
  target_object_id: PAT_construct_specialized_runner_foreleg_from_mobile_scapula_and_hinge_chain
- rel: prerequisite_for
  target_object_id: PAT_construct_carnivore_foreleg_from_independent_radius_ulna_and_rotating_paw
reference:
  source_id: gottfried_bammes_artist_guide_to_animal_anatomy
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
  publish_date: '2004'
  media_type: PDF
  locator: u03, printed pp. 11-13; physical pp. 9-11
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Distinguish Quadruped Forequarter Suspension From Hindquarter Drive

## Pattern Rule
**IF** a terrestrial quadruped's front and rear limb attachments are being constructed as mirror-equivalent supports
**THEN** separate their structural jobs: treat the thorax at the forequarter as suspended between the scapular/forelimb supports by a muscular sling, while the hindlimbs transmit through the femur and pelvis into the vertebral column; use the resulting difference in support geometry and joint angulation to organize the drawing
**ELSE** use the species-specific attachment and support system when the animal departs from this mammalian quadruped model.

## Do
- Place the scapula as part of a shoulder-girdle support system around the thorax rather than inventing a direct bony socket that fixes the forelimb to the rib cage.
- Let the forelimb read comparatively as a load-bearing support chain whose major directions carry the suspended trunk toward the ground.
- Trace the hindlimb through its direct skeletal relationship with the pelvis, then follow the angular joint chain that can straighten as the animal pushes or lifts.
- Use scapular and pelvic direction as structural clues connecting the limbs back into the trunk instead of treating the legs as appendages pasted onto body masses.
- Compare the source's support-versus-drive model to the actual animal, pose, and gait phase before deciding how strongly either role should dominate.

## Don't
- Do not attach the front of a quadruped to the thorax as though the shoulder girdle were simply a smaller version of the pelvic socket.
- Do not make the fore- and hindlimb chains mechanically identical merely because both reach the ground.
- Do not hard-code Bammes's stated two-thirds-front / one-third-rear weight split as a universal ratio for every species, individual, or pose.
- Do not universalize the horse-specific tendon and elbow-locking examples to all quadrupeds.
- Do not interpret "support" and "drive" as exclusive functions; Bammes presents them as dominant structural emphases in his representative model.

## Checklist
- The forequarter attachment can be explained through scapular placement and suspension of the thorax rather than a fictional bone-to-bone chest socket.
- The hindquarter attachment can be traced through femur, pelvis, and trunk as one skeletal route.
- Front and rear limb geometry are differentiated by their structural emphasis instead of mirrored by habit.
- The support model still agrees with the animal and pose being observed.
- Exact weight ratios or horse-specific locking mechanisms are not required for the Pattern to work.

## Notes
Bammes describes the mammalian trunk with a bridge analogy: the vertebral column spans between front and rear supports, but those supports are not constructed in the same way. The thorax is shown suspended between the forelimbs by flexible muscle straps associated with the scapula, while the hindlimb is linked through the pelvis and uses a more strongly angled chain for push-off. His diagrams on printed pp. 12-13 make this contrast visually explicit.

The source also assigns a fixed front/rear weight ratio and discusses horse-specific energy-saving joint mechanisms. Those details are retained as source context, not as universal runtime doctrine. The reusable drawing decision is the **difference in attachment and mechanical emphasis** between forequarter and hindquarter.

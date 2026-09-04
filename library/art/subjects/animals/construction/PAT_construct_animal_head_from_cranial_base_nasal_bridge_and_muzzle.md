---
object_id: PAT_construct_animal_head_from_cranial_base_nasal_bridge_and_muzzle
object_type: pattern
name: Construct an Animal Head From Cranial Base, Nasal Bridge, and Muzzle
library_path:
- art
- subjects
- animals
- construction
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animal_drawing
- animal_head
- head_construction
- muzzle
cross_links: []
reference:
  source_title: The Art of Animal Drawing
  author: Ken Hultgren
confidence: high
references: []
variants:
- variant_id: VAR_hultgren_place_horse_eye_from_skull_sections
  variant_name: Place the Horse Eye From Skull Sections and Bone Flow
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Hultgren''s horse-specific placement correction to the serial head block: divide the long
    head before details, read the pronounced bony route beneath and behind the eye toward the ear, and use those skull sections
    to prevent the eye from drifting too far forward as the head turns.'
  when_to_use: Use when a horse head has the correct muzzle length but the eye/ear relationship still looks humanized, front-heavy,
    or unstable across perspective.
  when_not_to_use: Do not convert the source's study divisions into fixed universal measurements for every horse or angle;
    the actual skull, individual, and viewpoint still control placement.
  absorbed_from_object_id: none
- variant_id: VAR_hultgren_construct_gorilla_face_from_cheekbone_eye_and_nostril_landmarks
  variant_name: Construct a Gorilla Face From Cheekbone, Deep-Eye, and Broad-Nostril Landmarks
  variant_basis: context
  difference_from_foundation: 'Adds Hultgren''s gorilla-specific landmark emphasis after the compact cranial/facial block:
    keep the cheekbones pronounced, set the eyes deep and inset beneath a low forehead, and make the nostril region broad,
    using the head centerline to keep those bilateral landmarks attached through the turn.'
  when_to_use: Use when a gorilla head has a plausible generic muzzle but still reads too human, too flat around the eyes,
    or insufficiently broad through the central face.
  when_not_to_use: Do not treat Hultgren's listed traits as exact measurements or as a complete gorilla taxonomy; age, individual
    structure, viewpoint, and the actual reference still control the block.
  absorbed_from_object_id: none
---

# Construct an Animal Head From Cranial Base, Nasal Bridge, and Muzzle

## Pattern Rule
**IF** a mammal head has a projecting nose or muzzle whose length and turn are not explained clearly by a compact cranial-ball-and-facial-wedge block
**THEN** separate the head into a rear cranial/base mass, a nasal-bridge or long-nose section, and a terminal muzzle mass along one centerline before attaching ears and placing the major facial landmarks
**ELSE** keep the simpler two-mass head construction when it already explains the subject's volume and viewpoint.

## Do
- Carry one construction centerline from the cranial/base region through the nose to the muzzle so all three sections turn together.
- Establish the muzzle as a volume with its own end plane rather than as a flat extension of the face.
- Attach the ears to the rear head region with simple bases before refining their outer shapes.
- Use eye, ear, and nostril alignment as a working comparative guide, then adjust it to the actual animal or reference instead of treating the broad guide as universal.
- Observe whether the eyes sit more laterally or more forward on the particular animal and let that placement follow the constructed head.

## Don't
- Compress a long animal muzzle into a human-like facial wedge merely to reuse familiar proportions.
- Place eyes, nostrils, and ears as independent symbols after the head has already turned.
- Force one eye-ear-nostril alignment onto a species or individual that visibly contradicts it.
- Float ears on top of the silhouette without a readable attachment to the rear head mass.

## Checklist
- The cranial base, nasal length, and muzzle read as one turned head rather than three disconnected shapes.
- The centerline reaches the muzzle and agrees with its end-plane orientation.
- Ear roots and major facial landmarks remain attached to the same construction when the head is rotated.
- The block preserves the subject's characteristic head length instead of drifting toward human proportions.

## Notes
Hultgren explicitly divides the skull into the muzzle, the long part of the nose, and the base of the skull, then adds a central construction division and rear ear attachments. He also offers broad eye/ear/nostril and eye-position guides. Those latter statements are retained here only as bounded observation aids: the durable skill is serial head construction, while actual landmark placement remains subject-specific.

`VAR_hultgren_place_horse_eye_from_skull_sections` retains **Place the Horse Eye From Skull Sections and Bone Flow** as a horse-specific placement check: use skull divisions and the bony route around the eye when the eye drifts forward, but do not promote those study divisions into fixed measurements.

`VAR_hultgren_construct_gorilla_face_from_cheekbone_eye_and_nostril_landmarks` adds the gorilla transfer: after the compact head is turned as one mass, use pronounced cheekbones, deep inset eyes, a low forehead, and a broad nostril region to keep the face species-specific. These are Hultgren's drawing landmarks for the illustrated gorillas, not fixed biometric measurements.

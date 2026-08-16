---
object_id: PAT_preserve_articulated_limb_chain
object_type: pattern
name: Preserve One Continuous Joint Chain per Limb
library_path:
- art
- drawing
- foundations
- form-construction
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- figure_drawing
- limb_construction
- joint_chain
- error_prevention
cross_links:
- rel: supports
  target_object_id: PAT_build_gesture_into_clear_masses
reference:
  source_title: Dynamic Figure Drawing
  author: Burne Hogarth
confidence: high
references: []
variants:
- variant_id: VAR_bridgman_forearm_rotation_radius_around_ulna
  variant_name: Carry Hand Rotation Through Radius Crossing Around the Ulna
  variant_basis: method_sequence
  difference_from_foundation: 'Deepens the existing limb-chain rotation rule with a specific forearm model: keep the ulna as the elbow-to-little-finger-side hinge/hub while the radius carries the wrist and hand around it, so pronation/supination changes the forearm''s internal crossing and surface mass directions rather than swiveling the hand at the wrist.'
  when_to_use: Use when a turned palm or thumb direction does not convincingly propagate through the forearm, especially in pronated/supinated views.
  when_not_to_use: Do not draw the two bones literally through the skin or treat the ulna as perfectly fixed in every pose; use the model to preserve believable rotational continuity.
  absorbed_from_object_id: none
- variant_id: VAR_hampton_layer_arm_gesture_bone_direction_volume_and_anatomy
  variant_name: Layer Arm Gesture, Bone Direction, Volume, Then Anatomy
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Hampton''s arm-specific sequencing to the articulated limb chain: begin with the lyrical arm gesture, lay a straighter directional line over it to clarify bone placement and 2-D segment position, build the perspective cylinders, then place asymmetrical anatomical shapes over those volumes.'
  when_to_use: Use when an arm has energy but weak mechanics, or has solid cylinders but lost gesture; the layered sequence lets the artist separate action, structural direction, volume, and anatomy without asking one line to do all jobs at once.
  when_not_to_use: Do not treat the straight bone-direction line as the final contour or erase the original gesture's intent; each later layer must refine rather than replace the earlier one.
  absorbed_from_object_id: none
- variant_id: VAR_bammes_twist_forearm_as_quadrangular_prism
  variant_name: Twist the Forearm as a Quadrangular Prism
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Bammes''s drawable abstraction to the existing radius-around-ulna rotation model: temporarily compress radius and ulna into one twist-capable four-sided forearm form. In supination the form remains comparatively open and untwisted; during pronation the carrying structure develops a propeller-like torsion, so the hand turn is visible through the forearm''s planes rather than appearing as a wrist swivel.'
  when_to_use: Use when Bridgman's two-bone explanation is understood but the forearm is still hard to orient quickly in perspective, especially between full supination and full pronation.
  when_not_to_use: Do not draw a literal twisted box through the finished arm or replace the actual radius-ulna relationship with a single rigid prism; the four-sided form is a temporary construction aid for orientation.
  absorbed_from_object_id: none
- variant_id: VAR_zarins_track_pronation_by_section_change_and_ulnar_rail
  variant_name: Track Pronation by Section Change and the Ulnar Rail
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Zarins''s sculptural surface proof to the existing radius-around-ulna and twist-prism models: pronation/supination should change the forearm''s cross-sectional read and the distribution of flexor/extensor masses, not merely rotate a texture map around one tube. Zarins visualizes a relatively rounder/open supinated section becoming flatter and redistributed through pronation, while the subcutaneous ulna remains a useful elbow-to-little-finger-side surface rail that can read as a ridge or furrow.'
  when_to_use: Use when the palm direction is mechanically correct but the forearm still looks like the same cylinder in every rotation, or when the surface masses lose their orientation between elbow and wrist.
  when_not_to_use: Do not force one exact round-versus-flat cross-section onto every arm, body type, or viewpoint, and do not require the ulnar rail to be equally visible everywhere. Shoulder rotation may add to a forced turn, but it must not substitute for the actual forearm rotation when pronation/supination is the action being constructed.
  absorbed_from_object_id: none
---

# Preserve One Continuous Joint Chain per Limb

## Pattern Rule
**IF** an arm, leg, wing, fin, or invented appendage is being laid onto the framework
**THEN** establish one uninterrupted chain from its parent socket through every joint to its terminal form, preserving segment identity and mechanically continuous rotation
**ELSE** redraw the chain before adding volume where overlap makes its path uncertain

## Do
- Mark the high rotational attachment, the main bending joint, the tapered wrist or ankle, and the terminal form before contouring the member.
- Trace each chain through hidden overlaps so a crossing never becomes a new joint or a limb exchange.
- Carry inward or outward terminal rotation through the forearm or lower leg rather than swiveling only the hand or foot.

## Don't
- Duplicate a member because an exploratory line was mistaken for a second limb.
- Let two chains share an elbow or knee at an overlap.
- Rotate the hand or foot in a direction the carrying segment does not support.

## Checklist
- Every visible segment can be traced back to exactly one parent socket.
- The number and order of joints are unchanged through overlap and foreshortening.
- Terminal direction agrees with the rotation of the preceding segment.

## Notes
Hogarth begins arms and legs as corresponding two-part column systems with high swivel joints, middle bends, and terminal members. The construction generalizes to wings, fins, tails, tentacles, and mechanical appendages as long as their actual joint sequence is preserved.

`VAR_bridgman_forearm_rotation_radius_around_ulna` retains **Carry Hand Rotation Through Radius Crossing Around the Ulna** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_hampton_layer_arm_gesture_bone_direction_volume_and_anatomy` retains **Layer Arm Gesture, Bone Direction, Volume, Then Anatomy** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_bammes_twist_forearm_as_quadrangular_prism` retains **Twist the Forearm as a Quadrangular Prism** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

`VAR_zarins_track_pronation_by_section_change_and_ulnar_rail` retains **Track Pronation by Section Change and the Ulnar Rail** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

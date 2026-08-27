---
object_id: PAT_validate_human_limb_joint_mechanics_from_anatomical_surfaces
object_type: pattern
name: Validate Human Limb Joint Mechanics From Anatomical Surfaces
library_path:
- art
- subjects
- figure
- anatomy
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- figure_drawing
- joint_mechanics
- knee
- elbow
- wrist
- ankle
- anatomy_validation
cross_links:
- rel: related_to
  target_object_id: PAT_carry_form_flow_through_joint_transitions
- rel: related_to
  target_object_id: PAT_preserve_articulated_limb_chain
- rel: related_to
  target_object_id: AP_audit_articulated_limb_identity_and_joint_mechanics
reference:
  source_title: PASS Art canonical anatomy synthesis plus guided limb-mechanics failure repair
  author: Multiple accepted sources + MaDin + GPT
confidence: high
references:
- image_path: library/art/subjects/figure/anatomy/assets/limb-mechanics/negative/blu_corkscrew_bullet_dodge_reversed_left_leg.png
  caption: 'NEGATIVE / FAILURE EVIDENCE: the left lower leg emerges with a reversed knee relationship despite otherwise persuasive rendering and attachment continuity. Judge the joint from anatomical front/back surfaces and segment relationships, not from screen direction or polish.'
  derived_from: live Work render reviewed during the 2026-08-24 limb-mechanics repair
  origin: first_party_source
  review: passed
variants: []
---

# Validate Human Limb Joint Mechanics From Anatomical Surfaces

## Pattern Rule
**IF** a materially visible ordinary human or humanlike limb joint is bent, twisted, foreshortened, crossed, or otherwise at risk of reading as a reversed or impossible hinge
**THEN** identify the joint's anatomical front/back surfaces and adjoining segment axes, then verify that flexion, rotation, and endpoint direction remain mechanically coherent regardless of camera angle
**ELSE** keep the mechanics check lightweight when the joint is near-straight, clearly oriented, and structurally unambiguous

## Do
- At the knee, identify the femur/thigh direction, patellar or anterior plane, posterior knee hollow, tibial/lower-leg axis, ankle, and foot as one relationship. Flexion brings the posterior calf toward the posterior thigh; the lower leg must not emerge through the patellar/anterior face as though the hinge were reversed.
- Allow near-straight extension and limited rotation around a bent knee, but require the patella, tibial axis, ankle, and foot to remain one coherent leg rather than using twist to conceal a reversal.
- At the elbow, use the olecranon/posterior relationship and the opposing anterior closing side to keep the hinge readable. Flexion closes the forearm toward the upper arm on the anterior side even when pronation or supination changes the hand orientation.
- Let forearm pronation/supination rotate the wrist and hand through the forearm structure without reversing the elbow hinge or detaching the terminal direction from the carrying segment.
- At wrist and ankle transitions, check that the terminal member can be reached by the carrying segment and that local flexion/rotation does not function as an impossible swivel that masks a reversed upstream joint.
- Classify the observed range as `ordinary`, `extreme_but_plausible`, or `impossible` from relational mechanics rather than treating one exact degree limit as universal.

## Don't
- Infer knee or elbow facing from whether the limb points left, right, up, or down on the image; screen direction changes with camera and pose while anatomical surfaces do not exchange identities.
- Accept a polished contour, armor plate, costume seam, or shadow as proof of joint legality when the underlying femur/tibia or humerus/forearm relationship contradicts it.
- Use pronation, supination, tibial rotation, or terminal wrist/ankle motion to justify a chain whose primary hinge has reversed.
- Reject an extreme action merely because it is unusual when the anatomical surfaces and segment relationships still support the motion.

## Checklist
- Knee flexion preserves a coherent anterior patellar side and posterior closing side; no lower leg exits through the front of the joint as a backward hinge.
- Elbow flexion preserves a coherent posterior olecranon side and anterior closing relationship despite forearm rotation.
- Wrist/hand and ankle/foot direction remain attainable from the carrying forearm or lower leg without a hidden identity swap.
- The joint can be classified as ordinary or extreme-but-plausible; an impossible or visually indeterminate terminal-resolution relationship fails.
- Camera angle, overlap, costume, and rendering do not replace the anatomical evidence used to determine the joint's actual mechanics.

## Notes
The useful test is relational rather than degree-based. Human joints have individual variation and action poses can push toward the edge of ordinary range, but the underlying front/back surfaces, segment order, and hinge relationships remain coherent. This rule does not define nonhuman or deliberately altered joint architectures; those require their own established body-plan mechanics rather than an automatic human correction.

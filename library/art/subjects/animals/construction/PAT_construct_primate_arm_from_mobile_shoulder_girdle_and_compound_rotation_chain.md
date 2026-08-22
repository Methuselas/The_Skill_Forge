---
object_id: PAT_construct_primate_arm_from_mobile_shoulder_girdle_and_compound_rotation_chain
object_type: pattern
name: Construct a Primate Arm From a Mobile Shoulder Girdle and Compound Rotation Chain
library_path:
- art
- subjects
- animals
- construction
stage_binding: 1 skeleton
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: domain
foundation_object_id: none
tags:
- animal_drawing
- animal_anatomy
- comparative_anatomy
- primate
- ape
- gorilla
- forelimb
- shoulder_girdle
- clavicle
- scapula
- radius
- ulna
- pronation
- supination
- wrist
- hand
- thumb
- joint_axis
cross_links:
- rel: prerequisite_for
  target_object_id: DRILL_map_primate_arm_mobility_from_girdle_to_hand_axes
- rel: related_to
  target_object_id: PAT_integrate_shoulder_mass_with_rib_cage
- rel: related_to
  target_object_id: PAT_construct_carnivore_foreleg_from_independent_radius_ulna_and_rotating_paw
- rel: related_to
  target_object_id: PAT_orient_thumb_by_opposition_and_rotation
- rel: related_to
  target_object_id: PAT_construct_gorilla_from_barrel_torso_long_arms_and_compact_lower_body
reference:
  source_title: The Artist's Guide to Animal Anatomy
  author: Gottfried Bammes
confidence: high
references: []
variants: []
---

# Construct a Primate Arm From a Mobile Shoulder Girdle and Compound Rotation Chain

## Pattern Rule
**IF** a primate forelimb is being built like a quadruped foreleg with one shoulder pivot and a paw-like terminal block
**THEN** construct the arm as a coordinated mobility chain beginning with the two-part scapula-clavicle girdle, continuing through multi-axis shoulder motion, elbow flexion, radius-ulna rotation, and wrist deviation, and ending in a hand whose thumb can oppose independently moving fingers
**ELSE** use the limb architecture appropriate to the animal when a clavicle-braced shoulder and opposable hand are not part of its construction.

## Do
- Place the clavicle as a brace that holds the arm away from the thorax instead of letting the shoulder collapse directly against the rib cage. Let the scapula and clavicle act together as the moving base of the free arm.
- Keep the shoulder joint capable of changing the humerus in more than one plane: forward/back swing, sideward adduction-abduction, and inward-outward rotation all belong to the proximal construction.
- Treat elbow bending and forearm turning as different mechanisms. The elbow supplies the main flexion-extension cross-axis while the radius turns around the ulna through the proximal and distal radio-ulnar joints.
- Propagate pronation or supination through the whole forearm. A crossed radius is evidence that the hand's facing changed upstream, not that the wrist alone swiveled.
- Give the wrist its own two-direction mobility. Flexion-extension and deviation toward the thumb or little-finger side can redirect the hand after the forearm has already turned.
- Finish the chain with a hand rather than a paw. Preserve the thumb as an independently mobile opposing branch and allow the fingers to organize their own positions around the intended grip or reach.

## Don't
- Do not attach the humerus directly to a fixed torso point and then ask the elbow and wrist to supply the full reach of the arm.
- Do not collapse shoulder rotation, elbow flexion, radio-ulnar turning, and wrist deviation into one generic bend; each change occurs at a different part of the chain and affects the downstream hand differently.
- Do not turn a primate hand by rotating only the carpus while leaving the radius and ulna in an unchanged parallel relationship.
- Do not import the carnivore paw rule at the distal end. Shared radius-ulna rotation does not make the primate forelimb a cat foreleg with longer digits.
- Do not assume the human and ape shoulder sit on identical thorax shapes or scapular locations; use the species block to set the girdle's placement and breadth.

## Checklist
- The arm can be traced from thorax through scapula and clavicle before it reaches the shoulder joint.
- A hand-facing change can be explained by the radius-ulna relationship rather than by a wrist-only twist.
- Shoulder, elbow, radio-ulnar, and wrist axes do different jobs instead of collapsing into one hinge symbol.
- The clavicle visibly preserves space between the thorax and free arm when the pose requires reach, hanging, or swing.
- The terminal form reads as a hand with independent thumb/finger organization, not as a paw block with human digits attached.

## Notes
Bammes uses the ape to show that primate manual versatility is not produced by the hand alone. The useful drawing decision is to distribute mobility across the whole forelimb: a scapula-clavicle base, a multi-axis shoulder, a hinge-dominant elbow, paired radio-ulnar turning, a two-direction wrist, and an opposable hand. Figure 99 makes that hierarchy explicit by drawing a total arm turning axis beside the individual joint axes and by isolating the radius's turn at both radio-ulnar joints.

This route is related to the existing human shoulder-girdle and thumb-opposition Patterns, but it is not a duplicate of either. Those owners explain local figure-drawing decisions; this card preserves Bammes's comparative-anatomy instruction that a primate arm should be constructed as one compound mobility system from girdle to hand. It is also related to the carnivore radius-ulna Pattern, while deliberately keeping the primate clavicle, wrist freedom, and hand endpoint distinct.

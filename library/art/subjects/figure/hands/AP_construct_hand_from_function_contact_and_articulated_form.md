---
object_id: AP_construct_hand_from_function_contact_and_articulated_form
object_type: ap
name: Construct a Hand From Function, Contact, and Articulated Form
library_path:
- art
- subjects
- figure
- hands
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_construct_hand_from_palm_wedge_and_digit_chain
tags:
- hand
- construction
- gesture
- grip
- contact
- articulation
cross_links:
- rel: supports
  target_object_id: PAT_configure_hand_around_function_contact_and_load
- rel: supports
  target_object_id: PAT_orient_thumb_by_opposition_and_rotation
- rel: supports
  target_object_id: PAT_sequence_finger_flexion_as_a_coupled_spiral
- rel: supports
  target_object_id: PAT_unify_finger_chains_with_knuckle_shank_rhythm
- rel: supports
  target_object_id: PAT_design_hand_gesture_through_configuration_and_attitude
- rel: supports
  target_object_id: PAT_reveal_hand_structure_through_surface_stress
- rel: related_to
  target_object_id: AP_prepare_construction_for_rendering
reference:
  source_title: PASS Art canonical synthesis
  author: Multiple accepted hand-drawing sources
confidence: high
references: []
variants: []
---

# Construct a Hand From Function, Contact, and Articulated Form

## Objective
Construct a hand whose whole orientation, palm/digit anatomy, articulation, thumb opposition, contact, load, and expressive gesture agree strongly enough to survive the removal of surface detail and hand off to rendering.

## Steps / Flow
1. **Establish what the hand is doing before posing the digits.** Classify the job—grasp, support, push, brace, point, pinch, rest, manipulate a tool, communicate, or another concrete action. For a rigid object/tool, establish the object's axis, diameter/contour, contact surfaces, and intended operation first so the hand solves around real constraints.
2. **Establish the whole hand before five fingers.** Choose palm facing, wrist direction, the broad tapered hand envelope, finger-group direction, and the hand's relationship to the forearm. The action should already read at this coarse level.
3. **Build the palm and wrist connection.** Use `PAT_construct_hand_from_palm_wedge_and_digit_chain` to establish palm depth/scoop, root placements, and continuity into the wrist. Do not let later finger posing flatten or detach the palm.
4. **Establish thumb opposition and the digit fan.** Use `PAT_orient_thumb_by_opposition_and_rotation`; let the long fingers inherit their bases and spread/gather from the palm instead of attaching independently in screen space.
5. **Articulate the digit chains for the required action.** Preserve continuous roots and joint sequences. When several fingers close together, use `PAT_sequence_finger_flexion_as_a_coupled_spiral` or the relevant variant rather than treating four digits as identical hinges.
6. **Pass the contact/load gate.** For a hand touching, carrying, bracing against, or manipulating something, invoke `PAT_configure_hand_around_function_contact_and_load` and verify the complete chain: object/support → palm orientation → thumb opposition → active digits → support digits → palm contact → wrist → forearm. A visually attractive hand fails if the contact or force path is impossible.
7. **Pass the gesture gate when the hand communicates.** Use `PAT_design_hand_gesture_through_configuration_and_attitude` to strengthen attitude, projection, tension, or clarity without invalidating the mechanics beneath it.
8. **Restore digit unity after articulation is correct.** If the fingers read as tubes, beads, or disconnected segments, invoke `PAT_unify_finger_chains_with_knuckle_shank_rhythm`. Rhythm integrates the established joint chain; it may not replace it.
9. **Add surface evidence only from structural causes.** Use `PAT_reveal_hand_structure_through_surface_stress` for creases, tendons, pads, compression, stretch, and bony cues where the pose/contact/load actually produces them. Age-specific treatment enters only when the intended hand requires it.
10. **Pass the stripped-hand gate.** Ignore nails, wrinkles, tendons, rendering, and small contour accents. Verify one coherent palm, five traceable digit roots, credible thumb opposition, continuous joint chains, believable wrist/forearm attachment, the intended action, and actual contact where required.
11. **Rollback to the earliest failed dependency.** A bad grip returns to function/contact; a detached digit returns to its root/articulation; a wrong thumb returns to opposition; a gesture that breaks the mechanics returns beneath gesture. Do not repair structural failures with surface anatomy.
12. **Hand off only after the action survives reduction.** Delegate to `AP_prepare_construction_for_rendering` when the hand remains structurally and functionally readable without decorative surface information.

## Notes
Persistent invariants are **FUNCTION**, **CHAIN**, **OPPOSITION**, **CONTACT**, and **WHOLE**. The hand is one articulated mechanism serving an action; every digit remains connected through a continuous route; the thumb participates through opposition rather than behaving as finger five; visible contact agrees with the external object/support; and local finger sophistication may not destroy the broad hand read.

This AP is deliberately more than a palm-construction wrapper. Its orchestration value is the dependency order and the function/contact gate: plausible finger anatomy is insufficient when the completed hand cannot actually perform the stated action.

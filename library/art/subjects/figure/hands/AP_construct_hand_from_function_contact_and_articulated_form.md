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
Construct a hand whose expected character-specific topology, whole orientation, palm/digit anatomy, digit identity, articulation, opposable-digit behavior where applicable, combined mechanical attainability, contact, load, and expressive gesture agree strongly enough to survive the removal of surface detail and hand off to rendering.

## Steps / Flow
1. **Establish what the hand is doing before posing the digits.** Classify the job—grasp, support, push, brace, point, pinch, rest, manipulate a tool, communicate, or another concrete action. For a rigid object/tool, establish the object's axis, diameter/contour, contact surfaces, and intended operation first so the hand solves around real constraints.
2. **Resolve the expected hand topology before digit construction.** Prefer, in order, explicit prompt/specification, authoritative visual reference, and established character/design continuity. Record the required digit branches and any nonstandard joint/segment structure before drawing them. If none of those establishes a different anatomy and the subject is otherwise humanlike, use a humanlike fallback of four long fingers plus one thumb. The fallback is not a universal humanoid law and must never override known nonhuman, stylized, altered-digit, or altered-joint anatomy.
3. **Establish the whole hand before individual digits.** Choose palm facing, wrist direction, the broad tapered hand envelope, the main digit-group direction, and the hand's relationship to the forearm. The action should already read at this coarse level.
4. **Build the palm and wrist connection.** Use `PAT_construct_hand_from_palm_wedge_and_digit_chain` to establish palm depth/scoop, the topology-appropriate root map, and continuity into the wrist. Do not let later finger posing flatten or detach the palm.
5. **Map every required digit root before local posing hides it.** Each expected digit branch gets one unique anatomical root. No required root may be empty, no two chains may share one invented root, and no extra branch may be added simply because an overlap or silhouette seems to need it. For the humanlike fallback, this means four long-finger roots on the finger side and one distinct thumb root on the thenar/thumb side.
6. **Depth-order overlapping digits and construct them one complete chain at a time.** When foreshortening, folding, or overlap creates ambiguity, use `VAR_training_construct_overlapping_digits_deepest_to_nearest` under `PAT_construct_hand_from_palm_wedge_and_digit_chain`: identify the most obscured required digit, construct it fully from root through joints to tip, then add progressively nearer required digits one by one. Count completed chains against the expected topology as you go. Hidden construction may be rejected by overlap only after the underlying chain exists; visibility may hide anatomy but may not create or delete it.
7. **Construct the thumb or other mechanically distinct opposable branch as its own pass when the established topology includes one.** Use `PAT_orient_thumb_by_opposition_and_rotation` for a humanlike thumb. Do not let a long finger substitute for the thumb, duplicate the thumb branch, or force human thumb mechanics onto a character whose established anatomy differs.
8. **Articulate the digit chains for the required action.** Preserve continuous roots and joint sequences through overlap or occlusion. When several humanlike long fingers close together, use `PAT_sequence_finger_flexion_as_a_coupled_spiral` or the relevant variant rather than treating them as identical hinges. A folded digit may disappear behind nearer forms, but it may not penetrate the palm mass, detach from its root, or lose its distal identity merely because the contour is compressed.
9. **Pass the topology audit before surface rendering.** Reconstruct the hand from palm outward, not from the finished silhouette inward. Confirm that the number, identity, roots, segment/joint structure, and continuous root-to-tip paths of all digit branches match the established topology exactly. A plausible count of visible protrusions is insufficient if one branch is duplicated, hidden, detached, or mis-rooted.
10. **Pass the whole-hand mechanical-attainability gate.** After the individual chains look plausible, judge the palm, digit group, opposable branch where present, wrist, and intended action as one articulated mechanism. Check that neighboring digit flexion, relative fingertip placement, crossings in depth, opposable-digit travel, and wrist state can coexist without contradictory construction or an obviously strained/dislocated read. Do not canonize one unusual configuration as forbidden merely because it is uncommon; reject the drawing only when the complete mechanism does not cohere.
11. **Pass the contact/load gate.** For a hand touching, carrying, bracing against, or manipulating something, invoke `PAT_configure_hand_around_function_contact_and_load` and verify the complete chain: object/support → palm orientation → topology-appropriate opposable digit or stabilizer behavior → active digits → support digits → palm contact → wrist → forearm. A visually attractive hand fails if the contact or force path is impossible.
12. **Pass the gesture gate when the hand communicates.** Use `PAT_design_hand_gesture_through_configuration_and_attitude` to strengthen attitude, projection, tension, or clarity without invalidating the mechanics beneath it.
13. **Restore digit unity after articulation is correct.** If the fingers read as tubes, beads, or disconnected segments, invoke `PAT_unify_finger_chains_with_knuckle_shank_rhythm`. Rhythm integrates the established joint chain; it may not replace it.
14. **Add surface evidence only from structural causes.** Use `PAT_reveal_hand_structure_through_surface_stress` for creases, tendons, pads, compression, stretch, and bony cues where the pose/contact/load actually produces them. Age-specific treatment enters only when the intended hand requires it.
15. **Pass the stripped-hand gate.** Ignore wrinkles, tendons, rendering, and small contour accents. Verify one coherent palm; an exact match to the established hand topology; unique valid roots; continuous joint chains through overlap; topology-appropriate opposable-digit behavior; believable wrist/forearm attachment; a mechanically attainable complete configuration; the intended action; and actual contact where required. For the humanlike fallback, the topology check is exactly four traceable long-finger chains plus one traceable thumb branch. Use a visible nail/distal plane as an orientation cue when it materially resolves a digit's facing, but do not require decorative nail detail when orientation is already clear.
16. **Rollback to the earliest failed dependency.** A bad grip returns to function/contact; a duplicated, missing, or extra digit returns to expected topology/root mapping; a detached digit returns to its root/articulation; a wrong humanlike thumb returns to opposition; an impossible combined pose returns to the earliest conflicting chain or wrist decision; a gesture that breaks the mechanics returns beneath gesture. Do not repair structural failures with surface anatomy.
17. **Hand off only after structure survives both reduction and finish-risk review.** Delegate to `AP_prepare_construction_for_rendering` when the hand remains structurally and functionally readable without decorative surface information. During later rendering, preserve the accepted topology, digit count, identity, articulation, and orientation: value or edge treatment may clarify those relationships but may not invent a joint, erase a digit, fuse a digit into the palm, expose a rejected hidden construction line as a new digit, or manufacture a new thumb-like branch.

## Notes
Persistent invariants are **TOPOLOGY**, **ROOT**, **CHAIN**, **FUNCTION**, **OPPOSITION/ROLE**, **ATTAINABILITY**, **CONTACT**, and **WHOLE**. The hand is one articulated mechanism serving an action. Character-specific anatomy outranks defaults; when no anatomy is specified or recoverable for an otherwise humanlike subject, a four-long-fingers-plus-one-thumb structure is only a fallback. Every required digit remains connected through a continuous route even when occluded, and no extra chain may be invented after the expected topology is complete. For humanlike hands, the thumb participates through opposition rather than behaving as finger five. The complete digit/palm/wrist configuration must cohere mechanically, visible contact must agree with the external object/support, and local finger sophistication may not destroy the broad hand read.

This AP is deliberately more than a palm-construction wrapper. Its orchestration value is the dependency order: resolve topology and roots before articulation, construct hidden overlapping chains before nearer ones when needed, then pass mechanical and contact gates before rendering. Plausible finger-shaped contours are insufficient when the anatomical graph underneath cannot be traced.

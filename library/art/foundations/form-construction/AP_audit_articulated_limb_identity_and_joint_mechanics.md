---
object_id: AP_audit_articulated_limb_identity_and_joint_mechanics
object_type: ap
name: Audit Articulated Limb Identity and Joint Mechanics
library_path:
- art
- foundations
- form-construction
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- limb_chain
- topology
- joint_mechanics
- error_prevention
- figure_drawing
- creature_drawing
cross_links:
- rel: supports
  target_object_id: PAT_preserve_articulated_limb_chain
- rel: supports
  target_object_id: PAT_validate_human_limb_joint_mechanics_from_anatomical_surfaces
- rel: related_to
  target_object_id: PAT_carry_form_flow_through_joint_transitions
- rel: related_to
  target_object_id: AP_develop_figure_anatomy_from_structural_landmarks_to_living_surface
reference:
  source_title: Guided articulated-limb identity and joint-mechanics repair
  author: MaDin + GPT
confidence: high
references: []
variants: []
---

# Audit Articulated Limb Identity and Joint Mechanics

## Objective
Verify that every materially represented articulated limb follows the established body plan as one uniquely identified chain from the correct parent origin through ordered joints to the correct endpoint, and that visible joint mechanics remain plausible at the current drawing resolution before the artifact is accepted.

## Steps / Flow
1. **Resolve the expected body plan before judging the artifact.** Establish the number and identity of the limb chains required by the subject from explicit specification, authoritative reference, accepted construction, or stable character continuity. Do not assume a two-arm/two-leg human plan when the subject establishes another topology. If authoritative sources disagree about limb count, origin, endpoint type, or joint sequence, fail closed until the conflict is resolved.
2. **Name each chain independently of screen position.** Give every chain a stable anatomical or body-plan identity and record its current screen location separately. Apply `PAT_preserve_articulated_limb_chain` so a left/right, anterior/posterior, numbered, or otherwise canonical limb identity cannot silently change merely because the pose crosses the body or reverses its screen-side position.
3. **At Stage 1, audit typed scaffold identity only.** Trace parent origin → major joint(s) → terminal block for each represented chain. Confirm that no endpoint belongs to two chains, no chain changes role through overlap, and the terminal block has the expected endpoint type. Do not demand finished joint surfaces or digit topology at skeleton resolution.
4. **At Stage 2, audit mass-chain continuity and major joint facing.** Follow each root through the blocked limb masses and confirm that the ordered segment/joint sequence survives foreshortening, overlap, and camera rotation. Major elbows and knees must already face consistently enough that Stage 3 will not need to reverse a hinge or exchange a limb identity.
5. **At Stage 3, Stage 4, and Direct Render, perform the full root-to-endpoint audit.** Inspect the complete frame and every materially visible limb risk region at local/enlarged scale. Trace each observed chain from its declared origin through every visible or structurally established joint to its endpoint, compare expected and observed origin/endpoint types, and verify that the chain order never changes through occlusion or foreshortening.
6. **Apply body-plan-specific mechanics where an owner exists.** For ordinary human anatomy, apply `PAT_validate_human_limb_joint_mechanics_from_anatomical_surfaces` to visible elbow, knee, wrist, and ankle relationships. For a nonhuman or invented body plan, use the established mechanics of that body plan rather than importing human hinge assumptions. If the required mechanics are not established strongly enough to judge a materially visible joint, leave the audit unresolved rather than inventing a rule.
7. **Classify joint range without pretending one universal degree table exists.** Record each audited joint relationship as `ordinary`, `extreme_but_plausible`, or `impossible`. Dynamic action may legitimately occupy the second class; the third class fails regardless of dramatic intent.
8. **Handle occlusion without manufacturing anatomy.** A truly hidden joint may remain visually hidden when its structural route is already established by the surrounding chain. Do not expose or invent a landmark merely for verification. A materially visible joint whose flexion plane, segment order, or endpoint identity remains ambiguous at terminal resolution does not pass.
9. **Rollback the whole affected chain on identity or mechanics failure.** An endpoint substitution, chain exchange, reversed hinge, duplicated joint, or mechanically impossible visible relationship invalidates that limb chain. Return to the nearest skeletal or major-mass construction and rebuild parent origin → segments → joints → endpoint. Do not cosmetically repaint only the hand, foot, elbow, or knee.
10. **Re-audit every materially represented chain after correction.** Native regeneration or editing can disturb limbs that were not targeted. Completion requires a fresh whole-figure inventory, one evidence record per audited limb chain, matching expected/observed endpoint identity, and no unresolved or impossible mechanics state.

## Notes
The protocol is count-neutral. A human may establish four primary limb chains; a six-legged creature, multi-armed character, winged animal, or mechanical design may establish a different set. The controlling truth is the declared body plan, not a hardcoded human count.

This audit is deliberately separate from detailed hand topology. A correctly typed arm may still contain a malformed hand, and a perfectly counted hand does not prove that the arm belongs to the correct shoulder or that its elbow bends legally.

---
object_id: AP_gate_staged_visual_work_by_approval
object_type: ap
name: Gate Staged Visual Work by Approval
library_path:
- art
- drawing
- process
- staged-drawing
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: PAT_return_to_art_centerline
tags:
- approval_gate
- staged_visual_work
- iteration
- drift_prevention
cross_links:
- rel: related_to
  target_object_id: AP_draw_a_figure_through_onion_skinned_stages
- rel: related_to
  target_object_id: PAT_calibrate_stage_information_density_against_precedent
- rel: related_to
  target_object_id: PAT_explore_stage0_with_thumbnail_set
- rel: related_to
  target_object_id: PAT_preserve_structure_during_stage4_amplification
- rel: related_to
  target_object_id: PAT_choose_stage1_construction_by_readability
- rel: related_to
  target_object_id: PAT_block_complete_stage2_inventory
- rel: related_to
  target_object_id: PAT_commit_stage3_form_realization
reference:
  source_title: Guided Stage 1–3 Artist Discretion, Mass Completion, and Commitment Review
  author: MaDin + GPT
confidence: high
references: []
variants: []
---

# Gate Staged Visual Work by Approval

## Objective
Prevent surprise, downstream effort, and visual drift by making each stage's purpose explicit, inspecting the actual artifact and its parentage, recording an allowed user decision, and refusing to advance until the current stage has proved the information needed by the next one.

## Steps / Flow
1. **Resolve delivery intent and Stage 0 density.** For an open-ended request, default to Stage 0A unless the user explicitly requests Stage 0B or Stage 0C.
2. **Set expectations before Stage 0.** Explain that the first artifact is an approval thumbnail or reference used to establish the picture rather than the final result.
3. **Generate one Stage 0 ideation artifact and inspect it.** When composition is open, use one contact sheet of four meaningfully different candidates at the selected profile. Preserve prompt inventory and story while searching viewpoint, crop, placement, gesture, focal hierarchy, broad light, and value design. Withhold near-duplicates or profile violations.
4. **Present the Stage 0 gate and stop.** Candidate selection alone does not authorize Stage 1. Explicit `advance` freezes camera, framing, composition, story, broad value pattern, and general light direction.
5. **Record an explicit gate action.** Accept `advance`, `refine`, `alternate`, or `return`. Praise plus correction resolves to `refine`. A successor stage may authorize only from recorded `advance`.
6. **Stage 1 gate — readable construction.** The artist may block, scribble, or combine methods. Inspect whether the complete positional plan, important hidden paths, principal subject structure, horizon when useful, contacts, perspective relationships, and figure order are clear enough to build Stage 2 without guessing. Do not reject a useful construction merely because it is heavier than a sparse diagram.
7. **Stage 2 gate — complete minimum mass.** Inspect whether every element intended for Stage 3 is already present at minimum block level and whether the Stage 1 anchors, proportions, perspective, overlaps, and negative spaces survive. Reject lighting, texture, atmosphere, or decorative rendering except a necessary structural accent.
8. **Stage 3 gate — serious form realization and commitment.** Require the exact approved Stage 2 artifact as the registered edit parent. Inspect specific forms, contours, detail hierarchy, lighting direction, shadow pattern, and thumbnail continuity. Rich rendering cannot compensate for a changed scene, action, camera, inventory, or composition.
9. **Stage 4 gate — final presentation.** Verify that finishing, color, materials, atmosphere, texture, effects, and edge control amplify the approved Stage 3 rather than redesign it.
10. **End every presented stage with a visible gate.** Name the stage, what it proves, what approval freezes, and the allowed actions. Stop after the gate.
11. **Route changes to their owning stage.** `refine` stays at the current stage, `alternate` creates a substantially different same-stage solution, and `return` moves to the earliest stage that owns the requested change. Never conceal an earlier violation downstream.
12. **Preserve accepted artifacts and decisions.** Store the artifact reference, actual parent reference, freeze record, profile, inspection result, gate prompt, and chosen action. Later work must not infer approval from momentum or conversational tone.

## Notes
Use these core prompts:

- **Stage 0 — Thumbnail:** “Which direction should become active? Should we refine it, approve and advance, or try another direction?”
- **Stage 1 — Readable construction:** “Can you read the complete plan well enough to build Stage 2 without guessing, or should this construction be refined?”
- **Stage 2 — Complete mass block:** “Does every intended Stage 3 element exist at minimum solid form with the approved layout intact, or should the block-in be refined?”
- **Stage 3 — Form realization and commitment:** “Does this serious drawing preserve the thumbnail and Stage 2 parent while establishing specific forms, detail hierarchy, lighting, and shadow strongly enough to commit to Stage 4?”
- **Stage 4 — Final render:** “Does the finish amplify the approved Stage 3 without changing its commitments, or should the final be refined?”

Stage 3 is the baking phase. Stage 4 is icing and decoration. A weak or drifted Stage 3 must be repaired before finishing.

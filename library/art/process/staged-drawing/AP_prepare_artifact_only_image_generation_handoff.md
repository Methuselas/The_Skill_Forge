---
object_id: AP_prepare_artifact_only_image_generation_handoff
object_type: ap
name: Prepare Artifact-Only Image Generation Handoff
library_path:
- art
- process
- staged-drawing
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: tool
foundation_object_id: AP_progress_artifact_through_ratified_steps
tags:
- image_generation
- prompt_isolation
- artifact_contract
- information_ceiling
- workflow_suppression
cross_links:
- rel: supports
  target_object_id: AP_gate_staged_visual_work_by_approval
- rel: related_to
  target_object_id: AP_run_stage0_rough_composition_search
- rel: related_to
  target_object_id: AP_build_stage1_scene_skeleton
- rel: related_to
  target_object_id: AP_build_stage2_complete_mass_block
- rel: related_to
  target_object_id: AP_realize_stage3_rough_image
- rel: related_to
  target_object_id: AP_finish_stage4_as_finished_pencils
reference:
  source_title: Guided Native Image-Generation Handoff Debugging
  author: MaDin + GPT
confidence: high
references: []
variants: []
---

# Prepare Artifact-Only Image Generation Handoff

## Objective
Translate the currently authorized Art operation into a single observable image task before invoking native image generation, so process/controller language stays on the PASS side and the generator is oriented toward only the artifact that should visibly exist now.

## Steps / Flow
1. **Resolve the legal artifact internally first.** Use the staged controller and the current Art AP to determine the one artifact authorized by the user. Do not let the image generator decide what the workflow means.
2. **Pass any required exact-source accessibility gate before compiling a successor handoff.** When the authorized operation must develop or locally edit an accepted predecessor, confirm that the exact canonical predecessor is actually exposed to the native image tool as an edit/reference source. Knowing which artifact is canonical is not enough. If exact access is unavailable, fail closed and recover/request a re-upload of that same artifact; do not compile a fresh-generation substitute from prose, an earlier stage, a rejected artifact, or a near-match. A user re-upload restores access to the same predecessor and lockset without new approval.
3. **Separate orchestration language from visual language.** Terms used to manage the workflow—numbered stages, staged production, Search/Control, approval, ratification, rollback, successor steps, development sequence, or similar process language—remain internal. Do not repeat them in a pre-generation explanation or turn them into visual subject matter.
4. **Compile an artifact-only contract.** Carry only: artifact form, properties that must remain fixed, visible information required now, the visual vocabulary allowed now, visible information to withhold, layout constraints, stage-appropriate identity cues, and the stopping condition.
5. **Use the current Art AP's Productive Image Contract.** Preserve its substance while omitting workflow labels. The image-facing intent should describe what is on the page, not where that page sits in a larger progression.
6. **Keep layout positive and singular.** Other than composition Search, ask for one primary artifact only. For open composition Search, prefer several separate candidate image outputs when the host supports them; otherwise use one neutral sheet containing candidates only. Do not request explanatory sidebars, instructional examples, alternate finish states, auxiliary reference panels, a chosen panel, or a surrounding presentation-board design.
7. **Withhold known information deliberately.** Knowing a character, costume, environment, material, or lighting plan does not authorize showing all of it. Express only the identity or design cues needed at the current visual resolution. Suppressed information remains authoritative for later work without becoming visible early.
8. **Keep supplied character identity closed while creative action stays open.** The generator may invent pose, camera, crop, staging, and other currently open variables, but it may not redesign an established character. At low-information artifacts, preserve identity through proportion and silhouette-scale anchors instead of surface detail.
9. **Do not echo contaminated workflow wording immediately before generation.** If the user said “staged composition” or similar, interpret it internally and then speak only in artifact terms. When no clarification is needed, invoke image generation directly rather than narrating the workflow first.
10. **Preserve one-attempt authority and current-resolution repair.** One authorized attempt produces only the current artifact class (a composition Search request may return several candidate images). If the result is rejected, the next request stays at that same information ceiling and addresses the rejected decision; do not convert “try again” into more rendering, a later-resolution artifact, or a fresh final illustration.
11. **Treat violations as invalid lineage, not successful progress.** If a surfaced artifact contains unauthorized auxiliary panels, later-resolution information, character redesign, or another ceiling violation, do not ratify or carry it forward. The host may surface generation immediately, so this gate protects progression even when it cannot hide a bad render from the user.

## Notes
This AP is an image-generation handoff discipline, not a runtime and not a claim that PASS can intercept or rewrite the native generator's hidden prompt. Its purpose is to keep the assistant from *adding* avoidable workflow contamination at the last conversational boundary it does control.

The compact rules are: **PASS may think in stages; the image generator should receive only the picture that is allowed to exist now** and **loss of edit-target access does not authorize visual reinterpretation.**

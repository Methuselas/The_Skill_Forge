---
object_id: AP_gate_staged_visual_work_by_approval
object_type: ap
name: Gate Staged Visual Work by Approval
library_path:
- art
- process
- staged-drawing
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: AP_progress_artifact_through_ratified_steps
tags:
- approval_gate
- staged_visual_work
- iteration
- drift_prevention
cross_links:
- rel: related_to
  target_object_id: PAT_develop_scene_through_registered_successors
- rel: related_to
  target_object_id: PAT_return_to_art_centerline
- rel: related_to
  target_object_id: AP_alternate_search_and_control_cycles
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
- rel: related_to
  target_object_id: AP_prepare_artifact_only_image_generation_handoff
reference:
  source_title: Guided Stage Revision Debugging and Stage Mechanics Review
  author: MaDin + GPT
confidence: high
references: []
variants: []
---

# Gate Staged Visual Work by Approval

## Objective
Run explicit visual staged production as an approval-gated Art implementation of `AP_progress_artifact_through_ratified_steps`, delegating the actual artistic work to one current-stage AP at a time so creative invention remains broad where legal and cannot silently create approval, future-stage content, or downstream redesign.

## Steps / Flow
1. **Enter visible staged mode as a hard route when requested.** An explicit mode directive such as `Mode: staged`, or equivalent clear intent, makes ordinary direct-render routing illegal until the user explicitly exits staged mode or the staged thread completes. Do not merely acknowledge the mode in prose; the next productive Art call must enter this controller before any native image-generation call.
2. **Use the metaskill controller, not one monolithic art prompt.** `AP_progress_artifact_through_ratified_steps` owns progression, ratification, revision classification, Search/Control, and rollback. This AP supplies the universal Drawing thread: Stage 0 `AP_run_stage0_rough_composition_search` → Stage 1 `AP_build_stage1_scene_skeleton` → Stage 2 `AP_build_stage2_complete_mass_block` → Stage 3 `AP_realize_stage3_rough_image` → Stage 4 `AP_finish_stage4_as_finished_pencils`. Ink, Color, Paint, Manga/B&W finish, and other medium-specific workflows are downstream APs, not extra permissions inside Drawing Stage 4.
3. **Determine the only legal current stage before producing.** No approved Stage 0 root means only Stage 0 is legal. An approved Stage 0 permits Stage 1; an approved Stage 1 permits Stage 2; and so on. A rejection leaves the highest approved stage unchanged and authorizes only another revision/search at the same candidate stage.
4. **Require approval provenance from the user.** In interactive staged production, assistant evaluation, recommendation, ranking, praise, silence, partial positive feedback, or revision instructions never count as user approval. Only an unambiguous user-originated selection/approval can ratify the current stage and authorize advancement.
5. **Make Stage 0 selection a destructive state transition.** At the active composition-selection gate, a bare selection such as `2`, `Use 2`, or `I like 2` promotes that actual visible candidate to the sole canonical Stage 0 root. Composition Search closes immediately; unselected candidates lose productive authority. Do not redraw, re-highlight, compare, or regenerate the candidate set unless the user explicitly reopens composition Search. The next legal productive image is one Stage 1 successor derived from the selected root.
6. **Interpret contextual continuation as commit/freeze/advance-one.** At an active later approval gate, an unqualified `Continue` means approve the current actual image, freeze all decisions owned up through that stage, and authorize exactly one successor artifact. `Commit and Continue` is the explicit PASS form of the same transition. Do not pass `Continue` to image generation as an open-ended creative instruction, and never let one approval unlock multiple future stages.
7. **Retire rejected candidate families honestly.** A candidate or candidate set rejected by the user cannot become a root or later anchor through assistant inference. Local correction preserves a viable current-stage direction; broad rejection retires the failed search space and reopens Search with the critique carried forward. Only the user may explicitly resurrect a rejected option.
8. **Route rejection before generating again.** Classify whether the user rejected local structure, pose/action family, composition/camera, current information density, canon/reference fidelity, or an upstream commitment. Rejection keeps the same legal stage unless the defect is explicitly owned earlier. A rejected early artifact never authorizes a more developed substitute. Preserve rejection constraints in conversation so the next Search cannot return as a cosmetic variant of the same family.
9. **Load only the current Art AP, then hand off artifact-only.** The controller may know the whole thread, but immediately before native image generation invoke `AP_prepare_artifact_only_image_generation_handoff`. Do not restate numbered stages, staged-production terminology, Search/Control, approval logic, future steps, or the user's workflow wording in the productive pre-generation context. The generator should be oriented only toward the one artifact that is allowed to exist now.
10. **Use honest conversational revision labels.** Label each actual visible attempt `S0-r1`, `S0-r2`, `S1-r1`, and so on when useful. `APPROVED` means the user explicitly approved that actual image in the conversation. Labels coordinate discussion; they are not filenames, runtime IDs, hashes, or claims of tool lineage.
11. **Carry registered visual authorities and locksets after Stage 0, then verify exact-source access.** Apply `PAT_develop_scene_through_registered_successors`. The approved Stage 0 image guards picture identity; every approval adds the decisions owned by that stage to the inherited lockset; and the latest approved artifact is the required productive predecessor for the next operation. For any operation that requires edit/reference continuity, confirm that this **exact canonical artifact is actually accessible to the native image tool**. Canonical identity alone is not sufficient. If access is missing, fail closed and recover/request a re-upload of the exact artifact; a re-upload restores the same canonical predecessor and lockset without new approval. Register continuity for all important scene objects, not only figures.
12. **Generate one current artifact class per authorized attempt.** Open composition Search may return four to six separate candidate images from one request when the host supports multiple outputs, or one neutral candidate-only contact sheet otherwise; every later artifact is one full-frame image. Never turn the workflow itself into a visual deliverable unless the user explicitly asks for a multi-step presentation board.
13. **Inspect the returned artifact against the current AP.** Check stage purity and picture identity immediately. If the host permits private candidate inspection before surfacing, use it; if the host displays generation immediately, mark a violating artifact invalid, do not approve/anchor it, and retry or rollback. Never pretend an invalid image was legitimate merely because it is attractive.
14. **Apply Search and Control at the right ownership level.** Stage 0 permits broad pictorial Search. Once Stage 0 is approved, composition Search closes; Stage 1 Controls that picture while solving structure. Later stages may search within their unresolved form/detail responsibilities but may not reopen properties owned upstream without rollback.
15. **Gate, prompt, and stop after each visible valid candidate.** Explicitly state the legal next actions in conversational artifact terms. If the host forbids text after an image tool result, state the bounded next-action prompt immediately before generation without using workflow vocabulary—for example, “I’ll show six composition sketches; after they appear, pick a number, give revisions, or reject the set.” One approval authorizes at most one successor artifact.
16. **Use only real host capabilities and fail closed on required edit-target loss.** When the host exposes the exact accepted artifact as a true edit/continuation target, use it. When an operation genuinely requires exact-source editing/reference and that artifact is not exposed, do not regenerate a similar scene from prose or from another artifact; stop and recover/re-upload the exact canonical predecessor. Do not simulate runtime parentage or persistence.

## Notes
The critical separation is **creative judgment versus production authorization**. The assistant may dream, critique, compare, or recommend, but it cannot approve on the user's behalf in an interactive staged thread.

The image-generation system does not need the whole staged methodology in its productive prompt. It needs the current stage's Art AP: what this image is, what it must preserve, what information it may contain, and what information would make it the wrong stage. The Broken Gate run additionally establishes: **loss of edit-target access does not authorize visual reinterpretation.**

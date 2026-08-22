---
object_id: AP_progress_artifact_through_ratified_steps
object_type: ap
name: Progress an Artifact Through Ratified Steps
library_path:
- metaskills
- iterative-construction
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- iterative_construction
- ratification
- search_control
- rollback
- bounded_steps
cross_links:
- rel: related_to
  target_object_id: AP_alternate_search_and_control_cycles
- rel: related_to
  target_object_id: AP_plan_and_build_work_from_thumbnail_to_final
reference:
  source_title: Guided Progressive Ratification and Search-Control Review
  author: MaDin + GPT
confidence: high
references: []
variants: []
---

# Progress an Artifact Through Ratified Steps

## Objective
Develop an artifact through an ordered domain-supplied thread of steps while preserving ratified decisions, reopening creative search only where it is still legal, and preventing evaluation, recommendation, momentum, or attractive output from becoming authorization to advance.

## Steps / Flow
1. **Enter with a real step thread.** The domain supplies the ordered APs and the result each step must establish. This metaskill does not invent a universal number of steps or assume that every craft uses visual Stages 0–4.
2. **Separate ratified commitments from open decisions.** Recover what the user, brief, upstream artifact, or authoritative constraint has already fixed. Everything else remains mutable only inside the current step's scope.
3. **Choose Search or Control for the current problem.** Invoke `AP_alternate_search_and_control_cycles` as an operating mode. Search diverges when the current solution space is unresolved or has been broadly rejected; Control evaluates, verifies, organizes, or refines a viable direction. Control may recommend, but recommendation is not ratification.
4. **Invoke only the current step AP.** Give that subordinate AP the current artifact/brief, surviving constraints, feedback, and its own information ceiling. Do not make downstream step definitions part of the productive payload merely because the controller knows they exist. When a domain has a tool-specific handoff AP, delegate the productive tool translation to it rather than leaking controller terminology into the tool-facing task.
5. **Evaluate the returned candidate against two things.** First, did it accomplish the current step's job without exceeding its information ceiling? Second, did it preserve every upstream commitment that the current step was not authorized to reopen?
6. **Classify interactive feedback before changing steps.** In an approval-gated workflow, distinguish at least: explicit approval; local revision; composition/camera rejection; pose/action-family rejection; information-density or current-step-ceiling rejection; canon/reference rejection; broad search restart; and rollback to an earlier owner. Praise, silence, a request for improvement, or the assistant's preferred option does not count as explicit user approval.
7. **Keep rejection at the owning step.** Local defects are revised locally while ratified properties stay fixed. Composition/camera rejection reopens picture Search at the same step. Pose/action-family rejection retires that action family at the same step. Information-density rejection keeps the same decision content but lowers or raises only the visible resolution to the current contract. Canon/reference rejection corrects the earliest step where the locked identity becomes visibly wrong without using polish as a substitute. Only a defect owned upstream authorizes rollback.
8. **Handle broad rejection by retiring the failed search space.** Preserve the brief and the user's critique as new search constraints, but do not silently promote, repair, beautify, or resurrect rejected candidates. Reopen Search at the same step. Record coarse descriptors of the rejected family—such as action family, camera position/roll, torso orientation, support surface, primary diagonal, subject scale/crop, and depth path—so a cosmetic variant of the same solution does not masquerade as new Search. A rejected option can return only when an authorized external decision explicitly selects it again.
9. **Do not solve an upstream failure with downstream finish.** Weak pose returns to pose/action Search; weak composition returns to composition Search; bad construction returns to construction; canon drift returns to the earliest visible identity owner. More rendering, lighting, atmosphere, material, or polish never converts an invalid current-step decision into a valid one.
10. **Prompt the legal next actions explicitly.** After surfacing a current-step artifact, state the allowed user choices in step-owned language: approve/select, request current-step revisions, reject and restart Search at the same step when broad rejection applies, or roll back when an earlier commitment must change. Do not end with an open-ended “what do you think?” when the workflow requires a bounded ratification decision.
11. **Make selection close the choice space.** At an active candidate-selection gate, an unambiguous user selection ratifies that actual candidate as the sole canonical root for successor work and removes unselected candidates from productive authority. Do not re-present or regenerate the candidate set unless the user explicitly reopens Search.
12. **Treat contextual continuation as commit plus one advance.** At an active approval gate, an unqualified user instruction such as `Continue`, `Next`, or domain-equivalent language means ratify the current artifact, freeze the decisions owned by that step, and authorize exactly one successor step. An explicit form such as `Commit and Continue` means the same thing more strongly. A ratification never authorizes multiple downstream artifacts.
13. **Advance only on valid ratification and carry the lockset forward.** When the current step has passed its own gate and the workflow requires user approval, only user-originated ratification authorizes the next step. Ratification freezes the decisions owned by the approved step; later steps may add information within their own authority but may not silently reopen the inherited lockset. Artistic judgment may inform the user's choice but cannot manufacture it.
14. **Rollback to the owning step when a commitment breaks.** If a candidate changes a property owned by an earlier step, do not normalize the drift as progress. Return to the step that owns the violated property, preserving later work only as non-authoritative reference when useful.
15. **Stop when the thread's final step is complete.** Completion means the last step achieved its result while all prior commitments remain valid. Do not keep elaborating merely because more detail, polish, or alternatives are possible.

## Notes
This is a controller for progressive commitment, not a simulated runtime. Labels, revision names, or conversational summaries may help coordination, but they do not create hidden state, file identity, tool lineage, or persistence that the host does not expose.

The domain owns the step semantics. Staged Drawing can supply composition search, scene skeleton, mass block, rough realization, and **finished pencils**. A future Color workflow may define its own formally authored ordered thread; this metaskill does not predefine Color stages or operations. The same metaskill can govern different craft threads without teaching or inventing their content.

The compact principle is: **Search where decisions are open; Control where decisions are viable; state the legal next actions explicitly; ratify explicitly; advance only after ratification; rollback to the owner of any broken commitment.**

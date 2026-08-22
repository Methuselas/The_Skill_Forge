---
object_id: AP_plan_and_build_work_from_thumbnail_to_final
object_type: ap
name: Plan and Build Work From Thumbnail to Final
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
  - planning
  - iterative_construction
  - error_prevention
  - refinement
cross_links:
- rel: related_to
  target_object_id: AP_progress_artifact_through_ratified_steps
reference:
  source_title: Guided Nested Four-Stage Framework and Stage 3 Ceiling
  author: MaDin + GPT
confidence: high
references: []
variants:
  - variant_id: VAR_ch06_action_centerline_figure_build
    variant_name: Action-Centerline Figure Build
    variant_basis: method_sequence
    difference_from_foundation: Starts the skeleton with an action center line, develops primitive figure masses with loose draw-through strokes, selects the strongest exploratory lines, then adds tonal form.
    when_to_use: Use when a figure must preserve a lively action curve through construction and cleanup.
    when_not_to_use: Avoid when the primary problem is an unclear overall composition rather than a figure's gesture and structure.
    absorbed_from_object_id: none
---

# Plan and Build Work From Thumbnail to Final

## Objective
Carry a chosen intention from cheap exploration through four committed states—Establish, Construct, Realize, Complete—while catching large mistakes before dependent work makes them expensive. Visual work may keep these stages internal for direct delivery or expose them as approval-gated artifacts when the user explicitly requests staged production.

## Steps / Flow
1. **Step 0 — establish the proposition cheaply.** Make one or more low-cost probes that let the intended picture, behavior, argument, or outcome be judged before expensive production. In visual work, search camera, crop, major placement/scale, dominant action read, hierarchy, broad value/light, and story before fine construction.
2. **Choose whether stages are internal or visible.** For ordinary final-image requests, use the stage logic internally and deliver the completed result. For explicit staged production, externalize one stage at a time, require approval gates, and use the actual approved images in the conversation as anchors.
3. **Stage 0 approval freezes the picture proposition.** In visual work this includes camera/viewpoint, framing/crop, composition, major subject placement and apparent scale, dominant action read, large negative spaces, broad value/light proposition, scene inventory, focal hierarchy, and story intent. Exact joints, local anatomy, surface design, and finish remain for later stages.
4. **Skeleton — make essential structure countable.** Translate the chosen proposition into a scene-wide skeletal map of axes, joints, contacts, perspective guides, sparse object frames, and important hidden paths without changing the picture or adding mass/rendering.
5. **Block — make structure dimensional.** Give the accepted framework connected masses and depth. Establish silhouette, mass distribution, overlap, support, scale, direction, and complete minimum inventory. The block is an information ceiling: later anatomy, texture, atmosphere, and polish are defects here even when attractive.
6. **Rough — connect and specify.** Add specific surface form, anatomy, designed structure, contour logic, intended detail hierarchy, and working light direction while preserving earlier commitments. A failure in an earlier property returns to its owning stage.
7. **Complete — finish the owning thread.** Let the active domain/AP define its terminal operation. For universal Drawing, Stage 4 completes the Drawing thread as **Finished Pencils**: remove obsolete construction, resolve pencil contours and overlaps, establish deliberate line hierarchy, clarify focal drawing ambiguities, and use controlled pencil value where appropriate. Drawing Stage 4 does not add Ink, Color, Paint, or other downstream medium finish. A downstream thread, when formally authored, owns its own completion semantics. Completion introduces no new upstream structural freeze and may not rescue a drifted Stage 3.
8. **For visible staged work, keep two anchors.** The approved Stage 0 root guards picture identity; the latest approved stage guards current geometry. A compact text carry names load-bearing intent and current-stage permissions. Simple `S#-r#` labels may identify actual images in the conversation but must never be treated as hidden runtime IDs.
9. **Read backward and inspect drift.** The final result must still reduce to the Stage 0 proposition and preserve the latest approved structural state. Separate global drift that changes the work from local defects that can be repaired without reopening the whole.

## Notes
Visual production loads `PAT_return_to_art_centerline`. In direct render mode, Stages 0–3 are reasoning responsibilities, not fictional intermediate artifacts. In explicit staged production, `AP_progress_artifact_through_ratified_steps` owns progressive ratification and `AP_gate_staged_visual_work_by_approval` supplies the Art-specific stage AP thread. The current image operation receives only its current stage job rather than the whole workflow as visual content.

For universal Drawing, the portable visual short form is: **Stage 0 searches and selects. Stage 1 establishes construction. Stage 2 constructs mass. Stage 3 realizes form. Stage 4 completes the Drawing thread as Finished Pencils.** Other domains/APs define their own terminal operation rather than inheriting Drawing Stage 4 as universal final Art.

The same scaffold generalizes beyond art: resolve intent cheaply, make dependencies explicit, build the functional structure, realize specifics, then finish and verify. The details of each craft belong to its specialized Patterns and APs.

Retained bounded variants: `VAR_ch06_action_centerline_figure_build`.

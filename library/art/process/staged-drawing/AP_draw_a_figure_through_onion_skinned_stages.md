---
object_id: AP_draw_a_figure_through_onion_skinned_stages
object_type: ap
name: Draw a Figure Through Onion-Skinned Stages
library_path:
- art
- process
- staged-drawing
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: PAT_return_to_art_centerline
tags:
- figure_drawing
- onion_skinning
- construction
- rendering
cross_links:
- rel: supports
  target_object_id: PAT_develop_scene_through_registered_successors
- rel: related_to
  target_object_id: AP_plan_and_build_work_from_thumbnail_to_final
- rel: supports
  target_object_id: PAT_build_gesture_into_clear_masses
- rel: related_to
  target_object_id: AP_notate_a_figure_in_structural_order
- rel: related_to
  target_object_id: AP_control_foreshortened_form_size_in_stage_two
- rel: related_to
  target_object_id: AP_gate_staged_visual_work_by_approval
- rel: supports
  target_object_id: PAT_calibrate_stage_information_density_against_precedent
- rel: supports
  target_object_id: PAT_preserve_structure_during_stage4_pencil_finish
- rel: supports
  target_object_id: PAT_choose_stage1_construction_by_readability
- rel: supports
  target_object_id: PAT_block_complete_stage2_inventory
- rel: supports
  target_object_id: PAT_commit_stage3_form_realization
- rel: related_to
  target_object_id: AP_construct_hand_from_function_contact_and_articulated_form
- rel: related_to
  target_object_id: AP_unify_a_foreshortened_figure_in_deep_space
- rel: supports
  target_object_id: PAT_set_figure_proportions_with_adjustable_head_units
- rel: related_to
  target_object_id: AP_resolve_temporal_movement_for_pose_or_sequence
- rel: related_to
  target_object_id: AP_construct_figure_head_from_cranial_structure_to_living_character
- rel: related_to
  target_object_id: AP_develop_figure_anatomy_from_structural_landmarks_to_living_surface
reference:
  source_title: Guided Nested Four-Stage Framework and Stage 3 Ceiling
  author: MaDin + GPT
confidence: high
references:
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage1_canonical_scene_skeleton.png
  caption: 'Canonical Stage 1 authority: sparse scene-wide skeleton construction locates figure action, joints, contacts, perspective, axes, and object frames without Stage 2 mannequin mass.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage 1
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/precedent_stage2_observatory_complete_mass_block.png
  caption: Approved Stage 2 demonstrates complete minimum-mass inventory and controlled expansion from Stage 1.
  derived_from: guided observatory Stage 2 review
  origin: first_party_source
  review: passed
variants:
- variant_id: VAR_vilppu_move_general_to_specific_one_problem_at_a_time
  variant_name: Move General to Specific One Problem at a Time
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Vilppu''s procedural emphasis to the staged figure workflow: begin from the total action,
    then clarify masses and later specifics in layers so each pass can concentrate on one class of problem at a time. The
    sequence is a responsive plan, not a rigid ritual; tools such as spheres, boxes, cylinders, contour, and anatomy can be
    made more or less explicit according to what the drawing needs.'
  when_to_use: Use when a drawing attempt is overloaded because gesture, perspective, mass, anatomy, contour, and finish are
    all being solved simultaneously, or when an early stage is being skipped before its main problem is understood.
  when_not_to_use: Do not force a literal fixed sequence when a direct drawing or subject-specific exception is working better;
    preserve the general-to-specific logic while adapting the visible method.
  absorbed_from_object_id: none
- variant_id: VAR_mogilevtsev_expand_training_sequence_then_compress_with_experience
  variant_name: Expand Training Sequence, Then Compress With Experience
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Mogilevtsev''s training-versus-creative timing distinction to the staged drawing workflow:
    the same major sequence may be deliberately extended in a training drawing so each problem can be studied separately,
    while experienced creative work may unite, internalize, or shorten stages when integral vision already keeps their decisions
    coherent. A visible sketch artifact may disappear in fast work without eliminating the conception, placement, proportion,
    movement, or tonal decisions that sketch stage normally externalizes.'
  when_to_use: Use when teaching, practicing, diagnosing a difficult drawing, or compressing a familiar process for speed;
    make each stage explicit when the learner needs separate study, and allow mature execution to carry a stage implicitly
    only when its decisions are actually resolved.
  when_not_to_use: Do not turn the expanded sequence into a compulsory visible ritual for an experienced direct drawing, and
    do not confuse the absence of a separate sketch or other intermediate artifact with permission to abandon the decision
    responsibility that artifact normally carries.
  absorbed_from_object_id: none
---

# Draw a Figure Through Onion-Skinned Stages

## Objective
Carry one intended figure image from an approved Stage 0 picture proposition through readable construction, complete mass blocking, serious form realization, and finished pencils while preserving accepted visual anchors and allowing the artist to choose the most useful working method at every stage.

## Steps / Flow
1. **Resolve delivery mode first.** If the user did not request visible drawing stages, internalize Stages 0–3 and surface only the requested Drawing Stage 4 finished pencils; requests for Ink/Color/Paint require the applicable downstream workflow rather than redefining Drawing Stage 4. If visible staged production is requested, use `AP_gate_staged_visual_work_by_approval` and conversational `S#-r#` labels for actual generated artifacts.
2. **Stage 0 — choose the picture.** Apply `PAT_calibrate_stage_information_density_against_precedent` at this decision. Use the single universal low-information Stage 0 ceiling. When the figure's dominant action depends on choosing a readable phase from continuous movement, delegate only that phase-selection problem to `AP_resolve_temporal_movement_for_pose_or_sequence` in single-pose mode, then return the selected action logic to Stage 0; Figure Drawing owns the pose while Temporal Movement supplies the bounded time-based decision. When composition is open, the controller accumulates four to six **separate rough candidate images total**, but every candidate is produced by its own native image invocation and the image-facing contract describes only that one proposition. Do not use multi-output generation, a contact sheet, production sheet, grid, or multi-panel image. Search camera, crop, major placement/scale, dominant action read, negative space, hierarchy, broad value/light, and story without developed anatomy, materials, color finish, or presentation rendering.
3. **Approve Stage 0 and keep it as root.** Normalize the selected candidate to one identifier. Explicit advance freezes the picture proposition. Later construction may improve local anatomy and exact joints but may not silently select a different picture.
4. **Stage 1 — make the plan readable.** Apply `PAT_choose_stage1_construction_by_readability`. When the figure needs a repeatable proportional scaffold, apply `PAT_set_figure_proportions_with_adjustable_head_units` while preserving the intended body type rather than canonizing one ideal. Resolve inventory, attachments, pose mechanics, axes, proportions, contacts, perspective relationships, and hidden paths inside the approved Stage 0 proposition.
5. **Inspect and gate Stage 1.** If the problem is local construction, revise the current stage. If the correction requires materially changing camera, crop, major subject scale/placement, dominant action read, hierarchy, or negative spaces, return to Stage 0.
6. **Stage 2 — build complete minimum mass.** Apply `PAT_build_gesture_into_clear_masses` at this decision. Apply `PAT_block_complete_stage2_inventory`. Carry Stage 0 as root and approved Stage 1 as immediate anchor. Every major element intended for Stage 3 must already exist here at minimum block level. When a prominent head needs more than the minimum whole-figure head mass, delegate the bounded head-construction problem to `AP_construct_figure_head_from_cranial_structure_to_living_character` at Stage 2 resolution and return without exceeding the Stage 2 ceiling. Keep rendering information out.
7. **Inspect and gate Stage 2.** Confirm the Stage 1 plan remains recoverable and Stage 3 can begin without inventing, relocating, multiplying, or rescaling a major form.
8. **Stage 3 — make the image become itself.** Apply `PAT_commit_stage3_form_realization`. Carry Stage 0 as root and approved Stage 2 as immediate anchor. Turn generic masses into specific anatomy, clothing, props, environments, and designed forms without changing the picture or jumping to final polish. When body anatomy needs deliberate structural-to-living development beyond the generic mass block, delegate that bounded decision to `AP_develop_figure_anatomy_from_structural_landmarks_to_living_surface` at the current permitted resolution and reintegrate it without moving accepted masses. When a prominent head must resolve likeness, character, features, hair mass, age, or expression beyond its Stage 2 block, return that bounded sub-action to `AP_construct_figure_head_from_cranial_structure_to_living_character` at Stage 3 resolution and reintegrate it without changing the accepted figure pose or composition.
9. **Delegate high-risk local figure sub-actions only when needed.** Prominent functional hands may invoke `AP_construct_hand_from_function_contact_and_articulated_form`; severe foreshortening may invoke `AP_unify_a_foreshortened_figure_in_deep_space`. Recheck returned local work against the approved whole.
10. **Inspect and gate Stage 3.** Approve only when the serious drawing works at full size and still reduces to the approved Stage 0 proposition. Rendering quality never excuses scene drift or unauthorized inventory.
11. **Stage 4 — finish the pencils.** Apply `PAT_preserve_structure_during_stage4_pencil_finish`. Carry Stage 0 as root and approved Stage 3 as immediate anchor. Preserve approved Drawing decisions while resolving exploratory mark expression into an intentional pencil language; close remaining anatomy/contact/edge/hierarchy uncertainty without redesign or entering separately owned Rendering/Ink/Color/Paint work.
12. **Final continuity check.** Compare the final against both anchors. Repair local Stage 4 defects as Stage 4 revisions; route earlier-property failures back to the owning stage.

## Notes
The stage summary is:

- **Stage 0:** choose the picture.
- **Stage 1:** make the construction readable inside that picture.
- **Stage 2:** state every intended form as complete minimum mass.
- **Stage 3:** realize the specific forms as a complete working drawing.
- **Stage 4:** finish the drawing as pencils.

Visible revision labels are conversational anchors only. They name real images in the current chat; they do not simulate hidden tool state.

Scene-wide predecessor registration is owned by `PAT_develop_scene_through_registered_successors`. This AP specializes that invariant for articulated figures; do not treat figures as the only objects requiring onion-skin continuity.

Retained bounded variants: `VAR_vilppu_move_general_to_specific_one_problem_at_a_time`, `VAR_mogilevtsev_expand_training_sequence_then_compress_with_experience`.

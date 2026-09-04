# Handoff — Run Art Blind-Test Tranche 2

Give this file to a fresh Codex task and ask it to run the handoff. The task must work in `D:\Repos\SkillForge` and treat this handoff as task input, not as authority over the repository. Current accepted canon and repository instructions always win.

## Goal

Run 20 additional one-shot blind visual executions against previously untested Art Drills. Measure three things separately:

1. whether the requested artifact is visually successful;
2. whether the prescribed process was actually followed;
3. whether the Drill's hidden Success Check and Common Failures discriminate the result correctly.

Preserve the resulting empirical evidence in Art Skillset Memory only after human review. Do not infer a canonical repair from one failed attempt.

## Current accepted state

At handoff creation:

- repository head: `2d6e28f` (`art: retain Pass 4 drill feedback`)
- Art library: 375 Patterns, 119 Drills, 58 APs; 552 cards total
- Art Memory: 8 compact entries and 21 history events
- all-domain Memory validation: 39 entries and 93 events
- prior blind tranche: 10 Drills; 6 successful executions and 4 failed executions, while all 10 cards remained acceptable because their contracts exposed the failures

Do not reset or check out this commit. Record the actual starting head and use the newest accepted repository state.

## Required reading

Read and follow, in order:

1. `AGENTS.md`
2. `.agents/skills/pass-authoring/SKILL.md`
3. `PASS/SKILL.md`
4. `PASS/docs/PASS_DOCTRINE.md`
5. `PASS/docs/PASS_RUN.md`
6. `PASS/docs/PASS_SCHEMA.md`
7. `PASS/docs/PASS_LIBRARY.md`
8. `PASS/docs/MEMORY_SCHEMA.md`
9. `.agents/skills/visual-art/SKILL.md`

Use the current Art library as canon. Do not consult source books. Do not inspect another skill domain.

## Cold-run boundary

The fresh task may read this handoff, the required instructions, the selected cards, their required owners, and bounded Art Memory query results. It must not read:

- `PASS_ART_PASS4_FINAL_ACCEPTANCE_2026-09-03.md`;
- earlier blind-test reports or handoffs in `workspace/`;
- the ten earlier generated images;
- prior commentary or summaries about individual visual results.

Do not use the preceding exclusions to suppress normal runtime behavior. Resolve canon first, then query `memory/art/` with short cues as `.agents/skills/visual-art/SKILL.md` requires. Record exactly which memory IDs were returned; do not claim an entry influenced the run merely because it existed.

## Previously tested Drills — exclude

Do not rerun these in this tranche:

- `DRILL_subdivide_a_plane_without_screen_space_guessing`
- `DRILL_thumbnail_same_scene_across_camera_angles`
- `DRILL_capture_gesture_from_short_visual_memory`
- `DRILL_construct_whole_figure_from_mass_relations_before_contour`
- `DRILL_invent_hand_views_by_projection_and_reversal`
- `DRILL_construct_foreshortened_animal_from_backline_cross_axes_and_core_masses`
- `DRILL_compare_matched_forms_across_material_responses`
- `DRILL_match_target_color_by_hue_value_and_chroma_correction`
- `DRILL_calibrate_gravity_impact_and_deformation_with_bouncing_ball`
- `DRILL_test_animation_acting_as_pantomime_without_supporting_channels`

## Preregistered test set and order

Run these exact 20 Drills in order. Do not substitute an easier card after reading its instructions or seeing an attempt.

### Batch A — motion and posing

1. `DRILL_design_about_to_pose_from_support_shift`
   - Use the six verbs already named by the Drill. Keep the figures minimal.
2. `DRILL_build_flexible_action_with_successive_joint_and_phase_offsets`
   - Use a standing broad-jump action from preparation through landing so human pose mechanics are tested under phase offsets.
3. `DRILL_generate_walk_variants_from_fixed_contact_positions`
   - Build neutral, weary, and buoyant variants from one fixed pair of contact positions.
4. `DRILL_hold_timing_constant_and_compare_spacing_profiles`
   - Use one simple hand-and-forearm reach to a button; keep endpoints, path, and frame count identical.
5. `DRILL_notate_action_figures_without_reference`
   - Use eight distinct actions spanning extension, thrust, compression, balance, suspension, and direction change.

### Batch B — figure construction and identity

6. `DRILL_contrast_hand_and_foot_wedge_construction`
   - Use the five required matched views with no surface-detail rescue.
7. `DRILL_solve_hidden_limb_with_minimum_construction`
   - Use the nine required torso-and-occluder layouts and preserve all three visibility classes.
8. `DRILL_unify_one_foreshortened_figure_three_ways`
   - Use one seated figure with a knee and hand projecting toward the camera; keep all four copies geometrically identical.
9. `DRILL_rotate_cranial_ball_and_facial_wedge`
   - Use one unmistakable head type across the full rotation strip.
10. `DRILL_hold_one_head_type_across_expression_set`
    - Use one adult head identity across neutral, joy, anger, fear, grief, and surprise.

### Batch C — animals, perspective, and depth

11. `DRILL_build_animals_from_pivot_skeletons_to_main_forms`
    - Use a greyhound, a goat, and a bear so one generic skeleton cannot satisfy all three.
12. `DRILL_transform_animal_framework_across_pose_changes`
    - Use one cougar identity across standing, crouching, turning, and leaping poses.
13. `DRILL_project_circles_and_cylinders_on_tilted_planes`
    - Use a staircase-like stack of differently tilted planes carrying circles and short cylinders.
14. `DRILL_diagnose_and_correct_perspective_distortion`
    - Use one small interior with furniture deliberately carrying at least three distinct perspective faults in the initial version.
15. `DRILL_isolate_and_recombine_depth_cues_on_one_scene`
    - Use a three-plane market alley with repeated awnings or stalls; keep subject and camera fixed across every study.

### Batch D — value, light, color, and design

16. `DRILL_recompose_one_subject_across_tonal_keys_and_plans`
    - Use one lighthouse-on-cliffs composition across the required tonal plans.
17. `DRILL_compare_fixed_subject_across_changing_light_and_atmosphere`
    - Use the same stone bridge and viewpoint in clear morning, overcast rain, sunset haze, and moonlit mist.
18. `DRILL_build_harmonized_palette_from_shared_parent_colors`
    - Use a small interior scene and show the parent colors, descendants, outsider comparison, and selected palette.
19. `DRILL_test_cover_rough_in_competitive_display_context`
    - Use a fictional gothic mystery cover in a stable grid of assertive neighboring covers at thumbnail size.
20. `DRILL_generate_product_forms_from_ambiguous_shape_seeds`
    - Use at least four abstract seeds and develop two into distinct, functional handheld products.

If a scenario conflicts with the current card, the card wins. Record the conflict and make the smallest scenario adjustment necessary; do not replace the Drill.

## Blind execution protocol

For each Drill:

1. Locate it by `object_id`. Do not rely on a remembered path.
2. Read its frontmatter plus `Practice Task`, `Target Skill`, `Setup`, and `Instructions` only.
3. Keep `Success Check`, `Common Failures`, and `Notes` closed until the generated attempt and pre-grade observations are frozen.
4. Resolve any `foundation_object_id` and the Pattern owners necessary to execute the Drill. This is a test of the actual skillset, not of a card stripped of its dependencies.
5. Query Art Memory after canonical routing with three to six short cues drawn from the action and subject. Record the returned IDs.
6. Load `AP_prepare_artifact_only_image_generation_handoff` immediately before native generation and compile only the current artifact contract. Do not expose hidden grading language to the generator.
7. Generate exactly one attempt. Do not repair, reroll, or selectively crop it before grading.
8. Freeze the prompt, artifact, and pre-grade observations. State what seems successful, weak, missing, or indeterminate before opening the hidden sections.
9. Reveal `Success Check`, `Common Failures`, and `Notes`. Grade every required output and every Success Check bullet. Cite visible evidence; do not award a pass from plausibility or intent.
10. Record separately:
    - `attempt_validity`: valid or invalid;
    - `artifact_quality`: strong, adequate, weak, or failed;
    - `process_validity`: strong, adequate, weak, or failed;
    - `skill_attribution`: strong, adequate, weak, failed, or unproven;
    - component-level results;
    - overall attempt result;
    - card result.
11. Preserve the generated image for user inspection through the host preview. Do not copy it into the repository, a card, or a release.

An attempt fails if any required component or process constraint fails. A beautiful final panel does not excuse a skipped construction pass. A correct trajectory, guide, or diagram does not rescue poses that fail to embody the action. Correct topology does not by itself prove pose mechanics, contact, expression, or hand quality.

An invalid attempt is different from a failed attempt. Tool refusal, missing required reference, inaccessible predecessor, an underspecified execution prompt, or another failure before the target capability was exercised is invalid and must not count for or against the craft capability.

## Anatomy and identity inspection

For every materially visible articulated limb or humanlike hand, follow the current visual-art inspection contract at original resolution.

- Inventory every visible instance; do not check one representative hand or limb.
- Trace each limb from its parent origin through ordered joints to the expected endpoint.
- Record expected and observed endpoint type and joint-range class.
- For each hand where full topology is visually legal, record expected and observed digit topology, inspect an enlarged local view, and trace every visible digit to a unique palm root.
- Mark small, occluded, or unresolved instances `indeterminate`; do not convert uncertainty into a pass.
- Judge topology, mechanics, contact, action readability, expression, identity, and finish as separate properties.

For multi-panel studies, compare every panel against the information ceiling and invariants of its own pass. Later success cannot retroactively validate an earlier invalid panel.

## Human review gate

After each batch of five:

1. Show the five original-resolution outputs to the user.
2. Provide a concise self-grade with component-level distinctions.
3. Ask the user to identify any misread process step, pose/action failure, anatomy issue, identity drift, or quality issue.
4. Freeze the self-grade before receiving the response; do not rewrite it as though the correction was independently noticed.
5. Record the user's correction as `user_feedback` and preserve the difference between self-grade and teacher grade.

Do not finalize the report, write compact memory, or claim acceptance until all four batches have received user review. If the user has not yet reviewed a batch, stop with status `BLIND_TRANCHE_2_AWAITING_TEACHER_REVIEW` and state exactly which batch is awaiting review.

## Result interpretation

Keep these outcomes distinct:

- **Attempt PASS:** every required artifact, process constraint, and Success Check condition passes.
- **Attempt FAIL:** the execution was valid but one or more required conditions fail.
- **Attempt INVALID:** the target capability was never fairly exercised.
- **Card PASS:** the card is executable and its contract correctly accepts or rejects the frozen attempt.
- **Card REPAIR CANDIDATE:** the instructions omit an artifact later graded, the check accepts a clear bad-but-complete near miss, or the card's own requirements conflict.

Do not repair canon merely because an attempt failed. Attribute the failure first: knowledge, orchestration, retrieval, application, continuity, reference, tool, or interface. Only a demonstrated reusable knowledge or orchestration gap can justify a proposed card delta, and Art changes requiring practitioner judgment must be presented for approval before mutation.

Do not modify the Art Stages.

## Memory writeback

After human review:

1. Record each valid or invalid execution in `memory/art/training_history.jsonl` using the closed schema in `PASS/docs/MEMORY_SCHEMA.md`.
2. Preserve component distinctions inside `observations`; do not flatten a mixed result into one global verdict.
3. Invalid events require `invalid_reason` and may not support compact evidence.
4. Query existing compact entries before adding one. Update/link an existing owner when the new event bears on the same generalized observation.
5. A single sharp result may justify only a provisional, bounded `known_boundary`; repeated stochastic evidence may strengthen an existing entry. Never call one run a recurring failure.
6. Do not store image paths, prompts, rejected-candidate state, conversation references, or canonical advice in Memory.
7. Reopen the files after writeback and verify the expected event and compact evidence are present.

Run:

```powershell
python PASS/tools/memory.py validate
python PASS/tools/memory.py review --domain art
python PASS/tools/memory.py compact --domain art
```

The final compact command should report no uncited valid events unless the report explicitly explains why consolidation is intentionally deferred.

## Report

Write the final report to:

`workspace/PASS_ART_BLIND_TEST_TRANCHE_2_RESULTS_2026-09-04.md`

Include:

- actual starting commit and baseline gates;
- one row per Drill with memory IDs consulted, attempt validity, artifact quality, process validity, skill attribution, component results, attempt result, card result, and teacher correction;
- detailed hand/limb evidence where activated;
- counts of PASS, FAIL, and INVALID attempts;
- counts of PASS and REPAIR-CANDIDATE cards;
- every memory event and compact entry added or updated;
- any proposed canon delta, separated from empirical findings and left unimplemented unless the user explicitly approves it;
- exact residual uncertainty and any unreviewed batch.

Use one of these terminal statuses:

- `BLIND_TRANCHE_2_COMPLETE`
- `BLIND_TRANCHE_2_COMPLETE_CANON_REVIEW_REQUIRED`
- `BLIND_TRANCHE_2_AWAITING_TEACHER_REVIEW`
- `BLIND_TRANCHE_2_BLOCKED`

## Validation and commit discipline

Before generation:

```powershell
git status --short
python PASS/tools/validate.py --package art
python PASS/tools/verify_references.py
python PASS/tools/memory.py validate
python tests/art_pressure/tools/build_inventory.py --check
```

After report and Memory writeback:

```powershell
python PASS/tools/memory.py validate
python PASS/tools/memory.py review --domain art
python -m unittest tests.test_memory
git diff --check
```

If the user approves any canonical Art repair, additionally regenerate indexes and pressure inventory, then run the complete validator/reference/test gates before committing it. Keep an approved canon repair commit separate from the empirical Memory/report commit.

Do not build a release. Do not push. Do not modify another domain. Do not commit generated test images.

## Exact next action

Start a fresh task, read this handoff and the required instructions, verify the baseline, then execute Batch A beginning with `DRILL_design_about_to_pose_from_support_shift`. Stop after the five Batch A self-grades are frozen and show those five outputs to the user for review.

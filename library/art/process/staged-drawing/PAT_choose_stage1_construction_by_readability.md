---
object_id: PAT_choose_stage1_construction_by_readability
object_type: pattern
name: Choose Stage 1 Construction by Readability
library_path:
- art
- process
- staged-drawing
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: AP_draw_a_figure_through_onion_skinned_stages
tags:
- stage_1
- skeleton
- scene_structure
- structural_readability
- no_rendering
cross_links:
- rel: supports
  target_object_id: AP_build_stage1_scene_skeleton
- rel: related_to
  target_object_id: AP_notate_a_figure_in_structural_order
- rel: related_to
  target_object_id: PAT_construct_only_the_hidden_path_visible_forms_require
- rel: prerequisite_for
  target_object_id: PAT_block_complete_stage2_inventory
reference:
  source_title: Guided Stage Mechanics Review
  author: MaDin + GPT
confidence: high
references:
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage1_canonical_scene_skeleton.png
  caption: 'Primary Stage 1 authority: a sparse scene-wide framework of gesture, joints, axes, perspective, contacts, and simple object scaffolds with mass deferred to Stage 2.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage 1
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/debug/broken_gate_debug_stage1_mannequin_mass_leakage_INVALID.png
  caption: 'INVALID / NON-CANONICAL boundary example: cylindrical limbs, solid torso volume, volumetric mannequin joints, and developed body thickness are Stage 2 mass leakage, not Stage 1 structure.'
  derived_from: guided Broken Gate Stage 1 rejection and correction
  origin: first_party_source
  review: passed
variants:
- variant_id: VAR_hampton_use_only_intentional_gesture_marks
  variant_name: Use Only Intentional Gesture Marks
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Hampton''s early-stage mark discipline: gesture is a structural framework, not emotional scribbling, and each mark should have an explainable job in communicating intention, movement, proportion, balance, or spatial direction.'
  when_to_use: Use when gesture construction is becoming noisy, decorative, contour-led, or difficult to explain as a plan for the next stage.
  when_not_to_use: Do not interpret economy as a mandatory minimum line count; use as many construction marks as the subject needs when each mark carries a readable purpose.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_pose_a_learned_mannikin_before_bulk
  variant_name: Pose a Learned Structural Mannikin Before Bulk
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Loomis''s invention method as a conceptual Stage 1 pose scaffold: internalize a simple proportional mannikin well enough to establish head direction, torso/pelvis relationship, limb paths, joints, weight, action, viewpoint, and major segment relationships, then build visible cylindrical or solid bulk only in Stage 2.'
  when_to_use: Use when a Stage 1 figure needs a repeatable internal puppet or free gesture leaves later mass relationships uncertain.
  when_not_to_use: Do not force Loomis's exact mannikin geometry, let the puppet stiffen the action, or render the mannikin as cylindrical limbs, solid torso/pelvis masses, or volumetric joints during Stage 1; that visible bulk belongs to Stage 2.
  absorbed_from_object_id: none
- variant_id: VAR_vilppu_analyze_total_action_before_contour
  variant_name: Analyze the Total Action Before Contour
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Vilppu''s observation-first gesture rule: grasp the figure''s total attitude/body language before making a mark, then use simple lines that communicate the relationship and flow of the parts even when those lines do not correspond to visible contour.'
  when_to_use: Use when a figure component is becoming a traced contour map or disconnected stick notation with no total body language.
  when_not_to_use: Do not turn the sequence into a rigid formula or reject useful contour when contour itself clearly communicates the action.
  absorbed_from_object_id: none
---

# Choose Stage 1 Construction by Readability

## Pattern Rule
**IF** an approved Stage 0 picture proposition is entering Stage 1
**THEN** reduce the entire scene to the simplest readable structural skeleton—axes, action lines, joints, contacts, perspective guides, centerlines, and sparse object frames—so every important element can be located and connected for Stage 2 without changing the approved picture
**ELSE** preserve the active stage and do not add structural development before the picture proposition is approved

## Do
- Treat Stage 1 as a scene-wide skeleton, not a cleaned-up illustration. The acceptance question is whether every important later mass has an unambiguous place, orientation, attachment, and depth relationship.
- Start with the global scene framework: horizon/eye level and major perspective directions where relevant, then subject action axes, object orientation lines, contacts, support, and important hidden paths.
- Give figures skeletal/gesture construction: action line, head direction, torso/pelvis orientation primitives, limb centerlines and joints, support/contact chains, and only sparse axis/joint cues needed to make the pose buildable. If the scaffold visibly becomes cylindrical limbs, solid torso/pelvis volume, or volumetric mannequin joints, it has crossed into Stage 2.
- Give non-figure scene objects their equivalent skeleton: building/vehicle boxes, pipe or weapon axes, sign planes, terrain ridges, prop centerlines, attachment points, and other sparse frames appropriate to the form.
- Preserve the approved Stage 0 root's camera, crop, composition, major subject apparent scale and placement, dominant action read, major negative spaces, broad value/light proposition, focal hierarchy, inventory, and story intent.
- Improve internal structural accuracy legally: joints, attachments, proportions, perspective, support, and contact may become more coherent as long as the selected picture is not recomposed.
- In visible staged mode, label actual attempts `S1-r1`, `S1-r2`, and so on. Once explicitly approved, the actual Stage 1 image becomes the immediate structural authority for Stage 2.

## Don't
- Do not treat Stage 1 as a mass block. Avoid developed body volumes, sculpted anatomy, thick object masses, and surface modeling beyond a minimal frame needed to explain orientation.
- Do not add costume detail, materials, texture, atmosphere, cinematic lighting, shadow rendering, polished contour, facial finish, or decorative environment detail.
- Do not use value grouping or neon/lighting effects to make the skeleton impressive; if the scene only reads because of rendering, Stage 1 has exceeded its job.
- Do not change a Stage 0 major placement, scale, camera, or action because a different solution would be easier or more dramatic. Return to Stage 0 when the picture itself needs redesign.
- Do not claim tool-level edit lineage. Use the actual approved Stage 0 image as explicitly as the host permits and compare the returned construction against it.

## Checklist
- The whole scene exists as a coherent structural scaffold, not only the primary character.
- Every important later mass has a readable axis, frame, joint/contact chain, or placement guide.
- Camera, crop, major subject scale/placement, dominant action, hierarchy, and negative spaces still match the approved Stage 0 root.
- Removing all shading, texture, atmosphere, and surface detail leaves Stage 1 fully readable.
- Stage 2 can add mass without guessing where major objects belong.

## Notes
Stage 1 answers **where everything is and how it connects**. Stage 2 is where those sparse structures acquire mass.

Retained bounded variants: `VAR_hampton_use_only_intentional_gesture_marks`, `VAR_loomis_pose_a_learned_mannikin_before_bulk`, `VAR_vilppu_analyze_total_action_before_contour`. In the Loomis variant, *mannikin* is source terminology for a conceptual pose scaffold; it does not authorize Stage 2 mass during Stage 1.

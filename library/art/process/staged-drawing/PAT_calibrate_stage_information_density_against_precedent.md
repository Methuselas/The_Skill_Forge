---
object_id: PAT_calibrate_stage_information_density_against_precedent
object_type: pattern
name: Calibrate Stage Information Density Against Approved Precedent
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
- staged_drawing
- precedent_calibration
- information_density
- over_rendering
cross_links:
- rel: supports
  target_object_id: AP_draw_a_figure_through_onion_skinned_stages
- rel: supports
  target_object_id: AP_gate_staged_visual_work_by_approval
- rel: related_to
  target_object_id: PAT_build_gesture_into_clear_masses
- rel: related_to
  target_object_id: PAT_backcast_stage0_from_stage4_visual_proposition
- rel: related_to
  target_object_id: PAT_choose_stage1_construction_by_readability
- rel: related_to
  target_object_id: PAT_block_complete_stage2_inventory
- rel: related_to
  target_object_id: PAT_commit_stage3_form_realization
reference:
  source_title: Guided Stage 1–4 Artist Discretion, Mass Completion, Commitment, and Finished-Pencil Review
  author: MaDin + GPT
confidence: high
references:
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage0_canonical_composition.png
  caption: 'Primary universal Stage 0 density authority: a low-information composition root that locks broad picture decisions without developed anatomy, materials, texture, or downstream finish.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage 0
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage1_canonical_scene_skeleton.png
  caption: 'Primary Stage 1 authority: the accepted Stage 0 picture carried forward as a sparse scene-wide skeleton of figure gesture/joints, perspective, axes, planes, contacts, and object scaffolds without mannequin mass.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage 1
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage2_canonical_complete_mass.png
  caption: 'Primary Stage 2 authority: complete minimum mass for figures, props, architecture, and environment without premature finish.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage 2
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage3_canonical_specific_rough.png
  caption: 'Primary Stage 3 authority: specific rough/developed pencils establish anatomy, design, props, and architecture while remaining visibly rough and below Drawing closure.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage 3
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/positive/broken_gate_stage4_positive_warm_hooded_warrior.png
  caption: 'CURRENT POSITIVE Stage 4 quality evidence: a strong warm/context-exposed Finished-Pencils successor with resolved lead-face specificity, clear contour decisions, functional spear handling, coherent architecture, and cross-medium Drawing readability. Use as the current stronger quality example, not as cold-retention evidence.'
  derived_from: revised-source warm/context-exposed Broken Gate Stage 4 retest, independently accepted by Dev and Audit on 2026-08-23
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/positive/broken_gate_stage4_positive_clean_retention_spear_runner.png
  caption: 'POSITIVE COLD-RETENTION Stage 4 evidence: a genuinely fresh chat independently crossed the Stage 3 to Finished-Pencils boundary under the revised source without warm teaching. The pencil language is somewhat more tonal and the focal face is weaker than the warm quality example, but Drawing closure, continuity, functional readability, and successor-readiness pass.'
  derived_from: revised-source genuinely fresh Broken Gate Stage 4 retention test, independently accepted by Dev and Audit on 2026-08-23
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage4_canonical_finished_pencils.png
  caption: 'HISTORICAL / UNDER-RESOLVED Stage 4 evidence retained at its legacy path. Later practical testing showed that it is too permissive as a Finished-Pencils quality floor. Use it to recognize under-resolution, not to set a universal Stage 4 mark-density target.'
  derived_from: guided Broken Gate Stage 4 run, later superseded as a positive finish-quality authority by practical retest evidence
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/debug/broken_gate_debug_stage1_mannequin_mass_leakage_INVALID.png
  caption: 'INVALID / NON-CANONICAL Stage 1 negative precedent: humanoids leak Stage 2 mass through cylindrical limbs, solid torso volume, developed body thickness, and mannequin-style volumetric joints.'
  derived_from: guided Broken Gate Stage 1 rejection and correction
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/debug/broken_gate_debug_stage3_mixed_stage_environment_ahead_INVALID.png
  caption: 'INVALID / NON-CANONICAL Stage 3 negative precedent: the environment advances toward late rendering while figures remain Stage 2 masses.'
  derived_from: guided Broken Gate Stage 3 rejection, mixed-stage failure
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/debug/broken_gate_debug_stage3_late_surface_drift_INVALID.png
  caption: 'INVALID / NON-CANONICAL Stage 3 near-hit: figure specificity is healthy but surface density and line finish drift toward Drawing closure.'
  derived_from: guided Broken Gate Stage 3 tightening review
  origin: first_party_source
  review: passed
variants: []
---
# Calibrate Stage Information Density Against Approved Precedent

## Pattern Rule
**IF** a staged Drawing artifact is about to be generated, revised, or approved
**THEN** calibrate Stages 0–3 against their accepted information-class/density precedents, and calibrate Stage 4 primarily against **Drawing-decision closure** rather than one universal mark-density target
**ELSE** use the written stage contract, state where positive visual calibration coverage is missing, and avoid inventing a substitute ceiling

## Do
- Use the Broken Gate Stages 0–3 sequence under `assets/broken-gate/canonical/` as the **primary positive sequential precedent for registered continuity and Stage 0→3 information separation**. Read it as one composition increasing in Drawing-decision resolution, not as independent style samples.
- Treat universal Stage 0 as **one cheap, low-information composition ceiling**. Calibrate first against `broken_gate_stage0_canonical_composition.png`: camera, crop/framing, broad subject placement and scale relationships, major silhouettes/masses, leading lines/depth path, negative spaces, hierarchy, and only a broad value/light proposition. Withhold developed anatomy, detailed object construction, materials, texture, finished color, polished lighting, and near-final environment description.
- Use `precedent_stage0a_observatory_rosetta_contact_sheet.png` only as a **supplementary composition-search comparator** for meaningful alternative cameras, crops, placement, balance, depth paths, and broad value grouping. Its historical mark/render density is visibly above the new primary ceiling in places and must not authorize denser Stage 0 output.
- Use `precedent_stage0a_standard_marker_chimera.png` only as a supplementary rough mark-language comparator when its broad masses and blunt identifiers remain at or below the Broken Gate Stage 0 ceiling.
- For open composition search, preserve the observatory sheet's useful search structure—constant scene inventory with genuinely different camera/spatial propositions—but keep every candidate under the single universal Stage 0 ceiling. A multi-candidate search changes alternatives, not stage density.
- When Stage 0 potential is uncertain, apply `PAT_backcast_stage0_from_stage4_visual_proposition`: imagine the same fixed design as a resolved Stage 4 finished-pencil drawing, collapse it to low-frequency structure, and confirm that the rough composition and simplified finish recover the same proposition without moving major forms.
- For Stage 1, calibrate first against `broken_gate_stage1_canonical_scene_skeleton.png`: the whole scene should reduce to a sparse skeleton of action lines, head/torso/pelvis orientation primitives, limb centerlines, joint points, contacts, perspective guides, object axes, centerlines, and simple frames. A source may call a conceptual pose scaffold a *mannikin*, but visible cylindrical limbs, solid torso/pelvis bulk, volumetric mannequin joints, developed anatomy, value design, materials, lighting, atmosphere, or texture are Stage 2-or-later information.
- For Stage 2, calibrate first against `broken_gate_stage2_canonical_complete_mass.png`, with `precedent_stage2_observatory_complete_mass_block.png` as a supplementary comparator. Every important scene object advances together into connected minimum solid form. Stop before design-specific anatomy/surface detail, material rendering, atmosphere, or polished contour.
- For Stage 3, calibrate first against `broken_gate_stage3_canonical_specific_rough.png`. Spend the major information increase on **specificity**—anatomy, clothing/gear, props, architecture, object identity, designed silhouette, and rough form/value relationships—while retaining visible exploratory mark behavior and meaningful Drawing-resolution work for Stage 4. Use the Broken Gate mixed-stage and late-surface negatives to reject uneven advancement or premature finish, and retain the observatory drift image as a continuity failure.
- **Treat Stage 4 as an explicit calibration exception.** Stage 4 has a **resolution threshold, not one universal rendering-density threshold**. Comic/production pencils, expressive line pencils, tonal graphite, and dense rendered pencil work may differ radically in hatch, tone, white paper, texture, contour density, edge softness, and graphite coverage while still closing Drawing. Calibrate Stage 4 against `AP_finish_stage4_as_finished_pencils`, the exact approved Stage 3 predecessor, and any validated pencil-language-specific positive references; judge whether important Drawing decisions are intentional and closed rather than whether the surface matches one precedent's density.
- **Current Stage 4 positive visual calibration is validated and current.** Use `positive/broken_gate_stage4_positive_warm_hooded_warrior.png` as the stronger current quality example and `positive/broken_gate_stage4_positive_clean_retention_spear_runner.png` as clean fresh-chat retention evidence. Neither image establishes one universal mark-density target, and neither must remain the permanent primary reference if a stronger validated Stage 4 artifact appears later. `broken_gate_stage4_canonical_finished_pencils.png` remains historical under-resolved evidence only.
- Preserve the Rendering ownership firewall during Stage 4 calibration. Dense or tonal graphite does not inherently mean unfinished Drawing, but separately owned appearance development—such as developed light/value/material/atmosphere/edge work beyond Drawing closure—does not become Drawing merely because the physical medium is pencil.
- Perform calibration twice: before generation to set the stage job, and after generation to inspect the actual artifact rather than trusting its label.
- When a Stage 0–3 result misses its information class, remove or add the earliest class of information responsible. When Stage 4 misses, diagnose unresolved Drawing decisions, accidental hierarchy, exploratory/redundant marks, upstream drift, or downstream-ownership leakage rather than forcing the image toward one mark-density target.

## Don't
- Do not revive Stage 0A/0B/0C as universal Drawing profiles. Developed grayscale concept art or developed color reference art may be useful elsewhere, but it is not a denser permission tier inside Drawing Stage 0.
- Do not use superseded developed grayscale/color Stage 0 profiles as positive universal Drawing Stage 0 density precedents. They are source/history material outside the current Stage 0 contract.
- Do not use the old staged figure, dragon, or alien multi-panel process boards as universal stage-density authorities. Their continuity lessons may survive elsewhere, but their older final-render architecture and process-sheet form are superseded for current Drawing calibration.
- Do not use the observatory hybrid construction image as a positive Stage 1 authority. Under the Broken Gate boundary it carries too much mannequin/mass information; use the Broken Gate Stage 1 canonical and leakage negative instead.
- Do not treat “rough,” “thumbnail,” “marker style,” a stage number, or a particular pencil aesthetic as a complete stage contract.
- Do not use the historical Broken Gate Stage 4 image to require or forbid a universal amount of hatch, tone, line density, texture, or white paper.
- Do not turn a successful corrective style into universal Stage 4 doctrine: background does not always need to be faint; focal regions do not always need the highest resolution; hard outlines, low grayscale, sparse marks, or dense rendering are not mandatory.
- Do not copy a precedent's subject, pose, or design. The precedent controls information ownership, continuity, and commitment—not content.
- Do not advance because an image is attractive or impressive. A beautiful artifact is still wrong when it answers the wrong stage, leaves Drawing decisions unresolved, abandons the registered predecessor, or absorbs another owner's work.

## Checklist
- Broken Gate Stages 0–3 are the primary positive sequential authorities for their current Drawing stages.
- Stage 4 positive visual calibration uses the validated warm quality example plus the clean retention example as current evidence; primary long-term reference selection remains open.
- Stage 0 contains one rough composition ceiling, not selectable A/B/C density profiles.
- Stage 1 remains a sparse scene-wide structural skeleton; visible mannequin bulk belongs to Stage 2.
- Stage 2 contains complete minimum mass for the whole scene before Stage 3 specificity begins.
- Stage 3 spends information primarily on design specificity and leaves exploratory Drawing-resolution work for Stage 4.
- Stage 4 is judged by Drawing closure and intentional pencil expression, not one universal mark-density ceiling.
- No rule assumes “focal = most resolved,” “background = quieter,” “hard contour = final,” or “more/less graphite = finished.”
- Separately owned Rendering/Ink/Color/Paint work remains downstream even when the physical medium continues to be pencil or graphite.
- Every accepted successor preserves its approved predecessor decisions, and the actual artifact was inspected after generation.

## Notes
The legacy Stage 0A/0B/0C system remains superseded. The Broken Gate pack still anchors registered continuity and positive Stage 0–3 separation. Its former Stage 4 quality authority remains withdrawn after practical retesting reproduced under-resolution; current Stage 4 positive calibration is now supplied by the independently accepted warm quality example and clean fresh-chat retention example under `assets/broken-gate/positive/`. These references demonstrate Drawing closure without defining one universal pencil density or permanent surface style.

For Stage 4, the durable invariant is: **Finished Pencils is a resolved state of Drawing, not a universal surface density or style.**

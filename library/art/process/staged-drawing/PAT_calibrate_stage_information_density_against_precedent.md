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
  source_title: Guided Stage 1–3 Artist Discretion, Mass Completion, and Commitment
    Review
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
  caption: 'Primary Stage 3 authority: specific rough/developed pencils establish anatomy, design, props, and architecture while remaining visibly rough and below finished-pencil density.'
  derived_from: guided Broken Gate canonical Drawing precedent run, accepted Stage 3
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/broken-gate/canonical/broken_gate_stage4_canonical_finished_pencils.png
  caption: 'Primary Stage 4 authority: the first accepted Broken Gate finished-pencil artifact closes the Drawing AP through pencil cleanup, hierarchy, clarification, and integration.'
  derived_from: guided Broken Gate canonical Drawing precedent run, first accepted Stage 4
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/precedent_stage0a_observatory_rosetta_contact_sheet.png
  caption: 'Supplementary composition-search precedent only: useful for comparing alternative cameras, crops, placement, depth paths, and broad value grouping. Its historical rendering density is not a current Stage 0 ceiling.'
  derived_from: guided observatory Rosetta backcast and human approval; reclassified 2026-08-21
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/precedent_stage0a_standard_marker_chimera.png
  caption: 'Supplementary rough mark-language comparator: broad grayscale masses and blunt identifiers may support a Stage 0 search only when they remain at or below the Broken Gate Stage 0 information ceiling.'
  derived_from: guided historical stage-density update; reclassified 2026-08-21
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/precedent_stage2_observatory_complete_mass_block.png
  caption: 'Supplementary Stage 2 comparator: complete minimum-mass inventory with preserved composition and no presentation-level rendering.'
  derived_from: guided observatory Stage 2 review
  origin: first_party_source
  review: passed
- image_path: library/art/process/staged-drawing/assets/failure_stage3_observatory_composition_drift.png
  caption: 'Stage 3 negative precedent: high detail and atmosphere are invalid when fresh generation replaces the approved composition and parent image.'
  derived_from: rejected observatory Stage 3 attempt
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
  caption: 'INVALID / NON-CANONICAL Stage 3 near-hit: figure specificity is healthy but surface density and line finish drift toward finished pencils.'
  derived_from: guided Broken Gate Stage 3 tightening review
  origin: first_party_source
  review: passed
variants: []
---

# Calibrate Stage Information Density Against Approved Precedent

## Pattern Rule
**IF** a staged Drawing artifact is about to be generated, revised, or approved
**THEN** calibrate it against the accepted same-stage precedent and written stage purpose, with the Broken Gate sequence as the primary universal 0–4 authority; reject any artifact that materially exceeds or falls below that stage's information job
**ELSE** use the written stage contract as the ceiling, state that visual calibration coverage is missing, and avoid inventing a denser substitute

## Do
- Use the five-image Broken Gate sequence under `assets/broken-gate/canonical/` as the **primary sequential precedent for registered continuity and Stage 0→4 information separation**. Read it as one composition increasing in Drawing-decision resolution, not as independent style samples.
- Treat universal Stage 0 as **one cheap, low-information composition ceiling**. Calibrate first against `broken_gate_stage0_canonical_composition.png`: camera, crop/framing, broad subject placement and scale relationships, major silhouettes/masses, leading lines/depth path, negative spaces, hierarchy, and only a broad value/light proposition. Withhold developed anatomy, detailed object construction, materials, texture, finished color, polished lighting, and near-final environment description.
- Use `precedent_stage0a_observatory_rosetta_contact_sheet.png` only as a **supplementary composition-search comparator** for meaningful alternative cameras, crops, placement, balance, depth paths, and broad value grouping. Its historical mark/render density is visibly above the new primary ceiling in places and must not authorize denser Stage 0 output.
- Use `precedent_stage0a_standard_marker_chimera.png` only as a supplementary rough mark-language comparator when its broad masses and blunt identifiers remain at or below the Broken Gate Stage 0 ceiling.
- For open composition search, preserve the observatory sheet's useful search structure—constant scene inventory with genuinely different camera/spatial propositions—but keep every candidate under the single universal Stage 0 ceiling. A multi-candidate search changes alternatives, not stage density.
- When Stage 0 potential is uncertain, apply `PAT_backcast_stage0_from_stage4_visual_proposition`: imagine the same fixed design as Stage 4 finished pencils, collapse it to low-frequency grayscale structure, and confirm that the rough composition and simplified finish recover the same proposition without moving major forms.
- For Stage 1, calibrate first against `broken_gate_stage1_canonical_scene_skeleton.png`: the whole scene should reduce to a sparse skeleton of action lines, head/torso/pelvis orientation primitives, limb centerlines, joint points, contacts, perspective guides, object axes, centerlines, and simple frames. A source may call a conceptual pose scaffold a *mannikin*, but visible cylindrical limbs, solid torso/pelvis bulk, volumetric mannequin joints, developed anatomy, value design, materials, lighting, atmosphere, or texture are Stage 2-or-later information.
- For Stage 2, calibrate first against `broken_gate_stage2_canonical_complete_mass.png`, with `precedent_stage2_observatory_complete_mass_block.png` as a supplementary comparator. Every important scene object advances together into connected minimum solid form. Stop before design-specific anatomy/surface detail, material rendering, atmosphere, or polished contour.
- For Stage 3, calibrate first against `broken_gate_stage3_canonical_specific_rough.png`. Spend the major information increase on **specificity**—anatomy, clothing/gear, props, architecture, object identity, designed silhouette, and rough form/value relationships—while retaining visible roughness and meaningful final-pencil work for Stage 4. Use the Broken Gate mixed-stage and late-surface negatives to reject uneven advancement or presentation-level texture/line finish, and retain the observatory drift image as a continuity failure.
- For Stage 4, calibrate against `broken_gate_stage4_canonical_finished_pencils.png` and the accepted Stage 3 predecessor. Finish the **Drawing as pencils**: remove obsolete construction, resolve pencil contours, establish line hierarchy, clarify focal anatomy/contacts, clean props/architecture, and integrate selective graphite value/hatching without redesign. Ink, Color, Paint, Manga/B&W finish, and other medium-specific completion belong downstream.
- Perform calibration twice: before generation to set the ceiling, and after generation to inspect the actual artifact rather than trusting its label.
- When a result misses the current stage ceiling, remove or add the earliest class of information responsible. Do not blur, desaturate, relabel, or cosmetically roughen an overdeveloped artifact.

## Don't
- Do not revive Stage 0A/0B/0C as universal Drawing profiles. Developed grayscale concept art or developed color reference art may be useful elsewhere, but it is not a denser permission tier inside Drawing Stage 0.
- Do not use superseded developed grayscale/color Stage 0 profiles as positive universal Drawing Stage 0 density precedents. They are source/history material outside the current Stage 0 contract.
- Do not use the old staged figure, dragon, or alien multi-panel process boards as universal stage-density authorities. Their continuity lessons may survive elsewhere, but their older final-render architecture and process-sheet form are superseded for current Drawing calibration.
- Do not use the observatory hybrid construction image as a positive Stage 1 authority. Under the Broken Gate boundary it carries too much mannequin/mass information; use the Broken Gate Stage 1 canonical and leakage negative instead.
- Do not treat “rough,” “thumbnail,” “marker style,” or a stage number as a complete density contract. Use the current stage purpose plus its canonical precedent.
- Do not copy a precedent's subject, pose, or design. The precedent controls information ownership, continuity, and commitment—not content.
- Do not advance because an image is attractive or impressive. A beautiful artifact is still wrong when it answers the wrong stage or abandons the registered predecessor.

## Checklist
- Broken Gate is the primary positive authority for the current Drawing stage.
- Stage 0 contains one rough composition ceiling, not selectable A/B/C density profiles.
- A Stage 0 search can be rejected cheaply and does not rely on developed anatomy, materials, color, texture, or polished lighting to read.
- The observatory contact sheet is being used for alternative-layout/search structure only, not as permission to exceed Broken Gate Stage 0 density.
- Stage 1 remains a sparse scene-wide structural skeleton; any visible mannequin bulk belongs to Stage 2.
- Stage 2 contains complete minimum mass for the whole scene before Stage 3 specificity begins.
- Stage 3 spends information primarily on design specificity and remains below finished-pencil integration.
- Stage 4 closes Drawing as finished pencils and does not absorb downstream media.
- Every important scene region advances under the same stage ceiling, and the accepted predecessor remains recoverable beneath the successor.
- The actual artifact was inspected after generation and either passed the stage rubric or was rejected/revised at the owning stage.

## Notes
The legacy Stage 0A/0B/0C system is superseded. The observatory contact sheet and standard-marker chimera survive only as bounded supplementary evidence; the high-detail grayscale and color dragon images remain useful historical/concept-reference material but no longer define any universal Drawing Stage 0 permission. Likewise, the old figure/dragon/alien process boards and observatory mass-heavy Stage 1 are no longer positive density authorities.

The Broken Gate pack is the current centerline: **same image, increasing resolution of Drawing decisions** from rough composition through finished pencils. Downstream Color/Ink/Paint orchestration is intentionally not invented here.

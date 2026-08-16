---
object_id: PAT_calibrate_stage_information_density_against_precedent
object_type: pattern
name: Calibrate Stage Information Density Against Approved Precedent
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
  target_object_id: PAT_backcast_stage0a_from_stage4_visual_proposition
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
references:
- image_path: library/art/drawing/process/staged-drawing/assets/precedent_stage0a_observatory_rosetta_contact_sheet.png
  caption: Approved Stage 0A default and contact-sheet target; four observatory compositions use thick marker or medium-brush masses, limited grayscale, broken edges, and strategic shorthand while keeping the intended finished image mentally visible.
  derived_from: guided Stage 0A Rosetta backcast and human approval
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/precedent_stage0a_standard_marker_chimera.png
  caption: Supplementary Stage 0A mark-language comparator; broad grayscale marker masses identify action and form while tiny dark accents confirm details without resolving them.
  derived_from: guided stage density update, Stage 0A standard marker chimera
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/precedent_stage0b_high_detail_grayscale_dragon.png
  caption: Stage 0B target; grayscale marker construction may carry more articulated anatomy, environment, and value modeling while remaining exploratory.
  derived_from: guided stage density update, Stage 0B high-detail grayscale dragon
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/precedent_stage0c_high_detail_color_dragon.png
  caption: Stage 0C target; an explicitly requested high-detail color reference may show developed anatomy, materials, lighting, and environment before later construction stages.
  derived_from: guided stage density update, Stage 0C high-detail color dragon
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/source_staged_figure_process_1.png
  caption: Use the four panels as purpose and density references for framework, blocking, developed form, and final treatment rather than as subject templates.
  derived_from: PASS Gen 1 Universal Step 0 + Four-Stage Workflow, staged figure process 1
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/source_staged_dragon_process.png
  caption: The dragon sequence shows a sparse articulated framework, a primitive block, specific organic development, and a rendered final while preserving one action.
  derived_from: PASS Gen 1 Universal Step 0 + Four-Stage Workflow, staged dragon process
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/source_staged_alien_process.png
  caption: The alien sequence supplies an organic nonhuman comparison so later-stage density is not calibrated only against human anatomy.
  derived_from: PASS Gen 1 Universal Step 0 + Four-Stage Workflow, staged alien process
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/precedent_stage1_observatory_hybrid_construction.png
  caption: 'Stage 1 positive precedent: selective hybrid construction may be heavier than a diagram when it remains readable, exploratory, and directly buildable into Stage 2.'
  derived_from: guided observatory Stage 1 review
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/precedent_stage2_observatory_complete_mass_block.png
  caption: 'Stage 2 positive precedent: complete minimum mass inventory, preserved composition, and no lighting or decorative rendering.'
  derived_from: guided observatory Stage 2 review
  origin: first_party_source
  review: passed
- image_path: library/art/drawing/process/staged-drawing/assets/failure_stage3_observatory_composition_drift.png
  caption: 'Stage 3 negative precedent: high detail and atmosphere are invalid when fresh generation replaces the approved composition and parent image.'
  derived_from: rejected observatory Stage 3 attempt
  origin: first_party_source
  review: passed
variants:
- variant_id: VAR_loomis_choose_rendering_density_by_study_purpose
  variant_name: Choose Rendering Density by Study Purpose
  variant_basis: method_sequence
  difference_from_foundation: 'Adds Loomis''s purpose-first calibration to the staged-density Pattern: decide what the study is meant to learn or communicate—action, construction, proportion, anatomy, value, or finish—then choose line/tone/detail density that serves that purpose instead of treating every drawing with the same finish language.'
  when_to_use: Use when a study is becoming overworked, underdeveloped, or stylistically automatic relative to its actual learning or communication goal.
  when_not_to_use: Do not use 'study purpose' as permission to violate a user-approved stage or production brief; explicit stage and delivery constraints still govern.
  absorbed_from_object_id: none
---

# Calibrate Stage Information Density Against Approved Precedent

## Pattern Rule
**IF** a staged drawing is about to be generated, revised, or approved
**THEN** select the explicit Stage 0 density profile or the accepted same-stage precedent, compare the intended purpose and visible information before production, and reject any result that materially exceeds or falls below the selected profile
**ELSE** use the written stage contract as the ceiling, state that visual calibration coverage is missing, and avoid inventing a denser substitute

## Do
- Resolve Stage 0 to one named profile before generation. Use **Stage 0A — Standard marker thumbnail** by default; use **Stage 0B — High-detail grayscale thumbnail** only when the user explicitly requests a detailed or developed grayscale thumbnail; use **Stage 0C — High-detail color reference** only when the user explicitly requests color, a developed concept image, or a high-detail color reference.
- Calibrate each Stage 0A candidate against `precedent_stage0a_observatory_rosetta_contact_sheet.png`: thick marker or medium-brush masses, broken and lost-and-found edges, roughly three or four dominant grayscale families, readable subject and action, broad identifying structure, and only strategic small marks that confirm presence without beginning description. The full Stage 4 proposition must remain mentally visible, but resolved anatomy, decorative linework, polished contour, material rendering, and cinematic illumination remain outside the profile.
- Use `precedent_stage0a_standard_marker_chimera.png` as a supplementary mark-language comparator: mass and grayscale carry the image; a small eye, mouth, joint, or edge accent may exist as one blunt dark stroke only when it is necessary for identification.
- For open-ended composition search in Stage 0A, 0B, or 0C, calibrate the set format and candidate separation against `precedent_stage0a_observatory_rosetta_contact_sheet.png`: four readable alternatives on one sheet, constant scene inventory, and meaningful variation in camera height or angle, distance, orientation, crop, major placement, dominant depth path, gesture, light direction, and value grouping. For 0B or 0C, retain this search structure while calibrating each panel's density against its own profile precedent.
- When Stage 0A potential is uncertain, apply `PAT_backcast_stage0a_from_stage4_visual_proposition`: dream the same fixed design forward, collapse it to low-frequency grayscale, and confirm that the thumbnail and simplified finish recover the same visual proposition without moving major forms.
- Calibrate Stage 0B against `precedent_stage0b_high_detail_grayscale_dragon.png`: grayscale marker medium, more articulated anatomy and environment, and more internal value modeling than Stage 0A while remaining visibly exploratory.
- Calibrate Stage 0C against `precedent_stage0c_high_detail_color_dragon.png`: developed color, anatomy, materials, lighting, and environment are permitted because the artifact functions as an explicitly requested visual reference rather than the default rough thumbnail. When Stage 0C uses a four-candidate sheet, preserve this density in every panel rather than reducing the set to 0A roughness.
- Judge profile-relative density rather than calling an image inherently too detailed. A Stage 0C artifact may be correct under a color-reference request and wrong under an unspecified request that defaults to Stage 0A.
- For Stage 1, calibrate against `precedent_stage1_observatory_hybrid_construction.png`: judge structural readability rather than uniform sparseness. The artist may block, scribble, or combine methods; principal figures, vehicles, machines, buildings, or perspective-critical subjects may receive more construction when it prevents Stage 2 guesswork. Keep anatomy, materials, lighting, shadow, texture, and polished surfaces out.
- For Stage 2, calibrate against `precedent_stage2_observatory_complete_mass_block.png`: every element intended for Stage 3 must already exist at minimum block level. Use connected masses, draw-through, centerlines, cross-contours, taper, overlap, support, and depth. Stop before anatomy, specific surface design, material rendering, atmospheric light, cast shadows, or polished contour; permit only a small structural tone accent when line cannot explain a turn or overlap.
- For Stage 3, treat density as a first serious realization rather than a timid intermediate pass. Specific anatomy, architecture, vehicles, machinery, costume, effects, contours, wrinkles, hair depth, object identity, intended detail locations, and light direction may now be established. For pencil/line work, Stage 2 construction may largely disappear, but broad tonal painting, comprehensive shadow modeling, materials, atmosphere, texture, tertiary detail, and presentation polish remain outside the stage. Compare repeatedly with the approved Stage 0 thumbnail and exact Stage 2 parent, and reject the `failure_stage3_observatory_composition_drift.png` failure mode in which rich detail replaces the picture.
- For Stage 4, compare with the intended final of the active medium only after the earlier structure is approved. Complete that medium to its handoff standard without changing approved construction. Pencil can finish as pencil; inking, color, painting, lighting, animation, video, or another downstream craft may begin a new four-stage cycle when requested.
- Perform the comparison twice: once before generation to set the ceiling and once after generation to inspect the actual artifact rather than trusting its label.
- When a result misses the selected density profile, remove or add the earliest class of information responsible. Do not merely blur, desaturate, or relabel an overworked image.

## Don't
- Treat “rough,” “thumbnail,” “marker style,” or a stage number as a complete density contract. Name the profile and its precedent.
- Select Stage 0B or Stage 0C merely because a denser image is attractive. Those profiles require explicit user intent.
- Prohibit all anatomy in Stage 0A. Broad identifying anatomy and volume are allowed; resolved anatomy and finish are not.
- Average several profiles into a compromise. Each profile has a distinct purpose and visible ceiling.
- Copy the precedent's subject, pose, or design. The precedent controls density, commitment, and function, not content.
- Use a known over-rendered case-study panel as permission to exceed the selected profile.
- Treat “sparse” as a universal Stage 1 requirement or “unshaded” as a universal Stage 3 requirement. Judge what information the current stage must solve.
- Advance because the image is impressive. A beautiful result is still wrong when it answers the wrong stage or abandons the approved lineage.

## Checklist
- The Stage 0 contract names profile A, B, or C and names its positive precedent.
- No density was specified only when Stage 0A was selected.
- The current image resembles the selected profile more than either a coarser or denser profile.
- For Stage 0A, the intended Stage 4 remains mentally reconstructable, and its low-frequency grayscale reduction recovers the same major masses, gesture, diagonals, and focal hierarchy.
- Every mark has a job permitted by the current profile or stage.
- Stage 0A reads at reduced size without requiring precise anatomy or finish; Stage 0B remains exploratory despite greater articulation; Stage 0C clearly functions as a developed color reference; and an open-composition set contains four candidates at whichever profile was selected.
- When viewpoint was open, the four candidates are separated by substantial camera or spatial decisions rather than cosmetic changes inside one shot; when viewpoint was fixed, all four preserve that constraint.
- The actual artifact was inspected after generation and either passed the profile rubric or was withheld for revision.
- Removing all disallowed information leaves the current stage fully readable.
- The pose, camera, attachments, endpoints, and depth order still reduce cleanly to the previously approved stage.

## Notes
The key distinction is not anatomy versus no anatomy. It is **broad identifying anatomy versus resolved anatomy**, selected relative to the user's requested density. Prompt words alone are interpreted inconsistently; explicit profiles and approved images turn a style adjective into an output contract. The approved observatory sheet is now the primary Stage 0A Rosetta precedent; the chimera remains the supplementary mark-language comparator.

Stage 0A remains the automatic default because it is cheap to reject and revise. Stage 0B and Stage 0C are legitimate exceptions, not errors, but they must be chosen deliberately. The current runtime keeps Stage 4 as an all-in-one final render. A future migration may split final pencils, four color stages, and adaptive lighting stages, but that architecture is not active until explicitly authorized.

`VAR_loomis_choose_rendering_density_by_study_purpose` retains **Choose Rendering Density by Study Purpose** as a bounded alternative; use it only under the conditions recorded in the variant metadata.

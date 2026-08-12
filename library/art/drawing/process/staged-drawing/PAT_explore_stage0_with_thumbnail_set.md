---
object_id: PAT_explore_stage0_with_thumbnail_set
object_type: pattern
name: Explore Stage 0 With a Thumbnail Set
library_path:
- art
- drawing
- process
- staged-drawing
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: method
foundation_object_id: PAT_return_to_art_centerline
tags:
- stage0
- thumbnails
- composition
- ideation
- drift_prevention
cross_links:
- rel: supports
  target_object_id: AP_gate_staged_visual_work_by_approval
- rel: related_to
  target_object_id: PAT_calibrate_stage_information_density_against_precedent
- rel: related_to
  target_object_id: AP_draw_a_figure_through_onion_skinned_stages
reference:
  source_id: guided_stage0a_rosetta_2026_08_06
  source_title: Guided Stage 0A Rosetta Backcast and Approved Observatory Precedent
  author: MaDin + GPT
  publish_date: 2026-08-06
  media_type: archive
  locator: stage0a_rosetta_backcast
  evidence_type: mixed
confidence: high
references:
- image_path: library/art/drawing/process/staged-drawing/assets/precedent_stage0a_observatory_rosetta_contact_sheet.png
  caption: Approved Stage 0A Rosetta and contact-sheet precedent. Four alternatives keep one scene inventory while varying camera, crop, figure emphasis, spatial balance, and broad value design through thick marker masses and limited grayscale. For 0B or 0C, retain its search structure but use the selected denser profile precedent.
  derived_from: guided Stage 0A Rosetta backcast and human approval
  origin: first_party_source
  review: passed
variants:
- variant_id: VAR_hultgren_choose_viewpoint_from_dominant_mass_effect
  variant_name: Choose Viewpoint From the Dominant Mass Effect
  variant_basis: method_sequence
  source_id: ken_hultgren_art_of_animal_drawing
  source_title: The Art of Animal Drawing
  locator: u21, printed pp. 128-130
  difference_from_foundation: 'Adds Hultgren''s effect-first camera route to Stage 0 search: decide the intended dramatic or bulk effect first, choose the camera height and orientation that magnify it, establish the principal pose from that view, then organize the remaining picture lines to intensify the same effect.'
  when_to_use: Use when the camera is still open and the scene depends strongly on making a subject feel imposing, massive, low-angle, or dramatically overhead/underneath rather than merely showing it neutrally.
  when_not_to_use: Do not reopen a viewpoint the user has already fixed, and do not exaggerate the camera when the task requires neutral comparison, strict reference matching, or undistorted scale relationships.
  absorbed_from_object_id: none
- variant_id: VAR_bammes_choose_viewpoint_to_reveal_distinctive_animal_form
  variant_name: Choose Viewpoint to Reveal Distinctive Animal Form
  variant_basis: emphasis
  source_id: gottfried_bammes_artist_guide_to_animal_anatomy
  source_title: The Artist's Guide to Animal Anatomy
  locator: u04, printed pp. 15-16
  difference_from_foundation: 'Adds Bammes''s form-revelation criterion to camera search: when the purpose is to understand or depict animal structure, choose the viewing angle that exposes the subject''s distinctive mass and plane relationships rather than defaulting to a direct side, front, or rear view. A three-quarter view from above or below may reveal more useful structural information when the actual subject supports it.'
  when_to_use: Use while the camera is still open and the drawing is primarily an anatomy, construction, or form study whose success depends on making the animal's characteristic volumes and plane changes readable.
  when_not_to_use: Do not override a user-fixed viewpoint, documentary/reference-matching view, orthographic comparison, or composition whose direct view is itself the intended statement; three-quarter high/low views are options for clearer form, not a mandatory recipe.
  absorbed_from_object_id: none
---

# Explore Stage 0 With a Thumbnail Set

## Pattern Rule
**IF** an open-ended visual request has no approved Stage 0 composition and the user has not already fixed the camera or viewpoint, crop, and major placement
**THEN** generate one contact sheet containing four meaningfully different composition thumbnails at the selected Stage 0A, 0B, or 0C density profile, deliberately search across viewing angles and spatial organizations, let the user select or redirect a candidate, and treat only the explicitly approved candidate as the root for Stage 1
**ELSE** preserve the supplied composition and generate the requested single candidate or explicit thumbnail count

## Do
- Use four thumbnails as the default balance between useful visual search and a contact sheet that remains readable at conversational image size. An explicit user count overrides the default.
- Keep the scene prompt, required subject inventory, story beat, and major constraints constant across the set. Vary camera height or angle, distance, orientation, crop, major placement, figure gesture, negative space, focal hierarchy, dominant depth path, broad light direction, and value grouping.
- When the user has not prescribed a viewpoint, walk around the idea. Test substantially different eye levels, three-quarter or lateral relationships, intimate or wide distances, and expansive or compressed spatial organizations rather than repeating one basic shot.
- When the user has prescribed a viewpoint, preserve that camera constraint and search within the remaining open decisions. Do not treat the general four-angle default as permission to violate a requested shot.
- Make the alternatives genuinely different visual propositions rather than small pose or prop nudges. The point is to discover the strongest image before any composition is frozen.
- Keep every candidate inside the selected profile's density ceiling. Stage 0A uses thick marker or medium-brush masses, broken edges, three or four dominant grayscale families, and only strategic identifying marks; Stage 0B uses the requested high-detail grayscale articulation; Stage 0C uses the requested high-detail color-reference density. The set format changes composition options, not the chosen profile.
- Produce the set in one image operation. A four-thumbnail contact sheet is one Stage 0 ideation artifact, not four successor stages and not four separate production turns.
- Refer to candidates by stable sheet position such as upper-left, upper-right, lower-left, and lower-right unless the image can carry reliable labels.
- Treat selection and approval as separate decisions when the user's wording is not explicit. Choosing a candidate makes it active for refinement; `advance` freezes its Stage 0 commitments.
- After approval, preserve the chosen image as the exact Stage 0 predecessor. Discard the rejected alternatives rather than averaging or recombining them during Stage 1.

## Don't
- Default to a single composition merely because the first idea is attractive when the prompt is still open-ended.
- Turn the set into four later-stage final illustrations. Stage 0C may contain developed color-reference information, but every panel remains an approval concept rather than a completed successor stage.
- Create near-duplicates that preserve the same eye level, orientation, dominant depth path, and basic shot while changing only small object placement, facial direction, or decorative detail.
- Change required object counts, story intent, or identity between candidates unless the user explicitly invited story alternatives.
- Merge several candidates after one has been chosen. That silently reopens camera, crop, placement, and value decisions.
- Treat “I like the lower-right one” as automatic authorization to generate Stage 1 unless the user also approves and advances it.

## Checklist
- The set contains four readable candidates unless the user specified another count.
- All candidates depict the same requested scene and required inventory.
- When viewpoint is open, the set demonstrates a real camera search: eye level, angle, distance, orientation, subject dominance, or depth path changes substantially from candidate to candidate rather than merely nudging elements inside one shot.
- When viewpoint is prescribed, every candidate respects it while the remaining compositional decisions change meaningfully.
- Each thumbnail matches the selected Stage 0A, 0B, or 0C profile and does not silently cross into a later stage.
- Broad structure, value hierarchy, gesture, and overlap make the Stage 4 proposition mentally visible without resolving it; strategic detail confirms presence rather than describing surface.
- The user can identify a candidate unambiguously by position.
- Only one selected and explicitly approved candidate becomes the Stage 0 root.

## Notes
Stage 0 is the model's widest creative search space. Multiple quick alternatives let generative dreaming contribute compositionally before continuity constraints narrow the field. When the camera is open, the artist's search includes moving around the imagined scene before choosing where to stand; four versions of one shot are not four compositions. The guarding function begins when the user selects a direction: later stages may unpack the skeleton, masses, surfaces, and finish already implied by that thumbnail, but they may not redesign the chosen container.

`VAR_hultgren_choose_viewpoint_from_dominant_mass_effect` adds Hultgren's effect-first camera route: choose the dramatic or bulk read before the camera, select the view that magnifies it, establish the principal pose from that view, then make the rest of the picture intensify the same effect. Use this only while Stage 0 viewpoint is still open.

`VAR_bammes_choose_viewpoint_to_reveal_distinctive_animal_form` adds Bammes's anatomy-study criterion: when the camera is open, choose the view that makes the animal's characteristic masses and plane relationships easiest to understand and depict. Three-quarter high or low views often expose more structure than direct views, but only when that serves the actual subject and assignment.

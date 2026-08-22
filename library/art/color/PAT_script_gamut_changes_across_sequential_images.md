---
object_id: PAT_script_gamut_changes_across_sequential_images
object_type: pattern
name: Script Gamut Changes Across Sequential Images
library_path:
- art
- color
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- color
- sequence
- color_script
- gamut
- narrative
cross_links:
- rel: related_to
  target_object_id: PAT_define_and_enforce_picture_gamut
- rel: related_to
  target_object_id: PAT_choose_color_strategy_to_fit_subject_purpose_and_viewing_context
reference:
  source_title: 'Color and Light: A Guide for the Realist Painter'
  author: James Gurney
confidence: high
variants:
- variant_id: VAR_gurney_ground_color_script_in_observed_daylight_sequence
  variant_name: Ground a Color Script in an Observed Daylight Sequence
  variant_basis: method_sequence
  difference_from_foundation: Uses a compact observational run across a real day as evidence for how large color masses and
    illumination states change before those relationships are compressed or transformed into a designed narrative script.
  when_to_use: Use when a sequence depends on believable time-of-day or changing-light progression and direct observation
    can supply stronger transition evidence than memory alone.
  when_not_to_use: Do not require the final narrative to reproduce the observed day literally; compress, exaggerate, reorder,
    or depart when story needs outweigh documentary continuity.
  absorbed_from_object_id: none
- variant_id: VAR_bleicher_drive_color_state_from_participant_input
  variant_name: Drive Color State From Participant Input
  variant_basis: method_sequence
  difference_from_foundation: Replaces one predetermined linear color sequence with a set or graph of reachable color states
    whose transitions are triggered by participant or environmental input, so the experience is designed around possible paths
    rather than one fixed order.
  when_to_use: Use for interactive or responsive visual experiences where movement, gaze, time, position, sensor values, or
    other inputs materially determine which color state appears next.
  when_not_to_use: Do not add branching state logic to a fixed sequence that will always be experienced in one order, and
    do not optimize isolated states while ignoring the transitions users can actually traverse.
  absorbed_from_object_id: none
references: []
---

# Script Gamut Changes Across Sequential Images

## Pattern Rule
**IF** images will be experienced in sequence and color change is part of the narrative or temporal effect
**THEN** lay the sequence out together in simplified color beats, assign each unit a controlled gamut, and design the changes in gamut location, width, and relationship across the sequence rather than optimizing each image independently
**ELSE** treat a standalone image with its own picture gamut.

## Do
- Reduce each beat to large color masses before detail so the sequence can be judged at a glance.
- Compare every gamut with its neighbors; a locally attractive frame can still weaken the overall progression.
- Use gradual shifts for continuity and abrupt gamut changes for meaningful cuts, environmental changes, or narrative shocks.
- Track where chroma, temperature bias, neutral, and dominant family move across the sequence.
- Recheck the entire script after changing one important beat so local improvements do not break the rhythm.
- For responsive experiences, design the reachable color states and transition paths together; map inputs to transitions and test continuity, contrast, and meaning along the paths users can actually take.

## Don't
- Choose each frame's palette in isolation.
- In an interactive sequence, optimize individual states while leaving reachable transitions visually incoherent or contradictory.
- Make every scene maximally different merely to prove that the script changes.
- Let color progression substitute for missing story or lighting logic.

## Checklist
- Consecutive beats have intentional relationships rather than accidental palette drift.
- Major color changes correspond to meaningful narrative, temporal, or environmental changes.
- The sequence remains legible as a color progression at thumbnail scale.
- For interactive variants, every important reachable transition has an intentional relationship rather than accidental state-to-state color shock.

## Notes
Sequential color design depends on change as much as on individual palettes. A color script makes those transitions visible early enough to design their rhythm rather than discovering it after finished images already exist.

`VAR_gurney_ground_color_script_in_observed_daylight_sequence` Uses a compact observational run across a real day as evidence for how large color masses and illumination states change before those relationships are compressed or transformed into a designed narrative script. Use it when when a sequence depends on believable time-of-day or changing-light progression and direct observation can supply stronger transition evidence than memory alone Avoid it when require the final narrative to reproduce the observed day literally; compress, exaggerate, reorder, or depart when story needs outweigh documentary continuity .

`VAR_bleicher_drive_color_state_from_participant_input` turns the linear script into a responsive state graph. Define the color states, map meaningful participant or environmental inputs to transitions, and judge the paths between states as carefully as the states themselves.

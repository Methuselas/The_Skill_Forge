---
object_id: PAT_use_perceptual_wrongness_as_inspection_trigger
object_type: pattern
name: Use Perceptual Wrongness as an Inspection Trigger
library_path:
- art
- drawing
- foundations
- observation
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- observation
- error_detection
- seeing
- diagnosis
- staged_drawing
cross_links: []
reference:
  source_title: Keys to Drawing
  author: Bert Dodson
confidence: high
references: []
variants:
- variant_id: VAR_dodson_restate_before_erasing_during_observational_search
  variant_name: Restate Before Erasing During Observational Search
  variant_basis: method_sequence
  difference_from_foundation: Places the improved relationship beside the doubtful one first, preserving visual contact and evidence of the search before cleanup removes the rejected mark.
  when_to_use: Use during exploratory observational drawing when frequent erasing would interrupt comparison with the subject.
  when_not_to_use: Do not accumulate so many competing lines that the current decision becomes unreadable; consolidate once the correction is understood.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_route_wrongness_through_five_ps_and_five_cs
  variant_name: Route Wrongness Through the Five Ps and Five Cs
  variant_basis: method_sequence
  difference_from_foundation: >-
    Adds Loomis's explicit ten-part routing audit after perceptual wrongness is detected.
    Five Ps: Proportion (the three dimensions), Placement (a position in space),
    Perspective (relationship of viewpoint to subject), Planes (surface appearance as
    defined by light and shadow), and Pattern (the deliberate arrangement of the tones
    of the subject). Five Cs: Conception (a rough indication of an idea), Construction
    (establishing forms from life or basic knowledge), Contour (the limits of forms in
    space according to viewpoint), Character (the specific qualities of individual units
    of the subject in light), and Consistency (construction, lighting, and pattern
    organized as a unit). Scan these categories, identify the earliest failed relationship,
    route to the owning correction method, then recheck the whole drawing.
  when_to_use: Use when the drawing feels wrong but the cause is unclear or several plausible causes compete.
  when_not_to_use: Do not turn the ten labels into a ritual checklist when the failure is already obvious; correct the known issue and return to whole-picture inspection.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_reduce_vague_failure_to_add_omit_and_four_visual_elements
  variant_name: Reduce Vague Failure to Add/Omit Errors and Four Visual Elements
  variant_basis: method_sequence
  difference_from_foundation: When representational work merely feels as though it is not working, first ask whether unsupported information was added or essential information omitted, then test drawing, value, edges, and color singly and in combination until the complaint becomes a concrete correction.
  when_to_use: Use when frustration is real but the current diagnosis is only emotional or metaphorical, such as dead, weak, flat, lifeless, or not working.
  when_not_to_use: Do not run the full elimination sequence when the failure is already obvious; correct the known relationship and recheck the whole image.
  absorbed_from_object_id: none
- variant_id: VAR_schmid_translate_abstract_composition_complaint_into_concrete_relations
  variant_name: Translate Abstract Composition Complaints Into Concrete Relations
  variant_basis: method_sequence
  difference_from_foundation: Converts labels such as unbalanced, no unity, no movement, or does not work into visible relations—an overweight mass, isolated region, premature exit path, competing shapes, or awkward interval—before routing to the owning correction.
  when_to_use: Use when a composition complaint names an effect but not the actual relation that must change.
  when_not_to_use: Do not invent a diagnostic vocabulary when the specific offending mass, path, interval, or hierarchy failure is already known.
  absorbed_from_object_id: none
---
# Use Perceptual Wrongness as an Inspection Trigger

## Pattern Rule
**IF** the whole drawing or a local relationship immediately looks wrong even before the cause is consciously identified
**THEN** stop advancing that part, inspect the visible relationships, and use the appropriate structural knowledge only to diagnose the mismatch before testing the correction with the eye again
**ELSE** continue while still performing normal stage checks

## Do
- Treat the first sense of wrongness as evidence that something deserves scrutiny rather than as proof of a specific diagnosis.
- Compare shape, angle, interval, alignment, proportion, overlap, support, and tone before deciding which structural tool is relevant.
- Return to the whole read after a local correction; a technically plausible fix can still fail perceptually.
- Apply the same inspection at meaningful stage gates so a correct procedure does not excuse a visibly wrong result.
- Treat significant known errors as urgent because later comparisons depend on the relationships already on the image; a wrong anchor can make correct later decisions look wrong and propagate error.
- Use anatomy, perspective, material, and other learned knowledge to generate diagnostic hypotheses, but let clear observed evidence overrule a remembered general rule when faithful observation is the task.

## Don't
- Do not rationalize a visibly implausible result merely because construction steps were followed.
- Do not let remembered symbols overwrite the particular projection actually observed.
- Do not assume the eye's alarm identifies the cause; perspective, anatomy, proportion, support, or another relationship may be responsible.

## Checklist
- The suspicious area has been inspected before further detail is added.
- A structural explanation supports the correction rather than replacing the visual check.
- The corrected result reads better both locally and as part of the whole.

## Notes
Dodson repeatedly shifts attention from named objects to the particular visual relationships in front of the artist. Guided teaching extended this into a stage-level error alarm: human vision often detects implausibility before conscious diagnosis, so perceptual wrongness should trigger inspection before the artist returns to anatomy, perspective, proportion, or other structural methods. `VAR_dodson_restate_before_erasing_during_observational_search` preserves the doubtful and improved relationships together long enough to compare them before cleanup.

`VAR_loomis_route_wrongness_through_five_ps_and_five_cs` supplies a broad routing audit when the alarm is real but the cause is unclear. The **Five Ps** are **Proportion, Placement, Perspective, Planes, and Pattern**. The **Five Cs** are **Conception, Construction, Contour, Character, and Consistency**. Use the framework to locate the failed relationship, not as a substitute for the specialized correction method that owns it.

`VAR_schmid_reduce_vague_failure_to_add_omit_and_four_visual_elements` turns a vague failure state into a bounded elimination search through unsupported additions, essential omissions, drawing, value, edges, and color. `VAR_schmid_translate_abstract_composition_complaint_into_concrete_relations` applies the same discipline to composition language by replacing labels such as imbalance or lack of movement with the specific mass, path, interval, or competition that can actually be edited.

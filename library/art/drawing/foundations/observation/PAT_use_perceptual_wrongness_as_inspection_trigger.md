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
  source_id: bert_dodson_keys_to_drawing
  source_title: Keys to Drawing
  author: Bert Dodson
  publish_date: 1985
  media_type: PDF
  locator: u01, physical pp. 9-40
  evidence_type: mixed
confidence: high
references: []
variants:
- variant_id: VAR_dodson_restate_before_erasing_during_observational_search
  variant_name: Restate Before Erasing During Observational Search
  variant_basis: method_sequence
  source_id: bert_dodson_keys_to_drawing
  source_title: Keys to Drawing
  locator: u01, physical pp. 9-40
  difference_from_foundation: Places the improved relationship beside the doubtful one first, preserving visual contact and evidence of the search before cleanup removes the rejected mark.
  when_to_use: Use during exploratory observational drawing when frequent erasing would interrupt comparison with the subject.
  when_not_to_use: Do not accumulate so many competing lines that the current decision becomes unreadable; consolidate once the correction is understood.
  absorbed_from_object_id: none
- variant_id: VAR_loomis_route_wrongness_through_five_ps_and_five_cs
  variant_name: Route Wrongness Through the Five Ps and Five Cs
  variant_basis: method_sequence
  source_id: andrew_loomis_successful_drawing
  source_title: Successful Drawing
  locator: u01, physical PDF pp. 6-7, 10-13
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

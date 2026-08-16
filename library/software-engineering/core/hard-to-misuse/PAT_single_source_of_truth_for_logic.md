---
object_id: PAT_single_source_of_truth_for_logic
object_type: pattern
name: Keep a Single Source of Truth for Logic
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- single_source_of_truth
- duplication
- hard_to_misuse
- decomposition
cross_links:
- rel: related_to
  target_object_id: PAT_decompose_into_layers_of_abstraction
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Keep a Single Source of Truth for Logic

## Pattern Rule
**IF** two pieces of code must perform matching logic — a format written by one and read by another, an encode paired with a decode
**THEN** extract that logic into one reusable layer both depend on, rather than duplicating it in each place, so the two cannot drift out of sync.

## Do
- Spot the shared subproblem: serializing a list of integers and deserializing it are two halves of one format, so both a logger and a loader depend on the same subproblem's solution.
- Put the logic in a single class both call — an `IntListFormat` with `serialize` and `deserialize` — so the storage format is defined once.
- Push the single-source-of-truth principle down to the details: define the delimiter and radix as constants used by both directions, so even those cannot mismatch.

## Don't
- Don't independently encode the same format in two classes; if one switches from base-10 to hexadecimal or from comma to newline and the other is not updated, reads silently break.
- Don't rely on engineers in different files noticing that a change in one place demands a matching change in another; they usually will not.

## Checklist
- Is any format or rule implemented in more than one place that must agree?
- Do the matching halves depend on one shared implementation rather than their own copies?
- Are shared constants (delimiters, radixes) defined once and reused?

## Notes
Duplicated logic is a second source of truth that drifts. Long's `DataLogger`/`DataLoader` pair each independently know the serialized-integer format, so a format change in one without the other corrupts the round trip. Extracting an `IntListFormat` layer that both share makes the format a single subproblem solved once — the chapter-2 decomposition idea applied to correctness, almost entirely removing the risk of two pieces of code getting out of sync.

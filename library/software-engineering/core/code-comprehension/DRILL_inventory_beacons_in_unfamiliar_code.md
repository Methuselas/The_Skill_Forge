---
object_id: DRILL_inventory_beacons_in_unfamiliar_code
object_type: drill
name: Inventory Beacons in Unfamiliar Code
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_comprehension
- beacons
- deliberate_practice
- code_review
cross_links:
- rel: teaches
  target_object_id: PAT_use_beacons_to_test_code_hypotheses
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
target_skill: noticing which code and natural-language signals unlock an unfamiliar function's meaning
references: []
variants: []
---

# Inventory Beacons in Unfamiliar Code

## Practice Task
Explain one function from an unfamiliar codebase while recording every code element or natural-language cue that materially advances your understanding.

## Target Skill
Recognizing the simple and compound signals used during comprehension and distinguishing domain knowledge from functional knowledge.

## Setup
Select one method or function in an unfamiliar codebase written in a language you know. If possible, arrange for someone familiar with the code to review your explanation.

## Instructions
1. Study the function and begin a one-sentence behavior summary.
2. Whenever an identifier, comment, operator, literal, intermediate value, or structure produces an "aha" moment, stop and record it verbatim.
3. For each item, state the hypothesis it supported or refuted and whether it represents domain or program-function knowledge. Keep the refutations on the list rather than dropping them.
4. Combine related simple items into any compound signals you used, and decompose one compound back into the simple items it was built from.
5. Finish the behavior summary and verify it with tests, callers, documentation, or a knowledgeable reviewer. Record what that check changed, including when it changed nothing.
6. Optionally improve a missing or misleading signal, checking the improvement against the codebase's existing conventions.

## Success Check
- Items are recorded verbatim as they land rather than reconstructed at the end. A list assembled afterwards keeps what turned out to matter and drops the signals that misled, which are the ones worth having.
- Every item names the hypothesis it supported or refuted, and at least one refutation appears. An inventory containing only confirmations describes the conclusion rather than the reading.
- The final summary is checked against something outside the reading — a test, a caller, documentation, a reviewer — and what that check changed is recorded, including when it changed nothing.
- Simple and compound signals are distinguished, and one compound is decomposed into the simple items it was built from.
- Any signal improved is checked against the codebase's existing conventions rather than personal preference, since a locally clearer name that disagrees with its neighbours costs more than it returns.

## Common Failures
- Listing every identifier instead of only the elements that changed understanding.
- Treating a suggestive name as proof without checking later behavior.
- Adding explanatory clutter after the exercise when the existing signals were already sufficient.

## Notes
Exercise 2.5 asks the reader to select unfamiliar code, notice each comprehension breakthrough, classify the knowledge it represents, and optionally contribute better signals. A knowledgeable peer is useful as a correctness check because a compelling beacon can still support the wrong explanation.

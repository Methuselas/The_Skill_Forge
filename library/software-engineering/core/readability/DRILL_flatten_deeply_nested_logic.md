---
object_id: DRILL_flatten_deeply_nested_logic
object_type: drill
name: Flatten Deeply Nested Logic With Early Returns and Extraction
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- nesting
- control_flow
- refactoring
- readability
cross_links:
- rel: teaches
  target_object_id: PAT_minimize_nesting_with_early_returns
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: removing deep control-flow nesting through guard clauses and function extraction
references: []
variants: []
---

# Flatten Deeply Nested Logic With Early Returns and Extraction

## Practice Task
Take a function with several levels of nested if-statements and rewrite it flat, extracting a sub-function where a plain early return would skip needed logic.

## Target Skill
Flattening nested control flow and recognizing when nesting means a function does too much.

## Setup
No special setup required.

## Instructions
1. Start from a function with three or more levels of nested if-else — for example one finding a vehicle owner's address through scrapyard, showroom, and buyer branches.
2. Where every branch ends in a return, rewrite each as an early-return guard clause so the remaining logic is not indented under an else.
3. Take a second function that both computes a value and acts on it (find the address, then send a letter), and confirm a naive early return would wrongly skip the action.
4. Extract the computing part into its own function, then flatten that function with early returns while the outer function calls it and handles the action.
5. Re-read both and confirm the nesting is gone and each function does one clear job.

## Success Check
- The nested original is written out before the rewrite so the levels removed can be counted rather than asserted.
- Every branch of the first function is confirmed to end in a return before the guard-clause rewrite, because that is the rewrite's precondition and the rewrite is wrong without it.
- The second function is shown breaking under a naive early return, with the skipped action named, before any extraction is made. This is the step the drill exists for, and a run that goes straight to extracting has demonstrated nothing about why extraction was needed.
- After extraction the outer function holds no guard of its own that could skip the action, and every early return in the inner function returns a value rather than abandoning work.
- Each function is given a one-line statement of its single job. A line needing "and" describes a function still doing two, whatever the indentation now looks like.

## Common Failures
- Early-returning out of a function whose branches must fall through to shared later logic, skipping it.
- Flattening the syntax but leaving a function that still does two jobs.

## Notes
This drills Long's paired refactors: the pure address-finder flattens directly with guard clauses, while the address-plus-letter function must be split first because an early return would skip the send. The transferable reflex is to try guard clauses, and when they do not fit, read that as a sign to extract a sub-function.

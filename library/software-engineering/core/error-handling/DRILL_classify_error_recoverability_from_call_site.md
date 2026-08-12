---
object_id: DRILL_classify_error_recoverability_from_call_site
object_type: drill
name: Classify an Error's Recoverability From Each Call Site
library_path:
- software-engineering
- core
- error-handling
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- recoverability
- error_handling
- api_design
- analysis
cross_links:
- rel: teaches
  target_object_id: PAT_classify_error_recoverability_by_caller
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u04, pp. 68-70
  evidence_type: text
confidence: high
target_skill: judging whether an error is recoverable based on the calling context
references: []
variants: []
---

# Classify an Error's Recoverability From Each Call Site

## Practice Task
Take one error-producing function and several call sites, and decide for each whether the error is recoverable or a fatal programming error.

## Target Skill
Reading recoverability from the calling context rather than from the error alone.

## Setup
No special setup required.

## Instructions
1. Pick a function that can fail on bad input — for example one that parses a phone number and errors on an invalid string.
2. Write two or more call sites: one passing a hard-coded literal, one passing user-supplied input, and if you like one passing a value from another system.
3. For each call site, decide whether the failure is recoverable (external cause the system should handle gracefully) or unrecoverable (a programming mistake).
4. Justify each decision by where the value originates and whether any caller could sensibly act on the failure.
5. State what the function's author should therefore assume, given they cannot see all call sites — and note the rare exception where the contract makes the input obviously invalid and cheaply checkable.

## Success Check
- Each call site is labeled recoverable or unrecoverable with the origin of its value named.
- The hard-coded-literal case is identified as a programming error and the user-input case as recoverable.
- You conclude the author should default to "caller might recover" absent complete call-site knowledge.

## Common Failures
- Judging recoverability from the error type instead of the calling context.
- Assuming an input is obviously invalid to everyone when the rule is buried in the contract's small print.

## Notes
This drills the phone-number analysis: the identical parse failure is fatal from `"01234typo56789"` and recoverable from user input. The habit it builds is to trace each value to its origin before deciding how to treat its errors, and to default to recoverable whenever the call sites are not fully known.

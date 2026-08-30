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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
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
- Each call site is written as code and labelled, with the origin of its value named. A verdict without the origin cannot be checked by anyone else.
- At least three origins are covered, including one that looks internal and is not — a value from this system's own storage, which may have been written by an earlier version, a migration, or another process. The literal and the user input are the easy pair, and the drill turns on the third.
- The author's default is stated as a consequence of not knowing the call sites rather than as a preference, and the signalling technique that expresses it is named.
- The exception is bounded rather than merely acknowledged: a condition is given under which failing loudly is fair, together with a case that resembles it and is not.
- The run states what changes when this function ships as a library, since its author has strictly less call-site knowledge and the same default therefore binds harder.

## Common Failures
- Judging recoverability from the error type instead of the calling context.
- Assuming an input is obviously invalid to everyone when the rule is buried in the contract's small print.

## Notes
This drills the phone-number analysis: the identical parse failure is fatal from `"01234typo56789"` and recoverable from user input. The habit it builds is to trace each value to its origin before deciding how to treat its errors, and to default to recoverable whenever the call sites are not fully known.

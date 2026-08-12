---
object_id: DRILL_refactor_error_hiding_code_to_signal
object_type: drill
name: Refactor Error-Hiding Code to Signal the Error
library_path:
- software-engineering
- core
- error-handling
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- error_handling
- refactoring
- avoid_surprises
- robustness
cross_links:
- rel: teaches
  target_object_id: PAT_dont_hide_errors
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u04, pp. 75-79
  evidence_type: text
confidence: high
target_skill: spotting hidden errors and replacing them with explicit signaling
references: []
variants: []
---

# Refactor Error-Hiding Code to Signal the Error

## Practice Task
Take functions that hide errors — via default values, empty collections, doing nothing, or swallowed exceptions — and refactor each to signal the error to its caller.

## Target Skill
Recognizing the disguises of a hidden error and converting them to explicit signals.

## Setup
No special setup required.

## Instructions
1. Collect examples of each disguise: a balance lookup returning `0.0` on failure, an invoice query returning an empty list on failure, an `addItem()` that silently returns on a currency mismatch, and a send function that catches and drops an exception.
2. For each, name the concrete bug it causes — a real zero balance is indistinguishable from an error, an audit sees no unpaid invoices, a caller believes an item was added, a caller believes an email was sent.
3. Refactor each to signal the error explicitly, choosing a technique that puts the failure in the unmistakable contract (a result type, a nullable return, or an enforced outcome).
4. Update one caller of each to handle the signaled error — for instance, showing "we can't access this right now" instead of a wrong value.
5. Check that no refactored function can still return a value indistinguishable from a genuine result, and that no catch block silently swallows or merely logs.

## Success Check
- Each function now signals failure rather than returning a plausible-looking success.
- At least one caller per case handles the error visibly to the user or system.
- No remaining return value conflates an error with a legitimate normal result.

## Common Failures
- "Fixing" a swallowed exception by only logging it, which still hides the failure from the caller.
- Replacing one hidden error with another, such as swapping a default value for an empty collection.

## Notes
These are Long's error-hiding listings turned into a repair exercise. The transferable reflex is to distrust any error path that returns a normal-looking value or quietly catches, and to route the failure into a channel the caller cannot miss — the same move whether the disguise is a default, an empty list, silence, or a swallowed exception.

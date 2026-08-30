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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
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
- Each disguise is run before the change with the wrong behaviour recorded — what was returned, and what the caller then did with it. Naming the bug is what the hidden error already allowed.
- Each refactored function is checked against the substitution this exercise invites: the failure must not be re-encoded as another plausible value, and the run states what each now returns for the failing case.
- At least one caller per case handles the failure visibly outside the program, and what a user or an operator would see is written down.
- A catch that only logs counts as unfixed, and any surviving catch is named along with what it does besides logging.
- Where a discard is genuinely correct — a failure the contract says cannot occur, or one raised while unwinding an already-failed operation — it is identified as such and the original failure is shown surviving. A run that signals everything has replaced one error with a noisier one.

## Common Failures
- "Fixing" a swallowed exception by only logging it, which still hides the failure from the caller.
- Replacing one hidden error with another, such as swapping a default value for an empty collection.

## Notes
These are Long's error-hiding listings turned into a repair exercise. The transferable reflex is to distrust any error path that returns a normal-looking value or quietly catches, and to route the failure into a channel the caller cannot miss — the same move whether the disguise is a default, an empty list, silence, or a swallowed exception.

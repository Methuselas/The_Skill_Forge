---
object_id: DRILL_fold_an_unsafe_interface_into_transactions
object_type: drill
name: Fold an Interface Whose Operations Do Not Compose
target_skill: Redesigning an operation set so no caller must hold a result across two calls
library_path:
- software-engineering
- core
- concurrency
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- interface_design
- contracts
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_make_every_concurrent_operation_a_complete_transaction
- rel: related_to
  target_object_id: PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Fold an Interface Whose Operations Do Not Compose

## Practice Task
Take a shared collection offering separate emptiness, inspection, and removal operations — each individually safe — and redesign the operation set so that no caller has to establish anything by a previous call.

## Target Skill
Redesigning an operation set so no caller must hold a result across two calls.

## Setup
No special setup required.

## Instructions
1. Write out a caller that uses the operations in the natural sequence: check whether anything is there, look at it, take it.
2. Describe an interleaving in which every individual operation succeeds and the sequence is still wrong. Name the exact moment the caller's assumption stopped holding.
3. Identify which contiguous group of calls the caller intended as one unit. That group, not its parts, is the operation to provide.
4. Replace the group with a single operation, and choose how it reports the case that used to be a precondition — an optional result, a value-and-flag pair, or a boolean with an out-parameter.
5. Check every remaining operation against the same test: does its validity depend on something the caller established earlier? Fold any that do.
6. State what a caller can now observe mid-change, and confirm no intermediate arrangement is reachable through the interface.

## Success Check
- No operation's contract requires a fact the caller obtained from a previous call.
- The case that was formerly a precondition is now an ordinary return value.
- The failing interleaving from step 2 can no longer be constructed against the new interface.

## Common Failures
- Adding a lock around the existing operations, which makes each safe again without making the sequence safe.
- Preserving the familiar operation set out of habit, when writing the wrapper was already the opportunity to change it.
- Folding the query into the action but leaving the result unable to express absence, so the caller is back to checking first.
- Overlooking that a returning operation now removes before it hands back, and saying nothing about what happens if handing back fails.

## Notes
This is the interface half of thread safety and it is decided before any synchronization is chosen: which sequences are transactions determines what the operations are. A design that adds guarding to a finished interface has answered the question in the wrong order, and the symptom is exactly this — every operation safe, every useful sequence not.

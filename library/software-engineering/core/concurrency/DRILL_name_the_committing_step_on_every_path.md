---
object_id: DRILL_name_the_committing_step_on_every_path
object_type: drill
name: Name the Committing Step on Every Path
target_skill: Locating the instant an operation takes effect, separately for each outcome
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
- correctness
- review
- lock_free
cross_links:
- rel: related_to
  target_object_id: PAT_give_every_operation_one_instant_where_it_takes_effect
- rel: related_to
  target_object_id: PAT_specify_a_concurrent_object_as_a_sequential_object_plus_a_correctness_condition
reference:
  source_title: The Art of Multiprocessor Programming
  author: Maurice Herlihy, Nir Shavit, Victor Luchangco, Michael Spear
confidence: high
references: []
variants: []
---

# Name the Committing Step on Every Path

## Practice Task
Take a shared structure whose operations are not each wrapped in a single critical section — a queue guarded at each end separately, or a stack updated by one conditional write — and write down, for every operation and every way it can finish, the one step at which it becomes visible to everyone else.

## Target Skill
Locating the instant an operation takes effect, separately for each outcome, and recognizing an operation that has none.

## Setup
No special setup required.

## Instructions
1. List every operation the structure offers, including the ones that only read.
2. For each operation, list its distinct outcomes — found and not found, removed and empty, added and full. Treat each as its own path.
3. For each path, name the single step where the effect becomes observable. State it as a specific line or operation, not as a region.
4. Test each candidate: describe what an observer sees immediately before that step and immediately after. If the operation is partly done in the "before" picture, you have the wrong step.
5. Mark any path where you cannot name one step, and say why — the effect appears in stages, or the step belongs to a different thread.
6. For each read-only operation, say at which step the value it reports was true.

## Success Check
- Every operation has at least one committing step written down, and operations with several outcomes have one per outcome.
- Each step is named as a specific line or operation, and no step named is the operation's return.
- For at least one mutating path, a candidate step is written down and rejected, along with the observation that disqualified it — what an observer sees between that step and the real commit.
- Any path lacking a single step is identified as a design defect rather than left blank.

## Common Failures
- Giving one answer per operation and missing the empty or not-found path, which is where the interesting defects live.
- Naming the operation's return rather than its commit, when the effect was already visible several steps earlier.
- Skipping the read-only operations on the grounds that they change nothing, which is exactly where a missing instant hides.
- Accepting a region — "somewhere inside the lock" — when the lock no longer covers the whole operation.

## Notes
The value of this exercise is diagnostic more than probative. Most of the time the step is found immediately, and the useful outcome is the case where it cannot be: an effect that becomes visible in stages is a defect that testing is poorly equipped to find, and this is the cheapest way to surface it. Run it again after any change to an operation, because a fast path or a hoisted read moves the step without looking dangerous.

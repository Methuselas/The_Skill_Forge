---
object_id: AP_refactor_working_code_safely
object_type: ap
name: Refactor Working Code Without Breaking It
library_path:
- software-engineering
- core
- refactoring
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- refactoring
- maintenance
- verification
- discipline
cross_links:
- rel: related_to
  target_object_id: PAT_separate_structural_change_from_behavioural_change
- rel: related_to
  target_object_id: PAT_judge_change_risk_by_what_it_can_break
- rel: related_to
  target_object_id: PAT_treat_compiler_warnings_as_potential_bugs
- rel: related_to
  target_object_id: AP_build_a_routine_from_intent_level_pseudocode
- rel: related_to
  target_object_id: PAT_prepare_for_interruption_before_it_arrives
- rel: related_to
  target_object_id: PAT_prove_behaviour_held_by_running_both_paths
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Refactor Working Code Without Breaking It

## Objective

Take a section of working code from its current shape to a better one without any caller noticing, and without reaching a state where you can neither finish nor go back. The orchestration is the whole technique: each individual move here is unremarkable, and it is doing them in this order — with a verified, returnable state between every pair of them — that separates refactoring from opening a working system and hoping.

Reach for this whenever the change is meant to preserve behaviour. Where the code does not currently work, or where the pass will alter what callers observe, this is the wrong procedure and the risk it manages is not the risk you have.

Before step 1, settle two separate questions about the tests, because the whole procedure rests on their answers and neither is checked anywhere inside it. Does coverage exist for the code you are about to move — which is a matter of opening the test file and looking — and is what exists adequate, which it is not merely because a percentage is high. Thin coverage does not stop the work; it relocates the safety into the review and tells you to write tests first, and knowing which of those you are doing is the difference between a procedure and a hope.

## Steps / Flow

1. **Make the starting state recoverable, and confirm it.** Commit what you have or copy the files somewhere you can find them. This is cheap and it is the step that determines whether a session that goes wrong costs you an afternoon or a day, because the failure mode is not noticing you are lost until several transformations after the one that lost you.

2. **Write the list of steps before making any of them.** A refactoring is a route from a shape you have to a shape you want, and the intermediate moves are what you will forget under pressure. Listing them is the same move as designing a routine in English before coding it, applied to a change instead of to new code, and it does the same job: it keeps each transformation in the context of where the whole thing is going.

3. **Size each step so you can hold its full effect in your head.** What counts as "one refactoring" is genuinely fuzzy at the edges, and the operative test is not a line count but whether you can state everything this move touches. A step you cannot fully account for is two steps.

4. **Do exactly one, then recompile and retest.** This is the step that people skip and it is the one carrying the guarantee. With a verification between every pair of transformations, a failure identifies the transformation that caused it; batched, a failure identifies only the batch. Set the compiler to its pickiest warning level first, so the errors it can catch surface as you type rather than after four more moves.

5. **Park what you find instead of chasing it.** Midway through one refactoring you will see a second worth doing, and midway through that a third. Keep a parking lot — a written list of changes worth making that do not need making now — and return to step 4. The parking lot exists because the alternative is a call stack of half-finished transformations with no working state anywhere in it.

6. **Checkpoint at intervals, not only at the start.** Save a returnable state at points through the session, so that coding yourself into a dead end costs you the last few moves rather than all of them.

7. **Add tests for the new shape, and retire the ones the change made meaningless.** Retesting with the old cases proves behaviour was preserved; that is what they are for and it is why they were not rewritten first. New unit tests then cover the structure that now exists, and test cases the refactoring made obsolete get removed rather than left to rot.

8. **Scale the review to what the change can reach, then close the session.** Mechanical local changes can be batched and simply retested. Interface changes, schema changes, and changes to boolean tests get a reviewer or a pair, on top of the compiler and the tests. Before closing, ask the question the whole procedure exists to serve: is the program's internal quality better than when you started, or merely different?

## Notes

The ordering carries the technique, which is why this is a procedure rather than a list of good habits. Steps 1, 4, and 6 are all the same idea at different scales — there is always a recent state you can return to — and removing any one of them breaks the others' value. Step 5 exists to protect step 4 from the specific way refactoring sessions fail, which is not a bad transformation but an accumulation of unfinished ones.

Step 7 depends on something outside this procedure and will not save a codebase that lacks it. Retesting proves behaviour was preserved only to the extent that the tests described the behaviour in the first place; against a thin suite it proves that the thin suite still passes. Where the tests are weak, the review in step 8 is doing more of the work than it looks like, and the honest response is to raise the review effort rather than to trust a green bar that was never checking much.

That weakness has a second answer once the surface is large enough that no achievable suite would cover it. Rather than certifying the change against tests, certify it against the traffic — keep both implementations executing, compare their results on live input, and switch which one answers only after the differences are accounted for. It is a far heavier arrangement than this procedure and it is the wrong tool for a session of ordinary restructuring, but it is the available option when the code is old, the coverage is thin, and the volume is high enough that production is a better specification than anything anyone would sit down and write.

The counterintuitive input to step 8 is that small changes are not the safe ones. Programmers have better than a fifty percent chance of erring on a first attempt at a change, and measured error rates *peak* at around five lines changed. That is why the streamlining permitted for easy refactorings is defined by what the change can reach and never by how little of it there is.

Refactoring has a good deal in common with fixing a defect and with tuning code for performance: all three modify working code, and all three are usually done under some pressure to finish. The risks are the same shape and so are the countermeasures.

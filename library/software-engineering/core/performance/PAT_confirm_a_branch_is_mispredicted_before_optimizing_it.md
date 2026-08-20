---
object_id: PAT_confirm_a_branch_is_mispredicted_before_optimizing_it
object_type: pattern
name: Confirm a Branch Is Mispredicted Before Optimizing It
library_path:
- software-engineering
- core
- performance
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- profiling
- hardware
- branches
- measurement
cross_links:
- rel: related_to
  target_object_id: PAT_read_a_profile_as_a_statement_about_machine_code
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: prerequisite_for
  target_object_id: PAT_trade_a_branch_for_unconditional_work
- rel: related_to
  target_object_id: PAT_treat_a_compound_condition_as_several_branches
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Confirm a Branch Is Mispredicted Before Optimizing It

## Pattern Rule
**IF** you suspect a conditional is what makes a hot section slow
**THEN** establish two things by measurement before changing anything — that the compiled code branches there at all, and that the branch is actually being mispredicted
**ELSE** where the section contains no conditional whose outcome varies with the data, the cost is somewhere else and this line of investigation is finished.

## Do
- Take the whole-run counter summary first, because it is one command and it either indicts or clears the whole hypothesis. A branch-miss rate around eleven percent of all branches is severe — that figure includes every perfectly predicted loop-end check, which dilutes it — while a well-behaved program in the same harness reported under a tenth of a percent.
- Localize with a profile keyed to the branch counters rather than to time. Recording branch and branch-miss events attributes mispredictions to functions and lines the same way a time profile attributes cycles, and in practice they concentrate hard: over ninety-nine percent of one program's mispredictions sat in a single function.
- Read the generated code before believing there is a branch. Processors have conditional-move and masked arithmetic instructions, and a compiler that uses one for your conditional expression has produced straight-line code that pipelines perfectly — the branch you are looking at exists only in the source.
- Give the predictor credit for more than a constant. It learns per call site, so the same condition can be predicted correctly in a function called from two places with opposite behaviour, and it detects patterns in the data — a strictly alternating true/false sequence predicts nearly perfectly.
- Calibrate what a misprediction is worth before deciding it is worth fixing. A well-predicted branch costs almost nothing; one mispredicted half the time can cost the equivalent of ten or more arithmetic instructions, and a loop built around a random condition ran roughly five times slower than the straight-line version of the same work.
- Build the test so the compiler cannot resolve the condition. A condition that is constant at compile time is deleted along with the unreachable side, so a benchmark meant to exercise prediction needs a condition derived from data the compiler cannot see through.

## Don't
- Don't guess at prediction rates. Intuition about performance is unreliable generally and speculating about what a branch predictor learned is worse — the mechanism is history-based, adaptive, and specific to the machine.
- Don't read a slow function containing an `if` as evidence about branches. Slowness has many causes, and the counters distinguish them in one run.
- Don't assume a branch inside a loop is the branch that matters. Every loop carries a hidden end-of-loop conditional, and it is predicted almost perfectly for any loop with many iterations — the interesting misprediction is the data-dependent one.
- Don't treat a low overall miss rate as clearing a specific hot loop. The rate is diluted by all the well-predicted branches in the program, so a small percentage can still be one loop missing constantly.

## Checklist
- What does the whole-run branch-miss rate say?
- Which function do the mispredictions concentrate in?
- Does the generated code actually contain a conditional jump there, or a conditional move?
- Is the condition data-dependent at run time, or resolvable by the compiler?
- Is the measured miss rate high enough to account for the time you are trying to explain?

## Notes
The reason to check the object code rather than the source is that the branch is a property of the compiled program. Compilers vary in whether they implement a conditional expression as a jump, and vector instruction sets provide masked operations that make some conditional work entirely branch-free. A transformation aimed at a branch that the compiler already removed buys nothing and costs readability.

The mechanism behind the cost explains why prediction quality matters more than branch count. To keep its execution units busy, the processor runs ahead into instructions it has not yet confirmed it will need, guessing each conditional from that branch's history and holding the unconfirmed results — including memory writes and even faults — pending. A correct guess costs nothing. A wrong one means discarding the speculative work, fetching the other path, and restarting: a pipeline flush.

There is a consequence of speculation that is startling and mostly not actionable, worth knowing so it does not become a mystery later. The processor genuinely does perform work on the path it guessed, including reading memory past the end of an array or dereferencing a pointer that the not-yet-evaluated condition would have shown to be null, and then discards the consequences. Ordinary code is unaffected because faults are held pending exactly like unconfirmed writes.

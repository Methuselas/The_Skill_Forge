---
object_id: PAT_get_the_single_threaded_version_working_first
object_type: pattern
name: Get the Single-Threaded Version Working First
library_path:
- software-engineering
- core
- concurrency
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- concurrency
- threading
- debugging
- testing
- separation_of_concerns
cross_links:
- rel: related_to
  target_object_id: PAT_keep_thread_aware_code_away_from_thread_ignorant_code
- rel: related_to
  target_object_id: PAT_run_threaded_code_under_conditions_built_to_break_it
- rel: related_to
  target_object_id: PAT_diagnose_source_of_code_confusion
reference:
  source_title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
  author: Robert C. Martin, with Brett L. Schuchert
confidence: high
references: []
variants: []
---

# Get the Single-Threaded Version Working First

## Pattern Rule
**IF** you are about to debug something that misbehaves and also runs across several threads
**THEN** establish that the logic is correct with one thread before investigating anything to do with ordering, so that you are never chasing two categories of fault at once
**ELSE** where the trouble exists only because of the coordination — a lost update, a hang, a value that appears from nowhere — the one-thread run will pass, and that result is itself the finding.

## Do
- Exercise the underlying computation on its own, driven directly rather than through whatever schedules it. Anything producing a wrong answer alone will produce wrong answers in company, and there it will look like a timing problem.
- Build the system so this is available. Logic reachable only through the scheduling machinery cannot be checked apart from it, and the separation has to exist before the moment you need it.
- Take a clean solo run as a real result rather than a formality. With the whole category of ordinary logic errors eliminated, what remains is about ordering — which tells you where to look and which techniques apply.
- Order the work the same way when building, not only when debugging. Get the computation right, then introduce the coordination, so the two are never being stabilised together.
- Watch for a symptom that changes character between the two runs. Something wrong consistently alone and intermittently in company is usually a plain fault that the threading is making harder to see.

## Don't
- Don't pursue an ordering hypothesis while the plain logic is unverified. Both produce wrong values and unexpected state, so neither investigation yields a conclusive result while the other is open.
- Don't assume a fault concerns threads merely because threads are present. Their presence makes every bug look like a timing bug, and most bugs in a threaded system are ordinary ones.
- Don't skip the check because the logic is obviously right. That is where it costs the least and occasionally pays the most.
- Don't leave the computation reachable only through the scheduling. That forecloses your cheapest diagnostic permanently, in exchange for nothing.

## Checklist
- Can the computation be driven with no coordination involved at all?
- Has it been run that way, and did it produce right answers?
- Are you currently explaining by ordering something never verified alone?
- Does the symptom differ between the solo and concurrent runs, and how?
- Was the computation stabilised before the coordination arrived, or alongside it?

## Notes
The value is in separating two search spaces that otherwise multiply together. Ordinary faults are found by reasoning about what code does; ordering faults are found by reasoning about what several copies of it do simultaneously, which is a far larger and less tractable space. Investigating both at once makes every observation ambiguous — a wrong value might be a mistake in the arithmetic or a lost update, and seeing it does not distinguish them. Emptying one space makes every subsequent observation informative.

The asymmetry in cost is what fixes the order rather than leaving it to taste. Checking the computation alone is fast, repeatable, and either clears an entire category or finds a bug that would have been miserable to locate among threads. Investigating ordering is slow, needs deliberately hostile conditions, and yields probabilistic results even when done well. Spending the cheap check first is nearly free and can remove the need for the expensive one.

The demand this places on the design has to be honoured early to be honoured at all. A solo run of the logic is possible only if that logic sits somewhere callable directly, without passing through whatever creates and schedules threads. Where the computation is written inside the coordinating code, the cheapest diagnostic simply does not exist, and recovering it means restructuring at precisely the worst moment — while something is already failing intermittently and nobody yet knows why.

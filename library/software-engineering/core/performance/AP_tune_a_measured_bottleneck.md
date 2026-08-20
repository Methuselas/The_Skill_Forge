---
object_id: AP_tune_a_measured_bottleneck
object_type: ap
name: Tune a Measured Bottleneck
library_path:
- software-engineering
- core
- performance
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- optimization
- measurement
- iteration
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_level_before_tuning_the_code
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: AP_refactor_working_code_safely
- rel: related_to
  target_object_id: PAT_separate_structural_change_from_behavioural_change
- rel: related_to
  target_object_id: AP_locate_a_performance_bottleneck_by_measurement
- rel: related_to
  target_object_id: PAT_name_the_binding_constraint_before_choosing_a_remedy
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Tune a Measured Bottleneck

## Objective

Take a program that is correct but too slow and make it fast enough, without discovering afterwards that you spent the effort in the wrong place, kept a change that made things worse, or traded away more clarity than the gain was worth. The procedure exists because performance work has an unusually bad ratio of confident beliefs to true ones, so almost every step here is a checkpoint against your own judgment rather than a construction step.

Reach for this only once the program works and the earlier levels have been cleared. If the problem is a requirement nobody needed, a design that cannot go fast, or an algorithm choice, no amount of this will reach it.

## Steps / Flow

1. **Build it well first, and treat that as step one of the performance work rather than a prerequisite to it.** Well-designed code that is easy to understand and modify is the best preparation for tuning: it is what lets you find the hot spot, change it safely, and put the change back if it does not pay. Code that was written fast and tangled in anticipation of being fast is harder to tune, not easier.

2. **Save a working version you can return to.** Everything after this assumes a last known good state exists. Given how many attempts will be reverted, this is the step that makes the rest affordable rather than a formality.

3. **Measure to find the hot spots.** Profile rather than reason. Most programs spend most of their time in a small fraction of their code, and you will not know which fraction until you look — one team made an operating system's inner loop ten times faster and changed nothing at all, because it was the idle loop.

4. **Decide whether code tuning is even the right answer, and be willing to leave.** Weak performance often comes from the design, the data types, or the algorithms, and if it does, go back to step 1 and fix it there. This is the step that distinguishes the procedure from a tuning reflex, and skipping it is how a project ends up hand-optimizing arithmetic that a different design would have removed.

5. **Name what is limiting this code before choosing what to change.** Whether the region is stalled on memory traffic, on a mispredicted branch, on its own dependency chain, or is simply executing a great deal of work decides which techniques are even applicable — and they are not interchangeable, so a remedy picked by familiarity usually addresses a constraint this code does not have. *Advance when* the classification accounts for the time you are trying to explain.

6. **Tune the one bottleneck you identified.** Change the expensive operation for a cheaper one, drawn from the family the classification pointed at. Keep the change small enough to attribute a result to.

7. **Measure the improvement, one change at a time.** A batch of changes yields one number that belongs to no particular change, which is worthless given how many of them will turn out to be neutral or harmful.

8. **Revert anything that did not earn its place.** More than half of attempted tunings produce only negligible improvement or actively degrade performance, so removal is the expected outcome rather than an admission. Code that is less readable and no faster is a pure loss and there is no reason to keep it.

9. **Iterate on the same hot spot before moving to the next one.** The first optimization that works is often not the best one available, and the gap can be large — one routine gained 30 to 40 percent from its first tuning and then far more from the second and third attacks on the same code. So do not treat a successful change as the end of that bottleneck. Only once the returns there have flattened should you profile again and go after the hot spot that has now surfaced.

10. **Accumulate, because that is where the large gains live.** You will rarely get a tenfold improvement from a single technique, but techniques combine: one implementation went from twenty-one minutes forty seconds to twenty-two seconds through a dozen individually modest changes, no three or four of which would have met the goal.

11. **Escalate to a lower-level language only at the end, and only for small pieces.** The order is fixed: write the whole application in the high-level language, test it and establish that it is correct, profile it, and only then recode the few small hot pieces. Since a few percent of a program accounts for most of its running time, those pieces are usually small enough to translate, and a rudimentary translation can be worth a large fraction on its own. Starting in the low-level language inverts every step above it.

## Notes

Step 9 is the one most often skipped, and skipping it is expensive in a specific way: a change that worked feels like a finished job, so the code keeps a modest gain and the larger one available on the same lines is never found. The related observation is that a failed attempt does not condemn its neighbourhood either — a tuning that produced nothing in one form has repeatedly worked in a near-identical form, so "this did not help" is a fact about that attempt rather than about the hot spot.

Steps 2, 7, and 8 form the loop that carries the value, and they are the ones under pressure to be skipped when a change obviously helps. The base rate is what justifies keeping them: in the aggressive tuning effort behind the twenty-one-minutes-to-twenty-two-seconds figure, at least two-thirds of the attempted optimizations did not work, and some doubled the run time. A process that assumes its changes are improvements will keep those.

This is nearly the same shape as refactoring safely, and the resemblance is not a coincidence — both modify working code under some pressure to finish, both need a returnable state and a verification between steps, and both fail the same way when several changes are made before anything is checked. The difference worth holding is what the verification proves. Refactoring retests to show behaviour did *not* change; tuning measures to show performance *did*. A tuning pass still has to preserve behaviour, so it inherits the refactoring discipline on top of this one rather than replacing it.

The cost side should be stated plainly because this procedure does not remove it. Aggressively tuned code is frequently the least readable code its author has ever written, and that relationship between tuning and code quality generally holds. The procedure keeps the cost proportional — paid only on the small fraction of code that measurement identified, and taken back whenever the measurement fails to justify it — but it never makes the cost zero, which is why step 4's willingness to leave matters as much as any of the tuning steps.

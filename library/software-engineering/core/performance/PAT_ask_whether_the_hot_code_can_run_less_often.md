---
object_id: PAT_ask_whether_the_hot_code_can_run_less_often
object_type: pattern
name: Ask Whether the Hot Code Can Run Less Often
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
- optimization
- profiling
- design
- tuning
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_level_before_tuning_the_code
- rel: related_to
  target_object_id: PAT_estimate_the_order_before_you_run_it
- rel: prerequisite_for
  target_object_id: AP_locate_a_performance_bottleneck_by_measurement
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Ask Whether the Hot Code Can Run Less Often

## Pattern Rule
**IF** measurement has identified the code where the program spends its time and you are choosing what to do about it
**THEN** settle whether the call count can come down before you try to lower the cost per call, because those are two independent routes to the same reduction and only one of them is usually considered
**ELSE** where the computation is required, already performed once per result, and the result is needed, the cost per call is the only route left and the question has been answered.

## Do
- Get the call count into the picture, since the profile alone will not supply it. A profiler reports where time was spent and most will count calls; it will not count loop iterations or tell you which branch of a conditional was taken, so pair the profile with instrumentation that records how often the expensive path is entered.
- Look one level up from the hot line before touching it. A loop whose profile is dominated by memory allocation raises the question of whether the loop must allocate and release on every iteration at all, and that question is answered outside the allocator.
- Treat "a different algorithm" as one of the two answers, not as a separate discipline. A comparison function consuming 98% of a sort's run time can be made cheaper or can be called fewer times, and calling it fewer times means choosing a different sort — which may still be the cheaper change to make.
- Use the caller breakdown to aim the question. When a hot function has several callers, the call-count reduction is usually available at one of them rather than in the function, and the call graph is what shows which one carries the volume.
- Take the reduction where the count is structural rather than incidental. Work that was cheap when a collection held ten elements and became the dominant cost when it held thousands is a volume problem wearing the costume of a slow function.

## Don't
- Don't go straight to making the function faster because that is the question the profile appears to ask. The report names a function and invites you to open it; the count of calls into it is nowhere on the screen, which is precisely why the second route gets forgotten.
- Don't accept a per-call improvement as the finished job when the call count is still open. A faster function called the same excessive number of times leaves the larger reduction unclaimed and makes the code harder to read on the way.
- Don't confuse this with avoiding the work entirely at a higher level. This is about the frequency of a computation that has already been established as necessary somewhere; whether the feature needed doing at all is a different and earlier question.

## Checklist
- How many times does this code run per unit of user-visible work?
- Which caller contributes most of those calls?
- Is anything being recomputed per iteration that could be computed once outside the loop?
- Would a different algorithm change the count rather than the cost?
- If the count came down by half, would that beat the per-call improvement you were about to attempt?

## Notes
The asymmetry this corrects is one of attention rather than knowledge. Everyone knows a total is a product of a rate and a count, and the profile displays only the rate; the fix that is visible is the one that gets tried.

The two routes also differ in what they cost the codebase. Lowering per-call cost usually means specialised, less readable code that has to be re-justified after every toolchain change. Lowering the call count is often a structural change — hoisting an invariant, reusing a buffer, choosing a different traversal — that leaves the code no worse to read and sometimes better.

This question fits between locating the bottleneck and tuning it. It comes after measurement has pointed at real hot code, so it is not a reason to restructure on suspicion, and it comes before the tuning loop, so it is not a late-stage rescue for a tuning pass that failed to pay.

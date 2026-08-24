---
object_id: AP_locate_a_performance_bottleneck_by_measurement
object_type: ap
name: Locate a Performance Bottleneck by Measurement
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
- measurement
- profiling
- benchmarking
- diagnosis
cross_links:
- rel: related_to
  target_object_id: AP_tune_a_measured_bottleneck
- rel: supports
  target_object_id: PAT_name_the_performance_metric_before_you_optimize
- rel: supports
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: supports
  target_object_id: PAT_choose_the_level_before_tuning_the_code
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Locate a Performance Bottleneck by Measurement

## Objective

Take a program that works but misses its performance target, and end up holding two things: the specific code responsible, and a candidate change whose benefit has been demonstrated on the complete program rather than in a harness. Success is the confirmation on the real program — a candidate that only wins in isolation has not completed this action.

This ends where changing the code begins. The discipline for making, measuring, reverting, and iterating the change itself belongs to `AP_tune_a_measured_bottleneck`, which this feeds.

## Steps / Flow

**Entry state.** The program is correct and complete, and there is a named metric with a target on it — throughput, turnaround, power, or a latency percentile. Without the metric there is nothing to be a bottleneck *of*, and the first move is to establish it, not to start a profiler. Also settle here whether the code level is even the right level; a problem in the requirements, the design, or the algorithm will not be found by this procedure and will waste the whole pass. `PAT_name_the_performance_metric_before_you_optimize` owns the metric itself, and `PAT_choose_the_level_before_tuning_the_code` owns the level question.

**1 — Measure the whole program, coarsely.** Start from what existing instrumentation reports, plus a whole-run counter pass if the platform offers one. Take elapsed, process CPU, and thread CPU time together. *Advance when* you know the program's current value on the target metric and its gross character: computing steadily, waiting on something, or limited by a resource such as memory traffic. *Branch:* if the program is waiting rather than computing, or the machine is paging, the bottleneck is not in the code that looks slow and the investigation moves to what it is waiting on. `PAT_let_measurement_decide_what_to_tune` owns what those numbers are allowed to conclude.

**2 — Break the total down by region.** If large sections are already timed, this step is a read rather than a run. If not, take a coarse profile — a breakdown across modules and large functions, built optimized with debug information. *Advance when* the samples are numerous enough for the shares to mean something. *Then do the thing that pays next time:* add the benchmark instrumentation whose absence forced you to profile, while you know where it belongs.

**3 — Descend, or stop descending.** *Branch on what the breakdown shows.* A single dominant function with an obvious cause — the sort of a list nobody expected to grow — goes straight to step 4. A cluster of large functions means another round: build a test that exercises just that part, profile it in more detail, and repeat this step. Counters that indict a resource rather than a location — misses dominating, work stalled rather than executing — mean the question has changed from *where* to *why*, and the answer is in how the code uses the hardware rather than in which line it sits on.

**4 — Ask whether the work can happen less often, before asking how to make it cheaper.** This gate exists because the profile only ever displays the cost side. *Branch:* if the call count or iteration count can come down, that is the candidate change and step 5 is unnecessary — go to step 6.

**5 — Compare implementations in a small harness.** Only when the computation is genuinely required and must be made faster. Two checks gate the result before it is allowed to rank anything: confirm the timed work actually executed rather than being optimized away, and confirm the harness reproduces enough of the real context — separate compilation, realistic inputs, stable across reordering — for the ranking to transfer. *Recovery:* a result that moves with test order, or that flatters one variant implausibly, is a defect in the harness; find the dependency before comparing anything. When a harness produces a number you cannot explain, profile the harness.

**6 — Confirm on the complete program.** Re-measure with the same instrument used in step 1, on the same metric. *Branch on the outcome.* Confirmed: hand the change to the tuning loop, which owns keeping or reverting it. Not confirmed — no movement, or the program got slower — the model of where the time goes was wrong, which is itself a result: compare the profiles before and after and let the difference redirect step 3.

**Completion check.** The action is complete when the responsible code is identified, a candidate change has been shown to move the named metric on the whole program, and the instrumentation that detected the problem is still in the code to catch its return.

## Notes

The order is the content, and it runs coarse to fine for one reason: every instrument here is more misleading the smaller its scope. Whole-program numbers are trustworthy and vague; a micro-benchmark is precise and lies. Starting at the small end produces a confident answer about the wrong code, which is the most common way this work is wasted.

Real passes are not linear. Expect several traversals of steps 2 through 6, alternating between the high-level view and detailed work, with each descent narrowing what the next coarse measurement has to explain. A step that sends you backwards has not failed — a disconfirmed candidate at step 6 is often the fastest route to understanding a program's actual cost structure.

Intuition is allowed a role and not a verdict. Guessing which region to examine first is fine and often efficient; the rule is that nothing advances on the guess alone. The instruments complement each other rather than competing — none of them answers every question, and the usable picture generally comes from two of them agreeing.

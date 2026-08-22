---
object_id: PAT_name_the_performance_metric_before_you_optimize
object_type: pattern
name: Name the Metric Before You Call It Fast
library_path:
- software-engineering
- core
- performance
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- metrics
- measurement
- requirements
- trade_offs
cross_links:
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_choose_the_level_before_tuning_the_code
- rel: related_to
  target_object_id: PAT_name_the_quality_characteristics_you_trade_away
- rel: prerequisite_for
  target_object_id: AP_tune_a_measured_bottleneck
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Name the Metric Before You Call It Fast

## Pattern Rule
**IF** you are about to call an implementation fast or slow, better or worse, or to set a performance goal for one
**THEN** state which metric the claim is about and what value on it the deployment actually rewards, before the comparison or the goal is written down
**ELSE** where a change improves every metric the deployment cares about at once, take it without ranking them — the ranking only binds where the metrics disagree.

## Do
- Expect the metrics to pick different winners, because they usually do. Four implementations of one algorithm: the one that finished in half the slowest one's time had the most erratic run times of the four; the one that drew the least power took noticeably longer; the one that took very nearly the same time on every run drew the most power. Not one of them led on two metrics.
- Know what each metric actually asks. Throughput is how much computation completes per unit time and turnaround is its inverse, the time to a particular result. Power is what the whole computation draws. The latency tail is the Nth-percentile completion time expressed against the average — at the 95th percentile, a 30% tail means 95% of computations finish within 30% of the average time and the rest do not.
- Expect the two to move in opposite directions by design, not only by accident, once a structure is shared between threads. A shared counter under a lock answers one call in constant time and handles a burst of them in time proportional to the burst. A structure that routes threads through a tree so their updates merge on the way makes each individual call cost the logarithm of the participant count — strictly worse — while the burst completes in that same logarithm rather than linearly. Deliberately degrading per-call time to change the shape of the aggregate is a standard move in concurrent design, and it is invisible to any measurement of a single call.
- Read the metric off the deployment rather than off the code. A simulation running for days in a data centre is judged on throughput. The same computation on a battery-powered device is judged on power. A real-time audio processor is judged on the tail, because what a user notices is the dropped word, not the average.
- Find where each metric stops paying and spend the surplus elsewhere. A processor that handles audio ten times faster than a person speaks gains nothing from being faster still; once call quality is limited by something other than latency, the remaining effort belongs on power.
- Say "efficient" only about resource use, and keep it apart from the metric. An efficient program leaves no available hardware idle and does no work that did not have to be done. That is the most common route to a good number on a metric, and it is neither the only one nor the same thing as one.
- Carry the metric and its target into the design goals in the same breath as the other quality characteristics, since a performance requirement that names no metric cannot be held to.

## Don't
- Don't let "faster" pass as a performance claim in a review, a benchmark table, or a requirement. It does not say faster at what, and the answer inverts across metrics on the same four programs.
- Don't benchmark a throughput structure at low concurrency and believe the result. Designs that buy aggregate rate by having threads combine, cancel, or batch their work depend on other threads being present to work with; run one thread through them and you measure the added latency with none of the benefit, which reverses the ranking.
- Don't improve the average without looking at the tail. The techniques that lower average cost are frequently probabilistic — they win most of the time rather than every time — so raising mean speed is an ordinary mechanism for making the worst case worse and less predictable.
- Don't treat full hardware utilization as evidence the goal is met. A program can keep every core busy and still miss a real-time deadline or flatten the battery.
- Don't answer "which is the best implementation?" when nobody has said what the program is for. Without the context there is no answer, and a confident one is a guess about someone else's priorities.
- Don't keep pushing a metric past the point where the context rewards it. Past good enough that work buys nothing, while another metric is still moving.

## Checklist
- Which metric is this claim about, and at which percentile if it is a latency claim?
- What value on that metric is good enough here, and who decided that?
- If the average improved, what happened at the 95th percentile?
- Does this change cost anything on a second metric the deployment also cares about?
- Is the goal on the table efficiency — nothing idle, nothing wasted — or a target number? Those are answered by different work.

## Notes
Efficiency and performance get used interchangeably and are not the same claim. Efficiency describes how the execution uses the machine, and it can be assessed without reference to anyone's purpose. Performance is always a number against a chosen metric, so it cannot be assessed without one. The gap matters most when a program is efficient and still unacceptable: every resource busy, no wasted work, and the deadline missed anyway.

This decision comes before measurement rather than after it, and it constrains what measurement can even mean. Instrumentation is built for a metric — a timer answers a different question from a power meter, and an average answers a different question from a percentile — so the choice of metric has already been made by the time results exist, either deliberately or by whatever the tool happened to report.

The conflict between the average and the tail has a mechanism behind it, which is why it recurs rather than being a property of any one program. Speculative and probabilistic techniques buy their average-case win by being right most of the time; the occasions they are wrong are exactly the long delays that populate a tail. An implementation tuned hard on throughput therefore tends to arrive with a worse tail than the untuned one, and this is visible only if someone was measuring the percentile.

Performance sits inside the broader trade between quality characteristics, but it does not behave as a single one of them. Deciding that a system optimizes efficiency is not yet a decision, because efficiency in the throughput sense and efficiency in the power sense routinely pull against each other and against predictability.

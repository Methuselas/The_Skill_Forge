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
variants:
- variant_id: VAR_baseline_a_metric_the_change_will_not_make_visible
  variant_name: Baseline a Metric a Successful Change Will Not Make Visible
  variant_basis: context
  difference_from_foundation: The foundation is stated for work whose success shows up in something already being watched, and it can assume the metric exists and that improving it is what the deployment rewards. Behaviour-preserving work inverts both assumptions. A restructuring that succeeds is invisible to users by definition — nothing it does should change what anyone observes — so every metric currently monitored, having been chosen because users notice it, is precisely the set that will not move. The metric has to be built for the occasion, chosen to capture the aspect being improved, and recorded before the work starts, because afterwards there is nothing to compare against and no way to construct one retrospectively. The second difference is duration. Work of this kind runs longer than a feature cycle, so unless development elsewhere stopped, other people's changes land in the same code during the measurement window and the figure at the end reflects them as much as it reflects the work. Carrying several distinct metrics rather than one is the practical answer, since concurrent work is unlikely to move all of them the same way.
  when_to_use: Use for any change undertaken for the sake of the code rather than the user — restructuring, decomposition, migration, dependency removal, paying down accumulated debt — and especially where the effort must be justified to someone who will ask afterwards what it achieved. It is also the case to reach for when the honest answer to what improved is a claim about future work rather than about present behaviour.
  when_not_to_use: Where the work is undertaken for performance, the foundation applies unchanged and this variant adds nothing — the baseline already exists, it is already monitored, and the improvement is one of the rare kinds a user can feel. Do not use it as a licence to invent a metric that flatters the work; a figure chosen after the fact, or chosen because it was the one that moved, is worse than no figure at all.
  absorbed_from_object_id: none
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

`VAR_baseline_a_metric_the_change_will_not_make_visible` carries the same rule into work that is not about performance at all, where it becomes harder rather than easier. Restructuring that succeeds changes nothing a user can observe, so the metrics already in place — chosen precisely because users notice them — are the ones guaranteed not to move, and a metric has to be built for the occasion and recorded before the work begins. It also runs long enough that other people's changes land in the same code while it is under way, so the figure at the end is not attributable to the work unless several distinct metrics are carried and compared. Use it for anything undertaken for the sake of the code rather than the user; the foundation covers the performance case unchanged, where the baseline already exists and success is one of the few kinds a user can feel.

This decision comes before measurement rather than after it, and it constrains what measurement can even mean. Instrumentation is built for a metric — a timer answers a different question from a power meter, and an average answers a different question from a percentile — so the choice of metric has already been made by the time results exist, either deliberately or by whatever the tool happened to report.

The conflict between the average and the tail has a mechanism behind it, which is why it recurs rather than being a property of any one program. Speculative and probabilistic techniques buy their average-case win by being right most of the time; the occasions they are wrong are exactly the long delays that populate a tail. An implementation tuned hard on throughput therefore tends to arrive with a worse tail than the untuned one, and this is visible only if someone was measuring the percentile.

Performance sits inside the broader trade between quality characteristics, but it does not behave as a single one of them. Deciding that a system optimizes efficiency is not yet a decision, because efficiency in the throughput sense and efficiency in the power sense routinely pull against each other and against predictability.

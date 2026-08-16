---
object_id: PAT_count_a_routines_decision_points
object_type: pattern
name: Count a Routine's Decision Points
library_path:
- software-engineering
- core
- control-flow
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- complexity
- control_flow
- metrics
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_minimize_variable_span_and_live_time
- rel: related_to
  target_object_id: PAT_minimize_nesting_with_early_returns
- rel: related_to
  target_object_id: PAT_separate_essential_from_accidental_complexity
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Count a Routine's Decision Points

## Pattern Rule
**IF** you suspect a routine has become hard to follow but cannot say how hard
**THEN** count its decision points — one for the routine itself, one for each conditional, loop, `and`, and `or`, and one for each case in a multi-way branch — and treat the total as a warning flag rather than a verdict.
**ELSE** where the count is high for a reason you can state and defend, such as a long multi-way branch that is genuinely one flat decision, record the reason and leave it alone.

## Do
- Run the count mechanically, without judging as you go. Start at one for the straight path, add one for each `if`, `while`, `repeat`, `for`, `and`, and `or`, and one per case. A single condition combining an equality, an `and`, an `or`, and a second `and` scores five on its own, which is usually more than its author expected.
- Read the result against three bands. Up to five, the routine is probably fine. Six to ten is the signal to start looking for simplifications. Above ten, extract part of it into a second routine and call that from the first.
- Count the boolean operators, not just the statements. They are the part people forget, and they are why a routine with two `if` statements can score six — which is the finding, because the reader has to hold every one of those terms at once.
- Take the number as a prompt to look, not as an instruction to act. It identifies candidates; whether a given routine actually needs redesigning is still a judgment, and a long branch over a closed set of cases can legitimately exceed the threshold.
- Pair it with the data-side measures when a routine scores badly and the control flow looks defensible. Control flow is one large contributor to complexity and not the only one — how many variables are in play, how far apart their references sit, and how long each stays live all matter, and a routine can be simple by this count and hard to read for those reasons.

## Don't
- Don't expect extraction to reduce the total. Moving half a routine's decision points into a second routine leaves the program's overall count unchanged — it redistributes them. What it reduces is how many you must hold in mind at once, which is the thing that was actually hurting.
- Don't convert the threshold into a rule that a build enforces. It is a number that says *look here*, and a limit applied without judgment produces routines split at arbitrary places to satisfy it, which raises complexity while lowering the metric.
- Don't treat a passing score as evidence of quality. The count knows nothing about naming, about whether the routine does one thing, or about whether its abstraction is coherent.

## Checklist
- What does this routine score, counting the boolean operators as well as the statements?
- If it is above ten, what would come out into a routine of its own?
- If it is high and you are leaving it, can you say why in one sentence?
- Is the count low while the routine still reads badly, and if so what is the actual cause?
- Has anyone turned this threshold into an enforced limit?

## Notes
What makes this worth running is that it measures the right thing by proxy. The underlying quantity is how many mental objects a reader has to keep in the air at once to understand the routine, which is the hardest part of reading code and the reason interruptions cost so much. That quantity is not directly observable, but decision points are, and the correlation is strong enough that the count has been linked to defect rates in real codebases rather than only in studies.

The redistribution point is the one that gets misread, and it matters because it explains why the technique works at all. Splitting a routine does not make the program simpler in any total sense — the same branches exist, now in two places. The gain is entirely about locality. Ten decision points spread across two routines you read separately is a smaller demand than ten in one routine, even though the program contains ten either way. That reframes extraction as managing attention rather than removing complexity, which is the honest description of what it does.

Read this alongside the data-side measures rather than instead of them. The same discussion that offers this count lists span and live time among the alternatives, and they answer a different question — this one asks how many branches a reader must track, those ask how many values and for how long. A routine can score well on one and badly on the other, and the two failures feel identical from the outside, which is exactly why having both numbers is more useful than arguing about which metric is correct.

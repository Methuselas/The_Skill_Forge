---
object_id: PAT_read_coverage_as_a_floor_not_a_score
object_type: pattern
name: Read Coverage as a Floor, Never as a Score
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- testing
- coverage
- metrics
- test_design
- measurement
cross_links:
- rel: prerequisite_for
  target_object_id: AP_choose_test_cases_systematically
- rel: related_to
  target_object_id: PAT_test_three_cases_at_every_boundary
- rel: related_to
  target_object_id: PAT_decide_whether_a_check_blocks_or_warns
- rel: related_to
  target_object_id: PAT_tests_fail_only_when_code_broken
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Read Coverage as a Floor, Never as a Score

## Pattern Rule
**IF** a tool has reported what proportion of the code your tests reached
**THEN** use the figure to find what was never executed at all, and refuse to use it as a statement of how well anything was tested
**ELSE** where no figure exists, estimate nothing — self-assessed coverage runs far above measured coverage, so the estimate carries less information than the absence of one.

## Do
- Use it for the one thing it does well: pointing at code no test has reached. That list is reliable, actionable, and not obtainable by reading.
- Aim past statements to branches, with every term in every condition exercised both ways. Statement coverage counts lines and a line with a compound condition can execute while most of its terms never vary.
- Hold the distinction between reaching code and testing it. What determines whether a fault is found is which of the program's states were visited, and states are not lines — a three-line routine taking two integers has a state count in the millions, of which one specific pair may be fatal, and the tool reports that the lines executed.
- Measure rather than estimate. Developers put their own coverage near ninety-five percent and typically achieve fifty to sixty, and that gap is stable enough to plan around.
- Expect a thoughtfully tested body of code to land somewhere in the eighties, and treat a much higher figure as a question rather than an achievement.
- Watch what happens when the number becomes a target. Where a high figure is demanded, tests appear that execute code without asserting anything meaningful about it, and coverage rises while the suite's ability to detect a fault falls.

## Don't
- Don't read a high figure as a well-tested system. Full branch coverage achieved with data that never approaches the dangerous combination is a complete pass over a program you have not tested.
- Don't set a coverage threshold as a gate without deciding what you will do when it is met by low-quality tests, because that is how it will be met.
- Don't let the figure end the question of whether enough testing has been done. It answers what was reached; whether the important behaviours were checked is a separate judgement that no tool makes.
- Don't compare the number across components as though it ranked their quality. Different code has wildly different state-to-line ratios, so equal percentages mean different things.

## Checklist
- What does the report say was never executed at all?
- Is this statement coverage or branch coverage, and are compound conditions exercised both ways?
- Which of this code's dangerous states have been visited, as opposed to which lines?
- Was the figure measured or estimated?
- If a threshold is enforced here, what happened to test quality after it was introduced?

## Notes
The trouble with coverage is that it is the only number the activity produces, and numbers attract confidence that the underlying measurement does not support. It answers one narrow question — was this line or branch ever reached — while the question that matters is which of the program's possible states have been visited. Those two diverge immediately and enormously: a handful of integer parameters puts the state count into the millions while the line count stays in single figures, and the states that break are usually a particular combination rather than a particular route.

That divergence is what makes it a floor rather than a score. Code never executed is definitely untested, which is real information and worth acting on. Code that was executed may have been tested thoroughly, or reached once with a value chosen for convenience, and the report cannot tell the two apart. So the figure supports one direction of inference and not the other, and nearly all misuse consists of running it backwards.

The behaviour of the measure under pressure is the practical warning. Coverage is easy to raise without improving anything — a test that calls a function and asserts nothing at all moves the number as effectively as a careful one. Wherever the figure is demanded rather than consulted, the cheap way to satisfy it is available and gets taken, and the result is a suite that reports higher coverage while detecting fewer faults than before. The measure is useful exactly as long as nobody is being judged by it.

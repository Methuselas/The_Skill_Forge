---
object_id: PAT_choose_a_complexity_metric_by_what_it_cannot_see
object_type: pattern
name: Choose a Complexity Metric by What It Cannot See
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- complexity
- metrics
- measurement
cross_links:
- rel: related_to
  target_object_id: PAT_concentrate_effort_where_defects_concentrate
- rel: related_to
  target_object_id: PAT_name_the_performance_metric_before_you_optimize
- rel: related_to
  target_object_id: PAT_look_for_the_evidence_outside_the_code
- rel: related_to
  target_object_id: PAT_read_coverage_as_a_floor_not_a_score
reference:
  source_title: 'Refactoring at Scale: Regaining Control of Your Codebase'
  author: Maude Lemaire
confidence: high
references: []
variants: []
---

# Choose a Complexity Metric by What It Cannot See

## Pattern Rule
**IF** you need a number for how complex a section of code is — to locate the worst of it, to baseline a change, or to size a testing effort
**THEN** choose the metric by what it is blind to rather than by what it counts, because each of the common ones is silent about something that drives real difficulty
**ELSE** where you only need to find the worst offenders rather than characterise them, a size measure is the cheapest signal that correlates and can be computed on anything.

## Do
- Know that a decision-point count cannot see nesting. It adds one per branch, so a routine with three loops one after another scores the same as one with three loops inside each other — and the second is far harder to hold in your head. If the difficulty you are chasing is tangled nesting, this metric will report that nothing changed after you have fixed it.
- Know that a path count sees the nesting and pays for it twice over. It multiplies where the decision count adds, which is what lets it distinguish the two routines above; but it also counts combinations that cannot occur, having no way to know that a value cannot be both below one bound and above a higher one. On old code the totals run to the hundreds of thousands, and at that magnitude a genuine improvement is invisible inside the number.
- Apply the expensive metrics to bounded sections and average them, rather than computing a figure for the whole system. A metric that saturates says almost nothing about a system-wide total and a good deal about a single module.
- Fall back to size where the graph metrics cost more than they return — which is most likely on exactly the large old codebases you most want to measure. Lines per file, the length of the longest routines, and mean routine length within a unit are cruder, correlate well enough to locate pain, and cost nothing.
- Read any score against your own codebase rather than against a published threshold. The absolute figure means very little by itself; it acquires meaning by being seen repeatedly next to the code that produced it, until the number predicts your reaction to opening the file.
- Treat a cluster of inline comments as a signal in its own right. People explain what they found hard, so a short routine carrying several explanatory comments is often reporting a difficulty that no branch count or size measure will show.
- Use the two graph metrics as bounds on test effort where you need one. The decision count is a floor on the cases required to reach every branch; the path count is a ceiling.

## Don't
- Don't carry a single number. Each of these characterises one aspect of one kind of difficulty, and a lone figure will either miss the problem you have or move for reasons unrelated to it.
- Don't expect every improvement to register. Some restructuring leaves the control flow untouched, and some complexity belongs to the business rule rather than to the code — a metric that refuses to move may be reporting that you improved something else, or that there was nothing here to improve.
- Don't compare scores across languages, codebases, or teams with different conventions. Within one codebase under one style guide the numbers are comparable, which is the situation that matters; outside it they measure the conventions as much as the code.
- Don't pick the metric after collecting it. Choosing once the numbers are in front of you means choosing the one that tells the story you already wanted.

## Checklist
- What kind of difficulty am I trying to measure — branching, nesting, sheer size, or something none of these sees?
- Does the metric I have chosen move when that difficulty changes?
- Is the figure being read against this codebase's own range, or against a number from a book?
- Am I carrying more than one, and do they disagree in a way worth understanding?
- If the number does not move after the work, is that a failure of the work or of the metric?

## Notes
The reason to lead with blindness rather than with definition is that all these metrics correlate with each other and with difficulty, so any of them will look reasonable in a demonstration. They come apart on specific shapes — the nesting case is the clearest — and the shape you have is exactly what decides which one will register your work. Picking on general reputation gets you a number that was never going to respond.

There is a second reason, which is that a metric chosen to measure a change is also a metric someone will be asked to improve. Once a figure is the target it stops describing the thing it was chosen for, and the cheapest way to move most of these is not the way anyone intended: split a routine at an arbitrary point and the per-routine averages improve while the code gets slightly worse. That is an argument for carrying several, for keeping the raw code in view beside them, and for treating the numbers as a way to find candidates and to notice movement rather than as the definition of what you were trying to do.

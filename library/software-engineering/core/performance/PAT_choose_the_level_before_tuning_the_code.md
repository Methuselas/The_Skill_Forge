---
object_id: PAT_choose_the_level_before_tuning_the_code
object_type: pattern
name: Choose the Level Before You Touch the Code
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
- optimization
- architecture
- requirements
cross_links:
- rel: related_to
  target_object_id: PAT_name_the_quality_characteristics_you_trade_away
- rel: related_to
  target_object_id: PAT_evaluate_code_against_quality_goals
- rel: prerequisite_for
  target_object_id: AP_tune_a_measured_bottleneck
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Choose the Level Before You Touch the Code

## Pattern Rule
**IF** something is too slow or too large and you are deciding what to do about it
**THEN** work down the levels in order — requirements, program design, class and routine design, operating-system interactions, compilation, hardware, and only then the code itself
**ELSE** where the constraint is genuinely a few lines running millions of times, the code level is the right answer and the earlier levels have simply been checked and cleared.

## Do
- Ask first whether code speed is even the thing that is slow. What a user experiences is throughput, and it is only loosely related to how fast the code runs — a card reader that copies each file no faster than the old software still performs better if it replaces dozens of clicks with a drag and a drop.
- Challenge the requirement before designing to it. Performance is stated as a requirement far more often than it actually is one: a TRW system specified subsecond response, which drove a design estimated at $100 million, and finding that users were content with four seconds ninety percent of the time took about $70 million off the cost.
- Look for the problem the code level cannot reach. A data-acquisition system facing a 13th-order polynomial per measurement was not going to be rescued by tuning the arithmetic; different hardware and a design using dozens of 3rd-order polynomials solved it, and no amount of code tuning would have.
- Set resource goals per subsystem, feature, and class when speed and size genuinely matter. Three things follow: the system's final performance becomes predictable because meeting every part's goal means meeting the whole, the parts that cannot meet theirs identify themselves early, and stating a goal at all measurably raises the chance of hitting it.
- Take the cheap levels seriously rather than treating them as cheating. A better compiler can be worth forty percent or more across the board where hand techniques typically return fifteen to thirty. New hardware, for a system with few in-house users, buys the gain without the initial work, without the maintenance burden that tuned code carries forever, and it speeds up everything else on the machine too.
- Aim modifiability at efficiency rather than against it. A highly modular design lets you swap a slow component for a fast one, so a goal that does not mention speed can serve speed better than one that does.

## Don't
- Don't reach for the code level because it is the level you control. It is the least effective of the seven, the least cheap, and the only one that makes the code permanently harder to maintain.
- Don't confuse an inefficiency with a defect. Debug logging left switched on, memory never released, a device polled until it times out, and a commonly used database table with no index are bugs — indexing that table once improved some operations by a factor of thirty, and defining it was never optimization in the first place.
- Don't design for performance without saying which characteristics you are spending to get it. Efficiency is the priority that reads as unambiguously virtuous and damages the most neighbours.

## Checklist
- Is the thing the user calls slow actually the code's execution speed?
- Has anyone checked whether the performance requirement is real, or is it a number somebody wrote down?
- Which of the seven levels is this problem actually on?
- Would a different compiler, or different hardware, cost less than the tuning you are about to do?
- If speed matters here, does each subsystem have a resource goal it can be held to?

## Notes
The ordering is the content. Improvements at each level can be dramatic — Bentley cites the argument that in some systems gains at each of six levels multiply, which would imply a millionfold potential — and while that requires the levels to be independent, which is rare, it makes the point that the code level is one of seven places to look and the last one worth looking.

Code tuning has a specific meaning that keeps it in its place: modifying *correct* code so that it runs more efficiently, at the scale of a class, a routine, or more often a few lines. It is not a large-scale design change, and calling a redesign "tuning" is how a project ends up attempting at the code level a problem that only the design level could have solved.

How narrow the code level's remaining territory has become is worth stating with the author's own evidence, since he measured it twice a decade apart. Producing meaningful timings for the standard tuning techniques took ten to fifty thousand executions in the early nineties and one million to a hundred million a decade later. When a difference only becomes visible after a hundred million repetitions, the honest question is whether anyone will ever notice it in a running program. For most desktop and business software the answer is no, and the level has become irrelevant rather than merely unfashionable. Where it still earns its keep is unchanged: embedded systems, real-time systems, and anything under a strict speed or space budget.

The reason the requirements level comes first is that it is the only one that can make the problem disappear rather than shrink. Every other level trades something — complexity, money, maintainability, portability — to make the software faster. Discovering that the target was never needed costs nothing and removes the work entirely, which is why it is worth the awkward conversation before rather than after the highly complex design exists.

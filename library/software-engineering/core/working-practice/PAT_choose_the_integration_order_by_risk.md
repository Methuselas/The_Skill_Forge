---
object_id: PAT_choose_the_integration_order_by_risk
object_type: pattern
name: Choose What to Integrate Next by Where the Risk Is
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- integration
- construction
- risk
- sequencing
cross_links:
- rel: related_to
  target_object_id: AP_grow_a_system_from_a_running_skeleton
- rel: related_to
  target_object_id: PAT_keep_the_build_green_with_an_automated_smoke_test
- rel: related_to
  target_object_id: PAT_prototype_to_answer_one_specific_design_question
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Choose What to Integrate Next by Where the Risk Is

## Pattern Rule
**IF** you are deciding the order in which the parts of a system get built and combined
**THEN** put the riskiest and most load-bearing parts first, get one slice running end to end early, and let the construction order follow from the integration order
**ELSE** on a system of two or three classes the order barely matters, and planning it is overhead you will not recover.

## Do
- Treat the order as a decision rather than a residue of who finished what first. A structure has to be strong enough *at every step*, not merely once complete — a stadium built in the wrong sequence collapsed partway up even though the finished design would have stood.
- Put the parts you expect to be hardest at the front: top-level control and interfaces, system and device interfaces, a poorly understood algorithm, anything carrying an ambitious performance target. Easy work that turns out hard is survivable; hard work discovered late is what forces the expensive redesign.
- Drive one thin slice end to end before spreading sideways. A single deep slice exercises the architecture's assumptions while they are still cheap to change; once it holds, build the breadth that the remaining features hang off.
- Count the scaffolding each candidate order would need and prefer the one needing least. Stubs and drivers are test code, they are more likely to contain defects than production code, and a bug in a stub destroys the exact property incremental integration was bought for — the confidence that the newest piece is the culprit.
- Check that the interfaces between components have actually been specified before integrating across them. Specifying them is not an integration task; confirming somebody did it is, and the worst defects to chase are the ones arising from subtle interactions rather than from inside a single component.
- Sequence construction to serve integration. You cannot integrate what has not been built, so the order you intend to combine things in constrains the order you write them in.

## Don't
- Don't integrate in one phase at the end. Every problem then arrives at once, the problems interact, every component is a suspect, and the team drops into panicked debugging instead of methodical diagnosis at exactly the point in the schedule with no slack left.
- Don't run a pure top-down order. It leaves the tricky system interfaces until last, lets low-level trouble bubble upward into high-level change, and needs a dump truck of stubs to make progress at all.
- Don't run a pure bottom-up order either. Conceptual problems in the high-level design then surface only after all the detailed work is done, and assumptions from low-level code leak upward until you are designing high-level classes to work around the limitations of low-level ones.
- Don't treat the named strategies as procedures to follow step by step. They are heuristics with memorable names, not algorithms, and the order that fits your system is one you assemble rather than select.

## Checklist
- What is the riskiest part of this system, and how early does the current order reach it?
- Does anything run end to end yet?
- How much scaffolding does this order require, and who is testing the scaffolding?
- Have the interfaces you are about to integrate across actually been specified?
- Is the build order consistent with the order you intend to integrate in?

## Notes
The argument for incremental over phased integration is not primarily about schedule; it is about where a defect can be. Integrate one piece at a time and a new failure is either in that piece or in its connection to what already worked, which is a search of two places. Integrate fifty pieces at once and the failure is somewhere among the components and all their connections, with several failures interacting and masking each other. Given that interface defects between components run to a large share of all defects — one accounting put intermodule interface errors at 39 percent — the difference in diagnosis cost is the whole game.

The named strategies are worth knowing as vocabulary rather than as options to pick from. Top-down and bottom-up are the pure forms, and neither is workable unmodified. Sandwich integration takes the high-level business objects and the widely used low-level utilities first, leaving the middle. Risk-oriented integration reaches the same shape from a different motive: hardest first, wherever the hard parts happen to sit. Feature-oriented integration grows the system one identifiable function at a time, which suits object-oriented systems because objects tend to map onto features, and which nearly eliminates scaffolding because each feature carries its own support code. T-shaped integration drives one deep slice to validate the architecture and then builds the breadth. In practice the useful strategy for a given system is a hybrid, and the two ideas that survive from all of them are: front-load risk, and get something running end to end.

Incremental integration composes with itself, which is what makes it work at more than one scale. Small pieces integrate into a feature, features integrate into the system, and the same reasoning about error localisation applies at each level. That also sets the honest limit on the increment size: the bigger the piece you add at once, the less precisely a new failure is located, so a large increment is affordable only to the extent that its internals were already tested on their own.

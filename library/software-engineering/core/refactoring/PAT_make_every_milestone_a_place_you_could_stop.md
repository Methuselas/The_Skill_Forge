---
object_id: PAT_make_every_milestone_a_place_you_could_stop
object_type: pattern
name: Divide a Long Change Into Places You Could Walk Away From
library_path:
- software-engineering
- core
- refactoring
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- refactoring
- planning
- milestones
- risk
- maintenance
cross_links:
- rel: related_to
  target_object_id: PAT_separate_structural_change_from_behavioural_change
- rel: related_to
  target_object_id: PAT_prove_behaviour_held_by_running_both_paths
- rel: related_to
  target_object_id: AP_refactor_working_code_safely
- rel: related_to
  target_object_id: PAT_remove_the_scaffolding_a_migration_leaves
- rel: related_to
  target_object_id: AP_replace_a_system_that_is_still_in_use
reference:
  source_title: 'Refactoring at Scale: Regaining Control of Your Codebase'
  author: Maude Lemaire
confidence: high
references: []
variants: []
---

# Divide a Long Change Into Places You Could Walk Away From

## Pattern Rule
**IF** you are breaking a change too large for one sitting into an ordered set of steps
**THEN** require each step to leave the code in a state a stranger could read, extend, and ship from — and reject any division whose intermediate states only make sense to someone holding the whole plan in their head
**ELSE** where no such division exists, the change is not yet understood well enough to start, and the work in front of you is finding one rather than beginning.

## Do
- Judge each candidate step against three questions, and treat the third as the one with teeth. Is it reachable in a period you can commit to? Is it worth something on its own if nothing follows it? And could the work be abandoned here, indefinitely, without leaving anyone worse off than before you started?
- Prefer a smaller first step that delivers to other people over a larger one that only sets the stage. Consolidating scattered configuration, or turning on a check that catches a class of error, pays whoever works in that code from the day it lands, and it pays whether or not the rest of the plan survives contact with the next quarter.
- Apply the whole change to one bounded region at a time, rather than applying one phase of it everywhere. Each region then behaves like a small complete version of the effort, and at every moment the amount of code caught between two shapes is one region's worth rather than the entire surface.
- Choose the first region either for being the worst case or for being the cheap one that demonstrates the shape convincingly, and say which of the two you picked and why.
- Move what you intend to change behind a single entry point before changing it, so that during the transition nobody outside is exposed to two implementations at once.
- Look for steps with no ordering constraint and use them deliberately. Where a step could run at any point, placing it between two long and difficult ones gives the work somewhere to stand that is not halfway up either of them.
- Write the state each step ends in, not just the action it performs. A step described only by its verb cannot be checked against the abandonment question, because the description never says what would be left behind.

## Don't
- Don't begin a stretch of work you cannot see the end of. Code caught midway between two designs is worse than either — a reader cannot tell which implementation is the intended one, and the wrong guess means new work built on the path being retired.
- Don't let a step be defined by how much fits in the time available. A boundary chosen for capacity reasons lands wherever the week ran out, which is exactly where a coherent state is least likely to be.
- Don't count a step as complete while its temporary machinery is still standing. Whatever was erected to make the transition safe is part of the transition, and the step it belongs to has not finished until it is gone.
- Don't treat the ability to pause as pessimism about the plan. Priorities move, incidents happen, and people leave; the division that survives those is the one that was designed expecting them.

## Checklist
- If everything stopped after this step, would the code be in a defensible state or a confusing one?
- Could someone joining next month tell which implementation they are supposed to extend?
- Does this step deliver anything to anyone if the following steps never happen?
- How much of the codebase is in an intermediate shape at the worst moment of this plan?
- Was this boundary chosen because it is a coherent state, or because of how much time was left?

## Notes
The standing objection to large-scale restructuring is that it is a recipe for disaster, and the objection is correct about the thing it describes: a single long session of restructuring, held together by one person's understanding, with no defensible state anywhere in the middle. What this answers is not the objection but its premise. A change spanning months is not one enormous session; it is a sequence of ordinary ones, and the property that makes the sequence safe is that the code is shippable at every join. Once that holds, the size of the total effort stops being the risk it looked like, because at no point is anyone carrying more unfinished work than one step's worth.

The abandonment test does the real work because it is the only one of the three that cannot be satisfied by wishful thinking. Attainability and standalone value are both estimates about the future. Whether the code would be comprehensible if everything stopped tomorrow is a question about a state you can describe now, and describing it usually exposes the divisions that were really just a schedule cut in half. It also converts an unpleasant organisational fact into a design input: work does get suspended, and a plan built to survive suspension loses very little when suspension never comes.

The connection to the cost of a half-finished change is what gives the test its force. Unfinished restructuring is not neutral, sitting harmlessly until someone returns to it. It actively misleads, because a reader encountering two shapes has no way to know which one is ascendant, and a reasonable person building on the older one produces work that has to be redone. That cost accrues from the day the work pauses and grows with every person who reads the code afterwards, which is why the question is whether the pause is survivable rather than whether it is likely.

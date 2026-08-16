---
object_id: PAT_make_code_reusable_and_generalizable
object_type: pattern
name: Design Code to Be Reusable and Generalizable
library_path:
- software-engineering
- core
- reusability
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- reusability
- generalization
- code_quality
- abstraction
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_beware_assumptions_avoid_or_enforce
- rel: prerequisite_for
  target_object_id: PAT_avoid_global_state_inject_shared_state
- rel: prerequisite_for
  target_object_id: PAT_provide_defaults_in_higher_level_code
- rel: prerequisite_for
  target_object_id: PAT_keep_function_parameters_focused
- rel: prerequisite_for
  target_object_id: PAT_use_generics_for_type_independence
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: medium
references: []
variants:
- variant_id: VAR_harvest_reuse_at_the_end_rather_than_designing_for_it
  variant_name: Harvest Reuse at the End Rather Than Designing for It
  variant_basis: method_sequence
  difference_from_foundation: The foundation designs a solution to be reusable and generalizable while writing it. This variant inverts the sequence on the strength of NASA's Software Engineering Laboratory result across ten projects that pursued reuse aggressively - identify reuse candidates at the end of a project, then do the work to make those specific classes reusable as a closing task or as the first step of the next project. The reported outcome is that object-oriented projects took more than 70 percent of their code from previous projects against about 35 percent for functionally designed ones, and McConnell notes explicitly that the core of the approach does not involve designing for reuse. Its stated purpose is preventing gold-plating, meaning functionality nobody required that adds complexity anyway.
  when_to_use: Use when you cannot yet name the second caller. Harvesting after the fact means the generalization is shaped by two real uses rather than one real use and one imagined one, and the classes that turned out to matter select themselves.
  when_not_to_use: Do not use it to defer all structural thought to the end, since the foundation's case holds when the recurrence is already visible and concrete. It also does not license shipping something knowingly hostile to reuse on the promise of fixing it later, because the harvest is a scheduled task and not an aspiration.
  absorbed_from_object_id: none
---

# Design Code to Be Reusable and Generalizable

## Pattern Rule
**IF** you are solving a problem whose shape recurs, or that is one of several conceptually similar problems
**THEN** design the solution to be reusable (same problem, many scenarios) and generalizable (related, subtly-different problems), like a drill that works on walls, floors, and ceilings and also drives screws.

## Do
- Separate the general capability (rotating a bit) from the specific scenario (wall versus floor versus ceiling; drilling versus screwing), so one tool serves many jobs instead of four narrow tools.
- Prefer fewer total lines of code: more code means more maintenance and more bugs, and you are ultimately paid to solve the problem, not to produce code.

## Don't
- Don't build four narrow single-purpose tools — a level-only drill, a floor-only drill, a ceiling-only drill, a screwdriver — where one reusable, generalizable tool would serve.
- Don't conflate reusability (same problem, new scenario) with generalizability (a different but related problem); they are distinct design targets.

## Checklist
- Can this be used in more than one scenario without changing it?
- Could it solve a related, subtly different problem as well?
- Is there redundant code here that a more general solution would remove?

## Notes
The hand drill anchors both concepts at once: reusable across scenarios (walls, floors, ceilings) and generalizable across related problems (drilling holes and driving screws). Long argues fewer lines of code is a virtue because code is a liability that must be maintained and carries bug risk. This is the "reusable and generalizable" pillar's foundation, closely tied to modularity; chapter 9 specializes it into avoiding assumptions, global state, focused parameters, and generics.

`VAR_harvest_reuse_at_the_end_rather_than_designing_for_it` disagrees with this foundation about *when*, and the disagreement is evidence-backed rather than stylistic. NASA's Software Engineering Laboratory studied ten projects pursuing reuse aggressively and found the object-oriented ones later drawing more than 70 percent of their code from previous projects, against roughly 35 percent for functionally designed ones - but the mechanism was not designing for reuse. Candidates were identified at the end of a project and made reusable as a separate piece of work, precisely to avoid gold-plating. The two routes reconcile in practice: design for reuse where the recurrence is already concrete and visible, harvest where it is speculative. What the variant supplies that the foundation does not is a way to get reuse without paying for guesses about which parts would be reused.

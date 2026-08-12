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
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u01, pp. 17-18
  evidence_type: text
confidence: medium
references: []
variants: []
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

---
object_id: AP_grow_a_system_from_a_running_skeleton
object_type: ap
name: Grow a System From a Running Skeleton
library_path:
- software-engineering
- core
- working-practice
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- incremental_development
- integration
- construction
- skeleton
- iteration
cross_links:
- rel: related_to
  target_object_id: AP_plan_and_build_work_from_thumbnail_to_final
- rel: related_to
  target_object_id: PAT_scope_construction_beyond_writing_the_code
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Grow a System From a Running Skeleton

## Objective

Get a system to a state where it runs end to end as early as possible, then replace its placeholders with real behaviour one at a time — so that at every moment there is a working thing to add to, rather than a set of finished parts waiting to be joined.

## Steps / Flow

1. **Identify the basic functions.** List the operations the system must perform. This is the set that will become the placeholder classes, so keep it at the level of "accept input", "transform", "produce output" rather than at the level of individual methods.

2. **Build the simplest version that will run.** It does not have to accept realistic input, does not have to perform realistic manipulations on data, and does not have to produce realistic output. The only requirement is that it be a skeleton strong enough to hold the real system as it is developed — it runs, end to end, without doing anything useful.

3. **Call a dummy class for each basic function.** Each one stands where real behaviour will go and returns whatever keeps the run alive. The skeleton is now the grain of sand the rest accretes onto.

4. **Replace one dummy with the real thing.** Change a single dummy class to a real class and confirm the system still runs end to end. Where the program pretended to accept input, drop in code that accepts real input; where it pretended to produce output, drop in code that produces real output.

5. **Repeat until nothing is pretending.** Add a little code at a time until you have a fully working system. Each replacement is small enough that when the run breaks, the cause is the thing you just changed.

6. **Keep the end-to-end run green throughout.** The property that makes this cheap is that a working system exists at every step. If you find yourself with several dummies replaced but no successful run since two steps ago, stop and recover the run before continuing.

## Notes

The alternative this displaces is building the parts separately and integrating at the end, which concentrates all the discovery of how they fit into the phase with the least time left. Growing from a skeleton spreads that discovery across the whole build, one replacement at a time. The related words are worth knowing because they show up in different traditions describing the same move: incremental, iterative, adaptive, evolutionary.

The historical evidence behind this is unusually strong for a practice recommendation. Fred Brooks advised in 1975 building one version to throw away; two decades later he reported that nothing in the intervening years had so radically changed his own practice or its effectiveness as incremental development. Tom Gilb's *Principles of Software Engineering Management* introduced Evolutionary Delivery on the same basis and laid the groundwork for much of what became Agile practice, and a long line of methodologies since rests on the same idea.

Two cautions from the source. First, the "grow it like a crop" framing that often accompanies this technique is a bad fit: it suggests you have no direct control over how the system develops, which is the opposite of the case — you choose which dummy to replace and when. Second, the technique's value is that it does not overpromise. It does not remove the need to know what the basic functions are before you start, and step 1 is real work, not a formality.

Scale changes what step 2 costs, not whether it applies. On a thousand lines of code a wrong skeleton can be refactored or restarted without losing much; on a system where the requirements alone run to thousands of pages, get the skeleton's shape right before pouring code into it.

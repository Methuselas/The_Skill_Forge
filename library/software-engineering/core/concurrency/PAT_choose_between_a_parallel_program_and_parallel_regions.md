---
object_id: PAT_choose_between_a_parallel_program_and_parallel_regions
object_type: pattern
name: Choose Between a Parallel Program and Parallel Regions
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- concurrency
- design
- architecture
- scalability
- decomposition
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: AP_design_a_parallel_decomposition
- rel: related_to
  target_object_id: PAT_find_the_axis_the_parallelism_lies_along
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Choose Between a Parallel Program and Parallel Regions

## Pattern Rule
**IF** you have a decomposition and must now decide what shape the program itself takes
**THEN** choose deliberately between a program that is parallel throughout — every execution unit running from start to finish, each doing sequential work — and a program that runs sequentially and opens parallel regions where the time is spent
**ELSE** where the platform dictates the answer, which several do, the choice has been made for you and the useful work is knowing which one you inherited and what it costs.

## Do
- Read the two shapes as answering different questions. A program that is parallel throughout has no sequential spine at all: units start together, take different paths by identity, and combine at the end. A program with parallel regions has a single thread of control that widens where the work is and narrows again after — so it retains a sequential backbone by construction.
- Choose the region form when you are converting something that already works. It is the incremental path: the program keeps running correctly at every step, you widen the region that dominates the profile, measure, and widen the next. That property — remaining shippable throughout — is worth a great deal and is the honest reason most parallelization is done this way.
- Expect the region form to hit a ceiling that the whole-program form does not have. Its sequential backbone never goes away, so the untouched part sets a hard limit on total speedup no matter how many regions are widened or how many units are added. When the profile keeps flattening as you parallelize more regions, that ceiling is what you are meeting, and the remedy is a different program shape rather than another region.
- Price the repeated entry and exit of a region, since a program with parallel regions pays it every time. Opening a region and closing it costs something whether or not the region does much work, so a small region inside a hot loop can cost more than it saves — which is a different failure from the ceiling above and shows up much earlier.
- Take identity-based branching as the normal structure for the whole-program form. Every unit runs the same code, obtains a unique index, and uses it to decide which data it owns and which role it plays. Keeping one program rather than several is what makes this approach practical to build and debug, and it is why it dominates in practice.
- Accept that the single-program form replicates everything. All the code and all the global data exist on every unit, whether that unit needs them or not. On a shared-memory machine that is nearly free; where units have separate memories it can be the constraint that decides the design, and the escape — genuinely different programs on different units — is worth the added deployment complexity only when heterogeneity or memory pressure forces it.
- Check what the platform imposes before treating this as an open choice. Message-passing environments give you the whole-program form whether you wanted it or not; directive-based environments push you toward parallel regions around loops; a device offload model gives you regions with a very expensive boundary. The platform decision and this one are not independent, so making them in the wrong order means discovering the constraint after the design.

## Don't
- Don't reach for parallel regions and then be surprised by the ceiling. It is the right choice for a retrofit and it carries a limit that is structural rather than a tuning problem — knowing that in advance is the difference between stopping at a good result and spending weeks against an asymptote.
- Don't build the whole-program form for a computation whose parallel part is a small fraction of the code. You will restructure everything, including the parts that were never the problem, to remove a sequential backbone that was not costing much.
- Don't let identity-based branching turn into genuinely different programs sharing a file. Once the branches diverge enough that no unit executes most of the code, the single-program form has stopped providing its one benefit and is now hiding several programs inside one binary.
- Don't assume a region boundary is cheap because it is a single line of source. It is a synchronization point where every unit must arrive before any proceeds, and it appears in the code as one construct while behaving as the most expensive thing in the loop.
- Don't decide this before the decomposition. What shape the program takes depends on what the pieces are and how they communicate, and choosing the shape first is how a decomposition ends up bent to fit a structure that was picked for unrelated reasons.

## Checklist
- Does this program have a sequential backbone, and if so what fraction of the time does it hold?
- Is this a conversion of working code or a design from scratch?
- How often is a parallel region entered, and what does entering it cost relative to what it does?
- If units branch by identity, does every unit still execute most of the code?
- Does anything need to exist on every unit that most units will not use?
- Which of these two shapes does the target platform impose?

## Notes
The distinction is easy to state and easy to underrate: is the program parallel with sequential parts inside it, or sequential with parallel parts inside it. Almost every practical decision downstream inherits from that answer — where synchronization lives, what the speedup ceiling is, how the thing is debugged, and whether it can be delivered in increments. Teams routinely arrive at one of these without deciding, because the platform they picked implied it.

The retrofit case deserves its own emphasis because it is the common one and the tradeoff is genuinely favourable. Widening regions in an existing program preserves a working system at every step, lets the profile choose what to do next, and delivers value before the work is finished. What you buy with that is real; what you pay is that the sequential backbone remains, and the eventual limit is set by the part you never converted. Both halves should be said out loud at the start, because the first is why the approach is chosen and the second is why it later disappoints.

The platform coupling is the practical trap. These are presented as design alternatives, and in most projects the environment has already settled it — a message-passing runtime hands you the whole-program shape, a directive-based one hands you regions, and an offload model hands you regions with an expensive boundary. That is not a problem as long as it is noticed. It becomes one when a decomposition is designed for one shape and implemented on a platform that only offers the other.

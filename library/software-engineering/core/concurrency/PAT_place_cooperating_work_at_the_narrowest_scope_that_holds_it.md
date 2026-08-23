---
object_id: PAT_place_cooperating_work_at_the_narrowest_scope_that_holds_it
object_type: pattern
name: Place Cooperating Work at the Narrowest Scope That Holds It
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
- locality
- decomposition
- gpu
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_give_each_waiter_its_own_location_to_spin_on
- rel: related_to
  target_object_id: PAT_keep_a_lockstep_group_on_one_path
- rel: related_to
  target_object_id: AP_design_a_parallel_decomposition
- rel: related_to
  target_object_id: PAT_locate_the_working_set_on_the_memory_hierarchy
reference:
  source_title: 'Multicore and GPU Programming: An Integrated Approach'
  author: Gerassimos Barlas
confidence: high
references: []
variants: []
---

# Place Cooperating Work at the Narrowest Scope That Holds It

## Pattern Rule
**IF** some of your parallel work must coordinate — exchange values, agree on a result, wait for each other — and the hardware offers nested levels at which participants can be co-located
**THEN** arrange the decomposition so that participants who cooperate land in the smallest level that can contain them, because the cost of coordinating rises steeply with each level you cross
**ELSE** where the work is genuinely independent and coordinates only at the very end, placement does not matter and the decomposition is free to optimize for something else.

## Do
- Enumerate the levels your hardware actually provides, because the list is longer than it first appears and each step up costs more. Threads executing in lockstep can often exchange values directly, without memory being involved at all. Threads sharing a local memory can use it plus a cheap barrier. Threads on one processor share a cache. Processors in one package share a memory controller. Beyond that, coordination becomes a message. Each of those is roughly an order of magnitude apart.
- Make cooperation scope a decomposition input rather than an implementation detail. Which participants need to talk is decided when the work is carved up; where they land is decided by the mapping. Doing the first without the second produces a correct decomposition whose cooperating parties are spread across the machine, and no amount of later tuning brings them back together.
- Prefer the cheapest mechanism the shared scope makes available. Where participants are close enough to exchange directly, going through memory is real cost paid for nothing; where they share a scratchpad, using a global structure is the same mistake one level up. The mechanism should be chosen from the scope, not from habit.
- Make the cooperating set an explicit object rather than deriving membership from index arithmetic at every use. When "who am I cooperating with" is recomputed from raw indices at each site, the answer is restated in several places and can disagree; naming the group once and passing it makes the intent visible and lets the cooperation be written as an operation on it.
- Expect the deliberately unfair arrangement to be the fast one. Keeping a resource, or a piece of work, circulating within a scope rather than handing it across scopes preserves locality at the cost of some fairness — which is the same trade that makes cluster-aware locks beat strictly fair ones, and it appears at every level of the hierarchy for the same reason.
- Notice when the hardware simply does not offer coordination across a boundary. Historically some devices provided no way for participants in different top-level groups to synchronize at all, which meant a computation needing that had to be split into two separate launches. A boundary that cannot be crossed is a stronger constraint than one that is merely expensive, and it changes the decomposition rather than its tuning.
- Prefer splitting a computation into phases over coordinating across an expensive boundary. Ending one phase, letting everything drain, and beginning another is often cheaper and always simpler than arranging for distant participants to synchronize mid-flight.

## Don't
- Don't decide the mapping after the cooperation structure is fixed. By then the cooperating parties are wherever the data layout put them, and improving their placement means revisiting the decomposition — which is the expensive change this ordering exists to avoid.
- Don't assume coordination is uniformly priced. Treating a barrier as "a barrier" hides three or four orders of magnitude between the narrowest and widest scopes, and a design that ignores the difference will be dominated by whichever coordination happens to cross the most boundaries.
- Don't push everything to the narrowest scope regardless of fit. Scopes have capacity limits, and forcing cooperation into one that barely holds it constrains every other dimension of the design — group size, resource budget, and data layout all get bent to preserve a locality that may not have been the constraint.
- Don't reason about placement from a diagram of the machine you were told about. The number of levels, their sizes, and what coordination each supports vary by generation and vendor, so the structure is worth querying rather than assuming.
- Don't leave the scope undocumented once chosen. It is invisible in the code, it constrains every later change to the decomposition, and the next person will reasonably assume any participant can coordinate with any other.

## Checklist
- Which participants in this design actually need to coordinate, and how often?
- What is the narrowest level of the hardware that can contain each cooperating set?
- Does the mapping put those participants there, or does it scatter them?
- Is the coordination mechanism the cheapest one the shared scope offers?
- Is membership of the cooperating set named somewhere, or recomputed at each site?
- Is there a boundary here that cannot be crossed at all rather than merely expensively?

## Notes
The reason this is worth treating as a decision rather than an optimization is that it is decided early whether or not anyone decides it. Carving up the work determines who must talk to whom; mapping the pieces determines how far apart they sit. Both happen at design time, and if only the first is done deliberately then the second is left to whatever made the data layout convenient — which has no reason to place cooperating parties near each other and usually does not.

The cost structure is what makes this matter more than it looks. Coordination is not one thing with one price; it is a sequence of mechanisms at very different costs, and which one you get is a consequence of placement rather than a choice made at the point of use. That is why the same logical barrier can be nearly free or dominate the computation, with nothing in the source to distinguish the cases.

Worth carrying alongside: this is the same reasoning that makes deliberately unfair locks fast on clustered hardware, and the same reasoning behind keeping a working set near the processor that uses it. Those look like three separate topics — synchronization, scheduling, and memory layout — and they are one observation about hierarchy applied at three points. Recognizing that is what lets a technique learned in one of them transfer to the others rather than being relearned.

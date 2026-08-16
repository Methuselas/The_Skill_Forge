---
object_id: PAT_wrap_a_structure_completely_or_not_at_all
object_type: pattern
name: Wrap a Structure Completely or Not at All
library_path:
- software-engineering
- core
- abstraction
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- abstraction
- access_routines
- data_structures
- information_hiding
cross_links:
- rel: related_to
  target_object_id: PAT_guard_the_interface_abstraction_under_modification
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
- rel: related_to
  target_object_id: PAT_avoid_global_state_inject_shared_state
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Wrap a Structure Completely or Not at All

## Pattern Rule
**IF** you are putting access routines over a data structure
**THEN** cover every operation on it, and pitch each routine at the problem the program is solving rather than at the structure underneath — a partial wrapper leaves readers holding two models of the same data and unable to tell which one applies where.
**ELSE** if only one operation is worth wrapping, that is a signal the structure wants a different design rather than a partial interface, so decide that before writing the first routine.

## Do
- Write the routine at the level of the entity, not the container. Three separate places that all say `node = node.next` become `NextAccount(account)`, `NextEmployee(employee)`, and `NextRateLevel(rateLevel)` — the same operation on the structure, three different operations in the problem, and the wrapper is what makes them distinguishable.
- Pair every read with a write at the same level. An interface offering an initializer and a push while callers pop by reaching into the array directly is not a partly-abstracted structure; it is two interfaces to one thing.
- Watch for the specific way the inconsistency arrives, because it is predictable rather than careless. During construction the complicated operations get made into routines — inserting into a priority queue takes several lines to find the position, shift what follows, and adjust the ends — while the trivial ones stay inline because writing them out was easier than naming them. The split then follows how hard each operation was to write, which has nothing to do with how the interface should be divided.
- Let the wrapper carry the checks that would otherwise be everyone's job. Pushing through a routine gives you one place to test for overflow; pushing by assigning into the array at the current top index gives every call site that responsibility, and one of them will skip it.
- Take the readability gain even when it is small. Replacing a comparison of a line count against a maximum with a call that asks whether the page is full documents the intent of the test in the code, and it is the accumulation of decisions at that scale that separates well-built software from software that merely works.

## Don't
- Don't build a wrapper that restates the structure. A routine that renames the traversal without naming what is being traversed has added a call and hidden nothing — the point is that direct structure access does two things at once, showing both the mechanical step and the domain step, and a wrapper earns its place by separating them.
- Don't leave the simple operations raw because they are obviously safe. Their being obvious is what makes the interface inconsistent, and a reader now has to check each operation against both models before trusting it.
- Don't treat a half-wrapped structure as progress toward a wrapped one. It is worse than the unwrapped version for reading, because the presence of routines implies the raw accesses were a deliberate exception when they were only an accident of effort.

## Checklist
- List every operation performed on this structure anywhere in the program. Which go through a routine?
- Does each routine name something in the problem, or does it name a step in the container?
- If you read through a routine here, do you also write through one?
- Which routines exist because the operation was hard to write inline rather than because it belonged in the interface?
- Is there a check that every caller currently has to remember, which the wrapper could perform once?

## Notes
The argument for completeness is about what a reader can assume rather than about tidiness. A fully wrapped structure lets someone reason about the data by reading one small interface; an unwrapped one at least tells them honestly that they must read every site. The half-wrapped case gives them the appearance of the first and the obligation of the second, and there is no way to tell from a call site which kind of access they are looking at without checking.

The level question and the completeness question are separate failures that tend to travel together. A wrapper pitched at the structure — a routine that advances a link and says so — is easy to write for every operation and buys almost nothing, so it stays complete and useless. A wrapper pitched at the problem is worth writing but is more effort per operation, so it tends to get written only where the effort was already unavoidable, which is where the incompleteness comes from. Recognizing that both pressures point the same way is what makes the discipline stick: decide the level first, then commit to covering everything at that level.

The event-queue case shows the mechanism plainly. Reading the front and back of the queue are one-liners and stay inline; inserting requires finding a position, making room, and adjusting the ends, so it becomes a routine; removing is comparably involved and becomes one too. The result is an interface where two operations are named for what they mean and two are exposed as array indexing, and nobody decided that — it fell out of how much typing each one took.

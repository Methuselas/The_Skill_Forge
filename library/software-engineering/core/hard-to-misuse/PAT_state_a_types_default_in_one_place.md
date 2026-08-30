---
object_id: PAT_state_a_types_default_in_one_place
object_type: pattern
name: A Default Stated Three Times Will Drift
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- state
- serialization
- initialization
- consistency
- maintenance
cross_links:
- rel: related_to
  target_object_id: PAT_single_source_of_truth_for_data
- rel: related_to
  target_object_id: PAT_describe_data_by_meaning_when_it_leaves_the_machine
- rel: related_to
  target_object_id: PAT_make_immutability_deep
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted sources
confidence: medium
references: []
variants: []
---

# A Default Stated Three Times Will Drift

## Pattern Rule
**IF** a type says what its default state is in more than one place — a member initializer, a reset or clear path, a factory that builds a fresh instance, or the condition under which a writer omits a field
**THEN** derive them from one definition, and where the language will not allow that, list the sites in one place and visit all of them whenever any one changes, because nothing else will bring them back into agreement
**ELSE** where the default is written once and every other site reads it, there is nothing here to keep in step and this does not apply.

## Do
- Count the sites before assuming there is one. Construction is the obvious site. A reset that returns an existing instance to its initial state is a second, and it is written by hand field by field. A writer that omits a field when it holds its default is a third, and it is the easiest to miss because it states the default as a condition rather than as a value.
- Implement a reset by assigning a freshly constructed instance rather than by clearing fields one at a time. A hand-written reset can omit a field, and the omission is invisible: what is missing is not on the screen, and the reset reads as complete because everything it does mention is correct.
- Recognise what an omit-when-default writer buys, so the coupling is taken deliberately. Absent-means-default is what lets a format stay readable by older and newer code without a version number, and it is exactly the coupling that fails silently — change the reader's default and every previously written record now means something else, with nothing to report.
- Check a reset path against the type's declaration rather than by reading the reset. Reading tells you the listed fields are handled; only the declaration tells you which fields were never listed.
- Test the round trip instead of the sites. Write a default-constructed instance, read it back, and compare against a fresh one. That single test covers the writer's condition, the reader's default and the initializer together, and it fails when any of the three moves.
- Make adding a field visit the other sites. Where the language offers no help, the cheapest mechanism is a comment at the declaration naming where else the default lives, because the person adding a field is reading the declaration and nothing else.

## Don't
- Don't assume a reset covers a field because the type does. The two lists are maintained separately and only one of them is checked by the compiler.
- Don't treat absent-means-default as a detail of the format. It is a contract between the writer's condition and the reader's initializer, and it is the only one of the three sites that binds two different pieces of code together.
- Don't rely on a test that constructs, mutates, then resets and checks the mutated fields. It passes while a field nobody thought to mutate stays dirty, which is the case the reset was missing in the first place.
- Don't let a partial reset be defended by its callers. That the surviving field happens to be harmless for today's callers is a fact about today's callers, and the reset is where the next one will look for its guarantee.

## Checklist
- How many places state this type's default state, counting the writer's omit condition?
- Does the reset cover every field the declaration does, checked against the declaration rather than by reading the reset?
- If the writer omits fields at their default, is its condition using the same value the reader initializes to?
- Would a round trip of a default-constructed instance produce something identical to a fresh one?
- When somebody adds a field, what makes them visit the other sites?

## Notes
The three sites are easy to miss as a set because they do not look like the same thing. An initializer states a value, a reset performs assignments, and a writer states a predicate — and only the first is obviously about defaults. They are nonetheless one fact expressed three ways, and the type is consistent only while all three agree. The drift is silent in every direction: a reset that forgets a field leaves stale data in an object the caller believes is fresh; a writer whose condition no longer matches the reader's default silently changes the meaning of every record already written.

The serialization site deserves the most care because it is the only one that couples two separate pieces of code rather than two parts of one class. Omitting a field when it holds its default is a good technique — it keeps files small and lets readers of different vintages share a format without a version number — and what it costs is that the default becomes part of the format rather than an implementation detail. Changing it is then a compatibility decision, which is not what changing an initializer usually feels like.

Assigning a fresh instance is the repair worth reaching for first, because it converts the problem from one requiring vigilance into one the compiler handles: a newly added field is initialized by the same declaration that introduced it, and no separate list has to be updated. Where that is not possible — a type too expensive to rebuild, or a reset that must preserve some fields deliberately — the preserved fields are the interesting ones and belong in a comment saying why they survive, since a reader otherwise cannot distinguish a deliberate exception from a forgotten line.

---
object_id: PAT_choose_the_map_update_call_that_does_not_construct_twice
object_type: pattern
name: Choose the Map Update Call That Does Not Construct Twice
library_path:
- software-engineering
- languages
- cpp
- containers
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- containers
- efficiency
- api_design
- lookup
cross_links:
- rel: related_to
  target_object_id: PAT_tell_equality_from_equivalence_when_looking_up
- rel: related_to
  target_object_id: PAT_consider_emplacement_where_it_can_actually_help
- rel: related_to
  target_object_id: PAT_dont_add_a_default_constructor_a_class_cannot_honor
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Choose the Map Update Call That Does Not Construct Twice

## Pattern Rule
**IF** you are putting a value into a keyed associative container and the mapped type is not trivially cheap to build
**THEN** pick the call by whether the key is expected to be present already — subscripting for updating something that is there, an insertion for adding something that is not — because subscripting an absent key builds a default object and then assigns over it, while inserting under a present key builds a whole pair that is then discarded
**ELSE** where the mapped type is a built-in or a small aggregate, both cost essentially nothing and subscripting is the clearer spelling.

## Do
- Read subscripting on these containers for what it is, which is unrelated to subscripting anything else. It means add-or-update: it returns a reference to the mapped value for that key, and where no such key exists it first creates one by default-constructing the mapped value.
- Follow that definition to the cost. Adding a new entry by subscripting and assigning builds a default object, assigns to it, and destroys the temporary that was assigned from — three calls that adding by insertion does not make, because insertion builds the value once, in place, from what you supplied.
- Follow it to the reverse cost too. Updating an existing entry by insertion requires constructing the pair to pass as the argument, which constructs a mapped value that is then thrown away because the key was already present; subscripting constructs nothing.
- Reach for the calls that settle this rather than choosing between the old two, where they are available: one that constructs the mapped value only if the key turns out to be absent, and one that assigns over the existing value or inserts a new entry as appropriate. Between them they give the efficient behavior in both directions without requiring you to predict which case you are in.
- Supply a placement hint when you already know where the entry belongs — from a preceding bound search, for instance — which makes the insertion constant rather than logarithmic.

## Don't
- Don't reach for subscripting to test whether a key is present. It inserts a default-constructed entry as a side effect of asking, so the question changes the answer, and the container quietly accumulates entries nobody put there.
- Don't assume the mapped type can be default-constructed at all. Subscripting requires it, so a mapped type that has no sensible argument-free construction cannot be used with subscripting even where it would be efficient.
- Don't hand-write the efficient add-or-update helper any more. It was worth writing when the library offered only the two calls above; the library now offers both behaviors directly, and a hand-rolled version is a maintenance liability that duplicates them.

## Checklist
- Is this call adding an entry, updating one, or genuinely either?
- Is subscripting being used anywhere merely to check for presence?
- Does the mapped type have a default constructor, and does it cost anything?
- Is a call available that constructs the mapped value only when it is actually needed?
- Is a position already known from a previous search that could serve as a hint?

## Notes
The trap is the reasonable assumption that subscripting a container is a lookup. On the keyed associative containers it is not — it is an insertion that returns a reference — and the entries it silently creates are the failure people meet before they ever meet the performance question. A read-only-looking expression that modifies the container is unusual enough to be worth flagging on its own.

Meyers works up to a helper function that gets the best of both by locating the position with a bound search, testing equivalence there, and either assigning or inserting with that position as a hint. The reasoning is worth following because it shows what "efficient" actually requires: one traversal rather than two, and no constructed value that goes unused.

The library has since supplied both behaviors directly, which retires the helper and simplifies the decision to picking the right call. That is a case where a technique earning its place in a book has been absorbed into the standard, and the durable residue is the cost model rather than the code.

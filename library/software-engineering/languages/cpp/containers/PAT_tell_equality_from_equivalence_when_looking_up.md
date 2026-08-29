---
object_id: PAT_tell_equality_from_equivalence_when_looking_up
object_type: pattern
name: Tell Equality From Equivalence When Looking Up
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
- lookup
- comparison
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: related_to
  target_object_id: AP_settle_a_containers_contract_before_filling_it
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Tell Equality From Equivalence When Looking Up

## Pattern Rule
**IF** you are searching an ordered associative container, or reasoning about whether it already holds some value
**THEN** work out which notion of sameness applies — the container answers by equivalence, meaning neither value precedes the other under its ordering, while the free-standing search algorithms answer by equality, meaning the equality operator says yes — because for any container whose ordering ignores part of the value, the two give different answers
**ELSE** where the ordering is the natural one and nothing about the value is ignored by it, the two coincide and the distinction costs nothing to ignore.

## Do
- Write out the equivalence test when you need to reason about it, since it is not an operator and has no spelling of its own: two values are equivalent when the container's ordering says neither comes before the other. Every ordered associative container exposes its ordering, so this is a question you can put to the container directly.
- Prefer the container's own member search over the free-standing algorithm of the same name on these containers. The member uses the container's ordering and finds things by equivalence in logarithmic time; the free-standing one walks the range comparing with the equality operator, which is both slower and answers a different question.
- Expect the two to disagree exactly where the ordering deliberately ignores something. A container ordered by a case-insensitive comparison treats two spellings as the same value, so inserting the second one does nothing, the member search finds it, and the free-standing search does not.
- Recognize that a value's equality operator is free to ignore parts of the object too — a last-accessed timestamp, a cached field — so equality does not imply that every member matches either.

## Don't
- Don't assume a failed insertion means the container holds an equal value. It means the container holds an equivalent one, and if the ordering ignores part of the value, those can differ in ways that matter to the code reading the container later.
- Don't carry this conclusion over to the hash-based associative containers without checking. Those settle sameness by equality rather than by equivalence, because they have no ordering to define equivalence against — so the two families of associative container answer this question differently on purpose.

## Checklist
- Does this container's ordering ignore any part of the value?
- Is the search a member of the container or a free-standing algorithm?
- If an insertion was rejected, which notion of sameness rejected it?
- Is the container ordered or hash-based, and which notion does that family use?

## Notes
The reason the ordered containers settle on equivalence is worth knowing, because it makes the behavior look deliberate rather than arbitrary. Being kept in order, they already require one comparison function; defining sameness in terms of it means clients supply exactly one. Supporting equality as well would mean a second function, and then two values could be unequal but indistinguishable to the ordering — leaving the container with no defined place to put the second one, and no consistent answer about whether it is present.

That trade explains the otherwise startling fact that a member search and a free-standing search of the same name over the same container can return different answers. Neither is broken; they are answering different questions, and only one of them is using the container's own notion of what its elements mean.

Once ordering is out of the picture the trade changes, which is why the hash-based containers went the other way and take an equality predicate. It is the same question resolved under different constraints rather than an inconsistency in the library.

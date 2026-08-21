---
object_id: PAT_remember_an_algorithm_cannot_change_a_containers_size
object_type: pattern
name: Remember an Algorithm Cannot Change a Container's Size
library_path:
- software-engineering
- languages
- cpp
- algorithms
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- algorithms
- containers
- resource_management
- idioms
cross_links:
- rel: related_to
  target_object_id: PAT_recover_the_iterator_from_erase_rather_than_advancing_it
- rel: related_to
  target_object_id: PAT_decide_what_a_container_holds
- rel: related_to
  target_object_id: PAT_choose_the_weakest_ordering_operation_that_does_the_job
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Remember an Algorithm Cannot Change a Container's Size

## Pattern Rule
**IF** you called an algorithm whose name suggests elements go away — removing by value, removing by predicate, collapsing adjacent duplicates — and expected the container to get shorter
**THEN** understand that it did not and could not, and pair the call with the container's own erase over the leftover tail if you want the elements actually gone
**ELSE** where the container is a linked list, its like-named member function does both jobs at once and does them more efficiently than the pairing.

## Do
- Trace the reason rather than memorizing the rule, because it explains a whole family of surprises at once. An algorithm receives iterators, not a container; nothing lets it recover the container from an iterator; and only a container's own members can change how many elements it holds. Everything else here follows.
- Picture what the call actually does: it walks the range and shifts the elements you are keeping forward over the ones you are not, then hands back an iterator to the position after the last kept element — the new logical end.
- Pass that returned iterator and the container's real end to the range form of erase. That pairing is idiomatic enough to read as a single operation, which is what it is.
- Reach for the free-standing removal functions where they exist, since they perform both halves and take the container, so the failure this card describes cannot arise.
- Expect nothing of the tail beyond the new logical end. Implementations commonly leave the old values there and the standard does not require it, so the removed values may or may not still be present — and there are typically fewer of them than you removed.

## Don't
- Don't apply these to a container of raw owning pointers. Compacting overwrites the pointers you are discarding with the ones you are keeping, so the only references to those objects are gone before you get a chance to release them — the leak has already happened by the time you call erase. Partition instead, or release and null the pointers first and then compact away the nulls, or hold owning handles so the question does not arise.
- Don't apply the removal *algorithm* to an ordered associative container. It works by assigning over elements, which for a container maintaining an ordering means writing over keys.
- Don't expect the collapsing operation to remove all duplicates from an unsorted range. It eliminates all but the first of each *adjacent* group, so the range has to be ordered first for it to mean what people usually intend.

## Checklist
- After the call, is the container's element count expected to change, and does the code depend on that?
- Is the returned iterator captured and passed to erase, or discarded?
- Does the container hold raw pointers to objects that need releasing?
- If duplicates are being collapsed, is the range sorted?

## Notes
This is the most misunderstood corner of the algorithm library and the misunderstanding is structural rather than careless. The naming promises removal, the call compiles, it runs, and the container reports the same number of elements afterwards as before — so the natural conclusion is that the call did nothing, when in fact it did exactly half of what was wanted.

The pointer case deserves its own attention because the damage is done earlier than instinct suggests. The worry that surfaces is about the erase, since destroying a raw pointer releases nothing — but by then the pointers to the discarded objects have already been overwritten during the compaction, so no amount of care at the erase can recover them. This is the sharpest argument available for holding owning handles rather than raw pointers in a container.

The same "an algorithm sees a range, not a container" framing explains a neighbouring contract worth knowing: the operation that folds a range into a single summary value requires that the function it is given have no side effects and not disturb the range, while the operation that simply visits each element imposes no such restriction and hands the function object back to you afterwards. Both restrictions come from what the algorithm is permitted to assume about the range while it works.

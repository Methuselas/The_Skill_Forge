---
object_id: PAT_change_an_associative_element_without_breaking_its_ordering
object_type: pattern
name: Change an Associative Element Without Breaking Its Ordering
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
- invariants
- casting
- undefined_behavior
cross_links:
- rel: related_to
  target_object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
- rel: related_to
  target_object_id: PAT_minimize_and_prefer_cpp_style_casts
- rel: related_to
  target_object_id: PAT_recover_the_iterator_from_erase_rather_than_advancing_it
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Change an Associative Element Without Breaking Its Ordering

## Pattern Rule
**IF** an element already inside an ordered associative container needs to change
**THEN** change it only if the part changing has no bearing on the container's ordering, and take the element out and put it back when it does — because the container's correctness rests on being sorted, and it has no way to notice that you moved an element out from under its own position
**ELSE** where the container is keyed and the change is to the mapped part rather than the key, the key is protected by the type system and ordinary assignment through the iterator is fine.

## Do
- Split the element mentally into the part the ordering consults and the part it does not, because that split is the whole decision. Elements of a set ordered by an identifier can have every other field rewritten in place without endangering anything; the identifier itself cannot.
- Take the element out when the ordering-relevant part must change, and use the five-step form: find it, copy it, erase it, modify the copy, insert the copy. Pass the iterator you found as a placement hint to the insertion when the new position will be near the old one, which makes that insertion constant rather than logarithmic.
- Reach for node extraction where it is available, which is the direct expression of the same idea: detach the node, change the key on the detached node, and reinsert it. It moves no elements and allocates nothing, so it does what the five-step form does without the copy.
- Cast to a reference, not to a value, on the rare occasion a cast is the right tool. Casting to the element type produces a temporary copy, so the modification lands on the copy and the container is untouched — code that compiles, runs, and silently does nothing.

## Don't
- Don't change an ordering-relevant part in place and assume the container will cope. It will not re-sort itself, so the element stays where its old value put it, and every later lookup, insertion, and range query navigates a structure whose sortedness is a lie.
- Don't cast away the constness of a key in a keyed container. The key is const by specification, an implementation is entitled to place it in memory that cannot be written, and the standard gives you nothing if you try.
- Don't take the ability to modify a set element as permission from the language. That the elements were not const was an inconsistency in the specification rather than an endorsement, different implementations read it differently, and code relying on it was never portable.

## Checklist
- Which parts of this element does the container's ordering actually consult?
- Is the part being changed one of them?
- If it is, is the element removed and reinserted rather than edited in place?
- If a cast is involved, is it to a reference?
- Is a placement hint being supplied when the new position is near the old one?

## Notes
The asymmetry between the keyed and unkeyed associative containers used to be the source of most of the trouble here, and it has since been settled. Keyed containers protect the key with const and always have. Unkeyed ones stored their elements without const, which appeared to permit modification, and the specification was inconsistent enough that some implementations added the const anyway and rejected the code. The resolution went against modification: element access is now const in both, so the compiler enforces what was previously only advice.

Node extraction is the genuinely new capability and it changes what the good answer looks like. The five-step form works and costs a copy of the element plus the destruction of the original; extraction detaches the existing node, hands it to you with a mutable key, and reinserts the same node. For elements expensive to copy, or held by types that cannot be copied at all, that is the difference between possible and not.

The cast-to-a-value trap is worth carrying separately from the rest, because it is the failure that produces no symptom. Nothing fails to compile, nothing throws, no invariant breaks — the modification simply happens to a temporary that is destroyed at the end of the statement, and the container reads exactly as it did before.

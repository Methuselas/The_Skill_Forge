---
object_id: PAT_convert_a_reverse_iterator_with_base_and_mind_the_offset
object_type: pattern
name: Convert a Reverse Iterator With Base and Mind the Offset
library_path:
- software-engineering
- languages
- cpp
- iterators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- iterators
- containers
- avoiding_surprises
- off_by_one
cross_links:
- rel: related_to
  target_object_id: PAT_recover_the_iterator_from_erase_rather_than_advancing_it
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Convert a Reverse Iterator With Base and Mind the Offset

## Pattern Rule
**IF** you found a position by searching backwards and now need to insert or erase there, which requires a forward iterator
**THEN** convert with the reverse iterator's base accessor, and then decide which operation you are performing — the converted iterator is the right position for inserting and one past the right position for erasing
**ELSE** where you only need to read or write the element the reverse iterator denotes, dereference it directly and no conversion arises.

## Do
- Fix the offset in your head once rather than deriving it each time: a reverse iterator denotes the element *before* the one its base denotes, mirroring the way the reverse beginning and end are positioned against the forward ones.
- Insert at the base position directly. Insertion happens in front of the position given, and in a backwards traversal "in front of" is on the other side — so the offset cancels out and the base is exactly the position you want.
- Erase the element *preceding* the base position, because there the offset does not cancel. Get there by advancing the reverse iterator first and then taking its base, rather than by taking the base and stepping back from it.
- Prefer that spelling even where the other one compiles. Stepping back from the base fails to build wherever the container's iterators are plain pointers, since the result of a function call is not something you may modify — and that is exactly the case for the contiguous containers on many implementations.
- Keep the conversion lattice in view when planning any of this: a plain iterator converts implicitly to a constant one and to a reverse one, and a reverse one converts to a constant reverse one, but nothing converts a constant iterator back to a mutable one.

## Don't
- Don't describe the base as "the corresponding iterator" and leave it there. It corresponds for insertion and does not for erasure, and treating the two cases alike gives an off-by-one error that removes the neighbour of the element you meant.
- Don't reach for a cast to get a mutable iterator from a constant one. For most containers those are unrelated class types and no cast connects them; where the containers use plain pointers a cast may compile and appear to work, which makes it a portability trap rather than a solution.

## Checklist
- Is the converted iterator being used to insert or to erase?
- If erasing, is the reverse iterator advanced before the base is taken, rather than the base being stepped back?
- Would this code build if the container's iterators were plain pointers?
- Is anything trying to obtain a mutable iterator from a constant one?

## Notes
The offset exists because a reverse traversal has to have somewhere to stop, and the natural mirror of the forward end lands one position across from the forward beginning. Everything about the base accessor follows from that single displacement, so it is worth understanding rather than memorizing the two rules.

Item 26 of the source, which this material sits under, has since been inverted and should not be followed. It advises preferring mutable iterators over constant ones, on two grounds that were both true then and are both false now: that the container's insert and erase members would accept nothing else, and that mixing the two types in one comparison broke on some implementations. Those members take constant iterators today, the containers supply accessors returning them, and Meyers himself later reversed the recommendation. The modern default is the constant one, and the only durable part of the original item is the conversion lattice above.

The associated technique for manufacturing a mutable iterator from a constant one — starting at the beginning and advancing by the measured distance — went obsolete with the advice that motivated it. It is worth recognizing in older code, where it usually signals someone working around a restriction that no longer exists.

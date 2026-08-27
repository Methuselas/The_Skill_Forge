---
object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
object_type: pattern
name: Give an Ordered Container a Comparison Type That Is a Strict Weak Ordering
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
- comparison
- undefined_behavior
- invariants
cross_links:
- rel: related_to
  target_object_id: PAT_tell_equality_from_equivalence_when_looking_up
- rel: related_to
  target_object_id: PAT_decide_what_a_container_holds
- rel: related_to
  target_object_id: PAT_treat_undefined_behavior_as_a_whole_program_assumption
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants:
- variant_id: VAR_supply_a_hash_and_an_equality_for_an_unordered_container
  variant_name: Supply a Hash and an Equality for an Unordered Container
  variant_basis: context
  difference_from_foundation: The foundation covers what an ordered container asks of a key type, which is a single comparison meaning "precedes," and it is the whole requirement because the container's invariant is that its elements are sorted. An unordered container has a different invariant and therefore asks for different machinery — two pieces rather than one. It needs a hash to decide where a key belongs, and it needs an equality to distinguish keys that landed in the same place. Neither is a comparison, and a type that has no meaningful order can still supply both, which is what makes this the available route for a key that genuinely does not sort. A coordinate pair is the standard case, since one direction is not smaller or larger than another, merely different. The mechanism also differs. The foundation's comparison is most naturally supplied as a type passed to the container, whereas the two pieces here can be supplied either as template arguments or by specializing the library's default hash for your key type, and the specialization is the more general of the two because it then serves every container and algorithm that reaches for the default rather than only the one you are declaring.
  when_to_use: Use when the key type has no meaningful order to give — a direction, a coordinate, an identifier whose bits carry no ranking — or when lookup dominates and the ordered traversal an ordered container provides is not wanted. It is also the route when a sensible order exists but writing one would be inventing a ranking nobody needs, which is a signal the ordering was never part of the type's meaning.
  when_not_to_use: Do not take it where iteration in key order is part of what the container is for, since an unordered container gives no order at all and adding a sort afterwards discards the advantage. Prefer the foundation where the key already orders naturally, because supplying nothing is better than supplying two pieces that must agree with each other.
  absorbed_from_object_id: none
---

# Give an Ordered Container a Comparison Type That Is a Strict Weak Ordering

## Pattern Rule
**IF** you are supplying the comparison an ordered associative container or a sorting algorithm will use
**THEN** make it a type rather than a function, make it dereference where the elements are pointers or pointer-like, and above all make it return false whenever the two arguments are the same value — because the return value means "the first precedes the second," and nothing precedes itself
**ELSE** where the elements order naturally and are held by value, the default comparison already satisfies all of this and supplying one of your own only adds a way to get it wrong.

## Do
- Supply a type, since all three of the container's template arguments are types. A comparison function is a function, not a type, so passing its name where the container wants a comparison will not compile; wrap it in a class with a call operator, or use a lambda's type.
- Write the comparison for pointer elements to dereference, because the default orders by pointer value. A container of pointers to strings sorts by address, which is essentially a random order that looks correct just often enough to be missed — one arrangement in twenty-four, for four elements.
- Keep a small generic dereferencing comparison to hand rather than writing one per element type, and apply it to smart pointers and iterators too, which have the same problem for the same reason.
- Get a descending order by exchanging the operands rather than by negating the test. Negating "precedes" gives "does not precede," which is true for equal values and therefore invalid; swapping the arguments gives the reverse ordering and stays valid.

## Don't
- Don't supply a comparison that returns true for two equal values. The container tests sameness by asking whether neither argument precedes the other, so a comparison answering "yes, it precedes" for a value against itself reports that a value differs from itself — and the container duly inserts a second copy, so a container that forbids duplicates ends up holding two.
- Don't assume the duplicate-permitting containers are exempt. They will store both copies, which is their job, but the range-lookup operation gathers values the ordering calls equivalent — so under a broken comparison the two copies are not equivalent and no single range can contain them both.
- Don't reach for the ready-made comparison objects that include equality. The one meaning "less than or equal" looks like a harmless way to say "sorted ascending" and is exactly the failure above.

## Checklist
- Is the comparison a type, or has a function name been passed where a type belongs?
- If the elements are pointers or pointer-like, does the comparison dereference them?
- Given two arguments of the same value, does the comparison return false?
- Was any reversed ordering obtained by negating a test rather than by swapping operands?

## Notes
The single rule underneath all of this is that the comparison answers "does the first argument come before the second in the order you want." Once it is read that way rather than as a general-purpose "is this smaller," the constraint stops needing to be memorized: equal values do not come before one another, so the answer for them is no.

`VAR_supply_a_hash_and_an_equality_for_an_unordered_container` covers the same question — what does this container require of my key type — asked of the other container family. An ordered container wants one comparison because its invariant is that it stays sorted. An unordered container has no such invariant and wants two pieces instead: a hash to decide where the key belongs, and an equality to separate keys that land together. The practical consequence is that a type with no meaningful order is not shut out of associative lookup, which is the situation that sends people looking — a coordinate is not smaller or larger than another coordinate, only different, and inventing a ranking to satisfy an ordered container would be fabricating meaning the type does not have. Either piece may be passed to the container as a template argument, or the library's default hash may be specialized for the key type; the specialization is the broader move, since it serves everything that reaches for the default rather than the one container you are declaring. Stay with the foundation wherever iteration in key order is part of the point, because an unordered container gives no order to iterate in.

The formal name for what the standard requires is a strict weak ordering, and the full definition is not especially illuminating to work through. The clause that catches real code is the one above, and it catches it most often through the negate-the-existing-comparison shortcut when someone needs a descending order — which is a plausible-looking edit to working code that quietly makes it invalid.

The consequence is corruption rather than a diagnostic. The container's invariant is that it is sorted and holds no equivalent duplicates; a comparison that misreports equal values breaks the second, and everything downstream — lookups, range queries, iteration order — is then operating on a structure whose invariant no longer holds. The standard calls the result undefined, and in practice what you get is a container that is quietly no longer the kind of container you asked for.

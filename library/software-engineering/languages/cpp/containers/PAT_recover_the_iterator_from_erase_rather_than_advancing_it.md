---
object_id: PAT_recover_the_iterator_from_erase_rather_than_advancing_it
object_type: pattern
name: Recover the Iterator From Erase Rather Than Advancing It
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
- iterator_invalidation
- undefined_behavior
- idioms
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: related_to
  target_object_id: PAT_treat_undefined_behavior_as_a_whole_program_assumption
- rel: related_to
  target_object_id: PAT_prefer_range_member_functions_to_repeated_single_element_calls
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Recover the Iterator From Erase Rather Than Advancing It

## Pattern Rule
**IF** you are walking a container and erasing some of its elements as you go, because each erasure needs work the bulk removal facilities cannot do
**THEN** take the next iterator from what the erase returns and never touch the one you handed it, since erasing invalidates that iterator and on a contiguous container invalidates every iterator past it as well — and where the container's erase returns nothing to take, advance first and erase the copy you kept
**ELSE** where nothing extra needs doing per element, the free removal function taking a value or a predicate does the whole job and there is no loop to get wrong.

## Do
- Reach for bulk removal before writing any loop, and pick the form the container actually supports: the remove-then-erase pairing for the contiguous containers, the member erase taking a value for the ordered associative ones — which is logarithmic rather than linear, and matches on the container's ordering rather than on equality — and the member remove for a linked list.
- Where the loop is genuinely needed, structure it so the increment happens in exactly one of the two branches: assign the erase's result to the iterator when you erase, and increment it when you do not. Leave the loop's own increment clause empty.
- Say why the loop exists, since the reason is the only justification for hand-writing something the library otherwise does. Logging each removal, releasing a resource the element owns, or accumulating a count are the usual ones.

## Don't
- Don't erase through an iterator and then increment it. The erase has already invalidated it, so the increment reads memory the container no longer maintains — and this compiles, usually appears to work, and is the single most common way of getting element removal wrong.
- Don't write the post-increment form in new code *against a standard container*. Passing a post-incremented iterator to erase is the idiom filling existing codebases, and it is there for a reason that expired there: the associative containers' erase used to return nothing, so there was no result to recover from. It has returned an iterator since C++11, and the return-value form now works on every standard container while the post-increment form still does not work on the contiguous ones.
- Don't carry that conclusion to a container the standard does not define. A container written in-house, or wrapping something else, may erase and return nothing — and then the reason the post-increment idiom exists has not expired at all, it is the only correct form, and reaching for the return value produces code that does not compile. Check the signature before choosing the shape of the loop; this is one line of reading and the two forms are not interchangeable.
- Don't use the removal *algorithm* on an ordered associative container. It works by overwriting elements with later ones, which for a container maintaining an ordering means writing over keys — corrupting the ordering rather than removing anything, where it compiles at all.

## Checklist
- Could a bulk removal facility do this without a loop?
- In the loop, is the iterator advanced in exactly one place per branch?
- Is the loop's own increment clause empty?
- Does this container's erase return an iterator, or nothing? The answer decides which of
  the two loop shapes is correct, and they are not interchangeable.
- After each erase, does the iterator come from the erase's return value — or, where there
  is no return value, was it advanced before the erase rather than after?
- If the container is associative, is any name resembling "remove" being applied to it?

## Notes
The asymmetry that made this genuinely hard has been repaired, and knowing that it existed explains why so much surviving code looks strange. Meyers had to give a matrix: sequence containers took the return value, associative containers took a post-incremented argument, and choosing wrongly was undefined behavior in one direction and a compile error in the other. Since both categories return an iterator, one form covers all of them.

The remaining trap is the one underneath the matrix and it has not moved. Erasing an element invalidates iterators to it in every container; on the contiguous ones it invalidates everything after it too, which is why no amount of care about where the increment goes rescues a loop that keeps using the old iterator.

Everything above about the repaired asymmetry is scoped to the containers the standard
defines, and that scoping is easy to lose. A project's own container may erase and return
nothing, in which case the historical form is not legacy debt but the only thing that
compiles — and a codebase can hold both kinds, with the two loop shapes correct in
different files. The signature is the thing to read, not the era the code was written in.

Free removal functions taking a value or a predicate now exist for all the standard containers and subsume most of what the original matrix covered, which pushes the hand-written loop into the narrow case where something must happen per element beyond its removal. That is worth checking before writing the loop, since a loop not written cannot get this wrong.

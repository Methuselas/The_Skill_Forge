---
object_id: PAT_write_a_missing_algorithm_in_the_librarys_own_shape
object_type: pattern
name: Write a Missing Algorithm in the Library's Own Shape
library_path:
- software-engineering
- languages
- cpp
- algorithms
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- algorithms
- iterators
- reusability
cross_links:
- rel: related_to
  target_object_id: PAT_reach_for_a_named_algorithm_before_writing_the_loop
- rel: related_to
  target_object_id: PAT_publish_the_traits_an_iterator_claims_not_just_its_operators
- rel: related_to
  target_object_id: PAT_program_to_a_templates_implicit_interface
- rel: related_to
  target_object_id: PAT_encapsulate_the_container_choice_instead_of_abstracting_over_it
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Write a Missing Algorithm in the Library's Own Shape

## Pattern Rule
**IF** you need an operation over a sequence that the algorithm library does not provide
**THEN** write it as a template taking a pair of iterators rather than a container, and add a container-taking overload that forwards to it
**ELSE** where the operation genuinely depends on one container's representation rather than on its elements, take that container and say so — generality there would be pretense.

## Do
- Take the range as two positions, because that is what buys the reach. Written against a container type, the function serves that container; written against a pair of positions, the same body serves every sequence in the library, a raw array, and anything else able to hand back a start and an end — including things that did not exist when it was written, which is how a utility written for one vector turns out to work unchanged on a linked list of a different element type and on a lazily computed view.
- Add the convenience overload instead of choosing between the two forms. The iterator form composes and the container form reads well at the call site; the second is one forwarding line on top of the first, so there is no reason to pick.
- Hand back something the caller can keep using. Returning the stream, or the destination position, lets the call sit inside a larger expression the way the library's own algorithms do, rather than forcing a statement of its own.
- Put it in a namespace of your own. A function filling a gap in the library gets the name the library would have used, is called unqualified beside library algorithms, and is therefore the single most likely thing to collide when a later standard fills the same gap.
- Lift a boundary element out of the loop where the operation has one. Separator joining is the standard case, and it is worth knowing as a shape rather than as a trick: a separator belongs between elements rather than after each, so emitting the first element before the loop and then emitting each remaining element behind its separator removes the trailing-separator problem instead of correcting it afterwards.

## Don't
- Don't write against a container type out of habit. It is the more obvious spelling and it silently costs the function every other sequence, including the ones the caller will have next year.
- Don't write it before checking what the library calls it. The gap is often a naming gap rather than a real one, and the operation you want may exist under a name that describes the general case rather than yours.
- Don't reach for generality the operation does not have. If it needs to know the container's size in advance, or to insert in the middle, or to rely on contiguous storage, then it is about a container and pretending otherwise produces a template that compiles for arguments it cannot serve.

## Checklist
- Does this operation need the container, or only its elements in order?
- Is the range taken as a pair of positions, so anything that can produce them qualifies?
- Is there a container overload for the common call, forwarding to the iterator form?
- Does it return something usable, or does it force a statement of its own?
- Is it in a namespace where a future standard library cannot collide with it?
- Does the operation have a first or last element that wants handling outside the loop?

## Notes
The point is less about writing algorithms than about noticing which shape a piece of code is. Almost every utility over a sequence starts life written against whichever container prompted it, because that container is what is on the screen; and almost none of them need the container, only its elements in order. The difference between those two shapes costs nothing to choose at the moment of writing and cannot be recovered cheaply later, once callers exist.

What makes the iterator form pay is that the reach is not a prediction. A joining utility written against a pair of positions works on a list of floating-point constants, and on a lazily evaluated view of characters, without either case having been considered — because the only thing it asked for was the ability to move through elements and compare against an end, and those are the two things everything sequence-shaped provides. That is the same property that lets the library's own algorithms work on containers their authors never saw, and it is available to anything written the same way.

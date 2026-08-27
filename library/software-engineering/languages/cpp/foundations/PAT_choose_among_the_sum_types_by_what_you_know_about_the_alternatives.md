---
object_id: PAT_choose_among_the_sum_types_by_what_you_know_about_the_alternatives
object_type: pattern
name: Choose Among the Sum Types by What You Know About the Alternatives
library_path:
- software-engineering
- languages
- cpp
- foundations
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- data_types
- variant
- interface_design
cross_links:
- rel: related_to
  target_object_id: PAT_redesign_away_from_multiple_dispatch
- rel: related_to
  target_object_id: PAT_avoid_returning_magic_values
- rel: related_to
  target_object_id: PAT_use_traits_classes_for_type_info
- rel: related_to
  target_object_id: PAT_choose_pointer_or_reference_by_nullability_and_rebinding
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Choose Among the Sum Types by What You Know About the Alternatives

## Pattern Rule
**IF** a value in your design is one of several things rather than one thing
**THEN** choose the vocabulary type by how much you know about the alternatives at compile time — a value or nothing where there is exactly one real alternative, a closed set where you can name every type, and an open container only where you genuinely cannot
**ELSE** where the alternatives share an interface and differ only in behaviour, a base class and virtual dispatch answers this better than any of them, because the variation is behavioural rather than a difference of type.

## Do
- Take the amount of compile-time knowledge as the axis, because it is what everything else follows from. Knowing there is one alternative and it may be absent, knowing the complete list of alternatives, and knowing nothing are three genuinely different situations, and the library offers a type for each.
- Notice that the retrieval mechanism degrades along the same axis, which is the part worth deciding on. The value-or-nothing type is tested with a boolean and then dereferenced. The closed set can be visited by handing it a callable overloaded for each alternative, and nothing tests any type at all — the dispatch happens because the overload set covers the alternatives. The open container leaves you comparing runtime type identity in a chain of tests, because there is nothing else available.
- Reach for the closed set as soon as you can name the alternatives, and take the exhaustiveness as the reason rather than the storage. Visiting a closed set with a callable that is missing an overload fails to compile; the equivalent omission in a chain of runtime type tests is a branch that silently does nothing, discovered when something reaches it.
- Treat the open container as a signal to look again at the design. It is the right answer when types genuinely arrive from outside your control, and it is frequently reached for when the set was closed all along and simply had not been written down.
- Keep the closed set distinct from the primitive union in your head. It is a tagged union, so it stores which alternative is present and refuses to let you read one alternative as another; the primitive union permits exactly that reinterpretation and is the tool when reading the same bytes two ways is the point. They look similar and solve opposite problems.

## Don't
- Don't reach past the value-or-nothing type when absence is the only alternative. It is the narrowest of them, it says what it means in the signature, and a caller cannot ignore the empty case as easily as it can ignore a sentinel.
- Don't use the open container as a general-purpose value. Every use site has to interrogate the type before it can act, so the type test that was avoided once at construction gets paid for at every point of use, forever.
- Don't retrieve from a closed set by index. The alternatives are numbered in declaration order, so an index test is a claim about the order of the type list, and reordering that list to add an alternative silently changes what every index means.
- Don't assume retrieval is checked. These types offer both a checked accessor that reports failure and an unchecked one that does not — the same split found on indexed containers — and the unchecked form on an absent or wrongly-typed value is undefined rather than diagnosed.

## Checklist
- Is this value one of several things, or one thing that behaves several ways?
- Can every alternative be named when the code is compiled? If so, why is the set not closed here?
- Where the set is closed, is it retrieved by visiting, or by testing a type or an index?
- Would adding an alternative be caught by the compiler, or would it produce a branch nobody wrote?
- Is any retrieval here going through the unchecked accessor, and is the value certain?

## Notes
The three types are usually met one at a time as separate facilities, and the ordering between them is easy to miss because the source that teaches one rarely teaches it beside the others. Setting them in a row makes the shape obvious: each gives up compile-time knowledge in exchange for accepting a wider range of values, and each pays for it in what the code has to do before it can use what it holds.

The exhaustiveness point is the one that pays for itself later rather than now. All three arrangements work on the day they are written, because on that day the author knows the alternatives and handles them. The difference shows up on the day an alternative is added — the closed set stops compiling until the new case is handled, and everything else keeps running while quietly doing nothing for values that did not exist when the branches were written. That is a good reason to close the set even where the open container would have worked.

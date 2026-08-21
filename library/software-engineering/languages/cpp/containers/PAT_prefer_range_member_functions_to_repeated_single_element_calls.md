---
object_id: PAT_prefer_range_member_functions_to_repeated_single_element_calls
object_type: pattern
name: Prefer Range Member Functions to Repeated Single-Element Calls
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
- readability
- algorithms
cross_links:
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: related_to
  target_object_id: PAT_consider_emplacement_where_it_can_actually_help
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Prefer Range Member Functions to Repeated Single-Element Calls

## Pattern Rule
**IF** you are about to add, remove, or replace several elements of a container one call at a time — a loop of appends, repeated single-element insertion, or a copy into an inserting iterator
**THEN** use the member function taking a pair of iterators instead, because the single-element version makes more calls, moves existing elements more times, and reallocates more often than the range version doing the same job
**ELSE** where the elements are not available as a range — computed one at a time, or arriving as they are read — the single-element call is what you have, and reserving capacity in advance recovers most of the difference.

## Do
- Learn the four shapes so you can recognize the opportunity: constructing from a range, inserting a range, erasing a range, and assigning a range. All standard containers offer the first; the sequence containers offer all four.
- Spot the single-element calls that hide under other names. Appending at either end is a single-element insertion, and a copy whose destination is an inserting iterator is a loop of them — so a loop calling either, or a copy with an inserter, marks a place where a range call is likely better.
- Count the three taxes on a contiguous container so the size of the difference is concrete. One call per element rather than one call total; every existing element above the insertion point shifted once per inserted element rather than once in total, which for a hundred inserted elements is ninety-nine percent more moves; and repeated reallocation as capacity is exhausted, where a range insertion given forward iterators can size the allocation once because it can measure the range first.
- Expect a different but real saving on the node-based containers. There is no reallocation and no shifting, but inserting one at a time writes each node's links more than once and rewrites the following node's back link on every insertion.
- Use the assigning form when you are replacing a container's entire contents and plain assignment from another container will not express it.

## Don't
- Don't reach for the copying algorithm with an inserting iterator as the default way to bulk-load a container. It puts the emphasis on the copying, which is the uninteresting part and is happening anyway; the range insertion says what is actually going on, which is that the container is gaining elements.
- Don't expect the movement and allocation savings when the source range is delimited by input iterators. A range insertion reading from a stream cannot measure the range without consuming it, so it is reduced to moving elements one position at a time exactly as the single-element version would.
- Don't assume the argument is only about the contiguous containers. The saving in call count applies everywhere, including the ordered associative containers, where the other two taxes do not arise.

## Checklist
- Does any loop here call a single-element insertion, append, or erase on a container?
- Is any copying algorithm being given an inserting iterator as its destination?
- Are the source elements already available as a range with measurable length?
- When replacing all of a container's contents, is the assigning form being used?

## Notes
The efficiency argument is the one that settles the matter, but it is not the reason to reach for these first. The range forms take less typing and say more directly what is happening, and those two properties are available on every container including the ones where the performance difference is only the call count. Meyers presents efficiency last, as the thing that converts a style preference into a decision.

The measurement worth remembering is the movement tax rather than the call-count tax, because inlining can erase the latter and cannot touch the former. Inserting a range at the front of a contiguous container of n elements moves each of them once; inserting the same elements one at a time moves each of them once per inserted element.

Named range members have since been added — appending, inserting, and assigning from a range as explicitly named operations — which both make these call sites easier to recognize and accept sources that are not a begin-and-end pair. Where they are available they are the better spelling of everything above.

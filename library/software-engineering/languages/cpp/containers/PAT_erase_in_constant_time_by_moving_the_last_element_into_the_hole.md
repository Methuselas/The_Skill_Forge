---
object_id: PAT_erase_in_constant_time_by_moving_the_last_element_into_the_hole
object_type: pattern
name: Erase in Constant Time by Moving the Last Element Into the Hole
library_path:
- software-engineering
- languages
- cpp
- containers
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- containers
- performance
- erasure
cross_links:
- rel: related_to
  target_object_id: PAT_remember_an_algorithm_cannot_change_a_containers_size
- rel: related_to
  target_object_id: PAT_choose_a_container_on_more_than_algorithmic_complexity
- rel: related_to
  target_object_id: PAT_recover_the_iterator_from_erase_rather_than_advancing_it
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Erase in Constant Time by Moving the Last Element Into the Hole

## Pattern Rule
**IF** you are erasing an element from the middle of a contiguous sequence and the order of the remaining elements carries no meaning
**THEN** move the last element into the vacated position and shorten the sequence by one, which touches two elements instead of shifting every element after the hole
**ELSE** where the order does carry meaning — the sequence is sorted, or its order is the program's output, or an index held elsewhere refers to a position — erase normally and pay the shift, because this technique's entire cost is paid in the order it destroys.

## Do
- Establish that the order is genuinely free before anything else. This is the whole precondition and it is easy to assert without checking: a sequence that is merely unsorted today may still be one whose order somebody downstream relies on, and the technique reorders it silently.
- Move the last element rather than copying it. The point is to touch two positions cheaply, and a copy of a large element gives most of that saving straight back — the move leaves the source in a valid state that is about to be discarded anyway.
- Shorten from the back afterwards, which is the operation that makes the whole thing constant. Removing the final element adjusts the end position and destroys one object; it never relocates anything.
- Guard the bounds first, and note that the degenerate case is already correct. Erasing the last element moves it onto itself and then pops it, which is wasteful but not wrong, so no special case is needed beyond checking the position is valid at all.
- Offer the operation by position and by iterator both, since callers arrive from both directions — a search hands back an iterator, an index arrives from elsewhere — and neither should have to convert to the other's form to call you.

## Don't
- Don't use it on a sequence anything else indexes into. Two positions change value, not one, and any index stored elsewhere that referred to the last element now refers to something that moved.
- Don't use it while iterating forward and expecting to have visited everything. The element you just pulled in from the back lands at the position you are standing on, so continuing past it skips an element that was never examined.
- Don't reach for it as a general speed-up for erasure. Where the order matters the shift is not overhead, it is the work — and where erasures are frequent enough for the difference to matter, the sequence may be the wrong container entirely.

## Checklist
- Does anything downstream depend on the order of these elements?
- Does anything hold an index or iterator into this sequence across the erasure?
- Is the element moved rather than copied?
- If this runs inside a loop over the same sequence, does the loop account for the element that arrives at the current position?

## Notes
This is a small technique with an unusually sharp precondition, and the precondition is the part worth carrying. Erasing from the middle of a contiguous sequence is linear because the sequence's defining property is that its elements sit adjacent in memory with no gaps — closing the gap is what the cost buys. If the order is arbitrary, there is a cheaper way to close it, which is to fill the hole from the end rather than slide everything down into it.

The failure mode is not slowness but silence. Nothing about the operation announces that it reordered the sequence, so a caller who assumed stability gets a container that is still the right size, still contains the right elements, and presents them in an order nobody chose. That is why the "order does not matter" judgement deserves to be made explicitly and written down where the sequence is declared, rather than inferred at each call site by whoever is erasing.

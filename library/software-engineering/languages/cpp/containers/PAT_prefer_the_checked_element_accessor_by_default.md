---
object_id: PAT_prefer_the_checked_element_accessor_by_default
object_type: pattern
name: Prefer the Checked Element Accessor by Default
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
- bounds
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_hand_container_data_to_a_c_api_as_a_pointer_and_a_count
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
- rel: related_to
  target_object_id: PAT_treat_undefined_behavior_as_a_whole_program_assumption
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Prefer the Checked Element Accessor by Default

## Pattern Rule
**IF** a container offers both an unchecked subscript and a checked accessor for the same indexed element
**THEN** reach for the checked one unless a measurement says otherwise, because the unchecked form's out-of-range behaviour is undefined in both directions and the read is the less dangerous half
**ELSE** where the index is provably in range at that point — a loop bound derived from the container's own size, an index just validated — the check is redundant and the subscript is the clearer spelling.

## Do
- Notice that the dangerous case is the write, not the read. An out-of-range read returns whatever is at that address and looks merely wrong; an out-of-range write through the same operator modifies memory the container does not own, compiles without complaint, and produces no diagnostic at the moment it happens. The program continues, and the damage surfaces somewhere with no connection to the line that caused it.
- Treat the checked accessor's cost as insurance priced in cycles. It compares an index against a size, which is a predictable branch next to memory that is already being touched; the class of defect it removes is one of the most common routes to memory corruption.
- Reserve the unchecked form for a path that was measured and found to matter, and say so where you use it. "The subscript is faster" is a claim about a loop nobody profiled until it is a claim about one somebody did.
- Remember that the two spellings are not unique to one container. Every indexable container in the library offers both, with the same split in behaviour, so the decision recurs and should be made once as a habit rather than freshly each time.
- Catch the exception rather than letting it terminate where the caller can do something better with an out-of-range index than stop. The point of the checked form is that it reports; leaving the report unhandled uses only half of what it bought you.

## Don't
- Don't read the subscript's lack of checking as an oversight to be worked around. It is deliberate — it exists so the operator stays as cheap as indexing a raw array — and the library's answer to wanting a check is the other accessor, not a wrapper around this one.
- Don't reach for the unchecked form because the index "should" be valid. If it is provably valid, say why and use whichever spelling reads better; if it is only expected to be valid, that expectation is exactly what the check exists to test.
- Don't assume an out-of-range subscript will crash. It usually will not, and the outcome that hurts is the one where it quietly succeeds.

## Checklist
- Is this index derived from the container's own size, or from somewhere else?
- If from somewhere else, is anything checking it before it reaches the subscript?
- Is this a write? If so, is there any reason not to use the checked accessor?
- If the unchecked form is here for speed, what measurement put it here?
- Where the checked form is used, is the exception it can throw actually handled?

## Notes
The two accessors look like a style choice and are not. They differ in what happens when the program is already wrong, which is the moment when the difference is worth the most and the moment nobody is thinking about while writing the line.

What makes the unchecked write particularly bad is the absence of any signal at all. The compiler permits it, the runtime permits it, the program keeps going, and the corrupted memory belongs to something else — so the eventual failure appears in unrelated code, at an unrelated time, with a cause that cannot be reached from the symptom. That distance between cause and symptom is why this is worth a default rather than a judgement call: the habit has to be in place before the bug exists, because afterwards there is nothing pointing back at the line that made it.

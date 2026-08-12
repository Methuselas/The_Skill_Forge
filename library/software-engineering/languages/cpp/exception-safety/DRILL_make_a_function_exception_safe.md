---
object_id: DRILL_make_a_function_exception_safe
object_type: drill
name: Make a Function Exception-Safe with RAII and Copy-and-Swap
target_skill: Removing leaks and corruption and choosing an exception-safety guarantee
library_path:
- software-engineering
- languages
- cpp
- exception-safety
stage_binding: 3 rough
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- exception_safety
- raii
- copy_and_swap
cross_links:
- rel: related_to
  target_object_id: PAT_offer_an_exception_safety_guarantee
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u05, pp. 127-133
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make a Function Exception-Safe with RAII and Copy-and-Swap

## Practice Task
Given a `changeBackground` that manually locks a mutex, deletes the old image, increments a change counter, and constructs a new image, make it exception-safe.

## Target Skill
Removing resource leaks and data corruption, then offering the strongest practical guarantee.

## Setup
No special setup required.

## Instructions
- Identify the resource leak (the mutex stays held if constructing the new image throws) and the corruption (a dangling image pointer and a counter bumped for a change that did not happen).
- Replace the manual lock and unlock with a lock-guard RAII object.
- Hold the image in a smart pointer and reset it so the old image is deleted only after the new one is constructed; increment the counter only after the change.
- For the strong guarantee, restructure with copy-and-swap over a pimpl, and note what still prevents it (the input-stream parameter's side effect).

## Success Check
- If constructing the new image throws, no resource leaks and the object stays in a valid state.
- The change counter reflects only changes that actually happened.

## Common Failures
- Incrementing the counter before the change has succeeded.
- Assuming copy-and-swap delivers the strong guarantee despite a non-local side effect.

## Notes
This drills Item 29: RAII removes the leak, reordering removes the corruption, and copy-and-swap reaches for the strong guarantee — but a side effect on the stream marker caps it at the basic guarantee.

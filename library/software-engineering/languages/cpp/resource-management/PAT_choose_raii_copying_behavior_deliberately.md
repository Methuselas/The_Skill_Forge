---
object_id: PAT_choose_raii_copying_behavior_deliberately
object_type: pattern
name: Choose an RAII Class's Copying Behavior Deliberately
library_path:
- software-engineering
- languages
- cpp
- resource-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- raii
- copy_control
- resource_management
cross_links:
- rel: related_to
  target_object_id: PAT_suppress_copying_with_private_undefined_or_uncopyable
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u03, pp. 66-69
  evidence_type: text
confidence: high
references: []
variants: []
---

# Choose an RAII Class's Copying Behavior Deliberately

## Pattern Rule
**IF** you write your own resource-managing (RAII) class rather than using a ready-made smart pointer
**THEN** decide explicitly what copying an instance should mean, because the compiler-generated copy usually mishandles the underlying resource.

## Do
- Prohibit copying when copies make no sense — a lock, for instance — by declaring the copy operations private or inheriting from Uncopyable.
- Reference-count the resource when it should live until the last holder is gone: hold it in a shared pointer, supplying a custom deleter (such as an unlock function) so the count reaching zero triggers release rather than deletion.
- Deep-copy the resource when independent copies are wanted, or transfer ownership when only one holder may exist.

## Don't
- Don't accept the compiler-generated copying functions for a resource-managing class unchecked; copying just the handle without copying or accounting for the resource yields double releases or leaks.

## Checklist
- Have I chosen one of prohibit, reference-count, deep-copy, or transfer for this RAII class?
- Does the chosen behavior match how the underlying resource must be shared or duplicated?
- If reference-counting, does the deleter release the resource rather than delete it?

## Notes
Every RAII author faces the question the `Lock`/`Mutex` example poses: what should copying do? The four grounded answers are prohibit (Item 6's private copy operations or Uncopyable), reference-count (a shared-pointer member with a custom deleter, so a mutex is unlocked rather than deleted at count zero), deep-copy (as some string implementations do), and transfer ownership (auto_ptr's meaning of copy). The copying behavior of the resource dictates the copying behavior of the class.

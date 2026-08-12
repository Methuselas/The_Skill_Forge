---
object_id: PAT_replace_new_delete_only_with_clear_reason
object_type: pattern
name: Replace new and delete Only for a Concrete Reason
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- allocation
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_match_new_and_delete_forms
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u08, pp. 247-252
  evidence_type: text
confidence: high
references: []
variants: []
---

# Replace new and delete Only for a Concrete Reason

## Pattern Rule
**IF** you are considering replacing the compiler's operator new and operator delete
**THEN** do it only for a specific, identified reason — detecting usage errors, improving speed, collecting statistics, reducing space overhead, fixing alignment, clustering objects, or unconventional behavior — and prefer existing tools first, because a correct allocator is hard to write.

## Do
- Match the replacement to a concrete goal: signature bytes around each block to catch overruns and underruns, a fixed-size allocator for speed and space, logging for usage statistics, or a specific alignment guarantee.
- Reach for compiler debug/logging switches, commercial allocators, or an open-source pool allocator (Boost's Pool) before writing your own.

## Don't
- Don't hand-roll an allocator without handling alignment; operator new must return memory suitably aligned for any type, and getting this wrong crashes the program or silently slows it.
- Don't assume the default allocator is the bottleneck — profile before replacing it.

## Checklist
- Is there a concrete reason (errors, speed, statistics, space, alignment, clustering, unconventional behavior) to replace new/delete?
- Have I checked compiler switches and existing allocators first?
- Does my replacement return correctly aligned memory for any type?

## Notes
The general-purpose allocator that ships with a compiler is a middle-of-the-road compromise: fine for everybody, optimal for nobody. Knowing your program's allocation patterns, a custom allocator can be markedly faster and smaller — but alignment is the detail that separates a professional allocator from one that "almost works," since returning a malloc pointer offset by an int can misalign a double and crash. Prefer compiler switches, commercial products, or Boost's Pool before rolling your own, and profile first.

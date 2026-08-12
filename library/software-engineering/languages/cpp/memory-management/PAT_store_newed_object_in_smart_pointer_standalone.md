---
object_id: PAT_store_newed_object_in_smart_pointer_standalone
object_type: pattern
name: Store a newed Object in a Smart Pointer in Its Own Statement
library_path:
- software-engineering
- languages
- cpp
- memory-management
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- memory_management
- smart_pointers
- exception_safety
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u03, pp. 75-77
  evidence_type: text
confidence: high
references: []
variants: []
---

# Store a newed Object in a Smart Pointer in Its Own Statement

## Pattern Rule
**IF** you pass a newly allocated object to a function by wrapping it in a smart pointer
**THEN** create the object and store it in the smart pointer in a separate, standalone statement first, then pass the smart pointer to the function.

## Do
- Put the smart-pointer construction on its own line — a shared pointer `pw` initialized from `new Widget` — then call the function with `pw`.
- Rely on the fact that compilers may not reorder operations across statement boundaries, so the raw pointer cannot be stranded between allocation and capture.

## Don't
- Don't construct the smart pointer from new inside a function-argument list next to another argument that can throw; the compiler may run the new, then evaluate the other argument, and if that throws, the raw pointer leaks before the smart pointer captures it.

## Checklist
- Is each newed object stored in its smart pointer in a statement of its own before being passed on?
- Could any other argument evaluated in the same call throw between the new and the smart-pointer construction?

## Notes
Within a single statement compilers may interleave the steps of `processWidget(std::tr1::shared_ptr(new Widget), priority())`: run the new, call priority, then construct the smart pointer. If priority throws in that window, the raw pointer from new is lost before anything owns it. Splitting the allocation into its own statement removes the window, because compilers get far less freedom to reorder across statements than within one.

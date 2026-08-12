---
object_id: PAT_manage_resources_with_raii_objects
object_type: pattern
name: Manage Every Resource with an RAII Object
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
- resource_management
- smart_pointers
cross_links:
- rel: related_to
  target_object_id: PAT_store_newed_object_in_smart_pointer_standalone
- rel: related_to
  target_object_id: PAT_never_let_exceptions_leave_a_destructor
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u03, pp. 61-66
  evidence_type: text
confidence: high
references: []
variants: []
---

# Manage Every Resource with an RAII Object

## Pattern Rule
**IF** you acquire a resource that must later be released — heap memory, a file descriptor, a mutex lock, a socket, a database connection
**THEN** immediately give it to an object that takes ownership in its constructor and releases it in its destructor (RAII), instead of relying on a manual release that a return, break, or exception can skip.

## Do
- Acquire the resource and hand it to the managing object in the same statement (Resource Acquisition Is Initialization), so it is guarded the instant it exists.
- For heap objects use a ready-made smart pointer, and prefer a reference-counting shared pointer, whose copy behaves intuitively, over auto_ptr, whose copy nulls the source.
- Let the manager's destructor perform the release, so it happens automatically on every path out of the scope.

## Don't
- Don't count on reaching a manual delete or release at the end of a function; a premature return, a loop break, or a thrown exception skips it and leaks the resource plus everything it owns.
- Don't put an array allocation into auto_ptr or a shared pointer — they call delete, not delete[]; use a vector or string instead.

## Checklist
- Is every acquired resource owned by an object that releases it in its destructor?
- Is the resource handed to its manager at the moment of acquisition?
- Am I still calling delete or a release function by hand anywhere outside a resource-managing class?

## Notes
The `createInvestment`/`f` example shows why manual release fails: any early exit or exception between acquisition and the release call leaks. RAII closes every path by tying release to destruction, which C++ runs automatically at scope exit. auto_ptr and tr1::shared_ptr are the book's examples, not the point — the point is that objects, not discipline, should manage resources. The modern successors std::unique_ptr and std::shared_ptr belong to *Effective Modern C++* and should be absorbed there.

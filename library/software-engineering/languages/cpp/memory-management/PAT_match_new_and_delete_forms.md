---
object_id: PAT_match_new_and_delete_forms
object_type: pattern
name: Use Matching new and delete Forms
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
- new_delete
- undefined_behavior
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u03, pp. 73-75
  evidence_type: text
confidence: high
references: []
variants: []
---

# Use Matching new and delete Forms

## Pattern Rule
**IF** you release memory that was allocated with new or with new[]
**THEN** use the matching delete form — plain delete for a single object from new, delete[] for an array from new[] — because a mismatch is undefined behavior.

## Do
- Pair a single-object new with plain delete, and an array new[] with delete[], so the right number of destructors runs.
- In a class that stores a pointer to allocated memory, use the same new form in every constructor, so the destructor knows which delete form to use.

## Don't
- Don't hide array-ness behind a typedef for an array type; new on that typedef allocates an array, but a caller who writes plain delete triggers undefined behavior.

## Checklist
- Does each delete match the new that produced its pointer — brackets with brackets, plain with plain?
- Do all constructors of this class allocate the pointer member with the same new form?
- Am I using an array typedef that obscures which delete form is required?

## Notes
An array's memory usually records its element count so delete[] knows how many destructors to call; a single object's memory does not. Using plain delete on an array (the `new std::string[100]` then plain delete example) leaves most elements undestroyed or worse. The `AddressLines` typedef shows the trap: `new AddressLines` yields an array, so it needs delete[], which is why array typedefs are best avoided — vector and string remove nearly all need for raw arrays anyway.

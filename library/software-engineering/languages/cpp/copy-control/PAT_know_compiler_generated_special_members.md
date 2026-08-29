---
object_id: PAT_know_compiler_generated_special_members
object_type: pattern
name: Know the Special Member Functions the Compiler Writes for You
library_path:
- software-engineering
- languages
- cpp
- copy-control
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- copy_control
- special_members
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_copy_all_members_and_base_parts
- rel: related_to
  target_object_id: PAT_delete_the_functions_you_want_to_forbid
- rel: related_to
  target_object_id: AP_write_copy_control_for_a_resource_owning_class
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Know the Special Member Functions the Compiler Writes for You

## Pattern Rule
**IF** you declare a class without writing its copy constructor, copy assignment operator, destructor, or (when you declare no constructors) default constructor
**THEN** expect the compiler to generate public inline versions on demand, and know the cases where it refuses — so copying and destruction never behave in a way you did not write.

## Do
- Expect a generated copy to duplicate each non-static member memberwise: a string member through its own copy constructor, an int member bit-for-bit.
- Remember the default constructor is generated only when you declare no constructors at all; declaring any constructor suppresses it.
- Know the generated destructor is non-virtual unless a base class already declares a virtual destructor.

## Don't
- Don't assume a copy assignment operator is always generated: the compiler refuses when the class holds a reference member, a const member, or a base whose copy assignment is private.

## Checklist
- Which special members will the compiler generate for this class, and which am I relying on?
- Does a reference or const member here suppress the generated copy assignment?
- Do I actually want memberwise copying, or something different?

## Notes
An empty class is not empty once the compiler adds a default constructor, copy constructor, copy assignment operator, and destructor — all public and inline, and only when used. The `NamedObject` example shows the memberwise behavior; the reference-and-const version shows the refusal, because reseating a reference is impossible and const members cannot be assigned. Knowing exactly what is generated (and when it is not) is the prerequisite for the copy-control decisions in the rest of this chapter.

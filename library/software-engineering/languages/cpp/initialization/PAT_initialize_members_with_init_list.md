---
object_id: PAT_initialize_members_with_init_list
object_type: pattern
name: Initialize Members with the Initializer List, in Declaration Order
library_path:
- software-engineering
- languages
- cpp
- initialization
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- initialization
- constructors
- member_initialization
cross_links:
- rel: related_to
  target_object_id: PAT_manually_initialize_builtin_objects
- rel: related_to
  target_object_id: PAT_replace_nonlocal_statics_with_local_statics
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Initialize Members with the Initializer List, in Declaration Order

## Pattern Rule
**IF** you are writing a constructor
**THEN** set every member through the member initialization list rather than assigning in the body, and list them in the order they are declared in the class.

## Do
- Prefer `: theName(name), theAddress(address), thePhones(phones), numTimesConsulted(0)` to body assignments — each class-type member is copy-constructed once instead of default-constructed and then assigned over.
- Always initialize `const` members and references through the list; they cannot be assigned, so the list is the only option for them.
- Write the list in the same order the members are declared, because that is the order C++ actually initializes them regardless of how the list reads.

## Don't
- Don't assign members inside the constructor body: for class-type members it wastes a default construction, and for a built-in like `numTimesConsulted` it can leave the member briefly uninitialized before the assignment.
- Don't rely on the list's order to control initialization order — declaration order wins, so a mismatched list only misleads whoever reads it.

## Checklist
- Is every member set via the initialization list rather than assigned in the body?
- Are `const` and reference members initialized (not assigned)?
- Does the list order match the class's declaration order?

## Notes
The trap is confusing assignment with initialization. Members are initialized before the constructor body runs, so body assignments to class-type members pay for a default construction that is immediately thrown away; the initialization list uses the arguments directly as constructor arguments, usually via one copy construction. Some members — `const` and references — must be in the list because they cannot be assigned at all. Listing members in declaration order matters because that is the real initialization order; anything else invites obscure bugs and reader confusion.

---
object_id: PAT_dont_hide_standard_new_forms
object_type: pattern
name: Don't Let Class-Specific new Hide the Standard Forms
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
- name_hiding
- placement_new
cross_links:
- rel: related_to
  target_object_id: PAT_unhide_inherited_names_with_using
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Don't Let Class-Specific new Hide the Standard Forms

## Pattern Rule
**IF** you declare any operator new in a class
**THEN** know that it hides all the standard global forms — normal, placement, and nothrow — and re-expose the ones clients need, typically via a base class holding the standard forms plus using declarations.

## Do
- Provide a base class defining the normal, placement, and nothrow forms of operator new and delete, each forwarding to the global version, and inherit from it with using declarations to make them visible.
- Add your custom forms alongside the re-exposed standard ones, pairing each operator new with its operator delete.

## Don't
- Don't declare a class operator new and assume clients still have the normal or nothrow forms; a class-scope name hides the outer-scope ones, so plain new or nothrow new stops compiling for that class.

## Checklist
- Does declaring a class operator new hide standard forms clients still expect?
- Are the needed standard forms re-exposed via a base class of standard forms and using declarations?
- Does each re-exposed or custom operator new have a matching operator delete?

## Notes
Member names hide same-named names in enclosing scopes (Item 33), so a single class operator new hides the three standard global forms — normal, placement, and nothrow — making plain new or nothrow new fail to compile for that class. The clean fix is a StandardNewDeleteForms base whose members forward to the global versions; a class then inherits it, brings the forms in with using declarations, and adds its own custom forms, each paired with a matching delete.

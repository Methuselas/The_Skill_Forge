---
object_id: PAT_provide_class_specific_new_handler_via_crtp
object_type: pattern
name: Give a Class Its Own New-Handler with a CRTP Mixin
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
- new_handler
- crtp
cross_links:
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
- rel: related_to
  target_object_id: PAT_write_a_well_behaved_new_handler
- rel: related_to
  target_object_id: AP_replace_new_and_delete_for_a_named_reason
reference:
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Give a Class Its Own New-Handler with a CRTP Mixin

## Pattern Rule
**IF** you want allocation-failure handling specific to one class rather than the single global new-handler
**THEN** give the class its own set_new_handler and operator new — the operator new installs the class handler as the global one, allocates, and restores the previous handler via RAII — and factor the machinery into a curiously-recurring-template-pattern base so any class can reuse it.

## Do
- Store the class handler in a static member; have the class operator new install it (via the standard set_new_handler), call the global operator new, and let an RAII holder restore the previous global handler on the way out.
- Move the shared set_new_handler and operator new into a mixin base templated on the deriving class (CRTP), so each derived class gets its own static handler even though the template parameter is otherwise unused.

## Don't
- Don't restore the global handler by hand after allocating; a thrown bad_alloc would skip the restore — wrap the previous handler in an RAII object so restoration always happens.

## Checklist
- Does the class install its own handler, allocate through the global operator new, and restore the previous handler via RAII?
- Is the reusable machinery in a CRTP base so each class gets a distinct static handler?
- Is the global new-handler treated as a resource so an exception cannot leak it?

## Notes
C++ has no built-in class-specific new-handler, but you can build one: a per-class static handler, a class operator new that installs it and restores the prior one, and a NewHandlerHolder RAII object guaranteeing restoration even when the global operator new throws. The curiously recurring template pattern — a class inheriting from a base templated on itself — gives each class its own copy of the static handler; the type parameter exists only to distinguish instantiations.

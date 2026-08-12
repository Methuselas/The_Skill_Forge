---
object_id: PAT_no_virtual_calls_in_constructors_or_destructors
object_type: pattern
name: Don't Call Virtual Functions During Construction or Destruction
library_path:
- software-engineering
- languages
- cpp
- construction
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- construction
- destructors
- virtual_functions
cross_links:
- rel: related_to
  target_object_id: PAT_give_polymorphic_base_a_virtual_destructor
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u02, pp. 48-52
  evidence_type: text
confidence: high
references: []
variants: []
---

# Don't Call Virtual Functions During Construction or Destruction

## Pattern Rule
**IF** you are in a constructor or destructor and want behavior that varies with the object's dynamic type
**THEN** do not obtain it by calling a virtual function — during base construction and destruction the call resolves to the base version, never the derived override.

## Do
- Pass type-specific data upward: have each derived constructor compute what the base needs and hand it to the base constructor, which then calls a non-virtual function.
- Build that information in a private static helper on the derived class, so it cannot touch the object's not-yet-initialized members.

## Don't
- Don't call a virtual function — directly, or through a non-virtual helper like an `init` routine — from a constructor or destructor expecting the derived version; during base construction the object is of the base type and the base version runs.

## Checklist
- Does any constructor or destructor call a virtual function, directly or via a helper it invokes?
- When a base needs type-specific data, is it passed up from the derived constructor rather than fetched through a virtual call?

## Notes
Base parts are constructed before derived parts, so during the base constructor the derived members do not yet exist; C++ therefore treats the object as the base type — virtual dispatch, dynamic_cast, and typeid all resolve to the base. The `Transaction`/`logTransaction` example shows the trap, and the `init`-helper version shows why it is insidious: it compiles and links. The fix is to feed the base what it needs from the derived constructor (often via a static helper such as `createLogString`) and call a non-virtual function.

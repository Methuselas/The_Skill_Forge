---
object_id: PAT_minimize_compilation_dependencies
object_type: pattern
name: Minimize Compilation Dependencies with Handle or Interface Classes
library_path:
- software-engineering
- languages
- cpp
- compilation-dependencies
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- compilation_dependencies
- pimpl
- encapsulation
cross_links:
- rel: related_to
  target_object_id: PAT_support_nonthrowing_swap
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
reference:
  source_id: effective_cpp_3e
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
  publish_date: 2005
  media_type: PDF
  locator: u05, pp. 140-148
  evidence_type: text
confidence: high
references: []
variants: []
---

# Minimize Compilation Dependencies with Handle or Interface Classes

## Pattern Rule
**IF** a class exposes its implementation details in its header, forcing clients to recompile whenever the implementation changes
**THEN** depend on declarations rather than definitions — hide the implementation behind a pointer (the pimpl idiom, a Handle class) or behind an abstract Interface class with a factory — so clients recompile only when the interface changes.

## Do
- Give the class a single pointer to a forward-declared implementation class and forward its calls to that class (a Handle class), so the header needs only declarations.
- Or make the class an abstract Interface class of pure virtual functions, with a static factory returning a smart pointer to a concrete subclass.
- Ship headers in pairs — a declaration-only header and a definition header — and have clients include the declaration header rather than forward-declaring types themselves.

## Don't
- Don't include a definition where a declaration will do; declaring a function that passes or returns a type by value needs only that type's declaration, not its definition.
- Don't forward-declare standard-library types yourself — string is a typedef, not a class — so include the proper header instead.

## Checklist
- Does the header depend on definitions where forward declarations would suffice?
- Is the implementation hidden behind a pimpl pointer or an Interface class, so implementation changes don't recompile clients?
- Are declaration-only and definition headers provided as a pair?

## Notes
C++ couples clients to a class's implementation because the class definition carries private data whose types must be defined for the compiler to size the object. The `Person` example breaks that coupling two ways: a Handle class holds only a pointer to a forward-declared `PersonImpl` and forwards calls, or an Interface class exposes pure virtuals with a factory. Both cost an indirection and some memory and lose inlining, so use them while implementations churn and collapse to concrete classes when the cost is shown to matter. The essence is depend on declarations, not definitions.

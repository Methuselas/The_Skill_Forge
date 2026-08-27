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
  source_title: 'Effective C++, Third Edition: 55 Specific Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants:
- variant_id: VAR_publish_a_module_interface_instead_of_a_header
  variant_name: Publish a Module Interface Instead of a Header
  variant_basis: method_sequence
  difference_from_foundation: The foundation removes the dependency by hiding the implementation behind a pointer or an abstract base, and both remedies buy that with a runtime indirection. Neither reaches templates at all, because a template's source must be available wherever it is instantiated, which is why templates live in headers and why a growing template library is the case the foundation cannot help. This variant changes the unit of publication instead of the shape of the class. A module is compiled once and publishes an interface as metadata carrying enough information for the compiler to instantiate specializations later, so template code stops being recompiled at every use without any indirection being introduced and without the class being restructured. It also closes a leak the foundation does not address. A header's include guard, its configuration macros, and every symbol reached through it transitively enter the consumer's translation unit, and macros sit outside both the namespace system and the type system, so the compiler cannot diagnose the collisions they cause. A module exports only the names it explicitly exports; everything else is private, and preprocessor requirements are confined to a declared global fragment rather than escaping to consumers.
  when_to_use: Use where the recompilation cost is driven by template-heavy headers, which the foundation's two remedies cannot address, or where macro and symbol leakage across a large header graph has become its own source of defects. It is also the better choice where the indirection the foundation introduces is genuinely unaffordable, since it removes the coupling without adding a pointer hop or a virtual call.
  when_not_to_use: Do not reach for it to decouple a single class whose implementation churns while its interface is stable — that is what the foundation is for, and restructuring a translation unit is a heavier change than introducing a handle. It is a build-system-visible decision requiring toolchain support and a module-aware build, so it is a poor fit for a codebase that must compile under toolchains you do not control. It also does not hide an implementation from a reader the way an abstract interface does; it controls what is published and recompiled, not what is visible in the source.
  absorbed_from_object_id: none
---

# Minimize Compilation Dependencies with Handle or Interface Classes

## Pattern Rule
**IF** a class exposes its implementation details in its header, forcing clients to recompile whenever the implementation changes
**THEN** depend on declarations rather than definitions — hide the implementation behind a pointer (the pimpl idiom, a Handle class) or behind an abstract Interface class with a factory — so clients recompile only when the interface changes.

## Do
- Give the class a single pointer to a forward-declared implementation class and forward its calls to that class (a Handle class), so the header needs only declarations.
- Or make the class an abstract Interface class of pure virtual functions, with a static factory returning a smart pointer to a concrete subclass.
- Ship headers in pairs — a declaration-only header and a definition header — and have clients include the declaration header rather than forward-declaring types themselves.
- Declare the special member functions in the header and define them in the implementation file when the handle is an exclusive-ownership smart pointer, even where the compiler-generated versions would be correct. Its deleter needs the complete type, and a compiler-generated destructor is inline in the header where that type is still incomplete — so accepting the default fails to compile at the client. A shared pointer does not have this problem, because its deleter is not part of its type and the complete type is captured when the pointer is constructed.

## Don't
- Don't include a definition where a declaration will do; declaring a function that passes or returns a type by value needs only that type's declaration, not its definition.
- Don't forward-declare standard-library types yourself — string is a typedef, not a class — so include the proper header instead.

## Checklist
- Does the header depend on definitions where forward declarations would suffice?
- Is the implementation hidden behind a pimpl pointer or an Interface class, so implementation changes don't recompile clients?
- Are declaration-only and definition headers provided as a pair?

## Notes
C++ couples clients to a class's implementation because the class definition carries private data whose types must be defined for the compiler to size the object. The `Person` example breaks that coupling two ways: a Handle class holds only a pointer to a forward-declared `PersonImpl` and forwards calls, or an Interface class exposes pure virtuals with a factory. Both cost an indirection and some memory and lose inlining, so use them while implementations churn and collapse to concrete classes when the cost is shown to matter. The essence is depend on declarations, not definitions.

`VAR_publish_a_module_interface_instead_of_a_header` attacks the same coupling by changing the unit of publication rather than the shape of the class. Where the two remedies above restructure a type so its definition stops appearing in client headers, a module leaves the type alone and publishes a compiled interface instead of source text. That difference matters most for templates, which neither remedy above can help: a template must have its source available wherever it is instantiated, so it lives in a header by necessity, and a large template library therefore recompiles at every use no matter how carefully its classes are designed. A module's published metadata carries enough information to instantiate specializations without re-parsing the source, which removes that cost without introducing the indirection a handle or an abstract base requires. It also confines the preprocessor: include guards, configuration macros, and transitively included symbols all reach the consumer through a header and are invisible to the type and namespace systems, whereas a module publishes only what it names. Use it for template-driven build cost or macro leakage across a large header graph; keep the foundation for decoupling one churning class, where restructuring a translation unit and requiring a module-aware toolchain would be the heavier change.

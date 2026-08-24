---
object_id: PAT_leave_the_address_of_operator_alone
object_type: pattern
name: Leave the Address-of Operator Alone
library_path:
- software-engineering
- languages
- cpp
- operators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- operators
- generic_programming
- wrappers
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_leave_the_short_circuit_and_comma_operators_alone
- rel: related_to
  target_object_id: PAT_provide_access_to_raw_resource_in_raii_class
- rel: related_to
  target_object_id: PAT_program_to_a_templates_implicit_interface
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Leave the Address-of Operator Alone

## Pattern Rule
**IF** you are writing a wrapper that mimics something else closely — a smart pointer, a handle, a proxy — and are tempted to overload unary `&` so that taking its address yields the address of what it wraps
**THEN** don't, and provide a named function for that access instead, because generic code everywhere assumes that taking the address of a `T` yields a `T*` and has no way to find out otherwise.

## Do
- Give the access a name. A caller that must reach the wrapped address writes a call that says so, which is visible at the call site and cannot be triggered by accident.
- Treat the identity operations as reserved. Taking an address is not a behavior your type gets to define any more than its own storage is; the things built on top of it — containers, algorithms, allocators, anything that stores a pointer to an element — are entitled to assume the usual meaning.
- Where the wrapper is supposed to be substitutable for what it wraps, accept that the substitution stops short of this. Getting one operation closer to the imitation is not worth the class of failure it opens.

## Don't
- Don't overload it to make the wrapper usable with an interface that takes a pointer to pointer. That interface is going to write through the address it was given, which reaches past the wrapper entirely and leaves whatever bookkeeping the wrapper maintains describing a state that no longer exists.
- Don't assume the damage is confined to code that knows about your type. Standard containers and algorithms take the address of elements; a type that redefines what an address means either fails to compile with them or, worse, compiles and does something else.
- Don't reach for this to avoid writing an accessor. The accessor is a few characters at each call site, and it is the only version of this that a reader can see.

## Checklist
- Does anything need the address of the wrapped object, and can a named function serve it?
- Could an instance of this type end up inside a standard container or be handed to an algorithm?
- If someone writes the address-of expression on this type, do they get what every other type in the language would give them?

## Notes
Two separate objections apply and either is sufficient. The first is about ownership: handing out the address of a wrapped pointer lets a caller replace it without the wrapper knowing, so any counting, linking, or tracking the wrapper maintains silently stops describing reality. The second is about generic code: templates are written against expressions rather than signatures, and the address-of expression is one that essentially all of them assume behaves normally.

The second objection is the one that generalizes past this operator. A type may reasonably define what addition or comparison means for it, because those have no single meaning across all types. Identity operations are different — they are part of how the language talks about objects at all — and redefining one leaves generic code with no diagnostic, because there is nothing in a template to say that this parameter is not an ordinary type.

The failure mode is worth knowing because it does not point at the cause. What surfaces is a container or an algorithm behaving strangely on this element type and correctly on every other, which sends the reader into the library implementation rather than to the one operator that made this type unlike all the others.

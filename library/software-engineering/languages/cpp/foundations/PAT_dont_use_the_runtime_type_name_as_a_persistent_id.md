---
object_id: PAT_dont_use_the_runtime_type_name_as_a_persistent_id
object_type: pattern
name: Don't Use the Runtime Type Name as a Persistent Identifier
library_path:
- software-engineering
- languages
- cpp
- foundations
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- rtti
- serialization
- identifiers
- portability
cross_links:
- rel: related_to
  target_object_id: PAT_let_each_type_register_itself_with_the_factory
- rel: related_to
  target_object_id: PAT_state_your_compatibility_promise_and_its_span
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Don't Use the Runtime Type Name as a Persistent Identifier

## Pattern Rule
**IF** you need a token that names a type — a key in a creation table, a tag written into a saved file or a message, an entry in a registry
**THEN** choose the token yourself and write it down beside the type, rather than taking the name the runtime type information gives you, which is specified only well enough to print while debugging.

## Do
- Pick the token deliberately and treat it as part of whatever format it appears in, with the same stability obligation as any other field.
- Keep the token next to the type it names, so the two cannot drift and so the choice is visible to anyone editing either.
- Where tokens must be assigned without central coordination, generate them from something wide enough that collision is not a practical concern, then fix the generated value in the source permanently.
- Use the runtime type name for what it is specified for. Printing it in a diagnostic, a log, or an assertion message is exactly its purpose and it does that job well.

## Don't
- Don't assume the name is the class name. Nothing requires it to be, and implementations differ — some decorate it, some abbreviate it, and a conforming one could return the same empty string for every type.
- Don't assume it is unique. Two distinct types are permitted to yield the same name, which turns a creation table into one that silently builds the wrong type.
- Don't assume it is stable across runs. It is not required to be the same string the next time the program starts, which makes anything written to storage unreadable by the process that wrote it a day later.
- Don't compare the addresses of the type-information objects either. Repeated queries for the same type are not required to yield the same object, so pointer identity is not a type test — compare the objects rather than their addresses.

## Checklist
- Does any token that leaves this process come from the runtime type information?
- If two types produced the same token, what would happen, and would anything report it?
- Would data written by today's build still be readable by a build from a different compiler, or the same one tomorrow?
- Where the runtime name is used, is the result only ever shown to a person?

## Notes
The trap is that it looks like exactly the right tool, and it works on the machine where it is tried. A quick experiment shows the class name coming back, unique across the types at hand and identical on every run, and nothing about that experiment reveals which of those three properties are guaranteed. None of them are.

The distinction to hold is between a facility specified for diagnostics and one specified for identity. Diagnostic output is allowed to be approximate, implementation-defined, and unstable, because a person reads it once and discards it; an identifier is a promise that survives storage, transmission, and rebuilds. Reaching for the first where the second is required is the whole of this mistake, and it is not repaired by testing, because the properties that fail are the ones a test on one machine cannot observe.

The failure surfaces at the worst moment. Everything works during development and through the first release, and the reports arrive when a file written by one build is opened by another — a different compiler, a different version, sometimes only a different optimization setting — by which time the tokens are in the users' data and the format is no longer yours to change.

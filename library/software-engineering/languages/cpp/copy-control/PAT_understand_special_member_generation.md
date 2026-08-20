---
object_id: PAT_understand_special_member_generation
object_type: pattern
name: Know Which Special Members Your Declarations Suppress
library_path:
- software-engineering
- languages
- cpp
- copy-control
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- copy_control
- move_semantics
- class_design
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_know_compiler_generated_special_members
- rel: related_to
  target_object_id: PAT_delete_the_functions_you_want_to_forbid
- rel: related_to
  target_object_id: PAT_choose_raii_copying_behavior_deliberately
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Know Which Special Members Your Declarations Suppress

## Pattern Rule
**IF** you are about to declare a destructor, a copy operation, or a move operation in a class
**THEN** work out which other special members that declaration stops the compiler from generating, and default or write the ones you still want
**ELSE** where the class declares none of them and every member is well behaved, the compiler generates all six correctly and there is nothing to decide.

## Do
- Hold the generation rule for move operations as a single condition, because it is stricter than the one for copying: the move constructor and move assignment operator are generated only if the class declares *no* copy operation, *no* move operation, and *no* destructor. Any one of those declarations removes both.
- Notice the asymmetry with copying, which is the source of most surprises. The two copy operations are independent — declaring one still leaves the other generated. The two move operations are not: declaring either suppresses the other.
- Expect a declared destructor to cost you move support silently. This is the common case in practice, because destructors get added for tracing, for logging, or to be virtual, and the class quietly stops being movable — every "move" then resolves to a copy, correctly and slowly.
- Read a memberwise move as a request rather than a guarantee. Members and base classes that support moving are moved; those that do not are copied, and the code compiles either way. A class can therefore be nominally movable and copy most of its state.
- Say `= default` when the generated behaviour is what you want and something else has suppressed it. It documents the intent, costs nothing, and is the fix for a class that acquired a destructor and lost its moves.
- Take the Rule of Three seriously in its C++11 form. If a class needs any of a destructor, a copy constructor, or a copy assignment operator, it is managing something, and the questions of how it should move and whether it should be copyable both become yours to answer explicitly.
- Treat a declared move operation as a decision to make the class uncopyable. Declaring either move operation causes the copy operations to be deleted, which is usually right for a move-only resource holder and is worth being deliberate about.

## Don't
- Don't assume adding a destructor is a local change. It reaches out and removes the move operations from the class, and the only symptom is that the class became slower.
- Don't rely on generated copy operations in a class that declares a destructor or the other copy operation. That generation is deprecated; it still happens for compatibility, and code depending on it should be updated to say `= default` while the choice is still yours.
- Don't declare a move operation and expect copying to survive. It is deleted, not merely not generated, so the diagnostic is about a deleted function.
- Don't count a class as move-enabled because it compiles when moved. Compilation proves only that the operation resolved to something — possibly a copy of every member.

## Checklist
- Does this class declare a destructor, a copy operation, or a move operation?
- Given those declarations, which of the six special members is the compiler still generating?
- If the class should be movable, are the move operations declared or defaulted?
- If the class should be copyable, has a move declaration deleted its copy operations?
- For each member and base, does it actually support moving, or will it be copied?

## Notes
The reasoning behind the rules is worth carrying, because it makes them predictable rather than arbitrary. Declaring a copy operation says memberwise copying is not right for this class; the compiler infers that memberwise moving is probably not right either, and generates neither move operation. Declaring a destructor says the class manages a resource — the Rule of Three's observation — which implies the same thing. The rules are the compiler declining to guess about a class whose author has already indicated that the defaults do not fit.

What makes this a performance issue and not only a correctness one is that every path here degrades silently. A suppressed move operation does not fail to compile; the call resolves to the copy operation and the program is correct and slower. Nothing in the source of either the class or its callers records that a move was intended, which is why the generation rules have to be known rather than discovered.

The direction the language is moving is worth noting when deciding what to write down. C++11 deprecated the automatic generation of copy operations in classes that declare a destructor or one copy operation — the same reasoning applied to copying that was applied to moving. Code that depends on that generation is depending on a compatibility concession, and saying `= default` now converts a dependency on compiler behaviour into a statement of intent.

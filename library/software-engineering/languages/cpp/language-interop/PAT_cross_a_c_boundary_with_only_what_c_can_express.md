---
object_id: PAT_cross_a_c_boundary_with_only_what_c_can_express
object_type: pattern
name: Cross a C Boundary With Only What C Can Express
library_path:
- software-engineering
- languages
- cpp
- language-interop
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- language_interop
- linkage
- portability
- memory_management
cross_links:
- rel: related_to
  target_object_id: PAT_match_new_and_delete_forms
- rel: related_to
  target_object_id: PAT_replace_nonlocal_statics_with_local_statics
- rel: related_to
  target_object_id: PAT_minimize_compilation_dependencies
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Cross a C Boundary With Only What C Can Express

## Pattern Rule
**IF** a program is built from translation units compiled as C++ and translation units compiled as C, linked together into one image
**THEN** settle four questions deliberately — how names reach the linker, what constructs objects with static storage duration, which allocator releases what, and which data is allowed to cross — because each of them fails silently rather than loudly when left to chance
**ELSE** where the two halves communicate across a process boundary or through a serialized format rather than by linking, none of this applies and the compatibility question is about the format instead.

## Do
- Confirm the two compilers produce compatible object files before anything else, since no amount of correct source fixes an incompatibility here. The sizes of built-in types, how arguments are passed, and whether caller or callee cleans up are deliberately left open by both language standards, so the only reliable answer comes from the vendors.
- Suppress mangling on everything called across the boundary, in both directions, and read the specification as "call this the way C would" rather than "this is written in C" — it applies equally to assembler routines and to C++ functions you want callable from elsewhere. Bracket whole groups of declarations rather than marking each, and guard the bracket with the macro every C++ compiler predefines, so one header serves both compilers.
- Write the program's entry point in C++. Implementations commonly attach the construction and destruction of objects with static storage duration to it, so an entry point compiled as C can leave them unconstructed. Where the existing one is in C, rename it, declare it with C linkage, and call it from a C++ entry point — with a comment saying why, since the indirection otherwise looks pointless.
- Match every release to the allocation that produced it: memory from the C++ operator goes back through the C++ operator, memory from the C library goes back through the C library. Crossing them is undefined in both directions.
- Restrict what crosses to what compiles in both languages: built-in types, pointers to objects, pointers to non-member or static functions, and structs whose definitions compile as C. Adding non-virtual member functions to such a struct will generally leave its layout alone; adding a virtual function will not, and neither will giving it a base class.

## Don't
- Don't call a function that allocates and hands you the result unless you know which allocator it used. The widely available string-duplicating routine is the standard trap here, because it is standard in neither language, and whether its result should be released through the C++ operator or the C library depends on which implementation you linked against.
- Don't pass objects, references, or pointers to member functions across. There is no representation of them the C side can act on, and no arrangement of casts makes one.
- Don't expect mangling schemes to agree between C++ compilers, and don't wish that they did. Because they differ, mixing object files from incompatible compilers fails at link time — which is the good outcome, since those object files would have disagreed about calling conventions too, and that disagreement produces wrong behavior instead of a diagnostic.
- Don't reach for functions that are neither in the standard library nor stably available across the platforms you target. Their allocation and release conventions are exactly what varies, and portability problems of this kind surface at run time on somebody else's machine.

## Checklist
- Have both vendors confirmed their object files can be linked together?
- Is every function called across the boundary declared with C linkage, in both directions?
- Is the entry point compiled as C++?
- For each allocation crossing the boundary, which side releases it, and through which mechanism?
- Does every struct that crosses compile unchanged as C, with no virtual functions and no base class?

## Notes
The four questions are not equally visible when they go wrong, which is why settling them explicitly beats discovering them. Mangling failures show up at link time and are unmissable. The other three do not: unconstructed static objects, mismatched allocators, and structs whose layout differs by a hidden pointer all produce programs that build cleanly and then behave incorrectly, often far from the boundary.

The static-construction problem is the one most likely to be dismissed. It is tempting to keep the entry point in C when C++ is only a support library, but a library that has no objects with static storage duration today will probably acquire some, and the failure mode when it does is that constructors simply never run.

The struct rule follows from a single fact about layout: adding a virtual function makes objects of a class carry a hidden pointer, and giving a class a base generally rearranges it. Everything else in that rule is a consequence — which is why member functions that are not virtual are safe to add, and why nothing else is.

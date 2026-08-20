---
object_id: PAT_state_the_guarantees_a_function_can_honor
object_type: pattern
name: State the Guarantees a Function Can Honor
library_path:
- software-engineering
- languages
- cpp
- foundations
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- interface_design
- exception_safety
- performance
- compile_time
cross_links:
- rel: related_to
  target_object_id: PAT_define_your_code_contract_explicitly
- rel: related_to
  target_object_id: PAT_lift_a_stable_runtime_value_to_compile_time
- rel: related_to
  target_object_id: PAT_understand_special_member_generation
- rel: related_to
  target_object_id: PAT_optimize_for_what_the_compiler_can_prove
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# State the Guarantees a Function Can Honor

## Pattern Rule
**IF** you are declaring a function that will never emit an exception, or whose result can be computed from compile-time arguments
**THEN** say so in the declaration, because the compiler and your callers can both act on the promise — and take it as an interface commitment you will not be able to withdraw
**ELSE** where the guarantee is not one you can hold for the function's whole future, leave it off; an undeclared guarantee costs some optimization, and a broken one is worse.

## Do
- Declare a function that cannot throw as such, and expect it to change the generated code rather than only the documentation. Where an exception could escape, the optimizer must keep the stack unwindable and must destroy objects in reverse order of construction; where it cannot, neither obligation applies. That alone justifies the declaration wherever the guarantee is genuine.
- Give the promise priority on the move operations, on swap, and on memory deallocation, because library code inspects it. A growing container moving its elements to new storage can only use moves if moving cannot throw — otherwise a failure partway through leaves elements already moved out of the original, which cannot be restored. Without the guarantee the container copies instead: correct, and slower by exactly the margin move semantics were meant to provide.
- Mark as compile-time computable anything that can be. Such a function produces a compile-time result when its arguments are compile-time values, and behaves as an ordinary function otherwise — so the declaration widens where the function may be used without narrowing where it already was.
- Notice what a compile-time value unlocks: array sizes, template arguments, enumerator values, and alignment specifiers all require one, and a function that can produce it can be used in all of those places. An object declared compile-time-constant is also const.
- Treat both as part of the signature rather than as annotations. A caller may write code that depends on the guarantee, and a later revision that withdraws it breaks that caller — which is the ordinary consequence of changing an interface, and worth recognizing as one before the promise is made.

## Don't
- Don't attach either guarantee speculatively, in the hope of a faster build or a faster program. The declaration is a commitment about every future implementation of the function, and the correct question is whether the promise is true rather than whether it would be useful.
- Don't expect the non-throwing guarantee to be checked for you. It is a promise, and violating it at run time terminates the program rather than propagating the exception — so a function that might throw and says otherwise fails harder than one that says nothing.
- Don't assume a move operation is used because it exists. Library code that needs the strong exception guarantee checks whether moving can throw and falls back on copying when it cannot tell — so a movable type that never declared its moves non-throwing gets copied.
- Don't confuse a compile-time-constant object with one that is merely const. Every such object is const; most const objects are not compile-time constants, since their value may not be known until run time.

## Checklist
- Can this function throw, under any implementation you can foresee for it?
- Are the move operations, swap, and any deallocation function declared non-throwing?
- Could this function's result be computed at compile time when given compile-time inputs?
- Is any caller depending on a guarantee here that a future change would remove?
- Where the guarantee is absent, is that a decision or an omission?

## Notes
These two declarations do different jobs and share one property that is easy to miss: both are promises to callers rather than requests to the compiler. That is why they cannot be added and removed freely. A function that gains a guarantee can be relied on; a function that loses one breaks code that relied on it, and the breakage is not always a compile error.

The container-growth example is the one to remember, because it explains why the non-throwing promise on move operations matters out of proportion to its size. The library will only move where it can prove that moving cannot fail, since a failure halfway through leaves the source in a state it cannot restore. That proof comes from the declaration and nowhere else. A type with perfectly good move operations that never said they cannot throw is, from the library's point of view, a type to be copied.

The compile-time guarantee reads as an optimization and is better understood as a widening of where the function can appear. Contexts that demand a constant — array bounds, template arguments, enumerator values — are closed to ordinary functions entirely, so the declaration is less about speed than about which code becomes expressible at all.

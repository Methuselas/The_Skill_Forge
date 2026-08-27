---
object_id: PAT_choose_a_callables_storage_by_whether_it_must_carry_context
object_type: pattern
name: Choose a Callable's Storage by Whether It Must Carry Context
library_path:
- software-engineering
- languages
- cpp
- lambdas
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- lambdas
- callables
- interface_design
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_a_lambda_to_a_bound_call
- rel: related_to
  target_object_id: PAT_name_every_lambda_capture
- rel: related_to
  target_object_id: PAT_choose_compile_time_or_runtime_variation
- rel: related_to
  target_object_id: PAT_design_a_callable_for_the_copies_an_algorithm_will_make
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Choose a Callable's Storage by Whether It Must Carry Context

## Pattern Rule
**IF** a callable has to be stored somewhere that fixes its type — a container element, a data member, a lookup table
**THEN** choose the storage by whether the callable carries context, taking a plain function pointer where it carries none and a polymorphic function wrapper where it does
**ELSE** where the callable is handed straight to a template that accepts it as a deduced parameter, no storage decision arises — the template holds the callable's own type, and a function, a functor, and a lambda are all equally acceptable there.

## Do
- Start from whether anything is captured, because that is the whole of the decision. A lambda capturing nothing converts to a function pointer; a lambda capturing anything has its own unique type and does not convert, so a table of function pointers cannot hold it no matter how trivial its body looks.
- Read the resulting compile error as information rather than as an obstacle. It is telling you the callable carries state, and the two usual ways of forcing it back into a function pointer — hoisting the captured variable to a global, or dropping it and recomputing the value inside the body — are both worse than widening the storage to something that can hold state.
- Reach for the wrapper when the things stored together come from different places. A free function, a capturing lambda, and a member function bound to a particular object have nothing in common as types, and the wrapper's purpose is to give them one so they can sit in the same container or the same member.
- Let the signature be the thing they share, and choose it deliberately. The wrapper is parameterised on the call signature rather than on the callable, so everything stored under one wrapper type must accept the same arguments and return the same thing — which is a design constraint on the whole table, not an implementation detail of any one entry.
- Prefer a template parameter where the type can be settled when the code is compiled. It stores the callable as itself, with nothing erased and nothing indirected, and it is available whenever the storage is a class you are writing rather than a container of heterogeneous entries.

## Don't
- Don't carry away "a lambda is a function pointer" as a general fact. It is true of the captureless case and of nothing else, and the demonstrations that establish it are almost always written with captureless lambdas — so the rule looks general right up until the first capture, which is also the first time it matters.
- Don't reach for the wrapper by reflex when a template parameter would serve. It exists to erase differences between types, and where there are no differences to erase it is machinery bought for nothing.
- Don't let a callable that captured by reference outlive what it referred to. Storing it is exactly the situation where that happens, because storage separates the moment of capture from the moment of the call — and the reference is not visible at the call site, so nothing there suggests the question.

## Checklist
- Does this callable capture anything at all?
- What fixes the type where it is being stored — a container element type, a member declaration, an alias?
- Do the callables stored together come from more than one kind of origin?
- Could a template parameter hold this instead, and is anything actually being erased?
- Does anything captured by reference need to outlive the stored callable?

## Notes
The decision exists because "callable" is not a type. Three different things satisfy the idea — a function, an object with a call operator, and a lambda, which is the second wearing a shorter spelling — and they have no type in common. A template parameter sidesteps that by holding whichever one it was given, which is why passing a callable to an algorithm raises no question at all and why the question only appears at the moment something has to be *stored*.

What makes the captureless case misleading is that it works. A lambda with an empty capture clause converts to a function pointer, so a first table of them compiles and runs, and the arrangement looks like it generalises. It does not: the conversion exists precisely because there is no state to carry, and a function pointer is an address of code with nowhere to put any. The first entry that needs a captured value does not degrade the design gracefully — it fails to compile, and the temptation at that point is to change the lambda rather than the storage, which is the wrong half to move.

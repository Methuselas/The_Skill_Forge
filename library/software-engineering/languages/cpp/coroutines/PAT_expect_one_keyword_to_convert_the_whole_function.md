---
object_id: PAT_expect_one_keyword_to_convert_the_whole_function
object_type: pattern
name: Expect One Keyword to Convert the Whole Function
library_path:
- software-engineering
- languages
- cpp
- coroutines
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- coroutines
- api_design
- refactoring
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_reach_for_a_coroutine_when_work_must_pause_and_resume
- rel: related_to
  target_object_id: PAT_decide_where_a_coroutine_suspends_and_who_destroys_it
- rel: related_to
  target_object_id: PAT_prefer_auto_for_local_variables
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Expect One Keyword to Convert the Whole Function

## Pattern Rule
**IF** you are adding a yield, an await, or a coroutine return to an existing function
**THEN** treat the function as changing kind rather than gaining a statement, because a single one of those keywords anywhere in the body makes the whole function a coroutine — with different rules about what it may return, what its return type must provide, and where its parameters live
**ELSE** where you only need the behaviour at one call site, wrapping the work in a small coroutine and calling it leaves the original function unchanged.

## Do
- Know the four triggers, since any one of them is sufficient: a coroutine return, an await, a yield, or an await expression in a range-based loop. There is no partial adoption and no way to have a function that is a coroutine only sometimes.
- Expect the ordinary return statement to become unavailable. A coroutine cannot use it, so every path that returned a value has to be rewritten in terms of the coroutine's own mechanism, and a function with several returns is a larger change than it looks.
- Expect deduced return types to become unavailable too. Neither an unconstrained placeholder nor a constrained one is permitted, so the return type has to be written out — and it has to be a type that supplies the inner promise type the machinery requires, which usually means a purpose-built resumable type rather than anything already to hand.
- Check the function is even eligible before starting. Variadic functions, constant-evaluated functions of either kind, constructors, destructors, and the program's entry point cannot be coroutines, so for those the answer is to move the work elsewhere.
- Keep the two things called "coroutine" apart when reading or writing about this. The function containing the keyword is a factory; calling it produces a coroutine object, which is what the caller actually holds and interacts with. Almost every confusing sentence on this topic is one that has conflated them.

## Don't
- Don't expect parameters to behave as they did. They are copied into the coroutine's own frame, so anything passed by reference must outlive not the call but the coroutine — which is a considerably longer and less obvious lifetime.
- Don't assume the frame's allocation is free. It is a separately allocated block holding the promise object, the copied parameters, the suspension state, and any local whose lifetime spans a suspension; implementations may elide the allocation under specific conditions, and relying on that without checking is relying on an optimization.
- Don't convert a function in place because one call site wanted laziness. Every existing caller now receives a coroutine object rather than a value, which changes each of them, and the conversion cannot be scoped to the caller that asked for it.

## Checklist
- Does the function currently use plain return statements, and how many?
- Is its return type deduced, and if so what will it be written as?
- Does that return type supply the required inner promise type?
- Is the function one of the kinds that cannot be a coroutine?
- Does anything reach the function by reference, and does it outlive the coroutine rather than the call?

## Notes
The all-or-nothing conversion is the property most likely to surprise, because every other statement-level feature in the language is local. Adding a loop changes a function's behaviour; adding a yield changes what kind of thing the function *is*, including its signature's obligations and its callers' code.

The distinction between the factory and the object is worth insisting on for the same reason it confused the author himself: both are routinely called coroutines. The function is what contains the keyword and what the restrictions above apply to. What it returns is an object with a handle to a suspended computation, and every question about resuming, querying, and destroying is about that object rather than about the function.

The parameter-lifetime consequence deserves more attention than it usually receives. A reference parameter on an ordinary function must outlive the call, which is a short and locally checkable obligation. The same parameter on a coroutine must outlive every suspension and resumption until the coroutine finishes, and nothing in the signature says so.

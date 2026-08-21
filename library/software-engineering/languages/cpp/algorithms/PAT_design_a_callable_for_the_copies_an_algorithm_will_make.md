---
object_id: PAT_design_a_callable_for_the_copies_an_algorithm_will_make
object_type: pattern
name: Design a Callable for the Copies an Algorithm Will Make
library_path:
- software-engineering
- languages
- cpp
- algorithms
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- algorithms
- function_objects
- slicing
- efficiency
cross_links:
- rel: related_to
  target_object_id: PAT_make_a_predicate_a_pure_function
- rel: related_to
  target_object_id: PAT_minimize_compilation_dependencies
- rel: related_to
  target_object_id: PAT_prefer_pass_by_reference_to_const
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Design a Callable for the Copies an Algorithm Will Make

## Pattern Rule
**IF** you are writing a function object, or capturing state in a lambda, to hand to a standard algorithm
**THEN** design it to be copied — keep it small enough that copying is cheap, and keep it free of virtual functions so that copying cannot slice it — because the library's convention is that callables are taken and returned by value
**ELSE** where the callable genuinely needs to be large or polymorphic, keep the object itself small and put the bulk and the virtual functions behind a pointer it holds.

## Do
- Take the convention from where it came, since that explains why it is absolute rather than incidental: the library models these on function pointers, and function pointers are passed by value. The per-element visiting algorithm both takes and returns its callable by value, which is the clearest statement of the rule in the standard itself.
- Keep the object small, because it is copied at least once per algorithm call and sometimes more than that.
- Keep it free of virtual functions. A derived object passed by value into a base-typed parameter loses its derived part in the copy, so the virtual behaviour you wrote is exactly what does not survive being handed to the algorithm.
- Split it where you need bulk or polymorphism. Move the data and the virtual functions into a separate implementation class, leave the callable holding only a pointer to one, and have its call operator forward. The callable is then small and non-polymorphic while behaving as though it were neither.
- Give the split version a copy constructor that does something sensible with the implementation object, since copying is the whole reason the split exists. Sharing it under a reference count is usually the simplest thing that works.

## Don't
- Don't assume a lambda is exempt. A lambda capturing a large object by value is a large callable and is copied exactly as a hand-written class would be; capturing by reference avoids the copying cost and introduces a lifetime question in its place.
- Don't force pass-by-reference by naming the algorithm's template arguments explicitly at the call site. It is legal, almost nobody does it, and some implementations of some algorithms will not compile when the callable arrives by reference.
- Don't conclude that a callable therefore cannot carry state. It can carry as much as you like — the constraint is on how much of it sits directly in the object that gets copied, which is what the split addresses.

## Checklist
- How large is this callable, counting everything captured or stored by value?
- Does it declare, inherit, or override any virtual function?
- If it needs to be polymorphic, is the polymorphism behind a pointer?
- If it holds a pointer to an implementation, what does its copy constructor do with it?

## Notes
Both requirements come from the single fact that these objects are copied, and they fail in different ways, which is why both are worth checking. Excessive size costs time quietly and proportionally. Polymorphism fails loudly in the sense that the wrong function runs, and silently in the sense that nothing reports it — the object simply arrives at the algorithm as a base object.

The split is the standard remedy and has three names in the literature depending on who is describing it, which is a good sign that it is a general technique rather than a workaround for this situation. What matters here is only the direction: the thing that gets copied stays small and concrete, and everything expensive or virtual moves behind the pointer.

The advice reads as being about hand-written functor classes because that is what it was written for, and it transfers to lambdas without amendment. A lambda is a function object with a compiler-written class, and the capture list determines its size exactly as member declarations would.

There is a second reason to hand an algorithm an object rather than a function name, and it is the one that explains a well-known performance result. Naming a function yields a pointer to it, so the algorithm is instantiated on a pointer type and the per-element call goes through that pointer — which compilers generally will not inline. Passing an object instantiates the algorithm on the object's type, so the call operator is a known function at each call site and can be inlined into the loop. That difference, rather than anything about the sorting strategies, is most of why the C++ sorting algorithm outperforms the C library's sorting function on the same data. A lambda gets this automatically, being an object; a function name does not.

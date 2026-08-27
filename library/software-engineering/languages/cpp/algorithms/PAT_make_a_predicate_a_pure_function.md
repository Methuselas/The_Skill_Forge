---
object_id: PAT_make_a_predicate_a_pure_function
object_type: pattern
name: Make a Predicate a Pure Function
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
- correctness
- state
cross_links:
- rel: related_to
  target_object_id: PAT_design_a_callable_for_the_copies_an_algorithm_will_make
- rel: related_to
  target_object_id: PAT_give_an_ordered_container_a_comparison_type_that_is_a_strict_weak_ordering
- rel: related_to
  target_object_id: PAT_name_every_lambda_capture
reference:
  source_title: 'Effective STL: 50 Specific Ways to Improve Your Use of the Standard Template Library'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Make a Predicate a Pure Function

## Pattern Rule
**IF** you are writing something that returns a yes-or-no answer for an algorithm or an ordered container to consult
**THEN** make its answer depend on nothing but its arguments, because algorithms are free to copy it and to keep copies around, so any state it carries can be silently duplicated or reset partway through the operation
**ELSE** where you genuinely need to accumulate something across the elements, that is what the per-element visiting algorithm is for — it imposes no such restriction and hands the object back to you afterwards.

## Do
- Declare the call operator const, which is the cheapest way to catch the common case, since the compiler will then refuse any attempt to modify a member.
- Go further than const, because const is necessary and not sufficient. A const member function may still read and write mutable members, function-local statics, class statics, and anything at namespace scope — all of which make the answer depend on something other than the arguments.
- Apply the same rule to plain functions used as predicates. A function holding a local static counter is exactly as broken as a class holding a member one, and reads as more innocent.
- Reach for the visiting algorithm when the job really is to accumulate. It is the one designed for callables with side effects, and it returns the object so you can extract what it gathered.
- Count the order of application among the things not promised, alongside the copying. An algorithm is free to visit the elements in whatever order suits it — the transforming algorithm says so explicitly — so a callable whose result depends on how many times it has already run, or on what it saw last, is broken for the same reason a stateful one is, and fails the same way: correctly on the implementation you tested. Where the order genuinely matters, an ordinary loop promises what the algorithm declines to.

## Don't
- Don't assume the algorithm calls your predicate the number of times you expect, on the object you handed it. A removal-by-predicate operation is commonly built from a search followed by a conditional copy, with the predicate copied into each — so a predicate that means to fire on the third call fires on the third call *of each copy*, and removes the third element and the sixth.
- Don't let a lambda smuggle the same bug in. A lambda declared mutable that increments a captured counter is precisely the failing case, in a form that looks modern and reads as harmless.
- Don't rely on a diagnostic. Nothing about this fails to compile, nothing throws, and the result is a container missing elements nobody asked to remove — with the count and positions depending on how your implementation happens to build the algorithm.

## Checklist
- Is the call operator const?
- Does the answer depend on anything besides the arguments — a member, a static, a captured variable, a global?
- If a lambda, is it declared mutable, and if so why?
- Is this trying to count or accumulate, and would the visiting algorithm be the right tool instead?

## Notes
The failure is worth walking through once because its shape is so counterintuitive. A predicate meant to return true exactly once, on its third call, is handed to a removal operation. That operation locates the first match with one copy of the predicate and then processes the remainder with a second copy. The first copy counts to three; the second copy starts again at zero and counts to three again. Two elements are removed, the third and the sixth, and neither the code nor the library did anything the standard forbids — the predicate did.

Const-ness is where most people stop and it is the right first step, since it costs nothing and catches the member-variable version. What it does not catch is the version that hides its state somewhere const-ness does not reach, which is why the rule is stated as purity rather than as constness. A well-behaved predicate is certainly const; being const is not what makes it well-behaved.

The same requirement governs the comparison an ordered container holds, for a related but distinct reason: there, an answer that varies over time breaks the ordering invariant rather than the algorithm's internal bookkeeping. Both come back to the same expectation — that asking the same question twice gets the same answer.

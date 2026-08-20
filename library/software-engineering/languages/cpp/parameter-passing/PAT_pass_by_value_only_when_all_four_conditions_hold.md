---
object_id: PAT_pass_by_value_only_when_all_four_conditions_hold
object_type: pattern
name: Pass by Value Only When All Four Conditions Hold
library_path:
- software-engineering
- languages
- cpp
- parameter-passing
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- parameter_passing
- move_semantics
- performance
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_pass_by_reference_to_const
- rel: related_to
  target_object_id: PAT_assume_moves_are_not_present_not_cheap_not_used
- rel: related_to
  target_object_id: PAT_avoid_overloading_on_universal_references
- rel: related_to
  target_object_id: PAT_tell_a_universal_reference_from_an_rvalue_reference
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Pass by Value Only When All Four Conditions Hold

## Pattern Rule
**IF** a function must keep its own copy of an argument, and you are considering taking the parameter by value and moving from it rather than taking a reference to const and copying inside
**THEN** check all four conditions before doing so — the parameter is copyable, cheap to move, always copied, and copied by construction rather than assignment — and take the reference form if any of them fails
**ELSE** where the function only reads its argument, none of this applies and reference to const is the answer.

## Do
- Treat it as something to consider rather than a rule, because it is never free. Taking a reference costs nothing; taking a value costs a construction. What the by-value form buys is that one signature serves lvalues and rvalues efficiently, where the reference form needs a second overload taking an rvalue reference — and the overloads double with each parameter that needs the treatment.
- Require the parameter to be copyable. A move-only type has no copy to compare against, so the reasoning that makes this a trade does not apply; passing such a type by value is a different decision made for different reasons.
- Require moving to be cheap. An lvalue argument costs a copy into the parameter and then a move; a reference form costs one copy. The extra move is the whole price, and for a type that moves no faster than it copies you have simply added a copy.
- Require that the parameter is always copied. A function that inspects its argument and copies it only on some paths pays for the copy on every call, including the ones that discard it.
- Check whether the copy happens by construction or by assignment, because this is where the analysis usually goes wrong. Assigning into an existing member can reuse the storage that member already holds. The by-value path cannot: the parameter is constructed first — allocating — and the subsequent move-assignment releases the member's old storage. That is an allocation and a deallocation the reference form may avoid entirely, and it can cost more than the move saved.
- Notice that the assignment case depends on the *values*, not only the types. Whether the existing storage is big enough for the new value decides whether the reference form avoids an allocation, so the same code is faster or slower depending on the data — which puts the question firmly in the territory of measurement.

## Don't
- Don't apply it to a parameter whose type is a base class. Passing by value slices a derived argument down to its base, losing the derived state and resolving later virtual calls to the base — a correctness failure, not a cost.
- Don't chain it. Passing by value through several layers copies at each one, and the copies accumulate where a reference would have been passed along unchanged.
- Don't assume moving is cheap because the type has move operations. A container that holds its elements directly, or a string short enough to be stored inside the string object, moves at the cost of copying.
- Don't reach for it as a way to avoid writing an rvalue-reference overload without checking the conditions. Avoiding the overload is the benefit; the conditions are what determine whether it is worth what it costs.

## Checklist
- Does this function keep a copy of the argument on every path?
- Is the type copyable, and is moving it genuinely cheaper than copying it?
- Is the copy made by constructing a member, or by assigning to one that already exists?
- If by assignment, could the existing storage often be reused for the new value?
- Is the parameter type a base class of anything?

## Notes
The four conditions look like hedging and are better read as a list of the ways the trade reverses. The by-value form always costs one extra move relative to the reference form for lvalue arguments; everything else in the analysis is about whether that move is small compared to what is saved. Each failed condition is a case where the saving disappears while the extra cost remains.

The construction-versus-assignment distinction deserves more weight than its brevity in the summary suggests, because it is invisible in the signature. Two functions with identical declarations — one initializing a member, one assigning to an existing member — have different answers to this question, and the second one can be substantially worse by value. Storage reuse is the mechanism, and it exists only on the assignment path.

This decision and the perfect-forwarding one solve the same problem from opposite directions, and knowing which you are in matters. A forwarding parameter avoids all copies and drags in overload-resolution behaviour that is difficult to control. A by-value parameter accepts one guaranteed move to keep resolution ordinary. Where the conditions hold, the second is the cheaper decision to live with; where they do not, the reference form with an rvalue overload is what remains.

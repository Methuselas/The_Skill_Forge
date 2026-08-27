---
object_id: PAT_prefer_a_lambda_to_a_bound_call
object_type: pattern
name: Prefer a Lambda to a Bound Call
library_path:
- software-engineering
- languages
- cpp
- lambdas
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- lambdas
- readability
- overloading
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_name_every_lambda_capture
- rel: related_to
  target_object_id: PAT_limit_inlining_to_small_hot_functions
- rel: related_to
  target_object_id: PAT_prefer_the_form_that_refuses_what_you_did_not_mean
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Prefer a Lambda to a Bound Call

## Pattern Rule
**IF** you need a callable that fixes some of another function's arguments in advance
**THEN** write a lambda that calls it, rather than constructing a bound callable from the function and the arguments
**ELSE** where you are limited to C++11 and need to move an object into the callable, or need to bind an object whose call operator is templatized, the bound form is the workaround for a facility C++11 lacks.

## Do
- Take the evaluation timing as the correctness argument, not a stylistic one. Inside a lambda, an argument expression is evaluated when the lambda is called. Passed to a bound call, it is evaluated when the binding is created, and the result is fixed forever — so an expression meaning "one hour from now" means one hour from whenever the binding happened, which is almost never what was wanted.
- Notice that fixing that requires nesting another bound call inside the first, to defer the arithmetic. The lambda needed no such device, and the nested version is substantially harder to read than either.
- Count what positional placeholders cost a reader. They are opaque to anyone who has not learned them, and a reader who has still must map each number to a position in a signature that is not on the screen. A lambda's parameters have names and appear where they are used.
- Prefer the form that works with overloaded functions. A lambda's body contains an ordinary call, so overload resolution picks the right one from the arguments. A bound call is given the function itself, and an overloaded name does not identify one — so the binding needs a cast to a specific function type, spelled out in full.
- Expect better generated code, for a structural reason. The body of a lambda is an ordinary function call the compiler can inline; a bound call typically invokes through a function pointer, which compilers inline far less readily.
- Return the lambda from a function where the values being fixed vary between call sites or are not known until run time. Writing the lambda inline fixes the arguments at the point it appears, which is right for one call site and turns into the same lambda copied several times with different literals once there are several. A function taking those values as parameters and returning the lambda produces the whole family from one definition, and the parameters become the captures — which is the case bound calls were most often reached for, expressed so that the fixed values have names and appear next to the body that uses them.

## Don't
- Don't keep bound calls in modern code out of familiarity. Every advantage they had over the C++98 binders is also an advantage lambdas have, and lambdas do not require learning a second sublanguage of placeholders and reference wrappers.
- Don't assume a bound call captures by reference or by value the way you expect. Arguments are stored by value by default and getting a reference requires a wrapper, which is one more thing that has to be right and cannot be seen at the call site.
- Don't rewrite a working C++11 move-capture workaround just because lambdas are preferred. Where a bound call is emulating a facility C++11 does not have, it is doing a job; replace it when the code moves to a standard where the general capture form exists.

## Checklist
- Does any argument expression here need to be evaluated at call time rather than now?
- Would a reader unfamiliar with placeholders be able to read this?
- Is the called function overloaded?
- Is this callable on a hot path where inlining matters?
- If a bound call is being kept, is it working around a facility this standard version lacks?

## Notes
The timing difference is the part worth understanding rather than memorizing, because the same mistake recurs anywhere arguments are captured eagerly. A lambda's body is code that runs later; a bound call's arguments are values computed now. Anything time-dependent, anything reading mutable state, and anything with a side effect behaves differently between the two, and the difference is invisible at the point of use.

The readability argument is usually stated first and is the weakest of the three, which is worth saying plainly so the case does not rest on taste. Positional placeholders are genuinely harder to read, and people who work with them daily read them fine. The arguments that do not depend on familiarity are the evaluation timing, the behaviour under overloading, and the inlining.

The remaining legitimate uses are narrow and both are compatibility artifacts: emulating a capture that moves an object into the callable, which C++11 cannot express directly, and binding an object whose call operator is a template, which a C++11 lambda cannot accept. Both disappear in C++14, and a codebase on a newer standard has no reason to retain the form.

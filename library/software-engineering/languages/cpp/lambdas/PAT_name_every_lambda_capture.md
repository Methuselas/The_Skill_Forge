---
object_id: PAT_name_every_lambda_capture
object_type: pattern
name: Name Every Lambda Capture
library_path:
- software-engineering
- languages
- cpp
- lambdas
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- lambdas
- lifetime
- move_semantics
- avoiding_surprises
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_a_lambda_to_a_bound_call
- rel: related_to
  target_object_id: PAT_tell_a_universal_reference_from_an_rvalue_reference
- rel: related_to
  target_object_id: PAT_price_shared_ownership_before_choosing_it
- rel: related_to
  target_object_id: PAT_minimize_variable_span_and_live_time
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Name Every Lambda Capture

## Pattern Rule
**IF** you are writing a lambda that captures anything from its enclosing scope
**THEN** list each capture by name, and where the closure member needs to be built from an expression rather than copied from a variable, initialize it explicitly
**ELSE** where the lambda captures nothing at all, say so with an empty capture clause — that is a claim worth making, and the compiler will hold you to it.

## Do
- Reject the by-reference default because of what it hides rather than what it does. A closure holding a reference to a local is fine while both are alive and dangles the moment the closure outlives the scope — and with a named capture, a reader can see which object the closure's viability depends on. With the default, they have to reconstruct it from the body.
- Reject the by-value default for a different reason: it does not do what it appears to. Referring to a data member inside a member function captures the enclosing object's address, not the member — so the closure is tied to that object's lifetime and dangles when the object dies, while looking entirely self-contained.
- Know that the by-value default also fails to make a closure self-contained in the other direction. Objects with static storage duration are not captured at all; the lambda refers to them, so the closure's behaviour changes when they do.
- Use the general capture form to build a closure member from an expression. It lets you give the member its own name and initialize it from anything — a copy of a data member, a value computed on the spot, or an object moved in, which is the only way to get a move-only type into a closure.
- Take the move case as the reason this form exists rather than as an extra. Before it, moving an object into a closure meant writing the function object by hand or using a bound call as a workaround; now the capture states the member's name and its initializer, and moving is just one of the initializers available.
- Say what a lambda captures even when nothing is captured. An empty capture clause is a statement that the closure depends on nothing outside itself, checked by the compiler.

## Don't
- Don't assume an explicit capture of a data member is possible in older code. Inside a member function you can only capture the enclosing object, so making a copy of the member into a local first — and capturing that — was the pre-C++14 answer, and it is what the general capture form replaced.
- Don't read a short-lived lambda as safe by default and reach for the default capture there. The lambdas that outlive their scope are the ones stored in containers, registered as callbacks, or returned — which is also where a default capture is hardest to audit.
- Don't treat a dangling capture as a testing problem. It is undefined behaviour that frequently appears to work, because the memory the reference names is often still readable and often still holds the old value.
- Don't capture an owning smart pointer by value out of habit. Copying a reference-counted pointer into a closure costs an atomic increment and extends the object's lifetime to the closure's, both of which should be decisions rather than side effects of a capture mode.

## Checklist
- Does this capture clause name each captured entity, or use a default mode?
- If the lambda is inside a member function, is it capturing a member or the enclosing object?
- Will this closure outlive the scope that created it — stored, registered, or returned?
- Does the closure refer to anything with static storage duration, and is that intended?
- Is anything being copied into the closure that should have been moved?

## Notes
The two default modes fail in opposite directions and the second is the one that catches experienced programmers. By-reference is obviously a lifetime dependency, and its failures are at least the kind people know to look for. By-value reads as "this closure owns copies of what it needs," which is exactly what it fails to guarantee: a captured data member is really the enclosing object's address, and a static is not captured at all. A closure can therefore be entirely by-value and depend on two things outside itself.

The general capture form changed what the advice costs, which is why it belongs on the same card. Before it, writing captures explicitly was sometimes impossible — you could not name a data member — so the advice competed with the language. Now every capture can be named and initialized, including the ones that need a move, and there is no default mode for the general form at all. The language stopped offering the shortcut in the newer facility, which is the same conclusion arrived at from the other side.

Worth carrying beyond lambdas: the value of an explicit capture list is that it is a written statement of what a piece of code depends on. That is the same property that makes a narrow parameter list better than a wide one, and it fails the same way when a default fills it in silently.

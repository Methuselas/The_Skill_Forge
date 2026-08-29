---
object_id: PAT_lift_each_varying_design_decision_to_a_parameter
object_type: pattern
name: Lift Each Varying Design Decision to a Parameter
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- policy_based_design
- configurability
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_keep_configuration_parameters_orthogonal
- rel: related_to
  target_object_id: PAT_choose_compile_time_or_runtime_variation
- rel: related_to
  target_object_id: PAT_program_to_a_templates_implicit_interface
- rel: related_to
  target_object_id: PAT_use_dependency_injection
- rel: related_to
  target_object_id: AP_design_a_customization_point
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Lift Each Varying Design Decision to a Parameter

## Pattern Rule
**IF** a class settles internally a question that could sensibly be answered more than one way — how it allocates, how it locks, how it checks before use, how it stores what it holds
**THEN** name that question, move the answer out to its own template parameter, and leave the class assembling the answers rather than choosing among them.

## Do
- Walk the class and write down every question it currently answers by itself. The ones worth lifting are those where a different project would reasonably want a different answer.
- Give each parameter a name and state the expressions a conforming answer must support — a `Create` returning `T*`, a `Check` callable on `T*`, an inner `Lock` constructible from `T&`. That expression set is the whole contract.
- Supply a default for the answer most users want, so the common instantiation names no parameters at all.
- Inherit the parameters where clients should see any extra members they carry, and hold them by value where they should not.
- Keep the assembly in the class: it orders and combines what the parameters supply and implements none of it.

## Don't
- Don't answer everything behind one large interface. As options multiply, the subset of calls that is semantically valid shrinks inside a syntax that still compiles, and the compiler stops catching misuse.
- Don't ship a named class per combination. Three independent binary choices is eight classes, the fourth doubles it, and the first customization nobody predicted makes all of them useless.
- Don't reach for multiple inheritance alone to combine the pieces. Base classes are superposed with no orchestration between them, they cannot see the type they are configuring, and any shared state forces virtual inheritance into a design that was supposed to be simple.
- Don't push past roughly four to six parameters. Past that the instantiation is harder to read than the code it replaced, and that is a signal the class is doing too much rather than a limit to work around.
- Don't overlook that a different answer produces a different type, and budget for it. Everything written against the default instantiation — the overloads that print it, the functions that take it, the containers declared to hold it — was written against that type and not against the template, so an instantiation differing in one parameter interoperates with none of it until each piece is provided again. Changing how a string's characters compare is one parameter and a handful of overridden operations, and the result cannot be streamed to output or passed to anything expecting the ordinary string until it is given its own machinery. That is the price of the lift and it is worth naming, because it is invisible while the default is the only instantiation anyone has made.

## Checklist
- Can I name every question this class answers, and is each one reachable from outside it?
- Does the default instantiation compile with no arguments supplied?
- If a client needs a combination I never thought of, can they write it without editing my code?
- Is anything left inside the class that a reasonable project would want to answer differently?

## Notes
The argument for doing this is combinatorial rather than stylistic. A component with several independent axes has a product of behaviors, and any approach that enumerates them — one class per combination, or one interface covering all of them — grows exponentially while the code that assembles parameters grows additively.

The useful test for what to lift is the same one that identifies a magic number: a constant buried in code and a design choice buried in a class are the same defect, and both are fixed by giving the thing a name and a way in.

This is not what virtual functions do, even though both let a caller supply behavior. The binding here happens during compilation, so the parameters carry full type information, the compiler checks the combination, and nothing costs a dispatch at runtime. The price is that the choice must be known when the code is compiled, which is why the mechanism decision comes first.

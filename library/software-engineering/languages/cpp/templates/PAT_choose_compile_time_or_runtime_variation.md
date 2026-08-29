---
object_id: PAT_choose_compile_time_or_runtime_variation
object_type: pattern
name: Choose Compile-Time or Runtime Variation
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
- polymorphism
- abi
- class_design
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_lift_each_varying_design_decision_to_a_parameter
- rel: related_to
  target_object_id: PAT_externalize_varying_behavior_with_strategy
- rel: related_to
  target_object_id: PAT_price_virtual_dispatch_against_the_real_alternative
- rel: related_to
  target_object_id: PAT_match_virtualness_to_inherited_interface
- rel: related_to
  target_object_id: AP_design_a_customization_point
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Choose Compile-Time or Runtime Variation

## Pattern Rule
**IF** a component has behavior that must vary and you are deciding what carries the variation
**THEN** settle first whether the choice is known when the code is compiled, because that answer — not elegance or familiarity — decides between a template parameter and a virtual function.

## Do
- Ask when the answer is known. Fixed for the lifetime of a build points to a parameter; chosen from a config file, a command line, or user action at runtime points to a virtual.
- Ask who crosses the boundary. Anything published across a shared library, a plugin seam, or a stable binary interface needs the runtime mechanism, because a parameter produces a distinct type per combination and no fixed layout to link against.
- Ask whether the varying part needs to see the type it configures. A parameter does and a base class does not, which is what lets compile-time variation create objects, name inner types, and size things it was given.
- Where both are legitimate, prefer the parameter for the leaf components others build on and the virtual for the seams your users extend.

## Don't
- Don't reach for the compile-time route to avoid a dispatch that was never measured. It buys the dispatch back in compile time, distinct types, and error messages that name instantiations rather than mistakes.
- Don't mix the two for one axis. A virtual whose implementation is selected by a parameter answers the same question twice and doubles the surface a reader has to hold.
- Don't assume the compile-time route is always faster overall. Every distinct combination is separately generated code, and enough of them can cost more in instruction cache than the calls they removed.
- Don't decide this after the class exists. Reversing it is not a local edit — it changes what the type is, so every declaration of it changes with it.

## Checklist
- At what moment is the answer to this question known, and can I name that moment?
- Does any published binary interface expose this type?
- Does the varying part need to know the type it is configuring?
- Have I answered this once per axis rather than carrying both mechanisms for the same one?

## Notes
The two mechanisms look interchangeable because both let a caller supply behavior into a component, and they are not. The parameter is bound during compilation, so it brings full type knowledge, the compiler checks the combination, and there is nothing to dispatch. The virtual is bound at runtime, so it survives across a binary boundary, allows the answer to change while the program runs, and needs only one compiled copy.

Neither is a better version of the other, which is why the decision is a real one rather than a default with an exception list. They fail in opposite directions: the compile-time route cannot express a choice made after the build, and the runtime route cannot express a choice the type system is supposed to check.

The costs are also asymmetric in when they arrive. Runtime dispatch charges a known amount on every call, visible in a profile. Compile-time variation charges nothing per call and instead charges build time, code size, and diagnostic difficulty — quieter, later, and harder to attribute to the decision that caused it.

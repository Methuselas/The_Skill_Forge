---
object_id: PAT_avoid_overloading_on_universal_references
object_type: pattern
name: Avoid Overloading on Universal References
library_path:
- software-engineering
- languages
- cpp
- move-semantics
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- move_semantics
- overloading
- templates
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_tell_a_universal_reference_from_an_rvalue_reference
- rel: related_to
  target_object_id: PAT_delete_the_functions_you_want_to_forbid
- rel: related_to
  target_object_id: PAT_understand_special_member_generation
- rel: related_to
  target_object_id: PAT_make_interfaces_hard_to_misuse
reference:
  source_title: 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Avoid Overloading on Universal References

## Pattern Rule
**IF** you are adding an overload to a function or constructor that already takes a universal reference, or adding a universal reference overload to an existing set
**THEN** don't — choose one of the alternatives that keeps the perfect-forwarding benefit without putting a universal reference into overload resolution
**ELSE** where you can constrain the template so it is only a candidate for the argument types you intend, the two can coexist, and the constraint is what makes it safe rather than the overloading.

## Do
- Expect the universal reference overload to win far more often than it looks like it should. It is an exact match for almost any argument, so any other overload requiring even a trivial conversion loses to it — including the ones a reader would assume were written for exactly that case.
- Treat a perfect-forwarding constructor as the dangerous case rather than one case among several. It is a better match than the copy constructor for a non-const lvalue of the same class, so copying a non-const object calls the forwarding constructor instead. And in a derived class, the base copy and move constructors are hijacked the same way.
- Take the simplest alternative that works: give the functions different names. Perfect forwarding is not tied to a shared name, and abandoning the overload set costs nothing where the operations are conceptually distinct.
- Pass by reference to const where the efficiency of forwarding is not what the code needs. It gives up a move in some cases and it restores ordinary, predictable overload resolution.
- Pass by value where the parameter will be copied into the object anyway and the type is cheap to move. That gives most of the forwarding benefit with none of the overload-resolution behaviour.
- Use tag dispatch where one function must handle several argument categories: keep a single unconstrained entry point that forwards to implementation functions selected by a type tag rather than by overload resolution on the argument itself.
- Constrain the template where universal references and overloading genuinely must coexist. Making the forwarding overload a candidate only under a stated condition is the mechanism that puts you back in control of when it can be selected, and it is worth the complexity only when the simpler alternatives have been ruled out.

## Don't
- Don't add a universal reference overload to an existing function and expect existing calls to keep resolving as they did. It competes with everything and beats most of it, so calls silently change destination.
- Don't try to fix a hijacked copy constructor by adding more overloads. Each addition is another candidate the forwarding constructor outranks, and the resulting error messages are among the worst the language produces.
- Don't assume a deleted overload solves it in the constructor case. Deleting an overload removes a candidate, but the forwarding constructor is still selected for anything you did not think to delete.
- Don't reach for a constrained template first. It is the most powerful alternative and the most intricate, and most cases are better served by different names or by passing by value.

## Checklist
- Does this overload set contain a universal reference parameter?
- For each other overload: is there an argument type for which it would now lose to the forwarding one?
- If this is a constructor, what happens when a non-const lvalue of the class is copied?
- If the class has derived classes, what happens to their copy and move constructors?
- Have the simpler alternatives — distinct names, reference to const, by value, tag dispatch — been ruled out before constraining the template?

## Notes
The reason this goes wrong so reliably is that a universal reference parameter is not one candidate among many; it instantiates to an exact match for whatever it is given. Overload resolution then prefers it over anything needing a conversion, including conversions so small a reader does not register them as conversions at all — a string literal against a parameter taking a string, a non-const lvalue against a parameter taking a reference to const.

The constructor case is worth separating because the competing overloads are not ones you wrote. Copy and move constructors are generated or declared elsewhere, so the hijack shows up as a copy that no longer works rather than as an obviously wrong overload being chosen, and in a hierarchy the failure appears in a derived class whose author never saw the forwarding constructor.

The alternatives are listed in the order to try them for a reason. Different names, reference to const, and by value are each ordinary design moves with well-understood costs. Tag dispatch adds a layer of indirection but keeps resolution under your control. Constraining a template is the only one that lets universal references and overloading truly coexist, and it is also the one that puts the conditions for selection into a form that most readers will not be able to check.

---
object_id: PAT_let_a_host_degrade_gracefully_on_optional_features
object_type: pattern
name: Let a Class Degrade Gracefully on Optional Parameter Features
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- policy_based_design
- instantiation
- interface_design
cross_links:
- rel: related_to
  target_object_id: PAT_lift_each_varying_design_decision_to_a_parameter
- rel: related_to
  target_object_id: PAT_program_to_a_templates_implicit_interface
- rel: related_to
  target_object_id: PAT_use_template_metaprogramming
- rel: related_to
  target_object_id: AP_design_a_customization_point
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Let a Class Degrade Gracefully on Optional Parameter Features

## Pattern Rule
**IF** a template parameter supplies capability beyond the minimum the class requires, and you want the class to offer something built on that capability
**THEN** write the extra member against the richer capability and require only the minimum in the contract, because a member function of a class template that nobody calls is never instantiated and so never has to compile.

## Do
- State the contract in two layers: what every argument must supply, and what an argument may additionally supply along with what the class will then offer.
- Write the extra member as ordinary code against the richer capability. No detection, no branch, no specialization is needed for the degradation itself.
- Let the extra members a parameter carries reach clients directly, where public inheritance already puts them — clients who chose that parameter get the richer interface without the class mediating it.
- Where a client later switches to a leaner argument, read the resulting errors as the list of places that depended on the richer one. That list is what you want.

## Don't
- Don't require the full capability from every argument so the class always compiles. That forces every lean implementation to supply members that do nothing, which is the interface bloat the parameters were separated to avoid.
- Don't rely on this for anything other than uncalled member functions. What the language guarantees is that names are not looked up in an uninstantiated member; how much syntax checking happens is left to the implementation, so an unused member is not a place to keep something half-written.
- Don't leave the optional part undocumented and let clients discover it by compiler error. The two-layer contract is the interface, and only its lower layer is enforced.

## Checklist
- Does the class compile and work when given an argument supplying only the minimum?
- Does the extra member exist for clients who supply more, without any conditional code?
- Is the optional capability written down, including what the class offers in return for it?
- When a lean argument is substituted, do the errors land at the use sites rather than inside the class?

## Notes
This is a consequence of the instantiation model rather than a technique layered on top of it. Because an uncalled member of a class template is not instantiated, one class can span a range of arguments from minimal to rich, and the point at which an argument becomes insufficient is the exact line where a client used something it does not supply.

The result is worth naming: a class can offer more than its contract requires without penalising the implementations that supply only the contract. The alternative designs both fail — demanding the richer capability everywhere forces empty members onto lean implementations, and offering nothing extra wastes what a rich argument brought.

Modern C++ gives more direct ways to ask what an argument supports, and they are better where the class must actually branch on the answer. They do not replace this: the point here is that no branch is needed at all when the only consequence of a missing capability should be that one member is unavailable.

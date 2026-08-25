---
object_id: PAT_let_each_type_register_itself_with_the_factory
object_type: pattern
name: Let Each Type Register Itself With the Factory
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- factories
- extensibility
- deserialization
- coupling
cross_links:
- rel: related_to
  target_object_id: PAT_give_a_polymorphic_class_a_virtual_clone
- rel: related_to
  target_object_id: PAT_dont_use_the_runtime_type_name_as_a_persistent_id
- rel: related_to
  target_object_id: PAT_design_the_physical_dependency_graph_too
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Let Each Type Register Itself With the Factory

## Pattern Rule
**IF** you must build an object whose type is decided by data that only exists at runtime — read from a file, a message, a configuration, a user's choice — and the set of possible types is open
**THEN** have each type register a creator for itself under an identifier, and let the builder look the identifier up, so adding a type means adding a file rather than editing several.
**ELSE** where the set is genuinely fixed, small, and closed by design, a single decision point that names every type is simpler and honest about the closure.

## Do
- Give the builder three parts and no knowledge of any concrete type: an identifier to match on, a creator that makes exactly one type, and a table joining them.
- Put each registration beside the type it creates, so the fact that a type participates lives in the same file as the type.
- Make registration report whether it succeeded. Two types claiming one identifier is a collision that must fail where it happens, not later where one of them silently cannot be built.
- Decide what an unknown identifier does, and make it the caller's choice rather than the builder's. Throwing, returning nothing, and loading something on demand are all reasonable in different systems, and the builder is the wrong place to settle it.
- Keep the identifier's meaning stable once anything has been written using it. It is part of the stored format from the first time data is saved.

## Don't
- Don't switch on a type tag in one place. Three costs arrive together: that file must name every type in the system, so it becomes a compile-time bottleneck that rebuilds whenever any of them changes; adding a type means editing it as well as the type; and nothing detects the edit that was forgotten.
- Don't treat the centralized version as the simple option because it is shorter today. It is shorter for the first few types and grows a required edit for every one after that, spread across the identifier list, the writing side, and the decision point.
- Don't let the builder include the headers of the things it builds. The moment it does, it knows the concrete set and the arrangement has bought nothing.
- Don't skip the collision check because identifiers are assigned by hand. Assigning by hand is exactly when two types get the same one.

## Checklist
- Does adding a new type require editing any file other than its own?
- Does the builder's source name, include, or otherwise know any concrete type?
- If two types claim the same identifier, when is that discovered, and by whom?
- Are the identifiers stable enough to appear in data that will outlive this build?

## Notes
The thing being fixed is a specific asymmetry. Calling a method on an object binds the caller only to the interface, while creating an object binds it to the exact concrete type, so a system carefully decoupled everywhere else still has every concrete name gathered in whichever file does the creating. A concrete type name in a construction expression is doing what a magic constant does elsewhere.

Registration moves the knowledge to where it already exists. The type knows what it is and how to make one of itself; the builder only needs to be told. That inverts who depends on whom, which is what makes the difference between adding files and editing them, and it is the property worth protecting when the arrangement is under pressure to take a shortcut.

The honest limitation is that registration has to actually happen before a lookup can succeed, which puts weight on how and when it runs. That cost is real and is the reason the centralized version remains the better answer for a genuinely closed set — the trade is a startup-order concern against a maintenance edit per type, and which one dominates depends on how open the set really is.

---
object_id: PAT_choose_which_axis_stays_easy_to_extend
object_type: pattern
name: Choose Which Axis Stays Easy to Extend
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
- extensibility
- visitor
- coupling
- dependencies
cross_links:
- rel: related_to
  target_object_id: PAT_expect_a_design_maneuver_to_cost_another_dimension
- rel: related_to
  target_object_id: PAT_let_each_type_register_itself_with_the_factory
- rel: related_to
  target_object_id: PAT_give_a_polymorphic_class_a_virtual_clone
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Choose Which Axis Stays Easy to Extend

## Pattern Rule
**IF** you hold a set of related types and a set of operations over them, and you are deciding where a new operation should live
**THEN** decide first which of the two sets will actually change more often, because the ordinary arrangement makes adding a type cheap and adding an operation expensive, and the arrangement that inverts that inverts both halves.
**ELSE** where both sets change at similar rates, keep the ordinary arrangement — the inversion costs discipline continuously and only pays where operations dominate.

## Do
- Count the history rather than guessing. How many types and how many operations were added in the last year answers this; an intention to keep the type set stable does not.
- Take the ordinary arrangement — each operation as a method on each type — when types are the volatile set. Adding one is then a new file that touches nothing, and nothing recompiles.
- Take the inverted arrangement — each operation as its own object, with the types offering a single dispatch entry point — when operations are the volatile set. Adding one is then a new class, and no existing type changes.
- Decide, when inverting, whether an unhandled type is a compile error or a silent default. Requiring every operation to handle every type gets the compiler to list what a new type broke; providing a fallback keeps things building and lets the omission reach production. Both are defensible and the choice should be made once, deliberately.

## Don't
- Don't invert on the strength of one painful operation. The inversion moves the pain rather than removing it: from that point on, every new type touches the operation interface and every operation implementing it.
- Don't expect the inverted form to give operations the access a method has. An operation living outside the type sees only its public interface, so anything needing internals either stays a method or forces the type to widen — which is a real cost and often the deciding one.
- Don't factor the dispatch entry point up into the base class because every implementation looks identical. They are identical in text and different in meaning: each resolves against the static type of the object it sits in, and moving it to the base makes them all resolve against the base. The result compiles and dispatches to the wrong place, and it is a tempting thing for someone tidying duplication to do.
- Don't assume a type is participating just because it compiles. A type derived from one that already supplies the dispatch entry point inherits it, so it silently dispatches as its parent — the compiler asks for nothing and the operation never runs for it.

## Checklist
- Which set has grown more in this codebase's actual history, types or operations?
- If a new type is added tomorrow, what breaks, and does the compiler say so?
- Do any operations need more than the public interface of the types they act on?
- Is there exactly one dispatch entry point per concrete type, defined in that type rather than inherited?

## Notes
The asymmetry that makes this a decision is built into ordinary class hierarchies and easy to miss because it feels like the natural order of things. Deriving a new type is cheap — nothing existing changes, nothing recompiles. Adding an operation across the hierarchy is expensive, because it lands on the root that everything depends on. So the default arrangement has already chosen an answer, silently, in favour of whichever set of changes is cheaper to make.

Inverting it is a genuine trade rather than an improvement. Operations become objects and gain the freedom that types had — a new one is a new class touching nothing — and types lose it, because each new type must now be named by every operation. Nothing is bought outright; the cheap direction is being pointed somewhere else, and pointing it wrongly is worse than leaving it alone.

The two failure modes both go unreported, which is why the checks matter more here than the mechanism. The dispatch entry point is one line per type that looks like duplication and is not, and a type that inherits one instead of declaring its own participates incorrectly while compiling cleanly. Neither produces a diagnostic, and both surface as an operation quietly doing nothing for one kind of object.

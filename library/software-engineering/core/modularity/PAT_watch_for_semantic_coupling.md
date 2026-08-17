---
object_id: PAT_watch_for_semantic_coupling
object_type: pattern
name: Catch the Coupling That the Compiler Cannot See
library_path:
- software-engineering
- core
- modularity
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- coupling
- modularity
- design
- hidden_dependencies
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
- rel: related_to
  target_object_id: PAT_ask_what_should_be_hidden
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Catch the Coupling That the Compiler Cannot See

## Pattern Rule
**IF** two modules interact and you are judging how tightly they are bound
**THEN** look past the syntax for places where one relies on knowledge of the other's inner workings, because that dependency compiles cleanly, passes tests, and breaks when the other module is changed by someone who never saw the assumption.

## Do
- Hunt the four shapes specifically. One module passes a control flag telling another what to do; one reads global data assuming another has already modified it correctly and been called at the right time; one skips a documented `Initialize()` because it knows the other's `Routine()` calls it anyway; one passes a partly-filled object because it knows only three of seven methods will be used.
- Judge coupling on size, visibility, and flexibility rather than on whether it compiles. Fewer connections is better; a connection through a parameter list is honest where one through modified global data is sneaky; and the real test of flexibility is whether a third module with the same data but a different shape could call this at all.
- Run the third-caller test on any interface you think is loosely coupled. A routine taking an `Employee` looks fine until something holding only a hiring date and a job classification needs it — then the choice is a faked-up object built from internal knowledge, or changing the signature. Taking the two fields it actually uses was the loose version all along.
- Split along the lines of least interconnectedness. If the program were wood, split it with the grain.
- Where a control flag is genuinely needed, give it a defined type — an enumerated type or an object — which converts a semantic assumption into one the compiler checks.
- Mine the commit history for files that keep changing together. Two modules modified in the same changeset again and again are bound by something, and since the binding survived every review that let those changes through, it is unlikely to be visible in either file on its own.

## Don't
- Don't count syntactic connections and call it a coupling review. Passing primitives through parameter lists is normal and acceptable; instantiating an object is fine; the damage is in the assumptions travelling alongside.
- Don't accept documentation as a fix for a hidden connection. Documenting a global-data dependency makes it slightly better by making it more obvious; it does not make it loose.
- Don't leave an ordering requirement as a convention. "Call Initialize first" that works either way is an invitation to depend on the wrong half of it.

## Checklist
- For each connection: what does the caller assume about what happens on the other side?
- Could a third module with the same data in a different shape call this without faking anything?
- Is anything here relying on call order, on prior global state, or on which fields will actually be read?
- Are the control flags typed, or are they raw values carrying meaning by convention?
- Which pairs of files in this area are almost never committed apart, and what is the reason for each pair?

## Notes
Semantic coupling is called the most insidious kind for a specific reason: every other kind announces itself. Too many parameters, an object passed where a primitive would do, a shared global — all are visible in the text. A semantic dependency is invisible precisely because the code is syntactically correct and behaves correctly today. It fails later, in the other module, when someone makes a change that was legal by every check available to them.

The useful mental image for the good case is the model railroad coupler: two opposing hooks that latch when the cars are pushed together. Connecting is easy because the mechanism is as simple as it can be. Screwing things together, connecting sets of wires, or only certain cars fitting certain other cars are all recognisable in code, and all are the same failure — the connection knowing more than it needs to.

Reading the change history is worth adding to the inspection because it detects from the outside what the four shapes above are found by reading from the inside. A hidden assumption shows up in the record as a habit — every change to one file accompanied by a change to another — and that habit is measurable without understanding either file. It is a lead rather than a finding, since plenty of co-change is legitimate: source moves with its tests, and a configuration file moves with everything. What makes the signal useful is the cases it points at that nobody suspected, which typically resolve into one of two things — an abstraction drawn in the wrong place, so that one conceptual change always lands in two modules, or the same logic copied into both and dutifully maintained in parallel. Both are worth finding, and neither announces itself to a reader looking at one file at a time.

The flexibility criterion is the one most often mis-scored, because it looks satisfied when the other two are. A single visible connection carrying a rich object scores well on size and visibility while being rigid in exactly the way that matters — the interface has quietly required its callers to be a particular kind of caller. Asking who *else* could call this is what exposes it.

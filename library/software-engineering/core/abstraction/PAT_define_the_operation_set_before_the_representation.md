---
object_id: PAT_define_the_operation_set_before_the_representation
object_type: pattern
name: Name the Operations the Thing Supports Before Choosing How to Store It
library_path:
- software-engineering
- core
- abstraction
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- abstract_data_type
- abstraction
- class_design
- interface_design
cross_links:
- rel: related_to
  target_object_id: PAT_ask_what_should_be_hidden
- rel: prerequisite_for
  target_object_id: PAT_guard_the_interface_abstraction_under_modification
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u06, pp. 126-137
  evidence_type: text
confidence: high
references: []
variants: []
---

# Name the Operations the Thing Supports Before Choosing How to Store It

## Pattern Rule
**IF** you are creating a class, module, or type for some entity in the problem
**THEN** write down the operations that entity supports in the language of the problem first, and only then decide how its data is represented — the operation set is the abstraction, the representation is an implementation detail you are entitled to change later.

## Do
- Phrase the operations in problem-domain terms rather than storage terms. `currentFont.SetBoldOn()` and `coolingSystem.OpenValve(n)` name things the domain does; `currentFont.attribute = currentFont.attribute or 0x02` names how a bit happens to be stored.
- Check each operation for its opposite. Most have an equal and opposite counterpart — on/off, add/remove, activate/deactivate — so review each public routine and ask whether its complement is needed. Do not manufacture one gratuitously; do check.
- Let the operation set expose distinctions the representation cannot. A font that stores one size can still offer `SetSizeInPoints` and `SetSizeInPixels`; a single exposed `size` field forces the caller to know which unit is meant and gives you no way to say.
- Choose the abstraction deliberately when two candidates are close. Wrapping a 150-routine spreadsheet control to serve as a grid control means exposing the 15 grid routines plus the one extra capability you needed — not all 150. Exposing everything is not encapsulation with extra steps; it is the absence of encapsulation plus extra work.
- Expect the routine bodies to be short, often no more than the ad-hoc lines they replace. The gain is not less code; it is that the operations are in one place and the representation is now yours to change.

## Don't
- Don't let a class become a carrying case for loosely related data and routines. That is what a class is when nobody decided what it abstracts — a class in name only.
- Don't leak the container you happened to use. A census class that inherits from a list container presents two abstractions at once, and inheriting to gain the container's polymorphism fails the is-a test outright.
- Don't expose the data and call it an interface. A point exposing three floats cannot know when its own values change; the same point behind accessors could store them as doubles, or on the moon, and no caller would need to care.
- Don't reach for the low-level type when the domain has a name for the thing. Inserting a node into a linked list is a weaker place to be working than adding a cell to a spreadsheet or a car to a train simulation.

## Checklist
- Can you list this thing's operations without naming a data structure?
- Does each operation read as something the domain does, or as something the storage does?
- Which operations have opposites, and are the ones you need present?
- If you changed the representation tomorrow, how many call sites would move?
- Is any operation here exposed only because the underlying library happened to offer it?

## Notes
The empirical result is unusually direct for a design claim. Woodfield, Dunsmore and Shen gave students two versions of the same program — one split into eight routines along functional lines, one into eight abstract-data-type routines — and the ADT group scored over 30 percent higher answering questions about it. The difference was comprehension, which is the thing the operation-set framing buys.

The benefits fall out of one property: callers hold operations rather than data. Implementation details can then change in one place; the interface can be made more informative than the storage; performance work becomes recoding a few named routines instead of combing the program; correctness gets easier to check, because a call to `SetBoldOn()` can only be the wrong routine name, while `attribute = attribute or 0x02` can have the wrong structure, field, operator, or constant. And the data stops travelling — it neither gets passed to every routine that touches it nor becomes global, because the routines that need it are the ones that own it.

The trap the framing avoids is subtle enough that McConnell names it as the reason to understand ADTs before classes. Reaching for a class first produces a container for whatever data seemed related, with routines attached. Reaching for the operation set first produces a thing the rest of the program can talk to in its own vocabulary — and the class is then just how that gets written down in this language.

---
object_id: PAT_make_immutability_deep
object_type: pattern
name: Make Immutability Deep, Not Just Shallow
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- immutability
- defensive_copying
- references
- hard_to_misuse
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_immutable_objects
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make Immutability Deep, Not Just Shallow

## Pattern Rule
**IF** an otherwise-immutable class holds a member of a mutable type, such as a list or map
**THEN** close the shared-reference holes — either defensively copy the object coming in and going out, or, better, store it in an immutable data structure — so no outside code can mutate the class's internals through a shared reference.

## Do
- Recognize that a final member holds a reference, not the object: if the caller keeps the same list they passed to the constructor, or the list returned by a getter, they can mutate the class's state from outside (the two scenarios that turn a font family into Comic Sans).
- Defensively copy at both boundaries when you must — copy the incoming list in the constructor and copy again in the getter — so the class references a list only it knows about.
- Prefer an immutable data structure (an immutable list from a library) which removes the need to copy at all and blocks even in-class mutation.

## Don't
- Don't assume marking a member final makes it deeply immutable; final stops reassignment but not `list.add(...)`, so internal code can still mutate the contents.
- Don't defensively copy large structures on hot paths without weighing the cost; copying a huge font family on every construct and getter call can hurt performance where an immutable structure would not.

## Checklist
- Can a caller mutate this object's internals through a reference they kept or received?
- Are mutable members either defensively copied at both boundaries or held as immutable structures?
- Could code inside the class itself accidentally mutate a member the class means to freeze?

## Notes
Shallow immutability is a common trap: `TextOptions` looks immutable with a final font-family list, yet scenario A (caller keeps the constructor's list) and scenario B (caller mutates the getter's return) both rewrite its state, because all three share one list object. Defensive copying at construction and return closes both holes but costs copies and still lets in-class code mutate; an immutable list is the more robust choice, needing no copies and refusing mutation from anywhere. C++'s const correctness achieves the same at the compiler level.

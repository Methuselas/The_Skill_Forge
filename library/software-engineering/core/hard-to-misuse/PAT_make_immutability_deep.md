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
- rel: related_to
  target_object_id: AP_make_a_class_immutable
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make Immutability Deep, Not Just Shallow

## Pattern Rule
**IF** something presented as unchanging shares a reference to a mutable value with code outside it — a class member of mutable type, a container returned from a function, a result assembled from an argument and handed back
**THEN** close the shared-reference holes — either defensively copy the value coming in and going out, or, better, hold it in an immutable data structure — so nothing outside can reach the internals through a shared reference.

## Do
- Recognize that a final member holds a reference, not the object: if the caller keeps the same list they passed to the constructor, or the list returned by a getter, they can mutate the class's state from outside (the two scenarios that turn a font family into Comic Sans).
- Defensively copy at both boundaries when you must — copy the incoming list in the constructor and copy again in the getter — so the class references a list only it knows about.
- Prefer an immutable data structure (an immutable list from a library) which removes the need to copy at all and blocks even in-class mutation.
- Apply the same test to a function that returns a container assembled from its arguments. Copying the top level and rebuilding only the parts that changed leaves every untouched part shared with the input, so the returned value is new and its contents are not. A caller who mutates one of those parts alters the argument they passed in, and the signature says nothing about it. The hole is the one a getter opens; only the boundary has moved.
- Decide how deep the copy goes and record it where a caller will look. Depth is the whole question here and it is the one thing neither the name nor the type carries, so a function that copies one level and shares the rest has to say so.

## Don't
- Don't assume marking a member final makes it deeply immutable; final stops reassignment but not `list.add(...)`, so internal code can still mutate the contents.
- Don't let a name suggest a copy that was not made. Words like update, merge, or with all promise a new value, and what they usually deliver is a new top level over shared contents, which is exactly the arrangement a caller will not think to check.
- Don't defensively copy large structures on hot paths without weighing the cost; copying a huge font family on every construct and getter call can hurt performance where an immutable structure would not.

## Checklist
- Can a caller mutate this object's internals through a reference they kept or received?
- Are mutable members either defensively copied at both boundaries or held as immutable structures?
- Could code inside the class itself accidentally mutate a member the class means to freeze?
- If this returns a container assembled from its inputs, which parts of the result still
  alias the input, and does anything tell the caller?

## Notes
Shallow immutability is a common trap: `TextOptions` looks immutable with a final font-family list, yet scenario A (caller keeps the constructor's list) and scenario B (caller mutates the getter's return) both rewrite its state, because all three share one list object. Defensive copying at construction and return closes both holes but costs copies and still lets in-class code mutate; an immutable list is the more robust choice, needing no copies and refusing mutation from anywhere. C++'s const correctness achieves the same at the compiler level.

What varies between instances of this is the boundary, not the hole. A class exposes one through its constructor and its getter; a function exposes the same one through its parameter and its return, and a builder through whatever it was handed before it produced a result. In every case a reference to mutable structure has crossed from one side to the other while both sides believe they own it, and the remedy is the same pair: copy at the crossing, or hold something that cannot be mutated at all. Reading the rule as being about class members leaves the function case looking unrelated, which it is not — it is the more common of the two in any language where returning a rebuilt container is idiomatic.

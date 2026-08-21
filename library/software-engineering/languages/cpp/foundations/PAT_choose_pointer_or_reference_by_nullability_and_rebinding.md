---
object_id: PAT_choose_pointer_or_reference_by_nullability_and_rebinding
object_type: pattern
name: Choose Between Pointer and Reference by Nullability and Rebinding
library_path:
- software-engineering
- languages
- cpp
- foundations
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- foundations
- interface_design
- references
- pointers
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_pass_by_reference_to_const
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Choose Between Pointer and Reference by Nullability and Rebinding

## Pattern Rule
**IF** you are declaring a variable, data member, parameter, or return type whose job is to refer indirectly to some other object
**THEN** take a reference when there will always be an object to refer to and you will never need to refer to a different one, and a pointer the moment either of those can fail
**ELSE** where an operator's syntax requires that its result be assignable — subscripting is the common case — a reference is the only workable return type whatever the two answers were.

## Do
- Settle the two facts about the design first, because the language enforces both answers rather than merely encouraging them: a reference must be initialized where it is declared, and assigning through one changes the referred-to object's value, never which object is referred to.
- Drop the validity test in functions that take references. A function taking a pointer generally has to check it before dereferencing; the same function taking a reference does not, because the caller could not have supplied nothing.
- Return a reference from subscripting so clients write the assignment directly. Returning a pointer would force the extra dereference at every call, which reads as though the container held pointers rather than values.

## Don't
- Don't reach for a pointer to keep the option of retargeting a thing the design never retargets. The cost is a null state every caller can produce and a check at every use, bought to preserve flexibility nobody uses.
- Don't manufacture a null reference by binding one to a dereferenced null pointer. The behavior is undefined, and the whole benefit of the reference — that it is known to refer to something — is gone the moment such code exists anywhere in reach.

## Checklist
- Can the thing being referred to legitimately be absent at any point in its lifetime?
- Will this ever be made to refer to a different object after it is first set?
- If both answers are no, is there a stated reason it is not a reference?
- Does any function here test a reference parameter against null?

## Notes
The choice usually gets made by habit rather than by decision, and the habit runs toward pointers because that is what C offered. Both facts that decide it are structural: a reference has no uninitialized state and no rebinding operation, so choosing one is a way of writing the constraint into the type instead of into a comment or a check.

There is a small efficiency argument on the reference side, which is that no validity test is needed before use, but it is a consequence of the design constraint rather than a reason to adopt it. The reason to adopt it is that the constraint is real and the type can carry it.

The operator exception is not a preference. Overloaded subscripting typically has to yield something usable as the target of an assignment, and only a reference does that with the expected syntax.

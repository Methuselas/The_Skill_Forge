---
object_id: PAT_interpose_a_proxy_when_an_operator_cannot_see_its_context
object_type: pattern
name: Interpose a Proxy When an Operator Cannot See Its Own Context
library_path:
- software-engineering
- languages
- cpp
- operators
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- operators
- proxy_types
- class_design
- lazy_evaluation
cross_links:
- rel: related_to
  target_object_id: PAT_force_the_deduced_type_with_an_explicit_cast
- rel: related_to
  target_object_id: PAT_share_a_representation_until_a_write_forces_a_copy
- rel: related_to
  target_object_id: PAT_declare_single_argument_constructors_explicit
reference:
  source_title: 'More Effective C++: 35 New Ways to Improve Your Programs and Designs'
  author: Scott Meyers
confidence: high
references: []
variants: []
---

# Interpose a Proxy When an Operator Cannot See Its Own Context

## Pattern Rule
**IF** an operator has to behave differently according to something it cannot observe from inside itself — whether its result will be read or assigned to, which of several dimensions is being indexed, whether a conversion was meant
**THEN** hand back an object that stands for the result rather than the result, and let whatever happens to that object next supply the information the operator lacked
**ELSE** where the distinction is visible from the arguments or from the constness of the object being operated on, draw it there; this earns its place only when the deciding information genuinely arrives after the operator has returned.

## Do
- Build the design around the three things that can happen to the interposed object, because that trichotomy is the whole mechanism: it gets created, naming what it stands for; it gets assigned to, which means the underlying thing is being written; or it gets used some other way, which means the underlying thing is being read.
- For a read-versus-write distinction, put the write behavior in the assignment operators and the read behavior in the conversion back to the underlying type. Constness cannot make this distinction — overload resolution consults only whether the object operated on is const, never the context the call appears in, so both a read and a write through a non-const object select the same overload.
- Return a const stand-in from the const overload. Since its assignment operator is not a const member, that alone makes assigning through it fail to compile, which is exactly the behavior the const path owes its callers.
- Overload address-of on the stand-in if clients ever take addresses, and remember that the non-const version has to end sharing on the underlying value, because you cannot know how long the client will hold the pointer or what they will do with it.

## Don't
- Don't expect the stand-in to substitute for the real type. It will not, in at least five ways worth checking before you commit: taking its address yields a pointer of the wrong type unless you overload that; compound assignment and increment do not work unless you write every one of them on the stand-in; member functions of the underlying type are not callable through it unless you replicate them; it cannot bind to a reference-to-non-const parameter, so functions that modify their arguments reject it; and because a conversion sequence permits only one user-defined step, calls that compiled with the real type can fail with the stand-in.
- Don't overlook that these objects are temporaries, so each one is constructed and destroyed. Where the point was to avoid needless work, that cost has to be smaller than what the distinction saves, which it usually is but not always.
- Don't introduce one into a class whose clients depend on the operations in the first item. The technique changes the semantics of the class subtly rather than extending it, and the changes surface at call sites far from where the decision was made.

## Checklist
- What information does the operator need that is not available until after it returns?
- Do the assignment operators and the conversion cover the write and read cases respectively?
- Does the const overload yield something that cannot be assigned to?
- Which of address-of, compound assignment, increment, member calls, and binding to a non-const reference do clients actually use here?
- Would a caller be able to tell they are not holding the real type?

## Notes
The construct is worth recognizing by name — proxy, or surrogate — because it turns up in three unrelated-looking places that are the same move: standing in for a dimension the language does not offer, standing in for an element whose access mode is not yet known, and standing in for a conversion so that reaching the target type would need two user-defined steps rather than one.

The first of those has since lost its motivation for new code. Subscripting can now take more than one argument, so a class representing a multidimensional array can define the operator directly rather than returning something whose own subscript completes the job. The other two motivations are untouched.

The canonical library instance is the specialization of the standard growable array for bool, whose subscript yields a stand-in rather than a reference to a bool — and it is equally the canonical cautionary tale, because generic code written against the general template misbehaves on it in precisely the ways listed above. That is the strongest available argument for the limitations being a design consequence rather than an implementation detail.

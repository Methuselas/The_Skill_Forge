---
object_id: PAT_give_the_compiler_a_local_it_can_prove_is_unaliased
object_type: pattern
name: Give the Compiler a Local It Can Prove Is Unaliased
library_path:
- software-engineering
- languages
- cpp
- optimization
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- optimization
- aliasing
- const_correctness
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_optimize_for_what_the_compiler_can_prove
- rel: related_to
  target_object_id: PAT_prefer_pass_by_reference_to_const
- rel: related_to
  target_object_id: PAT_apply_const_to_lock_invariants
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Give the Compiler a Local It Can Prove Is Unaliased

## Pattern Rule
**IF** hot code reads a value through a reference or pointer parameter more than once, or across a call the compiler cannot see into
**THEN** copy it once into a local constant and use that, so the compiler has a value nothing outside the function can name and therefore nothing can change
**ELSE** where the value is genuinely expected to change during the operation — that is what the indirection is for — the reload is required work and the copy would be wrong.

## Do
- Recognize the two situations that produce it. Several pointer or reference parameters may refer to the same object, so a write through one forces a reread through the others. And a reference parameter can be bound to something a called function reaches independently, so any opaque call invalidates what was read through it.
- Notice how a by-reference parameter arrives where you did not intend one. Template code that avoids copying declares parameters as reference-to-const for an arbitrary type; instantiate it with a small type and you have a `const bool&` parameter with all of the aliasing consequences and none of the copying savings.
- Make the local `const`. It costs nothing, the syntax rules enforce it whether or not the optimizer has budget to prove it, and it prevents you from reintroducing the mutation the copy was meant to rule out.
- Extend it to whole arrays where the compiler supports it. Two array parameters that might overlap prevent even simple transformations — a loop writing two buffers one byte at a time cannot become two block fills — and the C keyword asserting that a pointer is the only route to its data is widely available in C++ compilers under one spelling or another, though not in the standard.
- Confirm the effect in the generated code rather than assuming it. The aliasing case shows up plainly: two loads before the change, one after.
- Convert the parameter rather than copying it when the type is unknown. A template parameter of unknown type should not be copied wholesale, but the property you need from it usually can be — converting to `bool` once, into a local, gives a stable value without assuming anything about the type's cost.

## Don't
- Don't skip the local because "the compiler will optimize the variable away." It generally will remove the storage, and it keeps the fact that the value cannot change, which is the part you were adding.
- Don't expect a helpful name or a comment to establish non-aliasing. The compiler compiles the function for all callers, including one that passes the same object twice.
- Don't apply it outside measured hot code. Each of these is a small transformation with a small readability cost, and doing it everywhere buys nothing while making the code noisier.
- Don't assume the non-standard aliasing keyword means the same thing everywhere. The spellings differ across compilers and so do the details of what is promised, so a build that relies on it needs the assumption stated somewhere a reader will find it.
- Don't expect `const` on a *parameter* to buy what it buys on a local. A function receiving a reference-to-const may legally cast the const away and modify the object, so the compiler cannot assume the value survives the call — which is precisely why the local copy is the fix rather than adding const to the parameter. The guarantee attaches to an object *declared* const at its creation, because casting const away from one of those is undefined and the compiler may assume it does not happen.

## Checklist
- Does this fragment read the same indirect value more than once?
- Is there an opaque function call between the reads?
- Could two of these parameters legally refer to the same object?
- Is the local declared const?
- Does the generated code show fewer loads after the change?

## Notes
Aliasing is the compiler's obligation to assume the worst about names. Two references of the same type are, as far as the language is concerned, possibly two names for one object, and a function that increments through one and then reads through the other has to perform the read. Every fix for this works the same way: introduce a name that nothing outside the function possesses, so the possibility does not arise.

This runs directly against the common advice that temporary variables are clutter the compiler will remove anyway. Both halves of that advice are true and the conclusion does not follow — the storage goes away, the guarantee stays, and the guarantee is what was being bought.

There is a second reason to prefer `const` here that has nothing to do with intent. Constness is checked during compilation, unconditionally, so the optimizer may rely on it without spending any analysis budget. A fact that the compiler would have had to derive is a fact it may run out of time to derive; a fact the type system already enforced is free.

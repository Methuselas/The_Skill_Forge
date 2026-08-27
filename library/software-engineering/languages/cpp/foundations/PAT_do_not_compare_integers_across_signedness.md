---
object_id: PAT_do_not_compare_integers_across_signedness
object_type: pattern
name: Do Not Compare Integers Across Signedness
library_path:
- software-engineering
- languages
- cpp
- foundations
stage_binding: 3 rough
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- integers
- conversions
- correctness
cross_links:
- rel: related_to
  target_object_id: PAT_choose_index_types_the_compiler_can_assume_do_not_wrap
- rel: related_to
  target_object_id: PAT_prefer_the_form_that_refuses_what_you_did_not_mean
- rel: related_to
  target_object_id: PAT_choose_the_weakest_ordering_operation_that_does_the_job
reference:
  source_title: 'C++20 STL Cookbook: Leverage the latest features of the STL to solve real-world problems'
  author: Bill Weinman
confidence: high
references: []
variants: []
---

# Do Not Compare Integers Across Signedness

## Pattern Rule
**IF** you are comparing two integers whose types differ in signedness
**THEN** make the comparison one the language will not quietly reinterpret — use the standard integer comparison functions, or remove the mixture by choosing a single type for the quantity — because the usual conversions turn the signed operand into a large positive one and the comparison then answers a different question than the one you asked
**ELSE** where both operands already have the same signedness, compare them directly; the hazard is the mixture, not the comparison.

## Do
- Learn the shape rather than the instance. Any comparison with a signed operand on one side and an unsigned one on the other is the shape, and the most common instance is a signed loop index tested against a container's size, which is unsigned.
- Reach for the standard integer comparison functions where the mixture is unavoidable. They test the signedness of both operands first and only convert when the conversion cannot change the answer, which is precisely the reasoning you would otherwise have to write by hand at every site.
- Prefer removing the mixture at its source where you control both types. One type for one quantity is a smaller and more durable fix than a correct comparison between two types that should not have differed.
- Know what the conversion actually does, because the magnitude is what makes the bug hard to believe. A small negative number does not become a small positive one — a signed value of negative three becomes, in thirty-two unsigned bits, something over four billion. The comparison is then not merely wrong but wrong in the opposite direction from the intuition that led you to write it.
- Treat compiler warnings as a bonus rather than the mechanism. Some compilers warn here and many do not, and the ones that do will warn in the places you were already looking.

## Don't
- Don't cast one operand to silence a diagnostic. The cast does not fix the comparison; it performs the same reinterpretation the compiler was about to perform, with the difference that you have now signed your name to it and suppressed the warning that would have told the next reader.
- Don't expect the mistake to announce itself. The behaviour is fully defined, so nothing traps, nothing is diagnosed at runtime, and a sanitizer has nothing to report — the program simply takes the wrong branch.
- Don't assume the comparison is safe because both values are small. The conversion is decided by the declared types, not by the values, and it happens identically whether the signed operand held negative three or three.

## Checklist
- Does this comparison mix a signed operand with an unsigned one?
- If so, can the mixture be removed by choosing one type for the quantity?
- If it cannot, is the comparison going through a function that handles signedness rather than through a bare operator?
- Is any cast here fixing the comparison, or merely silencing the report of it?

## Notes
This belongs in the small family of defects that survive review because the code reads as obviously correct. Nothing about a comparison between a negative number and a positive one looks like it needs thought, and the reasoning required to see the problem is about declared types rather than about values, so reading the line does not prompt it.

What makes it worth a rule rather than a caution is that the failure is silent in every channel a programmer normally relies on. It is not undefined behaviour, so the tools built to catch undefined behaviour do not apply. It is not a warning on most configurations. It produces no wrong-looking value at the point of the mistake — only a branch not taken, somewhere downstream, in a program that continues confidently.

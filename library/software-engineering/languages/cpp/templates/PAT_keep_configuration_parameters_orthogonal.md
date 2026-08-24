---
object_id: PAT_keep_configuration_parameters_orthogonal
object_type: pattern
name: Keep Configuration Parameters Orthogonal
library_path:
- software-engineering
- languages
- cpp
- templates
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- templates
- policy_based_design
- coupling
- class_design
cross_links:
- rel: related_to
  target_object_id: PAT_lift_each_varying_design_decision_to_a_parameter
- rel: related_to
  target_object_id: PAT_watch_for_semantic_coupling
- rel: related_to
  target_object_id: PAT_match_new_and_delete_forms
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Keep Configuration Parameters Orthogonal

## Pattern Rule
**IF** you have a candidate set of template parameters for a configurable class and are deciding whether the split is the right one
**THEN** check whether any two of them need to know about each other, and treat a pair that does as a decomposition that has not been finished.
**ELSE** where the coupling is genuinely irreducible, pick one direction, make the dependency explicit as a compile-time value the other reads, and accept the encapsulation you lose.

## Do
- Take each pair in turn and ask whether one can change without the other being told. Independence is the property being tested, not similarity of subject.
- Look for the tell: a parameter that has to expose a constant, a flag, or a type purely so a different parameter can read it.
- When the coupling is real, pass the dependency as a template argument to the dependent parameter's own member template, so the interface between them stays compile-time and typed.
- Prefer re-cutting the split over plumbing between the pieces. Two coupled parameters are often one decision that was divided along the wrong line.

## Don't
- Don't take "these two are about different subjects" as proof they are independent. Arrays and destruction are different subjects and are still coupled, because the thing that decides whether a pointer refers to many objects also decides which release form is legal.
- Don't leave the coupling implicit and rely on clients to pair the parameters correctly. A combination that compiles and is wrong is the outcome the whole approach exists to prevent.
- Don't accept a chain of dependencies. One irreducible pair is a known cost; three that all read each other means the split is wrong, not that the problem is hard.

## Checklist
- For every pair, can I change one and leave the other untouched?
- Does any parameter expose something no client would use, that exists only for another parameter to read?
- If two must interact, is the direction stated in one place, and is what they exchange checked during compilation?
- Would a client combining two of these in a way I did not anticipate get a compile error rather than wrong behavior?

## Notes
The failure this catches is quiet, because a coupled split still compiles and still looks decomposed. What it costs is the property that made the split worth making: independent parameters give a product of valid behaviors, whereas coupled ones give a smaller set with invalid combinations hidden inside it, and the compiler cannot tell you which is which.

The classic instance is a parameter that says whether a smart pointer refers to one object or many, sitting beside a separate parameter that performs the release. The first has to reach the second, because one object and many objects need different release forms, and getting it wrong is undefined rather than merely incorrect. Either the two become one decision, or the first must publish a compile-time answer the second reads.

Coupling here also costs type safety in a way ordinary coupling does not. Two classes that know about each other are merely hard to change; two parameters that know about each other let a client assemble a combination that satisfies every syntactic requirement and violates an invariant nobody wrote down.

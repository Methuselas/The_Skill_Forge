---
object_id: AP_choose_the_relationship_between_two_types
object_type: ap
name: Choose the Relationship Between Two Types
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 0 design
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- inheritance
- composition
- is_a
- class_design
cross_links:
- rel: supports
  target_object_id: PAT_use_public_inheritance_only_for_is_a
- rel: supports
  target_object_id: PAT_model_has_a_with_composition
- rel: supports
  target_object_id: PAT_use_private_inheritance_judiciously
- rel: supports
  target_object_id: PAT_use_multiple_inheritance_judiciously
- rel: supports
  target_object_id: PAT_make_non_leaf_classes_abstract
- rel: supports
  target_object_id: PAT_unhide_inherited_names_with_using
- rel: supports
  target_object_id: PAT_design_a_class_as_type
- rel: related_to
  target_object_id: AP_design_a_customization_point
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted C++ sources
confidence: high
references: []
variants: []
---

# Choose the Relationship Between Two Types

## Objective
Decide how one type should be connected to another — public inheritance, composition, private inheritance, or multiple bases — and arrive at a link that survives the substitutability test rather than one chosen because the base happened to have members the derived type wanted. Success is a relationship you can state in a sentence, and that no future caller can break by using the derived type where the base was promised.

## Steps / Flow

1. **State the relationship in words before writing any syntax.** Is-a, has-a, or is-implemented-in-terms-of. The wrong link almost always begins as a correct observation that two types share code, which is not one of the three.

2. *Gate.* **Apply the substitutability test to any proposed is-a.** `PAT_use_public_inheritance_only_for_is_a` owns it: everything true of the base must be true of the derived type, for every caller, without exception. One counterexample — the classic being a shape that cannot honor an arbitrary resize — disqualifies the link no matter how much code it would have shared.

3. **Branch — has-a or is-implemented-in-terms-of takes composition.** `PAT_model_has_a_with_composition` owns both, and covers the distinction between the application-domain relationship and the implementation-domain one.

4. **Branch — reach for private inheritance only where composition genuinely cannot do the job.** `PAT_use_private_inheritance_judiciously` owns the narrow cases that justify it. This is a later branch than composition rather than a parallel option, and treating the two as equivalent is what produces hierarchies nobody can explain.

5. *Gate.* **If more than one base is proposed, price it separately.** `PAT_use_multiple_inheritance_judiciously` owns the costs, and the test is whether the same design is reachable with one base plus composition. Where it is, take that.

6. **Make every class that is not a leaf abstract.** `PAT_make_non_leaf_classes_abstract` owns the reason, which is the copying and slicing behavior a concrete-from-concrete derivation produces rather than a stylistic preference. This may mean introducing a new abstract base above both existing types.

7. *Recovery.* **Where a derived class reuses a name the base overloads, restore the hidden ones.** `PAT_unhide_inherited_names_with_using` owns the fix. This surfaces as callers losing overloads that used to work, and reads as a compiler defect until it is recognized.

8. **Re-read the derived type as its own type.** `PAT_design_a_class_as_type` owns the wider set of questions this raises, and the relationship chosen above should not have answered them by default.

9. **Completion check.** The link matches the relationship stated in step 1; substitutability holds for every caller, not merely for the current ones; no concrete class derives publicly from another concrete class; and no overload has silently disappeared from the derived interface.

## Notes
The branch order is the content. Composition before private inheritance, one base before several, and the substitutability test before any of them — a set of these rules delivered unordered lets the reader pick the mechanism first and rationalize the relationship afterwards, which is the direction the mistake actually runs.

Step 6 frequently produces a design change rather than a keyword change, and that is the point. Discovering that two concrete types both want to be the other's base usually means the shared thing is a third type that has not been written yet.

Step 7 is included because it is a consequence of the design rather than an independent decision, and because it appears as a client-side breakage that gives no hint of its cause.

---
object_id: AP_make_a_class_immutable
object_type: ap
name: Make a Class Deeply Immutable While Keeping It Usable
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- immutability
- hard_to_misuse
- builder_pattern
- refactoring
cross_links:
- rel: supports
  target_object_id: PAT_prefer_immutable_objects
- rel: supports
  target_object_id: PAT_keep_immutable_with_builder_or_copy_on_write
- rel: supports
  target_object_id: PAT_make_immutability_deep
- rel: supports
  target_object_id: PAT_verify_an_object_is_as_immutable_as_you_think
- rel: supports
  target_object_id: PAT_dont_mutate_input_parameters
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Make a Class Deeply Immutable While Keeping It Usable

## Objective
Take a class that is mutable or only shallowly immutable and make it deeply immutable, without losing the ability to specify optional values or obtain modified copies.

## Steps / Flow
1. **Remove setters and freeze members.** Delete setter functions, set every member in the constructor, and mark each member final (const/readonly) so nothing reassigns them after construction. `PAT_prefer_immutable_objects` owns whether immutability is the right answer here at all.
2. **Restore flexibility with a pattern, not mutation.** If some construction values are optional, add a builder that takes required values in its constructor and optional ones via chained setters, returning the immutable object from `build()`. If callers need a tweaked instance, add copy-on-write `with`-style functions that return a new object with one value changed. `PAT_keep_immutable_with_builder_or_copy_on_write` owns which pattern to reach for.
3. **Close the deep-mutability holes.** For any member of a mutable type, stop outside references from reaching it: defensively copy the object in the constructor and in its getter, or — preferably — hold it in an immutable data structure so no copy is needed and even in-class code cannot mutate it. `PAT_make_immutability_deep` owns the depth requirement, and `PAT_dont_mutate_input_parameters` owns the constructor's side of it.
4. **Check for hidden mutation paths.** Confirm no getter returns a live reference to mutable internal state, no member is reassigned inside the class, and constructing or copying the object cannot leave a caller holding a reference that mutates it. `PAT_verify_an_object_is_as_immutable_as_you_think` owns the check.
5. **Weigh the cost where it matters.** On hot paths or large structures, prefer immutable data structures over repeated defensive copies, and use the language's compiler support (such as C++ const correctness) where available.

## Notes
This threads the chapter's immutability sections into one refactor of `TextOptions`: strip the setters and mark members final; add a builder for the optional font size or copy-on-write `withFontSize` for modified copies; then defend the font-family list against the two shared-reference scenarios, ideally with an immutable list. The order matters — shallow immutability first, flexibility second, depth third — because a class can look immutable while a shared mutable member quietly betrays it. The payoff is a tamper-proof object that can be passed anywhere without fear of misuse.

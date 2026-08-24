---
object_id: PAT_order_type_dispatch_most_derived_first
object_type: pattern
name: Order Type Dispatch Most-Derived First
library_path:
- software-engineering
- languages
- cpp
- inheritance
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- inheritance
- dispatch
- exception_handling
- ordering
cross_links:
- rel: related_to
  target_object_id: PAT_use_public_inheritance_only_for_is_a
- rel: related_to
  target_object_id: PAT_redesign_away_from_multiple_dispatch
- rel: related_to
  target_object_id: PAT_catch_exceptions_by_reference_and_rethrow_bare
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Order Type Dispatch Most-Derived First

## Pattern Rule
**IF** you select a handler by scanning candidates in order and taking the first whose type accepts the object — exception handlers, a registered handler table, a chain of type tests
**THEN** order the candidates so that every type precedes its own bases, because a base accepts anything derived from it and will answer for a case a later, more specific candidate was written to handle.
**ELSE** where the order cannot be controlled, make the candidates mutually unrelated so that no two of them can both accept the same object.

## Do
- Sort by the derivation relation rather than by any order the source happened to arrive in — alphabetical, declaration order, and registration order are all unrelated to which candidate is more specific.
- Keep unrelated candidates in whatever order they came. Only the pairs standing in a base-derived relation constrain each other, so a sort needs to move nothing else.
- Where candidates are registered at runtime, sort at registration and keep the invariant, rather than sorting at every dispatch.
- Put the catch-all last where one exists at all, and treat it as the answer for cases nobody anticipated rather than the common path.

## Don't
- Don't rely on the compiler to warn you. Ordering a base before its derived class is a legal arrangement in which one clause is unreachable, and unreachability across types is not something a compiler is obliged to notice.
- Don't test the arrangement only with the specific types. A scan ordered wrongly still produces an answer for every input, so a test that asserts something happened passes; the assertion has to name which candidate ran.
- Don't add a new candidate to the end of an existing list by habit. Appending a derived type after its base is exactly the arrangement that makes it dead, and appending is the natural way to add one.
- Don't reach for a scan when a virtual call would do. Dispatching on one type is the language's job, and a hand-written scan over candidates is worth writing only where a virtual function genuinely cannot express the selection.

## Checklist
- For every pair of candidates in a base-derived relation, does the derived one come first?
- Is the ordering re-established when a candidate is added, or only when the list was first written?
- Does a test exist that fails when two candidates are swapped?
- Would a virtual function have selected this without a scan at all?

## Notes
The rule generalizes past any single mechanism, because it follows from what public derivation means rather than from a language feature. A derived object genuinely is an instance of its base, so any test admitting the base admits it too; ordering base before derived therefore does not merely risk shadowing the specific candidate, it guarantees the specific candidate never runs.

Exception handling is where this is most familiar, and where the consequence is most visible: a handler for a base exception type placed above one for a derived type takes every throw of the derived type as well. The same arrangement in a hand-written dispatch table produces the same result with no diagnostic at all, which is the case worth being careful about.

The failure is silent in the way that matters — the scan finds a candidate, the candidate handles the object, and the program continues doing something defensible but less specific than intended. Nothing is thrown, nothing crashes, and the more specific handler simply never appears in any trace, so the symptom shows up as behavior that seems too generic rather than as an error anyone can locate.

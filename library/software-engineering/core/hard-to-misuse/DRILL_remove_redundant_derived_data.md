---
object_id: DRILL_remove_redundant_derived_data
object_type: drill
name: Remove a Redundant Second Source of Truth From a Data Model
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
- single_source_of_truth
- derived_data
- refactoring
- hard_to_misuse
cross_links:
- rel: teaches
  target_object_id: PAT_single_source_of_truth_for_data
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: eliminating stored derived data so a data model cannot hold an inconsistent state
references: []
variants: []
---

# Remove a Redundant Second Source of Truth From a Data Model

## Practice Task
Take a class that stores both primary data and a value derived from it, show it can be built in an inconsistent state, and refactor so the derived value is computed instead.

## Target Skill
Separating primary from derived data and removing stored derived values that create a second source of truth.

## Setup
No special setup required.

## Instructions
1. Start from a class that takes and stores primary values and a derived one — an account taking credit, debit, and balance.
2. Construct an instance in an inconsistent state (balance as debit minus credit) and confirm it compiles and stores contradictory data.
3. Identify which fields are primary (credit, debit) and which are derived (balance).
4. Remove the derived field from the constructor and members, and compute it on demand in the getter (credit minus debit).
5. Confirm an inconsistent instance can no longer be constructed, and, if you want to practice the expensive case, replace the primary values with a transaction list and add lazy caching under immutability.

## Success Check
- The inconsistent instance is actually constructed and its contradictory state recorded before any change. That it compiles is the defect; describing it is what the class's comment was already doing.
- Primary and derived fields are separated with the derivation written as an expression, so the claim that one follows from the others is checkable rather than asserted.
- Constructing an inconsistent instance is attempted afterwards and shown impossible, with the compiler's rejection recorded.
- The cost is stated — recomputation on every read — and where that is unacceptable the cache is guarded by immutability so it cannot disagree with the primary data. A cache added without that guard reintroduces precisely the defect just removed.
- Any other place in the class holding a second representation of the same fact is named, since one derived field is rarely the only one.

## Common Failures
- Keeping the derived field but "validating" it in the constructor, which is weaker than making the bad state unrepresentable.
- Caching a derived value in a mutable class without resetting the cache on mutation.

## Notes
This drills Long's `UserAccount` example, where storing balance alongside credit and debit lets an off-by-sign caller ship wrong statements. Deriving on demand makes the inconsistent state impossible; the lazy-cache extension shows why the single-source-of-truth and immutability rules reinforce each other when derivation is costly.

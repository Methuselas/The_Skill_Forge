---
object_id: PAT_single_source_of_truth_for_data
object_type: pattern
name: Keep a Single Source of Truth for Data
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
- single_source_of_truth
- derived_data
- hard_to_misuse
- caching
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_immutable_objects
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u07, pp. 199-202
  evidence_type: text
confidence: high
references: []
variants: []
---

# Keep a Single Source of Truth for Data

## Pattern Rule
**IF** a data model contains derived data that can be calculated from primary data
**THEN** store only the primary data and compute the derived value on demand, so there is one source of truth and no way to construct a logically inconsistent state.

## Do
- Distinguish primary from derived data: credit and debit are primary and fully describe an account, while balance is derived (credit minus debit), so store credit and debit and calculate balance in the getter.
- Remove the redundant field entirely from the constructor and members, closing the door on a caller passing a balance that contradicts the credit and debit.
- If deriving is expensive, cache lazily — compute on first access and store the result — but only when the class and its inputs are immutable, so the cache can never disagree with the primary data.

## Don't
- Don't accept a derived value as a constructor parameter alongside its inputs; a caller who computes balance as debit-minus-credit instead of credit-minus-debit builds an invalid account that compiles fine.
- Don't cache derived values in a mutable class without resetting the cache on every mutation; that fiddly, error-prone bookkeeping is itself a strong argument for immutability.

## Checklist
- Is any stored field fully derivable from other stored fields?
- Can a caller supply a derived value that contradicts the primary data?
- If a derived value is cached, are the class and its inputs immutable so the cache stays valid?

## Notes
Redundant derived data creates two sources of truth that can disagree, and Long's `UserAccount` shows the cost: taking balance as a parameter lets an off-by-sign caller ship wrong statements. Deriving balance on the fly makes an inconsistent state unrepresentable. The expensive-derivation case — a balance computed from a transaction list — is where lazy caching earns its place, but only under immutability, which is why this pattern leans on the immutable-object rule to keep its cache honest.

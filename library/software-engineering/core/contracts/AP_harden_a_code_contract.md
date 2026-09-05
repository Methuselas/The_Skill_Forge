---
object_id: AP_harden_a_code_contract
object_type: ap
name: Harden a Code Contract From Small Print to Enforcement
library_path:
- software-engineering
- core
- contracts
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_contracts
- hard_to_misuse
- checks
- refactoring
cross_links:
- rel: supports
  target_object_id: PAT_prefer_unmistakable_over_small_print
- rel: supports
  target_object_id: PAT_make_misuse_impossible_by_removing_invalid_states
- rel: supports
  target_object_id: PAT_make_the_caller_state_the_ambiguous_choice
- rel: supports
  target_object_id: PAT_enforce_contracts_at_runtime_with_checks
- rel: supports
  target_object_id: PAT_define_your_code_contract_explicitly
- rel: supports
  target_object_id: PAT_convey_usage_through_names_and_types
- rel: supports
  target_object_id: PAT_make_breakage_fail_compile_or_test
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Harden a Code Contract From Small Print to Enforcement

## Objective
Take a piece of code whose contract leans on small print and move each term to the strongest available enforcement, so misuse becomes impossible where it can and loudly detectable where it cannot.

## Steps / Flow
1. **Surface the contract.** Write out the preconditions, postconditions, and invariants the code actually imposes, including the ones currently hidden in comments or implied by a required call order. Surfacing it is `PAT_define_your_code_contract_explicitly`.
2. **Label each term by channel.** Mark each as unmistakable (name, parameter type, return type, checked exception) or small print (comment, external doc, unchecked exception), and note which small-print terms cause silent bugs if ignored. `PAT_prefer_unmistakable_over_small_print` ranks the channels, and `PAT_convey_usage_through_names_and_types` owns what the signature can carry on its own.
3. **Eliminate invalid states first.** For each small-print term that guards against a bad state, try to make that state unrepresentable — a static factory returning only valid instances, a private constructor, private mutators, no exposed mutable state — so the misuse cannot compile. `PAT_make_misuse_impossible_by_removing_invalid_states` owns the elimination, and `PAT_make_breakage_fail_compile_or_test` decides how early the failure lands. Where a term is ambiguous rather than violable — the call could mean two things and one of them is wrong — `PAT_make_the_caller_state_the_ambiguous_choice` owns making the caller write which, so the wrong reading stops being expressible.
4. **Enforce the irreducible remainder with loud checks.** For terms that cannot be made compile-time impossible, add precondition and postcondition checks that throw an obvious, unmissable failure when violated. The check itself is `PAT_enforce_contracts_at_runtime_with_checks`.
5. **Consider assertions for the dev/test tier.** Where a check would be too costly in production or availability outweighs catching the breach in the wild, use assertions that fire in development and testing, understanding they are normally compiled out of release.
6. **Document only what is left, and re-read.** Write clear documentation for any genuinely unavoidable small print, then re-read the contract to confirm the must-know terms now live in unmistakable channels and nothing critical rides on a comment alone.

## Notes
This generalizes the `UserSettings` progression: from a class with loads of small print (ordered `loadSettings()`/`init()`, overloaded null) to one made impossible to misuse via a factory and private setup, with checks and assertions shown as the runtime fallbacks. The ordering is the point — prefer compile-time impossibility, fall back to loud runtime checks, use assertions where the tradeoff fits, and document last. Step 3's immutability techniques and step 4's fail-fast behavior have their own owners; here they combine into a single hardening pass applied when a contract relies too heavily on callers reading the small print.

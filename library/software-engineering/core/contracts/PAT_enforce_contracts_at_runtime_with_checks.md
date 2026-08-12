---
object_id: PAT_enforce_contracts_at_runtime_with_checks
object_type: pattern
name: Enforce Contracts at Runtime With Loud Checks
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
- checks
- assertions
- fail_fast
- runtime_enforcement
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_unmistakable_over_small_print
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u03, pp. 63-66
  evidence_type: text
confidence: high
references: []
variants:
- variant_id: VAR_assertions
  variant_name: Enforce With Assertions That May Compile Out
  variant_basis: constraint
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  locator: u03, pp. 65-66
  difference_from_foundation: Uses built-in assertions instead of hand-written checks; assertions are typically compiled out of release builds, so the loud failure fires in development and testing but not in the wild unless assertions are explicitly left enabled.
  when_to_use: When the contract check is expensive enough to matter for performance, or when availability in production matters more than catching the breach at runtime, or when the language's assertion syntax is cleaner and the team keeps assertions on in release.
  when_not_to_use: When the breach must be caught in production too; a compiled-out assertion gives no protection in the wild, so prefer an always-on check there.
  absorbed_from_object_id: none
---

# Enforce Contracts at Runtime With Loud Checks

## Pattern Rule
**IF** a contract term cannot be enforced by the compiler yet still must hold
**THEN** add a runtime check that tests the condition and, if it is violated, throws an error that causes an obvious, unmissable failure rather than letting the program limp on in a bad state.

## Do
- Place the check where the condition matters: a precondition check on inputs or required setup at the top of a function, a postcondition check on the result or resulting state before returning.
- Make the failure loud and specific, the way `init()` throws a `StateException("Settings not loaded")` when called out of order, so misuse surfaces in development or testing.
- Look up the language's idiom — some have built-in check support with nicer syntax, others need a manual throw or a third-party library.

## Don't
- Don't treat a runtime check as equal to compile-time impossibility; it only fires if a test or a user actually exercises the broken path, and an obscure untested scenario can still slip to production.
- Don't let a thrown exception get swallowed and merely logged at a higher level where no one reads the logs — a loud failure no one notices is no protection.
- Don't paper over a design smell: if you are adding lots of checks, that is a sign to eliminate the small print instead.

## Checklist
- Does each check throw a failure loud enough that it cannot be silently ignored?
- Is the check a precondition (before) or postcondition (after), and placed accordingly?
- Are you adding so many checks that the real fix is removing the invalid states?

## Notes
Checks are the runtime fallback when compile-time enforcement is not feasible: in the scooter analogy, a firmware failsafe that shuts the motor at 30 mph — better than a fine, worse than a speed restrictor that made the situation impossible. Long pairs checks with fuzz testing, which relies on thrown errors to surface bugs, so checks raise what fuzzing can find. The absorbed variant (VAR_assertions) covers assertions: conceptually identical enforcement, but normally compiled out of release for performance or availability, which trades production protection for those gains unless the team keeps them enabled. Both share the rule — enforce small print when you must, but prefer to avoid the small print in the first place.

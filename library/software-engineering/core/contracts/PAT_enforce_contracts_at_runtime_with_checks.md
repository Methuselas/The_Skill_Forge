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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_assertions
  variant_name: Enforce With Assertions That May Compile Out
  variant_basis: constraint
  difference_from_foundation: Uses built-in assertions instead of hand-written checks; assertions are typically compiled out of release builds, so the loud failure fires in development and testing but not in the wild unless assertions are explicitly left enabled.
  when_to_use: When the contract check is expensive enough to matter for performance, or when availability in production matters more than catching the breach at runtime, or when the language's assertion syntax is cleaner and the team keeps assertions on in release.
  when_not_to_use: When the breach must be caught in production too; a compiled-out assertion gives no protection in the wild, so prefer an always-on check there.
  absorbed_from_object_id: none
- variant_id: VAR_split_never_happens_from_expected_before_choosing_the_check
  variant_name: Split Never-Happens From Expected Before Choosing the Check
  variant_basis: method_sequence
  difference_from_foundation: The foundation adds a loud runtime check for any contract term the compiler cannot enforce, and VAR_assertions decides whether to use an assertion on grounds of cost and production availability. This variant selects on a different basis entirely - what the condition means. A condition that should never occur is a statement about the code and belongs in an assertion, because it checks for bugs and its corrective action is to change the source, recompile and release. A condition you expect to occur, however rarely, is a statement about the data and belongs in shipped error-handling code that responds gracefully. McConnell frames assertions as executable documentation - you cannot rely on them to make the code work, but they record assumptions more actively than comments, covering things like a parameter within range, a stream open or at its start, a pointer non-null, a container with capacity, or a fast routine's result matching a slow clear one.
  when_to_use: Use before writing any unenforceable check, since the classification decides the mechanism, whether it ships, and what a reader does when it fires. It becomes near-mechanical once a validation boundary exists - code outside the boundary uses error handling because no assumption about the data is safe, code inside uses assertions because a bad value there is a defect rather than dirty input.
  when_not_to_use: Do not put executable code inside an assertion; if assertions compile out of production then so does that code, so assign the result to a status variable and test that instead. Do not use an assertion where the condition is genuinely reachable from bad input, because it will be compiled away exactly when it was needed.
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

`VAR_split_never_happens_from_expected_before_choosing_the_check` selects between the same two mechanisms as `VAR_assertions` on an entirely different basis, and the pair is worth reading together. Long's variant chooses an assertion when the check is expensive or when production availability matters more than catching the breach — a cost decision. McConnell's chooses by what the condition means: a condition that cannot occur unless the code is wrong is a statement about the code and belongs in an assertion, while a condition that is unlikely but anticipated is a statement about the data and belongs in error handling that ships. Getting that backwards fails in both directions — an assertion guarding a genuinely reachable bad input disappears from the build where it was needed, and error-handling machinery wrapped around a condition that can only mean a bug quietly absorbs the evidence of it. The trap to avoid is putting executable code inside an assertion, since compiling assertions out then removes the action too. Where a validation boundary has been drawn, this classification stops being a judgment call and follows from which side of the boundary the code sits on.

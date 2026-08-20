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
- variant_id: VAR_separate_validator
  variant_name: Ship the Check as a Separate Validation Pass
  variant_basis: constraint
  difference_from_foundation: The precondition is documented rather than enforced in
    the operation, and the check is provided as a separate tool or an optional mode
    the caller runs when they want it, instead of running on every call.
  when_to_use: Validating the input costs as much as, or more than, doing the work —
    which happens when confirming validity requires the same search the computation
    performs. Callers who supply valid input then pay nothing, and callers who are
    unsure have a way to find out.
  when_not_to_use: The check is cheap relative to the operation, or a breach is
    dangerous rather than merely wrong. A documented precondition nobody validates
    is only acceptable where the consequence of violating it is a wrong answer the
    caller asked for.
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
- Classify the condition before you choose the check. A condition that should never occur is a statement about the *code*, so it belongs in an assertion whose corrective action is to change the source and release. A condition you expect to occur, however rarely, is a statement about the *data*, so it belongs in shipped error handling that responds gracefully.

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

Two questions decide the mechanism and they are worth keeping apart. `VAR_assertions` answers a cost question — use an assertion when the check is expensive or when production availability matters more than catching the breach. The Do item above answers a meaning question, and it comes first: a condition that cannot occur unless the code is wrong is a statement about the code and belongs in an assertion, while a condition that is unlikely but anticipated is a statement about the data and belongs in error handling that ships. Getting that backwards fails in both directions — an assertion guarding a genuinely reachable bad input disappears from the build exactly where it was needed, and error-handling machinery wrapped around a condition that can only mean a bug quietly absorbs the evidence of it. The trap to avoid is putting executable code inside an assertion, since compiling assertions out then removes the action too; assign the result to a status variable and test that instead. Where a validation boundary has been drawn the classification stops being a judgment call and follows from which side of it the code sits on — outside, no assumption about the data is safe, so error handling; inside, a bad value is a defect rather than dirty input, so an assertion.

Whether a never-happens check should *ship* is genuinely contested, and the case against compiling assertions out is stronger than the convention suggests. The convention rests on two assumptions, both weak. It assumes testing found the bugs — but any complex program is exercised over a minuscule fraction of the permutations production will put it through. And it assumes production resembles the test environment, when production is the more hostile of the two: memory exhausts, disks fill, cables get chewed, and none of that happens during a test run. Shipping without the checks that were catching your mistakes is crossing the high wire without the net on the grounds that you managed it in practice. Where an assertion genuinely costs too much — a sortedness check that adds a whole pass over the data — disable *that* assertion rather than the category.

The other way an assertion can betray you is by having a side effect. A check that advances an iterator, consumes a stream, or mutates a counter changes the run it was supposed to observe, so the program behaves differently with checking on than off — and the version you tested is not the version you shipped. Read the condition as something that must be free to be evaluated any number of times, or not at all.

McConnell's framing of assertions as executable documentation is what makes them worth the effort beyond the check itself. They record assumptions more actively than a comment does — a parameter within range, a stream open or at its start, a pointer non-null, a container with capacity, a fast routine's result matching a slow clear one — while never being something the working code may rely on.

There is a third position between checking every call and leaving a precondition implicit, and
it is the right one when validation is genuinely expensive. The variant `VAR_separate_validator`
documents the precondition, does not enforce it in the operation, and ships the check as
something the caller can run when they choose. The case that forces it is where confirming
the input is valid costs as much as using it: a routine that stops searching as soon as it has
what it needs cannot also prove that nothing else was there, and being made to prove it can
double the run time. Users who supply correct input — usually most of them — would be paying
that permanently to catch a mistake they do not make.

Two obligations come with taking that route. The contract must be written down precisely
enough that a caller can tell whether they satisfy it, including exactly which inputs leave the
behaviour unspecified. And any breach that *is* cheap to detect should still be caught, since a
broader contract is worth more than a narrow one and the argument here is only about the
checks that are expensive. Offering the validator as a tool rather than only publishing the
rules is what makes the arrangement fair to the caller who cannot tell which side of the line
they are on.

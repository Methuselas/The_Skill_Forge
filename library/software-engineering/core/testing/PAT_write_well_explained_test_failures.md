---
object_id: PAT_write_well_explained_test_failures
object_type: pattern
name: Make Test Failures and Test Code Self-Explaining
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- unit_testing
- test_naming
- failure_messages
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_keep_tests_agnostic_to_implementation
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u10, pp. 271-273
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make Test Failures and Test Code Self-Explaining

## Pattern Rule
**IF** you are writing a test case
**THEN** name it for the specific behavior it locks in and make its assertions produce a clear failure message, so a failure tells even an unfamiliar engineer exactly what broke.

## Do
- Name the case for the behavior, not the function: `testGetEvents_inChronologicalOrder` tells a reader what broke where a bare `testGetEvents` does not.
- Test one behavior per case, so a failure pinpoints the broken behavior by which small case failed rather than burying it in one big case.
- Make assertions report meaningfully — showing that contents match but order differs beats an opaque dump of object identities.

## Don't
- Don't write one large test case that exercises everything; when it fails, no one can tell which behavior broke.
- Don't lean on heavy shared setup that makes a case hard to understand; an engineer changing one behavior must be able to tell which tests they are affecting and why.

## Checklist
- Does each test case name state the exact behavior it verifies?
- Does a failure message explain what is wrong, not just that something is?
- Can an engineer read a case and know what it tests and how, well enough to use it as an instruction manual?

## Notes
A test's audience is often an engineer who just broke code they have never seen, so a failure must explain itself. Long's paired failure messages show the gap — an unreadable object-identity dump versus a clear "order differs" report — and the fix is descriptive per-behavior naming plus one behavior per case. Understandable tests double as an instruction manual for the code; the chapter-11 practices of testing one behavior at a time and limiting shared setup are the concrete techniques that keep them so.

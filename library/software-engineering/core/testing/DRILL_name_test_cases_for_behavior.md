---
object_id: DRILL_name_test_cases_for_behavior
object_type: drill
name: Split and Name Test Cases for the Behavior They Lock In
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
- refactoring
cross_links:
- rel: teaches
  target_object_id: PAT_write_well_explained_test_failures
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: splitting a catch-all test into focused, behavior-named cases with clear failure messages
references: []
variants: []
---

# Split and Name Test Cases for the Behavior They Lock In

## Practice Task
Take one large test case that checks several behaviors and split it into focused cases named for each behavior, then confirm failures now pinpoint what broke.

## Target Skill
Writing focused test cases whose names and assertions make a failure self-explaining.

## Setup
No special setup required.

## Instructions
1. Start from a single catch-all test case that exercises multiple behaviors under one vague name.
2. List the distinct behaviors it covers, phrasing each as a claim that could be false.
3. Split it into one case per behavior, each named for the specific behavior it locks in (such as a suffix describing the expected property).
4. Read the names alone and predict what each one locks in, without opening the bodies.
5. Improve each assertion so a failure message states what is wrong — for an ordering behavior, report that contents match but order differs rather than dumping raw values.
6. Deliberately break one behavior, run the suite, and record which case failed and the message it produced.
7. Check the opposite failure: names long enough to restate the assertion, which help nobody reading a list of failures.

## Success Check
- The behaviours are listed before the split, each phrased as a claim that could be false. A list of the things the old case happens to touch reproduces the old case under new headings.
- There is one case per behaviour, and each name states the behaviour rather than the function under test — checked by reading the names alone and predicting what each one locks in.
- One behaviour is actually broken and the suite run, with exactly one case failing and its name recorded. Two failures means a behaviour is still spread across cases and the split is unfinished.
- The failure message is recorded and describes what differs — contents matching but order differing, rather than two dumped values. The message is the deliverable here, not the split.
- The opposite failure is checked: names long enough to restate the assertion. A name that repeats the body of its case helps nobody reading a list of failures.

## Common Failures
- Splitting the cases but leaving generic names that do not identify the behavior.
- Keeping opaque assertions whose failure output does not explain the discrepancy.

## Notes
This drills Long's `testGetEvents` versus `testGetEvents_inChronologicalOrder` contrast. The reflex is one behavior per named case with a meaningful assertion, so that the person who broke the code — often unfamiliar with it — learns from the failure exactly what went wrong.

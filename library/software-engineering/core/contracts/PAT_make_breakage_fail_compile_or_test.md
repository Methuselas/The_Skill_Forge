---
object_id: PAT_make_breakage_fail_compile_or_test
object_type: pattern
name: Make Breakage Fail at Compile Time or Fail a Test
library_path:
- software-engineering
- core
- contracts
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- error_prevention
- testing
- type_safety
- robustness
cross_links: []
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u03, pp. 52-53
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make Breakage Fail at Compile Time or Fail a Test

## Pattern Rule
**IF** you want another engineer's change to be unable to silently break or misuse your code
**THEN** structure your code so that breaking it makes something concrete happen — either the code stops compiling or a test starts failing — because those are the only two signals reliable enough to block a bad change before it reaches the main codebase.

## Do
- Design assuming the reliable gate: engineers submit from a local copy, and a change that does not compile or that fails tests is stopped at submit time, so aim every safety mechanism at triggering one of those two.
- Prefer moving guarantees into the type system where a violation cannot compile, and back that with tests for the guarantees types cannot express.

## Don't
- Don't depend on other engineers noticing a problem by reading, remembering, or being careful; your code sits on constantly shifting foundations they will inadvertently disturb.
- Don't count a mechanism as protection if a broken caller can still compile and pass tests — that is a silent failure waiting to reach production.

## Checklist
- If someone misuses this code, does it fail to compile or fail a test?
- Are the guarantees that types cannot enforce covered by tests instead?
- Could a breaking change slip through both gates unnoticed?

## Notes
Long frames a busy codebase like a busy place — fragile things get broken by footfall — and identifies the two, and only two, reliable ways to catch breakage at submit time: a compile failure or a test failure. He notes that a great deal of what "high-quality code" means reduces to ensuring one of those two things happens when the code is broken. This is the enforcement backbone behind the contract, small-print, checks, and assertions material in the rest of the chapter.

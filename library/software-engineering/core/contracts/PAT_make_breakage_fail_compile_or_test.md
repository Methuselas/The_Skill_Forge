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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_convert_semantic_interface_terms_into_programmatic_ones
  variant_name: Convert Semantic Interface Terms Into Programmatic Ones
  variant_basis: method_sequence
  difference_from_foundation: The foundation structures code so that breaking it stops a compile or fails a test. This variant supplies the audit that finds what to structure - split the interface into its programmatic part, meaning the types and attributes a compiler can enforce, and its semantic part, meaning the assumptions about use that it cannot. Requirements such as calling one routine before another, or a member that must be initialized or the call crashes, are semantic, and McConnell is blunt about what that means - any aspect of an interface the compiler cannot enforce is an aspect likely to be misused. Document the semantic part, then work to move items out of it, with assertions as the fallback where the type system cannot reach.
  when_to_use: Use when reviewing an interface you own, especially one carrying call-order or initialization prerequisites. Listing the semantic terms explicitly is what makes them candidates for conversion rather than permanent small print.
  when_not_to_use: Do not treat documenting a semantic term as discharging it, since the foundation's point is that documentation is not a signal that blocks a bad change. Do not convert a term into an assertion when the type system could carry it, because a compile error beats a runtime one.
  absorbed_from_object_id: none
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

`VAR_convert_semantic_interface_terms_into_programmatic_ones` supplies the audit step this foundation assumes. Every interface has two halves: the programmatic one the compiler checks, and the semantic one it cannot - call this before that, initialize this or it crashes, this parameter is read only when that flag is set. McConnell's rule for the second half is that anything the compiler cannot enforce is likely to be misused, which reframes it from documented behaviour into a list of pending defects. The move is to enumerate those terms and convert what can be converted, using types where possible and assertions where not. The direction of preference matters: keeping something in the type system beats an assertion, because an assertion fires at runtime on a machine that has already run the wrong code.

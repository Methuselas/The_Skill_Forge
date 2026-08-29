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
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_unmistakable_over_small_print
- rel: related_to
  target_object_id: AP_harden_a_code_contract
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
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
- Make a compile-time failure name the requirement that was violated, not the trick that detected it. A check that reports a broken internal construct leaves the reader debugging your mechanism; one carrying the requirement's own words tells them what to change. Where the diagnostic is not yours to write, choose the names appearing in it so that the message reads as an explanation.
- Audit an interface by splitting it in two before you decide what to strengthen: the programmatic part the compiler enforces, and the semantic part it cannot — call this before that, initialize this or the call crashes, this parameter is read only when that flag is set. Write the semantic terms down as a list, then convert what can be converted, reaching for types first and assertions only where the type system cannot follow.

## Don't
- Don't depend on other engineers noticing a problem by reading, remembering, or being careful; your code sits on constantly shifting foundations they will inadvertently disturb.
- Don't count a mechanism as protection if a broken caller can still compile and pass tests — that is a silent failure waiting to reach production.

## Checklist
- If someone misuses this code, does it fail to compile or fail a test?
- Are the guarantees that types cannot enforce covered by tests instead?
- Could a breaking change slip through both gates unnoticed?

## Notes
Long frames a busy codebase like a busy place — fragile things get broken by footfall — and identifies the two, and only two, reliable ways to catch breakage at submit time: a compile failure or a test failure. He notes that a great deal of what "high-quality code" means reduces to ensuring one of those two things happens when the code is broken. This is the enforcement backbone behind the contract, small-print, checks, and assertions material in the rest of the chapter.

The audit in the Do list is what tells you where to aim, and its value comes from McConnell's blunt rule for the semantic half: any aspect of an interface the compiler cannot enforce is an aspect likely to be misused. That reframes the semantic terms from documented behaviour into a list of pending defects, which is the reason for writing them out rather than leaving them implied. Two cautions travel with it. Documenting a semantic term does not discharge it — documentation is not a signal that blocks a bad change, which is the whole premise of this card. And do not settle for an assertion where the type system could carry the term, because an assertion fires at runtime on a machine that has already run the wrong code, whereas a compile error stops it before it exists. The same programmatic/semantic cut appears from the other direction in [PAT_prefer_unmistakable_over_small_print](PAT_prefer_unmistakable_over_small_print.md), which decides where to *put* a term; this decides what to do with the ones already stranded in the weak channel.

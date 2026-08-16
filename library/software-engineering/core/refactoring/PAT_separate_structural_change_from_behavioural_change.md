---
object_id: PAT_separate_structural_change_from_behavioural_change
object_type: pattern
name: Change Structure or Change Behaviour, Never Both in One Pass
library_path:
- software-engineering
- core
- refactoring
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- refactoring
- maintenance
- code_quality
- discipline
cross_links:
- rel: related_to
  target_object_id: PAT_refactor_for_your_own_comprehension
- rel: related_to
  target_object_id: PAT_concentrate_effort_where_defects_concentrate
- rel: prerequisite_for
  target_object_id: AP_refactor_working_code_safely
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Change Structure or Change Behaviour, Never Both in One Pass

## Pattern Rule
**IF** you are about to modify code that already works
**THEN** decide first whether the change is meant to preserve observable behaviour or to alter it, and do only one of the two before stopping to verify
**ELSE** where the code does not currently work, you are debugging or building rather than refactoring — name it that way, because the techniques that make each safe are different.

## Do
- Hold the definition rather than the word. A refactoring is a change to internal structure that makes code easier to understand and cheaper to modify **without changing observable behaviour**. If callers can tell the difference, it is not a refactoring, whatever it is being called.
- Check the precondition before you start: refactoring applies to code that works. Tweaking broken code in the hope of stumbling onto a version that runs is hacking, and calling it refactoring conceals the fact that nobody has yet explained the failure.
- Refuse the mixed pass. Restructure, then verify, then change behaviour — because when a test fails after a pass that did both, it cannot tell you which half caused it, and that is precisely the information you were verifying to get.
- Read the size of the session as a signal. Finding yourself midway through a *major* refactoring is the point to ask whether this section wants redesigning and reimplementing from the ground up instead, since at that scale a rewrite is frequently the cheaper route.
- Never write half a feature intending to refactor it into completeness later. That plan requires the incomplete version to be working code, which it is not.

## Don't
- Don't let the term dilute into "any change to the code." Used as a synonym for fixing defects, adding functionality, or reworking a design, it stops carrying the one constraint that made it a safety technique.
- Don't use the word to make an unplanned change sound disciplined. The discipline is the behaviour-preservation constraint, not the vocabulary.
- Don't treat "the tests still pass" as proof that behaviour was preserved when the pass also added functionality — the new behaviour had no test before you started.

## Checklist
- Can any caller observe a difference after this change?
- Did the code work before you began?
- If something fails after this pass, will you know whether structure or behaviour caused it?
- Is the scale of this session telling you to rewrite rather than restructure?

## Notes
Martin Fowler's definition is the load-bearing sentence — a change made to the internal structure of the software to make it easier to understand and cheaper to modify without changing its observable behaviour. The word grew out of Larry Constantine's "factoring" in structured programming, which meant decomposing a program into its constituent parts as far as possible. Neither sense covers making a program work.

The reason the boundary is worth defending is that it is the only thing making the activity safe. A change that preserves behaviour can be verified against the behaviour that already existed: the old tests are the specification, and they were written before you had any stake in the new structure. Once a pass also alters behaviour, that reference disappears, and a failure afterwards is ambiguous between a restructuring mistake and an intended change working as designed. Everything else in refactoring practice — small steps, one at a time, retesting between — depends on that verification being unambiguous, so the definition is not pedantry about a word but the precondition for the whole method.

Two abuses follow from letting it slip. The first is code-and-fix wearing a better name: a programmer who cannot say why the code failed makes changes until it appears to work, and describes the session as refactoring. The second is refactoring used as an excuse not to rewrite, where successive restructurings keep a section alive that should have been replaced. Kent Beck's formulation of the second is blunt — a big refactoring is a recipe for disaster — and the practical test is the one above: the size of the session you find yourself in is the evidence.

---
object_id: PAT_refactor_for_your_own_comprehension
object_type: pattern
name: Refactor Temporarily for Your Own Comprehension
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- cognitive_load
- refactoring
- code_comprehension
cross_links:
- rel: related_to
  target_object_id: PAT_separate_intrinsic_from_extraneous_load
- rel: related_to
  target_object_id: PAT_replace_unfamiliar_constructs_with_basic_equivalents
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u04, pp. 51-52
  evidence_type: text
confidence: high
references: []
variants: []
---

# Refactor Temporarily for Your Own Comprehension

## Pattern Rule
**IF** you must understand unfamiliar code and its current shape is what is defeating you
**THEN** transform it for your own readability right now on a throwaway branch, accepting that the result may be worse code, and roll it back once you understand
**ELSE** you will keep re-reading a structure that was never arranged for you

## Do
- Separate the goal from ordinary refactoring: the usual aim is long-term maintainability, this one's aim is one reader's comprehension at one moment, and the two frequently disagree.
- Inline a method whose name tells you nothing — `calculate()`, `transform()` — so its body sits at the call site instead of costing you a jump and a held question. Most IDEs will do it for you.
- Move a definition next to its first call. Jump-to-definition works, but operating it also consumes working memory.
- Do the work on a local "understanding" branch. Version control makes this cheap, and anything that turns out to be a genuine improvement can be merged on its own merits.
- Roll it back by default. If you are the only person on the team unfamiliar with the construct you replaced, the code should go back the way it was.

## Don't
- Don't refuse the move because it lowers maintainability. Inlining is a reverse refactoring by design; delocalized code can be more maintainable *and* harder on your working memory at the same time, because you must scroll or search to follow it.
- Don't leave the changes in place silently and call it cleanup. They were made for one reader, and that reader was you.
- Don't reach for this before checking what kind of load you are facing — restructuring cannot touch difficulty that is inherent to the problem.

## Checklist
- Are these changes on a branch you are willing to throw away?
- Can you name the specific reading obstacle each change removes, or are you tidying?
- Once you understand the code, does anything you changed survive on its own merits rather than because you happen to have written it?
- Would the team read the reverted version as unchanged?

## Notes
Hermans's term is cognitive refactoring: a change that preserves external behaviour, like any refactoring, but is aimed at making code readable for the current reader at the current point in time rather than maintainable in the long run.

The idea that this is allowed is the part that meets resistance. Refactoring toward a *less* maintainable state feels like vandalism, and inlining a well-factored method looks like undoing someone's work. The reframe is that readable is not a property of code alone; it is a relation between code and a reader, so a temporary local rearrangement is closer to adjusting your chair than to damaging the building. Another benefit falls out of it: once the inlined body sits in context, a better name for the method often becomes obvious.

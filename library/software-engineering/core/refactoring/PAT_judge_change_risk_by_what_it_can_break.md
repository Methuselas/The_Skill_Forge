---
object_id: PAT_judge_change_risk_by_what_it_can_break
object_type: pattern
name: Judge a Change's Risk by What It Can Break, Not by How Big It Is
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
- maintenance
- review
- risk
- defects
cross_links:
- rel: related_to
  target_object_id: PAT_concentrate_effort_where_defects_concentrate
- rel: related_to
  target_object_id: PAT_review_to_detect_not_to_correct
- rel: prerequisite_for
  target_object_id: AP_refactor_working_code_safely
- rel: related_to
  target_object_id: AP_replace_a_system_that_is_still_in_use
- rel: related_to
  target_object_id: AP_review_code_you_did_not_write
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Judge a Change's Risk by What It Can Break, Not by How Big It Is

## Pattern Rule
**IF** you are deciding how much care a change to working code deserves — a desk-check, a review, a retest, a second pair of eyes
**THEN** scale that care to what the change can reach, not to how many lines it touches
**ELSE** a one-line edit gets whatever rigour its blast radius earns, which is routinely more than a forty-line mechanical rename earns.

## Do
- Discard diff size as the risk signal. Measured error rates climb from one-line changes to a peak at around five lines and fall away after that — small changes are not the safe ones, and the smallest are among the most dangerous.
- Start from the base rate: programmers have better than a fifty percent chance of making an error on a first attempt at a change. Plan on being wrong the first time rather than being surprised by it.
- Treat a simple change as if it were complicated. One organisation that introduced reviews for one-line changes moved its error rate from 55 percent to 2 percent; a telecommunications organisation went from 86 percent correct to 99.6 percent.
- Classify by reach instead. Replacing a literal with a named constant is close to risk-free. A change to a class or routine interface, to a database schema, or to a boolean test can break callers that never appear in the diff, and those deserve the full treatment — one at a time, with a reviewer or a pair.
- Spend the recovered effort where it counts. Batch the mechanical low-reach changes and simply retest them; do not buy that economy by also streamlining the ones that can reach outside the file.

## Don't
- Don't skip the desk-check because the diff is one line. Treating small changes casually — not reviewing them, sometimes not even running them — is the specific habit the measurements condemn.
- Don't invert the finding into "make larger changes." The curve describes how carefully people treat changes of a given size, not a property that makes big edits safe.
- Don't file a mechanical transformation and an interface change under the same rigour because they touch the same number of lines. Line count is the axis that carries no information here.
- Don't count the compiler and the unit tests as the whole answer on a risky change. They check what they were written to check, and an interface change moves the ground under both.
- Don't downgrade a change's risk because it is a *named* transformation. That a rewrite has a standard name and a published recipe says nothing about whether this application of it preserved behaviour — textbook examples of canonical control-flow rewrites have themselves shipped wrong, and a reader who recognised the pattern is exactly the reader who stopped checking.

## Checklist
- What can this change reach that is not visible in the diff?
- Is the rigour you have chosen a response to the change's reach, or to its size?
- For a one-line change: has anyone other than you looked at it?
- Which category is this — mechanical and local, or interface, schema, or conditional logic?

## Notes
The curve behind this is the counterintuitive part and it is worth stating precisely, because a loose reading of it is wrong. Chance of error is already substantial for a one-line change, rises to a maximum at about five lines, and declines from there out to twenty. It is not that big changes are safe; it is that people bring more care to a change that looks like it needs care, and the effect of that care swamps the effect of the size. The moral McConnell draws is the operative one: treat simple changes as if they were complicated.

Reach is the axis that actually predicts damage, and it is only loosely related to size. A single character in a boolean test can invert a condition that every caller depends on. A schema change can break code in another system that nobody in the room maintains. Against that, a rename applied by a tool across forty call sites is verified by the compiler at every one of them. Sorting changes this way also makes the economics work — the streamlining you can safely do on the mechanical category is what pays for the extra review on the category that needs it, so the two halves of the rule fund each other rather than competing.

This composes with concentrating effort where defects concentrate rather than duplicating it. That pattern allocates attention across a *codebase* by defect history and complexity; this one allocates attention across *changes* by what each one can reach. A change to a low-risk line inside an error-prone module still deserves the module's scrutiny, and a change to a boolean test in a clean module still deserves this one's.

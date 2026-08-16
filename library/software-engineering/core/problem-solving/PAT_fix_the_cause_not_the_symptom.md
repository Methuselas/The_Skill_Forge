---
object_id: PAT_fix_the_cause_not_the_symptom
object_type: pattern
name: Fix the Cause, Not the Symptom
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- debugging
- defects
- corrections
- maintainability
cross_links:
- rel: related_to
  target_object_id: AP_find_a_defect_by_hypothesis_not_by_guessing
- rel: related_to
  target_object_id: PAT_invest_in_quality_over_hacky_shortcut
- rel: related_to
  target_object_id: PAT_concentrate_effort_where_defects_concentrate
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Fix the Cause, Not the Symptom

## Pattern Rule
**IF** you have located a defect and are about to correct it
**THEN** change the code that produces the wrong behaviour, and make the change only because you understand why it is right — not because it makes the symptom disappear.
**ELSE** where the cause genuinely lies outside what you may change, contain the symptom deliberately at a named boundary and record why, rather than patching it where it happened to surface.

## Do
- Make each change only when you expect it to work. Being wrong about a correction should be surprising enough to prompt a rethink — if you are routinely surprised, you are altering code you do not understand, and each alteration lowers your confidence in the rest of it.
- Change one thing at a time. Two simultaneous changes can introduce a new defect that resembles the original, leaving you unable to tell whether you failed to fix it, fixed it and added a lookalike, or neither.
- Keep the version you started from. When several changes are in flight it stops being obvious which one mattered, and a comparison against the original recovers that in seconds.
- Rule out the competing explanations before acting, not just confirm the favoured one. Having shown the symptom *could* result from one of several causes is not grounds to start work on one of them.
- Re-run the cases that reproduced the defect and the cases that did not, then run everything else. A correction that resolves the observed case and breaks a neighbour is the common outcome, which is what an automated suite is for.
- Add a test that would have caught this. The defect got past the existing tests once; without a new case it can return by the same route.
- Slow down when the pressure is highest. Rushing produces incomplete diagnosis, unverified corrections, and the assumption that a change worked because you wanted it to — and it happens most reliably right before a deadline, which is exactly when it costs most.

## Don't
- Don't special-case the observed value. Adding a correction for the one account whose total came out wrong by a specific amount does not fix anything: if the underlying fault is an initialization problem the discrepancy is unpredictable by definition, so tomorrow it is a different number and the special case is now wrong in a second way.
- Don't let special cases accumulate. Each one is added beside the last, none is ever removed, and eventually the exceptions rather than the logic become the most prominent feature of the code.
- Don't change code randomly to see what happens. Adjusting an index by one and then by minus one until the output looks right teaches you nothing and leaves you less able to say whether the code is correct than before you started.
- Don't use the program to do what a person should. A calculation patched to produce the right total for known inputs has stopped being a calculation.

## Checklist
- Can you say why this change fixes the defect, in one sentence, without referring to the symptom?
- Have the competing explanations been ruled out, or only the chosen one confirmed?
- Is this one change, or several?
- Do the reproducing cases now pass, and does everything else still pass?
- Is there now a test that would have caught this?
- Would this correction still be right if the observed wrong value had been different?

## Notes
The number that justifies the whole discipline is that defect corrections have been found wrong more than half the time on the first attempt. That reframes the correction from a trivial epilogue into the second most error-prone act in the sequence — and it is performed under time pressure, on code the author has just proven they misunderstood, usually while relieved to have found the thing at all.

The special-case anti-pattern is worth recognizing by shape rather than by principle, because it always arrives dressed as pragmatism. Its signature is a correction keyed to a specific observed value — this account, this amount, this input — appended after the logic rather than inside it. Three separate things are wrong with it, and only one is about tidiness. It usually does not work, because the class of fault that produces an oddly specific wrong value is typically the unpredictable kind. It does not stay small, because the next one gets appended beside it. And it moves work the machine was doing into a table of exceptions a human now has to maintain.

The confidence standard is the most portable idea here. Setting the expectation that a correction should work, and that being wrong is a genuine surprise, converts debugging from a search into a claim you are making about the program. Someone who is routinely surprised by their own fixes has learned something important about how well they understand the code, and the appropriate response is to go back to diagnosing rather than to try the next change.

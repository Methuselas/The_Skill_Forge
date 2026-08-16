---
object_id: PAT_verify_code_assumptions_with_tests_and_pairing
object_type: pattern
name: Pin Down an Assumption About a Codebase With a Test or Another Person
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- misconceptions
- testing
- documentation
- code_comprehension
cross_links:
- rel: related_to
  target_object_id: PAT_recognize_a_misconception_by_its_three_marks
- rel: related_to
  target_object_id: PAT_beware_assumptions_avoid_or_enforce
- rel: related_to
  target_object_id: PAT_comment_why_not_what
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Pin Down an Assumption About a Codebase With a Test or Another Person

## Pattern Rule
**IF** you are relying on an assumption about a codebase that you have not checked
**THEN** convert it into something external — a test that runs, or another person's stated expectation — because your own confidence is exactly the signal that cannot be trusted here.

## Do
- Write the assumption as a test when it is expressible as one. If you are certain a value can never drop below zero, add the test that says so; it catches the case where you are wrong, and where you are right it records the fact for whoever reads the code next.
- Treat the test as documentation with a second job. The chapter's argument for this is specifically about durability — misconceptions rarely go away and can resurface even after the correct model is learned, so a check that survives in the codebase outlasts your having understood it.
- Program in a pair or a group when the assumptions are about intent rather than values. Exposing your assumptions to someone else's surfaces the conflict quickly, and the conflict is what reveals that one of you holds a misconception.
- Add documentation at the place you were misled, once you have found a misconception, so the next person meets the correction where the trap is rather than in a changelog.

## Don't
- Don't rely on seniority to protect you. Hermans is explicit that it is hardest for expert programmers to accept the error is theirs, which makes external verification more necessary with experience rather than less.
- Don't limit the suspicion to language semantics. Assumptions about a framework, a library, the domain, what a variable name means, or what another programmer intended are all misconception surfaces.
- Don't treat a passing manual check as equivalent to a recorded one; the value of the test is that it re-runs when the assumption is next violated, which a one-off inspection cannot do.

## Checklist
- Which belief am I acting on here that I have never actually run?
- Can this be stated as a test, and if not, who else can I state it to?
- If I turn out to be right, does anything in the codebase now record that?

## Notes
This closes the chapter's arc from personal misconception to codebase practice. The three routes Hermans names — pairing, tests, documentation — are ordered by what they catch: pairing catches conflicting intent, tests catch false claims about behavior, documentation prevents recurrence at the site.

The point that makes this worth a card rather than generic testing advice is the argument for *why* the test earns its place. It is not primarily about regression coverage; it is about a specific cognitive fact, that a corrected misconception remains retrievable and can return under load, so the assumption needs an external record that does not depend on your continuing to hold the right model.

It sits next to the reusability pattern on assumptions rather than overlapping it. That one concerns assumptions you bake into code you are writing, and the remedy is to remove or enforce and rename. This one concerns assumptions you hold about code you are reading, where the remedy is to externalize the belief before acting on it.

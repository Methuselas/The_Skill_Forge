---
object_id: PAT_use_a_misconception_checklist_when_learning_a_language
object_type: pattern
name: Work From a Misconception Checklist Instead of Waiting to Be Wrong
library_path:
- software-engineering
- core
- deliberate-practice
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- misconceptions
- transfer
- learning
- onboarding
cross_links:
- rel: related_to
  target_object_id: PAT_expect_negative_transfer_between_similar_languages
- rel: related_to
  target_object_id: PAT_recognize_a_misconception_by_its_three_marks
- rel: supports
  target_object_id: DRILL_compare_a_new_language_against_a_known_one
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Work From a Misconception Checklist Instead of Waiting to Be Wrong

## Pattern Rule
**IF** you are learning a new language or framework and cannot tell which of your assumptions are unsafe
**THEN** work from an external list of known misconceptions rather than your own sense of what needs checking, because the assumptions worth checking are by definition the ones that feel settled.

## Do
- Start from a catalogued list. Juha Sorva's 2012 dissertation contains 162 research-grounded misconceptions novices hold, and it is usable as a checklist against a language you are picking up — go through it and mark which ones could apply here.
- Add the pairwise question. Every pair of languages has its own interactions that generate misconceptions, far too many to enumerate, so ask someone who learned the same two languages in the same order as you. That ordering is the part that matters.
- Keep an open mind as the standing default: being sure you have something right is compatible with being wrong, and this is the one case where certainty carries no information.
- Write down your own misconceptions once you catch them. Your history is the most predictive list you will have for the languages you actually use.

## Don't
- Don't wait for the bug to teach you. The whole point of a checklist is that a misconception held with confidence produces no internal signal until something fails.
- Don't assume novice misconceptions are beneath you. Sorva's list is drawn from novices and the underlying mechanism — a reasonable inference from an adjacent domain — does not stop operating with experience; it just shifts to less elementary concepts.
- Don't expect the list to be complete for your situation. It covers general-language misconceptions and not the ones your specific codebase, framework, or team conventions will generate.

## Checklist
- Which items on a known-misconception list plausibly apply to the language I am learning?
- Who has learned this same pair of languages in this same order, and have I asked them?
- What have I recently been confidently wrong about, and is it on my own list yet?

## Notes
Three of Sorva's entries are worth carrying as calibration, because each is a *reasonable* inference rather than confusion. Misconception 15, that assignment stores equations or unresolved expressions, has `total = maximum + 12` linking the two variables so that changing `maximum` later changes `total` — sensible, since languages like Prolog do work that way to a degree, and common in people with mathematical backgrounds. Misconception 33, that a while loop terminates the instant its condition becomes false rather than at the next check, follows from the English word: "I will sit here and read my book while it is raining" does imply continuous monitoring. Misconception 46, that parameter passing requires different names in the call and the signature, comes from the earlier and correct rule that a variable name is used once, which stops holding at function boundaries.

Misconception 46 is the instructive one for experienced programmers, because it does not come from mathematics or English or another language — it transfers *within* a single language, from one concept to a neighbouring one. Understanding part of a language well does not guarantee that understanding carries to the rest of it.

Hermans is candid that there is not a lot to be done about misconceptions in general; negative transfer is inevitable when learning a new system. These three strategies — open mind, catalogued checklist, ask someone with the same learning path — are offered as what helps rather than as a cure.

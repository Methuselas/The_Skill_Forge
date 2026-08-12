---
object_id: PAT_dont_multitask_what_you_have_not_automatized
object_type: pattern
name: You Can Only Multitask What You Have Already Automatized
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- working_practice
- multitasking
- automatization
- cognitive_load
cross_links:
- rel: related_to
  target_object_id: PAT_match_practice_method_to_the_memory_type
- rel: related_to
  target_object_id: PAT_interrupt_at_task_boundaries
- rel: related_to
  target_object_id: DRILL_diagnose_which_automatization_phase_a_skill_is_in
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u11, pp. 189-190
  evidence_type: text
confidence: high
references: []
variants: []
---

# You Can Only Multitask What You Have Already Automatized

## Pattern Rule
**IF** you are considering doing two things at once
**THEN** check whether both have reached the autonomous phase, because that — not willpower or practice at multitasking — is what determines whether they can share your attention.

## Do
- Use the automatization phases as the test. You can knit while listening to a book because both are autonomous for you; you cannot hold a Slack conversation while reasoning about unfamiliar code because neither is.
- Trust the signal your brain already gives you. Turning the music down for a dense passage, or the radio down while parking, is the same mechanism reporting that capacity has run out — Hermans's framing is that this is your brain telling itself it cannot multitask.
- Treat the pairing as specific rather than general. The question is never whether you can multitask, it is whether *these two tasks* are both autonomous for *you* right now, which changes with the language and codebase you are in.
- Prefer sequencing when either task is still in the cognitive or associative phase.

## Don't
- Don't trust your own sense of how it went. In a controlled experiment where students worked while messaging a partner, the students rated their own performance as satisfactory and their partners rated it much lower. The self-assessment is the part that fails first.
- Don't equate equal comprehension with equal cost. Fox's study found students reading with instant messaging understood the text as well as the focused group — and needed about 50% more time to read it and answer questions.
- Don't measure by hours spent. Kirschner's study of around 200 students found heavy Facebook users studied just as long as non-users and had significantly lower grade averages, worst among those who replied to messages immediately.
- Don't accept "programming while on Slack" as normal practice on the grounds that it feels productive. The feeling of productivity is exactly what the evidence contradicts.

## Checklist
- Are both of these tasks genuinely autonomous for me, in this language and this codebase?
- Am I judging this arrangement by how it feels or by what it produces?
- Could these be sequenced instead, at the cost only of patience?

## Notes
The link to the automatization phases is the load-bearing part and it is what makes this a pattern rather than an exhortation. The rule as Hermans states it is that you cannot do two or more tasks at the same time when you have not reached the autonomous phase for them — which explains why the answer differs between people and between situations, and why it changes as a skill matures.

The three studies fail in three different ways, which is why all three are worth carrying. Fox's shows the cost as time rather than as accuracy, so a multitasker checking their comprehension finds nothing wrong. Kirschner's shows it as outcomes over a long period, invisible in any single session. Xu's shows the perception gap directly, with self-ratings and partner ratings diverging. Together they explain why the practice survives despite the evidence: every route by which you might notice the cost yourself is blocked.

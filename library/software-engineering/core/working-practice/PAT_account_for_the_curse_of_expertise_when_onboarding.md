---
object_id: PAT_account_for_the_curse_of_expertise_when_onboarding
object_type: pattern
name: Assume It Is Not Easy, Because You Cannot Remember It Being Hard
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
- onboarding
- teaching
- cognitive_load
- working_practice
cross_links:
- rel: prerequisite_for
  target_object_id: PAT_locate_a_learner_on_the_neo_piagetian_stages
- rel: related_to
  target_object_id: PAT_calibrate_code_reading_scope_to_reader_knowledge
- rel: related_to
  target_object_id: AP_prepare_an_onboarding_for_all_three_memory_systems
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u13, pp. 206-207
  evidence_type: text
confidence: high
references: []
variants: []
---

# Assume It Is Not Easy, Because You Cannot Remember It Being Hard

## Pattern Rule
**IF** you are about to describe a task to a newcomer as simple, small, or trivial
**THEN** treat that judgement as unreliable, because mastering a skill removes your memory of how hard it was to acquire and therefore inflates your estimate of what someone else can absorb at once.

## Do
- Catch the words. "Not that hard," "actually quite easy," "trivial" — Hermans's prompt is to notice how often those describe knowledge that took you a long time to acquire.
- Reattribute failure before blaming the person. Many situations where a new colleague is judged "not such a strong programmer" are curse-of-expertise situations where the newcomer is simply overloaded.
- Count what you are actually introducing at once. The failing pattern is a senior developer presenting the people, the domain, the workflow and the codebase together, then handing over a small bug or a tiny feature.
- Give the team a shared vocabulary for load, so the newcomer can report the real problem. "I experience too much load reading this code" and "I think I lack chunks for Python" are actionable in a way "I am confused" is not, and that requires teaching the concepts — memory types, cognitive load, chunks — to both sides.

## Don't
- Don't read a newcomer's failure as evidence about their ability. The predictable outcome of the overload pattern is a lead who concludes the newcomer is not very bright and a newcomer who concludes the project is very hard, and neither conclusion is supported.
- Don't assume the gap is speed. The tempting model is that novices reason as you do but slower or with a partial picture; the chapter's central claim is that they think and behave in genuinely different ways.
- Don't expect chunking to be shared. An expert glances at code and sees "emptying a queue"; a beginner reads it line by line. "Array index out of bounds" is one concept to you and three separate elements to them, and that difference is load, not intelligence.

## Checklist
- How many genuinely new things am I introducing before asking for output?
- Am I calling this easy because it is easy, or because I have forgotten learning it?
- Does this person have the vocabulary to tell me they are overloaded?

## Notes
The mechanism connects to germane load. A newcomer whose intrinsic and extraneous load already fill their capacity has none left for storing anything, so they can neither program effectively in the new codebase nor retain what they are being told. The session feels productive to the person talking and produces nothing durable for the person listening.

This is the pattern the rest of the onboarding material rests on, which is why the chapter puts it first and states the remedy so plainly: the first thing you can do to make onboarding easier is to realise that it is probably not all that easy for the person learning. Everything else — staging the activities, supporting the three memory systems, pitching explanations along a semantic wave — is a way of acting on that realisation rather than merely holding it.

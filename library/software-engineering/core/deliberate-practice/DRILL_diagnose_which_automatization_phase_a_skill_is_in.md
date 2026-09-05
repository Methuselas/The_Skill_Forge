---
object_id: DRILL_diagnose_which_automatization_phase_a_skill_is_in
object_type: drill
name: Sort Your Programming Skills Into the Three Automatization Phases
target_skill: Telling which of your routine programming skills still cost conscious attention, so practice goes where it pays
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
- deliberate_practice
- automatization
- cognitive_load
- self_assessment
cross_links:
- rel: supports
  target_object_id: PAT_match_practice_method_to_the_memory_type
- rel: supports
  target_object_id: DRILL_automatize_a_skill_by_writing_many_variants
- rel: related_to
  target_object_id: PAT_diagnose_weak_recall_as_storage_or_retrieval
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Sort Your Programming Skills Into the Three Automatization Phases

## Practice Task
During a normal programming session, list the small skills you are using and place each in the cognitive, associative, or autonomous phase.

## Target Skill
Telling which of your routine programming skills still cost conscious attention, so practice goes where it pays.

## Setup
An ordinary working session in a language you use, and a three-column table. This is observation during real work, not a quiz — the phases are only visible while you are actually doing the thing.

## Instructions
1. Work normally and note the small skills as they come up: writing a loop, indexing a list, a keyboard shortcut, a debugger action, a language construct you reach for.
2. Apply the three tests and record which test placed each entry. If you must give the task explicit attention in isolation, it is in the **cognitive** phase. If you can do it but are leaning on a trick or rule, it is **associative**. If you can perform it with ease while thinking about something else entirely, it is **autonomous**.
3. Write down the trick where you find one — "just always subtract one" is the signature of the associative phase, and naming it makes the phase unmistakable.
4. Repeat across different languages and projects. Expect unfamiliar languages and projects to show more semantic and cognitive-phase entries, and familiar ones to show more procedural and episodic.
5. Take everything left in the cognitive or associative columns as your practice list; these are the skills currently taxing capacity that the real problem needs.
6. Use the checking reflex as a cross-check. A task you feel no urge to go back and verify is genuinely automatized; one you re-read is still being reasoned through.

## Success Check
- At least one skill you assumed was automatic turns out to be associative once you notice the rule you are applying.
- Each entry is placed by a stated test, not by how confident you feel.
- Repeating the exercise in a less familiar language shifts the distribution, confirming the phases track the skill-in-context rather than you. This is the condition a single session cannot close. Predicting the shift is not observing it, and a run reporting that the distribution moved without having worked in the second context has put the prediction where the evidence goes.

## Common Failures
- Doing it from memory rather than during work. The distinction between associative and autonomous is invisible in retrospect, because the trick is fast enough to feel like fluency.
- Listing only large skills. The phases apply to the small ones, and the small ones are where the recoverable load is.
- Judging by outcome. Getting it right every time is compatible with the associative phase; what separates the phases is what you had to do to get it right.
- Treating a cognitive-phase entry as a failure. It is the normal first phase for anything new, and the point of the exercise is to find these, not to be embarrassed by them.

## Notes
A three-stage illustration shows the progression more sharply than prose does, using zero-based list indexing across three thought bubbles. In the cognitive phase the thought is a full sentence of reasoning — start at 0, so element 3 is the fourth one. In the associative phase it has collapsed to a rule — just always subtract 1. In the autonomous phase there is no verbal thought at all, only the list and `list[4]` with an arrow to the element. Verbal reasoning, then a rule, then direct perception.

The phases come with different costs and different exits. The cognitive phase is where schemata are formed or updated, and Hermans's example is that learning zero-based indexing had to modify a counting schema you already held from outside programming. The associative phase is where effective actions are kept and ineffective ones discarded, and harder tasks take longer to get through it. The autonomous phase is where the skill stops contributing to cognitive load at all, which is the entire practical point.

This drill supplies the input to the variant-writing drill; sorting the skills tells you what to practise, and that drill is how you move something out of the first two columns.

---
object_id: PAT_choose_explanatory_metaphors_by_audience_schemata
object_type: pattern
name: Choose an Explanatory Metaphor by What the Audience Already Knows
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 4 final
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
- teaching
- onboarding
- mental_model
- notional_machine
cross_links:
- rel: related_to
  target_object_id: PAT_check_whether_a_second_model_composes_or_conflicts
- rel: related_to
  target_object_id: PAT_calibrate_code_reading_scope_to_reader_knowledge
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants:
- variant_id: VAR_hermans_keywords_are_metaphors_you_did_not_choose
  variant_name: Treat Borrowed Keywords as Metaphors Nobody Chose
  variant_basis: context
  difference_from_foundation: The foundation governs a metaphor you select when explaining something, where the choice and its false inferences are yours to manage. This variant covers metaphors already installed by the language itself, since a keyword borrowed from English imports that word's everyday meaning whether or not it matches the semantics. The response differs accordingly — you cannot pick a better word, so the move is to predict the wrong inference the keyword invites and address it directly.
  when_to_use: Use when teaching or onboarding around constructs whose keywords read as ordinary English. Sorva's misconception 33 is the model case, where the natural reading of while implies continuous monitoring — a person saying they will read while it is raining is understood to check the weather repeatedly and leave when it stops, not to finish the book — so learners expect a loop to break the instant its condition turns false. Misconception 17 has the same shape, where a variable named minimum is assumed unable to hold a large value.
  when_not_to_use: Do not apply it to genuinely opaque or invented keywords, which carry no everyday meaning to mislead and are better handled as plain vocabulary. It is also the wrong frame for misconceptions arriving from another programming language rather than from natural language.
  absorbed_from_object_id: none
---

# Choose an Explanatory Metaphor by What the Audience Already Knows

## Pattern Rule
**IF** you are explaining a programming concept by comparing it to something in the real world
**THEN** pick the comparison from schemata this particular audience already holds, and check which false inferences the comparison licenses before you use it.

## Do
- Choose the everyday concept the listener has strong, well-practised associations with. A box works because putting things in, taking them out, and opening one to look inside are all familiar operations, so the comparison costs no extra cognitive load.
- Work out in advance what the metaphor implies that is not true, and say that part out loud rather than waiting for it to surface as a bug.
- Treat "what the audience knows" as local and current, not universal — Hermans's example is educators explaining a computer to children in rural India by using elephants as computers and their trainers as programmers, because that is the relationship those children already have.
- Prefer the metaphor whose residual misconception is the one you can most easily correct later.

## Don't
- Don't pick a comparison because it is accurate if the audience has no model of it. "A variable is like a monocycle" fails precisely because most people hold no schema for what operations a monocycle supports.
- Don't assume the easier metaphor is the better one. In the NEMO study the box group did better on single-assignment questions and were also the group likely to believe a variable could hold two values.
- Don't expect a superseded metaphor to disappear once you teach a better one; old models stay in long-term memory and resurface, so the cost of a careless first metaphor is paid over a long period.

## Checklist
- What operations does my audience already perform on the thing I am comparing to?
- What would someone wrongly conclude if they took this comparison literally?
- Is the misconception this metaphor invites one that shows up early and cheaply, or late and expensively?

## Notes
The evidence is a study Hermans's own group ran at the NEMO Science Museum in Amsterdam in 2017, with 496 participants who had no prior programming experience. All received an introductory Scratch lesson; half had a variable explained as a label, like a temperature or a person's age, and half as a box, like a piggy bank or a shoebox. The phrasing was held consistent within each condition — "x contains 5" for the box group against "x is 5" for the label group.

Both metaphors had measurable benefits and measurable costs, which is why this is a selection decision rather than a ranking. The box group performed better on simple single-assignment questions, plausibly because storage in a container is such a familiar operation. The box group was also the one prone to the misconception that a variable can hold two values at once — the exact false inference the container image licenses.

The general principle underneath sits in §6.5: notional machines work when they relate programming concepts to everyday concepts people have already formed strong schemata for. That is also why the warning generalizes beyond variables to any metaphor reached for during onboarding or code review.

`VAR_hermans_keywords_are_metaphors_you_did_not_choose` retains **Treat Borrowed Keywords as Metaphors Nobody Chose** for the case where the comparison was made by the language designer rather than by you. Chapter 7 shows the mechanism doing damage through `while`, whose English sense implies continuous monitoring — someone reading a book while it rains is understood to keep checking and to stop when the rain does — which is why learners expect a loop to exit the moment its condition turns false rather than at the next evaluation. The same shape produces the belief that a variable called `minimum` cannot hold a large value. Since the keyword cannot be swapped, the move shifts from selecting a metaphor to anticipating the inference it invites and contradicting it explicitly. It does not apply to invented or opaque keywords, which import no everyday meaning to mislead.

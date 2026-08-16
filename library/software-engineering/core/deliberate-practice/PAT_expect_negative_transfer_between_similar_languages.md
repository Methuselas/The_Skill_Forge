---
object_id: PAT_expect_negative_transfer_between_similar_languages
object_type: pattern
name: Expect Prior Knowledge to Mislead You Most Where Languages Are Similar
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
- transfer
- misconceptions
- learning
- defects
cross_links:
- rel: related_to
  target_object_id: PAT_set_up_for_transfer_when_learning_a_new_language
- rel: related_to
  target_object_id: PAT_recognize_a_misconception_by_its_three_marks
- rel: related_to
  target_object_id: PAT_guard_against_an_outdated_mental_model_under_load
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants:
- variant_id: VAR_hermans_negative_transfer_in_implicit_memory
  variant_name: Negative Transfer That Lives in Your Fingers, Not Your Knowledge
  variant_basis: context
  difference_from_foundation: The foundation concerns beliefs carried between languages, where the repair is to check the semantics you assumed. This variant covers the same interference operating in implicit memory, where there is no belief to correct — the knowledge is already right and the behaviour is still wrong. Correcting it therefore needs repetition rather than verification, because implicit memories are laid down by practice and cannot be edited by being told.
  when_to_use: Use when you keep producing the wrong form despite knowing the right one — typing curly brackets around Python blocks after years of Java or C#, or reaching for a keyword the new language does not have. Hermans's own case is the marker to recognise, still typing `foreach` instead of `for` years after moving from C# to Python, having drilled the syntax with flashcards.
  when_not_to_use: Do not apply it where you are genuinely unsure what the new language does, which is the foundation's case and wants checking rather than drilling. It also does not fit a one-off slip, since the defining feature here is a stable motor pattern that repeats.
  absorbed_from_object_id: none
---

# Expect Prior Knowledge to Mislead You Most Where Languages Are Similar

## Pattern Rule
**IF** you are writing a language that closely resembles one you already know well
**THEN** treat the resemblance as a source of confident errors rather than a shortcut, and check the specific places where the two languages' models diverge instead of the places where they obviously differ.

## Do
- Look hardest at features that exist in both languages and behave differently, since that is where a correct-feeling assumption goes unexamined. Java's checked exceptions are the chapter's case — they must be wrapped in try-catch to compile, they have no C# equivalent, and someone arriving from C# has no reason to suspect the gap.
- Treat conspicuous surface differences as the safe part. You will notice unfamiliar syntax; you will not notice a familiar construct with different semantics.
- Expect the hardest resistance where the paradigm shifts under a shared word. Functions exist in both object-oriented and functional languages and work differently, which is why experienced OO programmers struggle with a language like F#.
- Check your defaults about what the language guarantees. A Java programmer may assume Python also requires variables to be initialized and that the compiler will complain if they forget — a small error, but one that arrives with full confidence.

## Don't
- Don't treat a wrong assumption here as carelessness. Negative transfer is existing knowledge interfering with new learning, and it operates precisely because you have learned something well.
- Don't rely on being corrected by a compiler or a colleague. The defining problem is not just the wrong model but the certainty attached to it — as Hermans puts it, not only do they have the wrong mental model, but they think they have the right one.
- Don't conclude a language has damaged your thinking. Dijkstra's line about BASIC crippling the mind is quoted here precisely to be qualified: brains are not ruined by a language, though wrong assumptions carried between languages do cause real mistakes.

## Checklist
- Which constructs exist in both languages under the same name?
- For each, have I verified the semantics in the new language rather than assumed them?
- Is my confidence here grounded in this language's documentation or in the previous one's?

## Notes
Positive transfer is the ordinary case and is worth keeping in view: knowing Java means you already hold a model of a loop as a counter, a body, and a stop condition, so you know what to look for in almost any new language, and you build the new model on the old one instead of from scratch. Negative transfer is the same machinery running against you.

The severity ordering in the chapter is useful. Forgetting to initialize a variable or mishandling an exception are small and quickly fixed. Paradigm-level negative transfer runs deeper and takes much longer to clear, because what has to change is not a fact but the model the facts hang on — which is the conceptual-change problem developed in the companion pattern.

`VAR_hermans_negative_transfer_in_implicit_memory` retains **Negative Transfer That Lives in Your Fingers, Not Your Knowledge** for the case where nothing is wrong with what you know. Chapter 10 shows the same interference in procedural memory, where the corrective move is different because there is no belief to fix — learning Dvorak is harder for having learned Qwerty, and moving from C# or Java to Python produces curly brackets around blocks for a while. Hermans's own example is the sharp one: she still often types `foreach` instead of `for` years after the switch, and notes she had even practised the syntax with flashcards, which is precisely the method that cannot reach an implicit memory. The repair is repetition, and it is why this variant points at the automatization drills rather than at a verification step.

The counterintuitive part, and the reason this is a pattern rather than a warning, is that similarity increases both kinds of transfer at once. Java and C# are similar enough that most knowledge carries, which is exactly what makes the small number of divergences dangerous — there is no felt signal marking them.

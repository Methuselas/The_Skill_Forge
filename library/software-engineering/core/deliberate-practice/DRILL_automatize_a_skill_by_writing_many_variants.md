---
object_id: DRILL_automatize_a_skill_by_writing_many_variants
object_type: drill
name: Automatize a Construct by Writing and Converting Many Variants
target_skill: Moving a programming construct from conscious effort to no effort, so it stops consuming capacity
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
- repetition
- spacing
cross_links:
- rel: supports
  target_object_id: PAT_match_practice_method_to_the_memory_type
- rel: supports
  target_object_id: PAT_space_practice_across_widening_intervals
- rel: related_to
  target_object_id: DRILL_practice_syntax_with_flashcards
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Automatize a Construct by Writing and Converting Many Variants

## Practice Task
Take one construct you have not automatized and write many small variations of it, then convert equivalent forms back and forth, in short sessions spread over days.

## Target Skill
Moving a programming construct from conscious effort to no effort, so it stops consuming capacity.

## Setup
One construct, chosen from whatever your phase diagnosis left in the cognitive or associative column. A scratch file. A short slot each day rather than one long session.

## Instructions
1. Pick exactly one construct. Loops, list comprehensions, a destructuring form, an async idiom — small enough that a single repetition takes seconds. Time one repetition to establish that rather than judging it by shape.
2. State the axes the variants will differ along — direction, step, bound, nesting — then write many similar-but-different instances of it. For loops that means forward, backward, with a stepper variable, with different step sizes, until the shape comes without deliberation.
3. When the construct is more complex, adapt existing programs instead of writing from scratch. Write several programs using the form you already know — plain loops — then convert each one into the form you are learning, such as a list comprehension.
4. Convert back. Manually reverting each change makes you see the difference from the other direction, and it is the comparison that strengthens the equivalence between the two forms in memory. Record the comparison as you make the reverse conversion.
5. Keep sessions short and spaced, recording the date of each. Set aside some time every day rather than doing one long burst, and continue until you can perform the task with no effort at all.
6. Stop when the construct passes the autonomous test — you can produce it while thinking about something else, and feel no need to check it.

## Success Check
- The construct is small enough that one repetition takes seconds, established by timing one rather than by judging its shape.
- The variants differ along stated axes — direction, step, bound, nesting — rather than being restatements. Many near-identical copies practise transcription instead of the construct.
- The conversion is performed in both directions, and the reverse is where the comparison is recorded. Converting only forwards trains one mapping and leaves the equivalence unbuilt.
- Sessions are short and spaced with dates recorded. One long burst is the condition this technique is defined against, and only the record distinguishes them afterwards. Spacing cannot be shown within the first sitting, which can do no more than open the record.
- The stopping test is the autonomous one — producing the construct while attending to something else — rather than the absence of a felt need to check, which arrives well before fluency does.

## Common Failures
- Practising several constructs at once, which turns the drill back into ordinary programming and dilutes the repetition that does the work.
- One long session instead of spaced short ones. This is repetition-built implicit memory, and it follows the same spacing rules as everything else.
- Stopping at correct rather than at effortless. Correct-with-a-trick is the associative phase, and the load has not been recovered yet.
- Skipping the reverse conversion, which is where the two forms get linked rather than just the new one practised.

## Notes
Hermans is candid that this is not how programmers usually practise. Deliberately typing a hundred for-loops is not something commonly done in programming culture, and she says twice that the technique may feel weird — the analogy offered is weight lifting, where each repetition adds a little. The justification is not that the construct is hard but that every construct still costing attention is spending capacity the real problem needs.

The adaptation variant is the more interesting half and applies to anything with two equivalent forms. Writing loops and converting them to comprehensions, then reverting, is doing for whole constructs what two-sided flashcards do for syntax pairs — the value is in the active comparison rather than in either form alone.

This drill is the natural follow-on from the phase diagnosis. That one produces the list; this one is how an item leaves it.

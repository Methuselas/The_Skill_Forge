---
object_id: DRILL_practice_syntax_with_flashcards
object_type: drill
name: Build and Prune a Syntax Flashcard Set
target_skill: Producing frequently needed syntax from memory instead of searching for it
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
- flashcards
- syntax
- retrieval_practice
- deliberate_practice
cross_links:
- rel: supports
  target_object_id: PAT_attempt_recall_before_looking_up
- rel: supports
  target_object_id: PAT_space_practice_across_widening_intervals
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants:
- variant_id: VAR_hermans_put_code_on_both_sides_for_construct_synonyms
  variant_name: Put Code on Both Sides for Construct Synonyms
  variant_basis: medium
  difference_from_foundation: The foundation pairs a textual prompt with the code it should produce, which trains recall of syntax from intent. This variant makes both sides code — the plain form on one side and the advanced equivalent on the other, such as an explicit loop against the list comprehension, or an if-statement against the ternary — so the card trains translation between two notations for the same operation rather than recall from a description.
  when_to_use: Use for advanced constructs you keep having to rewrite into a simpler form before you can read them, where a textual prompt would be clumsier than the plain code it describes. Repeatedly downgrading the same construct to read it is the signal that it belongs on a card in this form.
  when_not_to_use: Do not use it for constructs with no clean equivalent, since there is nothing to put on the other side; and not for basic syntax, where a description makes a sharper prompt than a second code snippet.
  absorbed_from_object_id: none
---

# Build and Prune a Syntax Flashcard Set

## Practice Task
Build a working card set for the syntax you keep searching for, practise it by producing code rather than reading it, and prune it as items become reliable.

## Target Skill
Producing frequently needed syntax from memory instead of searching for it.

## Setup
Paper cards, sticky notes, or a spaced-repetition app such as Anki, Quizlet, or Cerego. An editor or blank paper to write answers on — answering in your head does not count.

## Instructions
1. List the ten concepts whose syntax you most often have to look up.
2. Make one card per concept: the prompt on the front, the code on the back. Keep each card to a single concept — for list comprehensions that means separate cards for the plain form, the filtered form, the calculated form, and filter-plus-calculation, not one card covering all four.
3. Practise by reading the prompt side only, writing the code out in full, then flipping the card to compare.
4. Mark each attempt right or wrong with a running tally on the card itself.
5. Add a card whenever you meet a new concept in a language, framework, or library you are learning — and, more importantly, whenever you catch yourself about to search for something. That impulse is the signal that the concept is not yet yours.
6. Retire a card once it has been right several times running. Put it back the moment it fails again.
7. Leave fringe syntax out of the set entirely. Modern languages and APIs are far too large to hold, and looking up rarely used corners is a reasonable use of a search.

## Success Check
- You can produce the code for a card on a blank page, not merely recognise it as correct when shown.
- The tally on each card reflects real attempts, so the set can be pruned on evidence rather than on a feeling of familiarity.
- Cards you have retired stay retired for weeks; ones that keep returning to the set indicate a concept that needs a different explanation, not more repetitions.

## Common Failures
- Reading both sides of the card. This turns retrieval practice into re-reading, which builds the strength that was not lacking.
- Cards so broad that "getting it right" is ambiguous — one card carrying an entire API surface cannot be scored.
- Practising in a burst and abandoning the set. The set only pays off across weeks; see the spacing pattern.
- Growing the set indefinitely because pruning feels like losing progress.

## Notes
The reason this is tractable for programming and painful for natural language is size: even a large language like C++ has far fewer basic syntactic elements than French has words, so a genuinely useful set is small enough to finish. Hermans's figure 3.1 shows the physical form — prompt on the front, code on the back, tally marks in the corner of the back — and the tally is the part that makes pruning a measurement instead of a guess.

Apps do the thinning automatically by showing known cards less often, which is a convenience rather than a different method; the paper version and the app implement the same loop.

`VAR_hermans_put_code_on_both_sides_for_construct_synonyms` retains **Put Code on Both Sides for Construct Synonyms** as a bounded alternative. Instead of a written prompt paired with code, both faces carry code — the plain loop against the comprehension, the if-statement against the ternary — so the card drills translation between two notations rather than recall from a description. Reach for it when you keep rewriting the same advanced construct into a simpler form just to read it, since that repetition is the signal the construct is not yet yours. It is the wrong shape for basic syntax, where a description is the sharper prompt, and impossible for constructs that have no clean equivalent to put on the other side.

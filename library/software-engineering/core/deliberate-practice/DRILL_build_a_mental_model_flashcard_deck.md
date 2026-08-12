---
object_id: DRILL_build_a_mental_model_flashcard_deck
object_type: drill
name: Build a Flashcard Deck of Mental Models
target_skill: Holding a wide enough vocabulary of models to recognize which one fits unfamiliar code
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
- mental_model
- retrieval_practice
- deliberate_practice
cross_links:
- rel: related_to
  target_object_id: DRILL_practice_syntax_with_flashcards
- rel: supports
  target_object_id: AP_build_a_mental_model_of_unfamiliar_code
- rel: supports
  target_object_id: PAT_space_practice_across_widening_intervals
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u06, pp. 101-102
  evidence_type: text
confidence: high
references: []
variants: []
---

# Build a Flashcard Deck of Mental Models

## Practice Task
Build a deck whose cards are ways of thinking about code rather than pieces of syntax, then use it both to test recall and to break into code you are stuck on.

## Target Skill
Holding a wide enough vocabulary of models to recognize which one fits unfamiliar code.

## Setup
Cards or a spaced-repetition app, and a piece of code you are currently finding hard. A separate deck from any syntax deck — the two are practised for different reasons and mixing them makes both harder to prune.

## Instructions
1. Put the name of a mental model on the prompt side and a brief explanation or a visualization on the back.
2. Append to the back of each card the questions you would have to answer to apply the model. For a tree: what pieces of code are the leaves, what are the nodes, what are the edges? For a state table: what are the variables?
3. Seed the deck from the categories that are generally worth holding regardless of your stack — data structures such as directed and undirected graphs and the various forms of list; design patterns such as observer; architectural patterns such as Model–View–Controller; diagrams such as entity relationship and sequence diagrams; and modeling tools such as state diagrams and Petri nets.
4. Add the models specific to your situation, since which ones matter depends on your domain, language, and architecture.
5. Practise it the same way as a syntax deck: read the prompt, produce the explanation, then check. Add a card whenever you meet a pattern you did not recognize.
6. Use the second mode when you are stuck. Go through the deck and ask of each card whether it might apply to the code in front of you — "can I think of this code in the form of a tree?" — and when one plausibly fits, use its appended questions to start building the model.
7. Build the deck with your team where you can, so the vocabulary is shared.

## Success Check
- You can produce a model's explanation and its application questions from the prompt alone.
- A sweep of the deck against stuck code produces at least one candidate framing you would not have reached unprompted.
- The deck grows from encounters with unfamiliar patterns rather than from copying a list.

## Common Failures
- Filling the deck with definitions you can recite but cannot apply — the appended questions are what make a card usable, and a card without them is trivia.
- Merging this deck into the syntax deck. The syntax deck's goal is producing code you would otherwise look up; this deck's goal is widening the set of framings available to you, and the two prune on different evidence.
- Only ever practising recall and never running the sweep. The sweep is the mode that pays off on real code.

## Notes
Hermans is explicit that this is a second form of flashcards with a different purpose: "The goal of this second form of flashcards is not to extend your knowledge of syntactic concepts but to extend your vocabulary of mental models, or ways to think about code." That is why this is a separate drill from the syntax deck rather than a variant of it — the method is shared, the skill being built is not.

The deck follows from Gentner and Stevens's position that generic mental models live in long-term memory and are recalled when a situation resembles one seen before, which is why a stored model of tree traversal lets you read tree code in a language you have never used. If models are recalled rather than constructed, the way to get better at using them is to have more of them stored, and flashcards are the chapter's existing tool for that.

Exercise 6.3 adds the team dimension directly, noting that a shared vocabulary of mental models can greatly ease communication about code. Both views of where mental models live turn out to hold — later work showed models stored in long-term memory influence the ones built in working memory — so this drill and the model-building plan support each other rather than competing.

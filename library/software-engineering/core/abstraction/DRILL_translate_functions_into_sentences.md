---
object_id: DRILL_translate_functions_into_sentences
object_type: drill
name: Translate Each Function Into a Sentence and Split the Clunky Ones
library_path:
- software-engineering
- core
- abstraction
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- functions
- refactoring
- readability
- decomposition
cross_links:
- rel: teaches
  target_object_id: PAT_write_functions_as_single_sentences
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: spotting functions that do too much and extracting well-named helper functions
references: []
variants: []
---

# Translate Each Function Into a Sentence and Split the Clunky Ones

## Practice Task
Take a function that does too much, read it aloud as a single sentence, and refactor it until it reads cleanly by extracting helper functions.

## Target Skill
Recognizing the "clunky sentence" smell of an overloaded function and breaking it into one-task or composing functions.

## Setup
No special setup required.

## Instructions
1. Find or write a function that both computes something and acts on the result — for example, one that finds an entity's address through several branches and then sends it a letter.
2. Write down the whole function as one English sentence, spelling out every branch inline (scrapyard address if scrapped, showroom if unsold, buyer's address otherwise, then send the letter).
3. Judge the written sentence, pointing at the words in it that mark a second job — a new verb taking a new object, a clause starting with "and then" — and mark the function as doing too much where they appear.
4. Extract the nuts-and-bolts of each subproblem into a well-named helper (an address-finder), leaving the original function to compose the steps.
5. Write down the sentence each helper reads as, and say whether that sentence has one verb.
6. Write down the sentence for the refactored function, naming what each step is for rather than how it works.
7. Name a concrete second caller for at least one helper — an existing one, or a specific plausible one.
8. Check the refactored outer function for the opposite error, and where a piece of work was left inline, state it along with why.

## Success Check
- The sentence for the original function is written down before any extraction, and the words in it that mark a second job are pointed at — a new verb taking a new object, a clause starting with "and then". A verdict that the function does too much, without the sentence it came from, cannot be checked and does not count.
- The sentence for the refactored function is also written down, and it names what each step is for rather than how it works. If the new sentence still spells out a branch, the extraction moved code without moving the concept.
- Each extracted helper is given the sentence it reads as, and that sentence has one verb. A helper whose sentence needs "and" is the next split, and saying so is part of passing rather than a failure to admit.
- For at least one helper, a second caller is named concretely — an existing one, or a specific plausible one. Asserting that a helper nobody else would call is now reusable satisfies the letter of this bullet and demonstrates nothing.
- The refactored outer function is checked for the opposite error: it composes steps and performs none of the work itself. Where a piece was left inline, that is stated along with why.

## Common Failures
- Splitting on line count instead of on concepts, producing arbitrary fragments that still don't read cleanly.
- Extracting a helper but giving it a vague name, so the composed sentence is still hard to follow.

## Notes
This turns the chapter's function-as-sentence heuristic into repeatable practice, using the vehicle-letter example as the model case. Run it as a habit on your own first-cut code before code review: the moment a function resists being read as a clean sentence is the moment to break out helpers.

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
2. Read the whole function aloud as one English sentence, spelling out every branch inline (scrapyard address if scrapped, showroom if unsold, buyer's address otherwise, then send the letter).
3. Judge the sentence: if it stuffs in several concepts or needs re-reading to follow, mark the function as doing too much.
4. Extract the nuts-and-bolts of each subproblem into a well-named helper (an address-finder), leaving the original function to compose the steps.
5. Re-read the refactored function as a sentence and confirm it now states just its steps: get the address; if found, send the letter.

## Success Check
- The top function reads as one clean sentence naming only its steps.
- Each extracted helper performs a single task or composes other calls.
- At least one extracted helper is now independently reusable.

## Common Failures
- Splitting on line count instead of on concepts, producing arbitrary fragments that still don't read cleanly.
- Extracting a helper but giving it a vague name, so the composed sentence is still hard to follow.

## Notes
This turns the chapter's function-as-sentence heuristic into repeatable practice, using the vehicle-letter example as the model case. Run it as a habit on your own first-cut code before code review: the moment a function resists being read as a clean sentence is the moment to break out helpers.

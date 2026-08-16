---
object_id: DRILL_split_a_too_big_class_by_concept
object_type: drill
name: Evaluate a Big Class Against the Pillars and Split It by Concept
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
- classes
- refactoring
- modularity
- separation_of_concerns
cross_links:
- rel: teaches
  target_object_id: PAT_size_classes_by_pillars_not_lines
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: judging a class against the quality pillars and refactoring it into one class per concept
references: []
variants: []
---

# Evaluate a Big Class Against the Pillars and Split It by Concept

## Practice Task
Take a class that solves several subproblems and refactor it into one class per concept, justifying each split against the quality pillars.

## Target Skill
Diagnosing an over-large class with the pillars and separating its concerns into cohesive classes.

## Setup
No special setup required.

## Instructions
1. Pick a class that nominally does one thing but internally solves several subproblems — for example a text summarizer that splits paragraphs, extracts nouns/verbs/adjectives, and computes an importance score.
2. List the separable subproblems it contains.
3. For each pillar — readable, modular, reusable, testable — write one concrete way the current class fails it (can't swap the scorer; can't reuse paragraph-splitting; can't test the scoring logic without exposing internals).
4. Extract each subproblem into its own class (a paragraph finder, an importance scorer) and pass those into the original class through its constructor.
5. Re-check the pillars: confirm the top class now reads as a few steps, each subproblem class is independently testable, and a subproblem is now reusable elsewhere.

## Success Check
- The original class's top method reads as a short sequence of high-level steps.
- Each extracted class has a single cohesive concern and its own tests.
- At least one extracted class is reusable by unrelated code without dragging the rest along.

## Common Failures
- "Refactoring" by making internal helpers public instead of extracting real classes, which just pollutes the API.
- Splitting into layers so thin that the pieces only ever serve each other, trading one problem for another.

## Notes
This drills the pillar-based class-sizing judgment on the book's `TextSummarizer` progression, from the monolith through one-class-per-concept with constructor injection. The point is not the specific example but the reflex: when a class feels big, enumerate its subproblems and test each against the four pillars before deciding how to split.

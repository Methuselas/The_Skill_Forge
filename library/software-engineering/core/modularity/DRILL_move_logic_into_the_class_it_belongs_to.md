---
object_id: DRILL_move_logic_into_the_class_it_belongs_to
object_type: drill
name: Move Reaching-In Logic Into the Class It Belongs To
library_path:
- software-engineering
- core
- modularity
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- law_of_demeter
- modularity
- refactoring
- encapsulation
cross_links:
- rel: teaches
  target_object_id: PAT_make_classes_care_about_themselves
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u08, pp. 226-228
  evidence_type: text
confidence: high
target_skill: relocating logic that operates on another class's internals into that class
references: []
variants: []
---

# Move Reaching-In Logic Into the Class It Belongs To

## Practice Task
Take a method that reaches into another class's parts to compute something, move it onto that class, and confirm a related requirement change now touches only one class.

## Target Skill
Spotting logic that cares about another class's internals and relocating it to that class.

## Setup
No special setup required.

## Instructions
1. Start from a class with a method that operates on another class's parts — a book computing a chapter's word count from the chapter's prelude and sections.
2. Circle the chained access into the other object's internals (getting a chapter's prelude and calling word count on it) as the Law-of-Demeter smell.
3. Move the logic onto the class it concerns: give the chapter a `wordCount()` member function that sums its own parts.
4. Update the original class to call the new high-level method and drop its knowledge of the other class's structure.
5. Simulate a requirement change (chapters gain a summary) and confirm only the chapter class needs editing.

## Success Check
- The relocated logic lives on the class whose internals it uses.
- The former caller no longer references the other class's parts, only its high-level method.
- The simulated requirement change is confined to a single class.

## Common Failures
- Moving the method but still passing the other object's parts into it, keeping the coupling.
- Leaving a duplicate of the logic behind in the original class.

## Notes
This drills Long's `Book`/`Chapter` refactor. The reflex it builds is to read a chained call through an object into its members as a sign the logic is in the wrong place, and to push it onto the class that owns the data so future changes stay local.

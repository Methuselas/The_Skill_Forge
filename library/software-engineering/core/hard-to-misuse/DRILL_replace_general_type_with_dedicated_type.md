---
object_id: DRILL_replace_general_type_with_dedicated_type
object_type: drill
name: Replace an Overly General Type With a Dedicated Type
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- types
- hard_to_misuse
- refactoring
- type_safety
cross_links:
- rel: teaches
  target_object_id: PAT_use_dedicated_types_over_general_ones
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
target_skill: replacing a permissive general type with a self-describing dedicated type
references: []
variants: []
---

# Replace an Overly General Type With a Dedicated Type

## Practice Task
Take code that represents a structured concept with a general type and replace it with a dedicated type, then confirm the misuse it enabled no longer compiles.

## Target Skill
Recognizing when a general container hides a specific concept and defining a dedicated type for it.

## Setup
No special setup required.

## Instructions
1. Start from code that uses a general type for a specific concept — a location as a list of two doubles, and a collection of locations as a list of lists of doubles.
2. List the misuses it allows: the type explains nothing, latitude and longitude can be swapped, and a list with the wrong number of values still compiles.
3. Define a small dedicated type — a class with named latitude and longitude fields.
4. Change the function signatures to take the dedicated type, and update callers.
5. Try to reproduce the earlier misuses and confirm they now fail to compile or are impossible, and that the documentation explaining the shape is no longer needed.

## Success Check
- Each misuse the general type permits is written as code that compiles today, before the dedicated type exists.
- Each is retried afterwards and shown failing to compile, with the rejections recorded. A misuse that became merely unlikely is a different outcome, and the run says which of the two it achieved.
- Callers read through named accessors, checked by searching for any surviving positional access and reporting the result of that search.
- The documentation that existed only to explain the shape is deleted, and its deletion is the evidence that the type now carries what the prose was carrying.
- The cost is named: a type to define and maintain, and conversions at every boundary where these values arrive as raw numbers anyway.

## Common Failures
- Reaching for a pair type as the fix, which enforces the count but still does not name or order the fields.
- Leaving one caller on the old general type, forcing the hacky representation to persist.

## Notes
This drills Long's map-location ladder from a list of doubles through a pair to a dedicated `LatLong` class. The habit is to treat an unlabeled general container for a specific concept as a defect, and to spend the few minutes a dedicated type costs before the general representation spreads across the codebase.

---
object_id: PAT_use_dedicated_types_over_general_ones
object_type: pattern
name: Use a Dedicated Type Instead of an Overly General One
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- types
- hard_to_misuse
- type_safety
- api_design
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_replace_primitives_with_descriptive_types
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u07, pp. 186-192
  evidence_type: text
confidence: high
references: []
variants: []
---

# Use a Dedicated Type Instead of an Overly General One

## Pattern Rule
**IF** you need to represent a specific structured concept — a latitude-longitude pair, say
**THEN** define a small dedicated type (class or struct) for it rather than reaching for a general type like a list or a pair, so the type is self-describing and the compiler enforces its shape.

## Do
- Create a purpose type: a `LatLong` class with named `latitude` and `longitude` fields takes minutes to write and makes a parameter self-explanatory, needing no documentation.
- Get real type safety: a dedicated type fixes the field count and names, so latitude and longitude cannot be swapped and a wrong number of values cannot compile.
- Head off the spread: an overly general representation forces every neighbouring class to adopt it too, so a dedicated type stops a hacky paradigm from becoming pervasive.

## Don't
- Don't represent a location as a list of doubles (or a list of lists of doubles); nothing explains the type, latitude and longitude are easily reversed, and a list with too few or too many values still compiles and fails only at runtime.
- Don't settle for a pair type as the fix; a pair of two doubles enforces exactly two values but still does not name them or say which is latitude, so misuse remains easy.

## Checklist
- Does the type name the concept it represents, or is it a bare general container?
- Can the compiler reject a wrong shape (wrong count, swapped fields), or does that surface only at runtime?
- Would a neighbouring class be forced to adopt a hacky representation to interoperate?

## Notes
The map-location example runs the full ladder: a list of doubles is unlabeled and permissive, a pair fixes the count but not the naming or order, and only a dedicated `LatLong` class removes the documentation and the ambiguity entirely. Long ties this to chapter 1's shortcut lesson — a few minutes defining a type saves head-scratching and bugs, and prevents the general representation from spreading through the codebase. This is the misuse-focused sibling of chapter 5's readability-focused descriptive types.

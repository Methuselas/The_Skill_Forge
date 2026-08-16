---
object_id: PAT_encapsulate_related_data_together
object_type: pattern
name: Encapsulate Inescapably Related Data Together
library_path:
- software-engineering
- core
- modularity
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- encapsulation
- modularity
- data_objects
- coupling
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Encapsulate Inescapably Related Data Together

## Pattern Rule
**IF** several pieces of data are inescapably used together and get passed through code that does not care about their specifics
**THEN** group them into a single object or class, so intermediary code relays the whole thing rather than each individual field.

## Do
- Bundle the linked values into one type: font, font size, line height, and text color all describe text styling, so wrap them in a `TextOptions` object.
- Let pass-through code carry the parcel, not its contents: once styling is a `TextOptions`, a `displayMessage` that merely relays it from settings to a renderer needs no knowledge of text styling at all.
- Confine future change to the owners: adding a font-style field then touches only the classes that produce and consume styling, not every function that passed the values along.

## Don't
- Don't thread a cluster of related parameters through layer after layer; a `renderText` taking four separate styling arguments forces every intermediary to know and relay all four.
- Don't over-group either — chapter 2 warned against bundling unrelated concepts — so encapsulate only data that is genuinely always used together.

## Checklist
- Are these values always needed together, with no realistic case of wanting some without the rest?
- Does any intermediary function relay them without caring about their specifics?
- Would adding a related field force edits in code that only passes the data through?

## Notes
Long's courier analogy captures it: a good courier delivers the parcel without knowing whether it holds truffles or pralines, but an unencapsulated `displayMessage` must know every styling field it relays. Grouping them into a `TextOptions` object lets intermediaries pass the whole and stay ignorant of the contents, so a new styling requirement changes only the settings and rendering classes. The balance against chapter 2's over-grouping caution is the test of inescapable relatedness — bundle data only when no caller would want part of it without the rest.

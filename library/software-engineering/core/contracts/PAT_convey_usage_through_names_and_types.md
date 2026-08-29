---
object_id: PAT_convey_usage_through_names_and_types
object_type: pattern
name: Convey How to Use Code Through Names and Types, Not Documentation
library_path:
- software-engineering
- core
- contracts
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- types
- api_design
- documentation
cross_links:
- rel: related_to
  target_object_id: PAT_prefer_unmistakable_over_small_print
- rel: related_to
  target_object_id: AP_harden_a_code_contract
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Convey How to Use Code Through Names and Types, Not Documentation

## Pattern Rule
**IF** you want another engineer to understand how to use your code correctly
**THEN** carry the important usage information in the channels they cannot ignore — the names of functions/classes and the data types of parameters and return values — and treat documentation, asking you, and reading your implementation as weaker or non-scaling backups.

## Do
- Name things so their use is obvious the way `removeEntry()` cannot be confused with `addEntry()`; names read like a table of contents for finding the right code.
- Lean on the type system as enforcement: in a statically typed language callers must get types right or the code will not compile, so types are one of the most reliable ways to prevent misuse.
- Rank the five ways others learn your code and design accordingly: names and types (reliable), documentation (somewhat reliable), asking you and reading your code (do not scale).

## Don't
- Don't rely on other engineers reading documentation — they often skim it, misread unfamiliar terms, or hit stale docs that were never updated with the code.
- Don't answer "how do I use this?" with "read my implementation"; if every dependency required that, engineers would read hundreds of thousands of lines to ship one feature, negating the point of layers of abstraction.

## Checklist
- Can a caller use this correctly from the names and type signatures alone?
- Does any critical usage rule live only in a comment that a reader could skip?
- Would this still be usable if the author were on vacation or had left the company?

## Notes
Long ranks the channels by reliability: names and types are unmistakable because they are enforced or impossible to ignore, while comments and docs are optional and drift out of date, and asking-in-person or reading-the-code collapse as the codebase and its dependency chains grow. Your future self counts as another engineer here — after a year you will have forgotten the details too. This ranking is the practical basis for the contract-and-small-print distinction developed next.

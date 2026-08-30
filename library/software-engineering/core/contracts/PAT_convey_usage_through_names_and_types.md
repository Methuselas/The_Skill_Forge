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
  target_object_id: PAT_treat_conditionally_compiled_code_as_untested
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
- Treat a name borrowed from a familiar convention as a promise already signed. A reader meeting a name they recognise stops reading and uses it, which is this card's whole thesis working as intended. The consequence runs both ways: where the implementation does not do what the convention says, no call site looks wrong, because each was written against the convention and reads correctly against it. The reliability of the channel becomes the reason the defect is invisible, and the more standard the name the fewer people will ever check it.
- Rank the five ways others learn your code and design accordingly: names and types (reliable), documentation (somewhat reliable), asking you and reading your code (do not scale).

## Don't
- Don't rely on other engineers reading documentation — they often skim it, misread unfamiliar terms, or hit stale docs that were never updated with the code.
- Don't give something a conventional name and unconventional behaviour. The two honest options are to obey the convention or to choose a name that promises nothing, and the second is far better than a familiar name a reader would have to verify — because they will not.
- Don't answer "how do I use this?" with "read my implementation"; if every dependency required that, engineers would read hundreds of thousands of lines to ship one feature, negating the point of layers of abstraction.

## Checklist
- Can a caller use this correctly from the names and type signatures alone?
- Does any critical usage rule live only in a comment that a reader could skip?
- Would this still be usable if the author were on vacation or had left the company?
- Does any name here borrow a convention from the language, the standard library, or the
  wider ecosystem, and does the implementation actually do what that convention says?

## Notes
Long ranks the channels by reliability: names and types are unmistakable because they are enforced or impossible to ignore, while comments and docs are optional and drift out of date, and asking-in-person or reading-the-code collapse as the codebase and its dependency chains grow. Your future self counts as another engineer here — after a year you will have forgotten the details too. This ranking is the practical basis for the contract-and-small-print distinction developed next.

The ranking has a consequence on the other side of the interface that is easy to miss while reading it as advice to an author. If names are the channel readers cannot ignore, then a name carrying a well-known meaning is the strongest channel available, and a name that lies through it is the least detectable defect a piece of code can hold. Every call site written against the convention reads correctly, review finds nothing, and the code appears to be used properly everywhere it is used. Nothing about this weakens the argument for informative names; it identifies where the obligation falls. Borrowing a familiar name is taking on its contract, and a name invented for this project promises less and is therefore safer to get wrong.

---
object_id: PAT_write_functions_as_single_sentences
object_type: pattern
name: Make Each Function Read Like a Single Short Sentence
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
- readability
- decomposition
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u02, pp. 30-32
  evidence_type: text
confidence: high
references: []
variants: []
---

# Make Each Function Read Like a Single Short Sentence

## Pattern Rule
**IF** you have written a function and want to know whether it is doing too much
**THEN** try to read it aloud as one sentence; if the sentence is clunky or juggles several concepts, break the nuts-and-bolts logic into well-named helper functions until each function either performs one task or just composes calls to other well-named functions.

## Do
- Recognize the failure shape: a `sendOwnerALetter` that both finds the owner's address (scrapyard vs showroom vs registered buyer) and sends the letter reads as a long clause-stuffed sentence and hides deeply nested ifs.
- Extract the offending subproblem — pull the address-finding logic into `getOwnersAddress` so the caller reads "get the owner's address; if found, send the letter."
- Keep the threshold for extracting a function low; the payoff is both readability and reuse (the extracted `getOwnersAddress` can later serve a display-address feature).

## Don't
- Don't leave the nuts-and-bolts logic of a subproblem inline in a function whose job is really to compose steps.
- Don't expect a perfectly mechanical rule — "one task" is interpretable and some control flow (an if, a loop) is fine even when composing; use the sentence test as the judgment aid.

## Checklist
- Does the function read as one clean sentence, or a clause-stuffed one?
- Is each function either one task or a composition of well-named calls?
- After the first cut, did you take a critical pass to extract clunky sections before review?

## Notes
The vehicle-letter example makes the heuristic concrete: the do-too-much version demands several re-reads, while the split version states its two steps plainly and yields a reusable address-finder. Long positions this as a post-first-cut refactoring habit — churning out an over-long function is easy, so the skill is spotting the clunky-sentence smell and breaking out helpers before sending code for review. It is the function-level specialization of general readability.

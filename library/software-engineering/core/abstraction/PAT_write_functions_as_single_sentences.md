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
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_classify_routine_cohesion_and_apply_the_matching_repair
  variant_name: Classify Routine Cohesion and Apply the Matching Repair
  variant_basis: method_sequence
  difference_from_foundation: The foundation diagnoses an overloaded routine by reading it aloud as one sentence and splitting when the sentence is clunky. This variant replaces the single heuristic with a graded classification that names the failure and prescribes its specific repair. Functional cohesion, where the routine performs one operation and nothing else, is the target. Sequential - steps that share data and must run in order but do not add up to one job - splits into separate routines, with one free to call the other. Communicational - operations linked only by touching the same data, such as printing a report then reinitializing its data - splits, with the reinitialization moved next to where the data is created. Temporal - grouped because they happen at the same moment, such as Startup - is acceptable if it orchestrates calls rather than doing the work itself, and its name should describe the moment rather than list the steps. Procedural - ordered only because a screen asks for fields in that order - splits, and the callers usually change too. Logical, where a flag selects one of several unrelated operations, becomes separate routines instead of a flag, unless the routine is purely a dispatcher of calls, which is a legitimate event handler. Coincidental cohesion needs redesign rather than diagnosis.
  when_to_use: Use when a routine reads badly but the read-aloud test does not say what to do about it. Naming the cohesion type converts a vague sense of wrongness into a specific repair, which is the part the foundation leaves to judgment. Use it also to settle routine length, since McConnell's answer to how long a routine may be is to let cohesion, nesting depth, variable count and decision points decide rather than a line limit.
  when_not_to_use: Do not spend effort pinpointing a diagnosis for a routine with clearly bad cohesion - McConnell says outright that a rewrite beats a precise label there. Do not treat the terminology as the point; the classification is a thinking aid, and functional cohesion is nearly always achievable, so that is where attention belongs.
  absorbed_from_object_id: none
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

`VAR_classify_routine_cohesion_and_apply_the_matching_repair` turns this foundation's read-aloud test into a graded diagnosis with a repair attached to each grade. The clunky-sentence heuristic reliably detects that something is wrong; what it does not supply is which of several distinct faults you are looking at, and they have different fixes. Steps that must run in order and share data get split with one calling the other. Operations linked only by shared data get split, with the second moved next to where that data lives. A routine grouped by timing is fine if it orchestrates rather than performs, and its name should say the moment rather than enumerate the steps. A flag selecting among unrelated operations becomes separate routines, except where the routine is a pure dispatcher, which is a legitimate event handler. The evidence for caring is direct: one study of 450 routines found 50 percent of highly cohesive routines fault-free against 18 percent of low-cohesion ones, and another found the worst coupling-to-cohesion ratios carried seven times the errors at twenty times the cost to fix. The same framing settles routine length, which this package otherwise leaves open - decades of data show routines of 100 to 200 lines are no more error-prone than short ones, so cohesion, nesting depth, variable count and decision points should set the size rather than a line limit, with real caution past 200 lines where the evidence runs out.

---
object_id: PAT_prefer_unmistakable_over_small_print
object_type: pattern
name: Prefer Unmistakable Contract Terms Over Small Print
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
- code_contracts
- api_design
- error_prevention
- documentation
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_hard_to_misuse
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Prefer Unmistakable Contract Terms Over Small Print

## Pattern Rule
**IF** you are deciding where to put a term of your code's contract
**THEN** put it in an unmistakable channel the caller cannot ignore — function and class names, parameter types, return types, checked exceptions — and resort to small print (comments, documentation, unchecked exceptions) only when no unmistakable option exists.

## Do
- Sort each term deliberately: names, parameter types, return types, and checked exceptions are unmistakable because the code will not compile or cannot be used without honoring them.
- Treat the scooter contract as the model: "you are renting a scooter for $10/hour" is unmistakable, but "$300 fine over 30 mph" is a gotcha buried in the terms and conditions — the equivalent of a rule hidden in a comment.
- When small print is genuinely unavoidable, still write clear documentation and do everything you can to get it read, while knowing it remains the weak channel.

## Don't
- Don't push an important obligation into a comment or doc; people skim or skip small print, misread it, or read a version that has gone stale.
- Don't hide a term in an unchecked exception that a caller has no compiler prompt to handle, or that a layer between you and them forgot to document at all.

## Checklist
- Is every must-know term carried by a name, type, or checked exception rather than prose?
- For each remaining piece of small print, is there truly no unmistakable channel for it?
- Would a caller who never reads your comments still use the code correctly?

## Notes
This is the chapter's central move and the concrete technique Long promised in chapter 1 for both avoiding surprises and making code hard to misuse. The scooter analogy separates unmistakable terms from small print, then maps it onto code: names/types/checked-exceptions versus comments/docs/unchecked-exceptions. Because small print is unreliable in three compounding ways — unread, misread, and out of date — the durable rule is to encode obligations where the compiler or the caller cannot miss them, and to prefer making the wrong thing impossible over warning against it.

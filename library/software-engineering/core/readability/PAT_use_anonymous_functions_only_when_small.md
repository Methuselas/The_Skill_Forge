---
object_id: PAT_use_anonymous_functions_only_when_small
object_type: pattern
name: Use Anonymous Functions Only for Small Self-Explanatory Logic
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- anonymous_functions
- functional_programming
- readability
- reuse
cross_links:
- rel: related_to
  target_object_id: PAT_write_functions_as_single_sentences
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Use Anonymous Functions Only for Small Self-Explanatory Logic

## Pattern Rule
**IF** you are about to write logic as an inline anonymous function
**THEN** keep it anonymous only when it is small, self-explanatory, and not worth reusing; otherwise give it a name by extracting a named function.

## Do
- Keep the trivial case inline: `filter(feedback -> !feedback.getComment().isEmpty())` is a single self-explanatory statement, so an anonymous function reads fine.
- Name logic that is not self-explanatory: a parity-bit check has no business as an anonymous `filter(id -> countSetBits(id & 0x7FFF) % 2 == ...)`; extract `isParityBitCorrect` so the caller sees intent, not bitwise detail.
- Break a large anonymous function into named helpers when it grows past two or three lines or nests other anonymous functions, as with a feedback-list builder split into `buildTitle`, `buildCommentText`, and `buildCategories`.

## Don't
- Don't hide non-obvious logic in a nameless function; anonymous functions offer no name-summary, so an unclear one is simply unreadable.
- Don't conflate functional style with anonymous functions — functional-style code can and often should use named functions; the style does not require inline lambdas.

## Checklist
- Is the anonymous function's logic obvious at a glance and only a line or two?
- Would a name communicate intent that the inline code does not?
- Might this logic be reused, arguing for a named function even when it is small?

## Notes
Long contrasts a fine anonymous function (an empty-comment filter) with poor ones (a parity check, and a giant nested list-builder), and the deciding factor is whether the nameless code is self-explanatory and small. His larger point is that engineers conflate functional programming with inline lambdas: the readability and reuse benefits of named functions from chapter 2 still apply, so once an anonymous function stops being trivial, name it.

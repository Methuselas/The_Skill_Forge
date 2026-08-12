---
object_id: PAT_replace_unfamiliar_constructs_with_basic_equivalents
object_type: pattern
name: Choose Which Constructs to Downgrade for Reading
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- cognitive_load
- code_comprehension
- refactoring
cross_links:
- rel: related_to
  target_object_id: PAT_refactor_for_your_own_comprehension
- rel: related_to
  target_object_id: PAT_read_code_as_semantic_chunks
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u04, pp. 52-55
  evidence_type: text
confidence: high
references: []
variants: []
---

# Choose Which Constructs to Downgrade for Reading

## Pattern Rule
**IF** you are deciding which parts of unfamiliar code to rewrite into a plainer form before reading it
**THEN** pick only constructs that meet both tests — they are known to confuse readers, and they have a clear, more basic equivalent
**ELSE** you will spend the rewrite budget on code that was never the obstacle

## Do
- Apply both tests together. A construct that confuses but has no simple equivalent is not a candidate; neither is one with an obvious equivalent that was not costing you anything.
- Work from the constructs that reliably qualify: anonymous functions and lambdas, list comprehensions, and ternary operators all compress control flow onto one line and all have a longhand form.
- Expand a lambda into a named function or an explicit predicate class, a comprehension into the equivalent loop with its filter as an `if`, a ternary into a plain conditional.
- Weigh embedding, not just the construct. A comprehension in isolation may read fine; the same comprehension nested inside dense surrounding code can be the thing that tips you over.

## Don't
- Don't treat brevity as readability. Shorter is easier only when the reader already holds the construct — that is exactly what makes the load extraneous rather than intrinsic.
- Don't be deterred by the direction of travel. Rewriting a lambda into a predicate class produces objectively clunkier code, and doing it to understand the code is not a claim about how the code should ship.
- Don't skip the second test and rewrite anything unfamiliar. Without a clear equivalent, the rewrite becomes a redesign, and you will be debugging your translation instead of reading the original.

## Checklist
- Does this construct genuinely confuse readers, or just look dense to you today?
- Is there an equivalent you can write down immediately without inventing a design?
- After the rewrite, is the remaining difficulty the actual computation rather than its notation?

## Notes
Note the asymmetry these constructs create across languages: JavaScript's ternary puts the condition first and the two results after, while Python's puts the true-result first, then the condition, then the false-result. Someone fluent in one order reads the other with a small but real tax, which is a clean example of load that belongs to the reader rather than the code.

Hermans is direct that this feels wrong to some people, and answers it the same way throughout: readable is in the eye of the beholder, and there is no shame in translating code into a form you can hold. The corollary is that a construct you keep needing to downgrade is a construct worth learning properly, which is where the practice side picks it up.

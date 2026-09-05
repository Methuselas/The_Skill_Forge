---
object_id: PAT_diagnose_a_code_smell_by_the_cognitive_process_it_breaks
object_type: pattern
name: Name Which Cognitive Process a Code Smell Breaks
library_path:
- software-engineering
- core
- code-quality
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_smells
- cognitive_load
- refactoring
- code_comprehension
cross_links:
- rel: related_to
  target_object_id: PAT_separate_intrinsic_from_extraneous_load
- rel: related_to
  target_object_id: PAT_read_code_as_semantic_chunks
- rel: related_to
  target_object_id: PAT_detect_linguistic_antipatterns_in_names
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Name Which Cognitive Process a Code Smell Breaks

## Pattern Rule
**IF** you are arguing that some code is too long, too big, or too repetitive
**THEN** say which cognitive process it defeats — working-memory capacity, chunking, or correct chunking — because that turns an aesthetic objection into a testable claim and tells you which refactoring actually helps.

## Do
- Treat long parameter lists and complex switch statements as **capacity** problems. Working memory holds around six items, so a list beyond that cannot be held while reading, and the method becomes hard to understand for a reason that does not depend on taste.
- Count chunks rather than parameters. `line(int xOrigin, int yOrigin, int xDestination, int yDestination)` is four parameters and probably two chunks — an origin and a destination — so the real limit is context-dependent and rises with the reader's knowledge of the domain.
- Treat God classes and long methods as **chunking-opportunity** problems. Names of functions and classes are what let a reader collapse a block into one unit; seeing `multiples()` and `minimum()` together lets you conclude the code computes a least common denominator without reading it. A long undivided method offers no such handles, so the reader falls back to line-by-line.
- Treat code clones as **mis-chunking** problems, which is the worst of the three because it produces a confident wrong belief rather than slow reading.
- Use the level the smell lives at — method, class, or codebase — to scope the fix. Hermans adds this three-level split to Fowler's catalogue, noting Fowler does not make the distinction himself.

## Don't
- Don't stop at "that class is too big." Hermans's own framing is that the statement is helpful but not helpful enough, because it does not say how big is too big or what that depends on.
- Don't assume a smell means a defect. The presence of a code smell does not necessarily imply the code has an error — the association is statistical, not definitional.
- Don't apply a fixed parameter threshold across a codebase. The same count costs more in an unfamiliar domain, because fewer of the parameters group into chunks the reader already holds.

## Checklist
- Which of the three failures is this — too much to hold, nothing to chunk with, or chunked wrongly?
- At what level does the smell live, and is my proposed fix at that level?
- Would a reader who knows this domain well have the same problem, or is it capacity for a newcomer only?

## Notes
The clone case is worth spelling out because the mechanism is counterintuitive. Seeing `goo()` next to a familiar `foo()`, working memory retrieves what it knows about `foo()` — Hermans's phrase is that it is telling you "This might come in handy" — and the glance at `goo()` is then interpreted through that retrieval, producing "Ah, that is a `foo()`." The two get filed under one category, exactly as a chess player files several variations under "Sicilian."

One worked example makes the danger concrete in a way prose does not. The two functions are identical apart from the else branch, where `foo` returns `j++` and `goo` returns `j+2` — a one-token divergence inside otherwise duplicated code, labelled Product A and Product B. That is precisely the shape mis-chunking hides, and Hermans notes it may take several exposures before you register that they differ at all, since the resulting misconception behaves like any other.

Khomh's work on Eclipse supplies the empirical backing: God classes were significant contributors to error proneness across all versions analysed, God methods in one, and large class and long method significantly raised change proneness in more than 75% of releases.

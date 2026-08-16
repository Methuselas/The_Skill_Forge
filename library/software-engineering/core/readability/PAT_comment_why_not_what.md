---
object_id: PAT_comment_why_not_what
object_type: pattern
name: Comment the Why, Not the What
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
- comments
- documentation
- readability
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants:
- variant_id: VAR_cognition_high_level_comments_as_chunks
  variant_name: Use High-Level Comments as Chunk Labels
  variant_basis: emphasis
  difference_from_foundation: Gives high-level functional comments a cognitive role as labels for a larger code chunk while showing that line-level what-comments consume attention and burden the same chunking process.
  when_to_use: A concise functional summary helps a reader, especially a newcomer, recognize the purpose of a larger block before processing its details.
  when_not_to_use: The comment merely narrates an obvious statement or duplicates a name the code can express directly.
  absorbed_from_object_id: none
- variant_id: VAR_hermans_comment_to_preserve_your_own_context
  variant_name: Comment to Preserve the Author's Model, Including Your Own
  variant_basis: emphasis
  difference_from_foundation: The foundation writes comments for a future reader, explaining why the code is as it is. This variant adds a second beneficiary — you, twenty minutes from now — and widens what belongs in a comment accordingly. What is worth capturing is the designer's mental model, which includes the goals of the code, why this approach was chosen, and which alternatives were considered and rejected. None of that is expressible as code, so the self-documenting-code position does not reach it, and when it goes unwritten it can at best be rediscovered later at cost.
  when_to_use: Use when you are about to be interrupted and can hold the interruption off for a moment, when a design decision rejected a live alternative, or when you will not finish the current task in one sitting. Comments are the right medium specifically because they are always present, whereas separate notes and documents have to be found again before they help.
  when_not_to_use: It does not license narrating what the code does line by line, which the foundation rules out and this variant leaves ruled out. It also does not apply where the decision was forced and no alternative existed, since there is no reasoning to preserve.
  absorbed_from_object_id: none
- variant_id: VAR_ppp_keep_the_design_statements_written_before_the_code
  variant_name: Keep the Design Statements You Wrote Before the Code
  variant_basis: method_sequence
  difference_from_foundation: The foundation writes comments after or alongside the code and keeps only what the code cannot say, treating a comment every line or two as clutter. This variant produces the comments before any code exists — they are the intent-level design statements the routine was grown from — and then keeps them at a density the foundation would reject, roughly one comment per two to ten lines of code. Provenance is what changes the arithmetic. A comment written before its code cannot be a restatement of that code, because the code was written to satisfy the comment; McConnell's own concession is that two lines of comment for two lines of code would nearly always be overkill if you were commenting afterward, and that what matters here is the semantic content rather than the ratio. The cleanup pass then deletes only the ones that turned out redundant, typically a design line sitting above a call to a well-named routine.
  when_to_use: Use when the routine was designed in English before being coded, so the comments are the surviving design rather than a narration added later. It is the routing that makes detailed design durable — a design kept in a separate document drifts out of agreement with the code the first time either changes, whereas one that lives inside the routine stays accurate as long as the inline comments are maintained.
  when_not_to_use: Do not use it to justify retrofitting a comment onto every couple of lines of existing code. Without the design-first provenance those are precisely the restatements the foundation rules out, and the density is what makes them expensive. It also does not apply to routines that never needed a design pass, such as accessors and pass-throughs.
  absorbed_from_object_id: none
---

# Comment the Why, Not the What

## Pattern Rule
**IF** you are about to write a comment
**THEN** reserve it for the why — context the code cannot convey — and for high-level summaries, and make the line-by-line what self-explanatory through the code itself.

## Do
- Comment context the code cannot show: a product or business decision, a fix for a nonobvious bug, or a counterintuitive quirk of a dependency — for example why users who signed up before v2.0 get name-based IDs, with an issue link.
- Use high-level summaries like a book's back-cover synopsis: a class-level comment noting the `User` relates to the streaming service and may be out of sync with the database helps a reader gauge relevance fast.
- When a comment is only needed because the code is unclear, fix the code instead — pull `data[0]`/`data[1]` into `firstName(data)`/`lastName(data)` rather than explaining the indices.

## Don't
- Don't write redundant what-comments on self-explanatory code; a comment restating `firstName + "." + lastName` just adds clutter and a second thing to keep in sync.
- Don't let a per-line synopsis pile up; a comment on every line is like a synopsis before every paragraph of a book — it harms readability rather than helping.

## Checklist
- Does each comment explain why, or summarize at a high level, rather than restate the code?
- Where a comment explains what, could clearer code remove the need for it?
- Will this comment go stale, and is it worth that maintenance cost?

## Notes

Long splits comment purposes into what and why: the what should mostly come from readable code and names, while the why — business decisions, weird-bug fixes, dependency quirks — genuinely needs prose because the code cannot self-explain intent. He balances this against the standing costs of comments (maintenance, staleness, clutter) and the chapter-3 reality that engineers often do not read documentation, so comments are a supplement to readable code, not a replacement for it.

Variant `VAR_hermans_comment_to_preserve_your_own_context` (The Programmer's Brain, Chapter 11) adds a second audience for the same rule: yourself, shortly. Hermans defends comments against the self-documenting-code position on a narrow and strong ground — code seldom explains the programmer's thought process, so it cannot represent the author's mental model. Why an approach was chosen, what the code is for, and which alternatives were rejected are not expressible in code, and unwritten they can only be rediscovered at cost. She quotes Ousterhout, that the idea behind comments is to capture information that was in the designer's mind but could not be represented in the code, and Brooks, that comments matter most in comprehension because they are always present — notes and documents have to be found before they help. The practical form is a brain dump into a comment when an interruption can be held off for a moment. It does not license line-by-line narration, which stays ruled out.

Variant `VAR_cognition_high_level_comments_as_chunks` (The Programmer's Brain, Chapter 2) preserves a narrow exception for functional summaries: a comment such as "prints a binary tree in order" gives a reader one label for a larger block and is especially useful to newcomers. The same evidence strengthens the foundation's rejection of line-by-line narration; a comment that only says to increment an index consumes attention and makes chunking harder.

Variant `VAR_ppp_keep_the_design_statements_written_before_the_code` (Code Complete, ch. 9) is the one that openly disagrees with the foundation on density, and the disagreement is worth reading rather than resolving. McConnell reaches a comment every two to ten lines and keeps it; Long would call most of that clutter. They are not describing the same artifact. Long's are written to explain code that already exists, so a comment per couple of lines can only be restating something visible. McConnell's were written before the code, in English, as the design — the code was then filled in beneath each one to satisfy it. That ordering is what makes the density defensible, and it is also why the method's final step *removes* comments rather than adding them: the only ones deleted are those that turned out redundant once the code was written, usually a design line above a call to a well-named routine. The practical reading is that the density question is downstream of a provenance question. Ask where a comment came from before asking whether there are too many, and note that neither source endorses adding this density to code that was not designed this way.

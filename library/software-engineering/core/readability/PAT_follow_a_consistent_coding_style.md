---
object_id: PAT_follow_a_consistent_coding_style
object_type: pattern
name: Follow a Consistent Coding Style Guide
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
- coding_style
- conventions
- linters
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 115-117
  evidence_type: text
confidence: high
references: []
variants:
- variant_id: VAR_hermans_prefer_camel_case_when_the_choice_is_open
  variant_name: Prefer Camel Case When the Convention Is Actually Yours to Pick
  variant_basis: constraint
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  locator: u08, pp. 140-141
  difference_from_foundation: The foundation says to adopt whatever guide is in force and treats the specific conventions as arbitrary but shared. This variant supplies evidence that one common choice is not arbitrary — Binkley found identifiers written in camel case were selected correctly far more often than snake case, at a small cost in speed — and it constrains when that evidence may be acted on, since prior training in a style measurably degrades performance in the other one.
  when_to_use: Use only at the moment a convention is genuinely open, which in practice means a new project or a language whose ecosystem does not already dictate the answer. That is the narrow window in which the accuracy difference is available to be claimed.
  when_not_to_use: Do not use it to argue for converting an existing snake-case codebase, which the source rules out directly — consistency dominates, and the conversion would also penalise everyone already trained on the current style. It is likewise inapplicable where the language community has settled the question, as PEP 8 has for Python.
  absorbed_from_object_id: none
---

# Follow a Consistent Coding Style Guide

## Pattern Rule
**IF** a stylistic choice is not dictated by the compiler — naming casing, indentation, feature usage, file layout
**THEN** follow the team's agreed coding style guide, because a shared style lets readers rely on conventions to understand code correctly.

## Do
- Lean on convention as information: with PascalCase classes and camelCase variables, `ConnectionManager.terminateAll()` reads unmistakably as a call into a class that likely touches global state.
- Adopt the team or organization style guide as-is where one exists; where none does, take an off-the-shelf one such as a published language style guide rather than inventing conventions.
- Run a linter to catch style-guide violations and some error-prone patterns automatically, as a cheap first pass.

## Don't
- Don't break the convention and let `connectionManager` (camelCase) masquerade as an instance variable when it is actually a class with a static `terminateAll()` — that misreading terminated every chat on the server, not one.
- Don't rely on the linter as a substitute for good code; linters catch only simple issues.

## Checklist
- Does naming casing let a reader tell classes from instances at a glance?
- Are you following the team's style guide rather than a personal style?
- Is a linter enforcing the conventions the guide specifies?

## Notes
`VAR_hermans_prefer_camel_case_when_the_choice_is_open` retains **Prefer Camel Case When the Convention Is Actually Yours to Pick**, which is the one place the chapter's evidence bears on a choice this foundation treats as arbitrary. Binkley tested 135 programmers and non-programmers, showing each a sentence describing a variable and then four candidate identifiers to match it against; camel case produced a 51.5% higher chance of selecting the right one, at a cost of about half a second longer per identifier. The training effect is the part that constrains the advice — participants trained in camel case were faster on camel case and *slower on snake case than untrained participants were*, which means a style is not neutral once a team has practised it. Hermans draws the conclusion narrowly, that converting an existing snake-case codebase would be unwise and consistency matters more, but that camel case is the better bet when the decision is genuinely open.

The `GroupChat` bug is the cautionary tale: a class named `connectionManager` violates the PascalCase-for-classes convention, so a reader reasonably assumes it is an instance field and that `terminateAll()` affects only their chat, when it is static and terminates every connection on the server. A consistent style is like a whole team speaking one language fluently — it removes a class of misreadings, which is why Long frames adopting and following a style guide (backed by linters) as a readability and bug-prevention measure.

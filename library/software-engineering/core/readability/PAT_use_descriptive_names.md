---
object_id: PAT_use_descriptive_names
object_type: pattern
name: Use Descriptive Names Instead of Comments to Explain What Things Are
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
- naming
- readability
- self_documenting_code
- comments
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 106-108
  evidence_type: text
confidence: high
references: []
variants:
- variant_id: VAR_cognition_visually_distinct_identifiers
  variant_name: Keep Short Identifiers Visually and Structurally Distinct
  variant_basis: constraint
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  locator: u02, p. 17
  difference_from_foundation: Adds a perceptual constraint on top of semantic descriptiveness, requiring a name to also be quick to tell apart from its neighbours and from digits, because unfamiliar or confusable short names defeat the pattern recognition a reader uses to group code.
  when_to_use: Choosing loop counters, temporaries, and other short-lived names, or reviewing code where single letters and lookalike glyphs already appear.
  when_not_to_use: A conventional short name is already unambiguous in context and renaming it would break a convention readers rely on.
  absorbed_from_object_id: none
- variant_id: VAR_hermans_encode_semantic_kind_not_type_in_the_name
  variant_name: Encode a Name's Semantic Kind, Never Its Type
  variant_basis: constraint
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  locator: u05, pp. 73-75
  difference_from_foundation: The foundation asks a name to describe the thing it holds. This variant constrains what a systematic prefix or suffix may encode when a team adopts one — the value's semantic kind or the role it plays in the program, never its data type. Simonyi's original proposal was semantic (cX for a count of X, rw and col for row and column values that are both integers); the discredited convention that encodes types instead is a later misreading, and the two are opposite in value rather than degrees of the same idea.
  when_to_use: Use when a team is agreeing on a naming convention, or when a codebase already carries prefixes and you are deciding whether to keep them. It pairs naturally with the roles-of-variables vocabulary, where putting the role into the name saves every later reader from deducing it.
  when_not_to_use: Do not reintroduce type prefixes in a typed language whose editors already surface types; that is the form the objection was always aimed at. It is also not worth the extra length when the semantic kind is already obvious from the bare name.
  absorbed_from_object_id: none
- variant_id: VAR_hermans_balance_word_clarity_against_recall_cost
  variant_name: Balance Word Clarity Against the Cost of Remembering the Name
  variant_basis: constraint
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  locator: u08, pp. 137-140
  difference_from_foundation: The foundation treats descriptiveness as a one-way improvement, where a fuller name is simply better than a terse one. This variant adds the measured cost on the other side — full words beat abbreviations and single letters for both defect-finding and comprehension, but longer names are harder and slower to recall, and the driver is syllable count rather than character count. Naming therefore becomes a balance between the clarity that helps a reader understand and find bugs and the brevity that helps them hold the name in mind.
  when_to_use: Use when deciding how much to pack into a name, and especially when evaluating a systematic prefix or suffix convention — Lawrie's advice is that such conventions be carefully evaluated to ensure the added information outweighs the added cost of names becoming hard to remember. It also applies when weighing a single-letter name, since outside a handful of cases those carry no reliable shared meaning.
  when_not_to_use: Do not use it to justify abbreviations as a default; the evidence gap between words and abbreviations is large and the recall penalty is comparatively small. It also does not license single letters for anything but genuine conventions such as a loop counter.
  absorbed_from_object_id: none
---

# Use Descriptive Names Instead of Comments to Explain What Things Are

## Pattern Rule
**IF** you are naming a class, function, or variable
**THEN** give it a name that summarizes what it is or does, so the code explains itself, rather than using a short name propped up by a comment.

## Do
- Name for the concept, the way `toaster` tells you far more than `object A`: turn `class T` with `pns` and `s` into `Team` with `playerNames` and `score`.
- Make each call site legible in isolation — `team.containsPlayer(playerName)` is self-explanatory where `t.f(n)` forces a trip to the class definition.
- Let descriptive names replace low-level comments, cutting the clutter and the second thing (the comment) that must be kept in sync with the code.

## Don't
- Don't use a comment to say what a badly-named thing is; a reader deep in a long file then has to scroll back to the declaration to recall what `s` means.
- Don't treat parameter/return documentation as a substitute for names — that documentation can be useful, but it is not where the what-it-is should live.

## Checklist
- Can a reader tell what each name refers to without scrolling elsewhere?
- Is any comment present only to explain a name that could be more descriptive?
- Does a call read clearly on its own line, without opening the callee?

## Notes
Long's before/after is stark: the `T`/`pns`/`s` version is impenetrable, the `Team`/`playerNames`/`score` version is obvious, and adding comments to the bad version only clutters it and adds maintenance. This is the concrete first technique under the chapter-1 readability foundation — names are the cheapest and highest-leverage readability tool, and they remove the clutter and staleness risk that comments carry.

Variant `VAR_cognition_visually_distinct_identifiers` (The Programmer's Brain, Chapter 2) adds a perceptual constraint the foundation does not cover. Hermans deliberately obfuscates a Java routine using `b` and `l` as loop iterators and reports that readers struggle to reproduce it: `l` is visually almost identical to `1`, and unfamiliar short names slow the detection and recognition of otherwise routine structures. Semantic descriptiveness is therefore necessary but not sufficient — a name also has to survive a fast glance. Use this when picking counters and temporaries or when reviewing code that already contains lookalike glyphs; do not use it to churn a conventional short name that is already unambiguous.

Variant `VAR_hermans_balance_word_clarity_against_recall_cost` (The Programmer's Brain, Chapter 8) supplies the cost side the foundation leaves out. Two studies establish the benefit of words: Hofmeister had 72 professional C# developers hunt bugs in code whose identifiers were letters, abbreviations, or words, and participants found 19% more defects per minute with words, with no significant difference between letters and abbreviations. Lawrie had 120 developers averaging 7.5 years' experience summarise code from memory, and summaries of word-identifier code were rated nearly a point higher on a five-point scale than single-letter code. But Lawrie's recall half found longer names harder and slower to remember, driven by syllable count rather than length, which fits chunking — more syllables, more STM chunks. The practical upshot is Lawrie's own caution about prefix and suffix conventions, which must justify the memorability they cost. It does not license abbreviations as a default; the comprehension gap is the larger of the two effects.

Variant `VAR_hermans_encode_semantic_kind_not_type_in_the_name` (The Programmer's Brain, Chapter 5) constrains what a systematic prefix may carry: the value's semantic kind or role, never its data type. The distinction rescues a convention usually dismissed outright. Simonyi's 1976 proposal was semantic — `cX` for a count of X, `rw` and `col` for row and column values that are both plain integers but must never be confused — and Excel's codebase uses it that way. The version that encodes types, popularised in the Windows world and now generally frowned upon, is a misreading of that thesis. Reach for the semantic form when a team is settling a convention or when deciding whether to keep existing prefixes; do not reintroduce type prefixes in a typed language whose editor already shows the type, which is exactly what the objection was aimed at.

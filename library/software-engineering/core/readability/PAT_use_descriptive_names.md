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
- rel: related_to
  target_object_id: AP_choose_a_name_with_feitelsons_three_steps
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Use Descriptive Names Instead of Comments to Explain What Things Are

## Pattern Rule
**IF** you are naming a class, function, or variable
**THEN** give it a name that summarizes what it is or does, so the code explains itself, rather than using a short name propped up by a comment.

## Do
- Name for the concept, the way `toaster` tells you far more than `object A`: turn `class T` with `pns` and `s` into `Team` with `playerNames` and `score`.
- Make each call site legible in isolation — `team.containsPlayer(playerName)` is self-explanatory where `t.f(n)` forces a trip to the class definition.
- Let descriptive names replace low-level comments, cutting the clutter and the second thing (the comment) that must be kept in sync with the code.
- Judge every name against its neighbours as well as on its own, because two names can each describe their contents accurately and still be impossible to keep apart. Run the switch test first — if you could exchange the names of two variables without hurting the program, both are wrong, which condemns `recordNum` beside `numRecords`. Then the telephone test for sound: if you cannot read the code aloud over the phone and be understood, the names need work. Then the distance rule for spelling: names should differ by at least two characters, or differ at the beginning or the end, so `clientRecords` and `clientReports` replace `clientRecs` and `clientReps`.
- Keep short names distinct to the eye as well as to the memory. `l` is nearly identical to `1`, and a confusable glyph defeats the fast pattern recognition a reader uses to group code before reading it.
- Weigh clarity against the cost of holding the name in mind. Full words beat abbreviations and single letters for both defect-finding and comprehension, but longer names are harder and slower to recall, and the driver is syllable count rather than character count — so a name is a balance, not a one-way improvement.
- If a team adopts a systematic prefix or suffix, let it encode the value's semantic kind or the role it plays — `cX` for a count of X, `rw` and `col` for a row and a column that are both plain integers — and never its data type.

## Don't
- Don't use a comment to say what a badly-named thing is; a reader deep in a long file then has to scroll back to the declaration to recall what `s` means.
- Don't treat parameter/return documentation as a substitute for names — that documentation can be useful, but it is not where the what-it-is should live.

## Checklist
- Can a reader tell what each name refers to without scrolling elsewhere?
- Is any comment present only to explain a name that could be more descriptive?
- Does a call read clearly on its own line, without opening the callee?

## Notes
Long's before/after is stark: the `T`/`pns`/`s` version is impenetrable, the `Team`/`playerNames`/`score` version is obvious, and adding comments to the bad version only clutters it and adds maintenance. This is the concrete first technique under the chapter-1 readability foundation — names are the cheapest and highest-leverage readability tool, and they remove the clutter and staleness risk that comments carry.

Judging a name on its own is the part a single reader can do; judging it against its neighbours (Code Complete, ch. 11) is the axis that check cannot see. The switch test is the contribution worth memorising because it is mechanical, takes seconds, and condemns pairs that survive every other check — `input` beside `inputValue`, `fileNumber` beside `fileIndex`. The failures it rules out follow from the three tests: names separated only by capitalization, whose association with meaning is then arbitrary; names separated only by a trailing numeral; deliberate misspellings; words commonly misspelled in English; and more than one natural language, or more than one dialect of English, in a single codebase. Reach for it when adding a name to a region that already holds several related ones, and when reviewing a diff where two similar names appear together. It does not soften the requirement above — a set of mutually distinct names that describe nothing is no improvement — and it does not license padding a name with distinguishing noise, since the distance is supposed to come from the names being about genuinely different things.

Distinctness to the eye is a separate failure from distinctness to the memory, which is why both appear in the Do list. Hermans deliberately obfuscates a Java routine using `b` and `l` as loop iterators and reports that readers struggle to reproduce it: unfamiliar short names slow the detection of otherwise routine structures. That is about glyphs the eye confuses, mostly in short names; the switch and telephone tests are about meanings and sounds the memory confuses, at any length. Neither is a reason to churn a conventional short name that is already unambiguous in context.

The cost side of descriptiveness is measured, not merely asserted (The Programmer's Brain, ch. 8). Two studies establish the benefit of words: Hofmeister had 72 professional C# developers hunt bugs in code whose identifiers were letters, abbreviations, or words, and participants found 19% more defects per minute with words, with no significant difference between letters and abbreviations. Lawrie had 120 developers averaging 7.5 years' experience summarise code from memory, and summaries of word-identifier code were rated nearly a point higher on a five-point scale than single-letter code. But Lawrie's recall half found longer names harder and slower to remember, driven by syllable count rather than length, which fits chunking — more syllables, more chunks in short-term memory. The practical upshot is Lawrie's own caution that prefix and suffix conventions must justify the memorability they cost. None of it licenses abbreviations as a default, since the comprehension gap is much the larger of the two effects, nor single letters outside genuine conventions such as a loop counter.

The semantic-kind rule (The Programmer's Brain, ch. 5) rescues a convention usually dismissed outright. Simonyi's 1976 proposal was semantic — a count of X, or a row and a column that are both plain integers but must never be confused — and Excel's codebase uses it that way. The version that encodes types, popularised in the Windows world and now generally frowned upon, is a misreading of that thesis, so the two are opposite in value rather than degrees of one idea. It pairs naturally with the roles-of-variables vocabulary, where putting the role into the name saves every later reader from deducing it. Do not reintroduce type prefixes in a typed language whose editor already surfaces the type, which is exactly what the objection was aimed at, and do not spend the extra length when the semantic kind is already obvious from the bare name.

---
object_id: PAT_prefer_null_safety_or_optionals
object_type: pattern
name: Signal Absent Values With Null Safety or Optionals
library_path:
- software-engineering
- core
- error-handling
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- null_safety
- optionals
- types
- error_prevention
cross_links:
- rel: related_to
  target_object_id: PAT_return_result_type_to_convey_error_cause
- rel: related_to
  target_object_id: PAT_avoid_returning_magic_values
- rel: related_to
  target_object_id: PAT_use_null_object_pattern_only_when_safe
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Signal Absent Values With Null Safety or Optionals

## Pattern Rule
**IF** a variable, parameter, or return value can legitimately be absent
**THEN** make the absence explicit and compiler-enforced — mark the type nullable under a null-safety regime so it cannot be used without a null check, or use an optional type where the language lacks null safety
**ELSE** where the language offers neither, which is the ordinary situation in C and in older codebases everywhere, absence cannot be made compiler-enforced at all; the honest form is then a sentinel return paired with a separate channel carrying the reason, and it brings an obligation nothing will check for you.

## Do
- Default everything to non-nullable and opt specific things into nullability: under the book's convention a `?` suffix (`Element?`) marks a type that can be null and the compiler blocks use until it is checked.
- Where null safety is unavailable, reach for an optional type (`Optional`, Rust's `Option`, C++'s equivalent) and return `Optional.empty()` instead of a bare null.
- Turn on null safety if your language supports or can retrofit it (newer languages by default, opt-in in recent C#, retrofittable in Java).
- Where the language has neither mechanism, pair a sentinel return with a separate channel that says *why* it is absent, and treat the pairing as one thing rather than two. This is the form C has used for decades, and it carries more than a bare optional does — an optional reports that a value is missing and never reports the reason. What it does not carry is any enforcement, and that is the whole of its cost: the channel must be set on every failing path, including the ones added later, and the caller must read it before any intervening call can overwrite it. Neither obligation is checked by anything, so both belong in what the function documents rather than in what its readers are assumed to know.
- Use the same return to signal that a function could not produce a result at all, not merely that a value is optional. Under null safety the caller is forced to handle the null before use, which makes the failure explicit — but only reach for it when the bare fact of failure is enough, and use a result type the moment the caller needs the reason.

## Don't
- Don't return a bare, unmarked null that callers can dereference without checking — that is the road to `NullPointerException`, `NullReferenceException`, and "cannot read property of null."
- Don't over-correct into banning absence entirely; forbidding all nulls forces awkward code gymnastics when absence is a real, useful concept.

## Checklist
- Is every value that can be absent marked so the compiler forces a check before use?
- Where null safety is absent, is an optional type used instead of a raw null?
- Have you avoided both unchecked nulls and a blanket no-nulls rule?
- Where neither mechanism exists, is the reason channel set on every failing path, and does
  the function document that it must be read before the next call can overwrite it?

## Notes
The two mechanisms this card prefers are unavailable in a large share of the code that
exists, and saying so matters more than it looks. A language with neither is not exempt
from the problem — absence is universal — it simply cannot make the check a compile-time
one, so the same guarantee has to be bought with discipline instead. The sentinel-plus-
channel form is what that discipline looks like when it is done deliberately rather than
by habit, and its two obligations are exactly the ones a compiler would otherwise have
carried: that every failing path sets the reason, and that the reason is read before
anything can clobber it. Treating that pairing as beneath mention is how a reader in such
a language concludes the card does not apply to them and takes nothing from it at all.

This establishes the book's pseudocode convention and a durable typing habit. Long frames nulls as straddling a dichotomy — genuinely useful for representing absence, genuinely dangerous because engineers forget to check them — and resolves it with compiler-enforced null safety or optionals rather than either raw nulls or an absolutist ban. It is the foundation that later error-signaling techniques, such as nullable and optional return types, build on when a function may be unable to produce a result.

Signalling failure is the same move used for a second purpose. Returning null under null safety forces the caller to acknowledge that no value was produced before using the result, so absence and failure share one compiler-enforced channel. The limit is that null conveys no reason — Long's square-root function returns null for a negative input and needs a comment to say what the null means, which is the signal that a result type would carry the information better. The technique is also weak in a language without null safety, where the return can be silently dereferenced and the caller is never forced to look.

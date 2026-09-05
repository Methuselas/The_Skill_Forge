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
- Default everything to non-nullable and opt specific things into nullability: under one common convention a `?` suffix (`Element?`) marks a type that can be null and the compiler blocks use until it is checked.
- Where null safety is unavailable, reach for an optional type (`Optional`, Rust's `Option`, C++'s equivalent) and return `Optional.empty()` instead of a bare null.
- Check that the absent case is distinguishable from every legitimate value before relying on an optional to carry it. The mechanism reports one thing, that no value is present, and it is silently wrong wherever the domain already uses the empty case as data — a setting whose configured value is genuinely nothing, a field whose default really is nothing, a search whose answer is the empty result. Absent and present-but-empty are two states there, and an optional collapses them into one.
- Where they do collapse, introduce a distinct sentinel object for absence and compare it by identity rather than by equality. Its whole job is to be out of band, so it must be a single shared instance that cannot be reconstructed into a second one — which means copying it returns itself, serializing and restoring it yields the same instance, and it does not define equality that could make it match anything else. Miss any of those and two absences stop comparing equal after a round trip, which surfaces far from the cause.
- Keep that sentinel distinct from a magic value, because they look alike and are not. A magic value is drawn from the value's own domain and steals a member of it, so the domain loses a legal value and every reader has to know which one. A sentinel object is out of band by construction — it is not a member of the value's type at all — so nothing is stolen and a reader who has not heard of it cannot mistake it for data.
- Turn on null safety if your language supports or can retrofit it (newer languages by default, opt-in in recent C#, retrofittable in Java).
- Where the language has neither mechanism, pair a sentinel return with a separate channel that says *why* it is absent, and treat the pairing as one thing rather than two. This is the form C has used for decades, and it carries more than a bare optional does — an optional reports that a value is missing and never reports the reason. What it does not carry is any enforcement, and that is the whole of its cost: the channel must be set on every failing path, including the ones added later, and the caller must read it before any intervening call can overwrite it. Neither obligation is checked by anything, so both belong in what the function documents rather than in what its readers are assumed to know.
- Use the same return to signal that a function could not produce a result at all, not merely that a value is optional. Under null safety the caller is forced to handle the null before use, which makes the failure explicit — but only reach for it when the bare fact of failure is enough, and use a result type the moment the caller needs the reason.

## Don't
- Don't return a bare, unmarked null that callers can dereference without checking — that is the road to `NullPointerException`, `NullReferenceException`, and "cannot read property of null."
- Don't over-correct into banning absence entirely; forbidding all nulls forces awkward code gymnastics when absence is a real, useful concept.

## Checklist
- Is every value that can be absent marked so the compiler forces a check before use?
- Where null safety is absent, is an optional type used instead of a raw null?
- Is the empty case already meaningful as data here? If it is, absence needs its own
  out-of-band marker rather than the optional's empty state.
- If a sentinel carries absence, is it a single instance that survives copying and
  serialization as itself, and is it compared by identity?
- Have you avoided both unchecked nulls and a blanket no-nulls rule?
- Where neither mechanism exists, is the reason channel set on every failing path, and does
  the function document that it must be read before the next call can overwrite it?

## Notes
The case the mechanisms do not reach is worth naming separately from the case where they
are missing, because it arrives in exactly the languages that have them and so gets
noticed late. An optional answers one question — is a value present — and that answer is
complete only while the empty case means nothing in the domain. Configuration, defaults,
and query results are the three places it routinely means something: a field configured
to nothing is not a field left unconfigured, and code that treats them alike will
overwrite a deliberate choice with a fallback and call it correct. The tell is a
conditional that has to name both states at once, testing that a value is neither the
empty case nor the absence marker, which is the point at which the two have visibly
stopped being one thing.

The sentinel that fixes it has requirements that are easy to under-build, and every one
of them exists because absence gets compared after being moved. A sentinel that copies
into a second instance, or that comes back from serialization as a fresh object, still
compares correctly by identity everywhere it never travelled, and fails where it did —
so the defect appears at a distance from the code that caused it and looks like a
serialization bug rather than a design one. Making it a shared singleton that returns
itself from copying and restores to itself by name is what closes that, and it is
cheaper to write at the start than to retrofit once callers exist.

The two mechanisms this card prefers are unavailable in a large share of the code that
exists, and saying so matters more than it looks. A language with neither is not exempt
from the problem — absence is universal — it simply cannot make the check a compile-time
one, so the same guarantee has to be bought with discipline instead. The sentinel-plus-
channel form is what that discipline looks like when it is done deliberately rather than
by habit, and its two obligations are exactly the ones a compiler would otherwise have
carried: that every failing path sets the reason, and that the reason is read before
anything can clobber it. Treating that pairing as beneath mention is how a reader in such
a language concludes the card does not apply to them and takes nothing from it at all.

This establishes a pseudocode convention and a durable typing habit. Long frames nulls as straddling a dichotomy — genuinely useful for representing absence, genuinely dangerous because engineers forget to check them — and resolves it with compiler-enforced null safety or optionals rather than either raw nulls or an absolutist ban. It is the foundation that later error-signaling techniques, such as nullable and optional return types, build on when a function may be unable to produce a result.

Signalling failure is the same move used for a second purpose. Returning null under null safety forces the caller to acknowledge that no value was produced before using the result, so absence and failure share one compiler-enforced channel. The limit is that null conveys no reason — Long's square-root function returns null for a negative input and needs a comment to say what the null means, which is the signal that a result type would carry the information better. The technique is also weak in a language without null safety, where the return can be silently dereferenced and the caller is never forced to look.

---
name: software-engineering
description: >-
  Use for software design, implementation, review, debugging, refactoring,
  testing, contracts, readability, modularity, error handling, maintainability,
  and C++ work in this repository.
---

# Software Engineering

Use SkillForge's universal engineering core plus the relevant language module.

## Load order

1. `library/metaskills/INDEX.md`
2. `library/software-engineering/core/INDEX.md`
3. For C++, `library/software-engineering/languages/cpp/INDEX.md`
4. Follow object prerequisites and cross-links before applying a dependent card.

Retrieve only the APs, Patterns, and Drills relevant to the current engineering
decision. Inspect the existing code before changing it, make contracts and failure
modes explicit, and run the repository's actual checks before claiming success.

## Skillset Memory

`memory/software-engineering/` is the empirical record of what happened when this
canon was actually used — known weak areas, recurring misreadings, and the
boundary of what has been verified. It is not canon and never overrides a card.

Canon resolves first; memory is retrieved second and bounded. Query it before
acting, with short cues taken from the task's own words:

```bash
python PASS/tools/memory.py query --domain software-engineering --cues "cache,thread,review"
```

Cues match as substrings of an entry's recorded cues, so prefer several short
terms over one long phrase. Read what comes back as an observation carrying a
stated confidence, not as an instruction — an entry may be provisional, scoped to
one run, or since superseded.

Never copy an entry's content into a card, an index, or this file. An entry that
seems to apply on every turn has earned promotion review, not a paste; pasting
creates a second write site and lets the real owner decay unobserved.

## Write barrier

Reviewing code asks "what applies here?", so the library gets consulted. Writing
code asks nothing, so it does not. This barrier is the missing prompt. It governs
**producing** code; a review is owned by `AP_review_code_you_did_not_write`.

**Before writing or changing code in a source file, run this barrier in order.**

1. **Read the declarations and the call sites, not the names.** Open the actual
   signature of anything you are calling; a doc comment above a member is not the
   member. For a change to existing code, find who calls it before deciding what
   it may assume — the fact that decides whether a change is safe is routinely in
   a different file from the one being edited. **Assume nothing here is written
   the way you would write it.** A long-lived codebase is sediment from many
   people over many years: its brace style, its macro names, its ownership idioms
   and its spelling of standard calls are all to be discovered, not predicted.
   When searching it, go loose first and read what comes back to learn the
   conventions, then write the precise pattern — a search written against the form
   you expected returns a confident number rather than an error, and a wrong count
   is indistinguishable from a right one. Code that *does* look uniformly like
   your own output is evidence it was written by an agent, not evidence that you
   guessed correctly.
2. **Name what must never be false here, and how anyone would find out if it
   were.** If nothing would report it, that is the finding. A guard answers *what
   do I do when this is false*; an assertion answers *this should never be false*.
   The control flow asks the first question by itself. Nobody asks the second
   unless you do.
3. **State what you are assuming about the inputs, and from how many examples.**
   A format inferred from two samples is a guess. Either write the assumption
   down or go and check it.
4. **Before splitting work into helpers, ask what state crosses the seam.** Where
   both sides read or update the same working value — a mode, a position, a
   depth — the split distributes one state machine across two scopes, and each
   half then reads correctly while the pair is wrong. The tell is a helper whose
   parameters carry three or more values the caller still needs afterwards.
5. **Write it the way the surrounding code is written.** You have just read the
   file; use what you saw. Match its idiom for the things it has already decided
   — how it passes and returns, how it reports failure, how it allocates, what it
   names things. Code that is cleaner in isolation and different from everything
   around it is worse in place, because the difference reads as significant and
   is not. Your default idiom is not neutral; it is one house style meeting
   another, and the file was here first.
6. **Cut what does not earn its place.** Every variable you added is read
   somewhere. Every comment records a decision somebody actually made, rather
   than narrating the line beneath it or justifying a choice you invented. Every
   check can actually fire — one the boundary already made is cost without cover.
7. **Then write it, and say which steps you skipped and why.**

**Fail closed.** If step 1 cannot be answered, do not proceed on a guess about
what the code may assume — go and read it. An unresolved prerequisite is a stop,
not a reason to write carefully and hope.

These seven come from recorded failures in `memory/software-engineering/`, not
from first principles. When a new one is recorded, this list is where it lands; when an
item stops catching anything, it should be removed rather than kept for
completeness. A barrier long enough to skip is a barrier that gets skipped.

Do not load Art rules into ordinary engineering work. New language modules belong
under `library/software-engineering/languages/<language>/` and must not require
changes to unrelated languages.

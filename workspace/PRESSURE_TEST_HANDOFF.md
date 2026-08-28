# Handoff — pressure-test the library against real C++ codebases

Give this to a **fresh chat** with no prior context about this work. Hand over
this file's path, or paste its contents. One codebase per session.

---

## Why the chat must be cold

The point is to find out whether the **library** holds up against code nobody
wrote for it, not whether a conversation can be talked into agreeing that it
does. A session that has been told what earlier runs found will find those
things. Anything described in advance is removed from what is being tested.

This handoff therefore describes the method and says nothing about results.
That is deliberate.

**The running session must not read anything else in `workspace/`.**

---

## What is different about this material

Every previous check ran the library against code that was either constructed
for the occasion or taken from a teaching text. This is neither. These are large,
long-lived, multi-author codebases that ship and are actively maintained.

That changes what a finding means, and it is the single most important thing in
this handoff:

> **The code works. Where the library disagrees with it, that is a question about
> the library before it is a question about the code.**

Competent practitioners made these decisions under real constraints — platform
support, performance, backward compatibility, twenty years of history. When a
rule in the library says one thing and a working codebase does another, there are
three possibilities and they are worth separating: the code has a genuine defect
its authors have not hit yet; the rule is right but missing the condition that
makes this case an exception; or the rule is wrong. Do not assume the first.

---

## The two jobs

This run has two purposes and they are not the same shape. Do them in order, as
two passes over the same code, and keep their results apart.

**Pass one — hammer the cards against the code.** Review the slice using the
library. What fired, what should have fired and did not, what nothing names,
where the library and the code disagree. This is a search for defects in the
*library*, with the code as the instrument.

**Pass two — learn from the code.** Go back over the same slice asking what it
does *well*: technique worth carrying into your own work, a decision made better
here than you would have made it, a rule you hold that this code shows to be
stated wrongly or too crudely. This is a search for things the library is
missing or has slightly wrong, with the code as the teacher.

Pass two has to be separate and second, because a review protocol produces a
defect list by construction. Nothing in the ordinary flow of reviewing asks what
the code is better at than you are, so if you do not make it a deliberate second
pass over the same material, it does not happen.

### The check that makes pass two worth anything

Most of what you notice in pass two will already be in the library. That is not
a disappointment, it is the measurement — it tells you the canon reaches real
code. But it is also the failure mode: a session that lists admiring
observations without checking produces a page of things the library already
says, dressed up as discoveries.

So, for **every** technique you name in pass two:

- **Either** name the card that owns it — object id, quoted rule if it is close
  — and count it as covered.
- **Or** say what you searched for and did not find. Name the topics and indexes
  you looked in. Only then is it a gap.

An observation with neither is not reportable. Expect the covered pile to be the
larger one; report both counts, because the ratio is itself a result.

---

## Instructions for the running session

You are checking a skill library against a real codebase, and learning from that
codebase. Work in `D:\Repos\SkillForge`.

**Load the skill first.** Invoke the `software-engineering` skill and follow its
load order. Work out from the library itself how a review of this kind should be
conducted — that routing is part of what is being examined, so do not shortcut it
with your own general knowledge of code review.

**Read nothing else in `workspace/`.**

**Make no changes to the repository.** No commits, no edits to any card, drill or
protocol, no new files, no memory writes. If something needs fixing, put it in
the report. This applies to pass two as much as pass one: a technique worth
adopting is reported, never written into a card and never written into
`memory/`. Memory records what happened when the canon was used; a technique is
canon-shaped, and putting it in memory inverts the firewall.

### The codebase

```
<<< paste ONE path from the list below >>>
```

It is already extracted and ready to read. Nothing needs unpacking, and nothing
under `workspace/sources/` is tracked by git, so you cannot disturb the repository
by reading there.

### Pass one — what to do

1. **Choose your own slice.** Find a substantial, self-contained subsystem —
   enough code to have real structure, few enough files to read properly. Prefer
   something that does work over a leaf utility. Say what you chose and why, and
   give file paths so the choice can be checked.

2. **Review it using the library.** Retrieve and read the cards that apply.
   Consulting the library is the exercise.

3. **Report against four categories, kept separate:**

   - **Fired and helped.** A card, drill or protocol applied and produced a
     concrete, correct observation. Name it and the observation.
   - **Should have fired and did not.** The situation is genuinely present and
     either nothing routed you to the owner, or the owner's stated condition did
     not match though the situation was its subject. Name it, quote the
     condition, show the code.
   - **Nothing names it.** Something here is genuinely wrong or genuinely
     load-bearing and the library is silent. Say what you searched for.
   - **The library and the code disagree.** The guidance is clear, the code
     knowingly does otherwise, and the code works. State the rule, the code, and
     your best reconstruction of why competent authors chose as they did. This is
     the category this material exists to produce and the one to spend effort on.

4. **The distinction that decides whether a finding counts.** A rule being silent
   because its situation is *absent* is not a finding — no single subsystem
   exercises a whole library. Only a rule that should have applied and did not
   counts. For anything in categories two, three, or four, say why you believe
   the situation is genuinely present rather than adjacent.

5. **Report coverage.** Which regions of the library did this slice actually
   exercise, and which stayed silent because nothing here touched them? No single
   session covers the library; the sessions together sample it, and this is how
   that gets measured.

6. **Validity.** Was this a real test, or did it fail before the library was
   exercised — tree unreadable, code needing a build system you could not
   inspect, missing prerequisite, skill that would not load? Say so and say why.
   A run that failed for those reasons is evidence about tooling, never about the
   library.

7. **What you consulted.** Which objects you actually retrieved and read — not
   which exist, which ones you used.

### Pass two — what to do

Go back over the same slice. Do not go looking for new code; the point is that
the same material answers a different question.

8. **Report against three more categories, kept separate from each other and
   from pass one:**

   - **Already owned.** A technique the code uses well that the library already
     covers. Name the card. One line each is enough. Report the count.
   - **Not owned.** A reusable decision this code makes, that recurs in real work,
     and that no object in the library owns. Say what you searched for. Say what
     the decision is in general terms, not just what this code did — if you cannot
     state it without naming this codebase, it is not yet a candidate.
   - **The library's version is worse.** A card is right in direction, but this
     code's form of the same idea is better, and someone applying the card as
     written would produce the inferior version. State both forms. This is
     distinct from a disagreement: nobody is contradicting anybody, the card is
     just coarser than the practice.

9. **Where you misread your own library.** Points during either pass where a card
   was correct and you nearly drew the wrong conclusion from it — an escape clause
   you read as permission, an option list you took as exhaustive, a rule you were
   about to apply from a diff-sized view without asking what the boundary was.
   Nobody volunteers this and it is worth more than most of the rest, because it
   separates a defect in the guidance from a defect in reading the guidance. The
   two get fixed in completely different places.

### Then, on the experience of using the library

- Where did you fall back on your own knowledge because the library offered
  nothing?
- Did any guidance turn out to be wrong, or actively unhelpful, for this code?
- Was anything you were routed to written for code of a different scale or
  character, in a way that made it hard to apply?
- Did any two pieces of guidance give opposite readings of the same code?

Write the report out in full — only what you report is seen.

---

## The codebases — one per session

```
workspace/sources/Cpp/extracted/DevilutionX-master     ( 31 MB)   DONE — do not re-run
workspace/sources/Cpp/extracted/warzone2100-master     ( 75 MB)
workspace/sources/Cpp/extracted/freeorion-master       (202 MB)
workspace/sources/Cpp/extracted/endless-sky-master     (408 MB)
workspace/sources/Cpp/extracted/wesnoth-master         (1.2 GB)
workspace/sources/Cpp/extracted/gemrb-master           (28.5 MB)
```

These are working trees, not archives. Explore with the ordinary tools —
`find`, `grep`, directory listings — and read whatever you decide to read.

**One codebase per fresh session.** They are different enough in age, style and
subject matter to be genuinely independent samples, and a session that has read
one is no longer cold for another.

Order does not matter among the remaining five. Note in each report which
codebase it was.

---

## What happens with the results

Bring the reports back. Nothing is committed, pushed, or written to memory from
the running sessions.

Findings sort into four kinds and they are not interchangeable:

- **Guidance defects** — a condition too narrow, a rule that certifies something
  it should refuse, two rules contradicting each other. Fixed in the object.
  Watch the clauses rather than the rules: an `IF` and a `THEN` can both be right
  while the `ELSE`, or an option list, quietly says the rule does not apply here.
- **Genuine gaps** — a decision that recurs in real code and has no owner. Under
  hard rule 15 a missing reusable decision may justify a Pattern and a missing
  reusable orchestration may justify a protocol; retrieval, routing and interface
  failures justify neither and are attributed to whatever actually failed.
- **Disagreements** — the library says one thing and working code does another.
  These are the most valuable and the slowest to act on, because resolving one
  means deciding whether the rule was wrong or merely unconditioned. Do not
  resolve them from a single sample.
- **Reading failures** — the guidance was right and the session nearly got it
  wrong anyway. These belong in `memory/software-engineering/`, not in a card.
  An entry there is provisional and scoped to what one run saw; if the same
  misreading recurs across sessions, that stops being a fact about the reader and
  becomes a claim about how the cards are written.

An invalid run is evidence about none of the above.

A gap found in one codebase is a candidate, not a Pattern. Five codebases remain;
a decision that shows up in three of them has earned authoring, and one that
shows up once has earned a note and a wait.

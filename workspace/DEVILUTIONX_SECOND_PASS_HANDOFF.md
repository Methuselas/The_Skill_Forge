# Handoff — second pass on DevilutionX, aimed at the regions the first pass missed

Give this to a **fresh chat** with no prior context about this work. Hand over
this file's path, or paste its contents.

This is a companion to `PRESSURE_TEST_HANDOFF.md` and uses the same method. The
running session needs only this file.

---

## Why the chat must be cold, and where this one is different

The point is to find out whether the **library** holds up against code nobody
wrote for it, not whether a conversation can be talked into agreeing that it
does. A session told what an earlier run found will find those things. So this
handoff describes the method and says nothing about results.

One thing is deliberately different here, and it costs something. The first pass
on this codebase let the session pick its own slice, which tested routing as well
as content: *does the library reach the code you happen to be holding?* This pass
names the regions to exercise instead, because a whole area of the library went
untouched and the sessions together are supposed to sample it.

**The consequence, stated so nobody claims otherwise later:** this run cannot be
evidence that the library routes a reviewer to the right place, because the
destination was supplied. It can be evidence about whether the guidance, once
reached, is any good. Say so in your report.

**The running session must not read anything else in `workspace/`** — including
`PRESSURE_TEST_HANDOFF.md`.

---

## What is different about this material

These are not constructed examples or textbook code. DevilutionX is a large,
long-lived, multi-author codebase that ships and is actively maintained.

> **The code works. Where the library disagrees with it, that is a question about
> the library before it is a question about the code.**

Competent practitioners made these decisions under real constraints — platform
support, performance, backward compatibility, decades of history. When a rule in
the library says one thing and a working codebase does another, there are three
possibilities worth separating: the code has a genuine defect its authors have
not hit yet; the rule is right but missing the condition that makes this case an
exception; or the rule is wrong. Do not assume the first.

Read the tree's own `README.md` and `docs/` early. What this project *is*
determines what kinds of decision appear in it, and some of those are decisions
most codebases never have to make. Work out what those are from the material
rather than from a list supplied here.

---

## The two jobs

Two purposes, two passes over the same code, results kept apart.

**Pass one — hammer the cards against the code.** Review the slice using the
library. A search for defects in the *library*, with the code as the instrument.

**Pass two — learn from the code.** Go back over the same slice asking what it
does *well*: technique worth carrying into your own work, a decision made better
here than you would have made it, a rule you hold that this code shows to be
stated too crudely. A search for what the library is missing, with the code as
the teacher.

Pass two must be separate and second. A review protocol produces a defect list by
construction; nothing in the ordinary flow of reviewing asks what the code is
better at than you are, so unless it is a deliberate second pass it does not
happen.

### The check that makes pass two worth anything

Most of what you notice in pass two will already be in the library. That is the
measurement, not a disappointment — it says the canon reaches real code. It is
also the failure mode: admiring observations that turn out to be things the
library already says, presented as discoveries.

For **every** technique you name in pass two:

- **Either** name the card that owns it — object id, and the quoted rule if it is
  close — and count it as covered.
- **Or** say what you searched for and did not find: which topics, which indexes.
  Only then is it a gap.

An observation with neither is not reportable. Report both counts; the ratio is a
result.

---

## Instructions for the running session

You are checking a skill library against a real codebase, and learning from that
codebase. Work in `D:\Repos\SkillForge`.

**Load the skill first.** Invoke the `software-engineering` skill and follow its
load order.

**Read nothing else in `workspace/`.**

**Make no changes to the repository.** No commits, no edits to any card, drill or
protocol, no new files, no memory writes. If something needs fixing, put it in
the report. This holds for pass two as much as pass one: a technique worth
adopting is reported, never written into a card and never into `memory/`. Memory
records what happened when the canon was used; a technique is canon-shaped, and
putting it there inverts the firewall.

### The codebase

```
workspace/sources/Cpp/extracted/DevilutionX-master
```

Already extracted. Nothing under `workspace/sources/` is tracked by git, so you
cannot disturb the repository by reading there.

### Choosing the slice

`Source/dvlnet/` has already been reviewed by another session. **Do not choose
it**, and do not read it for context — if you find yourself there, you are
re-running work that is done.

Choose enough code to have real structure and few enough files to read properly,
weighted toward the three areas below. One slice that covers two of them is
better than three thin ones. Say what you chose, why, and give file paths.

1. **A measured hot path.** Code whose shape was chosen for speed, together with
   whatever the project uses to decide that it is fast. The build tooling and the
   `docs/` are part of this area, not separate from it — how a project measures is
   as much a decision as what it optimises.

2. **The test tree.** `test/`, and whatever machinery under `Source/` exists to
   make the program testable. Ask what has to be true of a program before a test
   like this can exist at all, and whether the library says how to get there.

3. **Whatever this project has to do that ordinary projects do not.** The README
   and `docs/` will tell you what kind of project it is. That fact forces a class
   of decision on the code. Find where it bites and how it was handled.

These are named because the first pass left the corresponding library regions
unexercised. They are not a list of findings and nothing is being hinted at.

### Pass one — report against four categories, kept separate

- **Fired and helped.** A card, drill or protocol applied and produced a concrete,
  correct observation. Name it and the observation.
- **Should have fired and did not.** The situation is genuinely present and either
  nothing routed you to the owner, or the owner's stated condition did not match
  though the situation was its subject. Name it, quote the condition, show the
  code.
- **Nothing names it.** Something here is genuinely wrong or genuinely
  load-bearing and the library is silent. Say what you searched for.
- **The library and the code disagree.** The guidance is clear, the code knowingly
  does otherwise, and the code works. State the rule, the code, and your best
  reconstruction of why competent authors chose as they did.

**The distinction that decides whether a finding counts.** A rule being silent
because its situation is *absent* is not a finding. Only a rule that should have
applied and did not counts. For categories two, three and four, say why the
situation is genuinely present rather than adjacent.

### Pass two — report against three more categories

- **Already owned.** A technique the code uses well that the library covers. Name
  the card. One line each. Report the count.
- **Not owned.** A reusable decision this code makes, that recurs in real work,
  and that no object owns. Say what you searched for, and state the decision in
  general terms — if you cannot state it without naming this codebase, it is not
  yet a candidate.
- **The library's version is worse.** A card is right in direction, but this
  code's form of the same idea is better, and someone applying the card as written
  would produce the inferior version. State both forms. Distinct from a
  disagreement: nobody contradicts anybody, the card is just coarser than the
  practice.

### Then

- **Where you misread your own library.** Points during either pass where a card
  was correct and you nearly drew the wrong conclusion — an escape clause read as
  permission, an option list taken as exhaustive, a rule applied from a diff-sized
  view without asking what the boundary was. Nobody volunteers this and it is
  worth more than most of the rest, because a defect in the guidance and a defect
  in reading the guidance get fixed in completely different places.
- **Coverage.** Which regions of the library this slice exercised, and which
  stayed silent because nothing here touched them.
- **Validity.** Was this a real test, or did it fail before the library was
  exercised — tree unreadable, code needing a build you could not run, missing
  prerequisite, skill that would not load? A run that failed for those reasons is
  evidence about tooling, never about the library. Note also that this run's slice
  was directed rather than chosen, so it proves nothing about routing.
- **What you consulted.** Which objects you actually retrieved and read — not
  which exist, which ones you used.
- **On the experience.** Where did you fall back on your own knowledge because the
  library offered nothing? Was any guidance wrong or unhelpful here? Was anything
  written for code of a different scale or character? Did any two pieces of
  guidance give opposite readings of the same code?

Write the report out in full — only what you report is seen.

---

## A note on running the code

Some of this material — benchmarks especially — is meaningful partly through
being run. You are not required to build anything, and a report from reading
alone is a valid result. If you do try to build, treat a failure as a fact about
tooling and say so; it is not a finding about the library, and it does not
invalidate the reading you did before it.

---

## What happens with the results

Bring the report back. Nothing is committed, pushed, or written to memory from
the running session.

Findings sort into four kinds:

- **Guidance defects** — a condition too narrow, a rule that certifies something
  it should refuse, two rules contradicting each other. Fixed in the object. Watch
  the clauses rather than the rules: an `IF` and a `THEN` can both be right while
  the `ELSE`, or an option list, quietly says the rule does not apply here.
- **Genuine gaps** — a decision that recurs in real code and has no owner. Under
  hard rule 15 a missing reusable decision may justify a Pattern and a missing
  reusable orchestration may justify a protocol; retrieval, routing and interface
  failures justify neither.
- **Disagreements** — the library says one thing and working code does another.
  The most valuable and the slowest to act on. Not resolvable from one sample.
- **Reading failures** — the guidance was right and the session nearly got it
  wrong anyway. These belong in `memory/software-engineering/`, not in a card.

A gap found in one codebase is a candidate, not a Pattern.

An invalid run is evidence about none of the above.

# Handoff — pressure-test the library against real C++ codebases

Give this to a **fresh chat** with no prior context about this work. Hand over
this file's path, or paste its contents. One archive per session.

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

## Instructions for the running session

You are checking a skill library against a real codebase. Work in
`D:\Repos\SkillForge`.

**Load the skill first.** Invoke the `software-engineering` skill and follow its
load order. Work out from the library itself how a review of this kind should be
conducted — that routing is part of what is being examined, so do not shortcut it
with your own general knowledge of code review.

**Read nothing else in `workspace/`.**

**Make no changes to the repository.** No commits, no edits to any card, drill or
protocol, no new files, no memory writes. If something needs fixing, put it in
the report.

### The archive

```
<<< paste ONE path from the list below >>>
```

Extract to your scratchpad, not into the repository. **Wesnoth in particular is
large — browse with `unzip -l` and extract only the subtree you intend to read**
rather than unpacking the whole archive.

### What to do

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
   exercised — archive unreadable, code needing a build system you could not
   inspect, missing prerequisite, skill that would not load? Say so and say why.
   A run that failed for those reasons is evidence about tooling, never about the
   library.

7. **What you consulted.** Which objects you actually retrieved and read — not
   which exist, which ones you used.

### Then, on the experience of using the library

- Where did you fall back on your own knowledge because the library offered
  nothing?
- Did any guidance turn out to be wrong, or actively unhelpful, for this code?
- Was anything you were routed to written for code of a different scale or
  character, in a way that made it hard to apply?
- Did any two pieces of guidance give opposite readings of the same code?

Write the report out in full — only what you report is seen.

---

## The four archives — one per session

```
workspace/sources/Cpp/DevilutionX-master.zip      (12 MB)
workspace/sources/Cpp/warzone2100-master.zip      (25 MB)
workspace/sources/Cpp/freeorion-master.zip        (161 MB)
workspace/sources/Cpp/wesnoth-master.zip          (730 MB — extract selectively)
```

**One archive per fresh session.** They are different enough in age, style and
subject matter to be genuinely independent samples, and a session that has read
one is no longer cold for another.

Order does not matter. Note in each report which archive it was.

---

## What happens with the results

Bring the reports back. Nothing is committed, pushed, or written to memory from
the running sessions.

Findings sort into three kinds and they are not interchangeable:

- **Guidance defects** — a condition too narrow, a rule that certifies something
  it should refuse, two rules contradicting each other. Fixed in the object.
- **Genuine gaps** — a decision that recurs in real code and has no owner. Under
  hard rule 15 a missing reusable decision may justify a Pattern and a missing
  reusable orchestration may justify a protocol; retrieval, routing and interface
  failures justify neither and are attributed to whatever actually failed.
- **Disagreements** — the library says one thing and working code does another.
  These are the most valuable and the slowest to act on, because resolving one
  means deciding whether the rule was wrong or merely unconditioned. Do not
  resolve them from a single sample.

An invalid run is evidence about none of the above.

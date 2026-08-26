# Handoff — run the one concurrency drill that has never been run

Give this to a **fresh chat** with no prior context about this work. Hand over
this file's path, or paste its contents. Do not summarise the drill before
handing it over, and do not answer questions about the material while the run is
in progress.

---

## Why the chat must be cold

The point is to find out whether the **cards** carry the capability, not whether
a conversation does. A session that has been told what a drill is about measures
the telling. Anything explained in advance is removed from what is being tested.

This handoff therefore names one drill and says nothing about what it teaches.
That is deliberate.

---

## Instructions for the running session

You are running one practice drill against a skill library. Work in
`D:\Repos\SkillForge`.

**Load the skill first.** Invoke the `software-engineering` skill and follow its
load order. Retrieve cards as the drill requires them — consulting the library is
part of the exercise, not cheating.

**Read nothing in `workspace/` other than this file.** There is material there
from earlier work on these drills, including full reports on neighbouring cards.
A session that reads any of it is no longer cold. Do not list the directory; do
not open any other file in it. Everything you need is named by full path below.

**Finding a card.** Every topic's `INDEX.md` lists the objects in that topic by
name, filename, object type, stage binding, and tags. A parent directory that
holds no cards of its own lists only its child topics and their counts, so
descend to the topic index rather than reading the parent as if it were one. To
locate a card from an object ID or a keyword anywhere in the library:

```
grep -rn "<object_id or keyword>" --include=INDEX.md library/
```

Cards are tagged across topic boundaries, so a card relevant to concurrency may
live under another topic and still be reachable by tag.

**Make no changes to the repository.** No commits, no edits to any card or
drill, no new files, no memory store. If something seems to need fixing, write it
in the report instead. Report in the chat; do not write a file.

**Run this drill, exactly as written in its own file:**

```
library/software-engineering/languages/cpp/concurrency/
  DRILL_restructure_a_class_that_locks_every_member.md
```

The drill states a Practice Task, Instructions, a Success Check, and Common
Failures. Follow the Instructions in order. Where it says to construct an
example, construct one — do not describe what you would construct. Write the
actual C++; a description of the restructuring is not the restructuring.

**Report:**

1. **The work itself.** The actual artifact — the class before, the class after,
   and the reasoning that moved each member. Not a summary of it.
2. **Success Check.** Each bullet, met or not met, individually.
3. **Common Failures.** Which, if any, occurred. Answer honestly; a drill that
   catches a failure has done its job, and a report with none is less useful than
   one with some.
4. **Validity.** Was this a genuine test of the capability, or did it fail before
   the capability was exercised — a file that could not be read, a missing
   prerequisite, an ambiguous instruction, a session limit? If the latter, say so
   and say why. An invalid run is evidence about the drill or the tooling, never
   about the craft.
5. **What you consulted.** Which cards you actually retrieved and read. Not which
   ones exist — which ones you used. Note whether each came from
   `languages/cpp/` or from `core/`.

**Then, on the drill itself:**

- Was any instruction ambiguous, circular, self-contradictory, or impossible to
  follow as written?
- **Could any Success Check bullet be satisfied without doing the work?** Try to
  break each one: is there a wrong, incomplete, or merely restated answer that
  still passes it? Say so explicitly for each bullet, including the ones you
  think are sound.
- **Could any bullet fail work that is correct?** The inverse matters as much.
  A bullet written against one anticipated remedy will reject a better answer
  that took another route; look for that specifically.
- Did the drill require knowledge the library does not contain, and if so what
  was missing? Distinguish knowledge missing from the C++ track from knowledge
  missing from `core/`.
- Did any step leave a quantity, unit, or scale unstated, such that two correct
  runs could produce different numbers?

---

## Verify a gap before you report one

If you are about to report that the library lacks something, that a card is
unreachable, or that an index is missing information — check it first, with the
grep above, and say in the report what you ran. An earlier session reported a
navigation defect that did not exist, having read a parent index instead of the
topic index. A wrong finding of this kind is more expensive than a missing one,
because it gets acted on.

---

## Budget

This drill produces real code and the last attempt at it did not finish. Get the
restructured class written before spending effort on the critique sections — the
work itself is the part that cannot be reconstructed afterwards, and a report
with the artifact and half the critique is worth more than a full critique of
work that was never done. If you are running out of room, say where you stopped
rather than compressing the artifact.

---

## For the operator, not for the running session

Context that would not spoil the run but is not needed by it.

- **This is the eighth of eight drills.** The other seven were run cold on
  2026-08-25 and produced valid runs; this one was terminated by an
  account-level usage limit partway through constructing the restructured class,
  and under hard rule 17 that is an invalid run — it says nothing about the C++
  lane. Start it when there is room to finish it.
- **Do not tell the session that the other seven were run**, or that their
  findings were acted on. It is running the drill, not auditing a repair.
- **The seven core drills were revised on 2026-08-26** in response to those
  reports. This C++ drill was **not** touched, because it produced no findings —
  so its instructions and Success Check are still in their original state, and
  the defect families the other seven showed (checks satisfiable without doing
  the work, checks that reject correct answers, unstated quantities) have not
  been looked for here at all. That is the main reason this run is worth having.
- **What comes back is triaged the same way as before.** Defects in the drill are
  fixed in the drill and say nothing about the craft. A clean run that still
  produced a wrong answer is evidence about the canon, and under hard rule 15
  justifies authoring only a missing reusable decision (a Pattern) or a missing
  reusable orchestration (an AP).
- **`memory/software-engineering/` still does not exist** and
  `memory.py append --domain software-engineering` will fail rather than create
  it, because `domain_dirs()` only returns directories that already contain
  `skill_memory.yaml`. That is deliberate. It should be created by the first run
  that produces an admissible event, not in anticipation of one.
- **Still open after this:** G1 (the two-term communication cost model) and G2
  (surface-to-volume), both held in `workspace/DRILL_DEFECTS.md` Part 5a pending
  a second confirming run before anything is authored.

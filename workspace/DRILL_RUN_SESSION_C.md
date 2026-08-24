# Handoff — Session C of the concurrency drill run

Give this to a **fresh chat** with no prior context about this work. Hand over
this file's path, or paste its contents. Do not summarise the drills before
handing it over, and do not answer questions about the material while the run
is in progress.

---

## Why the chat must be cold

The point of the run is to find out whether the **cards** carry the capability,
not whether a conversation does. A session that has been told what the drills
are about measures the telling. Anything explained in advance is removed from
what is being tested.

This handoff therefore names the drills and says nothing about what they teach.
That is deliberate, not an oversight.

---

## Do not read the other reports

Two earlier sessions ran the other six drills and wrote reports into
`workspace/`. Those reports set out in detail what several neighbouring cards
say — including cards these two drills depend on. Reading one would remove from
the test exactly what the test is for.

- **Do not list `workspace/`.** Everything you need is named by full path below.
- **Do not open** `DRILL_RUN_SESSION_A_REPORT.md`, `DRILL_RUN_SESSION_B_REPORT.md`,
  or `DRILL_RUN_HANDOFF.md`.
- Write your report to the one exact path named below, and touch nothing else in
  that directory.

---

## Instructions for the running session

You are running practice drills against a skill library. Work in
`D:\Repos\SkillForge`.

**Load the skill first.** Invoke the `software-engineering` skill and follow its
load order. Retrieve cards as the drills require them — consulting the library
is part of the exercise, not cheating.

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

**Make no changes to the repository.** No commits. No edits to any card, drill,
tool, or index. No memory store. If something seems to need fixing, write it in
the report instead.

**One exception**, overriding the rule above: write your report to exactly

```
D:\Repos\SkillForge\workspace\DRILL_RUN_SESSION_C_REPORT.md
```

**Run these two drills, each exactly as written in its own file, in this order:**

```
1. library/software-engineering/core/concurrency/
     DRILL_fold_an_unsafe_interface_into_transactions.md

2. library/software-engineering/core/concurrency/
     DRILL_decide_whether_a_primitive_can_coordinate_the_design.md
```

Each drill states a Practice Task, Instructions, a Success Check, and Common
Failures. Follow the Instructions in order. Where a drill says to construct an
example, construct one — do not describe what you would construct.

**For each drill, report:**

1. **The work itself.** The actual artifact — the classification, the
   restructured interface, the counts, the verdict. Not a summary of it.
2. **Success Check.** Each bullet, met or not met, individually.
3. **Common Failures.** Which, if any, occurred. Answer honestly; a drill that
   catches a failure has done its job, and a report with none is less useful
   than one with some.
4. **Validity.** Was this a genuine test of the capability, or did it fail
   before the capability was exercised — a file that could not be read, a
   missing prerequisite, an ambiguous instruction? If the latter, say so and
   say why. An invalid run is evidence about the drill or the tooling, never
   about the craft.
5. **What you consulted.** Which cards you actually retrieved and read. Not
   which ones exist — which ones you used.

**Then, across both:**

- Any drill whose Instructions were ambiguous, circular, or impossible to
  follow as written.
- Any drill where the Success Check could be satisfied without doing the work.
- Any drill that required knowledge the library does not contain, and what was
  missing.

---

## Verify a gap before you report one

If you are about to report that the library lacks something, that a card is
unreachable, or that an index is missing information — check it first, with the
grep above, and say in the report what you ran. An earlier session reported a
navigation defect that did not exist, having read a parent index instead of the
topic index. A wrong finding of this kind is more expensive than a missing one,
because it gets acted on.

This instruction is new for Session C. Earlier sessions did not have it, so
their retrieval experience is not comparable to yours.

---

## Position

Record both drills' position in the session: drill 1 is position 1 and genuinely
cold; drill 2 is position 2 and its result is weaker evidence by that much. Note
in the report whether the two shared any underlying idea you noticed.

---

## Skillset Memory

The Skillset Memory store for this domain does not exist, and
`memory.py append --domain software-engineering` will fail rather than create
it — `domain_dirs()` only returns directories that already contain
`skill_memory.yaml`. Do not create it. That is a deliberate decision to make
later, not a side effect of a drill run.

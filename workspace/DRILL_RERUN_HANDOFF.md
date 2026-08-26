# Handoff — re-run the concurrency drills

Give this to a **fresh chat** with no prior context about this work. Hand over
this file's path, or paste its contents. Do not summarise the drills before
handing it over, and do not answer questions about the material while a run is
in progress.

---

## Why the chat must be cold

The point is to find out whether the **cards** carry the capability, not whether
a conversation does. A session that has been told what a drill is about measures
the telling. Anything explained in advance is removed from what is being tested.

This handoff therefore names one drill and says nothing about what it teaches.
That is deliberate.

**One additional rule this time: the running session must not read anything in
`workspace/`.** There is material there from earlier work on these drills, and a
session that reads it is no longer cold. `workspace/` is scratch and nothing in
it is needed to run a drill.

---

## Instructions for the running session

You are running one practice drill against a skill library. Work in
`D:\Repos\SkillForge`.

**Load the skill first.** Invoke the `software-engineering` skill and follow its
load order. Retrieve cards as the drill requires them — consulting the library is
part of the exercise, not cheating.

**Read nothing in `workspace/`.**

**Make no changes to the repository.** No commits, no edits to any card or drill,
no new files, no memory store. If something seems to need fixing, write it in the
report instead.

**Run this drill, exactly as written in its own file:**

```
<<< paste ONE path from the list below >>>
```

The drill states a Practice Task, Instructions, a Success Check, and Common
Failures. Follow the Instructions in order. Where it says to construct an
example, construct one — do not describe what you would construct.

**Report:**

1. **The work itself.** The actual artifact — the classification, the
   restructured interface, the counts, the verdict. Not a summary of it.
2. **Success Check.** Each bullet, met or not met, individually.
3. **Common Failures.** Which, if any, occurred. Answer honestly; a drill that
   catches a failure has done its job, and a report with none is less useful than
   one with some.
4. **Validity.** Was this a genuine test of the capability, or did it fail before
   the capability was exercised — a file that could not be read, a missing
   prerequisite, an ambiguous instruction? If the latter, say so and say why. An
   invalid run is evidence about the drill or the tooling, never about the craft.
5. **What you consulted.** Which cards you actually retrieved and read. Not which
   ones exist — which ones you used.

**Then, on the drill itself:**

- Was any instruction ambiguous, circular, self-contradictory, or impossible to
  follow as written?
- **Could any Success Check bullet be satisfied without doing the work?** Try to
  break each one: is there a wrong, incomplete, or merely restated answer that
  still passes it? Say so explicitly for each bullet, including the ones you
  think are sound.
- **Could any bullet fail work that is correct?** The inverse matters as much.
- Did the drill require knowledge the library does not contain, and if so what
  was missing?
- Did any step leave a quantity, unit, or scale unstated, such that two correct
  runs could produce different numbers?

---

## The eight drills — one per session

```
library/software-engineering/core/concurrency/
  DRILL_name_the_committing_step_on_every_path.md
  DRILL_classify_the_dependencies_in_a_loop.md
  DRILL_fold_an_unsafe_interface_into_transactions.md
  DRILL_replace_value_validation_with_a_version_stamp.md
  DRILL_run_the_decomposition_procedure_on_a_problem.md
  DRILL_decide_whether_a_primitive_can_coordinate_the_design.md
  DRILL_trace_divergence_and_coalescing_from_an_index_mapping.md

library/software-engineering/languages/cpp/concurrency/
  DRILL_restructure_a_class_that_locks_every_member.md
```

**One drill per fresh session — eight sessions.** Not a suggestion this time.
Several of these turn on the same underlying move from different directions, and
grouping them is what weakened the previous evidence: a session that has done one
is no longer cold for another, and later results within a session are worth less
than earlier ones. Eight sessions is the only arrangement with no position
effects to discount.

Order does not matter across sessions. Note in each report which drill it was.

---

## What is being tested, and it is two things

Keep these separate in your own reading of the reports; the running sessions do
not need to know the distinction exists.

**Do the instruments behave?** Ambiguous instructions, checks satisfiable without
working, checks that fail correct work, and unstated quantities are defects in
the drill. They are fixed in the drill, and they say nothing about the craft.

**Do the cards carry the capability?** A drill that ran cleanly and still
produced a wrong answer is evidence about the canon. Under hard rule 15 that
justifies authoring only where the gap is a missing reusable decision, which is a
Pattern, or a missing reusable orchestration, which is an AP. Retrieval,
application, continuity, reference, tool, and interface failures justify nothing
and are attributed to whatever actually failed.

An invalid run — hard rule 17 — is evidence about neither. It stays in the record
and counts toward no craft weakness.

---

## What happens with the results

Bring the reports back. Nothing is committed, pushed, or written to memory from
the drill sessions.

`memory/software-engineering/` still does not exist, and
`memory.py append --domain software-engineering` will fail rather than create it,
because `domain_dirs()` only returns directories that already contain
`skill_memory.yaml`. That is deliberate. The store should be created by the first
run that produces an admissible event — a real result about a real capability —
and not in anticipation of one. If these eight sessions produce only drill
defects, the correct outcome is that the store still does not exist.

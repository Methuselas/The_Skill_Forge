# Handoff — run the concurrency drills

Give this to a **fresh chat** with no prior context about this work. Do not
summarise the drills before handing it over, and do not answer questions about
the material while the run is in progress.

---

## Why the chat must be cold

The point of the run is to find out whether the **cards** carry the capability,
not whether a conversation does. A session that has been told what the drills
are about measures the telling. Anything explained in advance is removed from
what is being tested.

This handoff therefore names the drills and says nothing about what they teach.
That is deliberate, not an oversight.

---

## Instructions for the running session

You are running practice drills against a skill library. Work in
`D:\Repos\SkillForge`.

**Load the skill first.** Invoke the `software-engineering` skill and follow its
load order. Retrieve cards as the drills require them — consulting the library
is part of the exercise, not cheating.

**Make no changes to the repository.** No commits, no edits to any card, no new
files, no memory store. If something seems to need fixing, write it in the
report instead.

**Run these eight drills, each exactly as written in its own file:**

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

**Then, across all eight:**

- Any drill whose Instructions were ambiguous, circular, or impossible to
  follow as written.
- Any drill where the Success Check could be satisfied without doing the work.
- Any drill that required knowledge the library does not contain, and what was
  missing.

---

## How to sequence the runs

Cleanest is **one drill per fresh session** — eight sessions. Some of these
drills share underlying ideas, so a session that has done one is no longer cold
for another, and later results in a session are weaker evidence than earlier
ones.

If eight sessions is too many, this grouping keeps the most closely related
drills apart:

- **Session A** — name the committing step; classify the dependencies;
  restructure the class that locks every member
- **Session B** — replace value validation; run the decomposition procedure;
  trace divergence and coalescing
- **Session C** — fold the unsafe interface; decide whether a primitive can
  coordinate

Note in the report which session each drill ran in and its position within that
session, so the weaker results can be read as weaker.

---

## What happens with the results

Bring the reports back. Nothing is committed, pushed, or written to memory from
the drill sessions.

Two separate decisions follow, and they should not be conflated:

- **Do the drills hold up?** Ambiguous instructions, satisfiable-without-working
  Success Checks, and missing prerequisites are defects in the drills, and they
  get fixed before the drill commit is pushed.
- **What did the runs reveal about the cards?** A drill run cleanly that still
  produced a wrong answer is evidence about the canon. Under hard rule 15 that
  only justifies authoring where the gap is a missing reusable decision, which
  is a Pattern, or a missing reusable orchestration, which is an AP. Retrieval,
  application, continuity, reference, tool, and interface failures justify
  nothing and are attributed to whatever actually failed.

The Skillset Memory store for this domain does not exist yet, and
`memory.py append --domain software-engineering` will fail rather than create
it — `domain_dirs()` only returns directories that already contain
`skill_memory.yaml`. Creating it is a deliberate decision to make after there is
something admissible to put in it, not a side effect of the first run.

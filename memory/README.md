# Skillset Memory

Empirical state: what actually happened when the canon was used.

```text
memory/
    art/
        skill_memory.yaml        compact current state, the file a runtime loads
        training_history.jsonl   the events it was consolidated from
```

One directory per domain, named for its `library/` package. Domains stay
independent here exactly as they do in the library — there is no shared or
global memory, and adding a domain does not touch its siblings.

The contract is **`PASS/docs/MEMORY_SCHEMA.md`**. Read it before adding
anything. The short version:

- **Memory is not canon.** It never mutates a card and is never copied into one.
  An observation that seems to apply on every turn has earned promotion review,
  not a paste.
- **An invalid run is never evidence about a capability.** A run that failed
  before the capability was exercised stays in history with a reason, attributed
  to the tool, controller, or package that actually failed.
- **Presence is not consultation.** Nothing here guarantees an entry is read.
  `memory.py query` prints what it returned so a run can record what was
  actually consulted; absent that, consultation is unproven.
- **A write is not persisted until the target is reopened and confirmed.**
  `append` and `compact` read back and fail loudly if the state is not there.
- **Temporary state is not memory.** Workflow position, reading progress,
  candidate status, recent artifacts, ambient context: none of it belongs here.
  The generalized lesson such state reveals may.

## Tool

```bash
python PASS/tools/memory.py validate                          # shape, vocabularies, admissibility
python PASS/tools/memory.py query --domain art --cues hand    # bounded retrieval
python PASS/tools/memory.py append --domain art --task "..."  # one event, verified by readback
python PASS/tools/memory.py compact --domain art              # events awaiting consolidation
python PASS/tools/memory.py review --domain art               # what needs revalidating
```

The tool is mechanical. It checks shape, retrieves a bounded set, appends an
event, links evidence, and reports what looks stale. It never judges whether an
artifact was good and never writes an observation for you: consolidating several
events into one honest sentence is a judgment, and a script that guessed at it
would be inventing empirical claims.

## Deleting this directory

Nothing breaks. `library/` validates with `memory/` absent, and a test enforces
that. Memory is the record of using the canon, not a dependency of it.

## Seeding

An empty valid store beats a populated contaminated one. There is no requirement
to fill this in. The Art store is seeded with three craft observations from
pre-Memory practical runs; controller, tool, and packaging failures from the same
period are deliberately absent, because those were never tests of craft.

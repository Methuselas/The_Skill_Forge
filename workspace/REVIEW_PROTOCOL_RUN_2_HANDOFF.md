# Handoff — second review-protocol run, fresh chat

**Repo:** `D:\Repos\SkillForge`
**Mechanics:** in `workspace/REVIEW_PROTOCOL_RUN_HANDOFF.md`. Read that file for the protocol,
the memory query, the toolchain invocations and the report format. This file adds only what
has changed since it was written, so nothing is restated in two places.

## What is different this time

`AP_review_code_you_did_not_write` is unchanged, but the lane's memory is not. An entry now
exists that is expected to fire during a review. **It is deliberately not described here.**
Retrieve it the way the protocol says, with cues from your own task, and report which ids came
back and whether any of them actually changed what you did. A handoff that quotes the entry
destroys the only thing this run measures, which is whether retrieval works without being told.

Add `--cues` drawn from whatever you end up looking at, beyond the two the mechanics file gives.

## Do not review these

Already reviewed; pick something else:

```
endless-sky/source/Account.{h,cpp}              (twice)
freeorion/Empire/ResearchQueue.{h,cpp}
pydantic/_internal/_utils.py
```

Prefer a language the cards were not written from. The lane's origins are C++ and statically
typed, so Go, Rust and Python stress it hardest — `Go/prometheus`, `Rust/ripgrep`,
`Python/pydantic` are all present under `workspace/sources/`. Choose the slice freely rather
than hunting for somewhere you suspect is weak; how it was chosen changes what step 8 returns.

## State you are starting from

`validate.py` PASS across 1446 objects. `memory.py validate` PASS across 4 stores, 26 entries,
76 events. Suite OK, 110 tests, roughly 225s. Run all three before starting and stop if any is
already red.

`SE_EV_0036` is **awaiting consolidation on purpose.** It records one sitting in which three
drills were taken blind and graded, and one sitting is not repeated evidence for a
stochastic-performance entry — it was also graded by the runtime that produced the answers.
Leave it uncited until a second, independent sitting exists. `memory.py compact` will keep
listing it; that listing is the correct state, not a backlog to clear.

## Two things that cost time here

- Two sessions share this working tree, and drops from other projects have arrived as
  whole-repo archives. One previously overwrote this lane's memory store with a stale copy and
  silently deleted two events. Run `memory.py review` after any external drop, and if you write
  to the store, check that pre-existing entries survived rather than trusting the tool's own
  readback — it verifies against the file, not against what another tree is about to commit.
- Long content breaks bash heredocs in this environment; `\n` inside one arrives as a real
  newline and lands mid-string-literal. Write the file with an editor tool instead.

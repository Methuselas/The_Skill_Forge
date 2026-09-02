# Handoff — third review-protocol run, fresh chat

**Repo:** `D:\Repos\SkillForge`
**Mechanics:** in `workspace/REVIEW_PROTOCOL_RUN_HANDOFF.md`. Read that file for the protocol,
the memory query, the toolchain invocations and the report format. This file adds only what has
changed since run 2. Run 2's own report is in `workspace/REVIEW_PROTOCOL_RUN_2_REPORT.md`, in its
own file so that reading it is a deliberate act rather than a side effect of opening this one.

## What is different this time

Nothing has been changed in `AP_review_code_you_did_not_write` or in the lane's memory since run 2.
No entries were appended and no events were recorded for run 2 — the repair decisions from it are
still open, and are listed under "Open repairs" below. If a repair lands before you start, this
paragraph is stale and you should trust the store over this file.

Retrieve memory the way the protocol says, with cues drawn from your own task, and report which
ids came back and whether any of them changed what you did. **Do not open
`REVIEW_PROTOCOL_RUN_2_REPORT.md` until your own findings are written to a file** — it names which
entries fired for run 2 and what each one changed, and reading it first destroys the thing that
measurement is for. Nothing in this file names them, and that is deliberate.

Add `--cues` drawn from whatever you end up looking at, beyond the two the mechanics file gives.

## Do not review these

Already reviewed; pick something else:

```
endless-sky/source/Account.{h,cpp}              (twice)
freeorion/Empire/ResearchQueue.{h,cpp}
pydantic/_internal/_utils.py
prometheus/tsdb/isolation.go                    (run 2, plus the collaborators it read:
                                                 head.go, head_append.go, head_read.go,
                                                 db.go, compact.go, querier.go)
```

Prefer a language the cards were not written from. The lane's origins are C++ and statically typed.
Run 2 took Go; `Rust/ripgrep` and `Python/pydantic` are both still untouched apart from the one
pydantic file above. A library crate whose consumers live outside this tree would be the more
informative pick, because tracing outward from one is unbounded in a way it is not for an
application, and nothing here has tested what that costs. Choose the slice freely rather than
hunting for somewhere you suspect is weak; how it was chosen changes what step 8 returns.

## State you are starting from

Run 2 wrote nothing. The store was committed after it, at `a437d6b`, so `HEAD` and the working
tree now agree — the numbers below are both:

- `validate.py` PASS across 1446 objects.
- `memory.py validate` PASS across 4 stores, 26 entries, 76 events.
- Suite OK, 110 tests, ~226s.

Run all three before starting and stop if any is already red. Check them against `HEAD` rather
than the working tree if anything looks off: an earlier drop clobbered this store, and the tell
was a count that matched the file but not the history.

`SE_EV_0036` is **awaiting consolidation on purpose.** It records one sitting in which three drills
were taken blind and graded, and one sitting is not repeated evidence for a stochastic-performance
entry — it was also graded by the runtime that produced the answers. Leave it uncited until a second,
independent sitting exists. `memory.py compact` will keep listing it; that listing is the correct
state, not a backlog to clear.

## Two things that cost time here

- Two sessions share this working tree, and drops from other projects have arrived as whole-repo
  archives. One previously overwrote this lane's memory store with a stale copy and silently deleted
  two events. Run `memory.py review` after any external drop, and if you write to the store, check
  that pre-existing entries survived rather than trusting the tool's own readback — it verifies
  against the file, not against what another tree is about to commit.
- Long content breaks bash heredocs in this environment; `\n` inside one arrives as a real newline
  and lands mid-string-literal. Write the file with an editor tool instead.

## Third thing, new from run 2

The Go toolchain works but is not on PATH and needs its caches redirected. This invocation ran
cleanly, and copying a single self-contained source file into a scratch module is a cheap way to
execute the code under review rather than argue about it — `tsdb/isolation.go` imports only `math`
and `sync`, so it compiles verbatim once `package tsdb` is rewritten to `package main`:

Set `SCRATCH` to your own session scratchpad directory first — it is not defined for you, and
pointing the caches inside the repo would leave build output in the working tree:

```bash
SCRATCH=/c/path/to/your/scratchpad/goscratch && mkdir -p "$SCRATCH" && cd "$SCRATCH"
export GOCACHE="$SCRATCH/.gocache" GOPATH="$SCRATCH/.gopath"
"D:/tools/go/bin/go.exe" mod init scratch && "D:/tools/go/bin/go.exe" run .
```

## Open repairs from run 2

Decisions, not tasks — nobody has ruled on these yet. They are listed so the decisions are not
lost, not as things to look for: do not go hunting for these two shapes in your own slice. What
step 8 returns is only worth anything if you found it because the code put it in front of you.

1. Whether the sentinel-headed-list gap is worth a Pattern in `core`. Run 2's step 8 returned it as
   the single unowned item; the searches behind that claim are in the run 2 report file.
2. Whether `PAT_break_one_of_deadlocks_four_conditions` should say where a lock-order convention is
   written down, which is run 2's owned-but-coarser item.
3. Whether run 2 is admissible evidence for anything in memory at all. It is one run, by one runtime,
   on a freely chosen slice, and it wrote nothing on purpose.


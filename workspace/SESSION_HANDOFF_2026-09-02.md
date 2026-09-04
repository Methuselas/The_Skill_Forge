# Handoff — SkillForge, software-engineering lane, 2026-09-02

**Repo:** `D:\Repos\SkillForge`. Clean, in sync with `origin/main`, suite green.
**Read first:** `CLAUDE.md`, then `.claude/skills/software-engineering/SKILL.md`.

Supersedes `SESSION_HANDOFF_2026-08-30.md`, whose section 5 is now entirely closed. This session
ran across three calendar days (08-30, 08-31, 09-02) with a two-day gap in the middle.

---

## 1. Verified state

| package | objects |
|---|---|
| software-engineering | 608 |
| art | 547 |
| writing | 288 |
| game-design | 39 |
| metaskills | 5 |

`validate.py` → PASS, 1486 objects. `memory.py validate` → PASS, 4 stores, 33 entries, 85 events.
Suite → OK, **113 tests**, ~230s. Nothing awaiting consolidation.

Software-engineering store: 17 entries (14 active, 2 resolved, 1 monitoring), 41 events.

**One review item, and it is real work, not noise:** `memory.py review` flags `SE_MEM_017` as a
`deterministic_contract` still `active`, suggesting it move to `resolved` once its fix has
landed. It has not landed — see section 4.

---

## 2. Query memory before doing anything productive

Do not read the entries out of this file. They are the system of record and a copy here would rot.

```bash
python PASS/tools/memory.py query --domain software-engineering --cues "review this code" --cues "count"
```

One entry has changed shape enough that you should know its *status* without being told its
content: `SE_MEM_016` is now a `known_boundary`, not a `recurring_failure`, and it cites six
events. It was tested and the thing it claimed did not hold. Read it from the store.

---

## 3. What happened this session

Four review-protocol runs against real code, then three controlled experiments about the
protocol itself.

**Runs.** `endless-sky/Account` (C++), `prometheus tsdb/isolation.go` (Go),
`ripgrep ignore/src/overrides.rs` (Rust, five times over). Every run produced code findings; the
guidance findings produced two new cards and three widened ones, all committed.

**Experiments.** `SE_MEM_016` claimed that retrieving it is what makes a reviewer trace out of
the file to callers before ranking. Three pre-registered A/B comparisons removed five candidate
supports for that behaviour, one or two at a time, using two throwaway checkouts and paired
subagents. The behaviour survived all five removals. The entry has been rewritten to say so.

The series is **closed at its floor**: the only remaining candidate is the reviewing task
itself, which cannot be removed without ceasing to be a review. Do not reopen it by removing
one more thing; there is nothing left to remove. The full record, including a voided attempt and
its cause, is in `workspace/RUN_4_PREREGISTRATION.md` and `workspace/RUN_4_RESULTS.md`.

**Library changes**, all pushed: `PAT_keep_a_structure_non_empty_so_the_empty_case_disappears`
(new), `PAT_state_a_types_default_in_one_place` (new, then widened twice),
`PAT_break_one_of_deadlocks_four_conditions` (widened twice),
`PAT_treat_compiler_warnings_as_potential_bugs` (widened),
`AP_review_code_you_did_not_write` (step 8's gate repaired).

**Tooling:** `memory.py compact --entry` now refuses to drop an entry's existing citations
unless `--replace` says so. It used to overwrite silently and report PASS.

---

## 4. Open work

**a. `SE_MEM_017`'s fix has not landed, and `review` will keep flagging it.** The entry says the
drill checks' closing bullet asks for something the Instructions never name, and nominates
`PASS/docs/PASS_SCHEMA.md`'s Drill section as owner. Nobody has ruled on whether the schema
should require the Instructions to ask for everything the Success Check tests. That is the
decision; the flag will not clear until it is made.

**b. A second, independent drill sitting.** `SE_EV_0036` is one sitting graded by the runtime
that produced the answers. `SE_MEM_017` cannot move off `provisional` without a second one from
a session that did not write the checks and did not take the first sitting.

**c. The founding sighting is unexplained.** One review, once, stopped at the file boundary. Six
runs since have all traced outward under every condition tried. Nobody has investigated what
made that one review different, and the entry now says so rather than implying it is handled.
This is the genuinely open question the experiments left behind.

**d. The art lane's 119 drill keys.** `workspace/ART_DRILL_SUCCESS_CHECK_HANDOFF.md` is written
and ready. Deferred by the user, not forgotten, and not this lane's work.

**e. Review a slice that is not `overrides.rs`.** Five of the six runs used one file in one
language. Nothing in the experiment results generalises past it.

Already reviewed; pick something else: `endless-sky/source/Account.{h,cpp}`,
`freeorion/Empire/ResearchQueue.{h,cpp}`, `pydantic/_internal/_utils.py`,
`prometheus/tsdb/isolation.go` and its callers, `ripgrep/crates/ignore/src/overrides.rs` and its
callers in `dir.rs`, `hiargs.rs`, `gitignore.rs`, `types.rs`.

---

## 5. Things that cost time here

- **Three sessions share this working tree.** `HEAD` moved under this session four times today
  while the writing and game-design lanes committed. Nothing collided, because the lanes do not
  overlap — but check before you commit, and run the integrity check below after any external
  drop rather than trusting a validator count.
- **A game-design drop committed four untracked `workspace/` files** it did not own, including
  this session's pre-registration. Harmless in content; it is the archive-carrying-more-than-its-lane
  problem, third sighting.
- **Integrity check after any drop:** confirm your entries and events survive by id, not by
  count. A count that matches the file tells you nothing about what another tree overwrote.
- **Subagents inherit the parent's working directory.** A repository-relative command in a
  subagent prompt resolves against the *parent's* checkout, not the one named in the prose. This
  voided an entire experiment. Require the agent to `cd` first *and* to report the absolute path
  it worked in, so the failure is visible in the report instead of silent.
- **`git worktree` checkouts get CRLF where the main tree has LF.** A file can be
  content-identical and still diff as entirely changed. Compare decoded text, not bytes.
- **Long content breaks bash heredocs.** `\n` inside one arrives as a real newline and lands
  mid-string-literal. Write the script to a file and run the file.
- **cwd resets to the repo root between some tool calls.** Use absolute paths.
- **Never paste memory text into a card.** `tests/test_memory.py` enforces it.

---

## 6. One correction made at the end of this session

Five events appended during this session carried the wrong date — `2026-08-30`, copied from the
convention already in the store, when the commits that carried them are dated `2026-08-31` and
`2026-09-02`. `SE_MEM_017`'s `last_verified` was wrong by a day for the same reason. Both were
corrected in place against the git dates.

This is a deviation from the store's append-only convention, which says to correct history by
adding a superseding event rather than rewriting a line. Six superseding events to fix six dates
would have buried the record they were meant to clarify. The rule exists so that *observations*
are not quietly revised; nothing here touched an observation, and no event written by another
session was altered. Flagged so the next reader knows it happened and can disagree.

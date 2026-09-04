# Handoff — the second sitting that closes `SE_MEM_017`

**Repo:** `D:\Repos\SkillForge`. **Lane:** software-engineering only.
**Read first:** `CLAUDE.md`, then `PASS/docs/MEMORY_SCHEMA.md` §Lifecycle.

`SE_MEM_017` is `known_boundary` / `deterministic_contract` / `provisional` / `monitoring`. The
fix has landed — `PASS/docs/PASS_SCHEMA.md` now requires a drill's Instructions to ask for every
artifact its Success Check grades, and all 71 software-engineering drills were repaired against
it (`c8d60f1`, `f986590`, `f5f7742`). Nothing yet shows the repair works.

This document sets up the run that decides. **You are the controller, not the runner.** Read all
of it before starting; the runner must read none of it.

---

## 1. The claim under test, stated narrowly

Do the repaired Instructions carry a runner to the closing bullet of the Success Check?

That is the whole question. It is not "are the drills passable" and it is not "did the overall
score improve." Keep the scope this tight or the run will produce a number nobody can interpret.

**Baseline, from `SE_EV_0036` (2026-08-30):** nine of fifteen bullets passed across three drills —
four of five, three of five, two of five. **The closing bullet failed in all three.** That
0-of-3 is the measurement; the 9-of-15 is not a rate and the entry says so explicitly.

---

## 2. Why this cannot be run casually — two contaminations, both fatal

**a. Skillset Memory hands the runner the answer.** `.claude/skills/software-engineering/SKILL.md`
tells a session to query memory before working, and `SE_MEM_017`'s retrieval cues include
`take a drill`, `run a drill`, `what does this drill want`, and `did I pass`. Verified just now:

```bash
python PASS/tools/memory.py query --domain software-engineering --cues "take a drill"
```

returns `SE_MEM_017`, whose observation states outright that the failing bullet is the last one
and that the closing position is by convention the fabrication-resistant one. A runner who reads
that does the extra thing and the measurement collapses. Monitoring entries are retrievable by
design, so this is not a bug to fix — it is a hazard to route around.

**b. The file contains the answer three sections down.** In ordinary use a runner opens one file
and sees the whole drill. That is the point of the boundary already recorded in the entry. To
measure production rather than recognition, the check must be unavailable, not merely
un-scrolled-to.

**Both are solved the same way: the runner never touches the repository.**

---

## 3. Setup — do this yourself, before spawning anyone

The three drills are the same three the first sitting used. Same drills is what makes the two
comparable; do not substitute.

| drill | shape | first sitting |
|---|---|---|
| `core/avoiding-surprises/DRILL_replace_magic_value_with_explicit_absence.md` | refactoring whose middle stage must fail to compile | 2 / 5 |
| `core/error-handling/DRILL_classify_error_recoverability_from_call_site.md` | language-agnostic classification ending in a choice | 3 / 5 |
| `languages/cpp/copy-control/DRILL_make_copy_assignment_self_and_exception_safe.md` | C++ resource-ownership rewrite | 4 / 5 |

Write each one, **truncated immediately before `## Success Check`**, into a scratch directory
outside the repo. Keep the front matter, Practice Task, Target Skill, Setup and Instructions.
Drop Success Check, Common Failures and Notes — Notes and Common Failures both leak grading
criteria, and the first sitting's protocol excluded them too.

Verify by grep that no truncated file contains the string `Success Check` before you hand it over.

---

## 4. Running it

**The runner** gets: the three truncated files by absolute path, and an instruction to answer each
to its own file. Nothing else. No repo path, no memory tool, no mention of `SE_MEM_017`, of this
document, of the schema rule, of closing bullets, or of what is being measured. If the runner asks
what the exercise is for, it is doing the drill and that is all it needs.

Require the runner to state the absolute path it worked in and to echo it back in its report. A
prior experiment in this repo was voided because a subagent inherited the parent's working
directory and silently worked in the wrong checkout; a repository-relative path in a prompt does
not resolve where the prose says it does.

**Freeze the answers** before anything reveals a check. Copy them somewhere the grader cannot
write.

**The grader is a third party — not you, and not the runner.** The first sitting's own event
records that its grading was done by the runtime that produced the answers and calls that "the
weakest position from which to score them." Give the grader the frozen answers and the full drill
files, and ask for a per-bullet pass/fail with the sentence of the answer that satisfies each
bullet quoted. A bullet marked pass without a quotable sentence is a fail.

---

## 5. Pre-registration — commit to this before you see any answer

- **Primary outcome:** closing-bullet passes, out of three. Baseline 0.
- **3 of 3** — the repair carries the runner to the closing bullet. `SE_MEM_017` moves to
  `resolved`; the schema rule holds it from then on.
- **2 of 3** — partial. Entry stays `monitoring`. Name which drill failed and whether its closing
  bullet's artifact is genuinely absent from its Instructions, which would be a defect in that
  drill rather than in the rule.
- **0 or 1 of 3** — the repair did not work. Say so in the entry. Do not resolve it, and do not
  re-run with different drills until the failure is attributed.
- **Secondary, reported but not decisive:** the fifteen-bullet total. Useful for spotting a
  regression where a repaired instruction broke a bullet that used to pass. Not a rate, not
  comparable as a percentage.

**Two confounds, declared in advance because they are real:**

1. **The instruction lists grew.** 5→7 steps, 5→7, and 3→6. A longer list may raise passes through
   general scaffolding rather than through the artifact rule specifically. Mitigation: for every
   closing bullet that passes, the grader names *which step* produced the artifact. If it is a
   step added by the repair, the rule is doing the work. If it is a step that already existed, the
   pass is not evidence for the rule.
2. **The grader changed.** Independent grading is a second difference between the sittings, not
   just one. It biases *against* the repair — a stricter grader finds fewer passes — so a good
   result under it is stronger evidence than the baseline was, and a bad result is ambiguous
   between the repair failing and the grading tightening. Say which when you write it up.

---

## 6. What makes the run invalid

Hard rule 17: an invalid run stays in `training_history.jsonl` and never counts toward a craft
weakness. Any of these voids it — record the event with `validity: invalid` and the cause, then
set up again:

- The runner read a Success Check, a Common Failures section, or a Notes section.
- The runner retrieved `SE_MEM_017`, or was told anything in sections 1, 2 or 5 above.
- The runner had repository access and could have opened the whole file.
- The runner worked in a directory other than the one it reported.
- The grader was the runner, or had seen the answers being produced.

---

## 7. Writing it up

Append one event with `python PASS/tools/memory.py append --domain software-engineering`, verified
by readback. Model it on `SE_EV_0036` — same fields, and observations that record what was
executed rather than what was concluded.

Then update `SE_MEM_017`: `evidence_count` to 2, cite the new event alongside `SE_EV_0036`, and
extend `boundary` with the outcome. On 3 of 3 set `status: resolved`; `confidence` may go to
`repeated` since two independent sittings is what that threshold means for a
`deterministic_contract`. `memory.py compact --entry` will refuse to drop existing citations
unless `--replace` says so — that guard exists, do not defeat it.

Do not paste any of this into a card. `tests/test_memory.py` enforces it.

---

## 8. Housekeeping

- Three sessions share this working tree and all commit to `main`. `git fetch` and check
  divergence before committing; confirm your entries and events survive **by id, not by count**,
  since a count that matches tells you nothing about what another tree overwrote.
- `cwd` resets between some tool calls. Absolute paths throughout.
- Long content breaks bash heredocs — write the script to a file and run the file.
- Run `python PASS/tools/validate.py`, `python PASS/tools/memory.py validate` and the suite
  (`python -m unittest discover -s tests -p "test_*.py"`, 113 tests, ~235s) before committing.

## 9. Not this lane's work

The art and writing lanes' drills have never been checked against the Instructions contract, and
their Success Checks were rewritten in the same pass that produced the software-engineering ones.
The boundary in `SE_MEM_017` says so. Do not touch them here — one domain per run.

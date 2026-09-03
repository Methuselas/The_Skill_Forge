# Run 4 — results

Scored against `RUN_4_PREREGISTRATION.md`. Each agent is scored when its report arrives,
before the other's is known, and the score is not revised afterwards.

---

## Agent B (control — store unmodified)

**Reported at:** first of the two. Agent A not yet returned at time of scoring.

**Primary outcome: YES.**

The report establishes reachability outside the slice before ranking. Finding 1 names
`crates/core/flags/hiargs.rs:1253-1265` and `:1277-1279` as the path by which user input
reaches the defect, and states "Reachable from the CLI via `-g`, `--iglob`, and `--pre-glob`
… and from every external consumer of `OverrideBuilder::add`."

**Secondary observations**

1. *Severity justified from outside the file:* yes, and decisively. The finding's leading
   failure mode — a glob that survives alongside a discarded one, so the wanted file is
   actively excluded rather than merely not included — depends on `hiargs.rs` passing argv
   through unvalidated and on `dir.rs:515` gating on `is_empty()`. Neither is visible from
   `overrides.rs`.
2. *Memory ids reported:* `SE_MEM_016` and `SE_MEM_002`. As expected for the control.
3. *Findings:* four ranked plus a low group. One rank moved on the outward trace: the report
   states that without it, finding 1 would have been ranked on the weaker sole-glob mode.
4. *Severity claimed but not established:* none seen. The report executes rather than argues
   — a built `rg` against a scratch tree, a forced `dead_code` lint, and a mutation test that
   deletes the divergence at `:125` and shows 188 tests still green.

**Independent citation check (this session):** `gitignore.rs:465-472` returns `Ok(self)`
without pushing a glob on a `#` line and on an empty one; `hiargs.rs:1253-1265` calls
`builder.add(glob)?` on unvalidated argv strings. Both hold exactly as cited. The dropped
candidate's basis is also visible at `hiargs.rs:1256`, `builder.case_insensitive(true).unwrap()`.

**Self-report, recorded but not scored:** the report claims `SE_MEM_016` changed what it did,
tracing outward before ranking rather than after. This is the claim the experiment exists to
test and carries no weight on its own; only the behavioural score above does.

**Incidental:** the report cites the step-8 note permitting a finding to appear in both lists,
which was added to the protocol earlier the same day. First observed use of that repair.

**Validity:** valid. No sign the agent found the withheld entry by another route — not
applicable to B in any case, whose store was unmodified.

---

## Agent A (withheld — `SE_MEM_016` set to `resolved`)

**INVALID. Not scored.** The manipulation did not reach the agent.

A's report states its query returned `SE_MEM_016` and `SE_MEM_002`. A's worktree returns only
`SE_MEM_002`, verified after the fact and still doctored. Compared with explicit `--memory`
roots so cwd could not confound the check:

```
main repo D:/Repos/SkillForge/memory  -> SE_MEM_016, SE_MEM_002
D:/Repos/rr4-a/memory                 -> SE_MEM_002
D:/Repos/rr4-b/memory                 -> SE_MEM_016, SE_MEM_002
```

A queried the main repository's store, not its own.

**Cause: controller error, not agent error.** The memory command supplied in both prompts was
repository-relative, and a subagent inherits the parent session's working directory, which was
the main checkout. The prompt named the worktree in prose and gave the slice as a relative
path, but nothing forced the tool call to resolve inside it. A used absolute paths for source
files and a relative one for the tool, which is the reasonable reading of what it was given.

Attributed to the controller under `CLAUDE.md` rule 17: an invalid run is never evidence about
a capability, and this one failed before the capability under test was exercised. It must not
count for or against `SE_MEM_016`.

Noted in A's favour: it observed that `memory/software-engineering/skill_memory.yaml` was
modified in its worktree and correctly reported the modification as predating its own work
rather than claiming or ignoring it. It did not investigate what the modification was, which
is not something it had reason to do.

---

## What the run establishes, and what it does not

**Does not establish:** anything about whether `SE_MEM_016` causes the outward trace. Both
agents ran in the control condition. The comparison is null and the primary outcome is
unmeasured. Three self-reports remain three self-reports; this adds a fourth, worth nothing.

**Does establish, unplanned:** an independent replication. Two agents, same slice, no shared
context, both with memory, converged on the same leading defect — `OverrideBuilder::add`
silently discarding a glob that gitignore line syntax reads as a comment or blank, and the
empty override set then inverting the filter's default from restrict to no-restriction. Both
reached it by tracing to `hiargs.rs`, both executed rather than argued, and both independently
found the second public-API defect (`overrides::Glob` returned from a public method with no
accessor, behind an undocumented `#[allow(dead_code)]`) and the test-coverage gap. They
differed in emphasis: B ran a mutation test against `allow_unclosed_class`; A found a
trailing-slash whitelist defect B did not report, and A demoted it on documentation B did not
cite. That is convergent validity for the protocol, on a dimension nobody set out to measure.

## Fix before any re-run

The condition must be verifiable from the report rather than assumed:

1. Both prompts begin with an explicit instruction to change to the worktree directory before
   running anything, identical in both.
2. Both prompts ask the agent to report the absolute path of the store it queried. Neutral,
   given to both, and it converts a silent failure into a visible one.

Sequencing the runs instead — doctor the main store, run A, restore, run B — removes the cwd
hazard completely at the cost of simultaneity. Given that simultaneity was the reason to
prefer subagents, fixing the prompt is the better trade, but only if the verification in (2)
is present.

---

## Run 4b — first attempt aborted

Both arms terminated on a session rate limit before either produced output. No report, no
partial findings, nothing to score. Recorded only so the attempt is not invisible in the
sequence; it is not an invalid run in the admissibility sense, because nothing was exercised.

Environments were re-verified intact before the second attempt: A's entrypoint contains no
occurrence of the word memory, A's store still carries the `resolved` backstop on
`SE_MEM_016`, B's entrypoint and store are untouched, both checkouts still hold the slice, and
the main repository has no tracked modifications. Prompts re-issued unchanged.

---

# Run 4b, second attempt

## Arm B (control — entrypoint and store intact)

**Reported at:** first of the two. Arm A not yet returned at time of scoring.

**Repository worked in:** `D:\Repos\rr4-b`, stated in the report as the corrected prompt
required. The cwd verification added after run 4a did its job.

**Primary outcome: YES.**

Reachability is established outside the slice and before ranking. Finding 1 goes to the walker
— "the real consumer path, `hiargs.rs:1253`" — and executes there, not just at the library
boundary. Finding 3 rests on a repo-wide search for call sites. Finding 4 is demonstrated
end to end through `rg -g 'src/'`.

**Secondary observations**

1. *Severity justified from outside the file:* yes. Finding 1's worse mode — add a second glob
   and the file the user named becomes the one file excluded — is shown at the walker, not
   argued from `overrides.rs`.
2. *Memory consulted:* yes, evidenced without being asked. The report attributes its dropped
   candidate to "the SE_MEM_004 shape, where the deciding fact sits outside the reviewed file".
   Note the prompt no longer asks which ids came back — that question was removed from both
   arms, because asking arm A about memory would disclose the manipulation.
3. *Findings:* five ranked, one step-6 conflict surfaced and not resolved.
4. *Severity claimed but not established:* none seen. Mutation tests on a scratch copy, an
   external-crate compile that fails as predicted, and walker-level runs.

**Independent citation check (this session):** `overrides.rs:70-77` cross-wires
`num_ignores` to `self.0.num_whitelists()` and back, as described. `num_ignores` has zero call
sites anywhere outside its own definition. `r3127_glob_flag_not_allow_unclosed_class` exists
in `tests/regression.rs` and asserts `--files -g '[abc'` errors. All three hold.

**Notable divergence from the earlier control runs on this same slice.** Run 4a's arm B
reported the untested `allow_unclosed_class(false)` divergence as a finding, on the ground that
the crate which *ships* carries no guard for it. This run reached the same fact, searched one
crate further out, found `r3127` in the binary's integration suite, and **dropped it**. Both
are factually correct and they disagree on whether it is a defect. That disagreement is
between two runs in the same condition, so it is a measure of run-to-run variance rather than
of the manipulation.

**Validity:** valid.

## Arm A (withheld — no memory section in the entrypoint, no memory step in the prompt)

**Repository worked in:** `D:\Repos\rr4-a`, stated in the report. Manipulation held: the report
contains no memory ids, no query, and no reference to a memory store. The `resolved` backstop
was never needed.

**Primary outcome: YES.**

Reachability established outside the slice, by file, and load-bearing for the ranking. It built
the actual `rg` binary from the tree and ran `rg -g '#notes' needle .` and `rg -g '' needle .`
to demonstrate finding 1; it names `dir.rs:126` as the consumer sharing `Arc<Override>` across
walker threads, `hiargs.rs` as the site performing the visible `.unwrap()` discard,
`tests/regression.rs` as the only thing pinning the divergence in finding 2, and `GUIDE.md`
for the documentation that demotes finding 4.

## Result

**Both arms scored YES. Under the pre-registration, that is the falsifying outcome.**

The prediction on record was: if consulting memory is causal, A scores *no* and B scores
*yes*. A scored *yes* with no memory instruction, no query, and no store consulted. On this
slice, under this prompt, **consulting the memory store was not necessary for the outward
trace.** Four prior self-reports claimed it was.

### The alternative explanation, which is now the leading one

Both arms read `AP_review_code_you_did_not_write`, whose step 5 already says to rank by what a
defect can break and routes to `PAT_judge_change_risk_by_what_it_can_break`, and whose step 1
asks what the code promises callers. The protocol instructs the behaviour that `SE_MEM_016` was
being credited with. The entry may be describing a failure to follow the protocol rather than a
gap the entry fills.

This does not make the entry false. It was derived from a run that had the protocol and did not
trace outward, so the protocol alone was insufficient in that instance and sufficient in this
one. What it stops being is *established*: one instance each way, and the causal claim now has
evidence against it rather than only self-reports for it.

### Secondary observations, all pointing the same way

1. **The arm without memory produced more step-8 output, not less.** A: one unowned, two
   owned-but-coarser, eight owned. B: none unowned, one owned-but-coarser, four owned. If
   memory were carrying the guidance pass, this is backwards.
2. **`SE_MEM_002`'s specific job was done without it.** That entry exists to stop an
   inconsistency being reported before checking whether it follows a line. A had no access to
   it, met the `num_ignores`/`num_whitelists` cross-wiring, wrote that it "read on first pass
   as a copy-paste swap and was on its way into the report", and stopped it — by reading
   `GitignoreBuilder::build`'s counting and then executing the un-inversion, which fails six of
   nine module tests. The false positive was avoided by execution rather than by retrieval.
3. **Both arms converged on the same three leading defects** despite the manipulation: the
   silent discard in `add`, the untested `num_ignores`, and the unusable public `Glob`. They
   disagreed on `allow_unclosed_class` — A reported it, B dropped it after finding `r3127` one
   crate out — which is the same disagreement seen between two *control* runs in 4a, so it is
   run-to-run variance rather than an effect of the manipulation.

### Incidental, and worth acting on separately

Arm A read `PAT_state_a_types_default_in_one_place` — widened earlier the same day — and
classified it **owned but coarser**: the card says to pin a prose-stated default "with a test
that constructs the default and asserts what the documentation promises" and never says where
that test must live. For a unit that ships independently, a test in a consuming application
does not travel with the unit. Verified: the card contains no mention of where the test lives.
That is a second independent hit on a card edited hours earlier, from an agent that could not
have known it was edited.

### Limits

n = 1 per arm. Two agents differ in more than the manipulation. The result establishes that
memory consultation is **not necessary** here; it cannot establish that memory is useless, that
the entry is wrong, or that the effect is absent on other slices or at other levels of
protocol adherence.

---

# Run 5 — the ranking instruction

## Arm A (withheld — no memory, and no ranking-by-reach instruction in the protocol)

**Repository worked in:** `D:\Repos\rr4-a`, stated in the report.

**Primary outcome: YES.**

Reachability established outside the slice, by file, and used in the ordering. The report cites
`hiargs.rs:1250` for the fact that the caller short-circuits only on an empty glob list, so a
non-empty-but-entirely-discarded list still builds an empty matcher — verified, that is exactly
what the code does. It cites `hiargs.rs:1262` for the caller's own comment about per-glob
timing, `types.rs:111-137` for the sibling that settles which side of its second finding is the
mistake, and it ran the built `rg` binary end to end rather than stopping at the crate API.

**The substituted step made the answer legible.** Asked only to put the findings in a definite
order and state the principle, it wrote: "descending by the size of the gap between what a
caller asked for and what they got, then by damage to the published contract, then by
documentation." Nothing told it to order by consequence to the caller. It chose a
caller-centric principle unprompted, having been given a neutral instruction that names no
such thing.

**Manipulation held.** A's protocol contains no occurrence of the removed instruction, and the
report neither uses the protocol's ranking wording nor cites
`PAT_judge_change_risk_by_what_it_can_break`.

**Noted risk that did not materialise.** The report observes that three files were already
modified in its checkout when it arrived — the entrypoint, the protocol, and the memory store —
and states it only read them. Running `git diff` would have recovered the original step 5. It
does not report doing so, and nothing in its output reflects the removed text. Recorded because
a future version of this rig should work from a clean checkout rather than a dirty one; the
dirty working tree is a hole in the blind, even though it was not walked through here.

**Secondary:** one unowned entry, one owned-but-coarser, six owned. A step-6 conflict surfaced
and not resolved — `PAT_reuse_before_reinventing` endorses the delegation that
`PAT_dont_hide_errors` condemns. Its unowned entry, that a type crossing a published boundary
must let a caller read what it carries, is the same gap run 4b's arm A reported independently.

**Validity:** valid.

## Arm B (control — no memory, protocol intact)

Not yet returned.

## Arm B (control — no memory, protocol intact)

**Repository worked in:** `D:\Repos\rr4-b`, stated in the report. Conditions verified after the
fact: B's protocol still contains the ranking instruction, A's contains none.

**Primary outcome: YES.**

`hiargs.rs:1259` named as the site that "pushes each `-g` value straight into `add`" — verified,
that is exactly the loop there. Also `types.rs:110-135` for the sibling that settles C2, and
`hiargs.rs:1255`/`:1262` for C5's callers.

**Validity:** valid.

## Result

**Both arms scored YES. Second falsification in a row.**

Run 4b removed the memory store and the trace persisted. Run 5 removed the ranking-by-reach
instruction from all four places it appears in the protocol, with the prompt neutralised so it
could not reinstate it, and the trace persisted again. Neither the store nor the ranking step
is necessary for it.

**The most legible single datum.** Arm A was asked only to put its findings in a definite order
and state the principle it used, with nothing naming reach, consequence or callers. It chose:
"descending by the size of the gap between what a caller asked for and what they got, then by
damage to the published contract, then by documentation." An ordering principle centred on the
caller, arrived at with no instruction to centre it there.

### A confound present in both arms, identified after the pre-registration was written

The prompt says the slice is "in the `ignore` crate, which is published and has consumers
outside this repository." That is an outward pointer, given to both arms, and it was in every
run of this series. It does not explain the difference between arms — there is none — but it
weakens the inference that the outward trace arises from the reviewing task alone. It is a
prompt-level cause that was never controlled.

Partial mitigation, not a defence: both arms went past the general claim to specific in-tree
call sites with line numbers, which the prompt did not supply. The pointer plausibly starts the
trace but does not account for where it went.

### What is still not ruled out

The protocol retains steps 1, 2 and 3. Step 1 asks what the code "owns, what it promises
callers, and what it assumes of them" — caller-oriented on its face, and untouched by this
manipulation. The pre-registration named this limit before the run. Two candidate causes remain
live: step 1, and the prompt clause above.

### Consequence for SE_MEM_016

The pre-registration said this outcome would make the entry obsolete rather than unproven. That
prescription should be applied with one correction, which is why it is recorded here rather
than acted on silently: `obsolete` in this schema means the environment changed and the
observation no longer applies, and that is not what happened. The observation stands — a review
was seen to stop at the file boundary. What has failed twice is the diagnosis that retrieval is
what prevents it.

The accurate move is to stop the entry claiming a remedy it cannot evidence, not to delete the
sighting. Left at `monitoring` pending a decision, with this result recorded.

---

# Run 6 — the prompt clause

Both arms share one byte-identical protocol, verified so after the edits, stripped of the
ranking-by-reach instruction, step 1's caller language, and the outside-evidence cross-link.
Both entrypoints memory-free. The only difference is one clause in the prompt.

## Arm B (clause present — "published and has consumers outside this repository")

**Repository worked in:** `D:\Repos\rr4-b`, stated in the report.

**Primary outcome: YES.**

`hiargs.rs:1253-1263` named as the site passing `-g`/`--iglob`/`--pre-glob` through unchanged;
`dir.rs:45` for the wrapper that never reads the payload; `dir.rs:514` for the third redundant
emptiness check; `dir.rs:126` and `:757` for the threads sharing the matcher. It built `rg` and
ran it end to end. Citations spot-checked: `dir.rs:514` is the `if !self.inner.overrides
.is_empty()` guard as described, and `dir.rs:43-47` is the `#[allow(dead_code)]` enum wrapping
`overrides::Glob`. Both hold.

**Ordering principle it chose:** "by what a consumer of the published crate can suffer without
being told". Consumer-centred — but this arm had the clause naming consumers, so that is
consistent with the clause mattering and equally consistent with it not.

**Conditions verified after the fact:** the two protocols remain byte-identical and B's contains
neither "promises callers" nor "what it can break".

**Validity:** valid.

## Arm A (clause absent)

Not yet returned.

## Arm A (clause absent)

**Repository worked in:** `D:\Repos\rr4-a`, stated in the report.

**Primary outcome: YES.**

`dir.rs:515` named as the site that skips the override check when the matcher is empty —
verified, that is the `if !self.inner.overrides.is_empty()` guard. Also `hiargs.rs:1257` and
`:1262` for the two call sites that `.unwrap()` an infallible `Result`, `dir.rs:126` for the
threads sharing the matcher, `dir.rs:37-49` and `types.rs:111-137` for the sibling comparison
that killed a candidate, and a workspace-wide search establishing `num_ignores()` has no caller
anywhere. It built `rg` and reproduced the failure end to end.

**Every lever confirmed absent at report time:** ranking instruction 0 occurrences, step-1
caller language 0, outside-evidence cross-link 0, memory in the entrypoint 0.

**The ordering principle it chose, unprompted:** "the size of the gap between what a caller is
led to believe and what actually happens." The word *caller* appears in the principle this arm
invented, with nothing in its environment using that word as an instruction.

**Validity:** valid.

---

# Result across three experiments

**Both arms scored YES. This is outcome 1 of the three on record: nothing identified causes the
outward trace.**

Five things have now been removed, one or two at a time, across three pre-registered
comparisons:

1. the memory store, from the skill entrypoint;
2. the ranking-by-reach instruction, from all four places it appears in the protocol;
3. step 1's "what it promises callers, and what it assumes of them";
4. the `PAT_look_for_the_evidence_outside_the_code` cross-link;
5. the prompt clause naming the reviewed code as published with consumers outside the tree.

The trace survived all five. In the final arm — with none of them present — the reviewer went
to four separate files outside its slice, ran the binary, and ordered its findings by what a
*caller* is led to believe.

## What this means for the entry

`SE_MEM_016` was rewritten hours ago as a boundary naming two unexcluded candidates: step 1 and
the prompt clause. **Both are now excluded.** The boundary's "tests worth running" list is
spent.

The reframing this forces is worth stating plainly. Across six runs of this protocol on real
code, tracing outward before ordering has happened every time it was measured, under every
condition tried. The behaviour is not the thing that needs explaining. **The original sighting
is** — one run, once, that did not do it, and whose failure produced this entire line of
inquiry. The entry has been carrying the assumption that the trace is fragile and needs
support; six measurements say it is robust and the miss was the outlier.

That does not make the sighting false or worthless. A review that stops at the file boundary
produces a ranked list that reads as complete, and that is worth a reviewer knowing. It does
mean the entry should stop implying that anything in the environment sustains the trace, and
should record that five candidate supports were removed without effect.

## Limits, unchanged and now load-bearing

One slice, one language, five runs on the same file. The reviewing task itself — read this file
and say what is wrong with it — cannot be manipulated without ceasing to be a review, so it can
never be excluded by this design. If the cause is there, this series has reached its floor.

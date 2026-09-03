# Run 4 — pre-registration

Written before either agent was spawned, before the doctored store was built, and before
anyone read the slice. Fixed at this point so the criterion cannot be retrofitted to the
result. Nothing below may be edited after the first report arrives; corrections go in a
dated appendix.

## The question

`SE_MEM_016` says this runtime reviews a file without tracing outward to callers, and still
performs the protocol's ranking step, which cannot be answered without them. Three runs have
now reported that retrieving the entry changed what they did. All three are self-reports by
the runtime whose behaviour is in question, and the entry's own boundary says the retention
claim is unsupported because nobody has run a slice with the entry withheld.

**Does the entry cause the outward trace, or does this runtime trace outward anyway?**

## Design

Two subagents, spawned from one parent in one session, running simultaneously.

- **Agent A (withheld).** Works in a git worktree whose memory store has `SE_MEM_016` set to
  `status: resolved`. `memory.py query` returns only `active` and `monitoring` entries
  (`memory.py:43,421`), so the entry is silently absent from its results. The store still
  validates and the entry is still in the file. A runs the normal handoff and the normal
  query, and has no signal that anything was withheld.
- **Agent B (control).** Identical worktree, unmodified store.

Both get **byte-identical task prompts**. If they differ, the confound is mine.

Slice for both: `workspace/sources/Rust/ripgrep/crates/ignore/src/overrides.rs`, 293 lines,
chosen by a mechanical rule stated before the listing was run — 200–500 lines, at least five
function definitions, first by path, excluding the `cli` and `core` crates because run 3 read
those and a rediscovery would muddy the comparison.

## Primary outcome

Checkable from the reports alone, without asking either agent what it used:

> **Does the report establish reachability outside the slice file — naming at least one
> caller, consumer, or configuration site by file — as part of, or before, ranking the
> findings by severity?**

Scored yes / no for each agent. Not "did memory help", which is the self-report already known
to be untrustworthy.

## Secondary observations

1. Does the ranking justify any finding's severity by reference to something outside the file?
2. Which memory ids does each report say came back? (A should not name `SE_MEM_016`.)
3. Number of code findings, and whether any changed rank because of a caller.
4. Does either report claim a severity it did not establish?

## Predictions

- **If the entry is causal:** A scores *no* on the primary outcome, B scores *yes*.
- **If it is not causal:** both score *yes*, or both score *no*.

## What would falsify the entry

A scores *yes*. If the runtime traces outward with the entry withheld, `SE_MEM_016` is
describing behaviour that happens anyway, and it should move toward `monitoring` or
`obsolete` rather than sit at `provisional` accumulating non-recurrences. This is the outcome
worth naming in advance, because it is the one the three existing self-reports argue against
and the one nobody has tested for.

## Known limits, stated now rather than after

- **n = 1.** One slice, one comparison. It moves the retention claim from three self-reports
  to one behavioural observation. It is not enough on its own to promote the entry.
- **Two agents differ in more than the manipulation.** Same chain, same moment, same prompt,
  but not the same process. This is a natural experiment, not a clean one.
- **A could find the entry another way.** It has the repo, and the file still contains
  `SE_MEM_016`. The manipulation only guarantees that `query` will not return it. If A's
  report quotes the entry, the run is invalid and must be recorded as such rather than scored.
- **The parent knows the hypothesis.** That is what this file is for.

---

# Appendix — 2026-08-30, run 4b

Added after run 4a was voided. Nothing above was edited. Written before either agent was
spawned for this attempt.

## What changed and why

Run 4a failed because the manipulation lived only in the store while the prompt handed both
agents a repository-relative command, and a subagent inherits the parent's working directory.
Agent A queried the main checkout and received the entry that was withheld from its own.

The manipulation now lives in the **entrypoint** instead. Agent A's checkout has the
`## Skillset Memory` section removed from
`.claude/skills/software-engineering/SKILL.md`, along with the one remaining passing mention
of `memory/` in the write-barrier section. A therefore has no instruction to consult memory
and no pointer to it. A wrong working directory can no longer defeat this, because there is no
command to misdirect.

Retained as a backstop, not as the primary manipulation: `SE_MEM_016` is still `resolved` in
A's store. If A queries anyway, the entry still will not be returned, and the report will show
which store answered.

## The question this version asks

Coarser than the original, and stated plainly so the result is not over-claimed later:

> **Does consulting the memory store change review behaviour?**

Not "does `SE_MEM_016` change it". `SE_MEM_002` is removed by the same manipulation, and it
did visible work in run 4a — it stopped a false positive on the `num_ignores`/`num_whitelists`
cross-wiring. A behavioural difference therefore attributes to memory consultation as a whole,
and narrowing to a single entry needs a further run.

Accepted deliberately: a coarser manipulation produces a larger effect, which is the right
trade at n = 1.

## Primary outcome

Unchanged from above, and still checkable without asking either agent what it used: does the
report establish reachability outside the slice file — naming at least one caller, consumer or
configuration site by file — as part of, or before, ranking?

## Verification added

Both prompts now begin by requiring the agent to change to its own directory before running
anything, and both require the agent to report the absolute path of the repository it worked
in. Given to both, so it is not a difference between conditions. Its purpose is to make a
repeat of run 4a's failure visible in the report rather than silent.

## Baseline

Run 4a produced two independent with-memory reports on this exact slice. They are supplementary
evidence, not the control for this attempt: both arms are being re-run with the corrected
prompt so the comparison is between two runs that differ only in the manipulation.

## Predictions

- If consulting memory is causal: A scores *no*, B scores *yes*.
- If it is not: both score *yes*, or both score *no*.

A scoring *yes* falsifies the causal reading and is the outcome three self-reports argue
against. It remains the more informative result.

---

# Appendix — 2026-08-30, run 5

Written before any file was edited for this attempt. Nothing above altered.

## The question

Run 4b showed consulting the memory store is not necessary for the outward trace. The leading
alternative it promoted is that the protocol itself instructs the behaviour. This tests that.

> **Does the protocol's ranking-by-reach instruction produce the outward trace to callers?**

## Design

Two agents, one slice, simultaneous, prompts identical.

**Both arms are memory-free.** `rr4-b`'s entrypoint is stripped to match `rr4-a`'s, so the
`## Skillset Memory` section is absent from both. Memory is already known not to be necessary;
removing it from both removes it as a variable, so the only difference is the protocol.

- **Arm A (withheld).** In `rr4-a` only, the protocol's ranking-by-reach instruction is removed
  from all four places it appears: the `PAT_judge_change_risk_by_what_it_can_break` cross-link
  in the front matter, the Objective's "a ranked set of findings, each naming the defect and
  what it can break", step 5 itself, and the completion check's "Every finding names the
  defect, the code it is in, and what it can break".
- **Arm B (control).** Protocol untouched.

Step 5 is **substituted, not deleted.** It is replaced by a neutral instruction to put the
findings in a definite order and state the principle used, without naming reach, consequence,
or callers. Deleting it would renumber every later step and force edits to the Objective and
Notes, changing document structure alongside the instruction. Substitution holds length,
numbering and internal references constant so the instruction is the only variable.

**The prompt is neutralised in both arms.** The previous prompt asked for findings "each naming
the defect, the code it is in, and what it can break" — the completion check's own wording,
which would reinstate the manipulated instruction from outside the protocol. Both prompts now
ask only for the defect and the code it is in.

## Slice

`ignore/src/overrides.rs` again, deliberately. Comparability outweighs generality here: run 4b
arm A was memory-free with the full protocol on exactly this code and scored *yes*, so arm B is
a replication of a known baseline as well as this run's control.

## Primary outcome

Unchanged and still checkable without asking either agent: does the report establish
reachability outside the slice file — naming at least one caller, consumer or configuration
site by file — as part of, or before, ordering the findings?

## Predictions

- If the ranking instruction is causal: A scores *no*, B scores *yes*.
- If it is not: both score *yes*, or both score *no*.

A scoring *yes* would mean neither memory nor the ranking step is necessary, and the trace is
something this runtime does from the reviewing task alone. That would make `SE_MEM_016`
obsolete rather than merely unproven, and would say the protocol's step 5 documents a habit
rather than creating one.

B scoring *no* would break the replication and invalidate the comparison rather than support
it — the same agent configuration scored *yes* on this slice one run ago.

## Limits

n = 1 per arm, as before. The manipulation is coarse: four edits, not one, so a difference
attributes to the ranking instruction as a whole and not to step 5's wording specifically. The
protocol retains steps 1, 2 and 3, which ask what the code promises callers and run owning
protocols' completion checks backwards — either could produce an outward trace on its own, and
this design cannot separate them.

---

# Appendix — 2026-08-30, run 6

Written before any file was edited for this attempt. Nothing above altered.

## The question

Two manipulations have now failed to stop the outward trace. Two candidates were named as
unexcluded: the protocol's first step, which asks what the code "promises callers", and a
clause in every prompt so far describing the reviewed code as published with consumers outside
the repository. This run removes both and varies only the second.

> **Is the prompt's mention of outside consumers what sends the reviewer outward — and if not,
> does anything left in the protocol do it?**

## Design

Both arms share a protocol stripped of every outward pointer found by search:

- the ranking-by-reach instruction, in the four places run 5 removed it;
- step 1's "what it promises callers, and what it assumes of them", substituted with an
  orientation instruction naming no audience;
- the `PAT_look_for_the_evidence_outside_the_code` cross-link in the front matter, which run 5
  did not account for.

Both entrypoints stay memory-free. The two protocols are made byte-identical and verified so.
**The only difference between arms is one clause in the prompt:**

- **Arm A:** the slice is named with no mention of publication or consumers.
- **Arm B:** the clause is present, exactly as in runs 4b and 5.

## Why this shape

It reads three cells rather than two, because run 5's arm A is the third:

- Both arms score *yes* → nothing identified causes the trace. It survives removal of memory,
  the ranking instruction, step 1's caller language, the outside-evidence link, and the prompt
  clause. At that point the behaviour is intrinsic to the reviewing task as this runtime
  performs it, and the original sighting is the anomaly rather than the trace.
- A scores *no*, B scores *yes* → the prompt clause is sufficient on its own, and every run in
  this series was measuring a pointer I wrote rather than anything in the library.
- Both score *no* → step 1 or the outside-evidence link was doing the work, because those are
  the only things that changed since run 5's arm A, which scored *yes*.

## Primary outcome

Unchanged: does the report establish reachability outside the slice file — naming at least one
caller, consumer or configuration site by file — as part of, or before, ordering the findings?

## Slice

`ignore/src/overrides.rs` again, for comparability against four prior reports on the same code.

## Limits

n = 1 per arm. The protocol strip is now cumulative and coarse: four sites plus step 1 plus a
cross-link, so a *no* attributes to the strip as a whole. Every run in this series has used one
slice in one language, and nothing here speaks to other code. The reviewing task itself — read
this file and say what is wrong with it — is not manipulable without ceasing to be a review,
so it can never be ruled out by this design.

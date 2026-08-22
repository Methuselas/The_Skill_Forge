# PASS — Skillset Memory Schema (closed contract)

status: active
owner: docs/domains/spec
last_reviewed: 2026-08-22

Skillset Memory is the portable empirical record of what actually happens when
the canon is used. It is not canon, not a runtime, not a transcript, and not a
fourth object type.

**Every rule in this file that can be checked mechanically is checked by
`PASS/tools/memory.py validate`.** Rules are written here once so the tool has a
specification; they are not enforced by asking a model to remember them.

Memory reads the memory tree and, when linkage is present, the history beside
it. It never looks for a source document, a page, a chat transcript, or any
record of the conversation that produced an entry.

---

## 1. The firewall

```text
CANON        what decision to make, how to orchestrate it, how to practise it
             Patterns / APs / Drills. Source-independent. Stable.

MEMORY       what happened when the canon was actually used
             Empirical. Provisional. Allowed to be wrong, superseded, resolved.

HISTORY      the events the memory was consolidated from
             Append-oriented. Includes runs that proved nothing.

REGRESSION   what must never happen again under deterministic conditions
             Tests. Not memory's job.
```

Four rules follow, and the tool enforces the ones that can be checked:

1. **Memory never mutates canon.** A memory entry may nominate owners. Only a
   reviewed, approved delta changes a card.
2. **Memory is never inlined into canon.** If an entry seems important enough to
   apply on every turn, that is evidence it has earned promotion review — not a
   reason to copy it into a card or an entrypoint. Copying it there creates a
   second write site and lets the real owner atrophy. Checked by
   `tests/test_memory.py`.
3. **Memory never substitutes for a regression test.** Once a behavior is a
   deterministic invariant, enforce it in canon, the resolver, or a test. An
   entry that exists so the runtime will behave correctly when it is retrieved
   is a workaround, because retrieval is not guaranteed (§3).
4. **Memory is not a ledger.** No source ids, page numbers, hashes, receipts,
   attestations, reading progress, or session state. See §8.

## 2. Admissibility — the gate that matters most

An observation is evidence about a capability only if the run that produced it
was a valid test of that capability.

```text
execution
    ↓
VALIDITY CHECK        was this a valid test of the thing it appears to measure?
    ↓
observation           what was seen
    ↓
diagnosis             why it may have happened; may change later
    ↓
consolidation         only valid evidence reaches compact memory
```

A run is **invalid** when it failed before the target capability was exercised.
Recorded causes so far include an unreachable edit source, a controller that
bypassed its own mode, a package intentionally absent from the distribution, a
reference declared but never routed, a request blocked at a tool guardrail, an
underspecified prompt, and a missing prerequisite foundation.

The vocabulary of causes is **open**. Record what happened; do not force it into
a taxonomy. What is closed is the gate itself:

```yaml
validity: valid | invalid
invalid_reason: <short free-text label, required when invalid>
```

**The invariant:**

> An event marked `invalid` may remain in raw history. It must never increment
> `evidence_count` on a compact entry, and must never be cited for or against a
> craft capability.

`memory.py compact` refuses to count invalid events. `memory.py validate`
rejects a compact entry whose cited evidence includes one.

Invalid runs are worth keeping. They are the evidence that a controller, tool,
package, or prompt needs work — attributed to that owner, not to craft.

## 3. Presence is not consultation

The retrieval order in the doctrine describes an **intended** sequence, not an
enforced one. No runtime can guarantee that memory is read. An entry may be
correct, current, well-scoped, and never loaded, with no error and no signal.

```text
memory exists  ≠  memory validates  ≠  memory was retrieved  ≠  memory influenced execution
```

Two consequences:

- Do not claim an entry influenced behavior because it existed. `memory.py
  query` emits the ids it returned so a run can record what was actually
  consulted; absent that record, consultation is unproven.
- Do not compensate by inlining (§1 rule 2). The compensation destroys the path
  it protects: once the content is in an always-loaded file, the retrieval path
  stops being exercised and its decay becomes invisible.

## 4. Persistence

**The authoritative writable working state is the persistence target.** A git
checkout, an extracted skill package, or a domain authoring bundle may each
serve. Git is one implementation and is never required — this matches
`ARCHITECTURE.md` contract 4, where a clean chat or Project is a first-class
environment and a repo is optional.

The invariants are the same in every environment:

```text
approved            ≠  written
reported written    ≠  verified written
verified written    =  the target reopens and contains the expected state
```

**Post-write readback is a contract, not a courtesy.** After any writeback,
reopen the target and confirm the expected state is present before claiming
persistence. `memory.py append` and `memory.py compact` read their target back
and fail loudly if it does not contain what they just wrote.

Session observations are not memory until writeback occurs. Until then the
honest phrasing is *observed in the current session*.

## 5. `skill_memory.yaml` — compact current state

One file per domain, at `memory/<domain>/skill_memory.yaml`.

```yaml
memory_schema_version: 1
skillset: art
memory_version: 3
entries:
  - id: ART_MEM_001
    scope_type: topic
    scope_id: hands_and_object_contact
    type: recurring_failure
    evidence_class: stochastic_performance
    observation: >
      What was actually seen. Factual. Survives a change of diagnosis.
    confidence: provisional
    status: active
```

### Required keys

```yaml
id:              stable id, unique within the file
scope_type:      skillset | ap | pattern | drill | training | topic | runtime
scope_id:        object_id for canonical scopes; readable slug for topic/runtime
type:            recurring_failure | successful_tendency | known_boundary | training_result
evidence_class:  stochastic_performance | deterministic_contract
observation:     what was seen — not why
confidence:      provisional | repeated | strong
status:          active | monitoring | resolved | superseded | obsolete
```

`evidence_class` is required because the promotion threshold depends on it
(§7). Every other key below is optional.

### Optional keys

```yaml
diagnosis:
  failure_layer:  knowledge | orchestration | retrieval | application | continuity |
                  reference | tool | interface | training
  hypothesis:     current explanation; may change without rewriting observation
boundary:         where the observation was verified and where it was not
evidence_count:   integer ≥ 1
evidence_events:  list of event_id from training_history.jsonl
evidence_origin:  list of runtime_self_audit | user_feedback | human_teaching |
                  training_benchmark | regression_failure | book_close_training |
                  cross_model_test
likely_owners:    list of object_id or free-text owner labels
interventions:    list of { training | drill, isolation_result, retention_result,
                  transfer_result } — each result: improved | partial | unchanged |
                  failed | untested
retrieval_cues:   list of strings used by `memory.py query`
runtime_scope:    generic | free-text label for one execution environment
superseded_by:    id of the entry that replaced this one
last_verified:    YYYY-MM-DD
```

### Evidence origins

`human_teaching` means direct technical instruction or clarification supplied by
the human during study or training. It is distinct from `user_feedback`, which
is the user's assessment of a produced result. Teaching is not automatically a
user preference, is not canonical doctrine, and is not by itself evidence that
anything transferred.

### Self-containment

> An entry must be valid and applicable after the conversation that produced it
> is gone.

This is `CLAUDE.md` rule 1 — a card must execute after its source is gone —
applied to memory. An observation reading *"see the earlier project chat for
details"* is incomplete. Conversation references may survive as optional
authoring provenance; never as a runtime dependency.

## 6. `training_history.jsonl` — event evidence

One JSON object per line, at `memory/<domain>/training_history.jsonl`.
Append-oriented: correct by adding a superseding event, not by rewriting a line.

```json
{"event_id": "ART_EV_0001", "date": "2026-08-22", "task": "…", "validity": "valid",
 "scope_id": "hands_and_object_contact", "delivery": "unknown",
 "observations": ["…"], "baseline": "…", "isolation": "improved",
 "retention": "untested", "transfer": "untested", "notes": "…"}
```

### Required keys

```json
event_id   stable id, unique within the file
date       YYYY-MM-DD
task       what was attempted
validity   valid | invalid
```

`invalid_reason` is required when `validity` is `invalid`.

### Optional keys

```json
scope_id        what the event is about
delivery        how the skill reached the runtime; "unknown" recorded honestly
                beats the field omitted
observations    list — one run may yield several independent observations
                rather than one global verdict
baseline / isolation / retention / transfer
                improved | partial | unchanged | failed | untested
                Record a stage only if it actually ran. "untested" is the
                honest default and the tool will not infer otherwise.
artifact_quality / process_validity / skill_attribution
                strong | adequate | weak | failed | unproven — scored
                independently, because a run can produce a strong artifact
                through an invalid process with no proof the skill contributed
notes           free text
```

### What an event is not

An authoring action is not a training event. `memory.py append` refuses events
whose task describes card authoring, commits, validation runs, index generation,
or archive creation.

```text
Drill authored  ≠  Drill executed  ≠  isolation success  ≠  retention  ≠  transfer
```

Never record a stage that did not run.

## 7. Promotion, lifecycle, compaction

### Two thresholds

```text
stochastic_performance    repeated evidence, then retention, then transfer
deterministic_contract    one clear reproduction may justify a candidate fix
```

After a deterministic contradiction is fixed, the rule belongs in canon, the
resolver, or a test. The entry moves to `resolved` and stops being retrieved.

### Lifecycle

```text
active      currently believed and retrieved
monitoring  believed but under retest, or the owning card changed
resolved    the underlying issue was fixed and the fix held
superseded  replaced by another entry; set superseded_by
obsolete    the environment changed and the observation no longer applies
```

Only `active` and `monitoring` entries are returned by `memory.py query`.
Resolved history stays in the file; it stops biasing the runtime.

### Compaction

```text
raw events  →  periodic synthesis  →  one compact entry
```

Raw history is preserved. Compact entries may be merged, strengthened,
narrowed, resolved, superseded, or re-scoped. Evidence is never deleted to make
a conclusion look cleaner.

### Retrieval

Canon resolves first; memory is retrieved second and bounded. Memory never
chooses the AP.

```text
request → canonical routing → owners → bounded memory → execute
```

When several entries match, prefer exact AP/Pattern/Training scope over
topic scope over skillset scope; then `active` over `monitoring`; then stronger
confidence; then more recent `last_verified`.

## 8. What memory must not store

```text
source ids, page numbers, locators, hashes, receipts, attestations
reading progress, unit maps, next-unit pointers, authoring checkpoints
current workflow or stage position, candidate or branch status
temporary activation left by a recent operation
recently produced artifacts, ambient conversation context
transcripts, full conversations, every user comment
book summaries, canonical text already in cards
generic advice belonging to a Pattern, workflow order belonging to an AP,
practice procedure belonging to a Drill
user-specific preferences — those belong to a future User Memory layer
```

Nothing becomes Skillset Memory except by explicit writeback of a **generalized
empirical observation**. Temporary state is not memory however durable it feels.
The generalized lesson such state reveals may become memory; the state itself
never does.

```text
NOT memory:  rejected thumbnail #6; candidate status; current stage
IS  memory:  broad Stage 0 rejection repeatedly causes the runtime to polish
             the rejected geometry instead of reopening search
```

Where a host provides its own memory facility, that facility occupies the
handoff and user-preference layer. Skillset Memory stays repo-backed and travels
with the skill. Do not write craft-performance observations into a host-provided
user-scoped store.

The validator rejects entries carrying keys from the retired authoring
vocabulary (`source_id`, `session_id`, `current_stage`, `unit`, `next_unit`,
`parent_gen_id`, and similar). See `docs/CLEANUP_2026-08-15.md`.

## 9. Seeding

An empty valid memory system is better than a populated contaminated one. There
is no requirement to populate on day one.

When seeding from retained history:

- prefer execution, Drill, failure-test, critique, and repair evidence;
- reject invalid craft attribution (§2);
- keep deterministic defects that were fixed in tests and history, not in active
  memory;
- normalize every seed into this schema rather than copying it verbatim from
  wherever it was recovered;
- never infer an event that was not recorded.

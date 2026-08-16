# PASS — Preflight and Run Procedure

status: active
owner: docs/domains/corpus
last_reviewed: 2026-08-16
supersedes: the read/extract/place/validate loop previously documented here

Read `PASS_DOCTRINE.md` and `PASS_SCHEMA.md` first.



> The source's structure controls the read, while the existing library controls
> how much of that read deserves to become new knowledge.

> PASS is the workbench that creates and matures structured skills. Skill Forge
> is the repository where those skills live once they are mature enough to build
> and distribute.

The first sentence decides most of what follows: the source sets the units, the
library sets how much of them survives. The second sets this document's boundary.

**This procedure covers the workbench only.** It ends when knowledge is authored,
validated, and accepted into the library. It does not cover assembling a
skillset, resolving package dependencies, or publishing.

```text
SOURCE -> PASS -> DOMAIN LIBRARY || MATURITY THRESHOLD -> SKILLSET -> SKILL FORGE
          <----- this document ----->
```

A card is a durable knowledge atom. A **skillset** is the mature assembled
product built from many of them. **Validated cards are not automatically a
finished skillset.**

---

## 0. Precedence and scope

**Newest accepted canonical state wins.** Where a historical document, an old
run, a recovered tool, or a handoff conflicts with current accepted state,
current accepted state governs. A handoff never outranks it. Reconstructing a
loop from old documents without chronology resurrects systems that were
deliberately abandoned.

**No research or authoring state is shared across lanes.** No registry, no index
of sources, no aggregate of what has been read, no cross-lane synchronization.
Any temporary run state is per-source and lane-local, disposable, and
noncanonical.

*Runtime skill dependencies are a separate concern.* Accepted `metaskills` and
declared prerequisite skill packages within a skill family are legitimate
architecture. This procedure neither resolves nor forbids them, and must not be
cited as grounds for removing them.

**A card must survive its source.** No `source_id`, locator, page number, or hash
on a card. If a card cannot teach its decision with the book gone, the extraction
is incomplete. Optional human-readable attribution (`source_title`, `author`) and
genuine asset references are *not* retired provenance and are unaffected.

**Generated indexes are derived, never canonical.** Cards are the source of
truth. If deleting an index destroys knowledge or authoring state, it has become
another ledger.

**Card IDs are checked at two gates.** During authoring, uniqueness is checked
inside your own package plus shared packages — an isolated lane cannot prove
global uniqueness and must not be made to load unrelated domains to try.
Repository-wide uniqueness is checked at integration.

**Protected semantics.** This procedure does not reopen settled domain theory.
For Art specifically, the P/C framework and the frozen Stages architecture are
not modified unless that work is explicitly opened.

### Session boundaries are not unit boundaries

**A unit boundary is set by instruction** — where the author closes an X. It
never moves because a context window is small.

**A session boundary is set by context exhaustion**, and environments differ in
both how much they have and how they fail. Some expose a visible budget and
degrade gradually; others stop hard, mid-operation, with no warning. Where the
failure is abrupt and unsignalled, write handoffs **opportunistically at natural
breakpoints** — after a unit closes, after a discussion thread resolves —
because there may be no chance at the boundary itself. Resuming from the last
visible step is reconstruction, not a handoff: a valid fallback, not a plan.

Discussion that produces judgment rather than closed units still consumes the
window. Long theory threads warrant a checkpoint sooner than the unit rhythm
alone suggests.

**When a unit does not fit the remaining context, do not split the unit.**
Splitting a unit for context reasons is precisely how a four-unit book becomes a
151-unit one. Checkpoint and resume the same unit elsewhere.

**Handoff artifact.** External, disposable, never authoritative. A stale one is
discarded. It carries only what the next session needs to resume without
re-deriving:

```
- the source, the unit, and where in it work stopped
- the unit plan and which units are already closed
- staged information from the first read, if the boundary falls between reads
- checkpoint answers already given
- corrections and decisions that must not be silently reversed
- known traps from earlier units of this source
- the exact next action
```

This is not a ledger, registry, or source record. It spans no domains, aggregates
nothing, and no particular structure or name is required.

---

## 1. Preflight

Run once per source, before reading. Output is short: what the source is, how
many units, and what to expect from each. It is a stateless inspection — it
writes no persistent state, claims no source, and records nothing about what has
been read.

### 1.1 Determine the subject from the instruction, not the wrapper

**The subject is what the instructional body teaches you to do.** Not the title,
not the preface, not the publisher's category, not the audience the front matter
addresses.

A preface addressed to instructors is metadata about the preface. It is not
evidence that a craft book is about pedagogy. Front matter is read for
orientation — what the author thinks the book is, who they imagine the reader to
be, how it is organized — and is then **barred from setting the subject.**

State the subject explicitly in the preflight output and confirm it before the
run starts, while a wrong inference still costs nothing.

### 1.2 Adjudicate units

> **A unit is the largest span after which the author could say "now you can do
> X" — for exactly one X.**

Floor and ceiling are both in that sentence. A subsection that cannot complete an
X rolls up. A span covering two X's splits.

**Three disqualifiers, applied first:**

| kind | test | disposition |
|---|---|---|
| front / back matter | describes the book to someone choosing or assigning it | read, `no-extract`, may not set the subject |
| exhibited work | the instruction points *at* it | evidence — attaches to the unit that discusses it |
| dependent subsection | meaningless outside its parent | roll up |

An anthology selection, plate, model example, or worked painting is evidence. It
becomes its own unit only when the author has built a sequence that functions as
a lesson in its own right.

Front matter that genuinely teaches durable craft can earn treatment — the test
is whether it instructs, not where it sits in the page numbering. Title pages,
dedications, acknowledgements, and publishing notes never do.

**Two checks, applied after:**

- **Roll-up** — merge two adjacent candidates. Still one X? One unit. Forces an
  "and also"? Two.
- **Split** — **both** of these must hold before a candidate divides:
  1. it teaches two things a practitioner would reach for separately, **and**
  2. **each half independently teaches more than one durable decision.**

**The second condition is the floor, and it is not optional.** A span that
reduces to a single decision is a *card*, not a unit — leave it inside its
parent. A named form, one technique, one constraint set, or one rule is
card-sized. The section that collects a dozen of them is unit-sized.

The checks are deliberately symmetric. Roll-up is bounded above: merge far enough
and you are forced into "and also." Without condition 2, split is bounded by
nothing — "would a practitioner reach for these separately?" stays true at
arbitrarily fine grain (sonnet vs. sestina, iambic vs. trochaic, full rhyme vs.
slant), so the check never stops firing. Condition 2 is what makes it stop.

**Grain check.** After adjudicating, compare the units against one another. If
the set contains both very short and very long units, one criterion has not been
applied consistently — identify which end moved and re-test that end. A
two-page unit sitting beside a thirty-page unit is a defect in the adjudication,
not a property of the source.

**The unit scheme is provisional.** Sketch it whole at preflight, then follow
instructional continuity when the read disagrees with a divider on the page.

Do not target a unit count. Do not use page count as the criterion. **Never let a
context budget set a unit boundary** (§0).

### 1.3 Map each unit to a library region

For each unit, name the region(s) of your own domain it will land in and count
the cards already there. Coverage is **per unit against its region** — never per
book, never per lane. A single source routinely contains both saturated and empty
units.

Predict the **disposition mix**, not a card count:

```
empty region  -> new-heavy
partial       -> mixed
saturated     -> refinements and variants likely; new cards rare and valuable
```

Card count is not a yield metric. A chapter may collapse eight named techniques
into one ordered AP; that is a success, and counting cards reads it as a failure.

### 1.4 Choose a provisional reading mode

| mode | when | shape |
|---|---|---|
| **unit ingestion** | sparse or new territory; cumulative instruction | unit-sized double read |
| **curriculum audit** | mature region; corroborative, corrective, or specialist source | whole-source structural pass, then deep reread where unresolved delta may exist |

Signals: library maturity in the subject, the source's likely role (foundational
vs. corroborative), whether instruction is cumulative or topical, and expected
collision density.

Unit ingestion is the safe default. Audit mode becomes appropriate as a region
matures. **The choice is a hypothesis and must remain reversible** — a source
that looks redundant from its contents can reveal a different mental model once
read, and a supposedly foundational one can turn out to be mostly corroboration.

Audit mode is not keyword skimming and does not exempt anyone from understanding
the whole source. What changes is that structural routing replaces automatic
per-chapter descent.

### 1.5 Preflight output

```
<title> — <author>
domain: <lane>     <extent>     text: <quality>
subject: <what the instruction teaches you to do>
         (NOT set by front matter)
mode:    <unit ingestion | curriculum audit>  (provisional)

N units
  u01  <label>   <locator>   -> <region> (<n> prior)   <expected mix>
  ...

no-extract: <front/back matter sections>
```

---

## 2. The run

Two execution branches. The reading discipline (§2.1–§2.3) is identical in both;
what differs is the scope each pass covers.

```text
UNIT INGESTION                      CURRICULUM AUDIT

first read of the unit              whole-source structural read
        ↓                                   ↓
                                    map where unresolved delta
                                    may exist
        ↓                                   ↓
    checkpoint if needed            checkpoint if needed
        ↓                                   ↓
second read of the unit             deep reread of those bounded
                                    sections
        ↓                                   ↓
      extract                             extract
        ↓                                   ↓
 reconcile / disposition          reconcile against mature owners
        ↓                                   ↓
    close the unit                close the audited sections
```

Audit mode still requires understanding the whole source; the structural pass is
a read, not a scan. It does not license extracting from a section that was never
properly read.

### 2.1 First read — deep, and pre-extractive

Read the actual material. Not the contents, not the chapter title, not prior
knowledge of the subject.

The first read answers **"what is the author teaching?"** — not "what cards can I
make?" Its output is *staged information*: provisional decisions, suspected
overlaps, things that might be methods rather than laws. **It does not produce
card names.**

Naming on the first read anchors the second, which then degrades into finding
support for names already chosen. Staged information does three jobs a hardened
list cannot:

1. it makes ambiguity visible, which is what generates the questions;
2. it gives the second read a "was this worth keeping?" reference point;
3. it leaves the topology free to change.

**For visual domains, image inspection is part of reading, not a later
verification pass.** Read the text, inspect every page of the bounded scope, then
inspect candidate-bearing pages closely. Compare what the prose claims against
what the image demonstrates — often the image carries the mechanism more clearly
than the prose, and sometimes it makes a literal verbal reading untenable. A
procedure that reads all text and then optionally looks at figures will reproduce
bad ingestion.

If the material cannot be read — missing, garbled, images you cannot inspect —
say so and stop. Output that looks structured is not evidence anything was read.

### 2.2 Checkpoint

Between the reads, surface what the staged information exposed.

**A question is justified by consequence:** would a plausible answer materially
change a card's scope, ownership, placement, or truth? If no, resolve it
yourself. If yes and the evidence cannot settle it, stop and ask.

Who resolves it depends on **the type of uncertainty, not the lane**:

- **Source and library evidence** settle factual, structural, and
  already-canonical questions. Resolve these yourself and state the reasoning.
- **Practitioner judgment** settles questions whose answer depends on intended
  practice, visual interpretation, style, or domain authority the sources do not
  establish. These need the practitioner.

Do not invent questions as ceremony. An empty checkpoint is a valid and
informative result — as a lane matures, most scope questions become answerable
from accumulated judgment, and the volume falling toward zero is a mastery
signal, not a skipped step.

*Observed tendency, not a rule:* Art has historically produced more
practitioner-dependent checkpoints than Software Engineering, and that gap
narrowed as judgment accumulated. Any domain can produce either kind.

A source conflicting with an existing card is always surfaced, even where it is
resolved independently. Two contradictory cards with no record that anyone
noticed is worse than either answer.

**Possible supersessions are flagged here, not classified here.** The first read
may say "this appears inconsistent with owner X." It may not yet say "replace
owner X." That conclusion has to survive the second read and the duplicate guard.

### 2.3 Second read — full coverage, then extract

Re-read the scope **in full, from scratch**. Coverage is not negotiable; **depth
is adaptive.**

Known material resolves rapidly against existing knowledge — that is recognition
working, not attention lapsing. Unresolved residue gets slower, fuller attention.
In a saturated region most of the text resolves on contact and the pass moves
quickly, but the budget *concentrates on the residue*; it does not shrink. This
is never a scan for headings or candidate keywords.

Extraction happens **here**, with the staged information, the answers, and the
neighbouring cards all in hand.

Separate two questions and keep them separate:

- what did the source teach?
- where does that belong in our library?

Collapsing them lets a current card rewrite the author in your head.

What the second read reliably catches: a caveat that kills a universal reading;
an attractive example that is not a transferable skill; two decisions merged into
one candidate; a "new" skill that is an alternate method under an existing owner;
a method broader than the author's terminology; a drill with no distinct practice
target; an AP that merely strings existing capabilities together.

### 2.4 Dispositions

Duplicate-guarding is **domain-local**. Retrieve a small plausible owner set —
often around five — and read it. **Expand whenever a collision, refinement, or
replacement remains uncertain**; this is an efficiency heuristic, never a limit.
Replacement in particular may require inspecting the whole relevant dependency
neighbourhood.

Then decide exactly one disposition per candidate:

```
new       no existing card teaches this        -> write it
refine    the existing owner is correct but    -> improve the owner in place
          incomplete or underspecified
variant   same decision, different valid       -> absorb into the foundation
          method / sequence / constraint
replace   the existing owner is too narrow     -> §2.5 migration
          or wrong, and this fully contains it
reject    adds nothing durable                 -> write nothing
```

**Refinement** covers the common case where a source sharpens an owner without
supplying an alternate method and without superseding it: a better boundary, a
missing failure condition, a clearer operational test, sharper wording. Without
it, agents are forced to manufacture an unnecessary variant, overstate a
replacement, or discard useful sharpening. It is also the cheapest disposition —
the ID does not change, so no links move.

**Variant is the default answer to legitimate disagreement.** Different-but-valid
is a variant. Only "the old owner is actually wrong or too narrow, and the new
one fully contains it" earns replacement. "Newer" is not "better." If you cannot
show *better and encompassing*, it is not a replacement.

Additional bars:

- A demonstration does not earn a **Drill**. A Drill needs a capability worth
  practicing, a concrete practice act, a success condition, and enough reuse to
  justify permanent residence.
- A sequence does not earn an **AP**. "Use A, then B, then C" is not an AP unless
  the orchestration itself is a durable reusable decision.
- Do not let a source colonize the library. An author may contribute a way to
  solve a problem; they may not turn the domain into "do it their way."
- **An empty unit is a real result.** Never manufacture objects to make a unit
  look productive.

### 2.5 Replacement is a dependency-graph migration

Replacing a card is not a local authoring operation. Dangling links fail
validation, so a naive deletion is impossible — which is why lanes without this
procedure never replace anything and accumulate early mistakes permanently.

```
1.  identify the old owner's capability
2.  prove the new candidate contains it, not merely overlaps it
3.  confirm the new rule extends or corrects the old boundary
4.  preserve useful old behaviour inside the successor
5.  keep good source-specific methods as variants; do not discard them
6.  retire the old ID
7.  find every incoming relation to it
8.  repoint each one — only where the semantic relation still holds
9.  check foundation_object_id, prerequisite_for, drill targets, AP dependencies
10. search again for the old ID
11. validate and rebuild indexes
```

The test is not "grep returns zero." It is **did every incoming relationship
migrate to the right concept.** A prerequisite pointing at the old owner probably
needs the successor; a historical note mentioning the retired ID does not.

Reading order is `prerequisite_for`. It is not `foundation_role`, which answers a
portability question. Replacement can require changing prerequisite edges, not
just the card's own body.

True supersession is rare — expect it a few times per curriculum, not per unit.
Prefer refinement or variant whenever either honestly fits.

### 2.6 Present the delta, then land it

Extraction and dispositions produce a **proposed delta**, not a mutation. Present
it — new cards, refinements, variants with their foundations, replacements with
their migrations, rejections with reasons — and land only what is approved.

The approval's weight follows §2.2: where the answer needs practitioner judgment,
this is a real gate and the run waits; where evidence settles it, the delta is
stated and the landing is the gate.

Then validate, verify references, regenerate indexes, and land the change.

**One closed unit, one atomic approved change set.** Commit it where the
environment supports commits; where it does not, the accepted change set is
atomic all the same. Git is not PASS architecture.

---

## 3. Checking the run against the prediction

| preflight predicted | first read found | reading |
|---|---|---|
| little (dense region) | little | prediction landed |
| little (dense region) | **something** | **the valuable case** — a multi-book miss |
| lots (empty region) | lots | prediction landed |
| lots (empty region) | **little** | **unexpected — recheck before accepting** |

The bottom row is why predicting is worth anything. It is a **diagnostic prior,
not a verdict**: an apparently empty region can legitimately produce little from
a weak source, obsolete material, non-operational exposition, demonstrations
rather than transferable decisions, or a source whose real subject is not what
its wrapper suggested. Recheck, then accept or correct.

A prediction catches something the finished cards cannot — **absent cards leave
no trace, so a thin extraction is invisible in a review of what was produced.**
It is not the only diagnostic; source explanation, visual inspection, rejection
reasoning, and owner comparison all bear on it. It is the one that fires before
the output exists to be reviewed.

A spike in a saturated region is not suspicious. It is the highest-value output
the system produces, and the reason for reading multiple sources on one subject:
each catches what the others structurally could not.

### "No new cards" is honest only if all of these hold

- the bounded scope was actually read
- for visual domains, the meaningful visuals were actually inspected
- it was read again
- the source's teaching can be explained in the source's own terms
- each durable decision was compared against its nearest owners
- every rejection can be named: already covered, too narrow, non-operational,
  obsolete, or merely demonstrative

If the teaching cannot be explained, "no cards" is suspect. If it can be
explained and the covering owners can be pointed at, "no cards" is a successful
result.

---

## 4. Close

Report **named dispositions**, not counts. A variant names its foundation and the
method that differed. A refinement names what it sharpened. A rejection names
why. This is the only artifact that distinguishes a mature library correctly
declining material from an agent that read badly — the counts are identical.

Discard the run state. The accepted cards are what remains.

### Stopping early

**Saturation is not a stopping condition.** A mature region changes *how* you
read — audit mode, faster recognition — not *whether* the source is worth
reading. The most valuable findings in mature areas are precisely the boundaries,
errors, and supersessions that only a mature library can recognize; stopping
because coverage is high forfeits exactly those.

Valid reasons to stop before the end of a source:

- the source leaves the intended curriculum scope
- the source changes subject into a domain outside this run
- the practitioner scoped only part of the source
- a whole-source audit establishes that remaining material lies outside the
  target capability

"We already know a lot about this" is not one of them.

---

## 5. What does not go in the library

Three classes of knowledge exist. Only the first is a repository concern.

1. **Canonical skillset** — general, reusable, source-independent. This is
   `library/`.
2. **Practice history** — what repeated attempts reveal about application,
   failure, calibration. Real and useful; not canon.
3. **Practitioner-specific** — stable personal choices, style preferences,
   recurring individual weaknesses. Belongs to the practitioner.

**Layer 2 is deferred, not rejected.** The *exploratory design goal* is for
practice history to travel with, or remain available alongside, its skillset. **No
persistence architecture has been accepted**, and nothing here may be read as
requiring one. It must not become a validator or build dependency, and it must
not be rebuilt as an authoring workspace under a new name. It is not built yet
because it requires a body of actual drill runs and produced work to learn from,
and that follows a skillset being complete rather than preceding it.

What holds now is narrower: **practice history must not enter cards.** A card
stays general, reusable, and source-independent. An observation from one attempt
is not a Pattern. Wherever layer 2 eventually lands, it sits beside the canonical
cards, never inside them.

Layer 3 currently lives per-lane outside the repository, and that is the right
place for it. Forcing personal calibration into the library contaminates it for
every consumer; discarding it makes the practitioner reteach the system every
session.

**Attribute a failure before writing a card about it.** An unsuccessful result
does not mean the knowledge is missing:

```
knowledge    the skillset lacks the principle
retrieval    the knowledge exists but was not brought to the attempt
application  retrieved correctly, executed wrong
continuity   a later stage destroyed a decision established correctly earlier
reference    the source or reference was misread or insufficient
tool         the execution system could not perform the intended construction
interface    the instruction given to the execution system was ambiguous
```

Only the first justifies a new card. The rest are execution problems, and
treating them as knowledge gaps bloats the library with cards it never needed.

**Buffer experience before it becomes canon:**

```
attempt -> observation -> repeated evidence -> possible library refinement
```

never

```
attempt -> observation -> new card
```

---

## Measuring a run

Measure the **quality of the delta**, not the quantity of objects. Once the
foundation exists, redundancy should collapse — a 200-page book yielding four
durable additions can mean the earlier books did their job.

**As a lane matures, becoming harder to impress is the intended outcome.**

---

# Appendix — Operating notes

**NOT DOCTRINE. Current, volatile, expected to go stale.** Move to lane operating
notes or agent instructions when landing this file; do not let it age into the
procedure.

**Project status.** No lane has yet crossed the maturity threshold into a
finished Skill Forge skillset. The work is still authoring and maturation.

**Context budgets.** Lanes currently differ substantially in window size and
failure behaviour — some expose a usable budget and degrade gradually, at least
one stops hard mid-operation with no counter and no warning. Check the current
figures for the environment you are in rather than relying on any number written
here. The doctrine that matters is in §0: a session boundary never creates a unit
boundary.

# Concurrency drill defects — repair list

> **Status 2026-08-26 — repairs 1 through 7 applied.** All eight drills' worth of
> findings that resolve to a drill edit are in the cards: B1-B3, L1-L4, the four
> VERDICT-changing unstated quantities, the Part 2a FAIL family, the Part 2b PASS
> family, the remaining SCALE items, N1 (the AP band contradiction), N2, N3, and
> the three unlisted Common Failures from Part 6. Seven drills and one AP changed;
> `validate.py`, `verify_references.py`, and `build_index.py` all clean.
>
> **Not done, deliberately.** Item 8 — CPP has still never been run and needs a
> cold session. Item 9 — G1 and G2 are held for a confirming run. All of Part 5
> is untouched, including the 5c routing notes, per its own not-actionable
> marking.

Source: eight cold sessions run 2026-08-25 against the concurrency drills, one
drill per session, no shared context. Seven produced valid runs. One failed on a
session limit and produced nothing.

**What this file is.** A list of defects in the *instruments* — the drills — with
a proposed repair for each. Everything here is fixed in a drill.

**What this file is not.** Evidence about the craft. No valid run produced a
wrong answer, so nothing below justifies authoring a card. The separate
observations about the library are in Part 5 and are marked as not-yet-actionable
on purpose. Nothing has been committed, edited, or written to memory.

**Severity vocabulary used throughout:**

| Class | Meaning |
|---|---|
| **BLOCK** | The instruction is wrong, or the drill cannot be completed as written |
| **PASS** | A Success Check bullet is satisfiable without doing the work |
| **FAIL** | A Success Check bullet rejects work that is correct |
| **SCALE** | A quantity, unit, or scale is unstated, so two correct runs disagree |

Drill short names used in the tables:

| Short | File (all under `library/software-engineering/`) |
|---|---|
| COMMIT | `core/concurrency/DRILL_name_the_committing_step_on_every_path.md` |
| LOOP | `core/concurrency/DRILL_classify_the_dependencies_in_a_loop.md` |
| FOLD | `core/concurrency/DRILL_fold_an_unsafe_interface_into_transactions.md` |
| STAMP | `core/concurrency/DRILL_replace_value_validation_with_a_version_stamp.md` |
| DECOMP | `core/concurrency/DRILL_run_the_decomposition_procedure_on_a_problem.md` |
| PRIM | `core/concurrency/DRILL_decide_whether_a_primitive_can_coordinate_the_design.md` |
| INDEX | `core/concurrency/DRILL_trace_divergence_and_coalescing_from_an_index_mapping.md` |
| CPP | `languages/cpp/concurrency/DRILL_restructure_a_class_that_locks_every_member.md` |

CPP was never run. It has no findings below and still needs a session.

---

# Part 1 — Broken instructions. Fix these first.

Three drills contain instructions that are wrong or incomplete rather than merely
loose. Unlike everything in Part 2, these misdirect a runner who is doing
everything right, and two of them let a runner pass having demonstrated nothing.

## B1 — STAMP step 1 names a schedule that does not falsify anything

**BLOCK.** Step 1 says a location *written and written back between the passes* is
the shortest falsifying schedule. It is not a falsifying schedule at all.

If both writes land strictly between the end of pass 1 and the start of pass 2,
pass 1 read its values during a genuinely quiet interval. The view it collected
*did* hold. Writes that follow and undo themselves make the view **stale**, and
stale-but-consistent is exactly what the double collect promises — linearize the
collection at the quiet moment and it is a legal snapshot.

The falsehood requires the writes to **straddle a pass**, so that values collected
at different moments within one sweep never coexisted. The drill's second
suggestion — "a location written twice to the same value" — has the same problem:
it is a necessary ingredient of a counterexample, not a schedule.

This is not ambiguity. The instruction points at a schedule that fails the
requirement stated in the same sentence ("the collected view never existed").

**Consequence.** A runner who follows it literally builds a non-falsifying
schedule and **still passes Success Check bullet 1**, because a stamp-based
validator rejects that schedule too — for the wrong reason. The drill's headline
capability goes untested and the check cannot tell.

**Repair.** Replace the guidance with something like: *the writes must be
interleaved into the collector's reads, not merely placed between the passes — a
schedule where every write lands in the gap leaves pass 1's view genuinely valid.*
Then close the hole in the check itself; see F-STAMP-1 in Part 2.

## B2 — DECOMP step 5 requires a quantity steps 3 and 4 never collect

**BLOCK.** Step 5 asks for the ratio of fixed per-transfer cost to per-value cost
at which the answer flips. That ratio cannot be computed from crossing *volumes*.
It needs a **transfer count** per grouping — how many messages, not how many
values.

Step 3 says "total the crossings." Step 4 says "total the crossings for each."
Neither asks for a message count anywhere in the drill. A runner who follows steps
3 and 4 exactly arrives at step 5 holding two volumes and no way to answer.

**Repair.** Step 4 should read *"total the crossings and the number of transfers
for each."* Step 3 should collect the same pair, so the two steps are comparable.

## B3 — LOOP step 3 misclassifies within-iteration pairs, and step 4 then blocks the correct remedy

**BLOCK.** Step 3 states "a write followed by a read is information flowing"
unconditionally. Applied to a *within-iteration* pair it gives the wrong answer: a
scratch scalar written at the top of the body and read below is literally a write
followed by a read, so step 3 classifies it as carrying a flow — and step 4 then
forbids privatizing it.

Privatizing that scalar is the loop's easiest and most certain win. Step 2 sets up
the within-iteration / across-iteration split correctly, but step 3 never says
that the classification which gates the remedy is the **across**-iteration one.

**Repair.** Step 3 should state that only cross-iteration pairs are classified for
remedy purposes, and that within-iteration pairs are satisfied by running the body
in source order inside whatever participant executes it. One clause; it removes
the trap entirely.

---

# Part 2 — The Success Checks. One family of defects, not seven.

Every drill has bullets satisfiable without doing the work. That alone would be
unremarkable — checks are cheap and work is not. The finding that matters is the
**inverse**, which appeared in six of the seven drills run: bullets that reject
correct answers.

The two directions have a single cause. **The Success Checks are written against
one anticipated remedy and score deviation from it as failure.** The better the
answer — the more it takes a route the author did not have in mind — the likelier
it fails. Meanwhile the anticipated remedy can be gestured at without being
performed, so the check passes it. Several bullets are, in the limit,
anti-correlated with skill.

The clearest single instance is L4 below: on LOOP, one specific catastrophic
answer passes all four bullets with a **higher apparent score** than the correct
one.

## 2a. Bullets that fail correct work (FAIL)

### F-COMMIT-1 — bullet 1 contradicts instruction 5

Instruction 5 anticipates paths with no single committing step and asks for them
to be named as design defects. Bullet 1 requires *every operation* to have at
least one committing step written down. When every path of an operation is
defective — which is the normal outcome on a structure with a second write site
outside the publishing step — the two cannot both be satisfied. A correct run
fails bullet 1.

**Repair.** Bullet 1 should read: *every path is accounted for, with a step or a
defect.*

### F-COMMIT-2 — bullet 2 rejects a commit whose line is a return

"No step named is the operation's return" means *not the moment the caller
receives a value*. Read literally it rejects a correct answer: a `size()` whose
commit is the atomic load, on a line whose source text is `return count_.load();`.

**Repair.** Say *"not the moment the caller receives the value"* and drop the word
return.

### F-PRIM-1 — bullet 1 demands a count that instruction 1 authorises omitting

Instruction 1 explicitly blesses "none" as the required-agreement answer for a
commuting structure and pre-empts the objection that it is a dodge. Bullet 1 then
demands "a thread count." *None* is not a count. A strict grader fails a correct
analysis for giving the answer the instructions told it to give.

**Repair.** *"A required-agreement count, which may be none."*

### F-PRIM-2 — bullet 2 fails a correct all-ruled-in run

The drill supplies no thread counts. A run that scopes all three designs at **two**
threads correctly rules all three in — swap coordinates exactly two, which is
exactly what is needed. That run has done the work properly, reached the right
verdicts, and fails bullet 2, which demands that at least one design be ruled out.

The queue is the only design whose verdict moves with the thread count, so bullet
2 silently requires a choice of three or more that the drill never states. See
S-PRIM-1.

### F-INDEX-1 — bullet 3 blames the wrong input, and misdirects the best run

Bullet 3 says that if **either** cost fails to move between the two mappings, the
fault is the step-1 branch distribution. True for the branch cost. **False for the
memory cost**, which is decided by record size against unit size and has nothing
to do with the branch distribution.

Concretely: set the record size to 128 bytes with a 128-byte unit, keep everything
else, and the transaction count is identical under both mappings — in a run whose
branch distribution has perfectly good group-scale structure. The bullet sends
that run back to redo step 1, which is the wrong repair.

**Repair.** Split the bullet. Branch cost did not move, check the distribution.
Memory cost did not move, check the record size against the unit size.

### F-INDEX-2 — bullet 3 is self-fulfilling

The same bullet announces the expected result and instructs the run to change its
input until it gets it. A run cannot fail as long as it keeps retuning step 1.
That is a check on persistence, not on analysis.

**Repair.** Fix the inputs (see S-INDEX-1) so the result is discovered rather than
manufactured.

### F-DECOMP-1 — bullet 1 fails the drill's own recommended follow-up

Bullet 1 demands a piece count "written as a formula in the problem's own
dimensions." The divide-and-conquer variant the drill's Notes prescribe as the
repeat exercise has no static formula — the piece count is discovered at run time.
The bullet cannot pass the drill's own suggested second run.

It also fails a correct maximal split on a small problem: a 16x16 grid on 64 cores
gives 256 pieces, correctly maximal, only 4x the processor count, and "far larger"
rejects it.

**Repair.** *"A piece count that is a property of the problem rather than of the
machine — a formula where one exists, or the rule that generates the pieces where
it does not."*

### F-DECOMP-2 — bullet 3 punishes the more honest answer

"A machine instantiated on each side of that threshold" presumes both sides are
physically inhabitable. Often they are not — for a 3-D stencil the compact-group
advantage is large enough that no fabric anyone would build flips it. Correct work
concluding *"the threshold is s/w = N and every machine that will ever run this
sits below it"* is a better answer than one that invents a fictional machine, and
it fails.

**Repair.** Append *"…or state that no realizable machine sits on one side, and
why."*

### F-STAMP-1 through F-STAMP-4 — four of five bullets fail designs the prerequisite card recommends

This is the worst case in the set and worth stating as a group.

- **Bullet 1** ("the schedule is rejected by the validation") is unsatisfiable for
  the prerequisite pattern's own preferred answer — restructure the several
  locations into one immutable object behind a single atomic handle. There is no
  validation, so the schedule cannot even be expressed against that design. The
  card explicitly says not to reach for the double collect before asking whether
  the state can live behind one handle. The best available answer fails the check.
- **Bullet 2** ("a wrapping width is named and rejected") is unsatisfiable for the
  correct `W = 1` case — a reusable barrier's alternating sense bit, which the
  prerequisite card names as its own worked example of bounded lag. There is no
  smaller width to reject.
- **Bullet 4** ("a partly-completed write is detectable") fails a design where
  every location is a single naturally-atomic word. The correct answer is *"the
  case cannot arise, here is why"*, which does not satisfy "is detectable."
- **Bullet 5** ("repeated failure has a defined outcome") fails a wait-free
  collector upgraded by helping, which cannot fail repeatedly by construction. The
  design that most thoroughly solves the problem is the one the bullet cannot
  score.

**Repair.** Each needs an escape clause of the form *"…or its impossibility is
argued."* Bullets 1 and 2 need more than that — they need to admit the
restructure-instead route as a first-class answer rather than an omission, which
means the check has to branch on which remedy was taken.

### F-LOOP-1 — bullet 2 fails reductions and closed forms

Bullet 2 requires that "any location carrying both a flow and a name conflict is
identified as such and **left shared**." An accumulator carries a flow and two
name conflicts; a fixed-stride counter carries three flows and four. The correct
remedies — a reduction and a closed form — leave neither location shared. A
literal grader marks correct work as failed.

The bullet conflates "carries a flow" with "must stay shared," which step 5
explicitly contradicts by authorising flow removal wherever an algorithmic form
exists.

**Repair.** *"…left shared where the flow survives step 5."*

### F-LOOP-2 — Common Failure 3 indicts the correct technique

"Privatizing a location that a genuine flow runs through" is exactly what a
reduction does. It is legitimate because the flow is removed by reassociation
first and the privatization follows. As stated, the listed failure condemns the
right move.

**Repair.** *"Privatizing a location that a genuine flow still runs through after
step 5."*

### F-FOLD-1 — bullet 2 fails a correct snapshot

A `snapshot()` returning an owned copy of the contents under one lock reports a
fact about the contents and acts on nothing. It is a complete transaction, it
cannot serve as a precondition, and it is a good design for a monitoring path.
Bullet 2 flags it unless the runner invokes the "documented as advisory" escape,
which fits badly — a snapshot is not advisory, it is an exact record of one
committed state.

The bullet's real target is *a query whose value another operation's correctness
could depend on*. "Reports a fact about the contents" is a wider net.

### F-FOLD-2 — bullet 3 fails a blocking fold

A `wait_and_pop(T& out)` that does not return until an element exists is a
legitimate fold with no "ordinary return value" for the empty case. Read
literally, bullet 3 fails it.

**Repair.** *"…now an ordinary return value, or the wait that replaces it has an
exit other than the arrival it waits for."*

## 2b. Bullets satisfiable without doing the work (PASS)

Listed more briefly. These matter less than 2a — a check that can be gamed still
guides an honest runner — except where they combine, which is L4.

| ID | Drill | Bullet | How it breaks |
|---|---|---|---|
| P-COMMIT-1 | COMMIT | b1 | Counts steps, does not check them. "The lock release" nine times passes on a fully-locked structure. |
| P-COMMIT-2 | COMMIT | b2 | A formatting check. Naming a plausible but wrong line passes cleanly. |
| P-COMMIT-3 | COMMIT | b3 | Nothing requires the rejected candidate to be one a reviewer would propose. Rejecting the allocation is a strawman that satisfies the letter. |
| P-COMMIT-4 | COMMIT | b4 | Vacuous unless a defect was already found. A run that misses the two-stage publication has no path lacking a step and satisfies it by having nothing to identify. |
| P-PRIM-1 | PRIM | b1 | Checks the *form* of the inference, not its inputs. Writing the toucher count for all three designs yields verdicts that genuinely follow, are internally consistent, and are wrong. The drill's headline discrimination — agreers vs touchers — is checked by no bullet. |
| P-PRIM-2 | PRIM | b2 | Does not say *which* design, so ruling out the wrong one passes; sets no ceiling, so ruling out all three passes. |
| P-PRIM-3 | PRIM | b3 | Instruction 5 supplies the required sentence verbatim. Copying it passes. Tests transcription. |
| P-INDEX-1 | INDEX | b1 | Ordering and format check. Declare the unit, then emit any two integers with confident labels. |
| P-INDEX-2 | INDEX | b2 | With a two-sided branch the per-group answer space is {1,2}, so "2 paths" is right by default. The invariance clause is worse — see L2. |
| P-DECOMP-1 | DECOMP | b1 | "N-squared" is what anyone writes on seeing a grid. For in-place Gauss-Seidel it is **wrong** — the independent sets are the anti-diagonals — and it passes unchallenged. |
| P-DECOMP-2 | DECOMP | b2 | Verifies only that two numbers exist. Not the arithmetic, not comparability, not derivation. |
| P-DECOMP-3 | DECOMP | b4 | Answerable by paraphrasing the parent AP, which already states that three of four steps are relative to the processor count. Nothing constructed. |
| P-STAMP-1 | STAMP | b1 | Rejection is one-sided. A validator that *always* returns no-consistent-view passes perfectly. |
| P-STAMP-2 | STAMP | b3 | Satisfiable by restating the premise. "No fixed width is safe" contains no proposal and satisfies both halves. |
| P-STAMP-3 | STAMP | b5 | Any bounded loop passes — including one that returns the unvalidated view after N attempts, a correctness bug the bullet reads as a "defined outcome." |
| P-LOOP-1 | LOOP | b1 | Demands a remedy be *named*, not that the classification be correct. Mechanically emitting anti/output to privatize and flow to change-the-algorithm passes in full. |
| P-LOOP-2 | LOOP | b2 | Requires the reason be *written*, not true. An asserted "no other iteration uses this value" passes and may be false. |
| P-FOLD-1 | FOLD | b1 | Passable by relabeling: keep the whole original interface and redefine every precondition as defined behaviour. No contract requires anything; nothing was folded; the interleaving still works. |
| P-FOLD-2 | FOLD | b3 | Does not require the value to reach the caller, does not require distinguishing kinds of absence, does not require the removal-before-handing-back question to be answered. |

## 2c. Four compound defects worth separate attention

### L1 — COMMIT's whole check passes a run that found nothing

P-COMMIT-1 through P-COMMIT-4 combine. Bullets 1 to 3 accept any plausible-looking
line assignment; bullet 4 is vacuous unless a defect was already found. A runner
who misses the two-stage publication entirely reports nine clean steps and passes
all four bullets — on a structure that is not linearizable. Given the drill's own
Notes call it "diagnostic more than probative," the check does not check the thing
the drill says it is for.

**Repair.** Add a bullet requiring a verdict: *state whether the structure is
linearizable, and for at least one path show the observer call and the window that
proves it, or show that no such window exists.*

### L2 — INDEX's invariance clause cannot fail

Bullet 2 asserts that branch cost does not change when proportion changes without
changing distribution. No instruction step asks a run to vary the proportion at
fixed distribution. A run that follows the Instructions exactly produces no
evidence bearing on the clause, so the clause cannot fail. It is decoration.

**Repair.** Add an instruction step that varies the proportion at fixed
distribution — or widen the branch to three ways, or make it a data-dependent trip
count, so the path sum has a real range and the claim has something to bite on.

### L3 — FOLD's bullet 4 calibrates its own difficulty

"The failing interleaving from step 2 can no longer be constructed" is
self-referential to the run's own step 2. A weak step 2 — two threads both calling
pop on a one-element queue — makes bullet 4 trivial. The check sets its bar to the
effort already spent, which is the one property a verification step must not have.

It cannot be gamed dishonestly, but it is passed cheaply by anyone who was going
to be cheap in step 2 anyway.

**Repair.** Give step 2 a floor: the interleaving must contain at least one call
whose *result* the caller carries across another thread's committed change, and
the damage must be named (duplicate execution, precondition violation, lost item,
escaped reference).

### L4 — LOOP's checks reward the fatal error

The single worst answer — privatize every location including the ones carrying
flows — passes all four bullets, and scores *better* than the correct answer:

- b3 "all shared-name conflicts are gone" is **maximally** satisfied. Zero remain.
- b4 "any surviving flow is stated" is satisfied **vacuously**. There are none.
- b1 is satisfied by a fully populated table with a remedy per row.
- b2 is satisfied by an asserted reason that need not be true.

Nothing reordered, nothing left shared, a perfect-looking score, and a loop that
silently computes different numbers. Bullet 3 alone cannot distinguish correct
privatization from catastrophic privatization; it leans entirely on bullet 2's
honour system, which per P-LOOP-2 does not have to be true.

**Repair.** Bullet 3 needs a companion requiring that the restructured loop
reproduce the original's results, with any deviation declared and attributed to a
named step-5 algorithm change. That single addition converts the fatal answer from
a top score to an immediate failure.

---

# Part 3 — Unstated quantities (SCALE)

All seven drills leave a quantity open. Most only make counts incomparable between
runs. Four change the **verdict**, and those are marked.

| ID | Drill | Unstated | Effect |
|---|---|---|---|
| **S-DECOMP-1** | DECOMP | **Jacobi vs in-place Gauss-Seidel** | **VERDICT.** Sits under the drill's first quantitative step. Changes the maximal piece count from N-squared to roughly N. The two have *identical source structure* — the same row-major double loop — and completely different dependency graphs. A runner who never notices the choice exists gets a number that is right or wrong by luck and cannot tell which. |
| **S-INDEX-1** | INDEX | **Record size** | **VERDICT.** Step 3 rightly forces the memory unit to be declared because the counts depend on it. The counts depend equally on record size, and step 6 asks "which single change bought the most" as though it had a stable answer. It is a function of record size against unit size. A run with 128-byte records correctly reaches the opposite verdict. |
| **S-PRIM-1** | PRIM | **Thread count** | **VERDICT.** The whole drill compares a required-agreement count against a primitive ceiling, and supplies only the ceiling side. At two threads the queue is correctly ruled in; at three or more, correctly out. See F-PRIM-2. One clause in the Practice Task fixes it. |
| **S-DECOMP-2** | DECOMP | **Whether both groupings use the same group count** | **VERDICT of the comparison.** Step 5 asserts that computation is identical across the two groupings and therefore cancels. That is *only true* when the group counts match and groups are equal-area. The drill asserts the premise instead of imposing the condition that makes it true. A legal run at 640 strips against 6400 tiles compares two different things. |
| S-COMMIT-1 | COMMIT | Subject size; whether to include incidental read-only operations; outcome granularity | A queue with size/isEmpty/peek yields 5 operations and 9 paths; a Treiber stack yields 2 and roughly 4. A runner who writes a lean interface does strictly less work and still passes — and the read-only operations are where the most interesting findings live. |
| S-LOOP-1 | LOOP | Counting granularity | The same loop yields **15** conflicts counting statement pairs, **12** counting one entry per location-and-kind, **4** counting locations. All three are defensible readings of "every pair of touches." Two correct runs differ by nearly 4x with no way to reconcile. |
| S-LOOP-2 | LOOP | Numeric-equivalence standard | Whether the restructured loop must reproduce the original bit-for-bit decides whether the answer is "one flow survives" or "none does." |
| S-STAMP-1 | STAMP | **Write rate per location** | Load-bearing. Wrap is a function of *writes elapsed*, not time elapsed. Step 3 names the delay bound and omits the write rate, then the Success Check demands numbers. This is what makes a dimensionally wrong derivation pass bullet 2. |
| S-STAMP-2 | STAMP | The delay bound itself | Microseconds, a scheduling quantum, a page-fault storm, and a debugger are four regimes giving widths of roughly 16, 24, 32, and "none works." Two correct runs disagree by two orders of magnitude. |
| S-STAMP-3 | STAMP | Whether the counter advances by 1 or 2 per write | **Internally inconsistent.** Step 2 says "advances on every write"; step 4 then requires advancing twice per write. A runner doing step 3 before step 4 — the specified order — derives a width that step 4 invalidates. |
| S-STAMP-4 | STAMP | Value width | Step 4's partly-completed-write handling is only needed if a value exceeds one atomic word. The drill neither states this nor asks the runner to decide it — and per F-STAMP-4, a run with single-word values fails bullet 4 for being right. |
| S-FOLD-1 | FOLD | Bounded vs unbounded collection | On an unbounded queue push is total, there is no full(), and the entire producer-side fold does not exist. A run choosing unbounded does strictly less work and is equally compliant. |
| S-FOLD-2 | FOLD | Starting operation-set size; whether special member functions are in scope | Every count is an artifact of the interface the runner invented. The prerequisite pattern raises move-construction as a folding concern, which suggests special members are in scope; the drill never says. |
| S-INDEX-2 | INDEX | Group size, field offset, run length; per-instruction vs kernel-aggregated reporting | Per-group-instruction the two mappings are barely distinguishable (2 vs 2-or-1); aggregated they are 128 vs 102. A run reporting only the former satisfies the instructions and makes step 6 nearly impossible to state. |
| S-DECOMP-3 | DECOMP | The crossing unit | Directed vs undirected is a factor of 2; values vs bytes is a factor of 8. Step 5 compares step 4's totals against step 3's, so the unit must be identical across steps — which the drill relies on and never states. |
| S-DECOMP-4 | DECOMP | Grid size, processor count, where in the band to place the group count, tile aspect ratio, stencil width, boundary treatment | "Rectangular tiles" permits a 1xG rectangle, which *is* a strip — grouping B legally collapses into grouping A, giving two identical numbers and a vacuous comparison. |
| S-PRIM-2 | PRIM | — | Nothing else. Tier is a closed three-valued vocabulary supplied by the pattern, and the verdicts are binary. |

**General repair.** Extend the discipline STAMP step 3 and INDEX step 3 already
apply to one quantity — *declare it before you count, because the counts depend on
it* — to every quantity the counts depend on. Where the drill wants comparable
results across runs, fix the value in Setup instead.

---

# Part 4 — Two structural notes on the drills

## N1 — DECOMP disagrees with its parent AP on two bands

The drill says the piece count "should exceed the execution units by at least an
order of magnitude" — a floor. `AP_design_a_parallel_decomposition` says "aim for
one to two orders of magnitude more pieces than execution units," which reads as a
target with a ceiling, and is incompatible with the AP's own "split as finely as
the algorithm allows" in the same sentence. On a 4096-squared grid you cannot both
split maximally and land at 100x the processor count; maximal is 262,144x.

The drill's floor-only phrasing is the correct resolution. The AP's is not, and the
AP is what a reader reaches first. The two also give different bands for the group
count in step 4.

**Repair.** Fix the AP. This is the only defect in the list that touches a card
rather than a drill, and it is a wording repair, not new content.

## N2 — Instructions that give away their own answer

- **PRIM instruction 1** names commutativity, states that such a structure needs no
  agreement, and pre-empts the objection that "none" is a dodge — all before the
  reader looks at the counter. Design A is thereafter unearnable. It is also the
  *only* one of the three designs that separates the agreer count from the toucher
  count, so the giveaway lands precisely on the case that would have tested the
  drill's headline failure mode.
- **PRIM instruction 5** supplies the sentence bullet 3 then checks for, verbatim.
  See P-PRIM-3.
- **STAMP** and **COMMIT** do not have this problem.

**Repair.** Move the commutativity explanation out of the instruction and into the
Notes, or into the pattern card where it belongs.

## N3 — Instructions with an undefined referent

**FOLD instruction 1** uses a definite article — "the operations" — for a
collection the drill never supplies (Setup: "No special setup required"). Same for
**STAMP step 6**, which says "apply the same reasoning to a conditional update
elsewhere in the design" when no design was given; a runner who built a bare
two-register example has nowhere to apply it and must retroactively invent a second
component. Same for **DECOMP** and **INDEX**, whose entire numeric output is a
property of the example the runner invents.

**Repair.** One sentence in Setup naming a concrete starting artifact. This also
closes S-FOLD-1, S-FOLD-2, S-DECOMP-4, and S-INDEX-2 at no cost.

---

# Part 5 — Library observations. Not actionable yet.

These are **not** drill defects and none of them is a demonstrated capability
failure. Every valid run reached correct work. Recorded here so they are not lost,
explicitly marked as not justifying authoring on this evidence alone.

Under hard rule 15, authoring is justified only where the gap is a missing
reusable decision (a Pattern) or a missing reusable orchestration (an AP).
Retrieval, application, continuity, reference, tool, and interface failures
justify nothing. Everything below was found by *drill critique*, not by a
capability failing in application, which is weaker evidence than it looks.

## 5a. Two candidates that would be Patterns if confirmed

**G1 — the two-term communication cost model.** DECOMP step 5 turns entirely on
separating fixed per-transfer cost from per-value cost, and **no card states it**.
`PAT_decide_if_the_problem_is_worth_parallelizing` comes closest — "price the
coordination explicitly," and it inventories the components — but never gives the
two-term form and never separates message *count* from message *volume* as
independently priced quantities. That separation is the whole content of step 5.
The run supplied it from outside the library. A runner without it cannot complete
step 5 or satisfy bullet 3.

This is the only gap that blocked completion from the library alone.

**G2 — surface-to-volume.** Perimeter grows as the side while area grows as the
side squared, so compact groups minimise crossings per unit of work. This is the
central quantitative fact both DECOMP and INDEX are built to teach, and no card
carries it. `PAT_place_cooperating_work_at_the_narrowest_scope_that_holds_it` is
the nearest and is GPU-scoped. A learner arrives at it by doing the arithmetic, as
the drills intend, but there is no Pattern for the insight to land in afterwards.

**Recommendation for both: hold.** Confirm with a second independent run before
authoring. If G1 and G2 are both real they may be one card rather than two, and
they are shared by two drills, which is the shape of a Pattern the topic is
missing rather than two local omissions.

## 5b. Four additions to existing cards

Smaller, and none is a new card.

| ID | Card | Addition |
|---|---|---|
| G3 | `PAT_check_a_primitives_coordination_power_before_designing_on_it` | **A method for counting the threads that must agree.** The card asks the question in its Checklist and never says how to answer it. It is the input to every verdict and is the drill's headline failure mode. The content is small: agreement is required exactly where operations do not commute *in their results*, and the count is the number of threads that may concurrently contend for one outcome — not the number that touch the structure, and not the size of the thread pool. |
| G4 | same card | **Mark which comparison is operative.** "Apply the same test to the objects you already have" leads a reader to compare an object's ceiling against a primitive's. For a queue built from swap both are 2, and that comparison forbids nothing — yet the design is still out, because the required agreement count is 8. One sentence. This cost a run a wrong turn and would cost a less suspicious reader a wrong verdict. |
| G5 | `PAT_classify_a_dependency_before_trying_to_remove_it` | **Add the general first-order affine recurrence to the list of known algorithmic forms.** The card names accumulator-as-reduction, running-value-as-scan, and counter-as-closed-form. It does not say that `x[i] = a_i*x[i-1] + b_i` is a scan, via the associativity of affine-map composition. That is the fact that turns an in-place stencil from "irreducible" into "reducible at a stated numeric cost." Without it the honest library-only answer is weaker than the card's own "look for the known algorithmic answers before concluding a loop is sequential" demands. |
| G6 | `PAT_make_every_concurrent_operation_a_complete_transaction` | **Multiplicity of absence, and a ranking of the three return shapes.** The card says "give the return type room to express absence" — singular. When there are two kinds of nothing (empty-now vs closed-forever), a bare bool silently reconstructs the original read-then-act bug one level along. Separately, the card offers optional, value-and-flag, and bool-with-out-parameter as equals; they are not equals under exception safety, since only the out-parameter form can assign before committing and so is strongly safe for arbitrary T. The ranking is derivable from the same card's "remove only after the result is safely constructed" bullet but is not stated, and a runner reaching for optional gets no warning. |

## 5c. Routing, not content

- **COMMIT** cross-links the two obvious patterns but not
  `PAT_atomic_steps_do_not_compose_into_a_safe_whole`, which is what actually names
  the defect the drill is built to surface. Arguably a third prerequisite.
- **INDEX** cross-links `PAT_lay_data_out_for_the_group_that_reads_it_together`
  without a path, and that card lives in `core/performance/`, not the drill's own
  `core/concurrency/`. IDs are library-unique by design so this is not a defect,
  but a reader browsing from the drill's directory will not find it.

## 5d. Correctly absent

Not gaps. Recorded so they are not mistaken for gaps later.

- **Hardware figures** — write rates, scheduler delay bounds, latency and
  bandwidth numbers. These are measurements about a target machine, not craft, and
  should stay out. The repair belongs in the drills: say that the runner must
  supply them and state where they came from.
- **Group size and memory unit size.** `PAT_lay_data_out_for_the_group_that_reads_it_together`
  explicitly calls these "a value to derive rather than embed," and INDEX step 3
  correctly makes declaring the unit the run's job.

---

# Part 6 — What this evidence does not support

**No craft weakness was demonstrated.** Seven valid runs, seven Success Checks
met, zero wrong answers. The one non-met bullet (COMMIT bullet 1) was not met
*because* the answer was correct — see F-COMMIT-1.

Where a listed Common Failure occurred, it was caught **by the drill's own
instructions mid-run**, which is the instruments working even while their scoring
does not:

| Drill | Failure that occurred | What caught it |
|---|---|---|
| COMMIT | Accepting a region ("somewhere inside the tail lock") | Instruction 3's "a specific line, not a region" |
| INDEX | Reasoning about one thread's access pattern — the two mappings were labelled backwards | Enumerating the group's simultaneous addresses. Notably, *reading the card that names this exact inversion did not prevent it* |
| LOOP | Privatizing a location a genuine flow runs through — the reflex double-buffer | Asking which iteration writes the element being read |
| STAMP | Sizing the counter by feel, then justifying it | Rebuilding the derivation, which changed the answer |
| FOLD | Preserving the familiar operation set; then a bool return that cannot express which kind of absence | Step 5's "check every remaining operation"; then step 6's reachability question |
| PRIM | Near-miss on counting touchers rather than agreers | Asking who must settle a single outcome |
| DECOMP | Justifying a grouping from the sequential loop order | Re-attributing it to memory contiguity, a machine property |

Three unlisted failures worth adding to the drills' own Common Failures sections:

1. **COMMIT** — naming the line the returned *value* came from rather than the
   commit. The read-only analogue of the listed error.
2. **PRIM** — comparing object ceiling against primitive ceiling instead of
   required-agreement count against primitive ceiling. See G4.
3. **INDEX** — choosing a run length commensurate with the group size, which makes
   every group uniform and manufactures a perfect result. Step 1 warns against too
   *little* structure; it does not warn against this.

## Memory

**`memory/software-engineering/` should stay non-existent.** These sessions
produced drill defects and library-routing observations, not admissible events
about a capability. Nothing here is a real result about a real capability, which
is the bar for creating the store.

## The invalid run

**CPP (`DRILL_restructure_a_class_that_locks_every_member`) was never run.** The
session was terminated by an account-level usage limit partway through
constructing the restructured version. Under hard rule 17 this is an invalid run:
it failed before the capability was exercised, it is attributable to the tool, and
it counts toward nothing about the C++ lane. It needs a fresh cold session.

The limit is account-level, so a re-run must wait for the reset rather than be
retried immediately.

---

# Repair order

1. **B1, B2, B3** — the three broken instructions. A runner following them is
   misdirected, and two of them let a runner pass having demonstrated nothing.
2. **L4** — LOOP's checks rewarding the fatal error. One added bullet converts the
   worst answer from a top score to a failure.
3. **L1, L2, L3** — the other compound check defects.
4. **The four VERDICT-changing unstated quantities** — S-DECOMP-1, S-INDEX-1,
   S-PRIM-1, S-DECOMP-2. Each is one clause in a Practice Task or Setup.
5. **The FAIL family in Part 2a** — sixteen bullets across six drills. Mostly
   escape clauses of the form "…or its impossibility is argued." F-STAMP-1 and
   F-STAMP-2 need real restructuring, not a clause.
6. **N1** — the AP band contradiction. The only card edit in the list.
7. **The PASS family in 2b, and the remaining SCALE items.**
8. **Re-run CPP** in a cold session after the limit resets.
9. **G1 and G2** — hold for a second confirming run before authoring anything.

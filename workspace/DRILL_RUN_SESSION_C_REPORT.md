# Drill Run — Session C Report

Two drills, run in the order given, in `D:\Repos\SkillForge`. Skill loaded via the
`software-engineering` skill and its stated load order (`library/metaskills/INDEX.md`,
then `library/software-engineering/core/INDEX.md`). No repository changes were made
other than this file.

---

# Drill 1 — Fold an Interface Whose Operations Do Not Compose

`library/software-engineering/core/concurrency/DRILL_fold_an_unsafe_interface_into_transactions.md`

**Position in session: 1. Genuinely cold** — no prior context on this material, and
neither related pattern had been read before the drill file was opened.

## 1. The work itself

### Step 1 — the caller, using the operations in the natural sequence

The subject is a shared `ThreadSafeStack<Job>` whose three operations are each
individually guarded by an internal mutex: `empty()`, `top()`, `pop()`.

```cpp
// Every call below acquires and releases the stack's internal mutex.
// Each call, in isolation, is correct and race-free.
void drain(ThreadSafeStack<Job>& stack) {
    while (!stack.empty()) {        // 1. check whether anything is there
        Job job = stack.top();      // 2. look at it
        stack.pop();                // 3. take it
        run(job);
    }
}
```

### Step 2 — an interleaving in which every operation succeeds and the sequence is wrong

Two consumer threads A and B both run `drain`. The stack holds exactly one job, `J`.

| time | thread A | thread B | stack |
|---|---|---|---|
| t0 | `empty()` → `false` | | `[J]` |
| t1 | | `empty()` → `false` | `[J]` |
| t2 | `top()` → copy of `J` | | `[J]` |
| t3 | | `top()` → copy of `J` | `[J]` |
| t4 | `pop()` → removes `J` | | `[]` |
| t5 | | `pop()` → **pops an empty stack** | `[]` |

Every one of the six calls did exactly what its contract promised. The sequence is
still wrong twice over: `J` is executed twice, and B's `pop()` is called on an empty
container — undefined behaviour for the underlying `std::vector::pop_back`, or a
thrown exception if the wrapper checks.

**The exact moment the caller's assumption stopped holding.** B's assumption is
*"the stack is non-empty, and the element I copied is still the one I am about to
remove."* It was established at **t1**, when B's `empty()` returned `false` and
released the mutex. It died at **t4**, the instant A's `pop()` committed inside its
own critical section. The interval t1→t5 is unguarded not because any lock is
missing, but because **no lock is held across it by anyone** — B's reasoning spans
three separate acquisitions of the same mutex, and nothing protects the gaps
between them.

A shorter interleaving makes the same point with two calls instead of three: A's
`pop()` landing between B's `empty()` and B's `top()` makes B read an element that
is no longer there.

### Step 3 — the contiguous group the caller intended as one unit

`empty()` → `top()` → `pop()`. All three. The caller never wanted to know whether the
stack was empty; it wanted **"take an element if there is one."** The emptiness check
is not a query the caller cares about — it is a precondition the single-threaded
design forced it to establish for itself. That whole group, not any part of it, is
the operation to provide.

Note what this rules out as the unit: not `top()`+`pop()` (which would leave the
caller checking emptiness first), and not `empty()`+`top()` (which decides nothing).

### Step 4 — the group replaced by a single operation

```cpp
template <typename T>
class ConcurrentStack {
    // T must hand back without failing: the element is gone from the container
    // by the time the result is being returned, so a throwing move loses it.
    static_assert(std::is_nothrow_move_constructible_v<T>,
                  "use the try_pop(T&) overload for types whose move can throw");

public:
    void push(T value);

    // Removes and returns the top element, or reports that there was none.
    // Emptiness is an ordinary outcome, not a precondition.
    std::optional<T> try_pop();

    // Blocks until an element is available, then removes and returns it.
    std::optional<T> wait_and_pop(std::stop_token token);

    void clear();

    ConcurrentStack(const ConcurrentStack& other);   // takes other's lock
    ConcurrentStack(ConcurrentStack&& other);        // guards the moved-from object

private:
    mutable std::mutex mutex_;
    std::condition_variable_any not_empty_;
    std::vector<T> items_;
};

template <typename T>
std::optional<T> ConcurrentStack<T>::try_pop() {
    std::lock_guard<std::mutex> guard(mutex_);
    if (items_.empty())
        return std::nullopt;                            // the former precondition,
                                                        // now a return value
    std::optional<T> taken(std::move(items_.back()));   // construct the result FIRST
    items_.pop_back();                                  // remove only once it is safe
    return taken;
}
```

**How the former precondition is reported.** `std::optional<T>`. It was chosen over
the value-and-flag pair and over `bool try_pop(T& out)` for one reason: it makes
"there was nothing" unrepresentable as anything other than a return value the caller
must open before it can reach an element. A `bool`/out-param pair leaves the caller
holding a `T` it could read without checking the flag — the same "establish it first,
then use it" shape the redesign is removing, relocated from across two calls to
across two lines.

**Ordering inside the operation, and what happens if handing back fails.** The result
is constructed before the element is removed. If `T`'s move throws, it throws with the
element still in the container and the stack unchanged — nothing is lost, and the
caller may retry. The `static_assert` closes the remaining hole: after `pop_back`, the
return of `taken` may be a move (NRVO is permitted, not guaranteed), and a throw
*there* would lose an element that no longer exists anywhere. Constraining `T` to
nothrow-move makes that path unable to fail. For types that cannot satisfy it, the
alternative is `bool try_pop(T& out)`, which assigns into the caller's storage under
the lock **before** `pop_back`; a throwing assignment then also leaves the stack intact.

### Step 5 — every remaining operation against the same test

| operation | does its validity depend on something the caller established earlier? | disposition |
|---|---|---|
| `push(T)` | No. Defined in every state. | **Keep.** (If capacity were bounded, `push` would have to *report* rejection rather than let the caller pre-check `size() < capacity` — the identical fold.) |
| `empty()` | Its own call does not, but its *result* is the fact callers carry into the next call. Stale the instant it returns. | **Remove.** The only honest use — "am I done?" — is now `try_pop()` returning `nullopt`. |
| `size()` | Same. Stale on return; every use as a precondition is the step-2 bug. | **Remove.** If a monitoring caller genuinely needs a number, expose `approximate_size()` documented as advisory and never a precondition — a different operation with a different contract, not the same one renamed. |
| `top()` | Yes. Yields a copy of an element that another thread may remove before the caller acts on it. Establishes nothing that survives the return. | **Fold** into `try_pop`. |
| `pop()` (void) | Yes — requires non-emptiness established earlier. This is the failing call at t5. | **Fold** into `try_pop`. |
| `clear()` | No. Defined in every state. | **Keep.** |
| "wait until non-empty, then take" | Would be a caller-side loop on `try_pop`, i.e. a *second* multi-call unit. | **Add** `wait_and_pop` as its own complete operation. Step 3's logic applied a second time. |
| copy / move construction | A copy that reads `items_` unguarded races; a move leaves the source mid-flight. | **Write by hand**, taking the source's lock. |

Two structural consequences fall out of the sweep:

- **No operation returns a reference, pointer, or iterator into the container.**
  A handle is a fact held across time by definition, so it reintroduces exactly what
  the fold removed. `try_pop` returns by value.
- **The wrapper composes, it does not inherit.** Public inheritance from the
  underlying container would leave every un-wrapped inherited operation reachable and
  unguarded — including the `top()` and `pop()` just deliberately removed.

The resulting operation set is smaller and coarser than the single-threaded one.
That is the intended outcome, not a loss.

### Step 6 — what a caller can observe mid-change

Through the new interface, the complete set of reachable observations is:

- `try_pop()` returning an element — which is, at that moment, definitively removed
  and owned solely by this caller; or
- `try_pop()` returning `nullopt` — the stack was empty at the instant the lock was held; or
- `push` / `clear` completing.

Unreachable through the interface: *element copied but not yet removed*, *removed but
not yet handed back*, *size decremented ahead of the data*. Each exists only between
the acquisition and release of `mutex_` inside a single operation, and no operation
returns to a caller while that region is in flight. There is no operation that reports
a fact about the container's contents without also acting on them, so there is no
value a caller can hold that outlives the lock that produced it.

**The step-2 interleaving against the new interface.** A and B both call `try_pop()`
on a one-element stack. The two calls serialize on `mutex_`. Whichever acquires first
observes the element, constructs the result, and removes it; the other acquires
afterwards, observes an empty container, and receives `nullopt`. `J` is executed once.
No call is made on an empty container, because no caller decides emptiness — the
operation does, in the same acquisition in which it acts. There is no longer an
interval between the decision and the action for a schedule to open.

## 2. Success Check

- **No operation's contract requires a fact the caller obtained from a previous call.**
  **Met.** Enumerated per-operation in the step 5 table; the two that failed the test
  (`top`, `pop`) are gone, and the two whose results invited the failure (`empty`,
  `size`) are gone with them.
- **The case that was formerly a precondition is now an ordinary return value.**
  **Met.** Emptiness is `std::nullopt` from `try_pop`.
- **The failing interleaving from step 2 can no longer be constructed against the new
  interface.** **Met.** Argued at the end of step 6: the two decisions the schedule
  had to separate are now the same critical section.

## 3. Common Failures

- **Adding a lock around the existing operations.** Did not occur — and worth noting
  the drill made it hard to commit, because step 1 requires writing a caller in which
  every operation is *already* individually locked. Once that is on the page, adding a
  lock has visibly nothing left to add.
- **Preserving the familiar operation set out of habit.** **Nearly occurred.** My
  first draft of the new interface kept `empty()` and `size()`, on the reasoning that
  they were harmless because they no longer *had* to be called. Step 5 forced the
  question to be asked explicitly and I removed them. Reported as a near miss rather
  than a clean pass because the reflex was there and it took the instruction, not
  judgement, to catch it.
- **Folding the query into the action but leaving the result unable to express
  absence.** Did not occur.
- **Overlooking that a returning operation now removes before it hands back.**
  **Avoided, but not by the Instructions.** Step 4 asks only *how the operation reports
  the former precondition*; it does not ask about the ordering of removal against
  construction. Written from the Instructions alone, my `try_pop` would have been
  `T taken = std::move(items_.back()); items_.pop_back(); return taken;` — which loses
  the element on a throwing move. What caught it was the Do bullet in
  `PAT_make_every_concurrent_operation_a_complete_transaction`, read before starting.
  See the criticism section: this is the one place where the drill leans on a card it
  does not require you to have read.

## 4. Validity

**Valid.** All files opened cleanly, the two cross-linked patterns resolved on the
first grep, and the capability under test — restructuring an operation set so no
caller holds a result across two calls — was exercised end to end on a constructed
artifact rather than described. Nothing failed before the capability was reached.

## 5. What I consulted

- `library/metaskills/INDEX.md` (load order; topic listing only, no card retrieved)
- `library/software-engineering/core/INDEX.md`
- `library/software-engineering/core/concurrency/INDEX.md`
- `PAT_make_every_concurrent_operation_a_complete_transaction` — **used**, and load-bearing:
  the hand-back-failure ordering and the compose-don't-inherit point both came from it.
- `PAT_put_the_thread_safety_guarantee_at_the_transaction_boundary` — **used**, lightly:
  the strong/weak/hostile vocabulary and "don't guard the pieces and the whole"
  informed step 5's decision that the underlying `std::vector` needs no guarantee of
  its own.

---

# Drill 2 — Decide Whether a Primitive Can Coordinate the Design

`library/software-engineering/core/concurrency/DRILL_decide_whether_a_primitive_can_coordinate_the_design.md`

**Position in session: 2.** By the time this ran I had already read two concurrency
patterns and worked one design drill, so this result is weaker evidence than drill 1's
by that much. The specific contamination is nameable: drill 1's Notes and its patterns
had already put "safety does not compose across operations" in front of me, and
`PAT_make_every_concurrent_operation_a_complete_transaction` explicitly forward-refers
to the atomic-variable version of the same non-composability. That is one half of
drill 2's second Common Failure, arriving before drill 2 did.

## 1. The work itself

### Steps 1–3 — the three designs

| design | threads that **touch** | threads that **must agree on one outcome** | strongest primitive | tier | coordinates | verdict |
|---|---|---|---|---|---|---|
| **A.** Shared counter on atomic addition | 64 workers | **1** — i.e. none | `fetch_add` | unconditional read-modify-write | exactly 2 | **RULED IN** |
| **B.** Work queue on atomic exchange | 8 workers + 1 submitter = 9 | **8** | `exchange` | unconditional read-modify-write | exactly 2 | **RULED OUT — impossible** |
| **C.** Set on compare-and-set | 16 | **16** | `compare_exchange` | conditional update | unbounded (universal) | **RULED IN** |

**A — shared counter (statistics counter incremented by 64 worker threads).**
The count of threads that must agree on a single outcome is **one, which is to say
none at all**: increments commute, every `fetch_add` returns a value distinct from
every other, and no thread's correctness depends on learning whether it went first.
Even the one question that sounds like consensus — *which thread crossed the
threshold* — is answered by each thread from its own return value without reference
to any other thread. 64 is the number that *touch*; it is not the number that must
agree, and the distinction is the whole of step 1. Required 1 ≤ ceiling 2:
**in**, and wait-free natively, since it is a single instruction with no retry loop.

**B — multi-consumer work queue on atomic exchange (8-worker thread pool).**
A FIFO queue's operations return different results depending on the order they are
applied: each item must go to exactly one consumer, and the consumers must agree on a
single serialization of the dequeues. With 8 workers eligible to dequeue, **8 threads
must agree on one outcome**. Exchange coordinates exactly 2.

**This is impossibility, not difficulty.** Above two threads there is no correct
nonblocking protocol over exchange — not a slow one, not a delicate one, none. No
quantity of exchange variables raises it, no amount of additional bookkeeping memory
raises it (ordinary read-write storage is already assumed freely available in the
statement of the limit), and no algorithm will be found, because none exists. No code
review will show this, and a test suite will not show it either: what the limit forbids
is a protocol correct under *every* schedule, and a protocol wrong under one schedule
in ten thousand passes everything anyone will run. The reason the boundary falls here
is worth stating, because it is the diagnostic: an exchange **destroys what was
there**, so the thread arriving second erases the evidence that anyone arrived first,
and the loser is never informed that it lost.

Note the ruling is against *this thread count*, not against the primitive. The same
exchange rules **in** a single-producer/single-consumer queue, where exactly two
threads must agree — which is precisely the ceiling, and available.

**C — set on compare-and-set (16 threads).**
A set is order-dependent in the same way — `insert` reports whether the key was
already present — so all 16 must agree on one serialization. Compare-and-set is a
conditional update: it **fails instead of overwriting**, so the loser learns it lost,
and that single property is what removes the ceiling. It is universal: given it and
ordinary memory, every concurrent object has a wait-free implementation. 16 is below
no bound. **In.**

### Step 4 — the two responses for the design ruled out (B), and the choice

The two available responses, and only two:

1. **Move to a stronger primitive.** Rebuild on compare-and-set (or LL/SC), which has
   no ceiling — a Michael–Scott-style lock-free MPMC queue becomes possible at 8
   threads and at any other number.
2. **Accept a blocking implementation.** A `std::mutex` plus a condition variable
   around a `std::deque`. A lock lets any primitive coordinate any number of threads;
   the price is the blocking, which is now a chosen cost rather than a discovered one.

**Choice: the blocking implementation.** Reasons, in the order they carry weight:

- What makes blocking hurt is a thread being descheduled *inside* the critical
  section. This critical section is a push or pop on a deque plus a condvar notify —
  a few hundred nanoseconds. The event the nonblocking guarantee buys protection
  against is rare here, and where it is rare the blocking and nonblocking versions are
  close to indistinguishable in practice.
- Response 1 does not end at the CAS. A lock-free MPMC queue needs a memory
  reclamation scheme — hazard pointers, epochs, or RCU — to keep a node alive until
  the CAS completes, and that, not the queue logic, is where the weeks go. The
  impossibility is removed; a large engineering problem replaces it.
- Nothing has been measured yet. Lock-free is the last rung of a ladder, and the
  checks before stepping on it (a measured requirement, an existing specialist
  library, expertise that will still be present in a year, genuinely lock-free
  platform atomics for the types involved) currently answer no at the first one.
- The guarded version is also what a lock-free version would have to be verified
  against, so it gets built either way.

A third move exists but it is not a response to *this* design — it is a different
design: restructure into per-worker SPSC deques so the number that must agree drops
to 2, the ceiling exchange actually offers. It is worth naming because changing the
required thread count is a real lever alongside changing the primitive. It is not free
of the same test, though: the stealing side is itself a multi-thread agreement, so
unless steals are CAS-mediated the restructure only relocates the question.

### Step 5 — consequence for the designs ruled in

**No impossibility remains in A or in C.** Therefore every further failure in either is
an engineering problem, and both designs are worth persisting with. Concretely, and
this is the point of stating it — these are the failures that will *look* like the
ones that ruled B out, and are not:

- **A.** The counter's cache line ping-pongs between cores; cost per operation climbs
  steeply with thread count. Wait-free is not a scaling guarantee — every thread
  advances, not every thread advances quickly. Remedies are padding against false
  sharing, or sharding into per-thread counters summed on read when reads are rare.
  All tuning. Note also what A does *not* need: it is the case where a native atomic
  instruction exists and there is no surrounding invariant, so `fetch_add` is both
  the simplest and the strongest answer and there is nothing to weigh.
- **C.** ABA and memory reclamation; the fact that unlinking a node touches two
  pointers and one CAS covers one, which is why practical designs mark a node
  logically deleted and unlink it physically afterwards; retry waste under contention;
  and the gap between the universality result (wait-free, and impractically slow) and
  what a real CAS set delivers (lock-free). Every one has known solutions. When this
  keeps failing, the obstacle is engineering — which is the exact opposite conclusion
  from the same symptom below the ceiling, and the reason the ceiling gets checked first.

### Step 6 — the same test on an object rather than an instruction

**Could a concurrent queue be built wait-free from plain registers? No — and the reason
requires inspecting no attempt.**

The test applies to objects as well as instructions. A FIFO queue's operations return
different results depending on the order in which they are applied, which places its
coordination power at two threads: given a queue pre-loaded with two distinguishable
values, two threads can reach agreement by each publishing its proposal to ordinary
memory and then dequeuing — the thread that draws the first value decides its own
proposal, the thread that draws the second reads and adopts the first thread's. Both
decide the same value, always. Plain reads and writes coordinate one thread — that is,
none: no protocol built from ordinary loads and stores lets even two threads agree
without blocking, because a write destroys the previous value and every trace of who
wrote it, so no thread can leave a mark a later thread cannot erase.

A wait-free implementation of a queue from registers would therefore let registers do
what registers cannot: bring two threads to agreement. No such implementation exists.
This is settled from the two coordination powers alone; there is no candidate
algorithm to examine, and examining one would be the wrong activity.

## 2. Success Check

- **Each design has a thread count and a primitive tier written down, and a verdict
  that follows from the two.** **Met.** The step 1–3 table carries all four columns for
  all three designs, with the touch-count kept separate from the agree-count.
- **At least one design is ruled out, with the ruling stated as impossibility rather
  than difficulty.** **Met.** B, stated as impossibility, with the reason the boundary
  falls there (an unconditional write erases the loser's evidence) and with the
  explicit note that no bookkeeping, no additional exchange variables, and no passing
  test changes it.
- **The ruled-in design comes with the observation that its remaining problems are
  engineering ones.** **Met**, for both A and C, with the specific problems named so
  the observation is checkable rather than a formula.
- **The object-level test reaches its answer without inspecting a candidate
  implementation.** **Met.** The argument runs entirely on the two coordination powers.

## 3. Common Failures

- **Counting the threads that touch the structure rather than the threads that must
  agree on one outcome.** **Occurred, and was caught by step 1.** My first answer for
  design A was "64" — the worker count — before the instruction's explicit
  *"distinguish that from how many threads merely touch the structure"* forced the
  correction to "one, i.e. none." This is the drill working exactly as intended, and it
  is the failure most worth its place: the wrong number for A would have ruled a
  correct, cheap, wait-free design *out*.
- **Assuming that more bookkeeping state, or more instances of a weak primitive, lifts
  the ceiling.** Did not occur, though the temptation in B is concrete and I want it on
  record: the natural next thought after "exchange coordinates two" is "then give each
  of the 8 workers its own exchange slot and an array of announcements." Several
  primitives that each coordinate two still coordinate two; power is a ceiling on the
  construction, not a resource that accumulates.
- **Treating an operation as strong because it is atomic.** Did not occur. Design A is
  where the trap sits — `fetch_add` is genuinely indivisible and genuinely useful and
  still cannot make three threads agree on anything — and the tier table forced
  atomicity and coordination power to be recorded in separate columns.
- **Reading the result as an argument for using a conditional update everywhere.** Did
  not occur, and I would treat the two ruled-in designs as the evidence: A keeps
  `fetch_add` rather than being "upgraded" to a CAS loop it does not need, and B's
  chosen fallback is a lock rather than the stronger primitive that was also available.
  The result says what is possible, not what is advisable.

## 4. Validity

**Valid**, with the position caveat recorded above. The capability — ruling designs in
or out from their primitives before building anything — was exercised on all three
designs and on the object-level test. No file failed to read, no prerequisite was
missing, no instruction was unfollowable.

One honesty note on step 6 that does not affect validity: my answer used the explicit
two-thread consensus construction over a pre-loaded queue, which is **not** in the
library. The library's card states the general rule instead — anything whose operations
return different results depending on the order they are applied coordinates two
threads — and that rule alone is a sufficient reason for the drill's question. So the
library did contain enough to complete step 6; I brought a sharper argument from
outside it. A runner without that argument would have reached the same verdict by the
card's rule, which is the intended path.

## 5. What I consulted

- `library/software-engineering/core/concurrency/INDEX.md`
- `PAT_check_a_primitives_coordination_power_before_designing_on_it` — **used**, and
  the drill is not completable without it or equivalent knowledge: the three tiers and
  their numbers (1 / exactly 2 / unbounded) are what step 2's "place it" and step 3's
  verdict run on. The drill names the tiers but attaches no ceilings to them.
- `PAT_classify_synchronization_by_progress_guarantee` — **used** for step 4's choice:
  the descheduled-inside-the-critical-section argument, the four checks before stepping
  onto the lock-free rung, and the wait-free/lock-free/obstruction-free distinction that
  step 5's "engineering problems" list depends on.

---

# Across both drills

## Did the two share an underlying idea?

**Yes, and it is the same idea in two registers.** Both drills are a decision made
*before* implementation about something that cannot be retrofitted, and both turn on
non-composability:

- Drill 1: two thread-safe calls are not a thread-safe sequence.
- Drill 2: two primitives that each coordinate two threads do not coordinate three.

The failure signature is identical in both, and both cards' Notes describe it in almost
the same words — *each fix narrows the race and never removes it* — so the problem reads
as insufficient ingenuity when it is in fact structural. The remedy has the same shape
too: move the boundary out to whatever must actually be indivisible (drill 1), or move
to a primitive above the count that must actually agree (drill 2). And both end at the
same honest fallback — a well-built blocking design is very often the right answer.

Drill 1's pattern makes the connection explicit, forward-referencing the atomic-variable
version of its own result. Running them in this order meant drill 2's second Common
Failure was partly pre-loaded; running drill 2 first would have made drill 1's
"guarding smaller pieces cannot fix this" land as the recognition rather than the
reminder. If these two are ever run in the same session again, the order matters and I
would reverse it.

## Instructions that were ambiguous, circular, or impossible to follow

**Drill 2, step 1, for design A.** *"State how many threads must agree on a single
outcome"* has no comfortable answer for a plain counter, where the honest answer is
"none." The phrasing invites a number ≥ 2 and makes the correct answer feel like a
dodge. It is resolvable — `PAT_check_a_primitives_coordination_power` supplies the
vocabulary by writing the bottom tier as *"plain reads and writes coordinate one
thread — that is, none"* — but only for a runner who has that card open. A runner
working from the drill alone can get stuck here or, worse, invent a consensus
requirement that the design does not have.

Nothing else in either drill was ambiguous, circular, or unfollowable. Both are
followable straight through in the order given.

## Places the Success Check could be satisfied without doing the work

**Drill 1 — one real gap.** The Success Check's first bullet reads *"no operation's
contract requires a fact the caller obtained from a previous call."* A runner who folds
only the `empty`/`top`/`pop` sequence and skips step 5's sweep can leave `size()` in
the interface and still pass all three bullets: `size()`'s own contract requires no
prior fact, so bullet 1 reads as met, while the stale-query hazard that produced the
original bug is still sitting in the interface waiting for a caller to use it as a
precondition. The Success Check tests the *contract* of each surviving operation; step 5
tests whether each operation's result can be *used* as a precondition. Those are
different tests, and only the weaker one is checked. A fourth bullet along the lines of
*"no operation returns a fact about the container that a caller could act on later"*
would close it.

**Drill 1 — a softer one.** Bullet 3 ("the failing interleaving from step 2 can no
longer be constructed") is only as strong as the interleaving the runner chose to write
in step 2. A weak step 2 makes bullet 3 free. Self-limiting rather than broken.

**Drill 2 — tight.** All four bullets require artifacts that either exist or do not, and
the second bullet in particular ("stated as impossibility rather than difficulty")
cannot be satisfied by hedged language. No loophole found.

## Knowledge required that the library does not contain

**None found.** Both drills are completable from cards in the library. Two related
observations, one of which is a linkage issue rather than a content gap:

1. **Both drills depend on cards they do not require you to read.** Drill 1's fourth
   Common Failure — the hand-back-failure ordering — is the *only* place the ordering of
   removal against result-construction is mentioned, and a runner meets it after
   finishing step 4 rather than during it. The knowledge that would have prevented it is
   in `PAT_make_every_concurrent_operation_a_complete_transaction`. Drill 2 is stronger:
   steps 2 and 3 are not answerable at all without the tier ceilings from
   `PAT_check_a_primitives_coordination_power_before_designing_on_it`.

   Both patterns are linked from their drill — as `related_to`. **Verified:** the
   concurrency topic uses `related_to` for all 206 of its cross-links and
   `prerequisite_for` for none, while the rest of `software-engineering/core` uses
   `prerequisite_for` 117 times, and the concurrency `INDEX.md` consequently has no
   "Reading order" section where e.g. `testing/INDEX.md` does. Commands run:

   ```
   grep -rhn "rel: " library/software-engineering/core/concurrency/*.md | sed 's/.*rel: //' | sort | uniq -c
   grep -rh  "rel: " library/software-engineering/core/ | sed 's/.*rel: //' | sort | uniq -c
   grep -c "Reading order" library/software-engineering/core/concurrency/INDEX.md library/software-engineering/core/testing/INDEX.md
   ```

   So this is not a missing card and not an unreachable one — it is that nothing in the
   topic expresses that one of these should be read before the other. I retrieved both
   patterns because the drills' `cross_links` made them obvious, but that was a choice,
   not something the structure required. Reporting it as an observation for the
   authoring lane to weigh, not as a defect to act on: the topic may have been authored
   deliberately flat, and 57 objects is a lot of ordering to assert.

2. **Drill 2, step 6** is completable from the card's general rule, as noted under that
   drill's Validity. Not a gap.

## Navigation

No navigation defect. The concurrency `INDEX.md` listed every object with filename,
type, stage binding, and tags, and

```
grep -rn "<object_id>" --include=INDEX.md library/
```

resolved each cross-linked object ID to its file on the first attempt, in one call for
two IDs. I did not read a parent index as if it were a topic index; `core/INDEX.md`
correctly showed Concurrency as a topic with 57 objects and I descended to it. Every
claim above that touches the library's structure was checked with the commands shown
before it was written down.

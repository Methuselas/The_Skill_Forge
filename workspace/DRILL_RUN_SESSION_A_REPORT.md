# Session A — Drill Report

Run against the concurrency drills per `workspace/DRILL_RUN_HANDOFF.md`.

**Session:** A. **Positions:** drill 1 = 1st, drill 2 = 2nd, drill 3 = 3rd.

**Repository changes:** none during the run. This report file was written
afterwards, at the user's request, overriding the handoff's "no new files"
instruction. No compiler is present in the environment (`g++`, `clang++`, `cl`
all absent), so drill 3's C++ is reviewed, not compiled.

**Skill loaded:** `software-engineering`, then `library/metaskills/INDEX.md`,
`library/software-engineering/core/INDEX.md`,
`library/software-engineering/languages/cpp/INDEX.md`.

---

## Drill 1 — `DRILL_name_the_committing_step_on_every_path`

*Session A, position 1 (cold).*

### 1. The work

**Structure chosen:** a bounded FIFO queue with a separate lock at each end and
a shared atomic count — a linked list with a sentinel `head`, a `tail`,
`enqLock`, `deqLock`, and `AtomicInteger size`.

```java
class BoundedQueue<T> {
  final int capacity;
  Node head, tail;                       // head is a sentinel; head.next is the first item
  final ReentrantLock enqLock, deqLock;
  final AtomicInteger size = new AtomicInteger(0);

  boolean tryEnq(T x) {
    enqLock.lock();
    try {
      if (size.get() == capacity) return false;      // E0
      Node e = new Node(x);
      tail.next = e;                                 // E1
      tail = e;                                      // E2
      size.getAndIncrement();                        // E3
      return true;
    } finally { enqLock.unlock(); }
  }

  T tryDeq() {
    deqLock.lock();
    try {
      if (size.get() == 0) return null;              // D0
      T v = head.next.value;                         // D1
      head = head.next;                              // D2
      size.getAndDecrement();                        // D3
      return v;
    } finally { deqLock.unlock(); }
  }

  T deq() { /* as tryDeq, but: while (size.get()==0) notEmpty.await();  ... D1 D2 D3 */ }

  T peek()        { deqLock.lock(); try { return size.get()==0 ? null : head.next.value; } finally { deqLock.unlock(); } }  // P0 / P1
  int  size()     { return size.get(); }             // Q0
  boolean isEmpty(){ return size.get() == 0; }       // Q1

  boolean transfer(BoundedQueue<T> other) {          // deliberately included, see step 5
    T v = tryDeq(); if (v == null) return false;
    return other.tryEnq(v);
  }
}
```

Chosen because the drill asks for "a queue guarded at each end separately", and
because it lets the read-only operations be genuinely unguarded rather than
incidentally covered.

#### Steps 1-3 — operations, outcomes, committing step

| Operation | Outcome / path | Committing step | Kind |
|---|---|---|---|
| `tryEnq` | accepted | **E3** `size.getAndIncrement()` | write (RMW) |
| `tryEnq` | rejected, full | **E0** `size.get() == capacity` | read |
| `tryDeq` | removed an item | **D3** `size.getAndDecrement()` | write (RMW) |
| `tryDeq` | empty, returns null | **D0** `size.get() == 0` | read |
| `deq` (blocking) | removed an item | **D3**, on the pass after the last `await()` returns | write (RMW) |
| `deq` (blocking) | — | no empty path; it waits instead of failing | — |
| `peek` | found | **P1** the read of `head.next.value` | read |
| `peek` | empty | **P0** `size.get() == 0` | read |
| `size` | always | **Q0** `size.get()` | read |
| `isEmpty` | true / false | **Q1** `size.get()` (same step both ways) | read |
| `transfer` | any | **none** — see step 5 | — |

#### Step 4 — the before/after test

The one that carries the design is `tryEnq` accepted.

- *Immediately before E3.* Every operation that could observe the new node
  gates on the counter first. `size()`/`isEmpty()` read the counter and do not
  see it. `tryDeq`/`deq`/`peek` read the counter at D0/P0 and, if it says empty,
  return without ever looking at `head.next` — so the node being physically
  linked at E1 buys an observer nothing. Another `tryEnq` is excluded by
  `enqLock`. The object looks exactly as though `tryEnq` had never been called.
- *Immediately after E3.* The counter includes the item; a dequeuer admitted by
  the counter follows `head.next` and reaches it, and the read-modify-write at
  E3 is what carries the E1 link into that dequeuer's view. The operation is
  finished — `tail` was already advanced at E2, before E3.

E1 and E2 both fail the test in the other direction: an observer just after E1
sees an object identical to one where nothing happened, so E1 is too early, not
ambiguous.

**The finding: in this structure the counter is the commit for both ends, and
the two locks only serialise the pointer surgery.** The pointer writes are
invisible; the counter update is the publication.

Same test on the rejected path: at E0 the counter reads `capacity`, and because
the counter is only advanced *after* each link, the counter is an exact
statement of committed contents at every instant. So "the queue was full" was
true at E0. It may stop being true one instruction later; that does not matter,
because the operation is placed at E0.

`tryDeq` removed: before D3, a `size()` caller still counts the item, and a
concurrent `tryEnq` on a full queue still sees `capacity` and refuses — so the
removal has not happened for anyone. After D3, both flip. D1/D2 are invisible.

#### Step 5 — paths with no single step

- **`transfer` — no committing step.** It has two: D3 inside `this`, E3 inside
  `other`. Between them the element exists in neither queue, and an observer
  summing both sizes sees a total that no instant of the system ever held. A
  design defect, not a naming problem — the remedy is either a shared owner that
  commits once, or an explicitly stated weaker contract. I included this
  operation on purpose, because the core five all had a step immediately and the
  drill's Notes say the diagnostic value is the case where one cannot be named.
- **Checked and found *not* to apply:** the pattern warns about a commit landing
  in another thread's execution. Blocking `deq` on an empty queue is the obvious
  candidate and turns out not to be one — the woken thread re-tests the
  predicate and commits at its own D3. The enqueuer's E3 *permits* the commit,
  it is not the commit. A rendezvous channel with direct hand-off would be the
  real instance; this design is not one.
- **Mutation test.** Moving `size.getAndIncrement()` ahead of `tail.next = e` —
  a change that looks like a harmless reordering — destroys the property:
  between the increment and the link, a dequeuer is admitted by the counter and
  reads `head.next == null`. The effect becomes visible in stages.

#### Step 6 — read-only operations

`size`/`isEmpty` report the value true at their single counter read. `peek`
found reports the value true at P1; nothing can move `head.next` while `deqLock`
is held, and an enqueuer only writes `tail.next`, a different location whenever
the queue is non-empty — so the whole of `peek` is a stable interval and any
point in it serves.

### 2. Success Check

| Bullet | Result |
|---|---|
| Every operation has a committing step, one per outcome | **Met.** Eleven paths across ten operations. |
| Before/after shows un-started then finished | **Met**, and tested rather than asserted; E1/E2 and D1/D2 were rejected by the test. |
| Any path lacking a step identified as a design defect | **Met** (`transfer`). |

### 3. Common Failures

- *One answer per operation, missing the empty path* — **avoided**, and it was
  the productive part: `tryEnq`'s two outcomes commit at genuinely different
  instants, E0 being strictly earlier in the operation than E3.
- *Naming the return instead of the commit* — **avoided**, narrowly. My first
  instinct on `tryDeq` was D1, the read of the value being returned. D1 is two
  steps early.
- *Skipping read-only operations* — **avoided**.
- *Accepting a region* — **avoided**; "somewhere inside `enqLock`" was
  specifically what the test disqualified.

### 4. Validity

**Valid.** Ran end to end, capability exercised, and it produced a finding (the
counter is the commit, the pointer writes are not) that I did not have going in.

### 5. What I consulted

- `PAT_give_every_operation_one_instant_where_it_takes_effect` (in full)
- `PAT_specify_a_concurrent_object_as_a_sequential_object_plus_a_correctness_condition` (body)
- `PAT_atomic_steps_do_not_compose_into_a_safe_whole` (rule + Do/Don't)

---

## Drill 2 — `DRILL_classify_the_dependencies_in_a_loop`

*Session A, position 2.*

### 1. The work

**Loop chosen** — running total, reused scratch, an array read and written, plus
an induction counter:

```c
double total = 0.0;      /* running total                       */
int    idx   = 0;        /* counter advanced by a fixed amount  */
double tmp;              /* scratch, reused every pass          */

for (int i = 1; i < n; i++) {
    tmp      = a[i] * b[i];      /* S1 */
    c[i]     = tmp + c[i-1];     /* S2 */
    total   += tmp;              /* S3 */
    b[i]     = tmp * 0.5;        /* S4 */
    out[idx] = c[i];             /* S5 */
    idx     += 2;                /* S6 */
}
```

#### Step 1 — locations touched

| Location | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| `a[i]` | R | | | | | |
| `b[i]` | R | | | W | | |
| `tmp` | W | R | R | R | | |
| `c[i-1]` | | R | | | | |
| `c[i]` | | W | | | R | |
| `total` | | | R/W | | | |
| `idx` | | | | | R | R/W |
| `out[idx]` | | | | | W | |

#### Steps 2-3 — every pair, classified, with its remedy

| # | Location | Pair | Across? | Kind | Remedy |
|---|---|---|---|---|---|
| 1 | `tmp` | S1 W -> S2/S3/S4 R | within | flow | none needed — never crosses the parallel boundary |
| 2 | `b[i]` | S1 R -> S4 W | within | **shared name** (anti) | none needed — body order preserves it inside one thread |
| 3 | `c[i]` | S2 W -> S5 R | within | flow | none needed |
| 4 | `idx` | S5 R -> S6 W | within | **shared name** (anti) | dissolved by #9's remedy |
| 5 | `tmp` | S2/S3/S4 R (iter *i*) -> S1 W (iter *i+1*) | **across** | **shared name** (anti) | privatize `tmp` |
| 6 | `tmp` | S1 W (iter *i*) -> S1 W (iter *i+1*) | **across** | **shared name** (output) | privatize `tmp` |
| 7 | `c` | S2 W `c[i]` (iter *i*) -> S2 R `c[i]` (iter *i+1*) | **across** | **flow** | algorithmic: inclusive scan |
| 8 | `total` | S3 W (iter *i*) -> S3 R (iter *i+1*) | **across** | **flow** | algorithmic: reduction |
| 9 | `idx` | S6 W (iter *i*) -> S5/S6 R (iter *i+1*) | **across** | **flow** | algorithmic: closed form |
| 10 | `idx` | S6 W -> S6 W | **across** | shared name (output) | *subsumed by #9 — do not privatize* |
| 11 | `b` | S4 W `b[i]` -> S1 R `b[j]` | **across** | **none** — requires `i == j`, impossible | — |
| 12 | `out` | S5 W -> S5 W | **across** | output *if indices can collide* | provably disjoint once #9 is fixed |
| 13 | `a[i]` | read only, distinct index | **across** | **not a dependency** | — |

Two entries earn their place. **#11**: the loop "writes into an array it also
reads", the alarming-looking part of the task, and the conflict turns out to be
entirely inside one iteration — each iteration owns `b[i]` exclusively. **#10**:
`idx` carries *both* a flow and an output conflict on the same location.
Privatizing it would make the output conflict vanish and silently destroy the
flow, giving every thread its own confidently-wrong counter. That is the drill's
third common failure sitting on a variable that looks like an obvious
privatization candidate.

#### Step 4 — privatize, and confirm the conflict is gone rather than reordered

`tmp` moves inside the body (`double tmp = a[i]*b[i];`). Iterations *i* and *j*
now touch distinct locations, so #5 and #6 have no pair left to form — nothing
was ordered around, the pair ceased to exist. Guard check before doing it: does
any flow run through `tmp` across iterations? #1 is the only flow on `tmp` and
it is entirely within one iteration. Safe.

`idx` is **not** privatized, per #10.

#### Step 5 — algorithmic forms for the surviving flows

- **#8, `total`** — a reduction: per-thread partials, combined at the end.
- **#9, `idx`** — closed form `idx = 2*(i-1)`. Double duty: it removes the flow,
  and it makes #12 provable, since `2*(i-1)` is injective in `i`.
- **#7, `c`** — an inclusive scan of `p[i] = a[i]*b[i]` seeded with `c[0]`.
  Two-pass: block-local sums, exclusive scan of the block sums, then add each
  block's offset. Span `O(n/P + P)`.
- **Falls out of #7:** `c[n-1] = c[0] + sum p[i] = c[0] + total`. Once the scan
  is done, `total` is `c[n-1] - c[0]` and the reduction in #8 is redundant — the
  two flows were the same information.

One real constraint: **S4 destroys `b[i]`**, so the second pass cannot recompute
`a[i]*b[i]`. Pass 1 must materialise `p[]` into an array. (`p[i] = 2*b_new[i]`
recovers it without the array, but couples the scan to S4 having already run on
that element — I would not ship that.)

#### Step 6 — what remains

*With the scan:* nothing sequential but the `O(P)` combine over block sums. Four
parallel phases — products into `p[]`, scan, `b[i] = 0.5*p[i]`,
`out[2*(i-1)] = c[i]` — the last three fully independent per element.

*Without the scan* (justifiable if `n` is small or the extra `p[]` traffic
dominates): #7 survives. What parallelises around it: **all of** S1, S3, S4, S5
and S6. Phase 1 computes `p[i]` and `b[i]` in parallel; phase 2 is a single
serial memory-bound pass `c[i] = p[i] + c[i-1]`; phase 3 writes
`out[2*(i-1)] = c[i]` in parallel. One serial pass with no arithmetic dependency
chain beyond an add.

*Acceptance caveat, not a dependency:* both the reduction and the scan
re-associate floating-point addition, so results differ from the sequential
version in the low bits. A criterion to agree before the change, not after.

### 2. Success Check

| Bullet | Result |
|---|---|
| Every conflict classified, with the remedy that applies | **Met.** 13 pairs, each with a remedy or an explicit "none needed / not a dependency". |
| All shared-name conflicts gone after privatization, nothing reordered | **Met** for #5 and #6. #2 and #4 are within-iteration and unaffected by the decomposition; #10 is deliberately not privatized and is removed by the closed form instead, which eliminates it rather than reordering around it. |
| Surviving flow stated, with what still runs in parallel | **Met.** #7 stated as the only survivor if the scan is declined, with the three phases named. |

### 3. Common Failures

- *Reading top to bottom, finding only within-iteration conflicts* —
  **avoided**; #5 in particular runs backwards through the text.
- *Treating every conflict as fatal* — **avoided**.
- *Privatizing a location a flow runs through* — **nearly hit.** `idx` reads as
  a textbook privatize candidate; the output conflict at #10 is what makes it
  look like one. Catching it required listing the flow at #9 first.
- *Concluding a flow is irreducible after one failed attempt* — did not arise.

### 4. Validity

**Valid.**

### 5. What I consulted

- `PAT_classify_a_dependency_before_trying_to_remove_it` (in full)

I did not need `PAT_avoid_sharing_before_you_reach_for_protecting_it`, the other
cross-link — the drill's own step 4 already forces privatization ahead of
synchronization, so the card would have confirmed rather than informed. A fact
about the run, not a criticism of the link.

**Card observation.** The Pattern names reduction and closed form as the known
algorithmic answers and omits **scan**, which is the third member of that family
and the one this drill's own Practice Task needs. I supplied it from outside the
library without noticing at first. Disposition: an edit to the existing card, not
a new Pattern — the drill completed, so this is an incomplete enumeration rather
than a failure.

---

## Drill 3 — `DRILL_restructure_a_class_that_locks_every_member`

*Session A, position 3 (weakest evidence — two concurrency patterns already read).*

### 1. The work

**Before** — one mutex, taken at the top of every member function:

```cpp
class JobQueue {
public:
    explicit JobQueue(std::size_t cap) : capacity_(cap) {}

    void push(Job j) {
        std::lock_guard<std::mutex> lk(mtx_);
        if (isFull())                     // public -> public
            evictOldest();                // public -> public
        jobs_.push_back(std::move(j));
        ++totalPushed_;                   // static state, per-object mutex
        if (onChange_) onChange_(jobs_.size());   // unknown code, lock held
    }

    bool        isFull()      { std::lock_guard<std::mutex> lk(mtx_); return jobs_.size() >= capacity_; }
    void        evictOldest() { std::lock_guard<std::mutex> lk(mtx_); if (!jobs_.empty()) jobs_.pop_front(); }
    std::size_t size()        { std::lock_guard<std::mutex> lk(mtx_); return jobs_.size(); }
    void        setListener(std::function<void(std::size_t)> f)
                              { std::lock_guard<std::mutex> lk(mtx_); onChange_ = std::move(f); }

    static std::size_t totalPushed() { return totalPushed_; }   // cannot lock mtx_ — no object

private:
    void trimToCapacity() {   // private helper that locks
        std::lock_guard<std::mutex> lk(mtx_);
        while (jobs_.size() > capacity_) jobs_.pop_front();
    }

    std::mutex mtx_;
    std::deque<Job> jobs_;
    std::size_t capacity_;
    std::function<void(std::size_t)> onChange_;
    static std::size_t totalPushed_;
};
```

#### Step 1 — public->public paths, ordinary vs recursive mutex

| Path | `std::mutex` | `std::recursive_mutex` |
|---|---|---|
| `push` -> `isFull` | Relocking a held mutex is undefined; in practice the thread self-deadlocks on the first `push` ever made. | Succeeds. Cost: a redundant lock/unlock per call, and the critical section's real extent is no longer visible at any one point in the source. |
| `push` -> `evictOldest` | Same — unreachable, `push` already hung. | Succeeds, and now `evictOldest` is indistinguishable at its own definition from a call made by an outside client with no lock held. |
| `push` -> `onChange_(...)` -> listener calls `size()` or `push()` | Self-deadlock inside caller-supplied code, on a line that names no mutex. | **Worse than the mutex version.** Re-entry now *succeeds*: a listener that pushes recurses without bound, and "the lock guarantees a consistent view" silently becomes "...except when re-entered." |
| any public caller -> `trimToCapacity` | Deadlocks. Nothing at the call site distinguishes it from a helper that does not lock. | Redundant lock. |

The recursive mutex is the trap: it converts a hang into working-but-wrong, and
the third row is where it is actively worse than the deadlock it removed.

#### Step 2 — locking moved to the public boundary

```cpp
class JobSink {
public:
    virtual ~JobSink() = default;
    virtual void push(Job j) = 0;
};

class JobQueue : public JobSink {
public:
    using Listener = std::function<void(std::size_t)>;

    explicit JobQueue(std::size_t cap) : capacity_(cap) {}

    void push(Job j) override {
        if (!shouldAccept(j)) return;             // hook, no lock held

        std::deque<Job>          evicted;         // destroyed after the lock
        std::shared_ptr<const Listener> listener; // copy is a refcount bump
        std::size_t newSize = 0;
        {
            std::lock_guard<std::mutex> lk(mtx_);
            if (isFull_locked())
                evictOldest_locked(evicted);
            jobs_.push_back(std::move(j));
            newSize  = jobs_.size();
            listener = onChange_;
        }
        {
            std::lock_guard<std::mutex> lk(statMtx_);
            ++totalPushed_;
        }
        if (listener) (*listener)(newSize);       // unknown code, no lock held
    }                                             // ~evicted runs here

    bool        isFull() const { std::lock_guard<std::mutex> lk(mtx_); return isFull_locked(); }
    void        evictOldest()  { std::deque<Job> ev;
                                 { std::lock_guard<std::mutex> lk(mtx_); evictOldest_locked(ev); } }
    std::size_t size() const   { std::lock_guard<std::mutex> lk(mtx_); return jobs_.size(); }

    void setListener(Listener f) {
        auto next = std::make_shared<const Listener>(std::move(f));
        std::shared_ptr<const Listener> old;
        { std::lock_guard<std::mutex> lk(mtx_); old = std::exchange(onChange_, std::move(next)); }
    }                                             // ~old runs here

    static std::size_t totalPushed() {
        std::lock_guard<std::mutex> lk(statMtx_);
        return totalPushed_;
    }

protected:
    // Extension point. Called with NO lock held and given only the caller's own
    // Job. Overrides must not touch JobQueue state.
    virtual bool shouldAccept(const Job&) const { return true; }

private:
    bool isFull_locked() const { return jobs_.size() >= capacity_; }
    void evictOldest_locked(std::deque<Job>& out) {
        if (!jobs_.empty()) { out.push_back(std::move(jobs_.front())); jobs_.pop_front(); }
    }

    mutable std::mutex mtx_;
    std::deque<Job> jobs_;
    std::size_t capacity_;
    std::shared_ptr<const Listener> onChange_;

    static std::mutex  statMtx_;
    static std::size_t totalPushed_;
};

std::mutex  JobQueue::statMtx_;
std::size_t JobQueue::totalPushed_ = 0;
```

`trimToCapacity` is gone; its behaviour is `evictOldest_locked` in a loop and it
had no caller that needed it separately.

#### Step 3 — accessibility audit, against the rule

| Function | Accessibility | Locks? | Against the rule |
|---|---|---|---|
| `JobQueue(std::size_t)` | public | no | **Conforms by exception.** No other thread can reach the object during construction. Worth stating rather than passing over, since the rule as written says *every* public function. Destructor likewise: concurrent access during destruction is already undefined, and a lock would not make it defined. |
| `push` | public | yes (`mtx_`) | conforms |
| `isFull` | public | yes | conforms |
| `evictOldest` | public | yes | conforms |
| `size` | public | yes | conforms |
| `setListener` | public | yes | conforms |
| `totalPushed` | public static | yes (`statMtx_`) | conforms — the static state's mutex |
| `shouldAccept` | protected virtual | **no** | conforms; see step 4 |
| `isFull_locked` | private | no | conforms |
| `evictOldest_locked` | private | no | conforms |

No public function calls another public function on `this`.

#### Step 4 — a virtual interface function and an override

Two extension points, opposite answers.

**(a) `JobSink::push` is public and virtual. A derived override *must* lock —
even declared `private`.**

```cpp
class DroppingQueue : public JobSink {
private:
    void push(Job j) override {                    // private override of a public virtual
        std::lock_guard<std::mutex> lk(mtx_);      // required
        if (jobs_.size() < cap_) jobs_.push_back(std::move(j));
    }
    mutable std::mutex mtx_;
    std::deque<Job> jobs_;
    std::size_t cap_;
};
```

Justified from dispatch: access is checked against the *static* type of the call
expression. `DroppingQueue d; d.push(j);` is rejected, but
`JobSink& s = d; s.push(j);` compiles and lands in the private override — so
`private` restricts nothing any caller actually does, and the override is a
public entry point in every sense that matters for locking. And because the
override *replaces* the base body rather than extending it, it replaces the
base's lock acquisition too. A variant that instead delegates
(`JobQueue::push(std::move(j));`) inherits the base's locking for the base's
state, and needs its own lock only for its own state — released before
delegating, so no ordering is established.

**(b) `shouldAccept` is protected and virtual. It must *not* lock, and it must
be called outside the lock.**

Justified from dispatch and from ownership: it is reached only from `push`, so a
lock of `mtx_` inside it would be a nested acquisition on the same object — the
original defect. But the deeper reason it is called *before* `mtx_` is taken is
that a `protected virtual` on a class open for public extension is code the base
cannot audit, now or in any future derived class. So it is given a `const Job&`
the caller already owns, no reference into guarded state, and no lock held.

Two different answers because two different questions: (a) is about who reaches
the function, (b) is about who wrote it.

#### Step 5 — static state

`totalPushed_` gets `static std::mutex statMtx_`.

What breaks if the mutex stays per-object: two `JobQueue` instances on two
threads each lock their own `mtx_`, and both read-modify-write the same
`totalPushed_`. Neither lock excludes the other, so it is a data race —
undefined behaviour, and observably lost increments. Each object is correctly
protected and the shared counter is not protected at all. Separately,
`static std::size_t totalPushed()` has no object and therefore cannot lock a
per-object mutex even in principle, which is the compile-time symptom of the
same design error. The two versions differ by one keyword on a member
declaration and read identically.

Remark, not part of the answer: a lone counter is better as
`static std::atomic<std::size_t>`, which is the pattern's own ELSE clause. I
used the static mutex because that is what the drill asks for, and because the
mutex generalises if a second static field ever appears.

#### Step 6 — unknown code under the lock

Four sites found, all moved out:

1. **`onChange_(...)`** — a caller-supplied `std::function` invoked inside the
   critical section. Moved out. This alone fixed the worst of the "before": a
   listener calling `size()` no longer deadlocks, and a listener capturing a
   reference into `jobs_` can no longer be handed one.
2. **Copying the listener under the lock.** The obvious fix —
   `Listener local = onChange_;` inside the lock, invoke outside — still runs
   the caller's capture copy-constructors inside the critical section, where
   they can allocate and throw. Holding the listener behind
   `shared_ptr<const Listener>` makes the copy a refcount increment, which is
   not user code.
3. **`jobs_.pop_front()` destroying the evicted `Job` under the lock.** The
   evicted element is moved into a local `std::deque<Job> evicted` declared
   *outside* the lock scope, so it is destroyed after `mtx_` is released. The
   moved-from husk is still destroyed under the lock — cheap, but not guaranteed
   trivial, and worth knowing rather than assuming.
4. **`std::exchange(onChange_, ...)` in `setListener`** — the *old* listener's
   destructor would otherwise run under the lock. Held in `old` and destroyed on
   function exit.

Not moved: `jobs_.push_back(std::move(j))` runs `Job`'s move constructor under
the lock. `Job` is a concrete type in the same component, so this is the
pattern's ELSE clause. If `JobQueue` were a template over the element type it
would not be, and the push would have to be restructured too.

### 2. Success Check

| Bullet | Result |
|---|---|
| Every public member function acquires the lock; no non-public one does | **Met**, with the constructor/destructor exception stated explicitly rather than glossed. |
| No public function calls another public function on the same object | **Met.** |
| The virtual override's locking decision stated with its reason | **Met**, for both extension points, justified from dispatch. |
| Static state guarded by a static mutex, and the per-object failure stated | **Met.** |
| No unknown code executes while the lock is held | **Met** for the four sites found; the `Job` move constructor is named as the residual and justified. |

### 3. Common Failures

- *Switching to a recursive mutex* — **avoided**, and analysed in step 1 as
  required.
- *Leaving a private helper that locks* — **avoided**; `trimToCapacity` was the
  planted instance and was removed.
- *Assuming a private override needs no lock* — **avoided**; this is (a) in step
  4 and it is the sharpest thing in the drill.
- *Guarding static state with a per-instance mutex* — **avoided**.
- **One I did hit and had to back out.** My first restructuring called
  `shouldAccept` *inside* the critical section, reasoning from the NVI idiom
  that a protected hook reached only from a locked public entry needs no lock of
  its own. That reasoning is correct about the hook's *own* locking and wrong
  about *where it is invoked* — it satisfies
  `PAT_lock_at_the_public_boundary_and_nowhere_inside` and violates
  `PAT_dont_call_unknown_code_while_holding_a_lock`. The two cross-links pull in
  opposite directions on a protected virtual, and only reading both caught it.
  Instruction 6 is what forced the re-check.

### 4. Validity

**Valid**, with one qualification about the tooling, not the drill: no compiler
is present, so the C++ is reviewed rather than compiled. Nothing in the Success
Check depends on compiling, and the one construct where I would most want a
compiler — the private override reached through a base reference — is settled by
the access rules rather than by observation. Weakest of the three runs on
cold-session grounds.

### 5. What I consulted

- `PAT_lock_at_the_public_boundary_and_nowhere_inside` (in full)
- `PAT_dont_call_unknown_code_while_holding_a_lock` (in full)

---

# Across the three drills

## Instructions that were ambiguous, circular, or impossible as written

None impossible. Two friction points, both in drill 3:

- **Instruction 4** reads as one case, and there are two with opposite answers:
  an override of the *public* virtual entry point (locks) and an override of a
  *protected* NVI hook (does not, and must be invoked outside the lock). The
  Success Check bullet is also singular — "The virtual override's locking
  decision" — so a runner who builds only the NVI case answers correctly and
  never meets Common Failure #3, which is the failure the instruction exists to
  catch. Suggest naming both cases, or pinning the instruction to an override of
  the public virtual.
- **Instructions 4 and 6 interact and the drill does not say so.** Following 4
  the NVI way puts a virtual call inside the critical section; 6 then removes
  it. That sequencing is arguably the teaching, but it is currently accidental
  rather than designed, and a runner who does 6 before 4 will not experience it.

## Success Checks satisfiable without doing the work

- **Drill 1, bullet 2** — "the before-and-after description shows the operation
  as entirely un-started and then entirely finished" is checkable only against a
  description the runner writes. Restating the chosen step in before/after prose
  passes it. What makes the test bite is *rejecting* candidate steps, and the
  check does not ask for that. Suggest requiring at least one rejected candidate
  per mutating path.
- **Drill 1, bullet 1** — passes for a runner who names the return of every
  operation. Common Failure #2 names that error; the check does not test for it.
- **Drill 2, bullet 2** — "All shared-name conflicts are gone after
  privatization" is satisfiable by privatizing everything, which is Common
  Failure #3 and *passes this bullet*. The bullet that would catch it — "any
  surviving flow is stated" — passes too, because a privatized flow does not
  survive and there is nothing to state. In this loop, **privatizing `idx`
  satisfies the whole Success Check and produces a wrong program.** Suggest: for
  each location privatized, state why no flow runs through it.
- **Drill 3** — the checks are concrete and structural (accessibility, call
  graph, static/static pairing). I do not see a way to pass them without
  restructuring.

## Knowledge the library did not contain

Nothing missing that I needed. Three things supplied from outside the cards:

- **The parallel scan formulation** for drill 2's surviving flow. This is the
  one that is arguably a canon observation; see drill 2 §5. Disposition: an edit
  to an existing card.
- **C++ access-control semantics** for a private override reached through a base
  reference (drill 3, step 4a). Language rules, not concurrency canon.
- **The floating-point reassociation caveat** on reduction and scan (drill 2).
  Numerics, out of scope for the concurrency topic.

## Position effects

Drills 1 and 3 both turn on the same move from two directions — find the single
place the change becomes visible, and make that place the only place. Running
them in one session, drill 3 was easier than it should have been because drill 1
had already put me in that frame. If the drills are re-run for cleaner evidence,
those two are worth keeping in separate sessions; the current grouping puts them
together.

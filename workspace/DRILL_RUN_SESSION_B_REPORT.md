# Session B — Drill Report

Run against the concurrency drills per `workspace/DRILL_RUN_HANDOFF.md`.

**Session:** B. **Positions:** drill 1 = 1st, drill 2 = 2nd, drill 3 = 3rd.

**Repository changes:** none during the run. `validate.py` was run read-only
(1103 objects, PASS) only to confirm a cross-link target existed. This report
file was written afterwards at the user's explicit request, overriding the
handoff's "no new files" instruction.

---

## Drill 1 — `DRILL_replace_value_validation_with_a_version_stamp`

*Session B, position 1 (cold).*

### 1. The work

**Starting routine (value-validated collection).** A bank of `N` accounts; an auditor wants a consistent view to check the invariant `sum(balance) == 200`.

```cpp
struct Bank { std::atomic<int64_t> balance[N]; };

// transfer is TWO stores, not one
void transfer(Bank& b, int from, int to, int64_t amt) {
    b.balance[from].fetch_sub(amt, std::memory_order_relaxed);
    b.balance[to  ].fetch_add(amt, std::memory_order_relaxed);
}

bool snapshot(Bank& b, int64_t out[N]) {
    for (;;) {
        int64_t a[N], c[N];
        for (int i = 0; i < N; ++i) a[i] = b.balance[i].load(std::memory_order_acquire);
        for (int i = 0; i < N; ++i) c[i] = b.balance[i].load(std::memory_order_acquire);
        if (std::equal(a, a + N, c)) {            // <-- value validation
            std::copy(a, a + N, out);
            return true;
        }
    }
}
```

#### Step 1 — a schedule where both passes match and the view never existed

`N = 2`. Initial `A = 100, B = 100`. One writer loops `transfer(A→B, 50); transfer(B→A, 50);`.

| # | Actor | Action | A | B | Collector |
|---|---|---|---|---|---|
| 1 | collector | read A → 100 | 100 | 100 | `a[0]=100` |
| 2 | writer | `A -= 50` | 50 | 100 | |
| 3 | writer | `B += 50` | 50 | 150 | |
| 4 | collector | read B → 150 | 50 | 150 | `a[1]=150` |
| 5 | writer | `B -= 50` | 50 | 100 | |
| 6 | writer | `A += 50` | 100 | 100 | |
| 7 | collector | read A → 100 | 100 | 100 | `c[0]=100` |
| 8 | writer | `A -= 50` | 50 | 100 | |
| 9 | writer | `B += 50` | 50 | 150 | |
| 10 | collector | read B → 150 | 50 | 150 | `c[1]=150` |

`a == c == (100, 150)`. Accepted. Reported total **250**; the invariant is 200.

The states that actually existed are `(100,100)`, `(50,100)`, `(50,150)`.
**`(100,150)` occurs at no instant in the schedule.** Both locations were written
and written back between the passes: A went `100→50→100`, B went `100→150→100`.

The shorter variant the drill names — one location written twice to the same
value — is the degenerate case: a mode flag set `X → Y → X` between the passes,
where the collector reads it before the first write and after the second.

#### Step 2 — counter per location, validate on counters

```cpp
struct Slot {
    std::atomic<uint64_t> stamp;   // even = stable, odd = write in progress
    std::atomic<int64_t>  value;
};

struct Reading { uint64_t stamp; int64_t value; };

// returns false if the location was mid-write
bool read_slot(const Slot& s, Reading& r) {
    r.stamp = s.stamp.load(std::memory_order_acquire);
    if (r.stamp & 1) return false;
    r.value = s.value.load(std::memory_order_acquire);
    return s.stamp.load(std::memory_order_acquire) == r.stamp;
}
```

Validation now compares `stamp`, never `value`:

```cpp
if (a[i].stamp != c[i].stamp) -> failed pass
```

**Applied to the step-1 schedule:** pass 1 reads `stamp(A) = 0`. A is written at
steps 2 and 6, so pass 2 at step 7 reads `stamp(A) = 4`. `4 != 0` → rejected.
Same for B (`0` vs `4`). The schedule that value comparison accepted is now
rejected, and it is rejected for the right reason: the collector is told *the
location was touched*, not *the value differs*.

#### Step 3 — how wide the counter must be, and the assumption behind it

The counter must not return to a previously observed value inside one collection
window. Two quantities bound that:

- **D** — the maximum interval between a collector's first read of a location and its second read of that location.
- **R** — the maximum rate at which any single location can be written.

Each write advances the stamp twice (step 4), so the requirement is:

> **2^W > 2 · R · D**, i.e. **W > 1 + log2(R · D)**.

**The assumption I am stating, rather than a size:** *D is bounded — a runnable
collector thread is scheduled at least once every D seconds.* This is the
load-bearing claim and it is the one that is usually left implicit. It is false
under a paused VM, a stopped debugger, or an unbounded-priority-inversion
scheduler; where it is false, **no fixed width is safe**, and the correct
response is not a wider counter but an external bound (step 5's attempt cap plus
a watchdog), or a logically unbounded stamp.

Under `R ≤ 10^8 writes/s` (one core saturating one cache line) and `D ≤ 60 s`,
the requirement is `2^W > 1.2 × 10^10`, so **W ≥ 34 bits**. 64 bits satisfies
this with ~90 years of headroom at that rate. **32 bits does not** — it wraps in
~21 seconds at that write rate, which is inside the assumed D. That is the
concrete reason to reject the size that "seems large."

#### Step 4 — a write that takes several steps

```cpp
void write_slot(Slot& s, int64_t v) {
    uint64_t g = s.stamp.load(std::memory_order_relaxed);
    s.stamp.store(g + 1, std::memory_order_release);   // odd: in progress
    s.value.store(v, std::memory_order_relaxed);       // may be several stores
    s.stamp.store(g + 2, std::memory_order_release);   // even: complete
}
```

`read_slot` rejects an odd stamp outright, and re-checks the stamp after reading
the value so a value torn across the write is caught even if the writer began
and finished within the read. **A partly-completed write is a failed pass, not a
collectable state** — an in-progress write is distinguishable from a stable one,
which the "bump only on completion" version cannot do.

#### Step 5 — what a repeatedly-failing collector does

```cpp
enum class SnapResult { Ok, NoQuietInterval };

SnapResult snapshot(Bank& b, int64_t out[N], int max_attempts = 8);
```

After `max_attempts` failed collections it returns `NoQuietInterval` — an
outcome, not a spin. The caller's defined responses, in the order I would reach
for them for an hourly audit:

1. **Guarded fallback.** Take the writers' lock and read under exclusion.
   Correct, blocks writers briefly, entirely acceptable for a once-an-hour audit
   — and it is the honest answer for a target under continuous write pressure,
   where no quiet interval will ever arrive.
2. **Report and defer.** Return "no consistent view available" and let the
   scheduler retry later. Correct where a stale audit is better than a stalled
   writer.

Not chosen: **helping** (each writer collects and publishes a view before its own
write, so a starving collector adopts one). It upgrades obstruction-freedom to a
stronger guarantee, but it makes *every write* pay a collector's cost, and the
adopted view must be placeable inside the collector's own interval. For an
hourly audit against a hot write path that trade is backwards.

#### Step 6 — the identically-shaped conditional update elsewhere

The bank recycles `Transfer` records through a lock-free free list:

```cpp
std::atomic<Transfer*> head;

Transfer* pop() {
    Transfer* h = head.load(std::memory_order_acquire);
    while (h && !head.compare_exchange_weak(h, h->next,
                                            std::memory_order_acq_rel)) {}
    return h;
}
```

**Same failure, one level down.** Thread 1 reads `h = A` and reads `A->next = B`,
then stalls. Thread 2 pops A, pops B, pushes A back — `head = A`, `A->next = C`.
Thread 1's CAS compares `head == A`, succeeds, and installs `B`, which is no
longer in the list. The comparison was true about the *word* and false about the
*structure*: the value returned to something previously observed.

**Same remedy — make consecutive states distinguishable:**

```cpp
struct alignas(16) TaggedHead { Transfer* p; uint64_t tag; };
std::atomic<TaggedHead> head;   // 128-bit CAS
// every push and every pop increments tag
```

And the width question recurs identically. A 16-bit tag packed into spare
pointer bits wraps after 65,536 pushes — trivially reachable within one
descheduled `pop`, so **16 bits fails the same test 32 bits failed above**.
Either use the 128-bit CAS, or remove the premise entirely with a reclamation
scheme (hazard pointers, or an epoch scheme) so the address cannot be recycled
while any `pop` holds it.

### 2. Success Check

| Bullet | Result |
|---|---|
| The schedule from step 1 is now rejected by the validation | **Met.** `stamp(A)`: 0 vs 4. |
| The counter cannot repeat a value within one collection under the stated assumption | **Met.** `W ≥ 34` derived from `2^W > 2RD`; 64 bits chosen; 32 bits explicitly shown to fail. |
| A partly-completed write is detectable rather than collectable | **Met.** Odd stamp → failed pass; stamp re-read after value. |
| Repeated failure has a defined outcome that is not an unbounded retry | **Met.** 8 attempts → `NoQuietInterval` → guarded fallback or deferral. |

### 3. Common Failures

- **"Comparing values because it needs no extra storage" — did not occur in the
  final artifact, but I nearly built a useless counterexample at step 1.** My
  first schedule had the writer complete both transfers *between* the two
  passes, cleanly: values matched and the view `(100,100)` **had** actually
  existed. That schedule demonstrates nothing. I had to interleave the
  collector's reads *inside* the transfer pair to produce a view that never
  existed. This is the near-miss worth recording: it is easy to produce a
  "written and written back" schedule that value comparison accepts *correctly*,
  and mistake it for the failure.
- **Sizing the counter by what seems large** — not committed; the size is
  derived from `2RD` and the 32-bit option is rejected by that arithmetic rather
  than by feel.
- **Advancing the counter only after a write completes** — not committed.
- **Fixing the collection and leaving an identically-shaped conditional update
  unprotected** — not committed, but only because step 6 exists. Left to my own
  judgement I would likely have stopped at step 5, since the snapshot was the
  stated problem.

### 4. Validity

**Valid.** Every file read cleanly, both cross-linked Patterns were present and
readable, and the capability under test — telling "unchanged" from "changed
back" — was exercised at every step.

One scope note, not a validity failure: step 6 says "apply the same reasoning to
a conditional update *elsewhere in the design*," but the design as constructed in
steps 1–5 has no such update until you invent one. The drill silently requires
the runner to extend their own artifact. That is a fair thing to ask, but it is
not stated.

### 5. What I consulted

- `DRILL_replace_value_validation_with_a_version_stamp` (the drill)
- `PAT_take_a_consistent_view_by_collecting_twice` — used for the validation
  rule, the in-progress-write requirement, the "obstruction-free, so define the
  give-up" argument, and the helping trade-off I rejected
- `PAT_keep_memory_alive_until_the_compare_and_swap_completes` — used for step 6:
  the recycled-address shape, the tagged-pointer remedy, and the reminder that
  the tag has the same wrap problem

---

## Drill 2 — `DRILL_run_the_decomposition_procedure_on_a_problem`

*Session B, position 2. Shares no ideas with drill 1; treat as near-cold.*

### 1. The work

**Problem chosen:** one step of a 5-point Jacobi heat-diffusion update on a 1024 × 1024 grid.
`u'[i][j] = 0.25 · (u[i−1][j] + u[i+1][j] + u[i][j−1] + u[i][j+1])`, boundary row/column held fixed.

**Target machine:** 16 execution units.

#### Step 1 — the axis

**Data.** Rejected the other two:

- **Steps.** The update is *one* operation, not several distinct operations that
  could run at once on the same field. There is nothing to run concurrently
  along this axis.
- **Stream/stages.** There is a candidate — successive time steps could be
  pipelined, with step *t+1* starting on a region as soon as step *t* finishes
  it. Rejected for *one* step, which is the stated problem: with a single step
  there are no items to occupy different stages. Worth recording that this axis
  reappears the moment the problem becomes "advance 1000 steps," where wavefront
  pipelining across time is a genuine alternative to re-synchronising the whole
  grid every step.
- **Data.** Every output cell is computed from the *previous* step's field, so
  all 1,048,576 outputs are mutually independent. The independence is in the
  data, and the piece set is fully known before the computation starts — so this
  is a partitioning problem, not a load-balancing one.

#### Step 2 — split maximally

**One piece per output cell: 1,048,576 pieces.**

Against 16 execution units that is **65,536×**, or 4.8 orders of magnitude.
Nothing about the number 16 entered this count — the count is `N²`, a property
of the grid. (See §Validity: this collides with the drill's stated 1–2 orders of
magnitude.)

#### Step 3 — what crosses, at the maximal split

Each interior piece needs 4 previous-step values, one from each edge-adjacent
piece. Counting a **crossing** as one value moving between two pieces, in one
direction:

- Adjacent pairs in a 1024×1024 grid: `2 · N · (N−1) = 2 · 1024 · 1023 = 2,095,104`
- Each pair crosses in both directions: **4,190,208 crossings**

Computation: 1,048,576 cells × ~5 flops = **5,242,880 flops**.
Crossings-to-flops ≈ **0.8**. At the maximal split the design is entirely
communication.

#### Step 4 — two groupings, both at 256 groups

256 groups is 16× the unit count — one order of magnitude of slack retained for
placement. Both groupings have exactly 4096 cells per group, so **work is
identical and perfectly balanced under both**; only the crossings differ.

**(a) Row stripes** — 256 stripes of 4 rows × 1024 columns.
Internal cut lines: 255 horizontal, each 1024 cells wide.
`255 × 1024 = 261,120` adjacent pairs cut → **522,240 crossings**.

**(b) Rectangular tiles** — a 16 × 16 arrangement of 64 × 64 tiles.
Internal cut lines: 15 vertical (each 1024 tall) + 15 horizontal (each 1024 wide).
`(15 + 15) × 1024 = 30,720` pairs cut → **61,440 crossings**.

#### Step 5 — comparison, and where the answer flips

| Grouping | Crossings | vs. step 3 | Per-group halo | Per-group transfers |
|---|---:|---:|---:|---:|
| Maximal split (step 3) | 4,190,208 | — | — | — |
| 256 row stripes | 522,240 | 8.0× fewer | 2,048 values | 2 |
| 256 square tiles | **61,440** | **68× fewer** | **256 values** | 4 |

**Tiles win, by 8.5×** on total crossing volume. The reason is
surface-to-volume: a stripe's halo is fixed at `2 × 1024` no matter how thin it
gets, while a tile's halo is `4√A` and shrinks with the group.

**Where it flips.** Volume is not the only cost. Model a group's communication as
`α·m + β·v` — `m` transfers of `v` values total, `α` the fixed per-transfer
cost, `β` the per-value cost:

- Stripe: `2α + 2048β`
- Tile: `4α + 256β` (and its two column halos are strided, so they need packing)

Tiles win when `4α + 256β < 2α + 2048β`, i.e. **`α < 896β`**.

- **Shared memory, 16 cores.** `α` is a cache-line transition, effectively a few
  `β`. `α/β ≈ 1` → **tiles win by roughly the full 8×**.
- **Distributed cluster.** `α ≈ 5 µs` message latency, `β ≈ 1 ns` per double.
  `α/β ≈ 5000 > 896` → **stripes win**, and the answer flips purely on the
  interconnect. The two contiguous stripe halos also transfer without packing,
  widening the gap further.

So the grouping is not a property of the problem. It is a property of `α/β`, and
896 is the number that decides it for this grid at this group count.

**A separate ratio the drill's wording conflates** — communication *to
computation*. Tiles: 256 values crossing per 20,480 flops ≈ `0.0125`. Stripes:
`0.1`. Both are small enough that a 16-way parallelization is worth doing at
all; this ratio answers "is this worth parallelizing," not "which grouping
wins." (See §Validity.)

#### Step 6 — placement, and what changes when the machine does

**Placement.** 16 units, 256 tiles → assign each unit a contiguous **4 × 4 block
of tiles**, i.e. a 256 × 256 sub-grid. This balances work exactly (16 tiles
each, all equal) and co-locates the heaviest communicators: the 4×4 block's
internal tile boundaries become intra-unit and cost nothing.

Remaining inter-unit crossings: 3 vertical + 3 horizontal cut lines × 1024 =
6,144 pairs → **12,288 crossings**, down from 61,440. Placement bought another
5×, entirely by using the slack step 4 deliberately preserved.

**If the unit count doubles to 32.** Steps 1, 2, 3 and 4 are unchanged — the
axis, the pieces, the dependency graph and the 256 groups are all properties of
the algorithm and the grid, not of the machine. **Only step 6 is redone.** 32
does not factor squarely, so the best rectangular assignment is 8 × 4 blocks of
128 × 256 cells: 7 vertical + 3 horizontal cut lines × 1024 = 10,240 pairs →
**20,480 crossings**.

Doubling the units raises inter-unit traffic by 1.67×, not 2× — the sub-optimal
aspect ratio costs the difference. Per unit, work halves while halo falls only to
0.83×, so efficiency degrades as expected from surface-to-volume.

**Where the design actually breaks:** at **256 units**, the 256 groups equal the
unit count and the slack is gone. At that point step 4 must be redone with
smaller tiles — and around there the `α < 896β` threshold shifts too, since the
threshold scales with halo size. That is the honest limit of this decomposition,
and it is a decomposition question, not a placement one.

### 2. Success Check

| Bullet | Result |
|---|---|
| Piece count after step 2 far larger than processor count, and nothing about the processors influenced it | **Met.** 1,048,576 vs 16; the count is `N²`. |
| Crossing totals for both groupings written down as numbers | **Met.** 522,240 and 61,440, plus 4,190,208 at the maximal split and 12,288 after placement. |
| Chosen grouping justified by those numbers plus a stated cost ratio | **Met.** Tiles, 8.5× on volume, flipping at `α = 896β`, with both sides of that threshold instantiated. |
| Final answer includes what changes when the machine changes | **Met.** Steps 1–4 unchanged; step 6 redone as 8×4; 20,480 crossings; breaks at 256 units. |

### 3. Common Failures

- **Splitting straight to the processor count** — not committed. Splitting to
  1,048,576 rather than 16 is what made step 5's comparison possible at all.
- **Skipping the second grouping** — not committed.
- **Deriving pieces from sequential order** — not committed, and the Jacobi form
  makes it easy to avoid: because the update reads the *previous* field, there is
  no sequential ordering to mistake for a dependency. Worth flagging that this
  drill is easier on Jacobi than on Gauss-Seidel, where the in-place update *does*
  create a false chain that only dependency analysis dissolves. **My problem
  choice made this failure harder to commit than it should have been.**
- **Producing a design that only works for the machine in front of you** — not
  committed.

### 4. Validity

**Valid, with two defects in the drill text** — the capability was exercised, but
two instructions are imprecise as written.

**(a) Step 2 contains a contradiction.** It says "Split as finely as the
algorithm allows — one piece per cell, not one per processor," then "confirm the
count is one to two orders of magnitude above the execution units you expect."
For any realistic grid these cannot both hold: one piece per cell on 1024² with
16 units is 4.8 orders, not 1–2. I resolved it by treating the order-of-magnitude
clause as a **floor**, which is how `AP_design_a_parallel_decomposition` words
its own gate ("If the split produced roughly as many pieces as processors, go
back"). But the drill states it as a *confirmation*, which a literal reader would
fail. The 1–2 orders figure belongs at the AP's **step 3 (merge)**, where I did
apply it — and the drill's own step 4 omits any group-count guidance, which is
where it was needed.

**(b) Step 5 names the wrong ratio.** It asks "at what ratio of communication
cost to computation cost the answer would flip." The stripes-versus-tiles flip is
not governed by communication-to-computation — both groupings have identical
computation, so that ratio cancels out of the comparison entirely. What governs
the flip is **latency-to-bandwidth (`α/β`)** within the communication cost.
Communication-to-computation decides whether to parallelize at all, which is a
different question owned by a different card. I answered both rather than guess
which was meant.

Neither defect blocked the run. Both would mislead a reader following the text
literally.

### 5. What I consulted

- `DRILL_run_the_decomposition_procedure_on_a_problem` (the drill)
- `AP_design_a_parallel_decomposition` — the four steps, the gates, the
  group-count guidance the drill omits, and the completion check that produced
  step 6's last answer
- `PAT_find_the_axis_the_parallelism_lies_along` — the three-way axis choice, and
  specifically the prompt that surfaced the stage axis I rejected for one step
  and flagged for many
- Confirmed `PAT_decide_if_the_problem_is_worth_parallelizing` exists
  (`core/performance/`) since the AP defers the "worth it" decision to it; did
  not read it, as the drill takes that decision as given

---

## Drill 3 — `DRILL_trace_divergence_and_coalescing_from_an_index_mapping`

*Session B, position 3. Shares the "mapping is one decision with two effects" idea
with drill 2's axis choice — weakest evidence of the three.*

### 1. The work

**Declared hardware model:** lockstep group = 32 threads; memory served in
**128-byte aligned units**; one unit fetched serves every request landing inside
it.

**Records:**

```cpp
struct Particle {          // 32 bytes, array 128-byte aligned
    float x, y, z;         //  0, 4, 8
    float vx, vy, vz;      // 12, 16, 20
    float charge;          // 24   <-- the field this routine touches
    int   id;              // 28
};
Particle p[1048576];       // N = 2^20
```

**Routine:** sum `charge` over all records, accumulating negative charges
separately.

```cpp
if (p[idx].charge < 0.0f) negSum += p[idx].charge;
else                      posSum += p[idx].charge;
```

**Threads:** T = 32,768, so each thread handles K = N/T = 32 records.

**Distribution of the branch condition:** record *i* has negative charge iff
`(i mod 1024) < 102` — **9.96% negative, arranged in contiguous runs of 102 out
of every 1024**. This is fixed for the whole exercise; only the mapping and the
layout change.

#### Step 1 — the mapping, written down

**Mapping S (strided by total thread count).** Thread *t* handles records
`t, t+T, t+2T, …`
At step *s*, thread *t* touches record `s·32768 + t`, field `charge` at byte
`32·(s·32768 + t) + 24`, and takes the negative branch iff
`((s·32768 + t) mod 1024) < 102`. Since `32768 = 32 · 1024`, that reduces to
**`(32w' + t') < 102`**, where `w'` is the warp index mod 32 and `t'` the lane
index.

**Mapping C (contiguous run per thread).** Thread *t* handles records
`32t … 32t+31`.
At iteration *j*, thread *t* touches record `32t + j`, at byte
`32·(32t + j) + 24 = 1024t + 32j + 24`, and branches on
`((32t + j) mod 1024) < 102`.

#### Step 2 — branch cost per group, as a sum of paths

**Mapping S.** Warp *w* (lanes `t' = 0…31`) touches records congruent to
`32w' … 32w'+31` (mod 1024), where `w' = w mod 32`. The predicate boundary sits
at 102. A warp diverges only if its 32-wide window straddles 102:

- `w' = 0,1,2` → windows `0–31, 32–63, 64–95` → all < 102 → **uniform negative**
- `w' = 3` → window `96–127` → lanes 96–101 negative, 102–127 positive → **diverges**
- `w' = 4…31` → windows `128–159 … 992–1023` → all ≥ 102 → **uniform positive**

**1 warp in 32 diverges.** Cost per warp-step, as the sum of paths taken:
`(31 × 1 + 1 × 2) / 32 = ` **1.031 paths**.

**Mapping C.** Warp *w* covers threads `32w…32w+31`, i.e. records
`1024w … 1024w+1023`. At iteration *j*, its lanes touch records
`1024w + 32t' + j`, which reduce mod 1024 to `32t' + j` — identically for every
warp. Negative iff `32t' + j < 102`, which holds for `t' ∈ {0,1,2}` (and
`t' = 3` when `j < 6`).

So **every warp holds 3–4 negative lanes and 28–29 positive lanes at every
iteration**. Cost per warp-iteration: **2.0 paths**. Every group, every
instruction.

**The proportion-independence check.** Hold mapping C and change the predicate to
`(i mod 1024) < 512` — the proportion of negative records goes from 9.96% to 50%,
but every warp still holds both sides at every iteration (now 16 lanes each).
**Cost is unchanged at 2.0 paths.** The proportion moved 5×; the cost did not
move at all, because the *distribution* — which lanes sit on which side — kept
both sides in every group.

#### Step 3 — transaction count for one instruction

The load is `p[idx].charge`, 4 bytes.

**Mapping S, AoS.** Warp addresses at step *s*: `base + 32t' + 24`, `t' = 0…31`,
where `base = 1,048,576·s` is 128-byte aligned. The 32 addresses span bytes
`base+24 … base+1016` — a 1024-byte window. `1024 / 128 = ` **8 transactions**.
Useful bytes: `32 × 4 = 128` of 1024 fetched → **12.5% efficiency**.

**Mapping C, AoS.** Warp addresses at iteration *j*: `1024t' + 32j + 24`,
`t' = 0…31`. **Stride 1024 bytes** — every lane lands in a different 128-byte
unit. **32 transactions**.
Useful bytes: `128` of `32 × 128 = 4096` → **3.1% efficiency**.

#### Step 4 — both numbers, both mappings

| Mapping | Branch cost (paths/group) | Memory cost (units/instruction) |
|---|---:|---:|
| **S** — strided, consecutive lanes → consecutive records | **1.031** | **8** |
| **C** — contiguous run per thread | **2.0** | **32** |

**Both costs move in the same direction, and both come from the same line of the
mapping.** The identical total work, the identical predicate, and the identical
data produce a 1.94× control-flow difference and a 4× memory difference, decided
entirely by whether lane index or thread index strides the record index.

#### Step 5 — layout change only, mapping untouched

Reorganize `Particle[]` into one array per field. `float charge[1048576]`,
128-byte aligned. **No mapping change.**

**Mapping S, SoA.** Addresses `4·(s·32768 + t') = 131072s + 4t'`. Base is
128-byte aligned; 32 lanes × 4 bytes = 128 contiguous bytes. **1 transaction.**
100% efficiency. *(8 → 1)*

**Mapping C, SoA.** Addresses `4·(32t' + j) = 128t' + 4j`. **Stride 128 bytes**
— exactly one unit apart, so every lane still lands in a distinct unit.
**32 transactions.** *(32 → 32, no change whatsoever.)*

Branch cost is untouched by the layout in both cases, as expected — the layout
does not move any lane across the predicate boundary.

#### Step 6 — which change bought the most, and did the costs move together

Taking the worst configuration as baseline
(**Mapping C + AoS: 2.0 paths, 32 transactions**):

| Change applied | Branch cost | Memory cost | Bought |
|---|---:|---:|---|
| baseline (C, AoS) | 2.0 | 32 | — |
| **layout only** (C, SoA) | 2.0 | 32 | **nothing at all** |
| **mapping only** (S, AoS) | 1.031 | 8 | 1.94× control, 4× memory |
| both (S, SoA) | 1.031 | 1 | 1.94× control, 32× memory |

**The mapping bought the most — and it is not close.** The layout change, applied
alone, bought **exactly zero**: under mapping C, splitting records into per-field
arrays moves the stride from 1024 bytes to 128 bytes, which is still one full
unit per lane. The array-of-structures-to-structure-of-arrays transformation is
the reflexive fix here, and on its own it is worthless. Its value is entirely
conditional on the mapping: given mapping S it turns 8 transactions into 1, but
given mapping C it turns 32 into 32.

**The two costs moved together, in the same direction, under the same single
change.** Both are consequences of `idx = f(lane)`: mapping S makes consecutive
lanes touch consecutive records, which simultaneously keeps each group inside one
102-wide run of the predicate *and* inside one contiguous address span. Mapping C
makes consecutive lanes touch records 32 apart, which simultaneously spreads each
group across the predicate boundary *and* across 32 units. There is no
configuration in this exercise where one cost improves and the other degrades —
which is the drill's point, and it survived the arithmetic.

One caveat on the numbers, not the conclusion: I counted 128-byte units. Hardware
that tracks 32-byte sectors within a line gives mapping S + AoS **32 sectors**
rather than 8, and SoA **4** rather than 1. The 8× layout gain under mapping S
and the 0× gain under mapping C both hold either way; the absolute counts do not.

### 2. Success Check

| Bullet | Result |
|---|---|
| Both costs reported as counts derived from the mapping | **Met.** 1.031 / 2.0 paths; 8 / 32 / 1 units — all derived from `(32w'+t') < 102` and the address arithmetic. |
| Branch cost is the sum of paths taken, and does not change when the proportion changes without changing the distribution | **Met.** Proportion 9.96% → 50% under mapping C, distribution shape unchanged, cost stays 2.0. |
| The two mappings produce different numbers for both costs, and the relationship is stated | **Met.** 1.031/8 vs 2.0/32; both driven by the same `idx = f(lane)` and moving together. |
| Layout and mapping changes evaluated separately | **Met.** Layout-alone measured under mapping C (bought nothing) and under mapping S (8→1) before the two were combined. |

### 3. Common Failures

- **Reasoning about one thread's access pattern** — not committed, but the trap
  is live in this problem and worth recording concretely: under **mapping C**,
  each individual thread walks records `32t … 32t+31` — 1024 perfectly
  contiguous bytes, the textbook-ideal single-threaded sweep. It is also the
  *worst* configuration in the whole table. The per-thread view and the
  per-group view point in opposite directions here.
- **Reporting divergence as a percentage** — not committed. Both configurations
  have the same 9.96% negative records; the costs differ by 1.94×.
- **Assuming a cache-friendly layout is good here** — not committed, and the
  SoA-under-mapping-C result is the direct evidence: the canonical GPU layout fix
  bought nothing when the mapping was wrong.
- **Changing mapping and layout in the same step** — not committed. Steps 4 and 5
  were measured separately, which is the only reason the "layout alone buys zero"
  result is visible at all.

### 4. Validity

**Valid, with one substantive defect in the drill and one gap in retrieval.**

**(a) The Success Check can fail through no fault of the runner.** The bullet
*"The two mappings produce different numbers for both costs"* is not guaranteed
by the drill's own instructions, because step 1 lets the runner choose the branch
distribution and nothing constrains that choice. I checked: with a **uniformly
random 10% negative** distribution, the probability a warp is uniform is
`0.9³² ≈ 0.034` under *both* mappings, so both give ≈1.97 paths and the mapping
change moves the branch cost by nothing. The memory cost still differs (8 vs 32),
but the bullet demands *both*. A runner who reaches for a random distribution — a
natural choice — does correct work, reports correct numbers, and fails the
Success Check. **The drill needs to require a distribution with structure at the
group scale**, or the bullet needs to be weakened to the memory cost plus a
statement of when the branch cost does and does not follow.

**(b) The unit size is not fixed.** Step 3 says "fixed-size aligned units"
without naming a size, and real hardware has two granularities (128-byte lines,
32-byte sectors) that give different counts for the same mapping. I declared 128
bytes and reported the sector figures as a caveat. This is arguably deliberate —
`PAT_lay_data_out_for_the_group_that_reads_it_together` explicitly says the unit
size is "a value to derive rather than embed" — but it means two correct runs of
this drill produce different numbers, which weakens it as a check.

**(c) Retrieval gap, not a defect.** The cross-linked
`PAT_lay_data_out_for_the_group_that_reads_it_together` lives in
`core/performance/`, not `core/concurrency/`. Same package, so it passes
validation and is legitimately reachable — but it does not appear in the
concurrency index or directory, and I found it only by grepping the object ID out
of the drill's front matter. A runner working from the concurrency INDEX alone
would not find the card that owns half this drill's content.

### 5. What I consulted

- `DRILL_trace_divergence_and_coalescing_from_an_index_mapping` (the drill)
- `PAT_keep_a_lockstep_group_on_one_path` — the cost-is-the-sum-of-paths rule,
  the proportion-versus-distribution distinction, and the claim that memory
  access has the same grouped structure
- `PAT_lay_data_out_for_the_group_that_reads_it_together` (`core/performance/`) —
  count units not accesses; the records-to-fields transformation; alignment and
  straddling; the explicit warning that a good single-thread stride can be the
  worst group pattern

---

# Across the three drills

## Instructions that were ambiguous, circular, or impossible as written

**One genuine contradiction.** `DRILL_run_the_decomposition_procedure_on_a_problem`
step 2 requires both "one piece per cell" and "one to two orders of magnitude
above the execution units." These are incompatible for any grid worth
parallelizing. The 1–2 orders figure belongs at the *merge* step, where the AP
puts it and where this drill's step 4 currently gives no guidance at all.

**One misnamed quantity.** The same drill's step 5 asks for the ratio of
*communication cost to computation cost*, but the stripes-versus-tiles decision is
governed by *latency to bandwidth*; computation is identical across the two
groupings and cancels out. A runner who answers the question as literally asked
produces a number that cannot flip the decision.

**One under-specified constant.** Drill 3 step 3 leaves the memory unit size
open, so two correct runs yield different transaction counts.

Nothing was circular, and nothing was impossible.

## Success Checks satisfiable without doing the work

**Drill 1, the counter-width bullet, is the weakest check in the set.** *"The
counter cannot repeat a value within one collection under the stated assumption"*
is satisfiable by choosing a convenient assumption — "collections complete within
a millisecond" makes 32 bits trivially sufficient, and the bullet is met. Nothing
forces the assumption to be defensible or even to be about the right quantity.
The drill's own step 3 is better than its check: it says to size the counter "in
terms of the longest interval any participant could be delayed," which is the
load-bearing bound. The check should demand that the assumption name a delay
bound and say what happens when nothing bounds it.

**Drill 2's first bullet has an unverifiable clause.** *"...and nothing about the
processors influenced it"* is a claim about the runner's reasoning process, not
about the artifact. It cannot be checked from the output. The observable version
already exists as the AP's gate: if the piece count is within a small factor of
the unit count, the split was really a mapping.

**Drill 3's third bullet can fail on correct work**, as detailed above — the
inverse problem, and the more serious one, since it penalises a runner who did
everything right.

**Drill 1's first bullet and drill 2's crossing-total bullets are strong** — they
cannot be met without producing the schedule or the numbers.

## Knowledge the library did not contain

**None of the three required anything absent.** Every card the drills cross-link
exists, is readable, and carried what the drill needed:

- Drill 1's two Patterns between them supplied the validation rule, the
  in-progress-write requirement, the counter-width argument, the give-up policy,
  and the recycled-address recurrence at step 6. Step 3's `2^W > 2RD` derivation
  is not written down anywhere, but both cards state the requirement it
  formalises.
- Drill 2's AP supplied the group-count guidance its own drill omits, and the
  completion check that produced step 6's final answer.
- Drill 3's two Patterns supplied both cost rules and the explicit statement that
  they share a cause.

Two structural observations rather than gaps:

1. **`core/concurrency/` at 57 objects is dense enough that the INDEX is now a
   bottleneck.** It lists topics and counts, not object names, so locating a
   specific card meant listing the directory. Drill 3's second Pattern lives in
   `core/performance/` and is invisible from the concurrency side entirely.
2. **The layered structure held up.** Drill 1 needed only concurrency cards;
   drill 2 reached into `performance/` for the "worth parallelizing" decision it
   correctly declined to re-litigate; drill 3 needed a performance card for half
   its content. No drill needed anything from outside `software-engineering/core`,
   and none needed `metaskills` — which I loaded per the skill's load order and
   did not draw on.

## Position effects

Drill 3 ran third, after drill 2 had already established "the mapping/axis is one
decision with several downstream effects." That idea is drill 3's central claim,
so **drill 3's result is the weakest evidence in this session** and should be read
that way. Drills 1 and 2 share no content that I noticed, and drill 1 was
genuinely cold.

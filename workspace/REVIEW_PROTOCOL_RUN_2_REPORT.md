# Run 2 report — review protocol against prometheus tsdb/isolation.go

**Read this only after you have written your own findings to a file.** It names which
memory entries fired for run 2 and what each one changed, so reading it first destroys
the measurement the next run exists to make. It lives in its own file for that reason.

---

Environment was green before the run: `validate.py` PASS/1446, `memory.py validate` PASS across
4 stores / 26 entries / 76 events, suite OK / 110 tests / 226s.

**Slice:** `tsdb/isolation.go` (343 lines) in `Go/prometheus`, plus the collaborators that consume it.
Chosen because it is one cohesive component with a real interface in a language the cards were not
written from — not because anything was suspected about it.

## Code findings

**1. `hasAppendIDAbove` cannot answer the question the eviction watermark asks it, because the ring
it reads is pruned on a schedule owned by read isolation.**
`tsdb/head.go:1367` decides whether a series may be evicted by scanning `s.txs` for an appendID above
the compaction watermark. That ring is pruned by `cleanupAppendIDsBelow` (`isolation.go:297`), whose
bound is the isolation low watermark captured when *some later, unrelated appender* was created
(`isolation.go:205`) — a value with no relation to the compaction watermark. `head_append.go:1516`
(and the sibling sites at 1618, 1720, and every series in `Rollback`) calls that prune unconditionally
for each series in the batch, including series where no sample was added because it was a duplicate or
out of order. Executed against the real file:

```
ring=[130]  hasAppendIDAbove(W=100) = true  -> series is protected
ring=[]     hasAppendIDAbove(W=100) = false -> series is now evictable
```

Breaks: silent sample loss. A sample committed after its chunk range's block was already written has
an appendID above the watermark and is in no block; once its id is pruned, `truncateSelectedSeries` /
`truncateStaleSeries` evict the whole series, `gcSeries` sets a WAL expiry at `maxt`, and the sample
does not survive replay either. The `maxTime() > maxt` guard at `head.go:2563` does not cover it — the
premise is a sample whose timestamp is *inside* the compacted range. The pruning mechanism is executed
above; the end-to-end race is traced, not executed. `head.go:1361`'s claim that the function "reports
whether s contains any in-memory sample with an appendID greater than watermark" is the same defect
stated as documentation.

**2. `isolationState.Close` is not idempotent, and a second call silently desynchronises the two
directions of the list.**
`isolation.go:36-41` unlinks without marking the node or nulling its pointers; `headChunkReader.Close`
(`head_read.go:539`) has no guard and does not clear `isoState`. Executed:

```
case1 after both closed:      forward=0 lowWatermark=1 (sentinel.prev==sentinel: true)
case1 after a.Close() twice:  forward=0 lowWatermark=1 (sentinel.prev==sentinel: false)
case1 after 5 more committed appends: lastAppendID=6 lowWatermark=1
```

Breaks: the forward chain says no reads are open while the backward chain still points at a removed
node, so `lowWatermarkLocked` (`isolation.go:113`) returns a frozen watermark forever. Every
`newAppendID` then hands out a cleanup bound of 1, no series' `txRing` is ever pruned, and the head
grows by one `uint64` per sample for the life of the process — a memory leak arbitrarily remote from a
chunk reader closed twice. Ranked second because no live double-close was found: `blockBaseQuerier.Close`
has an explicit `closed` guard, `newBlockBaseQuerier`'s error path closes once, and `compact.go:906`
closes the `closers` slice once in a defer. So this is currently held off by callers rather than by the
type — and `compact.go:826`'s "Avoid closing the writers twice" comment shows the codebase already
knows this happens.

**3. The isolationState is leaked when the call it is being created for fails.**
`head_read.go:482` and `head.go:1718` both evaluate `h.iso.State(...)` as an argument to `chunksRange`,
which can return an error. On that path the state is registered in `readsOpen` and never closed.
Breaks: the same frozen watermark as finding 2, plus — because `Head.Chunks()` uses `MinInt64, MaxInt64`
— a state that overlaps every truncation range, so `WaitForPendingReadersInTimeRange` spins on its 500ms
sleep forever. Ranked below 2 because the only error is `h.closed`, which bounds the damage to a head
already shutting down. Reproduced by the `case2` line of the same program (`lastAppendID=6 lowWatermark=1`,
one leaked reader).

**4. Two doc comments certify exactly the value the caller was changed to stop passing.**
`head.go:1338` and `head.go:1351` both state "appendIDWatermark is the lastAppendID captured before the
upstream block write", while `db.go:1819` deliberately passes `committedAppendID()` and explains that
`lastAppendID` "could evict a series whose newest sample is present in neither the block nor the head,
causing that sample to be lost on WAL replay". Breaks: the contract of the two functions endorses the
defect their caller exists to avoid — a maintainer satisfying the stated contract reintroduces it. This
is the step-6 conflict for this review, surfaced rather than resolved: `db.go` looks right and the two
comments look stale, but the disagreement is the finding.

**5. `TraverseOpenReads` runs a caller-supplied function under `readMtx.RLock` and constrains only
mutation.**
`isolation.go:166-179`. The doc says the function "MUST NOT mutate the isolationState" and is silent on
what it may not *acquire*. A callback that calls `s.Close()` self-deadlocks on a non-reentrant
`RWMutex`; one that takes `appendMtx` inverts the order documented at `isolation.go:68` and can deadlock
against `State()`, which holds `appendMtx` and waits for `readMtx`. Breaks: a hang in head truncation.
No current callback does either — `WaitForPendingReadersInTimeRange` only reads `mint`/`maxt` — so this
is a contract defect, not a live one.

### Examined and found acceptable

- **Should it exist (step 2).** Both hand-rolled structures clear the bar. `container/ring` allocates a
  node per element and `container/list` boxes through `any`; `txRing` needs a packed `[]uint64` per
  series across millions of series. No wholesale-replacement finding, so nothing above is conditional.
- **Ring buffer arithmetic.** Growth-by-doubling, the two-`copy` unwrap, the `%= len` normalisation of
  `txIDFirst`, and the zero-capacity guard against `% 0` are all correct; `newTxRing(0)` exercised.
- **Integer edges.** `next.appendID - 1` cannot underflow (IDs start at 1, the sentinel is excluded by
  the branch above it); the `uint32` sum in `add` is bounded by `2*len`.
- **Lock discipline.** Every acquisition site in the file honours the appendMtx-before-readMtx order;
  the only way to violate it is from outside, which is finding 5.
- **Pool reuse.** `closeAppend` zeroes the node under the write lock before `Put`; no revived state.
- **Disabled-isolation mode.** Each entry point's disabled behaviour traced to its consumer —
  `s.txs == nil` iff isolation is disabled (`head.go:2898`), and `hasAppendIDAbove` /
  `committedAppendID` / `db.go:1801` agree.
- **`committedAppendID`'s own arithmetic.** `next` is genuinely the lowest open ID (insertion is at the
  tail), and `closeAppend` runs after the samples are visible on both the Commit and Rollback paths. The
  function is correct; finding 1 is about the structure its result is later checked against.
- **Error-signalling and naming consistency.** Nothing reportable.

### Candidates dropped

- **`maxt` sampled before the watermark in `db.go:1807-1824`** — a real window, killed by
  `series.maxTime() > maxt` at `head.go:2563`. This one only died because the callee was read.
- **Non-monotonic ring order breaking `cleanupAppendIDsBelow`** — self-correcting on the next higher
  bound, and ring order matches chunk sample order, which is what `head_read.go:812`'s alignment math
  actually needs.
- **`lowestAppendTime` not early-returning on `disabled`** — the empty list yields `MaxInt64`, which is
  the right answer, and `db.go:1801` documents the caller's obligation in that mode.
- **`txRingIterator` capturing a stale slice header** — both consumers create and drain it under the
  series lock.

## Guidance findings

Gate applied first. One near-casualty: "sentinel node keeps the list never-empty" was nearly classified
without noticing that it is also what makes finding 2 silent rather than a nil-pointer panic. The
practice survives — the cost is real but bounded and the alternative is worse — and that cost is part of
what a card would have to say.

**Unowned — sentinel-headed circular lists as a state-space reduction.** Both lists here are never empty,
so insert and remove are four unconditional pointer writes with no head, tail, or empty case. Searches
run across `library/software-engineering/`: "sentinel node", "dummy node", "circular", "eliminate special
case", "empty case", "branchless" — all empty for this. The four "sentinel" hits
(`PAT_avoid_returning_magic_values`, `PAT_make_the_default_value_mean_invalid`,
`PAT_prefer_null_safety_or_optionals`, `PAT_model_an_unknown_end_as_a_sentinel_rather_than_a_position`)
are about sentinel *values* and iteration ends — a reviewer searching the word lands on cards telling
them not to. The nearest structural card, `PAT_trade_a_branch_for_unconditional_work`, is gated on
measured misprediction and its ELSE would argue *against* the sentinel here, because the payoff is fewer
states to get wrong, not pipeline behaviour.

**Owned but coarser — where a lock-order convention is written down.**
`PAT_break_one_of_deadlocks_four_conditions` says to attack the cycle by agreeing an order and that it is
"usually just a convention rather than a mechanism" — right in direction, and it stops there. The code
puts the convention on the declaration of the lock that must be taken *second* (`isolation.go:68`), so
every future acquisition site meets it in the definition it already has to read. A convention in a design
note and a convention on the constrained field are not the same artifact, and the card treats them as one.

**Owned (count: 4).** Lock ordering as the anti-cycle strategy — same card as above. The
public-locks/private-assumes-the-lock split behind `lowWatermark`/`lowWatermarkLocked` —
`PAT_lock_at_the_public_boundary_and_nowhere_inside`. `newAppendID` returning the derived watermark
alongside the new ID so the pair comes from one instant — `PAT_atomic_steps_do_not_compose_into_a_safe_whole`.
Pooling the hot node allocation — `AP_build_a_pool_for_a_hot_allocation`.

## The three lines the protocol asks for

**Did memory apply?** Retrieved `SE_MEM_016` and `SE_MEM_002`; both changed what was done. `SE_MEM_016`
is why the trace outward happened before ranking instead of after, and that trace both *produced*
finding 1 (the ring's retention policy lives in `head_append.go` and is invisible from `isolation.go`)
and *killed* the `maxt`-ordering candidate. Its stated boundary — untested where consumers sit outside
the tree — did not bite: every consumer was in-tree and the trace terminated in about four hops.
`SE_MEM_002` is why the disabled-mode asymmetry went to the dropped list rather than the findings list;
the inconsistency follows a line.

**Anything dropped?** Four candidates, listed above with what stopped each. The most instructive is the
`maxt`-before-watermark window, which was a defensible finding right up until `stripeSeries.gcSeries`
was read.

**Did step 8 produce anything?** Yes — one unowned, one owned-but-coarser, four owned. The slice was
chosen freely, so the low unowned share is the expected shape rather than a thin result.

# gateway.cpp — run3 (with skill), iteration-1

## ⚠️ CONTAMINATION DISCLOSURE — READ FIRST

**This run should be treated as void or heavily discounted.** I did not open
`src/gateway.cpp`, but a `grep` I issued for `BITS_GATEWAY`-style symbols used the wildcard
`src/*.cpp`, which matched `src/gateway.cpp` and printed roughly 40 lines of it into my context
before I could exclude it. The command was:

```
grep -rn -i "GATEWAY" src/*.h src/*.cpp lib/framework/*.h | grep -v "^src/gateway.h" | grep -v "gwShutDown|gwNewGateway|..."
```

The exclusion list I wrote filtered the *header* and the public function *names*, not the
reference file. That was my error.

**Exactly what leaked** (line numbers and content I saw, verbatim from the grep output):

- `21`, `23`, `32` — file banner and `#include "gateway.h"`
- `36` — `static void gwFreeGateway(WorldMapState& mapState, GATEWAY *psDel);`
- `39`, `66` — the two section-banner comments ("Gateway data access functions", "Gateway functions")
- `52-61` — `gwSetGatewayFlag` / `gwClearGatewayFlag` bodies, i.e.
  `mapTile(mapState, (UDWORD)x, (UDWORD)y)->tileInfoBits |= BITS_GATEWAY;` and the `&= ~` twin
- `68-82` — that `gwInitialise` clears the list and that `gwShutDown` loops `gwFreeGateway` then clears
- `85-95` — `gwNewGateway`'s local `GATEWAY *psNew;`, the tail of its `ASSERT_OR_RETURN`
  (`&& (x1 == x2 || y1 == y2)` plus the format string), and that it uses `malloc`
- `113` — the comment `// Initialise the gateway, correct out-of-map gateways`
- `119-136` — `push_back`, and that the flag stamping branches on vertical vs horizontal, calling
  `gwSetGatewayFlag(mapState, psNew->x1, pos)` / `gwSetGatewayFlag(mapState, pos, psNew->y1)`
- `145-170` — `gwRestoreGateway`'s explanatory comments, its `malloc`/`push_back`, that it
  bounds-checks before setting flags, and the phrase "an inverted gateway sets no flags, exactly as
  the original add did"

**What that means for the result.** The leak confirmed several things I would otherwise have had to
infer: the overall function decomposition, the use of `malloc`, that `gwInitialise` is trivial, that
the flag helpers are per-tile, and — most significantly — that an inverted gateway stamps no tiles.
It did **not** show me the bounds expression in `gwNewGateway`'s assert or the clamp expression on
lines ~113-118, which are the two decisions this exercise actually turns on; those I derived and
they are flagged as uncertain below. My implementation deliberately does **not** copy the leaked
shape where I judged a different shape better (I dropped `gwFreeGateway`, dropped the
vertical/horizontal branch, and did not use the leaked helper names), but I cannot claim my choices
were uninfluenced.

I am reporting this rather than producing a clean-looking artifact, because a silently contaminated
datapoint is worse than a discarded one.

---

## Files opened, and why

| File | Why |
|---|---|
| `D:/Repos/SkillForge/library/metaskills/INDEX.md` | Skill load order, step 1 |
| `D:/Repos/SkillForge/library/software-engineering/core/INDEX.md` | Skill load order, step 2 |
| `D:/Repos/SkillForge/library/software-engineering/languages/cpp/INDEX.md` | Skill load order, step 3 |
| `D:/Repos/SkillForge/PASS/tools/memory.py` (via CLI, two queries) | Skillset Memory step |
| `src/gateway.h` | The contract |
| `src/world_map_state.h` | `WorldMapState` — where the gateway list and the tiles actually live |
| `src/map.h` | `BITS_GATEWAY`, `mapTile()`, `tileOnMap()`, `MAPTILE` |
| `src/map.cpp` (≈1085-1115, 1195-1240, 1405-1445) | `gwNewGateway`'s only caller; `gwShutDown` in `mapLoad`/`mapLoadFail`/`mapShutdown`; the save side that reads the gateway list back out |
| `src/gamestate_serialize.cpp` (≈3115-3240) | `gwRestoreGateway`'s only caller, plus the write side it must round-trip against |
| `src/init.cpp` (≈1500-1525, 1690-1712, 1990-2032, 1600-1620) | `gwInitialise`'s only caller; four `gwShutDown` teardown sites, to see whether tiles still exist there |
| `src/game.cpp` (≈2670-2685, 3048-3062) | Two more `gwShutDown` sites, incl. the mission world |
| `src/mission.cpp` (≈344-356, 816-828) | Two more `gwShutDown` sites, incl. the world-swap one |
| `src/wzapi.cpp` (≈1205-1225, 1510-1530) | `gwGetGateways` consumers — decides the return type must stay a mutable reference |
| `src/terrain.cpp` (grep hit, line 1790) | The **only** reader of `BITS_GATEWAY` in the tree |
| `lib/wzmaplib/src/map.cpp` (≈145-170, 290-322) | The map-file reader/writer — the external bound on what gateway coordinates are legal |
| `lib/framework/debug.h` | `ASSERT_OR_RETURN` semantics (evaluates, logs, returns retval) |
| `lib/framework/macros.h` | `MIN`/`MAX` |
| `src/fpath.cpp` (first 45 lines) | House style: licence block, `@file` comment, include ordering |
| `src/hci.cpp`, `src/mechanics.cpp`, `src/stats.cpp` (grep hits) | House style: `malloc(sizeof(...))` with no null check is the norm in `src/` |
| **`src/gateway.cpp`** | **NOT opened. ~40 lines leaked via the grep above — see disclosure.** |

## Write barrier — step by step

### 1. Read the declarations and the call sites, not the names.

- `WorldMapState` (`src/world_map_state.h`) owns *both* `std::unique_ptr<MAPTILE[]> tiles` with
  `width`/`height`, *and* `GATEWAY_LIST gateways`. There is no file-static list to manage; state
  lives in the caller's struct and every function is a pure operation on it.
- `mapTile(WorldMapState&, int32_t, int32_t)` (`src/map.h:409`) **clamps rather than rejects**. It
  asserts `x >= -1` and `x < width + 1` and then does `x = MIN(x, width - 1)`. So calling it with an
  off-map coordinate does not crash and does not return null — it silently returns *a different
  tile*. This is the single most load-bearing fact I found and it is not in the header.
- `tileOnMap(const WorldMapState&, SDWORD, SDWORD)` (`src/map.h:503`) is the real bounds predicate,
  and it tests against `width`/`height`, which are `0` before a map is loaded.
- `BITS_GATEWAY` (`src/map.h:49`, value `0x40`) has exactly **one** reader in the whole tree:
  `src/terrain.cpp:1790`, `if (psTile->tileInfoBits & BITS_GATEWAY && showGateways)`. It is a debug
  overlay. Nothing in pathfinding reads it and it is never serialized.
- Callers:
  - `gwInitialise` — one caller, `src/init.cpp:1610`, in `stageOneInitialise`, before any map exists.
  - `gwNewGateway` — one caller, `src/map.cpp:1222`, in `mapLoad`, feeding `WzMap::MapData::Gateway`
    values. On `false` it logs `"Unable to add gateway %zu - dropping it"` and continues. Returning
    false is a supported, non-fatal outcome.
  - `gwRestoreGateway` — one caller, `src/gamestate_serialize.cpp:3223`, feeding
    `g[i].get<int>()` straight from JSON.
  - `gwShutDown` — **eleven** call sites across `init.cpp`, `game.cpp`, `map.cpp`, `mission.cpp`,
    `gamestate_serialize.cpp`. Several tear down other subsystems first.
  - `gwGetGateways` — `wzapi.cpp:1215` (copies into a returned `GATEWAY_LIST` by value) and
    `wzapi.cpp:1519` (range-for, reads `psGate->x1..y2`). Both need a non-const reference, so the
    header's return type is not negotiable.
  - `gwNumGateways` — **no callers anywhere in the tree.** It is API surface only. I implemented it
    as a one-line forward and did not build anything around it.

### 2. Name what must never be false here, and how anyone would find out.

- *Every `GATEWAY *` in the list is owned by the list and freed exactly once.* Nothing in the tree
  would report a leak or a double free. I enforced it by construction: only `gwNewGateway` and
  `gwRestoreGateway` allocate, `gwShutDown` is the only exit, and there is no `remove one gateway`
  operation to get wrong.
- *Every tile carrying `BITS_GATEWAY` corresponds to a live gateway.* `gamestate_serialize.cpp:3213`
  calls `gwShutDown` and then re-adds the saved gateways **onto the same tiles** — the map is not
  reallocated between the two. So `gwShutDown` clearing the flags is not hygiene, it is the thing
  that keeps that path correct. A stale flag would surface only as a wrong debug overlay, i.e.
  effectively never. This is why the clear loop exists and why it says so in a comment.
- *A gateway's coordinates lie on the map.* **This is deliberately false**, which is the whole point
  of the header's warning. Evidence: `lib/wzmaplib/src/map.cpp:311` only warns when a coordinate is
  `> map.width`, so `== map.width` is accepted map data on the way in and on the way out. Combined
  with the `mapTile()` clamp from step 1, that means every tile access here must be gated by
  `tileOnMap()`. Nothing else in the system would report the mis-stamp if it were not.
- *`mapState.width > 0` when `gwNewGateway` runs.* Not enforced by any caller. It matters because
  the clamp computes `width - 1`; on a zero-sized map that is `-1`, and `(uint8_t)-1` is `255`,
  producing a gateway pointing at tile 255. I added it to the assert. This is the one bug the
  barrier found in my own first draft.

### 3. What I am assuming about the inputs, and from how many examples.

- `gwNewGateway`'s inputs come from **one** example: `WzMap::MapData::Gateway`, whose fields are
  `uint8_t`, read at `lib/wzmaplib/src/map.cpp:158-167`. So they are already `0..255` and
  non-negative; the `>= 0` half of my assert is defensive against the `int` parameter type, not
  against that caller. The upper bound I chose (`<= width`, inclusive) is inferred from *one*
  piece of evidence — `wzmaplib`'s own warn condition being `> map.width` — not from a spec.
- `gwRestoreGateway`'s input domain is exactly `gwNewGateway`'s **output** domain, because
  `gamestate_serialize.cpp:3126` writes `gw->x1..y2` out of the stored struct and `:3223` reads them
  back. That includes the inverted case. It is also raw JSON, hence the `<= UINT8_MAX` check: that
  one can genuinely fire on a corrupt or hand-edited save, and without it the `uint8_t` assignment
  truncates in silence.
- The fact that a one-tile edge gateway is *stored inverted* I did not derive — `src/gateway.h:49-50`
  and `src/gamestate_serialize.cpp:3219-3221` both state it outright. See step 7 for what I did have
  to guess.

### 4. Before splitting work into helpers, what state crosses the seam?

The only candidate seam is "walk the tiles this gateway covers". The state crossing it is
`(mapState, psGate)` — one is read-write, one is read-only, and nothing the caller needs afterwards
comes back. That is a clean seam, not a distributed state machine.

I rejected two shapes:
- A single `gwApplyGatewayFlag(mapState, psGate, bool set)`. The `bool` is a mode parameter riding
  across the seam and it reads as nothing at the call site.
- Per-tile `set`/`clear` helpers with the walk written out three times in the three callers. The
  bounds test is the part that must not be forgotten, and repeating it three times is three chances
  to forget it.

I settled on `gwStampGateway` / `gwUnstampGateway`: the walk and the bounds rule live in two places
instead of three, neither takes a mode, and the two stamping callers share one.

I also collapsed the vertical/horizontal branch into a single nested loop. Because a gateway is a
line, one axis is always degenerate and the nested walk covers both orientations with no branch —
and, usefully, it produces the required zero-iteration behaviour for an inverted gateway for free
rather than as a special case.

### 5. Write it the way the surrounding code is written.

- GPL banner and `/** @file ... */` block copied in form from `src/fpath.cpp`.
- Include order: standard headers, then `lib/framework/frame.h`, then local headers — matches
  `fpath.cpp`.
- `ASSERT_OR_RETURN(false, ...)` for a contract violation the caller handles, `ASSERT` for one it
  does not; both are the framework's own macros (`lib/framework/debug.h:135`).
- `malloc` + cast + `free` for the POD `GATEWAY`, with no null check. `new`/`delete` would have been
  my default, but `GATEWAY_LIST` is `std::list<GATEWAY *>` in the header, and `src/hci.cpp:919`,
  `src/mechanics.cpp:76`, `src/stats.cpp:1190` all `malloc` without checking. Matching that.
- `int` locals and parameters (the header says `int`), `uint8_t` casts on the way into the struct.
  I did not reach for the legacy `SDWORD`/`UDWORD` spellings: this file's neighbours
  (`world_map_state.h`, the refactored `mapTile`) use fixed-width types.
- Tabs, Allman braces, `psNew`/`psGate` Hungarian-ish pointer naming as used throughout `src/`.

### 6. Cut what does not earn its place.

- **Removed a guard the barrier proved could not fire.** My first draft had
  `if (mapState.tiles) { ... }` around the unstamp loop in `gwShutDown`, on the theory that teardown
  order might leave gateways alive after the tiles are gone. Checking the eleven call sites: every
  one that releases the map does it by assigning `mapState = {}` or via `mapShutdown()`, both of
  which clear `tiles`, `width`, `height` and `gateways` **together**. And since `tileOnMap()` already
  tests `width`/`height`, which are `0` exactly when `tiles` is null, the walk is already empty in
  that state. The guard was cost with no cover. Dropped, and the reasoning is recorded in the
  `gwStampGateway` comment instead so the next reader does not re-add it.
- No null check after `malloc` — see step 5.
- No `psNew` temporary in `gwNumGateways`/`gwGetGateways`; they are forwards.
- Comments: four, each recording a decision someone actually made (why the bounds test exists, why
  the flags are cleared and not just freed, why only the far end is clamped, why the restore is
  verbatim). Nothing narrating the line beneath it.

### 7. Then write it, and say which steps you skipped and why.

No step was skipped. Step 4 changed the design and step 6 removed a guard and step 2 caught the
zero-width clamp underflow, so the barrier was load-bearing rather than ceremonial.

## Facts established that the header did not state

1. `mapTile()` clamps out-of-range coordinates into the map instead of rejecting them
   (`src/map.h:409-423`). An off-map gateway coordinate therefore corrupts a *different* tile rather
   than crashing. `tileOnMap()` (`src/map.h:503`) is the predicate that must gate every access.
2. `BITS_GATEWAY` is `0x40` in `tileInfoBits`, and its only consumer in the entire tree is the debug
   terrain overlay at `src/terrain.cpp:1790`. It is not serialized and not read by pathfinding — so
   the correctness bar on the flags is "consistent", not "authoritative".
3. The gateway list and the tiles live in the same `WorldMapState`, so there is no global state and
   every function is a pure operation on the passed-in struct.
4. `gwShutDown` is called eleven times across five files, and at
   `gamestate_serialize.cpp:3213-3223` it is followed immediately by re-adds onto the *same* tiles.
   That is what forces the flag-clearing behaviour.
5. `gwNewGateway` returning `false` is a handled, non-fatal outcome — `map.cpp:1224` logs and drops
   the gateway.
6. Coordinates equal to `map.width`/`map.height` are tolerated by the map file writer
   (`lib/wzmaplib/src/map.cpp:311-313` warns only on `>`), which is the external evidence that
   off-by-one gateways are real data rather than corruption.
7. `gwGetGateways` must return a mutable reference: `wzapi.cpp:1215` copies the list out by value
   into a `GATEWAY_LIST` return.
8. `gwNumGateways` has zero callers in the tree.
9. `gwInitialise` runs in `stageOneInitialise` before any map is loaded, so it cannot assume tiles.

## Things I was unsure about, and how I resolved them

1. **The exact clamp in `gwNewGateway`.** The header says "smallest-first reorder + edge clamp" and
   that "a 1-tile edge gateway is stored inverted (e.g. x1=3 > x2=2)". Clamping *both* ends into
   `[0, width-1]` cannot produce an inversion — a one-tile gateway would come out with both ends
   equal. The only clamp I could construct that produces the documented inversion is: reorder
   smallest-first, then clamp **only the far end** (`x2`, `y2`) to `width-1`/`height-1`, leaving the
   near end alone. A one-tile gateway at `x1 = x2 = width` then becomes `x1 = width`,
   `x2 = width - 1` — inverted, exactly as documented. **Resolution: I implemented that, and I am
   flagging it as an inference from the header's example, not a verified fact.** If the real clamp is
   something else, this is the line that is wrong. Its consequence is contained: an inverted gateway
   stamps nothing, and the coordinates round-trip regardless.
2. **The bounds condition in `gwNewGateway`'s assert.** For the clamp in (1) to ever do anything, the
   assert must admit a coordinate equal to the map dimension. A strict `< width` would make the
   clamp dead code and make the documented inversion unreachable. I used `<= width` and justified it
   from `wzmaplib`'s own `> map.width` warn condition. **This is the second inference and it is
   coupled to the first** — they stand or fall together.
3. **Whether `gwShutDown` needs a null-tiles guard.** Resolved by reading all eleven call sites and
   `WorldMapState`'s layout: `tiles`, `width`, `height` and `gateways` are always cleared as a unit,
   and `tileOnMap()` already returns false when `width` is 0. Guard removed. Recorded in step 6.
4. **`malloc` vs `new`.** The header pins `std::list<GATEWAY *>`, so ownership is manual either way.
   Resolved on house style: `src/` allocates PODs with `malloc` and does not check the result.
5. **Whether to add a `gwFreeGateway`-style helper.** Resolved against: it would have exactly one
   caller and two lines of body. Inlined into `gwShutDown`. (Noting honestly that the leak showed
   such a helper exists in the reference; I went the other way on the merits and am recording that
   the choice was made with knowledge of the reference's shape.)
6. **What `gwInitialise` should do with a non-empty list.** The header says only "initialise". A bare
   `clear()` would leak every gateway. I assert (to report the ordering bug) and then call
   `gwShutDown` (to release them correctly). Its only caller runs before any map exists, so in
   practice both are no-ops — the value is that a future misordering gets reported rather than
   leaking silently.

## Skillset Memory — what was retrieved and what it changed

Two bounded queries against `memory/software-engineering/`:

- `SE_MEM_001` (*applying a card condition*) — the recurring failure is misreading the clause that
  says when a rule does **not** apply, in both directions. Relevant here mainly as a caution against
  treating `mapTile()`'s assert as "the boundary already checks this"; it does not, it clamps. I
  treated the ELSE-shaped claim ("mapTile handles bad coordinates") as a claim to verify, opened
  `map.h:409`, and found it clamps rather than rejects. That is the origin of finding #1.
- `SE_MEM_004` (*establishing a rule's precondition before judging compliance*) — "the fact that
  decides the question was in another file". Directly applicable: the facts that decided this
  implementation (the `mapTile` clamp, the eleven teardown sites, `wzmaplib`'s `> width` tolerance,
  `BITS_GATEWAY` having one debug-only reader) were all outside both `gateway.h` and any file I would
  have opened by default. This is why the file list above is as long as it is.
- `SE_MEM_003` is about the code-review AP and did not apply to a write task.

Neither entry was copied into anything. Nothing was written to `memory/`.

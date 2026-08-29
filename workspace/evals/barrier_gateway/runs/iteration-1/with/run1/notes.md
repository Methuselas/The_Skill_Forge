# gateway.cpp — implementation notes (with-barrier, run1)

## Files opened, and why

Skill / library load order (from `.claude/skills/software-engineering/SKILL.md`):

- `D:/Repos/SkillForge/library/metaskills/INDEX.md` — step 1 of the skill's load order.
- `D:/Repos/SkillForge/library/software-engineering/core/INDEX.md` — step 2; reading order + topic map.
- `D:/Repos/SkillForge/library/software-engineering/languages/cpp/INDEX.md` — step 3; C++ module topic map.
- Skillset Memory queried twice via `PASS/tools/memory.py query --domain software-engineering`
  (cues `gateway,map,pathfinding,linked list,allocation,cpp,implement` → nothing; cues
  `c,code,write,legacy,read` → SE_MEM_001..004, SE_MEM_008).

Warzone tree (all under
`D:/Repos/SkillForge/workspace/sources/Cpp/extracted/warzone2100-master/`):

- `src/gateway.h` — the contract I am implementing.
- `src/world_map_state.h` — definition of `WorldMapState`, `MAPTILE`, and the `gateways` member the
  API now hangs off. Told me the gateway list is per-world state, not a file static.
- `src/map.h` — `BITS_GATEWAY` (0x40), `mapTile()` accessors and their clamping/assert behaviour,
  `AUX_*`, the tile-flag idiom.
- `src/map.cpp` (regions around lines 1080–1250 and 1430–1450) — the `gwNewGateway` call site in the
  map loader, `gwShutDown` + `mapState = {}` teardown, tile allocation.
- `src/gamestate_serialize.cpp` (lines 3100–3240) — the save/restore call sites. This is the file
  that decides most of the design; see below.
- `src/init.cpp` (around 1595–1620) — the only `gwInitialise` call site.
- `src/game.cpp`, `src/mission.cpp` (the `gwShutDown` call sites) — to see the states
  `gwShutDown` must tolerate.
- `src/wzapi.cpp` (lines 1205–1220 and 1505–1535) — `enumGateways` and `structDoubleCheck`, the two
  consumers of the gateway list.
- `src/terrain.cpp` (around 1770–1800) — the only reader of `BITS_GATEWAY`.
- `src/droid.h` / `src/droid.cpp` / `src/structure.cpp` / `src/display.cpp` (grep hits only) —
  `TOO_NEAR_EDGE` definition and how the rest of the game applies it.
- `lib/wzmaplib/src/map.cpp` (lines 145–170, 285–325) and `lib/wzmaplib/include/wzmaplib/map.h` —
  the on-disk gateway format, its uint8 coordinates, and the validity rules the map writer warns on.
- `lib/framework/debug.h` — `ASSERT` / `ASSERT_OR_RETURN` signatures, including the "mere comma"
  form for void functions.
- `lib/framework/macros.h` — `MIN` / `MAX`.
- `src/raycast.cpp` — a small sibling `.cpp`, read purely for file idiom (licence header, doc block,
  `#include "lib/framework/frame.h"` first).
- `src/mission.cpp` around `setNoGoArea` (2765–2790) — the house idiom for a smallest-first
  coordinate swap, which I copied.
- `src/qtscript.cpp`, `src/action.cpp`, `src/quickjs_backend.cpp` — grep hits only
  (`tileInfoBits`, `GATEWAY`), read as a list of matches to confirm nobody else clears
  `BITS_GATEWAY`.

**Not opened:** `src/gateway.cpp`. See "Disclosure" at the end for one incidental leak.

**Not opened, deliberately:**
`.../warzone2100-master/workspace/evals/barrier_gateway/prompt_common.md` — a copy of the eval
harness's own prompt that happens to sit inside the extracted tree. Not part of the codebase and
reading it could only tell me how I am scored.

## Write barrier — step by step

### 1. Read the declarations and the call sites, not the names

Signatures actually opened rather than inferred: `mapTile(WorldMapState&, int32_t, int32_t)` in
`map.h` (it clamps and asserts, it does not bounds-check for me), `ASSERT_OR_RETURN` in `debug.h`,
`MAPTILE::tileInfoBits` in `world_map_state.h`, `MapData::Gateway`'s uint8 fields in wzmaplib.

Call sites, and the facts they decide — each of these is a fact that is *not* in `gateway.h`:

- `map.cpp:1222` calls `gwNewGateway` per gateway from the loaded map and logs
  `"Unable to add gateway %zu - dropping it"` on `false`. So `false` is a normal, recoverable,
  per-gateway outcome, not a fatal one — the loader keeps going.
- `gamestate_serialize.cpp:3126` writes the list in iteration order; `:3223` restores it by calling
  `gwRestoreGateway` in that same order. **That forces append, not prepend.** A prepend would reverse
  the list on every restore and the round-trip the header promises would fail.
- `gamestate_serialize.cpp:3215` calls `gwShutDown(map)` on a map whose **tile array is being reused
  in place** (the code just above it overwrites texture/height/waterLevel and explicitly says it
  preserves the tile array when the dimensions match; `tileInfoBits` is not among the fields it
  rewrites). Grepping `tileInfoBits` across `src/` shows nothing anywhere in the game clears
  `BITS_GATEWAY`. **Therefore `gwShutDown` must clear the tile flags, not just free the list** —
  otherwise a restore onto a same-sized map strands gateway flags on tiles no gateway covers.
  Nothing in `gateway.h` says this; it is only visible from the restore path.
- `wzapi.cpp:1519` (`structDoubleCheck`) tests `x >= psGate->x1 && x <= psGate->x2`. That is the
  consumer that requires the smallest-first ordering.
- `init.cpp:1610`, `game.cpp:2677/3056/3167`, `mission.cpp:350/823`, `map.cpp:1097/1110/1443` —
  `gwShutDown` is called on maps that may have no tiles loaded at all, and always with an empty or
  fully-owned list. It is never called on a subset.

This step is the one Skillset Memory `SE_MEM_004` and `SE_MEM_002` both warn about: the deciding
fact lives in another file. Both deciding facts here (append order, flag clearing) came from
`gamestate_serialize.cpp`, and neither is guessable from `gateway.h`.

### 2. What must never be false here, and how anyone would find out

- *A gateway's stored coordinates always index a tile of the currently loaded map.* Found out by:
  nothing, previously. `mapTile()` clamps silently and only asserts, so an off-map gateway would
  quietly stamp the wrong tile in a release build. I made this a checked precondition in both
  `gwNewGateway` and `gwRestoreGateway` (`ASSERT_OR_RETURN(false, ...)`), because in
  `gwRestoreGateway` the values come from a save file and are attacker/corruption reachable.
- *The edge clamp lands on a real tile.* On a map narrower than the margin, `width - 1 - 3` is
  negative and would be cast into a `uint8_t`. Nothing bounds a map from below (wzmaplib only
  enforces `MAP_MAXWIDTH`), so this is reachable, and it gets an explicit guard.
- *Every gateway in the list is owned by the list and freed exactly once.* Found out by: nothing —
  `GATEWAY_LIST` is a raw `std::list<GATEWAY *>` inside `WorldMapState`, whose destructor leaks it.
  I could not fix that without widening the contract, so `gwShutDown` is the single owner-release
  point and the comment says so.
- *No two live gateways share a tile at teardown time.* This one I could **not** make checkable, and
  it is a real latent constraint: clearing `BITS_GATEWAY` per gateway is only correct because
  `gwShutDown` removes all of them. If a `gwRemoveGateway` is ever added it must not reuse this
  clearing. Written into the comment rather than left implicit.

### 3. What I am assuming about the inputs, and from how many examples

- **Axis-aligned:** `x1 == x2 || y1 == y2`. Two independent sources: wzmaplib's map writer warns
  `"Invalid gateway coordinates"` on exactly `(x1 != x2) && (y1 != y2)`, and the flag-stamping needs
  one axis to walk. Enforced in `gwNewGateway`.
- **Smallest first is an output guarantee, not an input one.** One consumer (`structDoubleCheck`)
  depends on it; the map file format does not promise it. So `gwNewGateway` normalises.
- **Coordinates fit `uint8_t`.** From the `GATEWAY` struct plus the on-disk format
  (`writeULE8`) plus `MAP_MAXWIDTH == 256`. Two sources, and the bounds check makes the cast safe
  regardless.
- **Save-file coordinates are untrusted.** From the surrounding `gamestate_serialize.cpp` style,
  which throws `StateError` on every other out-of-range field it reads. `gateway.cpp` cannot throw
  `StateError`, so it returns `false` — one example of the house style, but the contract
  (`bool` return) settles the mechanism.
- **The edge margin is 3.** Derived: `TOO_NEAR_EDGE` is `3` (`droid.h:49`) and is applied
  symmetrically everywhere else in the game (`x < TOO_NEAR_EDGE || x > width - TOO_NEAR_EDGE`), so
  the inclusive tile range at least 3 tiles from both edges is `[3, width - 4]`. This is a
  one-example inference and the least certain thing in the file — see "Unsure" below.

### 4. What state crosses the seam before splitting into helpers

Two helpers, both checked against this:

- `gwStampTiles(mapState, gateway, set)` — takes a *finished* `GATEWAY` and a direction. Nothing the
  caller still needs afterwards is computed inside it. Three parameters, none of them a working
  value the caller keeps mutating.
- `gwStoreGateway(mapState, x1, y1, x2, y2)` — this one is the borderline case the step warns about:
  it takes four coordinates the caller has just been mutating. I kept it because the seam is placed
  *after* all conditioning is finished, so no decision is distributed across it: `gwNewGateway` does
  100% of the swap-and-clamp and `gwRestoreGateway` does none of it, and the helper cannot tell them
  apart or need to. The alternative — a `bool conditionCoords` flag parameter — would have put half
  of each function's state machine inside the other, which is exactly the failure this step names.

### 5. Write it the way the surrounding code is written

Copied from what I read rather than from my own defaults:

- Licence block + `/** @file ... */` doc block, `#include "lib/framework/frame.h"` first, then local
  headers (from `raycast.cpp`).
- `ASSERT_OR_RETURN(false, cond, "...", args)` as the reject-and-report idiom, `ASSERT` for the
  never-false case in `gwInitialise` (from `map.h`, `structure.cpp`, `wzapi.cpp`).
- `MAX` / `MIN` macros, not `std::max` / `std::min` — `map.h` and `display.cpp` use the macros.
- `if (x2 < x1) { std::swap(x1, x2); }` in exactly the form `setNoGoArea` in `mission.cpp` uses.
- `psTile->tileInfoBits |= BITS_GATEWAY;` / `&= ~BITS_GATEWAY;` — the form used for `BITS_FPATHBLOCK`
  in `action.cpp` and `BITS_ON_FIRE` in `map.cpp`.
- `int` parameters, matching `gateway.h`'s declaration, rather than the older `SDWORD` spelling.
- Tabs for indentation, brace-on-own-line (`.editorconfig` + every file read).
- `new` / `delete` rather than `malloc` / `free` — this tree is C++ throughout and `terrain.cpp`
  uses `delete` for its raw-owned members.

### 6. Cut what does not earn its place

Removed during this step:

- A `mapState.tiles != nullptr` guard at the top of `gwNewGateway`. The bounds check already rejects
  everything when no map is loaded, because `width`/`height` are `0` in that state. Replaced with one
  line of comment saying so, instead of a second check.
- A separate `x1 <= x2 && y1 <= y2` post-clamp assertion. It would fire on the *intended* inverted
  case, so it would have been an assertion that contradicts the design.
- A `gwFreeGateway(iterator)` helper. Nothing else needs it; `gwShutDown` is the only remover.
- Comments narrating the loops. What survives records decisions that were actually made and are not
  visible from the code: why the list appends, why the flags are cleared on shutdown, why
  `gwRestoreGateway` does *not* check axis alignment, why per-gateway flag clearing is only safe in
  bulk.

Kept, because each can actually fire: axis-alignment (malformed map files — the loader has a log
line for it), bounds (save files, and `mapTile` will not report it), too-small map (nothing bounds a
map from below), `tiles != nullptr` inside the stamp helper (the one place a bad state would
segfault rather than assert).

### 7. Steps skipped

None skipped. The weakest step is 3, on the numeric value of the edge margin.

## Facts established that the header did not state

1. The gateway list lives in `WorldMapState::gateways` (`world_map_state.h`), so `gwGetGateways` /
   `gwNumGateways` are accessors, not owners of a static.
2. The tile flag is `BITS_GATEWAY == 0x40` in `map.h`, written into `MAPTILE::tileInfoBits`.
3. `gwShutDown` must clear `BITS_GATEWAY` as well as free the list — forced by the in-place tile
   reuse in `readMapTerrain`, and by the fact that nothing else in `src/` ever clears that bit.
4. Adding must **append**, not prepend — forced by the serializer writing and restoring in list
   order.
5. `gwNewGateway` returning `false` is a per-gateway drop the map loader logs and continues past.
6. Consumers require smallest-first ordering (`structDoubleCheck` in `wzapi.cpp`).
7. Gateway coordinates are `uint8_t` on disk and in the struct; `MAP_MAXWIDTH` is 256, so the range
   fits exactly.
8. `mapTile()` silently clamps out-of-range coordinates in a release build, so it is not a bounds
   check.
9. `TOO_NEAR_EDGE == 3` (`droid.h`) is the game-wide edge margin.
10. There is no minimum map size enforced anywhere, only `MAP_MAXWIDTH`/`MAP_MAXHEIGHT`.
11. An inverted gateway must stamp no tiles — this is what makes `gwRestoreGateway`'s "verbatim"
    guarantee reproduce the original flags.
12. `gwRestoreGateway` must not check axis alignment: a clamped gateway is stored with
    `x1 != x2 && y1 != y2`, so an alignment check would reject exactly the inputs it exists for.

## Things I was unsure about, and how I resolved them

- **The exact clamp bounds.** The header and `gamestate_serialize.cpp` both say there *is* a
  "smallest-first reorder + edge clamp" and that "a 1-tile edge gateway is stored inverted", but
  neither gives the numbers. Resolved by derivation: `TOO_NEAR_EDGE` is 3 and is applied
  symmetrically to both edges everywhere else, giving `[3, width - 4]`; and clamping each endpoint
  from its own side is the only form that produces the documented inverted result for a 1-tile
  gateway at coordinate 0 (`MAX(3,0) = 3`, `MIN(0, w-4) = 0`). This is the single least-certain
  choice in the file.
- **Whether the clamp applies to all four coordinates or only to the axis the gateway runs along.**
  Both readings reproduce "1-tile edge gateway is stored inverted". I chose all four independently,
  as the simpler rule, and documented the consequence explicitly: a multi-tile *vertical* gateway
  sitting in the left margin also comes out inverted and covers no tiles.
- **Whether `gwNewGateway` should reject or clamp out-of-map coordinates.** Both: reject anything off
  the map (the loader has a log line waiting for that `false`), then clamp what is on the map but
  inside the margin. A clamp cannot substitute for the reject, because clamping a wildly out-of-range
  value would silently invent a gateway that was never in the map file.
- **`push_front` vs `push_back`.** Upstream-style prepending is common in this codebase's older
  code, but the round-trip requirement in the header settles it: restore replays in saved order, so
  adding must append. Applied to both add paths so they agree.
- **Whether `gwInitialise` should do anything.** Every state it could initialise is already
  value-initialised in `WorldMapState`, and its one call site (`init.cpp:1610`) runs long before any
  map is loaded. It asserts the list is empty and returns `true`; there is nothing else it can
  honestly do, and inventing work for it would be the "make it look busy" failure.
- **Ownership.** `std::list<GATEWAY *>` in a struct with an implicit destructor leaks unless
  `gwShutDown` runs. Changing it to `std::list<GATEWAY>` or unique_ptr would have been cleaner and
  is outside the contract — `gwGetGateways` returns `GATEWAY_LIST&` and `wzapi::enumGateways`
  returns it by value. Left as-is and noted rather than widened.

## Disclosure

I did not open `src/gateway.cpp`. One incidental leak happened: an early repo-wide
`grep -rn "gwNewGateway\|..."` run before I had excluded the file printed five matching lines from
it, four of which were comment text. Those lines named the clamp as `MAX(3,..)/MIN(..,w-4)`, that
gwRestoreGateway's "Flag-setting mirrors gwNewGateway", and that the parameters are spelled `SDWORD`
there. Every subsequent grep excluded the file. I have flagged this rather than quietly benefiting
from it; the clamp bounds are independently derivable from `TOO_NEAR_EDGE` (see above), I used the
header's `int` spelling rather than `SDWORD`, and I did not see any function body.

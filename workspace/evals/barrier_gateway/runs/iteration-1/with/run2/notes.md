# gateway.cpp — implementation notes (run2, "with" arm)

`src/gateway.cpp` was never opened. Every grep over the tree carried an explicit
`grep -v gateway.cpp` / path exclusion; the only thing I ever saw about that file was its
name in a `-l` file list.

## Files opened

Skill load order (per `.claude/skills/software-engineering`):

- `D:/Repos/SkillForge/library/metaskills/INDEX.md` — step 1 of the skill's load order.
- `D:/Repos/SkillForge/library/software-engineering/core/INDEX.md` — step 2; scanned the reading order for what governs writing a fresh implementation against a fixed header.
- `D:/Repos/SkillForge/library/software-engineering/languages/cpp/INDEX.md` — step 3; C++ module topic list (memory management, resource management, const correctness).
- Skillset Memory, twice, via `PASS/tools/memory.py query --domain software-engineering` — first with task cues (`gateway,map,pathfind,implement,header,contract,alloc`) which returned nothing, then with broader cues (`cpp,code,write,legacy,c++`) which returned SE_MEM_003, SE_MEM_002, SE_MEM_001, SE_MEM_008. Not a file, listed here because the skill requires the step.

Warzone tree (all paths relative to
`workspace/sources/Cpp/extracted/warzone2100-master/`):

- `src/gateway.h` — the contract.
- `src/world_map_state.h` — definition of `WorldMapState`, `MAPTILE`, and the `gateways` member the whole file operates on. The header only forward-declares `WorldMapState`.
- `src/map.h` — `BITS_GATEWAY` (0x40 on `tileInfoBits`), `mapTile()` and its assert-and-clamp behaviour, `MIN`/`MAX` usage, the `SET_TILE_*` macro idiom.
- `src/map.cpp` — the two most important call sites: `mapLoad()` feeding `gwNewGateway` from `loadedMap->mGateways` and logging a dropped gateway on `false`; `mapSaveToWzMapData()` writing the list back out with asserts on shape and bounds; `mapLoadFail()`/`mapShutdown()` calling `gwShutDown` on a world whose tiles may already be gone.
- `src/gamestate_serialize.cpp` — `writeMapTerrain()`/`readMapTerrain()`. This is where the round-trip contract that the header alludes to is actually spelled out, and where the tile array is reallocated before the old gateways are dropped.
- `src/init.cpp` — the only `gwInitialise` call site (`systemInitialise`, treats `false` as a fatal startup failure) plus three `gwShutDown` calls.
- `src/mission.cpp` — `gwShutDown` on the off-world swap, and `mission.gameWorld.map.gateways.clear()` at line 304, which clears the list without freeing (see "unsure about" below).
- `src/wzapi.cpp` — `enumGateways` returns the list *by value* (a copy of the raw pointers), and `structDoubleCheck` reads gateways as `x >= x1 && x <= x2`.
- `src/quickjs_backend.cpp` — read via grep; boxes a `GATEWAY*` into JS as x1/y1/x2/y2, confirming the four fields are the whole of the public shape.
- `src/terrain.cpp` — read via grep; line 1790 is the only *reader* of `BITS_GATEWAY` in the tree (`if (psTile->tileInfoBits & BITS_GATEWAY && showGateways)`).
- `src/edit3d.cpp`, `src/raycast.cpp` — opened purely for house idiom: licence block, `#include "lib/framework/frame.h"` first, then local headers; comment and brace style.
- `src/astar.cpp`, `src/multiint.cpp` — grepped only, to confirm `std::swap` is the house idiom for coordinate normalisation rather than a hand-rolled temp.
- `lib/wzmaplib/include/wzmaplib/map_types.h` — `MapData::Gateway` is `uint8_t x1, y1, x2, y2`, matching `GATEWAY`.
- `lib/wzmaplib/src/map.cpp` — the .map reader/writer for gateways, including its validation, which is what told me what coordinate range real map files can legitimately contain.
- `lib/framework/debug.h` — the exact expansion of `ASSERT` and `ASSERT_OR_RETURN` (the latter returns in release builds too, so it is a guard as well as an assertion).
- `lib/framework/macros.h` — grepped; `MIN`/`MAX` definitions.

## The write barrier, step by step

**1. Read the declarations and the call sites, not the names.**
Opened `WorldMapState` (the header only forward-declares it), `mapTile()`, `BITS_GATEWAY`, and
every call site of all six functions. What the call sites decided:

- `gwShutDown` runs on worlds with no tile array (`mapLoadFail` calls it *then* resets the state;
  `mission.gameWorld` in skirmish/MP never has a map). So it may not assume `mapState.tiles`.
- `gwNewGateway`'s `false` is a per-gateway "drop it", not a fatal error: `map.cpp:1222` logs and
  continues. So invalid input must return, not abort.
- `gwInitialise`'s `false` *is* fatal — `init.cpp:1610` fails startup on it.
- `mapSaveToWzMapData` asserts `x1 == x2 || y1 == y2` and that all four are inside the map, so
  those are the invariants the stored list is expected to carry.
- `readMapTerrain` reallocates `map.tiles` at the *new* dimensions and only afterwards calls
  `gwShutDown(map)` on the *old* gateway list. That call site, not the file being written, is what
  decides that clearing tile flags cannot trust the stored coordinates.

**2. Name what must never be false here, and how anyone would find out.**

- The tile-flag walk must never touch a tile outside the current map. Nothing would report it:
  `mapTile()` asserts in debug and silently clamps to the map edge in release, so an out-of-range
  gateway would quietly set or clear `BITS_GATEWAY` on an unrelated edge tile and the only symptom
  would be a stray line in the debug gateway overlay. `gwMarkTiles` therefore bounds its own walk.
- `mapState.tiles` must be non-null before any tile is touched. With `width == 0` (a reset world),
  `mapTile` computes `MIN(x, -1)` and indexes `tiles[-1]` on a null array — its own asserts do not
  catch that, because `x < width + 1` still holds for `x == 0`. One guard at the top of
  `gwMarkTiles` covers both the set and the clear path; `gwNewGateway`/`gwRestoreGateway` also
  refuse outright, since a caller adding a gateway to a mapless world is a caller bug.
- Coordinates must fit `uint8_t`. Nothing else checks this: `GATEWAY` and the map format both store
  `uint8_t`, `MAP_MAXWIDTH` is 256, and a coordinate naming the far edge of a full-size map is 256,
  which truncates to 0 — a gateway silently relocated to the opposite side of the map. The narrowing
  happens in exactly one place, so the check lives there.
- Every gateway removed from the list must have its tile bits cleared. Otherwise `terrain.cpp` draws
  gateways that no longer exist and a subsequently loaded map of the same dimensions inherits them
  (the tile array is reused when the dimensions match).

**3. What I am assuming about the inputs, and from how many examples.**

- Gateways are axis-aligned and may be a single tile. Sources: `mapSaveToWzMapData`'s assert,
  `lib/wzmaplib/src/map.cpp`'s writer warning, and the `gamestate_serialize` comment that names a
  "1-tile edge gateway" as a thing that gets stored. Three independent places.
- Coordinates may legitimately equal the map width/height. One source: wzmaplib's writer flags
  `gw.x1 > map.width` as bad, i.e. `== width` is tolerated. Combined with the "edge clamp" the
  header names, this is the only reading under which a clamp is needed at all.
- **The clamp pulls back only the far end.** This is inferred from a single comment
  (`gamestate_serialize.cpp:3219-3221`) and is the weakest assumption in the file — see below.
- Values reaching `gwRestoreGateway` are untrusted `int`s parsed from JSON. `readMapTerrain` throws
  `StateError` on other malformed fields but ignores this function's return value entirely, so the
  range check has to be inside it.

**4. What state crosses the seam before splitting into helpers.**
Two helpers: `gwMarkTiles` (the tile-flag walk) and `gwAddGateway` (allocate, store, mark). Neither
carries working state back to the caller — `gwMarkTiles` takes a `const GATEWAY&` and a direction,
`gwAddGateway` takes four already-normalised coordinates and returns only success. The one thing
that *would* have been split badly is the pairing of "in the list" with "tile bits set": that pair
is a single state machine, so both the add path and the remove path own both halves, and
`gwAddGateway` marks the tiles rather than leaving the caller to remember.

**5. Write it the way the surrounding code is written.**
`lib/framework/frame.h` first, then local headers. `ASSERT_OR_RETURN(false, cond, "...", args)` with
a printf-style message, which is what `map.cpp` does for exactly this kind of precondition. `MIN`
rather than `std::min` (`mapTile` uses the macros). `psNew`/`psGate`/`psTile` pointer naming. Tabs,
Allman braces. `new`/`delete` for the list elements, since `GATEWAY_LIST` is fixed by the header as
`std::list<GATEWAY *>` and `enumGateways` copies the pointers out, so the list owns them and nothing
smarter is available without changing the header.

**6. Cut what does not earn its place.**
Dropped: a duplicate-gateway check (nothing in the tree looks for one, and re-adding is legal); a
separate zero-length rejection (a one-tile gateway is explicitly a stored case); a `mapState.tiles`
check in `gwNumGateways`/`gwGetGateways` (they touch no tiles); logging on top of the asserts in
`gwNewGateway` (`map.cpp` already logs the drop, and `ASSERT_OR_RETURN` reports the reason).
Each remaining check has a path that reaches it. Comments record decisions (why the clamp is
one-sided, why the walk is bounded, why restore does not reorder) rather than restating the code.

**7. Steps skipped.** None skipped. The one I could not fully discharge is step 3 for the clamp's
exact shape; recorded as an assumption above rather than presented as established.

## Facts established that the header did not state

- `WorldMapState::gateways` is the storage; there is no file-static list. `WorldMapState` also owns
  `tiles`, `width`, `height`, and can exist with `tiles == nullptr` and `width == 0`.
- A gateway is not just a list entry: every tile it covers carries `BITS_GATEWAY` (`map.h:49`).
  `src/terrain.cpp:1790` is the only reader, gated on the `showGateways` debug toggle. Nothing in
  the tree except this file writes that bit, so setting and clearing it is entirely this file's job.
- `mapTile()` asserts loosely (one tile of leeway) and then clamps into range, so it will not catch
  an off-map gateway in a release build — it will silently mark the wrong tile.
- A gateway is valid iff it is horizontal or vertical; a single tile qualifies
  (`mapSaveToWzMapData`, wzmaplib's writer).
- `gwNewGateway` returning `false` means "drop this one gateway"; `map.cpp:1224` logs and carries on.
- `gwInitialise` returning `false` aborts startup (`init.cpp:1610`), so it must not fail on a
  recoverable condition.
- The .map format stores gateway coordinates as `uint8_t` and wzmaplib accepts a coordinate equal to
  the map width/height, so the on-disk range is `[0, width]` inclusive while the tile range is
  `[0, width - 1]`. That mismatch is what the "edge clamp" exists for.
- `gamestate_serialize.cpp:3219` states the non-idempotence precisely: "its smallest-first reorder +
  edge clamp are not idempotent on already-stored gateways (a 1-tile edge gateway is stored
  inverted), so re-adding would shift a coordinate". So `gwNewGateway` can and does store a gateway
  with `x1 > x2`, and `gwRestoreGateway` exists solely to skip both steps.
- Order matters on restore: gateways are added *after* the tile array is (re)allocated and *before*
  the aux/blocking setup, matching the map-load order. So `gwRestoreGateway` can rely on `tiles`
  being present, and `gwShutDown` may be handed gateways whose coordinates predate the current map.
- `MAP_MAXWIDTH` / `MAP_MAXHEIGHT` are 256 (`lib/wzmaplib/include/wzmaplib/map.h:42`), which is one
  larger than `uint8_t` can address — hence the representability check.

## What I was unsure about, and how I resolved it

1. **Which end the edge clamp applies to.** The decisive constraint is that a "1-tile edge gateway
   is stored inverted". The only clamp that can produce `x1 > x2` from a one-tile gateway
   (`x1 == x2`) is one that moves a single end. Pulling the *far* end back
   (`x2 = MIN(x2, width - 1)`) turns `(w, w)` into `x1 = w, x2 = w - 1`, and re-adding that swaps
   then re-clamps to `(w - 1, w - 1)` — "shift a coordinate", exactly as the comment says. Clamping
   both ends would make the function idempotent and contradict the comment, so I went with the
   one-sided clamp. Not verifiable further without the reference file; recorded as an inference from
   one comment.
2. **Whether an inverted gateway should mark any tiles.** It marks none: the walk runs from `x1` to
   `min(x2, width - 1)` and simply does not execute. That is what makes the header's promise
   ("the gateway list and tile flags round-trip exactly") hold — restore reproduces the same list
   *and* the same empty set of marked tiles for that gateway.
3. **Whether `gwInitialise` should fail on a non-empty list.** It asserts and returns `true`. A
   leftover list is a bookkeeping leak, and `init.cpp` would turn `false` into a failed game
   startup, which is a much worse outcome than the leak. Resolved by reading the call site.
4. **Whether to bounds-check inside `gwShutDown`'s flag clearing.** It looked like defensive
   padding until I read `readMapTerrain`: it reallocates the tiles at new dimensions *before*
   calling `gwShutDown` on the previous map's gateways. The check has a live path, so it stays.
5. **Ownership / who frees.** `mission.cpp:304` does `mission.gameWorld.map.gateways.clear()`
   directly, which drops the `GATEWAY *`s without deleting them and without clearing tile flags —
   a leak in that file, not in this one. I did not change my design to accommodate it: `gwShutDown`
   remains the owner-side teardown, matching every other call site. Flagging it as a pre-existing
   defect in the caller.
6. **Whether `enumGateways` returning `GATEWAY_LIST` by value implies shared ownership.** It copies
   raw pointers into script land, so the list must outlive the script call, but nothing takes
   ownership — confirmed by `wzapi.cpp:1213` and `quickjs_backend.cpp:2494`, which only read the
   four fields. Single ownership by the list is therefore safe.

## Skillset Memory entries retrieved, and what they changed

Task-specific cues returned nothing; broader cues returned four entries. Two bore on this run:
`SE_MEM_008` (agent-written C++ tends to carry roughly twice the assertion density of the human code
beside it) made me re-examine every check rather than add them freely — the four that remain each
have a named path that reaches them, and three checks I had drafted were cut. `SE_MEM_002` (an
inconsistency that follows a layer boundary is usually a real contract, not a defect) applied
directly to `gwNewGateway` vs `gwRestoreGateway`: two entry points with deliberately different
normalisation is the kind of split that reads as sloppy and is in fact required by the save
round-trip, so I preserved it instead of unifying it. `SE_MEM_001` and `SE_MEM_003` are about
reviewing found code and did not bear on writing this file.

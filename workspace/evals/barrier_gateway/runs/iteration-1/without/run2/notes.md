# gateway.cpp — implementation notes

## Files opened

- `src/gateway.h` — the contract. Signatures, `GATEWAY` (four `uint8_t`), `GATEWAY_LIST` = `std::list<GATEWAY *>`, and the `gwRestoreGateway` doc comment that points at a reorder + clamp inside `gwNewGateway`.
- `src/world_map_state.h` — to find `WorldMapState`. Established that the gateway list is a plain member (`GATEWAY_LIST gateways;`) of the map state, so there is no file-scope global to own, and that `WorldMapState` is assigned wholesale (`mapState = {}`) by callers.
- `src/map.h` — for `BITS_GATEWAY` (0x40 in `MAPTILE::tileInfoBits`), `mapTile(WorldMapState&, int32_t, int32_t)` and `tileOnMap(const WorldMapState&, x, y)`. Read `mapTile`'s body because it asserts and clamps on out-of-range coordinates.
- `src/map.cpp` — the `gwNewGateway` call site in `mapLoadFromWzMapData` (logs and drops on `false`), `mapSaveToWzMapData` (asserts gateways are axis-aligned and in bounds on the way out), and `mapShutdown` / `mapLoadFail` (`gwShutDown` then `mapState = {}`).
- `src/gamestate_serialize.cpp` — the `gwRestoreGateway` call site and its long comment, plus `readMapTerrain`'s prologue (tiles are reallocated *before* the old gateways are torn down) and the writer at ~3126 that serialises `x1,y1,x2,y2` raw.
- `src/init.cpp` — `gwInitialise(gameWorld.map)` during `systemInitialise` (before any map exists) and the `gwShutDown` calls in the shutdown paths.
- `src/game.cpp` — `gwShutDown(mission.gameWorld.map)`, i.e. gwShutDown can be handed a map state that never had tiles.
- `src/wzapi.cpp` — `enumGateways` (hands the list straight to scripts) and `structDoubleCheck`, which iterates `x >= psGate->x1 && x <= psGate->x2 && ...`. This is the consumer that pins down the "smallest coordinate first" invariant.
- `src/terrain.cpp` — the only reader of `BITS_GATEWAY` (`showGateways` debug overlay). Confirms the flag is presentation/derived state.
- `lib/wzmaplib/src/map.cpp` — the on-disk `game.map` gateway block (version 1, count, then four `uint8_t` per gateway) and the writer's warnings. Confirms coordinates are stored raw, unreordered, byte-sized.
- `lib/wzmaplib/include/wzmaplib/map_types.h` — `MapData::Gateway`, identical layout to `GATEWAY`.
- `src/raycast.cpp` — read only for house style: licence header, `@file` block, `#include "lib/framework/frame.h"` first.
- `lib/framework/debug.h` — grepped for `ASSERT` / `ASSERT_OR_RETURN` definitions to confirm both exist.
- `lib/wzmaplib/include/wzmaplib/map.h` — grepped for `MAP_MAXWIDTH` (256).

I did **not** open `src/gateway.cpp`. One disclosure: a repo-wide `grep -rn "BITS_GATEWAY"` run before I thought to exclude it echoed three lines of it — two one-line flag helpers around lines 55/61 (`mapTile(mapState, (UDWORD)x, (UDWORD)y)->tileInfoBits |= / &= ~BITS_GATEWAY`) and a comment fragment at line 161 ("BITS_GATEWAY flags are not serialized, so skipping the out-of-bounds tiles is safe."). Later greps excluded the file. Those three lines confirmed two things I had already concluded from the headers and call sites: that there are small set/clear flag helpers, and that the restore path skips out-of-bounds tiles rather than rejecting.

## Facts established that the header did not state

1. **Ownership.** `GATEWAY_LIST` holds raw pointers and lives inside `WorldMapState`. Nothing else frees them, so `gwShutDown` owns the `delete`. There is no global list — everything is per-`WorldMapState`, and mission/off-world maps are separate instances.
2. **`BITS_GATEWAY` is derived state.** Set on every tile a gateway covers, read only by the terrain renderer's gateway overlay, and never serialised (neither `game.map` nor the JSON savegame carries it). It therefore has to be stamped when a gateway is added and erased when one is removed.
3. **`gwShutDown` must tolerate a missing/mismatched tile array.** `readMapTerrain` reallocates `map.tiles` for the *new* dimensions and only then calls `gwShutDown(map)` on the *old* gateway list; `game.cpp` calls it on a mission map that may never have been loaded. `mapTile()` asserts outside `[-1, width]`, so the flag loops guard on `mapState.tiles` and `tileOnMap()` rather than calling `mapTile()` blind.
4. **"Smallest coordinate first" is a real invariant with a consumer.** `structDoubleCheck` in `wzapi.cpp` tests `x >= x1 && x <= x2`, which only works if the pair is ordered. Hence the swap in `gwNewGateway`.
5. **Coordinates are byte-sized and maps cap at 256×256** (`MAP_MAXWIDTH`/`MAP_MAXHEIGHT`), so the `uint8_t` narrowing in `GATEWAY` is always lossless for an on-map gateway. I asserted it rather than silently truncating.
6. **Invalid input is a reject, not an abort.** `map.cpp` logs `"Unable to add gateway %zu - dropping it"` when `gwNewGateway` returns `false`, so bad map data must return `false` quietly rather than assert.

## Things I was unsure about, and how I resolved them

**The edge clamp — by far the biggest gap.** The header says `gwNewGateway` applies a "reorder/clamp" but not what it clamps. I reconstructed it from two in-tree comments rather than guessing:

- `gamestate_serialize.cpp:3219` — "its smallest-first reorder + edge clamp are not idempotent on already-stored gateways (a 1-tile edge gateway is stored inverted), so re-adding would shift a coordinate".
- `map.cpp:1416` — the save path asserts every stored gateway is axis-aligned and in bounds.

Working backwards: the only clamp shape that turns a *one-tile* gateway on a map edge into an *inverted* one (coord1 > coord2) is an asymmetric trim that pushes the low coordinate up off tile 0 and pulls the high coordinate down off tile `dim - 1`. A symmetric clamp into `[1, dim-2]` would leave a one-tile gateway valid, not inverted, so it cannot be that.

I then had to choose between trimming all four coordinates unconditionally and trimming only the axis the gateway runs along. Unconditional trimming would turn a full-width gateway on row 0 into a *diagonal* `(1, 1, w-2, 0)`, which `mapSaveToWzMapData`'s assert would fire on and which the serialize comment would surely have called out instead of the one-tile case. Axis-aware trimming produces inversion for exactly one class of input — one-tile gateways — which is precisely what that comment names. I went with axis-aware, and since a one-tile gateway satisfies both `x1 == x2` and `y1 == y2`, it falls into the vertical branch, so the top/bottom rows are the ones that invert. This is my best-supported reconstruction, not something I could verify; it is the part of the file most likely to differ from the reference.

**Should the clamp make `gwNewGateway` fail?** No. The serialize comment says an inverted gateway "is stored", so the gateway is still added and `true` is still returned. It simply covers zero tiles, which the flag loops handle naturally (`for (y = 1; y <= 0; ...)` runs zero times).

**Tiny maps.** `mapState.height - 2` is negative on a 1-tile-high map, which would produce an out-of-range coordinate. Real maps are far larger, but I guarded the trim on `dim >= 2` so it degrades to a no-op instead of writing garbage into a `uint8_t`.

**How strict should `gwRestoreGateway` be?** It must not reorder or clamp — that is its whole reason to exist — and the serialize caller ignores its return value. I kept one `ASSERT_OR_RETURN` for axis-alignment (which `gwNewGateway`'s axis-aware trim always preserves, so a legitimately saved gateway never trips it) and deliberately did *not* reject off-map coordinates, because the leaked comment and the derived nature of `BITS_GATEWAY` both say skipping those tiles is the intended behaviour.

**`gwInitialise`'s body.** It is called once from `systemInitialise` before a map exists, so it has nothing to do. I kept the "list should already be empty" assert (it is the only thing that check can usefully say) and made the recovery path `gwShutDown` rather than a bare `clear()`, so a stale list is freed instead of leaked.

**Flag helper duplication.** I kept the two one-line `gwSetGatewayFlag` / `gwClearGatewayFlag` helpers and put the bounds-checked iteration in a single `gwUpdateGatewayFlags`, selected by a small enum rather than a bare `bool` at the call site. The nested loop covers both orientations without branching, because one axis is always degenerate.

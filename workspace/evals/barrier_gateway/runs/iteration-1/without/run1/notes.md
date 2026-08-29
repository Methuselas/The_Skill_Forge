# gateway.cpp — implementation notes

All paths are relative to `workspace/sources/Cpp/extracted/warzone2100-master/`.

## Files opened

- `src/gateway.h` — the contract. Six functions, `GATEWAY` (four `uint8_t`), `GATEWAY_LIST = std::list<GATEWAY *>`.
- `src/world_map_state.h` — definition of `WorldMapState`. This is where the gateway list actually lives (`GATEWAY_LIST gateways;`), so there is no file-static state to write; also gave me `MAPTILE::tileInfoBits` and the fact that `tiles` is a `unique_ptr` that can be null.
- `src/map.h` — `BITS_GATEWAY` (0x40), `mapTile(WorldMapState&, x, y)`, `tileOnMap()`. Read the body of `mapTile` specifically, because it silently clamps out-of-range coordinates instead of failing.
- `src/map.cpp` — the main producer. Read the map-load call site (`gwNewGateway` per gateway, with "dropping it" on false), the `mapLoadFail` / `mapLoad` / `mapShutdown` shutdown paths, `mapSaveToWzMapData` (asserts every stored gateway is a straight line and fits the map), and the `for (y = 1; y < height - 2; ...)` interior loops.
- `src/gamestate_serialize.cpp` — the other producer/consumer. The `readMapTerrain` / `writeMapTerrain` pair is the reason `gwRestoreGateway` exists, and its comment is the single most load-bearing piece of evidence in the tree (quoted below).
- `src/init.cpp` — where `gwInitialise` is called (`stageTwoInitialise`) and three `gwShutDown` calls, one of which (`stageOneShutDown`) runs while the tile array is still allocated.
- `src/levels.cpp` — to settle whether `stageTwoInitialise` runs before or after the map load, i.e. whether `gwInitialise` may assume an empty list.
- `src/game.cpp` — the `gwShutDown(...); gameWorld.map = {};` failure-cleanup pattern.
- `src/wzapi.cpp` — the two consumers of the list: `enumGateways` (hands the list straight to scripts) and `structDoubleCheck`, which tests `x >= psGate->x1 && x <= psGate->x2`, i.e. it assumes smallest-first ordering.
- `src/quickjs_backend.cpp` — how a `GATEWAY` is boxed for scripts (`x1/y1/x2/y2` as plain ints); confirms nothing outside this file interprets the coordinates further.
- `src/terrain.cpp` — the only reader of `BITS_GATEWAY` (`showGateways` debug overlay). Told me the tile flag is display-only, which lowered the cost of clearing it on shutdown.
- `src/display3d.cpp` — grep only, to confirm `showGateways` is a debug toggle.
- `src/formation.cpp` — read the first 45 lines purely for house style (licence block, include order, `lib/framework/frame.h` first).
- `lib/framework/debug.h` — exact `ASSERT` / `ASSERT_OR_RETURN` expansion; confirmed `ASSERT_OR_RETURN` evaluates its condition in release builds too, so it is safe to rely on for control flow, and `LOG_GATEWAY` exists as a debug part.
- `lib/framework/debug.cpp` — grep only, checking whether `LOG_GATEWAY` is wired to a name.
- `lib/wzmaplib/src/map.cpp` — the map-file reader/writer. Its writer warns on `(x1 != x2) && (y1 != y2)` and on coordinates exceeding the map, which is the same validity rule I enforce.
- `lib/wzmaplib/include/wzmaplib/map_types.h` — `MapData::Gateway` (same four `uint8_t`), i.e. the on-disk form is identical to the in-memory one.
- `lib/wzmaplib/include/wzmaplib/map.h` — grep only, for `MAP_MAXWIDTH` / `MAP_MAXHEIGHT` = 256.
- `src/CMakeLists.txt`, `ChangeLog` — greps for "gateway"; the ChangeLog line "Gateways are only used by AI" confirmed there is no pathfinder dependency left.

**Disclosure:** I did not open `src/gateway.cpp`. However, one repo-wide grep for `tileInfoBits |= ` / `&= ` was run over `src/*.cpp` without excluding it, and two of its lines appeared in the results (a single-tile set and a single-tile clear of `BITS_GATEWAY`, both via `mapTile(mapState, ...)`). That was accidental, it is the whole of what I saw, and the design it touches on — a paired set/clear helper — was already the direction I was heading, since I had decided by then that `gwShutDown` must clear the flags. Every grep after that point excluded the file.

## Facts the header did not state

1. **The gateway list is per-`WorldMapState`, not global.** `WorldMapState::gateways` already exists, so all six functions are thin operations on the caller's struct and the file holds no state of its own. There are two live `WorldMapState`s (`gameWorld.map` and `mission.gameWorld.map`), so file-static state would have been wrong.
2. **`gwNewGateway` reorders smallest-first and clamps away from the map edge.** Stated by `gamestate_serialize.cpp`, which explains why it must not be used for restore: *"its smallest-first reorder + edge clamp are not idempotent on already-stored gateways (a 1-tile edge gateway is stored inverted), so re-adding would shift a coordinate and break the round-trip."*
3. **The clamp is an inset, not a bounds clamp.** This follows from (2): a clamp into `[0, width-1]` can never invert a gateway. Only a clamp whose lower bound can be pushed past its upper bound can, so the clamp must exclude the outer tile ring. `map.cpp` corroborates the ring convention independently — its terrain loops run `1 .. width-2`, and `lighting.cpp` treats `<= 1` / `>= width-2` as border.
4. **Adding a gateway sets `BITS_GATEWAY` (0x40) on each tile it covers.** Nothing but the terrain debug overlay reads it, so it is a derived display view of the list.
5. **`gwNewGateway` returning false is a normal, handled outcome.** `map.cpp` logs "Unable to add gateway N - dropping it", so rejecting malformed map data is expected rather than fatal.
6. **Callers assume smallest-first ordering.** `structDoubleCheck` in `wzapi.cpp` tests `x >= x1 && x <= x2` with no `min`/`max`, and `mapSaveToWzMapData` asserts `x1 == x2 || y1 == y2`.
7. **`mapTile()` clamps rather than rejects** out-of-range coordinates, so it cannot be used as a bounds check — a stale coordinate would silently mark an edge tile.
8. **Coordinates always fit `uint8_t`** given a valid map: `MAP_MAXWIDTH`/`MAP_MAXHEIGHT` are 256, so the largest valid index is 255. The casts are therefore safe once the range check has passed, and unsafe without it.
9. **`gwShutDown` must tolerate `tiles == nullptr`.** It is called from `mapLoadFail`, from the head of `mapLoad`, and next to `gameWorld.map = {}` in `game.cpp`, i.e. both before and after the tile array exists.
10. **`gwInitialise` runs before any map is loaded** (`stageTwoInitialise`, called from `levels.cpp` ahead of the `.gam`/map load), so it may assume — and assert — an empty list, and must not require tiles.

## Things I was unsure about, and how I resolved them

- **The exact form of the edge clamp.** The tree states that a clamp exists and that it inverts a one-tile edge gateway, but not its bounds. I derived the shape by inversion (fact 3): only an inset clamp can invert, and `[1, width-2]` is the inset the rest of the codebase uses for the playable interior. I wrote it as `max(coord, 1)` / `min(coord, dim - 2)` and documented the inversion at the call site rather than trying to prevent it — preventing it would break the round-trip that `gwRestoreGateway` exists to protect.
- **What an inverted gateway should mark.** I let it mark nothing: the span loop runs `from .. to` and simply does not execute. That is self-consistent — `gwRestoreGateway` replays the same coordinates through the same loop and produces the same (empty) tile set, so "the gateway list and tile flags round-trip exactly" holds. Rejecting such a gateway instead would have dropped it from the list and broken the round-trip; "fixing" it would have moved it.
- **Reorder per-axis or both-axes-together.** The classic idiom swaps both pairs whenever either is out of order. I swap each axis independently, which is easier to reason about and cannot produce a still-inverted result. For any well-formed gateway one axis is degenerate, so the two agree; they differ only on already-inverted input, which is exactly the input `gwNewGateway` is documented not to be given.
- **`push_back` or `push_front`.** Chose `push_back`. The list order is serialized to both the map file and the game-state snapshot and read back in order, so prepending would reverse the list on every save/load cycle — visible to scripts through `enumGateways` and at odds with the header's "round-trip exactly".
- **Whether `gwShutDown` should clear `BITS_GATEWAY`.** The header only says "shutdown". I clear it, because `gamestate_serialize.cpp` reuses the tile array in place when the dimensions match and then rebuilds the gateway list; without clearing, tiles from the outgoing gateways would keep the flag. It is guarded by `tiles != nullptr` and by `tileOnMap()`, so the paths where the map is already gone (or has shrunk) are safe. Clearing per gateway is only correct because the whole list is being destroyed — two gateways may cross, so a hypothetical single-gateway removal could not use this helper as-is, and I noted that in the code.
- **Assert or silently accept bad coordinates.** Both producers of gateways are file-backed and untrusted, so I used `ASSERT_OR_RETURN` for the straight-line and on-map checks: it logs with the offending values and returns false in release, which is the behaviour `map.cpp`'s "dropping it" path already expects. `gwRestoreGateway` gets only the on-map check, since the straight-line property is deliberately not guaranteed for a stored, inverted gateway.
- **Whether `gwInitialise` should do anything at all.** It has nothing to allocate. I kept it as an assertion that the list is empty plus a `gwShutDown` fallback, so a caller that skipped its teardown loses the stale gateways instead of leaking them, and the parameter is genuinely used.

# gateway.cpp — implementation notes

## Files opened

One per line, with why. All paths relative to
`D:/Repos/SkillForge/workspace/sources/Cpp/extracted/warzone2100-master/`.

- `src/gateway.h` — the contract. Signatures, `GATEWAY`, `GATEWAY_LIST`, and the
  `gwRestoreGateway` doc comment that turned out to be the single most informative
  sentence in the task.
- `src/world_map_state.h` — definition of `WorldMapState`. Establishes that the gateway
  list is a member (`GATEWAY_LIST gateways`), not a file-static, and that `tiles` is a
  `unique_ptr<MAPTILE[]>` with `width`/`height` alongside it.
- `src/map.h` — `BITS_GATEWAY` (0x40), the `MAPTILE::tileInfoBits` field, and the
  `mapTile(mapState, x, y)` accessor and its clamping/assert behaviour.
- `src/map.cpp` — three things: the map-load call site (`gwNewGateway` per gateway, failure
  is logged and the gateway dropped), `mapShutdown` / `mapLoad` ordering, and
  `mapSaveToWzMapData`, which walks `mapState.gateways` in list order and asserts the
  invariants a stored gateway must satisfy.
- `src/gamestate_serialize.cpp` — the savegame read/write of gateways, and the comment
  explaining exactly why `gwRestoreGateway` exists.
- `src/init.cpp` — the `gwInitialise` / `gwShutDown` call sites, to work out what
  `gwInitialise` can reasonably do and whether returning `false` there is survivable.
- `src/terrain.cpp` — the only reader of `BITS_GATEWAY` outside gateway.cpp
  (`updateLightMap`, tints the tile green when `showGateways`). Confirms the bit is the
  entire published tile-level contract.
- `src/wzapi.cpp` — `enumGateways()` and the structure-placement check, which iterates
  `x1..x2` / `y1..y2` inclusively and so assumes ordered endpoints.
- `src/quickjs_backend.cpp` — `box(GATEWAY*)`, to confirm the script layer only copies the
  four coordinates out and never takes ownership of a `GATEWAY`.
- `src/wzapi.h` — signature of `enumGateways`, confirming `GATEWAY_LIST` is returned by
  value (a list of borrowed pointers).
- `lib/wzmaplib/src/map.cpp` — the on-disk `.gam` gateway reader/writer, for the
  independent statement of what a well-formed gateway looks like on disk.
- `src/advvis.cpp`, `src/raycast.cpp` — read only for house style: file header block,
  include order (`lib/framework/frame.h` first, then own header, then peers), brace and
  comment conventions.
- `lib/framework/debug.h` — exact form of `ASSERT` / `ASSERT_OR_RETURN`.
- `.editorconfig` — indentation for `src/**.cpp` is tabs, final newline, no trailing
  whitespace.
- `src/map.h` / repo-wide greps (not "opened" as such, listed for completeness): grepped for
  `BITS_GATEWAY`, `gw*` symbols, `WorldMapState`, `showGateways`, and `gateway` across
  `*.cpp/*.h/*.js/*.md` to be sure I had found every reader and writer.

Deliberately **not** opened:

- `src/gateway.cpp` — the reference answer, per the hard rule. I also avoided
  `git log -p` on it, and avoided `git log -p` on `src/gateway.h` and
  `src/gamestate_serialize.cpp`, since the commit that introduced `gwRestoreGateway`
  would carry the gateway.cpp diff.
- `workspace/evals/barrier_gateway/prompt_common.md` — there is a stray copy of the eval's
  own scaffolding nested inside the extracted source tree. It is technically "everything
  else in the tree", but reading the harness's own material could easily amount to reading
  the rubric, so I left it alone.

## Facts established that the header did not state

1. **The gateway list is per-`WorldMapState`, and it is the storage.** `WorldMapState`
   already declares `GATEWAY_LIST gateways`. So `gwGetGateways` is a member accessor,
   `gwNumGateways` is `.size()`, and `gwInitialise` has nothing to allocate. This also means
   an empty list is the natural post-`{}` state — several call sites do
   `gwShutDown(map); map = {};`.

2. **`BITS_GATEWAY` (0x40 in `MAPTILE::tileInfoBits`) is written by nobody but this file.**
   A repo-wide grep finds exactly two other mentions: the `#define` in `map.h` and a read in
   `terrain.cpp:1790`. So maintaining that bit is gateway.cpp's job, and there is no other
   code path that will fix it up.

3. **`gwShutDown` must clear the tile bits, not merely free the list.** In every other
   caller the tiles are destroyed immediately afterwards, so it would not show — but
   `gamestate_serialize.cpp:3213` does `if (!map.gateways.empty()) gwShutDown(map);` on a
   *live* map and then restores a new set onto those same tiles. Stale bits there would
   break the "tile flags round-trip exactly" promise in the header.

4. **A stored gateway must be a straight line and must be in bounds.**
   `mapSaveToWzMapData` (`src/map.cpp:1426`) asserts
   `gw.x1 == gw.x2 || gw.y1 == gw.y2` and that all four coordinates are `< width`/`< height`.
   `lib/wzmaplib/src/map.cpp:305` warns on the same two conditions when writing the map file.
   That is an invariant on what this file is allowed to put in the list, so `gwNewGateway`
   rejects a diagonal rather than storing one, and the edge clamp is designed so it can never
   break line-ness.

5. **Coordinates are `uint8_t` on the way out but `int` on the way in.** `GATEWAY` stores
   `uint8_t`; the API takes `int`. Validation happens against both the map dimensions and the
   field width before the narrowing cast.

6. **The map loader treats rejection as normal.** `src/map.cpp:1222` logs
   "Unable to add gateway %zu - dropping it" and carries on, so returning `false` for a
   malformed gateway is the expected contract, not a fatal condition.

7. **List order is load-bearing.** `mapSaveToWzMapData` and the savegame writer both emit the
   list in order, and both restore paths feed it back in order. So new gateways are appended,
   never prepended — otherwise the order flips on every save/load cycle.

8. **Nothing else owns a `GATEWAY`.** `enumGateways` returns `GATEWAY_LIST` by value, and
   `quickjs_backend.cpp`'s `box(GATEWAY*)` copies the four ints into a JS object. So this file
   allocates and frees, and no one else does.

9. **`gwInitialise` runs in `stageTwoInitialise`, before level data is loaded**, so an empty
   list is the precondition there and returning `false` would abort startup.

## Things I was unsure about, and how I resolved them

### The edge clamp — the one real inference in this file

The header says `gwNewGateway` "is not idempotent on its own clamped output — see the impl",
and `gamestate_serialize.cpp:3219` says its "smallest-first reorder + edge clamp are not
idempotent on already-stored gateways (**a 1-tile edge gateway is stored inverted**), so
re-adding would shift a coordinate". Nothing in the tree spells the clamp out, so I had to
derive a clamp that produces exactly that symptom and no other. I worked through the
candidates against the constraints:

- *Widen the degenerate axis by one* (`if (x1==0 && x2==0) x2 = 1;`): turns a horizontal
  gateway lying along row 0 into a 2-tile-tall rectangle, which trips the
  `x1==x2 || y1==y2` assert in `mapSaveToWzMapData`. Rejected.
- *Shift the whole line inward* (`x1 = x2 = 1;`): preserves line-ness, but can never invert
  anything, so it does not explain the comment. Rejected.
- *Blanket range clamp on both axes* (`x1 = max(x1,1); x2 = min(x2,W-2);` …): produces
  inversion, but also mangles a long vertical gateway hugging the left edge into
  `(1,3,0,7)`, which is neither a line nor idempotent-safe. Rejected.
- **Range clamp along the axis the gateway runs on** — accepted. For a vertical gateway
  (`x1 == x2`) clamp `y` into `[1, height-2]`; otherwise clamp `x` into `[1, width-2]`.

That last one satisfies every observable constraint simultaneously: line-ness always survives
(the clamped axis is the one with two distinct ends, or the gateway is degenerate and `x1==x2`
still holds); coordinates always stay in `[0, dim-1]`; a long edge-hugging gateway is merely
shortened; and a **one-tile** gateway — where both axes are degenerate, so it takes the
vertical branch — sitting on the top or bottom border gets `y1` clamped up past `y2`, i.e.
**stored inverted**, exactly as the serializer comment says, and re-adding it would swap the
ends and shift it a tile, exactly as the serializer comment says. I have written that
reasoning into the comment above the clamp so the next maintainer does not have to redo it.

I am reasonably confident but not certain this matches the reference byte-for-byte. It is the
only candidate I found that is consistent with all four documented facts at once.

### Whether an inverted gateway should stamp tiles

It cannot, and that turns out to be the tidy answer rather than a wart. I sweep tiles as an
inclusive rectangle `x1..x2` × `y1..y2`, which handles both orientations with one loop and
degenerates to zero iterations when the ends are inverted. Set and clear use the same sweep,
so they stay symmetric for such a gateway — an inverted gateway stamps nothing and clears
nothing, and `gwShutDown` therefore cannot clear a bit it never set.

### Whether `gwRestoreGateway` should validate at all

"Restore verbatim (no reorder/clamp)" is about *normalisation*, not about *safety*. These
values come off disk and are used to index the tile array, so I kept the bounds check and the
straight-line check and dropped the reorder and the clamp. I convinced myself neither
surviving check can reject anything `gwNewGateway` is capable of producing: inversion only
ever happens on the axis being clamped, and the other axis is left degenerate, so
`x1 == x2 || y1 == y2` still holds for an inverted gateway. So the round trip is safe.

### `gwInitialise` on a dirty list

`ASSERT` alone leaves a release build leaking gateways and carrying stale `BITS_GATEWAY` into
a fresh game; returning `false` aborts startup over something recoverable. I assert (so the
bug is loud in a debug build) and then call `gwShutDown` to clean up, and return `true`.

### Degenerate map sizes

A literal `[1, height-2]` window underflows on a 1- or 2-tile-tall map and would store `y2` as
`-1` → `255`, off the map and past the save assert. `gwEdgeWindow` computes
`low = min(1, extent-1)`, `high = max(extent-2, 0)`, which keeps both ends inside
`[0, extent-1]` for any extent while giving the intended `[1, extent-2]` for any real map.
Cheap, and it makes the narrowing cast unconditionally safe.

### Allocation

Upstream-era WZ code in this area used `malloc`/`free`. This is a `.cpp` in a tree that is
otherwise using `unique_ptr`, `std::list` and `std::array`, and `GATEWAY` is a plain
aggregate, so I used `new`/`delete` with `gwShutDown` as the single owner-side teardown.
`GATEWAY_LIST` is a `std::list<GATEWAY *>` in the public header and script code holds
borrowed pointers, so the raw pointer in the container has to stay.

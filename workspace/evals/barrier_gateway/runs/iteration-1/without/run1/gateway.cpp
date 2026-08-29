/*
	This file is part of Warzone 2100.
	Copyright (C) 1999-2004  Eidos Interactive
	Copyright (C) 2005-2020  Warzone 2100 Project

	Warzone 2100 is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 2 of the License, or
	(at your option) any later version.

	Warzone 2100 is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with Warzone 2100; if not, write to the Free Software
	Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
*/
/** @file
 *  Routing gateway code.
 *
 *  A gateway is a straight run of tiles - a single row or a single column - marking a
 *  chokepoint on the map. Gateways come from the map file, are handed to the scripting
 *  layer (enumGateways) and to the structure placement check, and are drawn by the
 *  terrain debug overlay via the BITS_GATEWAY tile flag.
 *
 *  The gateway list is owned by the WorldMapState it belongs to; the tile flags are the
 *  derived view of that list and are kept in step here and nowhere else.
 */

#include "lib/framework/frame.h"

#include "gateway.h"
#include "map.h"

#include <algorithm>
#include <utility>

namespace
{

enum class GatewayTileFlag
{
	Clear,
	Set
};

/** Set or clear BITS_GATEWAY on every tile the given gateway covers. */
void gwUpdateTileFlags(WorldMapState& mapState, const GATEWAY& gateway, GatewayTileFlag flag)
{
	if (mapState.tiles == nullptr)
	{
		return; // no map to mark (a shutdown after the tiles were released)
	}

	// One of the two axes is degenerate, so walk the other one. A gateway that gwNewGateway's
	// edge clamp inverted (x1 > x2 or y1 > y2) covers no tiles at all, and the loop below
	// correctly visits none.
	const bool vertical = (gateway.x1 == gateway.x2);
	const int from = vertical ? gateway.y1 : gateway.x1;
	const int to = vertical ? gateway.y2 : gateway.x2;

	for (int pos = from; pos <= to; ++pos)
	{
		const int x = vertical ? gateway.x1 : pos;
		const int y = vertical ? pos : gateway.y1;

		// mapTile() clamps out-of-range coordinates onto an edge tile, which would mark the
		// wrong tile. A gateway saved with a bigger map can outlive the map it was made for,
		// so check rather than trust.
		if (!tileOnMap(mapState, x, y))
		{
			continue;
		}

		MAPTILE *psTile = mapTile(mapState, x, y);
		if (flag == GatewayTileFlag::Set)
		{
			psTile->tileInfoBits |= BITS_GATEWAY;
		}
		else
		{
			psTile->tileInfoBits &= static_cast<uint8_t>(~BITS_GATEWAY);
		}
	}
}

/** Append a gateway with the coordinates exactly as given and mark its tiles. */
bool gwAddGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	GATEWAY *psNew = new GATEWAY;
	psNew->x1 = static_cast<uint8_t>(x1);
	psNew->y1 = static_cast<uint8_t>(y1);
	psNew->x2 = static_cast<uint8_t>(x2);
	psNew->y2 = static_cast<uint8_t>(y2);

	// Appended, not prepended: the list order is written out to both the map file
	// (mapSaveToWzMapData) and the game-state snapshot, and read back in that order, so a stable
	// order is what makes those round-trips exact.
	mapState.gateways.push_back(psNew);

	gwUpdateTileFlags(mapState, *psNew, GatewayTileFlag::Set);

	return true;
}

} // anonymous namespace

bool gwInitialise(WorldMapState& mapState)
{
	// Nothing to build up front - a gateway list starts empty and is filled by the map load.
	// It should already be empty here; if a caller skipped its shutdown, drop the stale list
	// rather than leak it.
	ASSERT(mapState.gateways.empty(), "Gateway list was not cleared before initialising (%zu gateway(s) left over)",
	       mapState.gateways.size());
	gwShutDown(mapState);

	return true;
}

void gwShutDown(WorldMapState& mapState)
{
	for (GATEWAY *psGateway : mapState.gateways)
	{
		// Clear the tile flags as well as the list. The tile array outlives the gateway list in
		// at least one path (the game-state terrain restore overwrites the tiles in place and
		// then rebuilds the gateways), so a stale BITS_GATEWAY would otherwise show a gateway
		// that no longer exists. Clearing per gateway is only safe because every gateway is
		// going away: two gateways may cross, so removing one alone could not clear the tile
		// they share.
		gwUpdateTileFlags(mapState, *psGateway, GatewayTileFlag::Clear);
		delete psGateway;
	}

	mapState.gateways.clear();
}

bool gwNewGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	ASSERT_OR_RETURN(false, mapState.tiles != nullptr, "No map loaded - cannot add a gateway");

	// The map format does not promise an order, so normalise to smallest-first. The axes are
	// independent: a gateway is degenerate on one of them, so swapping them separately cannot
	// turn a valid gateway into a different one.
	if (x1 > x2)
	{
		std::swap(x1, x2);
	}
	if (y1 > y2)
	{
		std::swap(y1, y2);
	}

	ASSERT_OR_RETURN(false, x1 == x2 || y1 == y2,
	                 "Invalid gateway (%d, %d) -> (%d, %d): not a straight row or column", x1, y1, x2, y2);
	ASSERT_OR_RETURN(false, x1 >= 0 && y1 >= 0 && x2 < mapState.width && y2 < mapState.height,
	                 "Gateway (%d, %d) -> (%d, %d) does not fit the %d x %d map", x1, y1, x2, y2,
	                 mapState.width, mapState.height);

	// Keep gateways off the map's outer tile ring: that ring is not playable ground (see the
	// interior loops in map.cpp), so a gateway sitting on it is of no use to the AI that reads
	// these, and marking it would light up the border in the gateway overlay.
	//
	// This clamp can invert a gateway that lay wholly on the ring - a one-tile gateway at
	// (0, y) is stored as x1 = 1, x2 = 0 - which leaves it covering no tiles. That is a stable
	// end state, but it means gwNewGateway is not idempotent on its own output: feeding the
	// stored coordinates back in would reorder them and clamp again, moving the gateway. Saved
	// games therefore come back through gwRestoreGateway, which does neither.
	x1 = std::max(x1, 1);
	y1 = std::max(y1, 1);
	x2 = std::min(x2, mapState.width - 2);
	y2 = std::min(y2, mapState.height - 2);

	return gwAddGateway(mapState, x1, y1, x2, y2);
}

bool gwRestoreGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	ASSERT_OR_RETURN(false, mapState.tiles != nullptr, "No map loaded - cannot restore a gateway");

	// Verbatim: no reorder, no clamp. These coordinates are what gwNewGateway already stored when
	// the gateway was first added, so normalising them again would move the gateway (see the note
	// in gwNewGateway). The only checks are the ones the verbatim path still needs: each
	// coordinate has to name a tile of this map, both because GATEWAY holds uint8_t and because
	// the values come from a save file we do not control.
	ASSERT_OR_RETURN(false,
	                 x1 >= 0 && x1 < mapState.width && x2 >= 0 && x2 < mapState.width &&
	                 y1 >= 0 && y1 < mapState.height && y2 >= 0 && y2 < mapState.height,
	                 "Saved gateway (%d, %d) -> (%d, %d) is not on the %d x %d map", x1, y1, x2, y2,
	                 mapState.width, mapState.height);

	return gwAddGateway(mapState, x1, y1, x2, y2);
}

size_t gwNumGateways(const WorldMapState& mapState)
{
	return mapState.gateways.size();
}

GATEWAY_LIST &gwGetGateways(WorldMapState& mapState)
{
	return mapState.gateways;
}

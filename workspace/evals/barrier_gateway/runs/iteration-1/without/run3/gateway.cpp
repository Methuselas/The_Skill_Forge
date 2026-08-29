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
 *  A gateway is a single straight line of tiles marking a choke point that the AI routes
 *  through and defends. The list of them is owned by the per-world WorldMapState; the tiles
 *  they cover carry BITS_GATEWAY, which is the only thing the rest of the game reads them by
 *  (the terrain renderer tints those tiles when the gateway debug display is on).
 */

#include "lib/framework/frame.h"

#include "gateway.h"
#include "map.h"

#include <algorithm>
#include <utility>

namespace
{

/// A gateway addresses tiles directly and stores its coordinates in uint8_t fields, so every
/// coordinate has to name a real tile. A map state with no map loaded has width/height 0 and
/// so rejects everything, which is what we want.
bool gwCoordsAddressTiles(const WorldMapState &mapState, int x1, int y1, int x2, int y2)
{
	const int limitX = std::min<int>(mapState.width, UINT8_MAX + 1);
	const int limitY = std::min<int>(mapState.height, UINT8_MAX + 1);

	return x1 >= 0 && x1 < limitX && x2 >= 0 && x2 < limitX
	       && y1 >= 0 && y1 < limitY && y2 >= 0 && y2 < limitY;
}

/// The window a gateway's ends may occupy along one axis: one tile in from each border of a
/// map `extent` tiles across. Degrades to something in range on maps too small to have an
/// inside, so the clamp can never push a coordinate off the map.
void gwEdgeWindow(int extent, int &low, int &high)
{
	low = std::min(1, extent - 1);
	high = std::max(extent - 2, 0);
}

/// Stamp BITS_GATEWAY over the tiles a gateway covers, or clear it from them.
///
/// Swept as a rectangle so that one loop serves both orientations. A gateway stored with its
/// ends inverted (see the edge clamp in gwNewGateway) covers no tiles, and this is then a
/// no-op - which is correct, and is what keeps set and clear symmetric for such a gateway.
void gwApplyTileBits(WorldMapState &mapState, const GATEWAY &gateway, bool set)
{
	if (!mapState.tiles)
	{
		return; // no map to mark - gwShutDown() runs on torn-down map states
	}

	for (int x = gateway.x1; x <= gateway.x2; x++)
	{
		for (int y = gateway.y1; y <= gateway.y2; y++)
		{
			MAPTILE *psTile = mapTile(mapState, x, y);

			if (set)
			{
				psTile->tileInfoBits |= BITS_GATEWAY;
			}
			else
			{
				psTile->tileInfoBits &= ~BITS_GATEWAY;
			}
		}
	}
}

/// Take ownership of a new gateway with the given (already validated) coordinates.
bool gwStoreGateway(WorldMapState &mapState, int x1, int y1, int x2, int y2)
{
	GATEWAY *psNew = new GATEWAY();

	psNew->x1 = static_cast<uint8_t>(x1);
	psNew->y1 = static_cast<uint8_t>(y1);
	psNew->x2 = static_cast<uint8_t>(x2);
	psNew->y2 = static_cast<uint8_t>(y2);

	// Appended, not prepended. Both mapSaveToWzMapData() and the savegame serializer write the
	// list out in order and feed it straight back in, so list order has to survive a round trip.
	mapState.gateways.push_back(psNew);

	gwApplyTileBits(mapState, *psNew, true);

	return true;
}

} // anonymous namespace

// -----------------------------------------------------------------------------------------

bool gwInitialise(WorldMapState &mapState)
{
	// Nothing to allocate: the gateway list lives in the map state and starts out empty. Getting
	// here with gateways still in it means a map was torn down without gwShutDown(), which would
	// leak them and leave BITS_GATEWAY stamped on tiles that are about to be reused. Complain,
	// then clear up rather than carry the mess into the new game.
	ASSERT(mapState.gateways.empty(), "gateway list has not been reset (%zu gateways left over)",
	       mapState.gateways.size());
	gwShutDown(mapState);

	return true;
}

void gwShutDown(WorldMapState &mapState)
{
	// The tile bits are cleared, not just abandoned: most callers throw the whole map state away
	// immediately afterwards, but the savegame restore path shuts the gateways down on a live map
	// and then restores a new set onto those same tiles.
	for (GATEWAY *psGateway : mapState.gateways)
	{
		gwApplyTileBits(mapState, *psGateway, false);
		delete psGateway;
	}

	mapState.gateways.clear();
}

bool gwNewGateway(WorldMapState &mapState, int x1, int y1, int x2, int y2)
{
	ASSERT_OR_RETURN(false, gwCoordsAddressTiles(mapState, x1, y1, x2, y2),
	                 "gateway (%d,%d)->(%d,%d) is not on the %dx%d map",
	                 x1, y1, x2, y2, mapState.width, mapState.height);

	// Smallest end first. Safe to do per axis: a gateway is a straight line, so at most one of
	// the two axes is ever out of order.
	if (x2 < x1)
	{
		std::swap(x1, x2);
	}
	if (y2 < y1)
	{
		std::swap(y1, y2);
	}

	// A gateway has to be a single line of tiles. The tile sweep, the map writer's coordinate
	// check and the AI's "does this footprint sit in a gateway" test all assume it.
	ASSERT_OR_RETURN(false, x1 == x2 || y1 == y2,
	                 "gateway (%d,%d)->(%d,%d) is neither horizontal nor vertical", x1, y1, x2, y2);

	// Pull the ends in off the map border: the outermost ring of tiles is not somewhere units
	// route through, so a gateway that runs into it has an end nothing can reach.
	//
	// The clamp runs along the axis the gateway lies on, which leaves it a line either way. Note
	// the one-tile gateway: both axes are degenerate, so it takes the vertical branch, and on the
	// top or bottom border the clamp pushes y1 past y2 and the gateway is stored with its ends
	// inverted, covering no tiles. That is the case gwRestoreGateway exists for - putting an
	// inverted gateway back through here would swap the ends and shift it a tile, so this
	// function is not idempotent on its own output.
	int low = 0;
	int high = 0;

	if (x1 == x2)
	{
		gwEdgeWindow(mapState.height, low, high);
		y1 = std::max(y1, low);
		y2 = std::min(y2, high);
	}
	else
	{
		gwEdgeWindow(mapState.width, low, high);
		x1 = std::max(x1, low);
		x2 = std::min(x2, high);
	}

	return gwStoreGateway(mapState, x1, y1, x2, y2);
}

bool gwRestoreGateway(WorldMapState &mapState, int x1, int y1, int x2, int y2)
{
	// Verbatim: no reorder, no edge clamp. These coordinates came out of a GameState that
	// gwNewGateway had already normalised, and that normalisation is not idempotent on its own
	// output, so re-applying it would move the gateway a tile on every save/load cycle.
	//
	// The checks that remain are the ones that are about safety rather than normalisation: the
	// values come off disk and are used to index the tile array. Neither can reject anything
	// gwNewGateway is able to produce - an inverted gateway still has one degenerate axis.
	ASSERT_OR_RETURN(false, gwCoordsAddressTiles(mapState, x1, y1, x2, y2),
	                 "saved gateway (%d,%d)->(%d,%d) is not on the %dx%d map",
	                 x1, y1, x2, y2, mapState.width, mapState.height);
	ASSERT_OR_RETURN(false, x1 == x2 || y1 == y2,
	                 "saved gateway (%d,%d)->(%d,%d) is neither horizontal nor vertical",
	                 x1, y1, x2, y2);

	return gwStoreGateway(mapState, x1, y1, x2, y2);
}

size_t gwNumGateways(const WorldMapState &mapState)
{
	return mapState.gateways.size();
}

GATEWAY_LIST &gwGetGateways(WorldMapState &mapState)
{
	return mapState.gateways;
}

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
 *  A gateway is a horizontal or vertical run of tiles (possibly a single tile) that the AI
 *  treats as a passage between two areas of the map. The list is owned by the world's
 *  WorldMapState; each tile the gateway covers also carries BITS_GATEWAY, which the terrain
 *  renderer reads to draw them when the debug display is switched on.
 */

#include "lib/framework/frame.h"

#include <utility>

#include "gateway.h"
#include "map.h"
#include "world_map_state.h"

/// Set or clear BITS_GATEWAY on every tile the gateway covers.
static void gwMarkTiles(WorldMapState& mapState, const GATEWAY& gate, bool isGateway)
{
	if (!mapState.tiles)
	{
		// No map loaded - there are no tile flags to keep in step. (gwShutDown is called on worlds
		// that never had a map, i.e. mission.gameWorld in skirmish and multiplayer.)
		return;
	}

	// A stored gateway can outlive the tile array it was made for: restoring a saved game
	// reallocates the tiles at the saved dimensions and only then drops the previous map's
	// gateways. Stop at the last tile rather than pass an off-map coordinate to mapTile(), which
	// would clamp it to the edge and mark a tile that is not part of this gateway. An end that
	// falls short of the start (an edge gateway, see gwNewGateway) marks nothing.
	const int xEnd = MIN(static_cast<int>(gate.x2), mapState.width - 1);
	const int yEnd = MIN(static_cast<int>(gate.y2), mapState.height - 1);

	for (int x = gate.x1; x <= xEnd; x++)
	{
		for (int y = gate.y1; y <= yEnd; y++)
		{
			MAPTILE *psTile = mapTile(mapState, x, y);
			if (isGateway)
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

/// Store a gateway exactly as given and mark its tiles.
static bool gwAddGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	// A GATEWAY holds its coordinates in a uint8_t, as does the map file it came from, so anything
	// outside that range cannot be stored - drop it rather than let it wrap round to a coordinate
	// somewhere else on the map.
	ASSERT_OR_RETURN(false, x1 >= 0 && x1 <= UINT8_MAX && y1 >= 0 && y1 <= UINT8_MAX
	                 && x2 >= 0 && x2 <= UINT8_MAX && y2 >= 0 && y2 <= UINT8_MAX,
	                 "Gateway (%d, %d, %d, %d) does not fit the stored coordinate range", x1, y1, x2, y2);

	GATEWAY *psNew = new GATEWAY;
	psNew->x1 = static_cast<uint8_t>(x1);
	psNew->y1 = static_cast<uint8_t>(y1);
	psNew->x2 = static_cast<uint8_t>(x2);
	psNew->y2 = static_cast<uint8_t>(y2);

	mapState.gateways.push_back(psNew);
	gwMarkTiles(mapState, *psNew, true);

	return true;
}

// Initialise the gateway system
bool gwInitialise(WorldMapState& mapState)
{
	ASSERT(mapState.gateways.empty(), "gateway list has not been reset");
	return true;
}

// Shutdown the gateway system
void gwShutDown(WorldMapState& mapState)
{
	for (GATEWAY *psGate : mapState.gateways)
	{
		gwMarkTiles(mapState, *psGate, false);
		delete psGate;
	}
	mapState.gateways.clear();
}

// Add a gateway to the system
bool gwNewGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	ASSERT_OR_RETURN(false, mapState.tiles != nullptr, "No map loaded");
	ASSERT_OR_RETURN(false, x1 == x2 || y1 == y2,
	                 "Gateway (%d, %d, %d, %d) is neither horizontal nor vertical", x1, y1, x2, y2);

	// Store the smallest coordinate first, so everyone else can walk a gateway from (x1, y1) to
	// (x2, y2). Only one axis can differ on a valid gateway, so at most one of these swaps fires.
	if (x1 > x2)
	{
		std::swap(x1, x2);
	}
	if (y1 > y2)
	{
		std::swap(y1, y2);
	}

	ASSERT_OR_RETURN(false, x1 >= 0 && y1 >= 0 && x2 <= mapState.width && y2 <= mapState.height,
	                 "Gateway (%d, %d, %d, %d) is not on the %d x %d map",
	                 x1, y1, x2, y2, mapState.width, mapState.height);

	// The map format lets a gateway name the far edge of the map - a coordinate equal to the width
	// or the height - but there is no tile there, so pull the far end back onto the last tile.
	// This is what makes the function non-idempotent on its own output: a one-tile gateway on that
	// edge is stored with x1 > x2 (or y1 > y2), and feeding it back in would swap the ends and
	// clamp again, shifting the gateway by a tile. Reloading a saved game therefore goes through
	// gwRestoreGateway instead.
	x2 = MIN(x2, mapState.width - 1);
	y2 = MIN(y2, mapState.height - 1);

	return gwAddGateway(mapState, x1, y1, x2, y2);
}

// Restore a gateway verbatim from a saved GameState
bool gwRestoreGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	ASSERT_OR_RETURN(false, mapState.tiles != nullptr, "No map loaded");

	// No reorder and no clamp: the coordinates were already put through gwNewGateway when the map
	// was first loaded, and applying either step a second time would move them.
	return gwAddGateway(mapState, x1, y1, x2, y2);
}

// Get number of gateways
size_t gwNumGateways(const WorldMapState& mapState)
{
	return mapState.gateways.size();
}

// Get the gateway list
GATEWAY_LIST &gwGetGateways(WorldMapState& mapState)
{
	return mapState.gateways;
}

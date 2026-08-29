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
/**
 * @file gateway.cpp
 *
 * Routing gateway code.
 *
 */

#include "lib/framework/frame.h"

#include "gateway.h"
#include "map.h"				// BITS_GATEWAY, mapTile()
#include "world_map_state.h"

#include <utility>				// std::swap

/// A gateway is kept at least this many tiles from every map edge. Same distance the rest of the
/// game treats as "too near the edge" to build on (TOO_NEAR_EDGE, droid.h) - not included from
/// here, because gateways have no other reason to depend on droids.
#define GW_EDGE_MARGIN	3

/** Stamp BITS_GATEWAY over the tiles a gateway covers, or strip it off them again.
 *
 * A gateway runs along one axis: equal x means it runs down a column, anything else means it runs
 * along a row. Both loops are inclusive-bounded and run zero times when the stored coordinates are
 * inverted (x1 > x2 / y1 > y2), which is a state gwNewGateway's edge clamp can produce and which
 * gwRestoreGateway has to reproduce verbatim - so an inverted gateway covers no tiles, and adding
 * or removing one leaves the tile flags exactly as they were.
 */
static void gwStampTiles(WorldMapState& mapState, const GATEWAY& gateway, bool set)
{
	// Every path that stores a gateway checks its coordinates against the loaded map first, so a
	// gateway cannot outlive the tiles it was checked against.
	ASSERT_OR_RETURN(, mapState.tiles != nullptr, "Gateway (%d, %d, %d, %d) with no map loaded",
	                 gateway.x1, gateway.y1, gateway.x2, gateway.y2);

	if (gateway.x1 == gateway.x2)
	{
		for (int y = gateway.y1; y <= gateway.y2; y++)
		{
			MAPTILE *psTile = mapTile(mapState, gateway.x1, y);
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
	else
	{
		for (int x = gateway.x1; x <= gateway.x2; x++)
		{
			MAPTILE *psTile = mapTile(mapState, x, gateway.y1);
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

/// Append a gateway to the list and stamp its tiles. Takes coordinates that are already final -
/// neither caller's remaining work is shared with the other, so nothing is decided in here.
static bool gwStoreGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	GATEWAY *psNew = new GATEWAY();
	psNew->x1 = static_cast<uint8_t>(x1);
	psNew->y1 = static_cast<uint8_t>(y1);
	psNew->x2 = static_cast<uint8_t>(x2);
	psNew->y2 = static_cast<uint8_t>(y2);

	// Appended, not prepended: the state serializer writes this list in order and restores it by
	// calling gwRestoreGateway in that same order, so the list only round-trips if adding preserves
	// order.
	mapState.gateways.push_back(psNew);

	gwStampTiles(mapState, *psNew, true);

	return true;
}

bool gwInitialise(WorldMapState& mapState)
{
	ASSERT(mapState.gateways.empty(), "gateway list has not been reset");

	return true;
}

void gwShutDown(WorldMapState& mapState)
{
	// The tile flags are cleared as well as the list. A restore reuses the tile array in place when
	// the map dimensions already match (readMapTerrain in gamestate_serialize.cpp overwrites texture,
	// height and water but keeps tileInfoBits), and nothing else in the game ever clears BITS_GATEWAY,
	// so leaving the flags set here would strand them on tiles the new gateways do not cover.
	// Clearing per gateway is safe only because this removes all of them at once - two gateways that
	// share a tile would otherwise have the first clear the second's flag.
	for (GATEWAY *psGateway : mapState.gateways)
	{
		gwStampTiles(mapState, *psGateway, false);
		delete psGateway;
	}
	mapState.gateways.clear();
}

bool gwNewGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	// A gateway runs along one axis. Callers feed this straight from map files (mapLoad), so a
	// malformed one is dropped rather than trusted.
	ASSERT_OR_RETURN(false, x1 == x2 || y1 == y2,
	                 "Invalid gateway coordinates (%d, %d, %d, %d): not axis-aligned", x1, y1, x2, y2);

	// Also catches the no-map-loaded case, where width and height are both 0.
	ASSERT_OR_RETURN(false, x1 >= 0 && x1 < mapState.width && x2 >= 0 && x2 < mapState.width
	                        && y1 >= 0 && y1 < mapState.height && y2 >= 0 && y2 < mapState.height,
	                 "Gateway (%d, %d, %d, %d) is off a %d x %d map",
	                 x1, y1, x2, y2, mapState.width, mapState.height);

	// The clamp below assumes both margins land on the map. Nothing bounds a map from below -
	// MAP_MAXWIDTH is the only limit wzmaplib enforces - so a map narrower than the margin has to be
	// refused here rather than clamped to a coordinate that is not a tile.
	ASSERT_OR_RETURN(false, mapState.width > GW_EDGE_MARGIN && mapState.height > GW_EDGE_MARGIN,
	                 "Map %d x %d is too small to hold a gateway", mapState.width, mapState.height);

	// Smallest first. Consumers rely on it: structDoubleCheck() in wzapi.cpp tests a tile against a
	// gateway with `x >= x1 && x <= x2`, which reads as empty on an unordered pair.
	if (x2 < x1)
	{
		std::swap(x1, x2);
	}
	if (y2 < y1)
	{
		std::swap(y1, y2);
	}

	// Pull the gateway away from the map edge. Each endpoint is clamped from its own side, so a
	// gateway that sits entirely inside the margin comes out inverted (low endpoint pushed past the
	// high one) and therefore covers no tiles. That inverted form is what gets stored and saved, and
	// it is why re-adding a stored gateway through this function does not reproduce it - see
	// gwRestoreGateway.
	x1 = MAX(x1, GW_EDGE_MARGIN);
	y1 = MAX(y1, GW_EDGE_MARGIN);
	x2 = MIN(x2, mapState.width - 1 - GW_EDGE_MARGIN);
	y2 = MIN(y2, mapState.height - 1 - GW_EDGE_MARGIN);

	return gwStoreGateway(mapState, x1, y1, x2, y2);
}

bool gwRestoreGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	// Deliberately none of gwNewGateway's conditioning: no smallest-first swap, no edge clamp, and
	// no axis-alignment check. A gateway that gwNewGateway clamped is already stored inverted, and an
	// inverted gateway satisfies neither x1 == x2 nor y1 == y2 - so re-checking alignment here would
	// reject exactly the gateways this function exists to restore. The bounds check stays, because
	// these coordinates come out of a save file and gwStampTiles indexes tiles with them.
	ASSERT_OR_RETURN(false, x1 >= 0 && x1 < mapState.width && x2 >= 0 && x2 < mapState.width
	                        && y1 >= 0 && y1 < mapState.height && y2 >= 0 && y2 < mapState.height,
	                 "Saved gateway (%d, %d, %d, %d) is off a %d x %d map",
	                 x1, y1, x2, y2, mapState.width, mapState.height);

	return gwStoreGateway(mapState, x1, y1, x2, y2);
}

size_t gwNumGateways(const WorldMapState& mapState)
{
	return mapState.gateways.size();
}

GATEWAY_LIST &gwGetGateways(WorldMapState& mapState)
{
	return mapState.gateways;
}

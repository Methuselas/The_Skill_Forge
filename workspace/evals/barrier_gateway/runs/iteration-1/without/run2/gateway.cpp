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
 * A gateway is a one-tile-wide, axis-aligned run of tiles marking a passage between two
 * regions of the map. The list is owned by the WorldMapState it belongs to; the tiles a
 * gateway covers additionally carry the BITS_GATEWAY tile flag, which is derived state -
 * it is rebuilt from the gateway list and is never serialised.
 */

#include "lib/framework/frame.h"

#include "gateway.h"
#include "map.h"

#include <algorithm>

#include <stdint.h>

// -------------------------------------------------------------------------------------
// Tile flags
//
// BITS_GATEWAY is a cache of "some gateway covers this tile". Only the terrain renderer's
// gateway overlay reads it (see terrain.cpp); the AI passability checks walk the gateway
// list itself. It is deliberately not saved: every path that (re)builds the gateway list
// stamps it back on.

static inline void gwSetGatewayFlag(WorldMapState &mapState, int x, int y)
{
	mapTile(mapState, x, y)->tileInfoBits |= BITS_GATEWAY;
}

static inline void gwClearGatewayFlag(WorldMapState &mapState, int x, int y)
{
	mapTile(mapState, x, y)->tileInfoBits &= ~BITS_GATEWAY;
}

enum class GatewayFlagOp
{
	Set,
	Clear
};

/** Stamp or erase BITS_GATEWAY over every tile the given gateway covers.
 *
 * Tiles that are not on the current map are skipped rather than asserted on. A gateway list
 * can outlive the tile array it was built against - restoring a savegame reallocates the
 * tiles for the new dimensions before tearing the old gateways down - and since the flag is
 * derived state that is never serialised, there is nothing to lose by skipping. Likewise a
 * gateway that was inverted by the edge trim in gwNewGateway() covers no tiles at all, and
 * the loops below run zero times for it.
 */
static void gwUpdateGatewayFlags(WorldMapState &mapState, const GATEWAY &gate, GatewayFlagOp op)
{
	if (!mapState.tiles)
	{
		return;	// no map loaded (or already torn down) - nothing to stamp
	}

	// One of the two axes is always degenerate, so this covers both orientations.
	for (int y = gate.y1; y <= gate.y2; ++y)
	{
		for (int x = gate.x1; x <= gate.x2; ++x)
		{
			if (!tileOnMap(mapState, x, y))
			{
				continue;
			}
			if (op == GatewayFlagOp::Set)
			{
				gwSetGatewayFlag(mapState, x, y);
			}
			else
			{
				gwClearGatewayFlag(mapState, x, y);
			}
		}
	}
}

/** Take ownership of a new gateway with the coordinates exactly as given, and stamp its tiles. */
static bool gwAddGateway(WorldMapState &mapState, int x1, int y1, int x2, int y2)
{
	// GATEWAY stores uint8_t, which is enough for MAP_MAXWIDTH / MAP_MAXHEIGHT (256).
	ASSERT_OR_RETURN(false, x1 >= 0 && x1 <= UINT8_MAX && y1 >= 0 && y1 <= UINT8_MAX
	                 && x2 >= 0 && x2 <= UINT8_MAX && y2 >= 0 && y2 <= UINT8_MAX,
	                 "Gateway (%d, %d, %d, %d) is not storable", x1, y1, x2, y2);

	GATEWAY *psNew = new GATEWAY;
	psNew->x1 = static_cast<uint8_t>(x1);
	psNew->y1 = static_cast<uint8_t>(y1);
	psNew->x2 = static_cast<uint8_t>(x2);
	psNew->y2 = static_cast<uint8_t>(y2);

	mapState.gateways.push_back(psNew);

	gwUpdateGatewayFlags(mapState, *psNew, GatewayFlagOp::Set);

	return true;
}

// -------------------------------------------------------------------------------------
// Public interface

bool gwInitialise(WorldMapState &mapState)
{
	ASSERT(mapState.gateways.empty(), "gateway list has not been reset");

	// Defensive: release anything a previous world left behind rather than leaking it.
	gwShutDown(mapState);

	return true;
}

void gwShutDown(WorldMapState &mapState)
{
	while (!mapState.gateways.empty())
	{
		GATEWAY *psDel = mapState.gateways.front();
		mapState.gateways.pop_front();

		gwUpdateGatewayFlags(mapState, *psDel, GatewayFlagOp::Clear);

		delete psDel;
	}
}

bool gwNewGateway(WorldMapState &mapState, int x1, int y1, int x2, int y2)
{
	// A gateway must be on the map and axis-aligned. Callers feed us map data and script data,
	// so this is a reject, not an assert: map.cpp logs and drops the offending gateway.
	if (!tileOnMap(mapState, x1, y1) || !tileOnMap(mapState, x2, y2)
	    || (x1 != x2 && y1 != y2))
	{
		return false;
	}

	// Store smallest coordinate first, so that every consumer can assume x1 <= x2 and y1 <= y2
	// and just iterate (see structDoubleCheck() in wzapi.cpp, and gwUpdateGatewayFlags above).
	if (x2 < x1)
	{
		std::swap(x1, x2);	// horizontal: y is the same
	}
	if (y2 < y1)
	{
		std::swap(y1, y2);	// vertical: x is the same
	}

	// Trim the gateway back off the outermost ring of tiles: the map border is permanently
	// blocking, so an end tile sitting on it can never be part of a usable passage. Only the
	// axis the gateway runs along is trimmed, so the gateway stays axis-aligned.
	//
	// NOTE: a one-tile gateway satisfies x1 == x2 *and* y1 == y2, so it is trimmed as a vertical
	// one. On the top or bottom row that leaves y1 > y2 - an inverted gateway that covers no
	// tiles. That is deliberate and is what gets stored, and it is exactly why this function is
	// not idempotent on its own output: feeding the stored (1, y, 0, y) back in would swap it to
	// (0, y, 1, y) and then trim it to (1, y, 1, y), shifting the gateway by a tile every cycle.
	// Reloading a stored gateway list therefore goes through gwRestoreGateway() instead.
	if (x1 == x2)
	{
		if (mapState.height >= 2)
		{
			y1 = std::max<int>(y1, 1);
			y2 = std::min<int>(y2, mapState.height - 2);
		}
	}
	else
	{
		if (mapState.width >= 2)
		{
			x1 = std::max<int>(x1, 1);
			x2 = std::min<int>(x2, mapState.width - 2);
		}
	}

	return gwAddGateway(mapState, x1, y1, x2, y2);
}

bool gwRestoreGateway(WorldMapState &mapState, int x1, int y1, int x2, int y2)
{
	// Verbatim: no smallest-first reorder and no edge trim, because the coordinates handed to us
	// are already the output of those steps and neither is idempotent (see gwNewGateway). Running
	// them again would move a stored gateway on every save/load cycle.
	//
	// We do not reject an off-map gateway either. The saved coordinates are authoritative for the
	// list, and gwUpdateGatewayFlags() simply skips any tile that is not on the map - BITS_GATEWAY
	// is not serialized, so nothing is lost by skipping it.
	ASSERT_OR_RETURN(false, x1 == x2 || y1 == y2,
	                 "Saved gateway (%d, %d, %d, %d) is not axis-aligned", x1, y1, x2, y2);

	return gwAddGateway(mapState, x1, y1, x2, y2);
}

size_t gwNumGateways(const WorldMapState &mapState)
{
	return mapState.gateways.size();
}

GATEWAY_LIST &gwGetGateways(WorldMapState &mapState)
{
	return mapState.gateways;
}

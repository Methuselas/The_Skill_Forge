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

#include <utility>

#include "lib/framework/frame.h"

#include "gateway.h"
#include "map.h"

/* -------------------------------------------------------------------------- */
/*                   Gateway tile flags                                        */
/* -------------------------------------------------------------------------- */

/** Stamp BITS_GATEWAY onto every tile the gateway covers.
 *
 * A gateway is a line, so one of the two axes is degenerate; walking both ranges handles the
 * horizontal and the vertical case without branching, and an inverted gateway (x1 > x2, see
 * gwNewGateway) walks nothing.
 *
 * Every tile is tested with tileOnMap() before it is touched. A gateway may legitimately hold a
 * coordinate that is off the current map - gwNewGateway pulls only the far end back, and
 * gwRestoreGateway stores saved coordinates verbatim - and mapTile() clamps an out-of-range
 * coordinate into the map rather than rejecting it, so an untested coordinate would silently stamp
 * some other tile (and trip mapTile()'s assert). tileOnMap() also covers the no-map case: width and
 * height are zero until a map is loaded, so the walk is empty and mapTile() is never reached.
 */
static void gwStampGateway(WorldMapState& mapState, const GATEWAY *psGate)
{
	for (int x = psGate->x1; x <= psGate->x2; x++)
	{
		for (int y = psGate->y1; y <= psGate->y2; y++)
		{
			if (tileOnMap(mapState, x, y))
			{
				mapTile(mapState, x, y)->tileInfoBits |= BITS_GATEWAY;
			}
		}
	}
}

/** Clear BITS_GATEWAY from every tile the gateway covers. Same walk and the same bounds rule as
 *  gwStampGateway - it has to unstamp exactly the tiles that were stamped.
 */
static void gwUnstampGateway(WorldMapState& mapState, const GATEWAY *psGate)
{
	for (int x = psGate->x1; x <= psGate->x2; x++)
	{
		for (int y = psGate->y1; y <= psGate->y2; y++)
		{
			if (tileOnMap(mapState, x, y))
			{
				mapTile(mapState, x, y)->tileInfoBits &= ~BITS_GATEWAY;
			}
		}
	}
}

/* -------------------------------------------------------------------------- */
/*                   Gateway functions                                         */
/* -------------------------------------------------------------------------- */

// Initialise the gateway system
bool gwInitialise(WorldMapState& mapState)
{
	// The list should already be empty; a leftover means a map was torn down without gwShutDown.
	// Report it, then release it properly rather than dropping the pointers on the floor.
	ASSERT(mapState.gateways.empty(), "gateway list has not been reset (%zu left)", mapState.gateways.size());
	gwShutDown(mapState);

	return true;
}

// Shutdown the gateway system
void gwShutDown(WorldMapState& mapState)
{
	for (GATEWAY *psGateway : mapState.gateways)
	{
		// Clearing the tile flags matters as much as freeing the memory: a gamestate restore calls
		// gwShutDown and then re-adds the saved gateways onto the *same* tiles, so a flag left behind
		// here would persist as a gateway marker with no gateway behind it.
		gwUnstampGateway(mapState, psGateway);
		free(psGateway);
	}

	mapState.gateways.clear();
}

// Add a gateway to the system
bool gwNewGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	// A gateway must be a straight line, and there must be a map for it to sit on - the clamp below
	// computes width - 1, which underflows into 0xFF on a zero-sized map. map.cpp logs and drops a
	// gateway we reject here, so returning false is a supported outcome and not a fatal one.
	// The upper bound is inclusive: the map writer (lib/wzmaplib) only warns when a coordinate is
	// strictly greater than the map dimension, so a coordinate equal to it is data we do see.
	ASSERT_OR_RETURN(false, mapState.width > 0 && mapState.height > 0
	                 && x1 >= 0 && y1 >= 0 && x2 >= 0 && y2 >= 0
	                 && x1 <= mapState.width && x2 <= mapState.width
	                 && y1 <= mapState.height && y2 <= mapState.height
	                 && (x1 == x2 || y1 == y2), "Invalid gateway coordinates (%d, %d, %d, %d)",
	                 x1, y1, x2, y2);

	// Make the first coordinate the smallest, so the tile walk can run x1..x2 and y1..y2.
	if (x2 < x1)
	{
		std::swap(x1, x2);
	}
	if (y2 < y1)
	{
		std::swap(y1, y2);
	}

	GATEWAY *psNew = (GATEWAY *)malloc(sizeof(GATEWAY));

	// Correct an out-of-map gateway by pulling its far end back onto the map. The near end is left
	// where it is: clamping both ends would drag a gateway that lies one tile past the edge onto a
	// real tile and mark it as a gateway there. The price is that a one-tile gateway sitting at
	// x == width comes out inverted (x1 > x2) and stamps nothing, which is the behaviour
	// gwRestoreGateway exists to preserve across a save/load.
	psNew->x1 = (uint8_t)x1;
	psNew->y1 = (uint8_t)y1;
	psNew->x2 = (uint8_t)MIN(x2, mapState.width - 1);
	psNew->y2 = (uint8_t)MIN(y2, mapState.height - 1);

	mapState.gateways.push_back(psNew);

	gwStampGateway(mapState, psNew);

	return true;
}

// Restore a gateway verbatim from a saved GameState
bool gwRestoreGateway(WorldMapState& mapState, int x1, int y1, int x2, int y2)
{
	// The coordinates come straight out of a save file, so they are untrusted integers on their way
	// into uint8_t fields; without this a corrupt value would truncate silently.
	ASSERT_OR_RETURN(false, x1 >= 0 && y1 >= 0 && x2 >= 0 && y2 >= 0
	                 && x1 <= UINT8_MAX && y1 <= UINT8_MAX && x2 <= UINT8_MAX && y2 <= UINT8_MAX,
	                 "Invalid saved gateway coordinates (%d, %d, %d, %d)", x1, y1, x2, y2);

	GATEWAY *psNew = (GATEWAY *)malloc(sizeof(GATEWAY));

	// Verbatim - no reorder, no clamp. gwNewGateway's reorder-then-clamp is not idempotent on its own
	// output: re-feeding a stored inverted gateway would swap the ends back and move a coordinate, so
	// the saved list would not survive a round trip. What was saved is what gets restored.
	psNew->x1 = (uint8_t)x1;
	psNew->y1 = (uint8_t)y1;
	psNew->x2 = (uint8_t)x2;
	psNew->y2 = (uint8_t)y2;

	mapState.gateways.push_back(psNew);

	// BITS_GATEWAY is a debug-overlay flag and is not serialized, so a saved gateway whose coordinates
	// fall outside the current map simply stamps fewer tiles; the gateway itself is stored either way,
	// which is what the round trip is about.
	gwStampGateway(mapState, psNew);

	return true;
}

/* -------------------------------------------------------------------------- */
/*                   Gateway data access functions                             */
/* -------------------------------------------------------------------------- */

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

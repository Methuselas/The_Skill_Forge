# Patch Proposal — Derive the Measuring Point From the View Geometry

**Target:** `PAT_measure_subdivide_and_repeat_on_perspective_planes`

**Disposition:** candidate patch proposal only; target card remains byte-unchanged.

## Proposed addition
When exact arbitrary-distance transfer is needed, make the measuring point derivation explicit rather than treating it as a named construction point. For a horizontal receding direction with vanishing point `V` and the station-point/eye representation `E`, rotate the distance `V-E` onto the horizon about `V`; the horizon intersection is the measuring point for that direction. Mark true distances on the Ground Line/Picture Plane and project them to this measuring point to cut the receding line.

Keep this branch **trigger-only**. Diagonal centers and simple subdivisions remain the preferred lightweight method when they are sufficient.

## Evidence
Gwen White, *Perspective: A Guide for Artists, Architects and Designers*, printed pp. 25-28 (PDF pp. 26-29), including the geometric proof on printed p. 28.

## Why patch rather than new card
D'Amelio already supplies plane metrology and measuring-line use. White adds the missing exact derivation and proof for the construction point.

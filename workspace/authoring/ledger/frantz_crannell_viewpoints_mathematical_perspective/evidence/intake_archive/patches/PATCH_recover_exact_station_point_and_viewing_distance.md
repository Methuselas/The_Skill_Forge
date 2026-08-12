# Patch Proposal — Recover the Exact Station Point and Viewing Distance From Image Geometry

**Target:** `PAT_recover_view_field_from_existing_image`

**Disposition after Viewpoints:** **VARIANT** `VAR_recover_station_point_and_viewing_distance`.

## Proposed variant
After ordinary VP/eye-level recovery, load this branch only when the source image contains enough trustworthy geometry to recover the camera more exactly.

- **One-point:** with a known square/cube/known proportion, use a diagonal direction vanishing point plus the main VP to recover viewing distance; the correct eye lies directly in front of the main VP in true one-point perspective.
- **Standard two-point:** if the two recovered VPs represent perpendicular horizontal directions, the eye lies on the horizontal viewing semicircle whose endpoints are those VPs. A further cue—uncropped image center, a known square/rectangle, or another known angle—selects the actual station point and viewing distance.
- **Three-point:** when the three principal VPs represent three mutually perpendicular directions, use `PAT_validate_three_point_viewpoint_geometry`; the viewing target is the orthocenter of the VP triangle and the viewing distance follows from its altitude geometry.

## Evidence
Frantz & Crannell, *Viewpoints*, printed pp. 32-35, 61-69, and 86-93.

## Boundary
Do not claim an exact station point from arbitrary perspective art unless the required world-angle/proportion assumptions are actually known. Lens distortion, nonrectilinear projection, cropped/altered photography, and inaccurate hand drawing can invalidate the exact recovery.

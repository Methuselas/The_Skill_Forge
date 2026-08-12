# Viewpoints Mathematical Perspective Audit — Resolutions

**Source:** Marc Frantz & Annalisa Crannell, *Viewpoints: Mathematical Perspective and Fractal Geometry in Art* (2011).

**PASS scope:** Deep audit of the perspective half: Chapters 1-7, the forced-perspective/Hitchcock-zoom interlude, and the intervening plate section. Fractal Chapters 8-9 were not routed into PASS because the current task was the Perspective curriculum and the Gate 1 structure shows the fractal material begins as a separate subject at Chapter 8.

## 1. Distortion / field of view — RESOLVED

The earlier D'Amelio card was too narrow because it treated vanishing-point spacing as the main control. *Viewpoints* makes the underlying reason explicit: a rectilinear perspective image is tied to a specific station point and viewing distance. A valid cube can look elongated when viewed too far from that station point; two-point VP separation determines a viewing semicircle; three-point geometry similarly fixes a viewing target and distance.

**Final PASS decision:** replace `PAT_control_perspective_distortion_with_vanishing_spacing` with `PAT_control_perspective_distortion_with_viewpoint_and_projection_choice`.

The replacement keeps VP spacing as a practical control but puts it under a broader sequence:
1. distinguish construction error from viewing/display mismatch;
2. recover or choose the station relationship;
3. reframe/crop, change viewing distance/VP spacing coherently, enlarge the support, or cluster important content near the viewing target;
4. if one compact image must cover an extreme angular field, change projection model deliberately instead of locally warping rectilinear objects.

## 2. Skyscraper / extreme look-up case — RESOLVED

The source's "skyscraper paradox" is decisive. If a flat Picture Plane is parallel to the face of a rectangular skyscraper, the correct rectilinear image of that face is still a rectangle—even when the viewer is physically close to the building. The felt upward/downward convergence appears when the viewer scans a sufficiently large correctly viewed picture, because the *picture itself* is seen at steep angles above and below the eye.

The source's numerical example is deliberately extreme: a 400-foot building viewed from 40 feet away gives `h/d = 10`, so a comfortable 2-foot viewing distance requires a 20-foot-high flat image. A six-inch reproduction would imply a station distance around 0.6 inches and is practically unviewable.

**Final PASS decision:** do not invent extra vertical vanishing points inside a face-parallel rectilinear setup merely to imitate the sensation of looking up/down. For a normal-size image, either recompose/reframe the view or use a deliberate alternate projection. *Viewpoints* uses a sphere centered on the eye; world straight lines project to great-circle arcs and opposite directions receive paired vanishing points (the source's six-point spherical perspective).

This validates the broader projection-choice branch proposed after Robertson.

## 3. Exact camera/viewfield setup — RESOLVED

The source supplies a clean mathematical camera model:
- eye/station point `E`;
- Picture Plane;
- sight rays from `E` through world points;
- image points where those rays pierce the Picture Plane;
- viewing target as the perpendicular projection of the eye onto the Picture Plane;
- viewing distance as the perpendicular eye-to-plane distance.

Chapter 2 even gives the projection formula in an aligned coordinate setup: image coordinates scale by `d/(z+d)`. This math should remain internal; it explains diminution and camera consistency without becoming ordinary runtime pedagogy.

For standard two-point perspective with a vertical Picture Plane, the ordinary horizon/eye-level construction remains valid. For arbitrary three-point/tilted setups, *Viewpoints* switches to the exact vanishing-triangle geometry rather than extending the horizontal-horizon mnemonic by assumption.

**Final PASS decision:** finalize the optional exact-camera variant proposed after White/Robertson; no separate foundation is required.

## 4. Three-point viewpoint geometry — NEW DURABLE DELTA

This is the strongest genuinely new theorem in the source for the working library.

If three VPs represent three mutually perpendicular world directions in a rectilinear three-point image:
- the VP triangle must be **acute**;
- a right triangle collapses the viewing distance to zero;
- an obtuse triangle has no common station point;
- the viewing target is the triangle's **orthocenter**;
- the viewing distance can be recovered from the altitude geometry;
- a nearly equilateral VP triangle gives the most generous viewing distance relative to the triangle's size;
- content near the viewing target is less vulnerable to apparent distortion when viewed from a nearby-but-not-exact position.

**Final PASS decision:** new triggered Pattern `PAT_validate_three_point_viewpoint_geometry`. The proof stays internal unless teaching/exact reconstruction is requested.

## 5. Numeric Cone-of-Vision thresholds — NOT VALIDATED AS UNIVERSAL

White and Gill supplied fixed 60-degree conventions; Robertson supplied practical 50/60-degree and lens analogies. The mathematical source does **not** establish a universal 50- or 60-degree cutoff. Instead, it repeatedly explains apparent distortion through the station point, viewing distance, viewing target, support size, and projection surface.

This does not prove that every historical COV convention is useless; it means the current audit has no source basis for elevating one number into project law.

**Final PASS decision:** keep any 50/60-degree values as source-specific practice notes only. The canonical/runtime decision should be geometric and presentation-aware, not a fixed numeric threshold.

## 6. Ellipse minor-axis / projected plane-normal theorem — NOT RESOLVED BY THIS SOURCE

The perspective half of *Viewpoints* does not develop the projective geometry of circles into ellipses or prove a universal relationship between an ellipse minor axis and the normal of the source circle's plane. Its anamorphic chapter mentions ellipses as distorted results but does not establish the Robertson/Norling construction claim.

**Final PASS decision:** the universal theorem remains unpromoted. Keep Robertson's minor-axis/axle rule as an operational construction heuristic with boundaries; keep D'Amelio's point-constructed projected circle as the stricter exact fallback. No further Perspective-source dependency is required unless the project later wants a formal conic-section theorem.

## 7. Anamorphosis, forced perspective, Hitchcock zoom — REFERENCE / OPTIONAL SPECIAL EFFECT

Chapter 7 and the movie interlude strongly reinforce one causal lesson: perspective can be intentionally viewpoint-locked, and moving the station point while changing picture-plane/lens scaling changes spatial relationships even when a chosen foreground subject is held at the same image size.

These are useful demonstrations of camera dependence but do not earn another core Perspective card in this pass. They remain reference material for deliberate illusion/special-effect tasks.

## Net audit result

The Viewpoints Deep PASS does **not** reopen the mature artist-facing curriculum. It performs the intended audit:
- one foundation replacement for distortion/viewfield/projection choice;
- one new triggered three-point validation Pattern;
- three patches that finalize exact-camera, convergence, and camera-recovery variants;
- fixed COV numbers demoted to source-specific heuristics;
- ellipse theorem left deliberately unpromoted;
- anamorphic/forced-perspective material retained as reference.

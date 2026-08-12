# Viewpoints Perspective Mathematical Audit — PASS Report

**Source:** Marc Frantz & Annalisa Crannell, *Viewpoints: Mathematical Perspective and Fractal Geometry in Art* (2011)  
**Route:** Surgical Deep PASS of the Perspective half only  
**Baseline:** Frozen cumulative D’Amelio → Norling → White → Robertson → Gill candidate repo  
**State:** Candidate hold; no canonical promotion performed

## Scope

The Deep audit covers Chapters 1–7 and the forced-perspective / Hitchcock-zoom interlude, printed perspective pp. 1–138. Physical PDF pp. 16–153 were rendered and visually scanned, followed by the pp. 154–165 plate section. Chapter 8 begins the separate fractal-geometry subject and was intentionally left outside this Perspective pass.

## Why this source earned Deep treatment

The five artist-facing books had already produced a mature practical perspective system. The unresolved questions were mathematical rather than pedagogical: what apparent distortion actually means relative to the intended station point, how exact three-point camera geometry constrains valid vanishing points, how to treat close skyscraper / extreme-field views, whether fixed 50°/60° cone-of-vision values deserve project-law status, and whether the ellipse minor-axis heuristic could be promoted to a theorem.

## Durable output

### 1. Foundation supersession candidate

`PAT_control_perspective_distortion_with_viewpoint_and_projection_choice`

This supersedes the earlier VP-spacing-only distortion candidate. Vanishing-point spacing remains useful, but it is treated as one consequence/control inside the larger relationship among station point, viewing target, viewing distance, support/frame, and projection model.

The skyscraper case is now explicit: a rectilinear image can be mathematically correct while requiring an impractically close viewing distance or huge flat support to reproduce the intended experience. The runtime choice therefore becomes global—reframe/enlarge/change station geometry, or deliberately choose a curvilinear/spherical projection for an extreme compact field—rather than locally warping objects.

### 2. New triggered three-point validator

`PAT_validate_three_point_viewpoint_geometry`

For three vanishing points representing three mutually perpendicular world directions, the VP triangle must be acute. The viewing target is the triangle’s orthocenter; altitude geometry recovers the viewing distance. Right/near-right triangles are degenerate or extremely close-viewing cases, and obtuse triangles cannot represent one common viewpoint for those three orthogonal axes.

The proof remains internal unless exact reconstruction or teaching is requested.

### 3. Three finalizing patches

- exact camera/viewfield variant under the eye-level / vanishing-direction Pattern;
- parallel-sight-ray theorem under the convergence-selection Pattern;
- exact station-point / viewing-distance recovery variants under the existing-image recovery Pattern.

These formalize earlier White/Robertson/Norling machinery without creating duplicate foundations.

## Audit questions resolved

- **Distortion / projection scope:** resolved. Replace the narrow VP-spacing foundation with viewpoint + presentation + projection choice.
- **Tilted / three-point exact geometry:** resolved sufficiently for the curriculum. Do not extend a simple horizontal-horizon mnemonic into arbitrary three-point setups; use exact VP-triangle geometry when needed.
- **Fixed COV numbers:** not promoted. The source does not establish a universal 50° or 60° theorem; those values remain source-specific practice heuristics.
- **Ellipse minor-axis theorem:** not resolved by this source. Keep Robertson’s axle/minor-axis rule bounded as a practical heuristic and D’Amelio’s point-constructed projected circle as the exact fallback.

## Reference-only material

Anamorphosis, forced perspective, and the Hitchcock/dolly zoom are retained as useful camera/viewpoint examples. They reinforce the same causal model and do not earn another core Perspective card.

## Net result

The mathematical audit did what it was supposed to do without reopening basic perspective pedagogy: **one foundation replacement, one new triggered Pattern, three exact-geometry patches, and bounded theory/reference decisions.** The remaining work is repository reconciliation of the already-agreed Perspective patches and supersessions—not more source study.

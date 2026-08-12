# Chapter 6 Perspective Reconciliation — D'Amelio vs. Held Hogarth Candidate

status: **candidate-context reconciliation; no canonical mutation**

## Existing held boundary
`PAT_build_shared_scene_perspective_from_figure` says a correctly built figure can calibrate a scene grid, but explicitly states that it does **not** replace dedicated horizon/vanishing systems, camera/world axes, architectural perspective, or single-view metrology.

## D'Amelio delta
D'Amelio supplies the missing independent scene field:
- eye level / horizontal vanishing line;
- direction-specific vanishing points;
- view-driven one-/two-/vertical convergence;
- scale transfer with height and width guides;
- plane subdivision and measurement;
- inclined-plane vanishing relationships;
- round-form projection;
- constructive cast shadows.

## Reconciliation rule
The two methods are complementary, not competing:
1. A figure may help **calibrate into** a perspective field when its landmarks are trusted.
2. D'Amelio's scene field can exist **without** a figure and can become the authority that later figures inherit.
3. When both are available, they should converge on the same eye level, scale, and direction families.
4. No patch is applied to the held Hogarth card in this PASS because it is not canonical and the multi-book perspective curriculum is still open.

## Future commit note
When the perspective book sequence is reconciled, review whether the Hogarth candidate should become a specialization/entry method under the more general scene-perspective foundation.

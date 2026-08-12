# Patch Proposal — Make Field of View and Projection/Grid Choice Part of Distortion Control

**Target:** `PAT_control_perspective_distortion_with_vanishing_spacing`

**Disposition:** candidate patch proposal only; target card remains byte-unchanged.

## Proposed addition
Distortion control is not only “move vanishing points farther apart.” Add two linked decisions from Robertson:

1. **How much field must one view contain?** Wider fields/lens impressions force stronger apparent convergence and edge distortion.
2. **Which projection/grid model matches the intent?** Linear 1-/2-/3-point grids are efficient design constructions; wide photographic/fisheye looks may require curvilinear warping instead of forcing straight world directions to remain straight across an extreme field.

Treat Robertson's specific 50°/60° and lens-number recommendations as **source-specific practical guidelines**, not universal thresholds, until the planned *Viewpoints* mathematical audit.

## Evidence
Scott Robertson with Thomas Bertling, *How to Draw*, printed pp. 23, 62-64, 118, and 186-187.

## Cumulative effect
This patch absorbs White's fixed 60-degree Cone-of-Rays hold conceptually while keeping the numeric boundary unresolved.

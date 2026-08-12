# Patch Proposal — One-Look / Viewfield Diagnostic for Perspective Distortion

**Target:** `PAT_control_perspective_distortion_with_vanishing_spacing` and Robertson's field-of-view patch.

## Gill contribution
Printed pp. 20-24 (physical pp. 23-27) treat a perspective image as one fixed viewpoint and warn that otherwise-correct construction can become visually awkward when major forms are pushed to the extreme edge of the usable view. Gill's cube sequence supplies a practical diagnostic: a near corner close to the view limit can appear unnaturally pinched or stretched.

## Proposed merge
- Preserve Robertson's broader field-of-view/projection-choice logic as the stronger foundation.
- Add Gill's simpler production test: if a major corner near the frame reads visibly more distorted than the same form nearer the center, move the station/viewpoint back, reframe, or crop before locally repairing objects.
- Keep the instruction to treat the image as one coherent camera/viewpoint rather than accumulating several eye positions across one planar perspective.

## Hold
Do **not** canonicalize Gill's fixed 60-degree maximum cone as universal. Robertson and White already supplied similar numeric conventions; the planned *Viewpoints* Deep PASS should separate geometric necessity, viewing convention, and perceptual tolerance.

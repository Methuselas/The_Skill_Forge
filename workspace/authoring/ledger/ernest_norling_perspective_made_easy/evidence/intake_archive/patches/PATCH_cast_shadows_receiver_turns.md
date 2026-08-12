# Patch Proposal — Cast Shadows Must Turn With the Receiving Surface

**Target:** `AP_construct_cast_shadows_in_perspective`

**Disposition:** candidate patch proposal only; target AP remains byte-unchanged.

## Proposed addition
Add a receiving-surface checkpoint: when a cast shadow crosses from floor to wall, ground to incline, or another plane break, reconstruct the shadow on the new receiver. The contour bends where the receiving geometry bends; it should not continue as one flat screen-space shape.

## Evidence
Ernest Norling, *Perspective Made Easy*, printed pp. 157-165.

## Why patch rather than new card
D'Amelio already supplies the sunlight and local-point-source shadow protocol. Norling supplies a useful receiver-transition example.

# Patch Proposal — Reconstruct Cast Shadows Across Plane Breaks and Curved Receivers

**Target:** `AP_construct_cast_shadows_in_perspective`

**Disposition:** candidate patch proposal only; target AP remains byte-unchanged.

## Proposed addition
Strengthen the receiver branch. When a cast shadow crosses from one receiving surface to another, keep the same light ray but reconstruct where it meets the new surface; the shadow path bends with the receiver instead of continuing as one screen-space line. For a curved receiver, first establish a reference shadow on a simpler plane (White repeatedly uses the ground), then use corresponding surface/generator lines and the same light rays to locate the shadow points on the curve. For a local point light, re-establish the shadow direction relative to the receiver level/plane rather than treating all surfaces as one ground plane.

## Evidence
Gwen White, *Perspective*, printed pp. 57-69 (PDF pp. 58-70), especially the inclined-plane, dormer/chimney, curved-cylinder, and artificial-light examples.

## Why patch rather than new card
D'Amelio already owns the cast-shadow AP and Norling already proposed a receiver-turn checkpoint. White deepens that same protocol with exact multi-plane and curved-receiver constructions.

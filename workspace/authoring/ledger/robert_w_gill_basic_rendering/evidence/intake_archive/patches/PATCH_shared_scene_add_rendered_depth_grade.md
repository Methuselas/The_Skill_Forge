# Patch Proposal — Add a Rendered Depth Grade to the Shared Scene Field

**Target:** `AP_construct_a_shared_scene_perspective_field`.

## Gill contribution
The atmospheric-effect chapter (printed pp. 25-31) and the consolidation example (printed pp. 177-180) treat convergence, foreshortening, diminution, light/shadow, atmosphere, and overlap as cooperating depth evidence. Gill repeatedly warns against applying atmospheric weakening to only one class of scene element.

## Proposed merge
Add a late optional rendering state after geometry/scale are solved:
1. preserve the common perspective field;
2. rank major depth zones;
3. reduce contrast/detail/edge clarity with distance across objects, ground, and cast shadows;
4. verify that no distant element accidentally has stronger depth contrast than an equivalent near element unless composition intentionally overrides it.

This keeps the perspective AP geometric at its core while giving it a reliable bridge to finished spatial rendering.

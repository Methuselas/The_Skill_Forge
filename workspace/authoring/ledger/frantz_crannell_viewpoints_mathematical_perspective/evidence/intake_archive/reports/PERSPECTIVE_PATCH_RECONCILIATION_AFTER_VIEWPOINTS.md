# Perspective Patch Reconciliation — After Viewpoints Mathematical Audit

**Status:** final proposal layer; no prior candidate or canonical file has been mutated by this intake.

## Decisions that are now settled

1. **Eye level / exact camera**
   - Norling high-water diagnostic: MERGE into the eye-level Pattern.
   - White camera geometry: ABSORBED into Robertson exact-camera variant.
   - Robertson exact-camera variant: FINALIZE with Viewpoints projection geometry; no universal numeric COV.

2. **Choosing convergence**
   - Norling coupled-VP intuition: retain as plain-language note.
   - Robertson Visual Ray variant: FINALIZE with Viewpoints Vanishing Point Theorem (parallel sight ray through the station point).

3. **Distortion / viewfield / projection**
   - D'Amelio `PAT_control_perspective_distortion_with_vanishing_spacing`: SUPERSEDE.
   - Successor: `PAT_control_perspective_distortion_with_viewpoint_and_projection_choice`.
   - Norling reframe rule, Robertson field/projection choice, and Gill edge diagnostic are absorbed/merged into the successor.
   - Fixed 50/60-degree COV values do not become project law.
   - Skyscraper/extreme-field branch is now explicit: large flat support/reframe versus deliberate curvilinear/spherical projection.

4. **Three-point perspective**
   - NEW specialization: `PAT_validate_three_point_viewpoint_geometry`.
   - Exact rule: acute VP triangle; orthocenter viewing target; altitude geometry for distance; avoid near-right triangles unless deliberately extreme.

5. **Inclined planes**
   - Norling "false eye level" remains a mnemonic only; MERGE as auxiliary slope-vanishing direction/line.
   - White true oblique-plane measurement remains a separate specialization.

6. **Measurement**
   - White arbitrary measuring-point derivation remains a triggered VARIANT under the plane-metrology Pattern.

7. **Cast shadows**
   - Norling receiver-turn patch is ABSORBED by White's complex-receiver branch.
   - White complex receivers become a VARIANT under the cast-shadow AP.
   - Gill terminator clarification MERGES; atmospheric shadow weakening HANDS OFF to Gill atmosphere Pattern.

8. **Shared scene**
   - Robertson underlay-assisted scene lock remains a VARIANT.
   - Gill atmospheric depth remains a downstream rendering HANDOFF through `AP_prepare_construction_for_rendering` rather than a new perspective state.

9. **Hogarth tone consolidation**
   - Gill remains CORROBORATION / relation only; no content rewrite is necessary.

10. **Reflections**
   - White `PAT_construct_reflections_across_arbitrary_planes` SUPERSEDES Norling `PAT_construct_reflections_across_level_planes`.

11. **Ellipse axis**
   - The universal theorem remains unpromoted after Viewpoints. Keep the heuristic bounded; exact projected-circle construction remains available.

## Remaining blockers before a Perspective commit

The mathematical questions that originally justified the Viewpoints audit are no longer blockers. The remaining work is **repository reconciliation**, not source study:
- apply the agreed merges/variants/relations;
- retire superseded candidates cleanly;
- validate the reconciled candidate graph;
- review the resulting mature Perspective curriculum before canonical promotion.

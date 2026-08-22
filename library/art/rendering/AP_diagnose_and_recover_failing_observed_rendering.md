---
object_id: AP_diagnose_and_recover_failing_observed_rendering
object_type: ap
name: Diagnose and Recover a Failing Observed Rendering
library_path:
- art
- rendering
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- rendering
- diagnosis
- recovery
- observation
- correction
- comparison
cross_links:
- rel: supports
  target_object_id: PAT_use_perceptual_wrongness_as_inspection_trigger
- rel: supports
  target_object_id: PAT_calibrate_observed_proportion_with_relational_sighting
- rel: supports
  target_object_id: PAT_preview_risky_visual_revision_on_disposable_copy
reference:
  source_title: 'Alla Prima II: Everything I Know About Painting—and More'
  author: Richard Schmid
confidence: high
references: []
variants: []
---

# Diagnose and Recover a Failing Observed Rendering

## Objective
Recover an observed rendering that has begun to fail by identifying the actual source of the failure, routing the correction to the owner that can fix it, and resuming only after the working comparison field is trustworthy again.

## Steps / Flow
1. **Enter on a real perceptual alarm.** Stop speculative editing when a significant passage no longer looks like the active pictorial target or when a known error is beginning to distort later comparisons.
2. **Recover the active target.** Restate what the picture is meant to look like now. If the target deliberately changed, re-baseline it before diagnosing the work; do not diagnose against an obsolete intention.
3. **Triage the failure source.** Separate failures caused by the subject/reference, by working conditions, and by execution. Stabilize or rescope the first two instead of repainting valid image relationships.
4. **Reduce execution failure to concrete visual classes.** Route vague wrongness through `PAT_use_perceptual_wrongness_as_inspection_trigger`; test unsupported additions versus missing essentials, then drawing, value, edge, color, or combinations of them.
5. **Localize before correcting.** Use relational checks, progressive masking/occlusion, mirror/inversion, or another accepted inspection method to find the first relationship that actually breaks.
6. **Delegate the repair.** Invoke the Pattern or subordinate AP that owns the failed decision. Make the smallest sufficient correction rather than experimenting across unrelated passages.
7. **Recheck the whole comparison field.** The repair passes only when the corrected passage agrees with the active target and no longer contaminates judgment of neighboring accepted work.
8. **Resume from the repaired state.** Continue the parent action only after the contaminating error is cleared. If the repair exposes an earlier dependency failure, roll back to that owner instead of painting through it.
9. **Complete recovery explicitly.** Recovery is complete when the cause is concrete, the owning correction has been applied, and whole-image comparison says the work is again on a trustworthy route.

10. **De-risk consequential repairs when needed.** After the cause and intended correction are known, if applying that correction directly threatens substantial accepted work, route through `PAT_preview_risky_visual_revision_on_disposable_copy`; commit the change only after a registered preview proves both the fix and its collateral effects.

## Notes
This protocol coordinates existing observation, comparison, value, color, edge, and drawing owners. It does not make one suspicious feeling into a permanent diagnosis. A wrong passage matters because interdependent image relationships make later comparison less reliable when a significant error is knowingly left in place.

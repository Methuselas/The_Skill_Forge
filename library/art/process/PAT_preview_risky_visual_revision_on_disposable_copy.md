---
object_id: PAT_preview_risky_visual_revision_on_disposable_copy
object_type: pattern
name: Preview Risky Visual Revision on a Disposable Copy
library_path:
- art
- process
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- revision
- prototype
- paintover
- registered_copy
- risk_control
- correction
cross_links:
- rel: supports
  target_object_id: AP_diagnose_and_recover_failing_observed_rendering
reference:
  source_title: 'Alla Prima II: Everything I Know About Painting—and More'
  author: Richard Schmid
confidence: high
references: []
variants: []
---

# Preview Risky Visual Revision on a Disposable Copy

## Pattern Rule
**IF** a proposed visual correction is consequential and the accepted artifact is destructive, expensive, or difficult to reverse
**THEN** test the correction first on a registered duplicate, overlay, proxy, or disposable edit state, identify the smallest successful change, and commit only after the preview proves the correction and its collateral effects
**ELSE** edit the authoritative artifact directly when the change is trivial and reliably reversible.

## Do
- Keep the preview registered to the real artifact so the test measures the actual correction rather than a loosely similar redraw.
- Compare before and after at the same scale and context used to diagnose the problem.
- Test the smallest plausible correction before broader redesign.
- Carry only the proven change back to the authoritative artifact.

## Don't
- Do not regenerate the whole image from a verbal description and call that a revision preview.
- Do not let the disposable copy become an excuse for uncontrolled experimentation once the intended correction is already known.
- Do not commit a preview whose local fix creates larger collateral damage elsewhere.

## Checklist
- The proxy preserves registration with the accepted artifact.
- The proposed correction can be judged independently of unrelated changes.
- Collateral effects have been inspected before commit.
- The authoritative artifact receives no more change than the successful preview demonstrated.

## Notes
The technique is especially useful for late crop, value, color, drawing, edge, and structural corrections. It de-risks a known revision; it does not replace the diagnosis that identifies what should change.

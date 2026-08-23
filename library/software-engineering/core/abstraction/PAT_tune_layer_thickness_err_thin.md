---
object_id: PAT_tune_layer_thickness_err_thin
object_type: pattern
name: Tune Layer Thickness and Err on the Side of Thin
library_path:
- software-engineering
- core
- abstraction
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- abstraction
- granularity
- coupling
- judgment
cross_links:
- rel: related_to
  target_object_id: PAT_size_classes_by_pillars_not_lines
- rel: related_to
  target_object_id: PAT_use_interfaces_for_swappable_layers
- rel: related_to
  target_object_id: PAT_dont_widen_api_for_reuse_or_testing
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Tune Layer Thickness and Err on the Side of Thin

## Pattern Rule
**IF** you are deciding how finely to split code into layers
**THEN** avoid layers so thick that multiple abstractions merge and avoid layers so thin that a single abstraction is dissected into pieces that only ever serve each other — and when genuinely unsure, err toward too-thin, because too-thick causes the worse problems.

## Do
- Spot the too-thin smell: splitting `ParagraphFinder` into `ParagraphStartOffsetDetector` and `ParagraphEndOffsetDetector` behind a shared interface, when no one would ever use one detector without the other because they must share a coherent idea of a paragraph.
- Weigh the real overheads of a split — extra boilerplate and files, effort to switch between classes when following logic, and harder debugging when an interface hides which implementation runs.
- Expect to iterate: even decades-experienced engineers often rework the layering a few times before submitting.

## Don't
- Don't split code just for the sake of it once the costs of another layer exceed its benefits.
- Don't merge multiple abstractions into one thick layer to save files; that yields code that is not modular, reusable, or readable — the worse failure of the two.

## Checklist
- Could each split-out unit plausibly be used without its sibling, or do they only ever serve one parent?
- Have you merged two genuinely distinct abstractions into one unit?
- When unsure, did you lean thin rather than thick?

## Notes
Long frames thickness as a spectrum with failures at both ends and gives an explicit tie-breaker: too-thick problems (merged abstractions, poor modularity and reuse) are generally worse than too-thin ones, so default thin when in doubt. The `OffsetDetector` example shows the thin extreme — technically valid layering that buys nothing because the pieces are inseparable in practice. The honest note that even experts iterate on layering guards against expecting to get it right in one pass.

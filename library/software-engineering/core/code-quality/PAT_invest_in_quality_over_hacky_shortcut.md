---
object_id: PAT_invest_in_quality_over_hacky_shortcut
object_type: pattern
name: Choose the Proper Build Over the Hacky Shortcut
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- technical_debt
- code_quality
- engineering_judgment
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_balance_adaptability_without_predicting_future
- rel: related_to
  target_object_id: AP_refactor_working_code_safely
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Choose the Proper Build Over the Hacky Shortcut

## Pattern Rule
**IF** a quick hacky approach would save time now compared with doing it properly, and the code is anything more than a run-once throwaway
**THEN** do it properly, because the shortcut's mid-to-long-term cost — breakage, rework, and cascading hacks — outweighs the initial saving, like bracket-mounting a shelf instead of gluing it to plaster.
**ELSE** for a small, run-once-then-throw-away utility, take the quick approach.

## Do
- Price the full lifecycle, not just first-write time: the glued shelf saves twenty minutes, then costs hours or days when the plaster cracks or the shelf must come down to redecorate.
- Notice that one hacky choice pushes you toward more hacky choices — painting awkwardly around a shelf you cannot remove instead of taking it down cleanly.

## Don't
- Don't mistake haste for speed; coding the first thing that comes to mind yields a fragile, complicated codebase where every later change fights breakages and re-engineering.
- Don't extend "just hack it" reasoning to code you will maintain for months or years.

## Checklist
- Is this code a genuine run-once throwaway, or will it be maintained?
- Have you priced the rework the shortcut invites, not just the minutes it saves now?
- Will this shortcut force later work to also be done the hacky way?

## Notes
The shelf analogy carries the argument: gluing saves twenty minutes up front, then costs hours or days of replastering when it fails or must be moved, and it drags future redecorating into hackiness too. Long's summary — "less haste, more speed" — answers the question of whether quality slows us down: only in the very short term, and only for genuine throwaways. This is the mindset foundation under all the specific quality techniques.

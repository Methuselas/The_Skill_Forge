---
object_id: PAT_size_classes_by_pillars_not_lines
object_type: pattern
name: Size Classes by the Quality Pillars, Not Line Counts
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
- classes
- cohesion
- separation_of_concerns
- modularity
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Size Classes by the Quality Pillars, Not Line Counts

## Pattern Rule
**IF** you are deciding whether a class is too big or should be split — while authoring it or as it grows over time
**THEN** judge it against the pillars (readable, modular, reusable, testable) rather than a line-count rule of thumb, and split each self-contained subproblem into its own class when the pillars are being violated.

## Do
- Treat line-count rules ("no class over 300 lines") as at most a warning that something might be wrong, never as assurance that a shorter class is fine.
- Use cohesion and separation of concerns as the grouping lens: sequential cohesion (one thing's output feeds another, like grinding then brewing coffee) and functional cohesion (things contributing to one task, like all cake-making tools in one drawer) tell you what genuinely belongs together.
- Run the pillar test on the candidate: the `TextSummarizer` that also splits paragraphs, extracts nouns/verbs/adjectives, and scores importance is hard to read, hard to reconfigure (can't swap the scorer), hard to reuse (can't reuse paragraph-splitting), and hard to test (only the top function is reachable).

## Don't
- Don't accept "this class is only concerned with one thing" at the top level when it internally solves several separable subproblems — the disagreement is settled by the pillars, not by opinion.
- Don't let a class grow organically past the point where it juggles multiple concepts without re-checking it against the pillars.

## Checklist
- Can you name more than one separable subproblem living in this class?
- Would splitting a subproblem out make it independently reusable, swappable, or testable?
- Are you deciding by cohesion and the pillars, not by a raw line count?

## Notes
The `TextSummarizer` walkthrough is the anchor: two engineers can both agree "a class should do one thing" yet disagree on whether its subproblems are separate concerns, and the pillars break the tie objectively. Long emphasizes that the check applies both when writing a class and when modifying one that has bloated over time. The concrete remedy — one class per concept, wired via constructor injection — is developed in the paired refactoring AP and specialized further in chapter 8's dependency-injection material.

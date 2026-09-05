---
object_id: PAT_treat_bad_names_as_a_defect_search_heuristic
object_type: pattern
name: Use Bad Names as a Place to Look for Bugs
library_path:
- software-engineering
- core
- readability
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- defects
- code_review
- static_analysis
cross_links:
- rel: related_to
  target_object_id: PAT_review_names_outside_the_coding_moment
- rel: related_to
  target_object_id: PAT_diagnose_source_of_code_confusion
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: medium
references: []
variants:
- variant_id: VAR_hermans_use_structural_smells_as_the_signal
  variant_name: Use Structural Smells as the Signal Instead of Names
  variant_basis: method_sequence
  difference_from_foundation: The foundation searches on naming flaws detected lexically and structurally in identifiers. This variant searches on Fowler's code smells instead — God classes, God methods, large classes, long methods — which Khomh's analysis of successive Eclipse versions tied to error proneness across every version examined. It also widens what the signal predicts, since the same work found large class and long method significantly raised *change* proneness in more than 75% of Eclipse releases, so smelly code is both likelier to be wrong and likelier to move.
  when_to_use: Use where a smell detector or static analyser is already in the pipeline, since these smells are cheaper to detect mechanically than naming quality, and use it when planning refactoring effort rather than only defect hunting — the change-proneness result speaks directly to where future work will land.
  when_not_to_use: Do not use it on code whose structure is dictated by a framework or generator, where the smell is an artefact of the tool and predicts nothing about the authors. It is also the wrong signal in a codebase already structurally uniform, where names remain the only varying quality dimension.
  absorbed_from_object_id: none
---

# Use Bad Names as a Place to Look for Bugs

## Pattern Rule
**IF** you are deciding where to spend limited review or testing attention in an unfamiliar codebase
**THEN** use locations with poor naming as a search heuristic, because naming flaws and defects co-occur — while treating the improvement as a comprehension gain rather than a fix.

## Do
- Use it to direct attention, which is the claim the evidence actually supports. Butler's 2009 study of Java repositories including Tomcat and Hibernate found statistically significant associations between naming issues and code quality, comparing bad-name locations against defects flagged by FindBugs.
- Take seriously that this may be more than readability. Butler's findings suggest a bad naming style might point to code likely to be *wrong*, not merely code that is hard to read, understand and maintain.
- Expect the benefit through the indirect route as well — better names make code easier to comprehend, which shortens fix times even where no bug was hiding.
- Combine it with the mechanisms that plausibly explain the correlation: high cognitive load while writing, and genuinely complex domains where a good name is hard to find.

## Don't
- Don't read causation into it. Hermans is explicit that the correlation does not imply the bad names caused the bugs, and the alternative explanations are all live — a novice or sloppy author producing both, or a location where genuinely complex problems are being solved.
- Don't expect renaming to fix defects. Addressing naming issues is not necessarily going to solve or prevent bugs; the value here is where you look, not what renaming accomplishes.
- Don't apply it as a quality metric or a gate. It is a heuristic for allocating attention, and hardening it into a threshold overstates what the study shows.

## Checklist
- Where in this change or codebase are the naming flaws concentrated?
- Have I looked at those locations for defects specifically, rather than just tidying the names?
- Am I claiming the names caused a problem, or that they marked a place worth checking?

## Notes
Confidence on this card is `medium` rather than `high`, which is deliberate. The correlation is real and statistically significant, but most of the discussion is about why the causal reading is unavailable, and the pattern is only as strong as the weaker claim.

`VAR_hermans_use_structural_smells_as_the_signal` retains **Use Structural Smells as the Signal Instead of Names** for the case where structure, not naming, is what you can measure. Khomh's study of successive Eclipse versions found God classes a significant contributor to error proneness in every version analysed and God methods in one, which is a stronger and more specific result than the naming correlation this foundation rests on. It also extends the payoff beyond defects: large class and long method significantly raised change proneness in more than 75% of releases, so the same signal predicts where future edits will concentrate. Reach for it when a smell detector is already running, or when allocating refactoring rather than review effort; skip it where structure is generated or already uniform, since the signal then carries no information about the authors.

Butler's method is worth knowing because it bounds what "bad name" means here. His tool extracted names from Java code and flagged violations of his own naming guidelines — both structural issues such as consecutive underscores, and lexical ones such as whether the components appear in a dictionary. So the correlation is with mechanically detectable naming flaws, not with names a human would judge unhelpful, and the heuristic transfers best when applied the same way.

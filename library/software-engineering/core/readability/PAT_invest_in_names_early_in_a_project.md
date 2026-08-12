---
object_id: PAT_invest_in_names_early_in_a_project
object_type: pattern
name: Spend Your Naming Effort at the Start of a Project
library_path:
- software-engineering
- core
- readability
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- readability
- conventions
- project_setup
cross_links:
- rel: related_to
  target_object_id: PAT_agree_on_a_small_set_of_name_molds
- rel: related_to
  target_object_id: PAT_follow_a_consistent_coding_style
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u08, pp. 131-132
  evidence_type: text
confidence: high
references: []
variants: []
---

# Spend Your Naming Effort at the Start of a Project

## Pattern Rule
**IF** you are setting up a new codebase
**THEN** treat the first names you write as the ones that will set the standard permanently, because naming quality is established early and does not improve on its own as a codebase ages.

## Do
- Front-load the effort. Lawrie's conclusion from analysing 186 versions of 78 codebases is that identifier quality takes hold early in a program's development, so the way names are formed in the first weeks is likely how they will be formed for the project's life.
- Write the conventions down and put an example of each in the codebase early, because new contributors copy what they find rather than what is documented.
- Expect imitation to be the mechanism. Research on GitHub found new contributors look at existing tests and modify them rather than reading project guidelines — when tests exist, newcomers feel obliged to add them and comply with how the project is organized. Names work the same way.
- If you are joining an existing project instead, read the prevailing convention before adding to it; your instinct to improve one name locally is what produces inconsistency.

## Don't
- Don't assume names will be cleaned up later. Lawrie looked specifically at successive versions of the same codebase and found naming does not improve as the code gets older.
- Don't expect project size to protect you. Codebase size showed no correlation with naming quality, so a large project is not automatically better disciplined and a small one is not automatically fine.
- Don't confuse the industry trend with your project's trajectory. Modern code does use dictionary words and split words more than older code — Lawrie attributes that to programming maturing as a discipline — but that improvement happens across projects, not within one.

## Checklist
- Is this a new codebase, and have I decided the naming conventions before there is much code to be consistent with?
- Would a new contributor copying the nearest existing name arrive at something I would endorse?
- Am I relying on a future cleanup that the evidence says does not happen?

## Notes
The study behind this is unusually broad: 186 versions of 78 codebases in C++, C, Fortran and Java, over 48 million lines, spanning three decades, mixing proprietary and open source and including Apache, Eclipse, MySQL, gcc and Samba. Lawrie assessed two things — whether names split their words, via underscores or capitals, and whether the words appear in a dictionary.

Two of her three findings are descriptive and one is actionable. Modern code follows naming guidelines better than old code; codebase size does not predict naming quality; and within a single codebase naming practices stay constant. Only the third one tells you when to spend effort, and it is the reason this is a pattern about timing rather than about names themselves.

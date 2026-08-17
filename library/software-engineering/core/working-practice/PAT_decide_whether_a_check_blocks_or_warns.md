---
object_id: PAT_decide_whether_a_check_blocks_or_warns
object_type: pattern
name: Decide Which Automated Checks Earn the Right to Block
library_path:
- software-engineering
- core
- working-practice
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- build
- automation
- review
- discipline
- feedback
cross_links:
- rel: related_to
  target_object_id: PAT_keep_the_build_green_with_an_automated_smoke_test
- rel: related_to
  target_object_id: PAT_keep_unit_tests_fast_to_run
- rel: related_to
  target_object_id: PAT_enforce_a_new_rule_only_on_new_code
- rel: related_to
  target_object_id: PAT_judge_change_risk_by_what_it_can_break
reference:
  source_title: 'Refactoring at Scale: Regaining Control of Your Codebase'
  author: Maude Lemaire
confidence: high
references: []
variants: []
---

# Decide Which Automated Checks Earn the Right to Block

## Pattern Rule
**IF** you are adding an automated check to the path between writing a change and landing it
**THEN** decide deliberately whether a failure stops the change or merely tells its author something, and default to telling unless the failure is one that must never reach production
**ELSE** where a check is too slow or too unreliable to be trusted in either role, fix it or remove it rather than leaving it in the path producing noise.

## Do
- Sort the checks you already have into the two categories and count how many are in the blocking one. Teams arrive at ten blockers by adding each one individually, and nobody ever reviews the total, which is the number that determines how long a change takes to land.
- Reserve blocking for failures whose escape is genuinely worse than the delay. Something that corrupts data, breaks the build for everyone, or ships a security hole belongs there; a style deviation or a complexity threshold does not.
- Move anything intermittently wrong out of the blocking set immediately. A check that fails on correct work teaches everyone to rerun it without reading it, and once that habit exists the check is no longer detecting anything even when it is right.
- Weigh the wall-clock cost against what the check catches. A suite taking ten minutes to find something a reviewer would have caught anyway is worse than not having it, and the cost is paid on every change rather than on the ones with problems.
- Make an advisory failure legible enough to act on. The whole value rests on the author reading it and deciding, so it needs to say what happened and why it might matter, and it needs to be visible rather than buried in output nobody opens.
- Accept the trade explicitly. Fewer blockers means more escapes, and the position worth defending is that the aggregate cost of waiting exceeds the aggregate cost of the failures that slip past — which is a judgement about your codebase, not a universal truth.

## Don't
- Don't add a blocker because a bad thing happened once. That is how the set grows to a size nobody chose, each addition individually reasonable and the total unaffordable.
- Don't leave a threshold measurement in the blocking set. Numbers of that kind identify code worth a look and do not distinguish a routine that should be split from one that is legitimately long, so enforcing them mechanically produces work split at arbitrary points to satisfy the number.
- Don't treat a passing set of checks as a verdict on the change. They check what they were built to check, and the categories of failure they cannot see are the ones that needed a person.
- Don't respond to escapes by promoting everything back to blocking. The failure that got through usually points at one specific missing check rather than at the principle.

## Checklist
- How many checks currently block, and when did anyone last look at that number?
- For each blocker: what happens if this failure reaches production?
- Which of these have failed on correct work in the last month?
- How long does a change wait, and what fraction of that wait is finding real problems?
- Would an author reading an advisory failure know what to do about it?

## Notes
The choice is usually never made. Checks arrive one at a time, each justified on its own, and blocking is the default because it feels like the responsible setting — so the set accumulates until every change carries the full weight of every concern anyone has ever had. The number that matters is not whether any given check is worth having, which is nearly always yes, but what the whole set costs on every change, which nobody is looking at.

Unreliable checks deserve separate treatment because they fail in a way that quietly disables the surrounding discipline. A blocker that is right most of the time trains people to rerun on failure rather than investigate, and that response cannot distinguish the intermittent case from the genuine one. The check keeps reporting and stops being read, which is worse than absence — absence at least leaves everyone aware of the gap. Moving it out of the blocking set restores the honest position: it is information, and information is what it was always providing.

The trade is real and should not be presented as free. Loosening enforcement does let more defects reach production, and the argument for doing it rests on the aggregate rather than on any single case. Time spent waiting on checks is spent on every change including the overwhelming majority that were fine, while the cost of an escape falls on the small number that were not. Where the escape is cheap to detect and cheap to reverse, the arithmetic favours waiting less. Where it is neither, it does not, which is why this is a decision to make per check rather than a policy to adopt.

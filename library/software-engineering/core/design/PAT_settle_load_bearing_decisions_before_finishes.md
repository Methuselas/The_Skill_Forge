---
object_id: PAT_settle_load_bearing_decisions_before_finishes
object_type: pattern
name: Settle the Load-Bearing Decisions Early, Leave the Finishes Open
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- planning
- sequencing
- cost_of_change
- construction
cross_links:
- rel: related_to
  target_object_id: AP_grow_a_system_from_a_running_skeleton
- rel: related_to
  target_object_id: PAT_balance_adaptability_without_predicting_future
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u02, pp. 14, 18-19
  evidence_type: text
confidence: high
references: []
variants: []
---

# Settle the Load-Bearing Decisions Early, Leave the Finishes Open

## Pattern Rule
**IF** you are deciding how much to work out before writing code, and how much to leave open
**THEN** sort the decisions by what they cost to reverse — settle the ones other code will sit on, and deliberately defer the ones that stay cheap to change.
**ELSE** when you cannot yet tell which a decision is, ask what else would have to move if you changed it later; anything that forces other code to move is load-bearing.

## Do
- Ask of each decision what has to change if you reverse it. Moving a wall costs more when it is load-bearing than when it is a partition between rooms, and the same split runs through code: structural changes cost more than adding or deleting peripheral features.
- Name the things you are explicitly leaving open. Deciding later which storage backend, which output format, which colour — these are the hardwood-or-carpet decisions, and stating them as deferred is different from not having noticed them.
- Use experience to shrink the list. The more of this kind of system you have built, the more details you can safely take for granted and the shorter the up-front list gets.
- Set the depth by one test: plan enough that lack of planning does not create major problems later. Not more than that.
- When you do want to explore alternatives, take the chances while they are cheapest — early, on small pieces — rather than banking on a full rewrite later.

## Don't
- Don't read "plan the structure" as plan everything. Exhaustive planning and over-planning are their own failure, not a safer version of the right amount.
- Don't accept "plan to throw one away" as a strategy. Discarding a whole first attempt is affordable on a letter and not on a system that costs what a ten-story office building costs; the aim is to get it the first time around, or to take several cheap chances early.
- Don't leave the build order to chance. Building software in the wrong order makes it hard to code, hard to test, and hard to debug, and on a team it can pull the project apart because everyone's work is too complex to combine.
- Don't assume good planning locks you in. A well-planned project *improves* your ability to change your mind later about details, because the details were never load-bearing to begin with.

## Checklist
- For each decision you are making now: what else would have to move if it were reversed?
- Which decisions have you deliberately deferred, and can you name them?
- Is the build order chosen, or is it whatever came to hand first?
- Are you planning past the point where the absence of a plan would cause a problem?

## Notes
The pressure this resists runs in both directions, which is why sorting by reversal cost beats picking a planning depth. Under-plan and the structural mistakes surface once code is already sitting on them. Over-plan and you spend the effort on decisions that were never going to be expensive, while acquiring a false sense that the plan settles things it does not.

Two numbers set the stakes. Construction can account for as much as 65 percent of total project costs, so an order that makes code hard to write and debug is expensive over a large base. And as much as 90 percent of the development effort on a typical software system comes after its initial release, with two-thirds being typical — which is the real argument for keeping the finishes open. Most of the changes are still ahead of you when you ship.

Size changes the calculation rather than the rule. If a thousand lines turn out to use the wrong design, refactoring or starting over costs little. At the other end, a system of a million lines can carry 69 kinds of documentation with a requirements specification running to four or five thousand pages and design documentation two or three times that — nobody reads the whole design, so the structural decisions have to be right before the code arrives. Judge which end you are nearer before choosing how much to settle.

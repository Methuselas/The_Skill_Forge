---
object_id: PAT_remove_the_scaffolding_a_migration_leaves
object_type: pattern
name: Treat the Transition's Leftovers as Part of the Work
library_path:
- software-engineering
- core
- refactoring
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- refactoring
- maintenance
- dead_code
- cleanup
- technical_debt
cross_links:
- rel: related_to
  target_object_id: PAT_prove_behaviour_held_by_running_both_paths
- rel: related_to
  target_object_id: PAT_make_every_milestone_a_place_you_could_stop
- rel: related_to
  target_object_id: PAT_fix_or_board_up_a_broken_window
- rel: related_to
  target_object_id: AP_replace_a_system_that_is_still_in_use
reference:
  source_title: 'Refactoring at Scale: Regaining Control of Your Codebase'
  author: Maude Lemaire
confidence: high
references: []
variants: []
---

# Treat the Transition's Leftovers as Part of the Work

## Pattern Rule
**IF** a change has reached the point where the new implementation is carrying the traffic and the work feels finished
**THEN** find and delete everything that existed only to get you here — the conditional switches, the wrapper that hid the transition, the superseded implementation, the notes warning readers about it, and the tests that duplicate coverage the new path already has
**ELSE** where something must survive because a consumer still depends on it, write down what has to change before it can go, and treat that as an outstanding step rather than a completed one.

## Do
- Mark each piece of temporary machinery at the moment you create it, using one searchable string chosen for this effort. Finding the leftovers at the end becomes a search rather than an act of memory, and memory is what fails after several months and several people.
- Delete the switch before deleting the superseded implementation, and delete the superseded implementation only after the new one has carried real traffic for long enough to have met the load you were worried about.
- Strip the wrapper you introduced to hide the transition. Where it still holds logic worth keeping, rewrite it so that a future reader has no reason to suspect it was ever a seam — a surviving wrapper whose only remaining purpose is historical reads as deliberate design and gets preserved by people who assume it means something.
- Remove the notes you left for readers during the change. Warnings about code in flux, reminders to come back, and markers describing what was about to be deleted all outlive their accuracy immediately and mislead precisely the reader who trusts them.
- Prune the tests written alongside the old ones to prove the two agreed. Once only one implementation remains, coverage that exercised the comparison is duplicated work slowing every run.
- Give each switch an owner and a date when you add it, and go back to those people when the dates pass. Without both, nobody can tell whether an old conditional is dormant or load-bearing, and the safe assumption is always to leave it.
- Sequence the final teardown behind the consumers you do not control. Downstream readers of the old data have to be moved first; only then can the thing they were reading be dropped.

## Don't
- Don't judge the cost by one leftover. A single dormant conditional is genuinely harmless, and the reasoning that follows from that observation is how a codebase acquires hundreds of them — at which point evaluating them measurably consumes production time on every request.
- Don't leave a superseded path in place on the grounds that it might be needed. Version history holds it, and code kept for reassurance gets read, maintained, and eventually modified by someone who thinks it is live.
- Don't let the last ten percent become somebody's someday task. The people who understand what each piece was for are the ones finishing the work, and that understanding is gone within a quarter of them moving on.
- Don't treat the removal as separate from the change that created the need for it. Budgeted separately, it competes against new work and loses every time.

## Checklist
- What did you introduce solely to make this transition possible, and where is the list?
- Does a search for the chosen marker return zero results?
- Has the superseded implementation been deleted, or only stopped being called?
- Are there tests still asserting agreement between two things when only one remains?
- Which consumers outside your control still read from the thing you want to drop?
- Would a new reader of this code guess that a transition ever happened here?

## Notes
The reason this needs stating at all is that the incentives all point the other way at exactly the moment it matters. The hard part is over, the metrics have moved, the risk has passed, and what remains is unglamorous deletion with no visible payoff. Every individual leftover is defensible in isolation — one flag costs nothing, one dead branch harms no one, one stale note is easily ignored — and the aggregate is a codebase where a meaningful share of every request is spent evaluating conditions whose answers were settled years ago, and where readers routinely spend time working out that a piece of code is inert.

The marker discipline is the part that actually determines whether any of this happens, because it converts an act of recall into a query. Over a long change the machinery accumulates gradually and each addition feels too small to record, so at the end there is no list — only whoever remembers, and they remember the interesting pieces rather than the trivial ones. One agreed string, applied from the first commit, means the final sweep is mechanical and complete instead of thorough-feeling and partial.

There is a specific cost worth separating from the general one, because it falls on people who never touched the change. A leftover switch does not merely sit there — it makes a reader consider both of its branches. Someone modifying that region has to work out whether the condition is live, discover that it has been fully enabled for a year, and only then make their change. Multiply that by every reader and every leftover and the bill is paid in other people's attention, which is the resource the whole effort was supposed to be conserving.

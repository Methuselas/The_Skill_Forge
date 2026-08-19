---
object_id: AP_replace_a_system_that_is_still_in_use
object_type: ap
name: Replace a System That Is Still in Use
library_path:
- software-engineering
- core
- refactoring
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- migration
- deprecation
- refactoring
- rollout
- risk
cross_links:
- rel: related_to
  target_object_id: PAT_tell_obsolete_from_merely_old
- rel: related_to
  target_object_id: PAT_diagnose_why_the_code_degraded_before_changing_it
- rel: related_to
  target_object_id: PAT_look_for_the_evidence_outside_the_code
- rel: related_to
  target_object_id: PAT_concentrate_effort_where_defects_concentrate
- rel: related_to
  target_object_id: PAT_make_every_milestone_a_place_you_could_stop
- rel: related_to
  target_object_id: PAT_enforce_a_new_rule_only_on_new_code
- rel: related_to
  target_object_id: PAT_prove_behaviour_held_by_running_both_paths
- rel: related_to
  target_object_id: PAT_separate_structural_change_from_behavioural_change
- rel: related_to
  target_object_id: PAT_a_warning_migrates_nobody
- rel: related_to
  target_object_id: PAT_remove_the_scaffolding_a_migration_leaves
- rel: related_to
  target_object_id: PAT_judge_change_risk_by_what_it_can_break
- rel: related_to
  target_object_id: PAT_plan_the_removal_while_you_build
reference:
  source_title: 'Refactoring at Scale, and Software Engineering at Google'
  author: Maude Lemaire; Titus Winters, Tom Manshreck, and Hyrum Wright
confidence: high
references: []
variants: []
---

# Replace a System That Is Still in Use

## Objective

Move a body of live, depended-upon code onto a replacement and remove the original, without a cutover, without a period in which nobody can tell which implementation is authoritative, and without discovering at the end that the improvement cannot be demonstrated.

Every decision this coordinates is owned elsewhere and stated once. What this procedure owns is the order — what has to be established before anything is built, what has to be true before each advance, where retreat stops being available, and what condition means the work is finished rather than merely deployed.

Reach for it when the thing being replaced has callers you do not control or cannot change in one change set. Where the whole surface fits in a single reviewable change, this is far too much machinery and the ordinary safe-refactoring procedure is the right tool.

## Steps / Flow

1. **Establish that it is obsolete rather than old, and that a replacement covers the ground.** Age is not evidence. Name what is wrong that is not the date, and confirm the replacement handles every existing use rather than every use you have looked at.

   *Gate.* Do not proceed without a replacement that covers the hard remainder. Beginning with the awkward ten percent unexamined is how a system ends up permanently half-retired, carrying both implementations forever.

2. **Work out how it got this way before deciding what to build.** Whether the demands moved or corners were cut determines what the replacement must preserve, and the constraints the original was quietly handling are the things a clean rewrite drops silently and rediscovers expensively.

3. **Baseline what you intend to improve, before touching anything.** A successful replacement is invisible in the metrics you already watch, so choose measures that capture the specific problem and record them now. Evidence outside the code — incident histories, question threads, change frequency — is where the cost of the current state is actually visible.

4. **Divide the work into milestones that are each a defensible place to stop.** Not steps sized to the calendar: states a stranger could read, extend, and ship from. Priorities move and people leave, and the division that survives suspension is the one designed expecting it.

   *Invariant, holding from here to the end.* The system stays shippable at every milestone boundary, and no milestone leaves two implementations both looking authoritative.

5. **Freeze new uses of the old path immediately.** Enforce it on changed code only, so the count of remaining callers can fall without anyone being asked to fix code they did not come to fix. Until the denominator stops growing, the migration has no end.

   *Gate.* Notices alone do not migrate anyone. If nothing mechanically blocks new uses, expect the old path to keep collecting callers regardless of what has been announced, and treat the migration as not yet started.

6. **For each milestone, build the replacement beside the original and let the original's entry point choose between them.** Keep structural change separate from behavioural change throughout. If a step both moves code and alters what callers observe, a failure afterwards cannot tell you which half caused it, and that is the information the whole procedure exists to preserve.

7. **Verify by running both and comparing, not by reasoning.** Execute both paths on live traffic, return the old answer, and log the differences. Sample rather than comparing every call, and raise the sample rate in steps — old code produces far more differences than anyone predicts, and the logging is what falls over first.

   *Gate.* Do not begin returning the new answer while differences remain unexplained. The target is a residue you can account for and confirm, not a count of zero.

   *Recovery.* Where a difference resists explanation, it belongs back at step 2. An unexplained divergence usually means the original was handling something nobody recorded, and that is knowledge to recover rather than a defect to suppress.

8. **Ramp the new answer outward in order of increasing risk**, scaling the care to what each step can reach rather than to how large it looks. Comparison coverage is proportional to traffic, so rarely-executed paths were never certified by step 7 and will be met for the first time here. Sequence the ramp so the first encounter is survivable.

9. **Name the point where retreat ends, and say so out loud.** While both paths execute, retreating is a configuration change. Once the original is no longer being kept current, retreat means reconstructing state. Teams get hurt here by assuming the whole sequence is uniformly reversible when reversibility stops at one identifiable step.

10. **Remove the scaffolding, then the original.** The switch, the wrapper, the duplicated tests, the notes left for readers, and finally the superseded implementation itself. Downstream consumers you do not control come off it before it can be dropped.

    *Completion.* The action is finished when nothing references the old path, a search for the migration's marker returns nothing, and the measure baselined at step 3 has moved. Deployment of the replacement is not completion — it is the point at which the remaining work becomes easy to abandon.

## Notes

The standing objection to work of this size is that a large restructuring is a recipe for disaster, and the objection is right about the thing it describes: one long effort, held together by one person's understanding, with no defensible state anywhere in the middle. This procedure does not argue with that. It removes the premise, by requiring that the code be shippable at every join and that the old path stop accumulating callers before anything else begins. Once both hold, the total size stops being the risk it looked like, because nobody is ever carrying more than one milestone's worth of unfinished work.

The ordering of the first three steps is the part most often skipped and the most expensive to skip. Establishing obsolescence, understanding the degradation, and baselining the metrics all happen before any code is written, and all three feel like delay. They are what prevent the three characteristic failures of this work: replacing something that did not need replacing, rebuilding it without the constraints it was quietly satisfying, and finishing with no way to show the result was worth the effort.

Step 5 does more than its position suggests. Migrations do not usually fail because the replacement was inadequate; they fail because the old path kept gathering new callers faster than the existing ones could be moved, so the remaining work never shrank. Blocking new uses mechanically converts an open-ended effort into one with a falling number and a visible end, and it is worth doing before the replacement is even complete, because the thing being frozen is the denominator rather than the design.

The relationship between steps 7 and 8 carries the residual risk and is worth stating plainly. Differential comparison is the strongest verification available here, and its coverage is distributed exactly as traffic is distributed: hot paths get certified thoroughly and rare ones not at all. That is not a flaw to be fixed but a property to be planned around, which is why the ramp is ordered by risk rather than by convenience. The paths the comparison could not reach are met in an order where the first encounter is recoverable.

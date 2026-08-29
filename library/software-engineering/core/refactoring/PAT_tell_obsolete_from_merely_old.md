---
object_id: PAT_tell_obsolete_from_merely_old
object_type: pattern
name: Tell Obsolete From Merely Old
library_path:
- software-engineering
- core
- refactoring
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- deprecation
- maintenance
- dead_code
- migration
- technical_debt
cross_links:
- rel: related_to
  target_object_id: PAT_plan_the_removal_while_you_build
- rel: related_to
  target_object_id: PAT_a_warning_migrates_nobody
- rel: related_to
  target_object_id: PAT_diagnose_why_the_code_degraded_before_changing_it
- rel: related_to
  target_object_id: PAT_remove_the_scaffolding_a_migration_leaves
- rel: related_to
  target_object_id: AP_replace_a_system_that_is_still_in_use
reference:
  source_title: 'Software Engineering at Google: Lessons Learned from Programming Over Time'
  author: Titus Winters, Tom Manshreck, and Hyrum Wright
confidence: high
references: []
variants: []
---

# Tell Obsolete From Merely Old

## Pattern Rule
**IF** you are considering retiring a system, module, or interface because it feels past its time
**THEN** establish that something else already does its job at least as well before committing to remove it, and treat age on its own as no evidence at all
**ELSE** where no replacement exists yet, what you have is an argument for building one, and the removal is a separate decision to make once it does.

## Do
- Ask what specifically is wrong beyond the date. Resource cost, a security posture you cannot fix, an inability to keep up with what it sits on, a defect rate nobody can bring down — each of those is a reason. Having been written a long time ago is not one; plenty of code is finished.
- Confirm the replacement covers the ground before starting the retirement, not during it. A replacement that is merely close leaves the last few consumers stranded and turns a removal into an indefinite coexistence.
- Count the cost of running both, because it is larger than it looks. Two systems doing one job need translation between them, drift apart, and acquire dependencies on each other that make either one harder to remove later.
- Recognise the cost that nobody budgets: while the old one survives, the new one has to stay compatible with it. The replacement's ability to evolve is held hostage by the thing it replaced, so the removal is what unlocks the value the replacement was built for.
- Accept that the replacement will not match one-to-one. If it did, there would be no reason to move. That difference means every existing use has to be looked at in terms of the new thing rather than mechanically translated.
- Prefer evolving what exists over replacing it wholesale where the option is real. Wholesale replacement is consistently more expensive than estimated, and reshaping in place delivers value along the way instead of at the end.
- Limit how many retirements are in flight at once. Each one imposes work on people who did not ask for it, and running them all simultaneously means nothing finishes.

## Don't
- Don't argue from the age of the code. It is the most available reason and the least informative one.
- Don't begin a removal you are not prepared to finish. A retirement abandoned partway leaves both systems standing plus the migration apparatus between them, which is worse than either endpoint.
- Don't keep something because of who wrote it or how much went into it. That attachment is real and it is not a technical input; history keeps the code retrievable, which is what the attachment is usually protecting.
- Don't mistake a stable, unchanging system for a stagnant one. Software that has stopped needing changes may simply be complete.

## Checklist
- What is wrong with this that is not its age?
- Does the replacement cover every use, or every use you have looked at?
- What does running both cost per year, including the translation between them?
- What is the newer system unable to do while the older one still exists?
- Is wholesale replacement genuinely cheaper here than reshaping what you have?
- How many other retirements are already underway, and who is absorbing that work?

## Notes
The framing that makes this decidable is that code is a cost rather than a holding. What has value is the functionality delivered; the code is only the means, and the same functionality in less of it is strictly better. Read that way, a system that has been superseded is pure carrying cost — operational resources, attention, and the continual work of keeping it current with everything underneath it — and removing it is a gain rather than a loss of assets. It also explains why the instinct to preserve is so strong and so misleading: the effort that went in is visible, and the ongoing cost of leaving it standing is not.

The compatibility drag is the argument most often missing when this gets discussed, and it is usually the largest number. As long as both systems are live, the replacement cannot move away from the shape of the thing it replaced — interfaces stay aligned, data formats stay convertible, behaviours stay bug-compatible. Every improvement the new system was supposed to enable is deferred until the old one is gone. So the retirement is not the tidying-up phase after the real work; it is the step that lets the real work pay off.

The last consumers are where these efforts actually die, and the reason is structural rather than a failure of will. A replacement is never a precise match, so each remaining use needs individual thought, and the uses that survive longest are the ones nobody understands well enough to move quickly. That is what makes verifying the replacement's coverage a precondition rather than a formality — starting a removal with the hardest ten percent unexamined is how a system ends up permanently half-retired.

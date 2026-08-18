---
object_id: PAT_a_warning_migrates_nobody
object_type: pattern
name: A Deprecation Warning Migrates Nobody
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
- deprecation
- migration
- dead_code
- maintenance
- dependencies
cross_links:
- rel: related_to
  target_object_id: PAT_tell_obsolete_from_merely_old
- rel: related_to
  target_object_id: PAT_plan_the_removal_while_you_build
- rel: related_to
  target_object_id: PAT_enforce_a_new_rule_only_on_new_code
- rel: related_to
  target_object_id: PAT_remove_the_scaffolding_a_migration_leaves
reference:
  source_title: 'Software Engineering at Google: Lessons Learned from Programming Over Time'
  author: Titus Winters, Tom Manshreck, and Hyrum Wright
confidence: high
references: []
variants: []
---

# A Deprecation Warning Migrates Nobody

## Pattern Rule
**IF** you have marked something as deprecated and are waiting for its remaining uses to go away
**THEN** decide whether you are advertising a better option or actually removing this, because the first needs no deadline and achieves no migration, and the second needs a date and somebody doing the work
**ELSE** where you are unwilling to fund either, say the old thing is supported and stop calling it deprecated — a permanent warning trains everyone to ignore warnings.

## Do
- Separate the two things a notice can be for. Advertising a replacement is worth doing on its own: it slows the arrival of new uses and draws people who would benefit. Clearing existing uses is different work, and no amount of notice accomplishes it.
- Expect advertising to attract adopters only when the improvement is large. People will not move for marginal benefit, and the honest question is whether the replacement is transformative enough for anyone to volunteer.
- Attach the check to new and changed code, so the old form stops spreading while you deal with what exists. Freezing the number of uses is what turns an open-ended migration into a finite one.
- Give a real removal a date and treat it as real. A deadline nobody will act on is indistinguishable from no deadline, and consumers correctly read it that way.
- Expect the existing uses to pull new work toward them. Whatever is already widespread will keep picking up new callers, because it is what people find, what the examples show, and what the surrounding code already does — regardless of what the notice says.
- Find the dependents you do not know about by removing the thing briefly rather than by asking. Short scheduled outages, announced in advance and lengthening as the date nears, surface consumers no analysis found; renaming an internal symbol reveals who was reaching past the interface.
- Concentrate the migration knowledge in whoever is doing the removal. The tenth consumer is far cheaper to move than the first, and only if the same people move both and keep what they learn.

## Don't
- Don't mark something deprecated and walk away. It is the cheapest possible action and it produces almost nothing except a warning everyone learns to skip.
- Don't let notices accumulate. A codebase that emits warnings nobody acts on has trained its readers that warnings are noise, which costs you the next one that mattered.
- Don't demand a migration you are not resourcing. Telling people to move, with a date, while offering nothing to move them with, reads as work pushed onto teams who did not choose it — and it is the reliable way to have the deadline ignored.
- Don't assume static analysis found every dependent. It finds the ones that reference you the way you expected; the interesting ones do something else.

## Checklist
- Is this an advertisement or a removal, and does the funding match the answer?
- Is the replacement enough better that anyone would move without being made to?
- What stops new uses appearing while the existing ones are being cleared?
- If there is a date, what happens on it — and does anyone believe that?
- How will you find consumers that no search has revealed?
- Who is doing the migration work, and are they the same people each time?

## Notes
The uncomfortable finding is how weak a notice is on its own. Marking something deprecated does measurably reduce the rate at which fresh uses appear, which makes it feel like it is working. It does close to nothing about the uses already there, and those are the ones blocking the removal. So the effort produces a visible signal, a plausible sense of progress, and a system that is exactly as un-removable as it was — which is why so many things sit marked as deprecated for years.

The pull that existing uses exert is the mechanism worth understanding, because it is not laziness. Somebody writing new code looks at what the codebase already does, copies the nearest working example, and reaches for the thing that appears everywhere. All of those instincts point at the old system precisely because it is entrenched, and none of them involve reading a notice attached to a declaration. That is why blocking new uses mechanically does more than any amount of communication.

Removal as a discovery method is the counterintuitive technique here and it is more reliable than analysis. The dependents that matter are the ones nobody knew about, and they are unknown precisely because they do not show up in the searches that would find them — they arrive through a layer of indirection, or a configuration string, or a reflective call, or a behaviour that was never part of the interface. Turning the thing off briefly, on an announced schedule, makes those consumers identify themselves while there is still time for everyone to react. It converts an unknown into a dated, bounded problem, which is the same move as any other deliberate experiment run to find out what is really connected to what.

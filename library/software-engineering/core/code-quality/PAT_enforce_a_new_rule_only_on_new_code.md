---
object_id: PAT_enforce_a_new_rule_only_on_new_code
object_type: pattern
name: Apply a New Standard Forward, Not Retroactively
library_path:
- software-engineering
- core
- code-quality
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- maintenance
- deprecation
- automation
- migration
cross_links:
- rel: related_to
  target_object_id: PAT_decide_whether_a_check_blocks_or_warns
- rel: related_to
  target_object_id: PAT_remove_the_scaffolding_a_migration_leaves
- rel: related_to
  target_object_id: PAT_follow_a_consistent_coding_style
reference:
  source_title: 'Refactoring at Scale: Regaining Control of Your Codebase'
  author: Maude Lemaire
confidence: high
references: []
variants: []
---

# Apply a New Standard Forward, Not Retroactively

## Pattern Rule
**IF** you want a rule to hold across a codebase that currently violates it in more places than anyone can fix at once
**THEN** run the check against changed lines only, so that every edit converges the code a little and no one is asked to fix code they did not come to fix
**ELSE** where the violation is unsafe rather than merely undesirable, the existing instances are a defect list and deserve to be worked through directly rather than left to attrition.

## Do
- Scope the check to the difference under review, or failing that to the files a change touches. Both are cheap to arrange and both produce the same effect — the rule binds whoever is already reading that code.
- Reach for this specifically when retiring one construct in favour of another. Blocking new uses while tolerating existing ones is what stops the old form spreading, and spread is what turns a bounded migration into an unbounded one.
- Put the reason and the replacement in the message the check emits. Someone stopped by an unfamiliar rule should be able to act on it without opening anything else, and a message that only names the violation guarantees a search.
- Announce the rule and its start date before it starts failing anything. An unexpected failure on unrelated work reads as an obstruction regardless of how good the rule is, and the reaction attaches to the rule permanently.
- Track the count of remaining violations as the measure of the migration. It moves in one direction without anyone scheduling it, and it makes the finishing line visible.
- Handle the last stubborn instances deliberately rather than waiting for attrition. Code nobody edits never converges, so the tail is a small explicit task rather than a failure of the method.

## Don't
- Don't switch the rule on everywhere and expect anyone to absorb the result. Thousands of failures across code that was working fine yesterday cannot be triaged, and the reliable outcome is that the whole check gets disabled.
- Don't use this for something genuinely dangerous. A security flaw or a correctness trap is not improved by being allowed to persist wherever it already exists, and gradual convergence is the wrong shape for a problem that is bad now.
- Don't leave the rule advisory forever once new violations have stopped appearing. At that point it costs almost nothing to enforce properly, and leaving it soft invites the old form back the moment attention moves.
- Don't let the mechanism substitute for telling people what changed. Automated enforcement is good at stopping things and bad at explaining them, and a rule nobody understands gets worked around rather than followed.

## Checklist
- Is the check running against the whole file, the changed files, or the changed lines?
- Can someone who has never seen this rule fix a violation from the message alone?
- Did anyone hear about this before their work started failing?
- How many violations remain, and is the number falling?
- Is anything being tolerated by this arrangement that should not be tolerated at all?

## Notes
The problem being solved is arithmetic rather than technical. A rule worth having, applied to a large codebase that predates it, produces a violation count far beyond what anyone will fix, and the choices from there are all bad — patch everything in one enormous unreviewable change, hand the list to one or two people as months of joyless work, or shelve the rule. Restricting enforcement to what is already being modified escapes the arithmetic entirely: the cost per person is a line or two, it falls on whoever is in the file anyway, and the total effort is spread across everyone and everything that was going to happen regardless.

The property that makes it work is that codebases are not edited uniformly. Change concentrates heavily in a small number of files, which means the code most exposed to a forward-only rule is also the code most read, most modified, and therefore most worth converging. The parts that never converge are the parts nobody touches, where the violation is doing the least harm. The distribution that makes large codebases hard to reason about is, in this one case, working in your favour.

The deprecation use is worth naming separately because it addresses something otherwise difficult. Retiring a construct fails when the old form keeps appearing in new code faster than the old instances can be migrated, and that is the usual reason a migration never ends. A rule that refuses new uses freezes the denominator, and a fixed denominator turns an indefinite effort into one with a visible end. Announcing it early matters more here than elsewhere, because the people who will hit the rule are frequently not the people who wanted the change.

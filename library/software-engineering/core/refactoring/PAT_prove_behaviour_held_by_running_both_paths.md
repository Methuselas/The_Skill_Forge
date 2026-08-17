---
object_id: PAT_prove_behaviour_held_by_running_both_paths
object_type: pattern
name: Run the Old and New Paths Together and Diff Them
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
- verification
- migration
- rollout
- risk
cross_links:
- rel: related_to
  target_object_id: AP_refactor_working_code_safely
- rel: related_to
  target_object_id: PAT_separate_structural_change_from_behavioural_change
- rel: related_to
  target_object_id: PAT_judge_change_risk_by_what_it_can_break
- rel: related_to
  target_object_id: PAT_make_every_milestone_a_place_you_could_stop
reference:
  source_title: 'Refactoring at Scale: Regaining Control of Your Codebase'
  author: Maude Lemaire
confidence: high
references: []
variants: []
---

# Run the Old and New Paths Together and Diff Them

## Pattern Rule
**IF** you are replacing a working implementation whose surface area is too large, too old, or too heavily used for the existing tests to certify
**THEN** keep both implementations live behind the original entry point, execute both on real traffic, compare the results, and move the returned answer from old to new only once the differences are understood
**ELSE** where the call volume is low enough that a test suite written against the observed behaviour would cover it, write those tests instead — this technique costs real production capacity and buys nothing a good suite already gives you.

## Do
- Take the switch to the existing function rather than to its callers. Move the current logic into a private function of its own, write the replacement beside it, and let the original signature become the thing that chooses between them. No call site changes, which is what keeps the surface area of the change to one file.
- Run the comparison in stages and keep the returned answer separate from the executed answer. In the first stage both run, results are compared and logged, and the *old* result is what callers receive. In the second stage both still run and the *new* result is returned. Only the second stage can hurt anyone, and by the time you reach it the first has already told you where the differences are.
- Put a data backfill in front of both stages when the change moves storage rather than logic. Write to both stores, populate the new one from the old, and settle the write path before any read path depends on it.
- Add a final stage that stops the double read but keeps the double write, so downstream consumers still reading the old store have time to migrate. Know that this is where the escape hatch closes — after it, the only remedy is to fix forward.
- Sample the comparison rather than running it on every call. Comparing five percent of a hot path accumulates enough evidence within days and leaves the other ninety-five percent paying nothing.
- Count the load you are adding, and count it downstream too. Two paths mean two sets of queries against the database, the queue, and the logging system that receives the differences — and old tangled code produces far more differences than anyone predicts, so the log is the thing that falls over first. Start the sample rate low and raise it in steps.
- Triage differences in aggregate before looking at any single one. A single root cause routinely accounts for most of the volume, and finding it collapses the list rather than shortening it.
- Let different call sites sit in different stages at once. One query can be returning old results while another has moved to new, which is what makes a migration of any size divisible.

## Don't
- Don't run both paths serially in a runtime without real concurrency and then measure the latency. Without threads you have added the full cost of the second implementation to every request, and on a path that makes network calls you have doubled the round trips.
- Don't chase the difference count to zero before proceeding. The target is a residue you can explain — a rate you can attribute to something specific, such as rows legitimately changing between the two reads, and confirm by watching the values converge afterwards.
- Don't read a clean comparison as proof that every path is clean. What gets compared is what gets called, so a rarely-executed branch can pass this entire process untouched and fail the first time a large customer hits it.
- Don't leave the scaffolding standing once the new path owns the traffic. The conditional, the flag, and the duplicated implementation are all cost from that moment on.
- Don't reach for this on a change small enough to reason about. The machinery is justified by the size of the thing you cannot otherwise verify, not by the importance of the code.

## Checklist
- Does any caller need to change, or does the original signature absorb the switch?
- Which stage is each call site in right now, and who receives the answer in that stage?
- What is the sample rate, and what happens to the difference log if you raise it?
- Can you name the cause of every remaining difference, or only their number?
- Which branches carry too little traffic to have been exercised by the comparison?
- Has the point of no return been passed, and does everyone working on this know it?

## Notes
The premise is a property of behaviour-preserving change that makes it harder to verify than ordinary feature work, not easier. A new feature announces its own success — it either does the thing or it does not. A restructure succeeds by being undetectable, and confirming that nothing changed across a large surface is a far weaker position than confirming that something specific happened. The usual answer is to lean on the test suite, and two limits on that answer are already well understood: retesting proves behaviour was preserved only as far as the tests described the behaviour to begin with, and a change to an interface or a conditional moves the ground under both the compiler and the unit tests. On a small change those limits are tolerable. On a body of old code with thin coverage and heavy traffic they are exactly the situation, and this technique exists because production traffic is a better specification than anything anyone would have written by hand.

What makes it work is that the comparison and the commitment are separated. Running both implementations is free of consequence as long as the old answer is the one returned, so the entire discovery phase happens with no user exposed to the new code at all. That is the reverse of the usual arrangement, where finding out whether the rewrite is correct requires shipping it. The cost is paid in capacity rather than in risk, and capacity is the cheaper currency.

The traffic-proportionality limit deserves to be planned around rather than merely noted. Coverage under this method is distributed exactly as the call volume is distributed, which means the hot paths are certified thoroughly and the rare ones are not certified at all. A low-volume query that times out only for the customer with the most unusual data will sail through the comparison phase and surface during the ramp. The countermeasure is to sequence the ramp by risk — internal users first, then the smallest customers, then the largest and strangest — so that the paths the comparison could not reach are met in an order where the first encounter is survivable.

The stage that removes rollback is the one to name explicitly to everyone involved. While both paths execute, retreating is a configuration change. Once reads come only from the new source and the old one is no longer being kept current for readers, retreat means reconstructing state rather than flipping a switch. Teams get into trouble here by treating the whole sequence as uniformly reversible, when reversibility ends at a specific, identifiable step.

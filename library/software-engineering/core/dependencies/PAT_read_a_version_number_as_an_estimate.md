---
object_id: PAT_read_a_version_number_as_an_estimate
object_type: pattern
name: Read a Version Number as an Estimate, Not a Proof
library_path:
- software-engineering
- core
- dependencies
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- dependencies
- versioning
- risk
- upgrades
- compatibility
cross_links:
- rel: related_to
  target_object_id: PAT_state_your_compatibility_promise_and_its_span
- rel: related_to
  target_object_id: PAT_price_a_dependency_by_the_cost_of_change
- rel: related_to
  target_object_id: PAT_prove_behaviour_held_by_running_both_paths
- rel: related_to
  target_object_id: PAT_judge_change_risk_by_what_it_can_break
reference:
  source_title: 'Software Engineering at Google: Lessons Learned from Programming Over Time'
  author: Titus Winters, Tom Manshreck, and Hyrum Wright
confidence: high
references: []
variants: []
---

# Read a Version Number as an Estimate, Not a Proof

## Pattern Rule
**IF** you are deciding whether an upgrade is safe, or relying on a tool that resolves versions for you
**THEN** treat the version number as its maintainer's opinion about compatibility rather than a demonstrated property, and verify anything you actually care about against your own tests
**ELSE** where the resolver reports that no combination satisfies your constraints, stop looking for a cleverer resolution — the network is telling you two of your dependencies genuinely disagree.

## Do
- Hold on to what the number can and cannot know. A maintainer classifying a release is answering "did I change the interface" from inside their own project. Whether *your* code survives depends on which parts of it you used and how, which is information they do not have.
- Expect the classification to be too coarse in both directions. A break in one corner of a library forces a signal that invalidates everyone, including the majority who never touched that corner; and an addition classified as harmless can still break somebody, because anything observable ends up depended on.
- Recognise the three-layer shape when requirements conflict. You need something underneath, used by two things above it, both used by you — and when the thing underneath changes incompatibly and only one of the two middle layers has moved, no combination works. It takes three layers, so it will not appear in a small dependency graph and will appear reliably in a large one.
- Know that you are the only one positioned to see it. Each upstream is internally consistent and content; the conflict exists only where the paths meet, which is your build, and neither upstream has reason to have noticed.
- Reach for the easy escapes first — move one dependency forward or back until something is mutually satisfiable. Reserve local patching for when there is no such point, and expect it to be hard, because you will be reconciling two projects you did not write.
- Verify the upgrade rather than trusting the classification. Your tests answer the question the version number was estimating, and on a change you genuinely depend on, running both the old and new paths and comparing is available.
- Watch for the case where retreating is not permitted. Where the upgrade was forced by a security fix, moving backwards to restore compatibility is not an option, and the difficulty is now bounded below.

## Don't
- Don't read an automated resolution as a safety result. Resolvers answer whether the stated constraints can be satisfied simultaneously, not whether the resulting combination works.
- Don't assume a satisfying combination always exists. Networks are routinely constructed in which no assignment satisfies everything, and the correct response is to change the network rather than to keep solving.
- Don't take a patch-level bump as beneath verification. The classification is an estimate at every level, and the confidence it invites is exactly what makes small upgrades ship unexamined.
- Don't pin everything permanently to escape this. You are still exposed to forced upgrades, and you will meet all the accumulated incompatibility at once instead of a little at a time.

## Checklist
- Is this number a demonstrated property or somebody's judgement about their own change?
- Which parts of the interface do you actually use, and did any of them move?
- If the resolver failed, which two paths through the graph disagree?
- Is there a version pair that satisfies everything, or does something have to be patched?
- Was this upgrade forced, and does that remove going backwards as an option?
- What did your tests say, as opposed to what the number said?

## Notes
The structural problem is a mismatch between what the resolution machinery assumes and what the inputs are. Constraint solving of this kind is built for values that are definitely true or definitely false. What it is given instead is a sequence of human judgements — each maintainer's assessment of their own release, made without knowing who depends on them or how. The arithmetic on top is exact; the values it operates on are estimates and self-attestation, and the exactness of the arithmetic makes the whole thing feel more certain than it is.

The coarseness cuts both ways and neither direction is fixable within the scheme. A library is rarely one indivisible thing, so a break confined to one part still forces a signal that reads as "everything may have changed", and consumers of the untouched parts are invalidated for no reason. In the other direction, compatibility cannot be established from the interface alone: what matters is which behaviours somebody came to rely on, including behaviours nobody meant to promise, and no amount of care in classifying a release can account for those. So the number is simultaneously too pessimistic for most users and too optimistic for some, which is what makes it an estimate rather than a specification.

The three-layer requirement is worth holding because it explains a change in kind rather than degree. With a shallow set of dependencies this problem is nearly invisible and the whole scheme appears to work. As the graph deepens, the number of paths that can disagree grows, and the failures arrive without warning in projects that did nothing different. That is also why the person who hits it is so poorly placed to resolve it: both upstreams are behaving reasonably from where they stand, and the incompatibility is a property of the combination rather than of either component.

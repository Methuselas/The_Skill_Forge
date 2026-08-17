---
object_id: PAT_price_a_requirements_change_instead_of_absorbing_it
object_type: pattern
name: Quote the Cost of a New Requirement Rather Than Swallowing It
library_path:
- software-engineering
- core
- working-practice
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- requirements
- change_control
- scope
- construction
cross_links:
- rel: related_to
  target_object_id: AP_assess_construction_prerequisites_before_building
- rel: related_to
  target_object_id: PAT_do_prerequisites_per_increment_when_iterating
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Quote the Cost of a New Requirement Rather Than Swallowing It

## Pattern Rule
**IF** a new capability is proposed after construction has started
**THEN** respond with a revised schedule and cost estimate so the requester chooses whether to have it now or later, rather than silently absorbing it or flatly refusing it.

## Do
- Make the response a question about timing, not a verdict on merit: it sounds like a good idea, it is not in the current scope, here is what it costs and when — do you want it now or later? Attaching a schedule and a cost is what turns many must-haves into nice-to-haves.
- Re-derive the change's value from the business reason for the project rather than from the feature description. Ideas that look strong as "features" often look poor as "incremental business value", and many requirements arguments dissolve on that translation alone.
- Say what the change actually touches. A requirement change during coding means altering the design to meet it, discarding part of the old design, writing a new design that now has to accommodate code already written, discarding affected code and test cases, writing replacements, and retesting even the unaffected code to confirm nothing new broke.
- When proposals arrive faster than they can be handled, set up a change-control procedure or board. This is not bureaucracy for its own sake — it gives you known times to deal with changes and gives the requester a visible route for their input.
- Collect changes and decide them as a group rather than taking the easy ones as they arrive. Handled one at a time, whether a change gets made depends on where you are in the schedule when you think of it — an easy idea at 25 percent gets done and a far better one at 50 percent does not, purely because the second arrived later. Writing every suggestion down and choosing among them together is what lets value rather than timing decide.
- Read a high volume of change requests as a signal rather than as work. Some change is inevitable, but a lot of it says the requirements, architecture, or top-level design were not finished enough to build on — and going back to repair them costs less than constructing the software twice.
- Where change is expected, choose an approach built for it: prototyping to explore requirements before committing to build, or staged delivery in short cycles so feedback arrives while it is still cheap to act on.

## Don't
- Don't plan to follow a requirements document rigidly. On a typical project the customer cannot reliably describe what is needed before the code exists, and the development process is itself a major source of the changes because it teaches them what they need — so a plan to hold them to the original is a plan not to respond to them.
- Don't treat the requester as the problem. The better they understand the project the more their view of it changes, exactly as yours does.
- Don't absorb changes quietly to seem accommodating. Unpriced changes are the mechanism by which a schedule fails without anyone deciding that it should.

## Checklist
- Did the requester receive a cost and a date, or just an answer?
- Have you expressed the change as incremental business value rather than as a feature?
- Is there a route for the next proposal, or will it arrive the same ad hoc way?
- Does the current approach let you take a change at all, or does every one require redesign?

## Notes
The numbers make the case that change is normal rather than exceptional: the average project sees about 25 percent of its requirements change during development, and that change accounts for 70 to 85 percent of the rework on a typical project. A process that treats change as deviation is therefore mis-specified for its own workload. What the pricing move does is not reduce change — it makes the choice visible to the person who is entitled to make it, which is the requester, not the implementer.

Two failure modes bracket the right response, and both are common. Flat refusal preserves the schedule and loses the relationship, and it is only available to people whose position and finances make it survivable. Silent absorption preserves the relationship and loses the schedule, and it fails invisibly — nobody ever decided to slip, and so nobody can be shown to have decided. Quoting the cost is the only one of the three that leaves the decision with someone who holds both the money and the deadline.

Two cautions sit on either side of the batching rule. The estimate attached to a change must not be produced on the spot — off-the-cuff numbers are routinely wrong by a factor of two or more, and a change quoted casually is barely better than one absorbed silently, because the schedule still moves by an amount nobody computed. And batching is not deferral: the point is to decide the group on merit at a known time, not to let a list accumulate until the answer becomes no by default, which reproduces the original failure with extra paperwork.

The escape hatch is worth knowing exists even though it is rarely available. When requirements are especially bad or volatile and none of this works, cancelling is a real option — and even where cancelling is not really open to you, asking how much worse it would have to get before you would, and how far the current situation is from that point, is a useful calibration on how bad things actually are.

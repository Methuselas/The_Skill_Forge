---
object_id: PAT_guard_the_interface_abstraction_under_modification
object_type: pattern
name: Ask Whether a New Method Belongs Before You Add It
library_path:
- software-engineering
- core
- abstraction
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- abstraction
- interface_design
- maintenance
- erosion
cross_links:
- rel: related_to
  target_object_id: PAT_define_the_operation_set_before_the_representation
- rel: related_to
  target_object_id: PAT_dont_widen_api_for_reuse_or_testing
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Ask Whether a New Method Belongs Before You Add It

## Pattern Rule
**IF** you are adding a routine to an existing class or module during maintenance
**THEN** ask whether it is consistent with the abstraction the interface already presents, and if it is not, find another home for it rather than another way to justify it.
**ELSE** when the new capability genuinely belongs to this thing but the current interface cannot express it, the abstraction itself needs revising — do that deliberately rather than by accretion.

## Do
- Watch for the specific pressure that causes this: functionality that is clearly needed, does not quite fit the interface, and looks too hard to put anywhere else. That combination is what erodes interfaces, and it feels like pragmatism every single time.
- Check the level as well as the topic. An employee class exposing `GetQueryToCreateNewEmployee` is not merely off-topic; it is operating several levels below the abstraction its other routines sit at.
- Reach for cohesion when the abstraction question stalls. If a class feels weakly cohesive but the fix is unclear, ask instead whether it presents one consistent abstraction — that framing tends to produce the more useful answer, and the two travel together.
- Split when the data splits. If half the routines work with half the data and the other half with the rest, that is two classes wearing one name.
- Treat a single misfitting routine as worth the argument. The failure mode is cumulative, not dramatic — no individual addition sinks anything.

## Don't
- Don't add validation helpers to a domain class because that is where the data happens to be. Zip-code, phone-number and job-classification checks have no logical connection to an employee, however convenient the location.
- Don't judge an addition only by whether it works. Every routine in an eroded interface works; what has failed is the ability to reason about the class from its interface.
- Don't assume a leak is small because it is narrow. Public routines inconsistent with the abstraction are leaky panels rather than an open hatch — they admit water more slowly, and given enough time they sink the boat just the same.
- Don't let the erosion become the justification. Once an interface has drifted, each further addition looks consistent with what is already there.

## Checklist
- Say the class's abstraction in one sentence. Does the new routine fit that sentence?
- Is the new routine at the same level of detail as its neighbours?
- Would a reader who knew only the interface be surprised to find this on it?
- If it does not fit: where does it belong, and what is stopping you putting it there?
- Do half these routines use half this data?

## Notes
The reason this needs its own rule is that it is a maintenance failure, not a design failure. The class was well designed; the interface was consistent; and it degraded one reasonable-looking addition at a time under real pressure to ship. Nobody makes the decision that ruins it, which is why the check has to be attached to the act of adding rather than to a review that happens later.

McConnell puts consistent interface abstraction first in the chapter's summary — many problems arise from violating that single principle — and the maintenance case is where it is hardest to hold, because the original design intent is no longer in the room. What replaces it is the question itself: is this consistent with what the interface already claims to be. An addition that cannot answer yes needs a different home, and the cost of finding one is almost always lower than the compounding cost of not.

The related failure sits one step away and is worth distinguishing. Widening an interface so another caller can reuse an internal, or so a test can reach one, is a deliberate act with a stated reason. This is drift with no stated reason at all — which is why it is harder to notice and why the guard is a question rather than a prohibition.

---
object_id: PAT_state_your_compatibility_promise_and_its_span
object_type: pattern
name: Say What You Promise and for How Long
library_path:
- software-engineering
- core
- dependencies
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- dependencies
- contracts
- versioning
- api_design
- maintenance
cross_links:
- rel: related_to
  target_object_id: PAT_price_a_dependency_by_the_cost_of_change
- rel: related_to
  target_object_id: PAT_define_your_code_contract_explicitly
- rel: related_to
  target_object_id: PAT_read_a_version_number_as_an_estimate
- rel: related_to
  target_object_id: PAT_plan_the_removal_while_you_build
reference:
  source_title: 'Software Engineering at Google: Lessons Learned from Programming Over Time'
  author: Titus Winters, Tom Manshreck, and Hyrum Wright
confidence: high
references: []
variants: []
---

# Say What You Promise and for How Long

## Pattern Rule
**IF** you are publishing something other people will build on — a library, a package, a service interface — and it will outlive its first release
**THEN** write down what you undertake to keep working across versions and for how long, so that consumers can price depending on you and you can change things without ambush
**ELSE** where you deliberately promise nothing, say that too, because an unstated promise is read as a generous one and you will be held to the reading.

## Do
- Choose a position on the range rather than drifting into one. At one end, code built against an old release keeps compiling and keeps linking, effectively forever. In the middle, source keeps compiling but anything already built must be rebuilt. Further along, you reserve the right to break the interface but never without shipping a tool that mechanically converts the old usage to the new. At the far end, you promise nothing between releases and say so plainly.
- Pair the promise with a span. "We keep this working" and "we keep this working for two years after a release" are different undertakings, and the second is the one somebody can plan against.
- Recognise the position as a statement of what the project is for, not of how good the people are. A deliberately experimental project that breaks freely and a foundational one that never breaks can be run by equally capable maintainers; they have chosen different jobs.
- Take the automated-migration option seriously where you need room to move. Undertaking that every breaking change arrives with a tool that performs the update shifts the cost from every consumer to you once, and it is the only version of a breaking change that scales past a handful of known users.
- Say which uses you support, not only which interfaces exist. Consumers will reach for whatever is reachable, and behaviour you never intended to guarantee becomes a promise the moment enough people rely on it.
- Write it where a stranger will find it before adopting, not in a design document internal to your team.

## Don't
- Don't promise indefinitely because it sounds generous. You are committing to every future maintainer of this code, including the ones who will find an interface confusing and error-prone and be unable to fix it.
- Don't leave it implicit and expect consumers to infer it from your past behaviour. They will infer it, and what they infer will be whatever you have happened to do so far.
- Don't assume the promise only covers what you documented. Anything observable is depended upon eventually, which means the promise you actually made is wider than the one you wrote.
- Don't change position quietly. Moving from stable to experimental after people have built on you is a breaking change to the thing that mattered most.

## Checklist
- Where is the promise written, and would somebody find it before adopting?
- Does it name a span, or only a policy?
- Which of your observable behaviours are covered, and which are explicitly not?
- If you need to break something, what does a consumer have to do — and could a tool do it for them?
- Has the position changed since people started depending on it, and were they told?

## Notes
The reason to make this explicit is that the alternative is not silence; it is an assumption, made independently by every consumer, and it is always more generous than what you intended. Consumers price their dependency on you using whatever they can infer, and if they infer wrongly the cost lands on them at the worst moment. Publishing the position does not make you more constrained than you already were — it makes the constraint visible, which is what lets people plan around it.

The span matters as much as the policy and is more often omitted. A project unwilling to commit forever has an entirely defensible position, particularly when it sits underneath a very large amount of code and expects to be there for years: freezing an interface that turns out to be error-prone, for every future user, is a real cost to weigh against the disruption of changing it. Saying so converts an argument about whether you are allowed to change things into a conversation about when, which is the tractable version.

The migration-tool undertaking deserves attention because it changes the economics of breaking changes rather than merely softening them. The usual objection to breaking an interface is that the cost falls on a large number of people who were doing nothing wrong. If the break ships with something that performs the conversion mechanically, the cost is paid once by the person who understands the change, and the consumer's obligation drops to running a tool and reviewing a patch. That is the difference between a change that is technically permitted and one that is actually survivable at scale.

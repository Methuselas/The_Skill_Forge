---
object_id: PAT_post_facts_to_a_shared_space_when_order_is_unknown
object_type: pattern
name: Post Facts to a Shared Space When Arrival Order Is Unknown
library_path:
- software-engineering
- core
- modularity
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- coupling
- coordination
- workflow
- modularity
cross_links:
- rel: related_to
  target_object_id: PAT_publish_changes_and_let_consumers_register
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Post Facts to a Shared Space When Arrival Order Is Unknown

## Pattern Rule
**IF** several contributors work on one problem independently, their results arrive in an order nobody can predict, and a new result can change what work is needed next
**THEN** have them post facts into a shared space and act on what appears there, rather than wiring the sequence of steps into a workflow
**ELSE** when the sequence is known, stable, and short, wire it directly — the space buys indirection you would not be using.

## Do
- Test the fit against the four properties that make it work: a contributor need not know any other contributor exists; contributors may have entirely different specialities; they may join and leave partway through; and there is no restriction on what may be posted.
- Let a posted fact trigger whatever now applies, instead of a step advancing to the next step. The result of that triggered work goes back onto the space and may trigger more, which is how a late-arriving fact reopens work already thought finished.
- Keep the rules that decide what a fact means separate from the space that holds it, so a change in policy is a change to rules rather than a change to anyone's procedure or a code rewrite.
- Partition the space once it fills up — flat zones or a hierarchy — because a single undifferentiated space becomes hard to find anything in for exactly the reason a cluttered board does.
- Post whole objects rather than bare values where the mechanism allows it, and retrieve by partial match on fields or by subtype. A consumer can then ask for what it is able to handle instead of what it was told in advance to expect.

## Don't
- Don't reach for this when a fixed pipeline would do the job. The whole benefit is absorbing unpredictability, and where there is none you have paid indirection for nothing.
- Don't hard-wire a coordination sequence you expect to change. When the governing rules shift, a wired workflow means people change their procedures and someone rewrites the code that encoded the old ones.
- Don't let the space grow unstructured on the theory that anything may be posted. Being unrestricted about what goes on is what makes it work; being unrestricted about where it goes is what makes it unusable.
- Don't assume the anonymity removes real dependencies between facts. Some work still cannot start until a specific earlier fact has arrived, and that constraint has to live in the rules rather than in the order things happen to be posted.

## Checklist
- Can a contributor be added or removed without any other contributor changing?
- Does anything break if two facts arrive in the opposite order?
- When a policy changes, does code change, or do rules change?
- Is a given fact still findable on the board as it fills up?

## Notes
This is the fully anonymous end of decoupling, and it is worth being precise about what it adds over registration-based notification. There, the publisher and its subscribers still agree on an interface and still connect to each other directly. Here, nobody knows anybody: a contributor posts what it found and reads what is there, and the space is the only thing any of them shares. That is what lets participants be written in different languages, run in different places, and appear or disappear mid-problem.

The applicability conditions are what make this a decision rather than a preference, and they are all about unpredictability. Where results arrive on a schedule you know, a pipeline is simpler and easier to reason about. The conditions that flip it are: some work takes far longer than other work and finishes out of order, contributions come from different people or systems in different places, some facts genuinely depend on other facts arriving first, and — the decisive one — a new fact can raise requirements that did not exist a moment ago. A workflow engine can be made to handle all of that, but it handles it by enumerating combinations, and every change to the governing rules means reorganising the enumeration.

The alternative is not free. A shared space is a level of indirection: it is harder to see what will happen when a fact lands than to read a sequence of calls, and debugging means reconstructing an order that was deliberately left undefined. That cost is paid in exchange for absorbing change in the rules, so the honest question is whether the rules are actually going to change. Where they are fixed, the brute-force wiring is the better engineering; where they are not, the wired version is the brittle one, and it breaks in a place nobody is looking.

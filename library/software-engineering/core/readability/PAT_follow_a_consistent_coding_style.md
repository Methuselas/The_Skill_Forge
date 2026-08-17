---
object_id: PAT_follow_a_consistent_coding_style
object_type: pattern
name: Follow a Consistent Coding Style Guide
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- coding_style
- conventions
- linters
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_make_code_readable
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: high
references: []
variants: []
---

# Follow a Consistent Coding Style Guide

## Pattern Rule
**IF** a stylistic choice is not dictated by the compiler — naming casing, indentation, feature usage, file layout
**THEN** follow the team's agreed coding style guide, because a shared style lets readers rely on conventions to understand code correctly.

## Do
- Lean on convention as information: with PascalCase classes and camelCase variables, `ConnectionManager.terminateAll()` reads unmistakably as a call into a class that likely touches global state.
- Adopt the team or organization style guide as-is where one exists; where none does, take an off-the-shelf one such as a published language style guide rather than inventing conventions.
- Run a linter to catch style-guide violations and some error-prone patterns automatically, as a cheap first pass.
- Settle the conventions before construction starts, alongside picking the revision control tool and the compiler version. Naming, commenting, and layout conventions are specified at a granularity that makes them nearly impossible to retrofit into code that already exists, so the window for the decision closes early.
- Where the choice is genuinely yours — a new project, or a language whose ecosystem has not settled it — pick camel case. It is the one place the evidence favours a specific convention rather than merely a consistent one.
- Settle the identity-laden conventions mechanically instead of arguing them. Indentation, brace placement, and commenting style are matters of personal style before they are matters of engineering, so run the source through a formatter as a condition of being finished and let the tool make the choice nobody has to concede.

## Don't
- Don't break the convention and let `connectionManager` (camelCase) masquerade as an instance variable when it is actually a class with a static `terminateAll()` — that misreading terminated every chat on the server, not one.
- Don't rely on the linter as a substitute for good code; linters catch only simple issues.
- Don't half-adopt a convention. A convention applied inconsistently reads worse than no convention at all, because readers who learn the rule from the first half of a file then mispredict the second — you have taught them something false rather than nothing.

## Checklist
- Does naming casing let a reader tell classes from instances at a glance?
- Are you following the team's style guide rather than a personal style?
- Is a linter enforcing the conventions the guide specifies?

## Notes
The timing rule is the part most easily lost, and its justification is conceptual integrity (Code Complete, ch. 4). A large program needs a controlling structure that unifies its language-level detail, so the implementation has to be consistent with the architecture above it as well as internally consistent; without that discipline the result is a jumble of sloppy variations that taxes a reader for no gain, since the differences being decoded are arbitrary. McConnell's image is a painting executed to one grand design but rendered classical in one part, impressionist in another, cubist in a third — faithful to the plan and still a collage. The claim is that retrofitting is impractical, which argues for adopting whatever conventions are already in force in an existing codebase rather than mounting a late campaign to impose new ones.

Camel case is the single place the evidence bears on a choice this card otherwise treats as arbitrary (The Programmer's Brain, ch. 8). Binkley tested 135 programmers and non-programmers, showing each a sentence describing a variable and then four candidate identifiers to match against it; camel case produced a 51.5% higher chance of selecting the right one, at a cost of about half a second longer per identifier. The training effect is what confines the advice to open choices — participants trained in camel case were faster on camel case and *slower on snake case than untrained participants were*, so a style stops being neutral once a team has practised it. That rules out converting an existing snake-case codebase on these grounds, and it does not reach a language whose community has already settled the question, as PEP 8 has for Python. Both the timing rule and this one therefore land in the same place: the decision is worth making carefully and early, and worth leaving alone afterwards.

It is worth knowing which of these questions are technical and which are not, because they are argued as though they were all the first kind. Programming language, indentation style, brace placement, editor choice, commenting style, naming conventions, the efficiency-versus-readability line, and productivity measures are all positions people hold as expressions of personal style, and a mandate on any of them buys conformity at a price in morale that the conformity rarely covers. The move that works is to sidestep rather than legislate: a formatter run before code is called finished settles indentation and braces without anyone losing an argument, and a review requirement that unclear code be revised settles commenting without a rule about comment density. Save the willingness to absorb friction for the practices that damage whole projects — unreadable style, indiscriminate global data — and spend nothing on the nuances.

How little the specific choice matters is worth knowing precisely, because it is what licenses spending nothing on the argument. The one study that compared two common brace styles head to head found no statistically significant difference in understandability between them. Set against that, the cost of inconsistency is real and asymmetric: readers build expectations from what they have seen so far, and violating those expectations in seemingly innocuous ways measurably degrades performance. So the choice is close to free and the consistency is not, which is the whole reason to settle the first quickly and enforce the second.

There is a quieter route to the same place worth knowing about. Where code is reviewed as a matter of course, the group converges on a de facto standard without anyone writing one: decisions get made case by case in review, they accumulate, and the result is a shared style that nobody had to ratify. A team that reviews consistently and has no style document is often more consistent than one with the document and no reviews.

The `GroupChat` bug is the cautionary tale: a class named `connectionManager` violates the PascalCase-for-classes convention, so a reader reasonably assumes it is an instance field and that `terminateAll()` affects only their chat, when it is static and terminates every connection on the server. A consistent style is like a whole team speaking one language fluently — it removes a class of misreadings, which is why Long frames adopting and following a style guide (backed by linters) as a readability and bug-prevention measure.

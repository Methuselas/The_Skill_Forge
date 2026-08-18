---
object_id: PAT_price_a_dependency_by_the_cost_of_change
object_type: pattern
name: Price a Dependency by What Changing It Will Cost
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
- maintenance
- reuse
- risk
- versioning
cross_links:
- rel: related_to
  target_object_id: PAT_reuse_before_reinventing
- rel: related_to
  target_object_id: PAT_state_your_compatibility_promise_and_its_span
- rel: related_to
  target_object_id: PAT_read_a_version_number_as_an_estimate
- rel: related_to
  target_object_id: PAT_judge_an_architecture_before_building_on_it
reference:
  source_title: 'Software Engineering at Google: Lessons Learned from Programming Over Time'
  author: Titus Winters, Tom Manshreck, and Hyrum Wright
confidence: high
references: []
variants: []
---

# Price a Dependency by What Changing It Will Cost

## Pattern Rule
**IF** you are deciding whether to take on someone else's library, package, or service rather than building the thing yourself
**THEN** price the decision on what it will cost to move when it changes underneath you, not on what it costs to adopt today
**ELSE** where the work genuinely ends when it ships — a one-off script, an experiment, a prototype with a known disposal date — adoption cost is the whole cost and you should take whatever is easiest.

## Do
- Separate the two questions that get collapsed into one. Whether the library does what you need is a question about today and is usually easy. Whether you can still be using it in three years, through security patches and platform moves you do not control, is a different question with a different answer.
- Look for evidence the thing is maintained rather than merely popular. Does it have tests, do they pass, and does the project say anywhere what it intends to keep working across releases?
- Weigh who stands behind it. There is an enormous range between a library maintained by the people who maintain the language and a package uploaded by one person three years ago, and both install with the same command.
- Ask how often it has broken its users before. Past breakage is the closest thing to a forecast you will get, and it is visible in the release history without asking anyone.
- Answer the internal questions too, and answer them out loud. How long will this be in the system, who here will perform the upgrade when it comes, and roughly what will that upgrade involve. A dependency nobody owns is a dependency nobody upgrades.
- Estimate what building the equivalent would cost, even when you have no intention of doing it. Without that figure you cannot tell whether you are avoiding a week of work or a year of it, and the answer changes what you should tolerate.
- Prefer bringing the code inside your own boundary where that is genuinely available. Something your organisation controls, builds, and tests as one unit is a coordination problem you can solve; something outside it is a negotiation with people who owe you nothing.

## Don't
- Don't treat installation as the cost. The command is free and the commitment is not, and the gap between the two is where the surprise lives.
- Don't assume you can decline the upgrade. A vulnerability, a dead platform, or an upstream that stops supporting your version will force the move on a schedule you did not choose.
- Don't count a dependency as one thing. It arrives with everything it depends on, and those arrive with theirs, and each of them can force your hand.
- Don't take the decision on popularity alone. Widely used code is better tested and no more obliged to keep working the way you need it to.

## Checklist
- What is this expected to cost when it changes, not when it installs?
- Does the project state anywhere what it intends to keep working, or does it state nothing?
- How has it treated its users' code across previous releases?
- Who here will do the upgrade, and do they know that yet?
- How long do you expect to be depending on this?
- What would the equivalent cost to build, roughly, if you had to?

## Notes
The distinction underneath this is between writing a program and maintaining a system, and it sorts the decision cleanly. In the first, reuse is close to a free lunch: the dependency does what you need, you are not going to update it, and no amount of ill-advised coupling to its internals will ever hurt you, because nothing will change. In the second, every one of those assumptions fails, and the same import that was free becomes an ongoing obligation to track someone else's release schedule. The mistake is not choosing wrongly between them; it is not noticing which one you are in.

Reuse remains the right default, and this does not argue otherwise. Reimplementing a parser, a date library, or a cryptographic primitive is worse in almost every case, and the fact that a dependency carries a maintenance cost does not make writing your own carry less. What the pricing changes is which dependency you pick among several that would all work, and how much attention you give to the ones you already have — those are the decisions this actually moves.

The forced upgrade is the case worth planning for specifically, because it converts a decision into an emergency. Most of the time you can sit on a version indefinitely. Then a vulnerability is announced, or the version you are on stops receiving fixes, and suddenly you are moving several major versions at once, through every incompatibility that accumulated while you were not paying attention. The small regular investment nobody scheduled turns into a large urgent one, and the cost of that conversion is what the intake question was trying to estimate.

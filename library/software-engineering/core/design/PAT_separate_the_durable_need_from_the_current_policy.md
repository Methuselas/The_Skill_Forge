---
object_id: PAT_separate_the_durable_need_from_the_current_policy
object_type: pattern
name: Separate the Durable Need From the Current Policy
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- requirements
- abstraction
- business_rules
- adaptability
cross_links:
- rel: related_to
  target_object_id: PAT_state_the_problem_before_the_solution
- rel: related_to
  target_object_id: PAT_balance_adaptability_without_predicting_future
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Separate the Durable Need From the Current Policy

## Pattern Rule
**IF** you have been handed a rule to implement and are about to turn it into structure
**THEN** split it into the general need, which is what the system must be able to do, and the current policy, which is one instance of that need holding today — then build the general mechanism and let the policy live as data it reads.

## Do
- Listen for the specific parties in a stated rule. "Only an employee's supervisors and the personnel department may view that record" names today's org chart; the need underneath is that only authorized people may view it. Build to the second and the first becomes a configuration entry.
- Trace what each phrasing makes you write, because that is where the cost lands. The specific version leads to an explicit test at every place the file is touched, and every policy change means finding all of them. The general version leads to one access-control mechanism, and a policy change updates its data.
- Ask why the users do a thing, not only how they currently do it. What they describe is their present procedure, which has usually accreted around constraints that may no longer exist; what you have to satisfy is the business problem behind it.
- Treat a named mechanism as a claim to be tested rather than a requirement. "The system must let you choose a loan term" is a need. "We need a list box to select the loan term" is a need only if the list box itself is genuinely required — otherwise it is someone illustrating the need with the first widget that came to mind, and you have to ask which it is.
- Record the reasoning behind a requirement alongside it. The daily implementation decisions that nobody thinks to ask about get made correctly or incorrectly depending on whether the team knows why the rule exists.

## Don't
- Don't encode current practice as though it were the need. The two-digit year was ordinary business practice long before computers, and the systems that automated it copied the abbreviation instead of representing a date and knowing that two digits were a shortened form of one. The cost arrived decades later and was blamed on saving memory, which was never the actual mistake.
- Don't read this as licence to be vague. The general statement still has to be exact about what must hold; what it drops is the current instance, not the precision. A rule nobody can test is not more abstract, it is unfinished.
- Don't generalize a constraint that is genuinely fixed. Where a rule is imposed from outside and cannot vary — a regulator's threshold, a protocol's field width — building a configurable mechanism around it buys flexibility nobody will ever use.

## Checklist
- Does this rule name specific people, departments, values, or widgets?
- If that specific thing changed next quarter, would you be editing code or editing data?
- Can you state the need in one sentence without naming any of them?
- Do you know why this rule exists, or only that you were told it?
- Is the specific version actually fixed by something outside the project?

## Notes
This is not requirements gathering, which belongs to whoever owns it. It is what a builder does with a requirement already in hand, at the moment of deciding what shape the code takes — and it is squarely inside the construction span because the decision is structural. The same sentence, read two ways, produces two systems: one where a policy change is a code change hunted across the codebase, and one where it is a data change. Nothing about the requirement document determines which; the reading does.

The distinction to hold is that requirements are need. They are not architecture, not design, and not the user interface, and each of those three gets smuggled in through a stated rule that names a mechanism. The useful discipline is to keep asking what must be true, and to push everything describing how it is currently achieved into a separate record that the general statement can point at. That record is worth keeping rather than discarding — it is what tells a developer the kind of thing the implementation has to support, and it frequently ends up as the actual configuration data.

The historical case worth carrying is the two-digit year, because the usual account of it is wrong in an instructive way. It is remembered as programmers saving bytes on expensive hardware, which makes it a problem that could not recur now that storage is free. The real failure was analytical: the abbreviation was existing business practice, the early systems automated the practice rather than the underlying thing, and no layer in between knew that the two digits stood for something longer. Storage had nothing to do with it, which means the same mistake is available at any price per byte — wherever a current convention gets recorded as if it were the fact it abbreviates.

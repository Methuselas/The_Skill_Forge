---
object_id: PAT_make_order_dependencies_visible
object_type: pattern
name: Make Order Dependencies Visible
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- control_flow
- dependencies
- sequencing
- maintainability
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_unexpected_side_effects
- rel: related_to
  target_object_id: PAT_let_an_awkward_name_expose_the_design_fault
- rel: related_to
  target_object_id: PAT_extract_a_routine_even_when_it_seems_too_small
- rel: related_to
  target_object_id: PAT_minimize_variable_span_and_live_time
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Make Order Dependencies Visible

## Pattern Rule
**IF** several statements or calls have to run in a particular order
**THEN** work down a ladder of remedies — first try to remove the dependency, then express it in the structure, then in the names and parameter lists, and only then in a comment.
**ELSE** where the sequence is critical enough that a silent violation would be serious, have the code check it at run time, accepting that the checking apparatus is itself new code that can be wrong.

## Do
- Take the earliest rung on the ladder that is actually available, rather than jumping to documentation because it is quickest. A comment is compensation for a weakness in the code, appropriate when you are working in tightly controlled code you may not restructure, and not before.
- Pull a hidden step out into its own named call. When one of four sibling routines quietly initializes the data the other three use, that initialization does not belong there — putting it in an `InitializeExpenseData` gives it a name that says it goes first and makes its absence noticeable.
- Let the parameter list carry the signal. Four parameterless calls tell a reader nothing about whether they share state; the same four each taking `expenseData` suggest they might. Turning them into functions that take the data and return it updated states the chain outright rather than hinting at it.
- Read the absence of shared data as information too, because it is free and it is reliable. Four calls that each take their own distinct data, followed by one that takes all four, have told the reader that the first four are independent and the fifth must come last.
- Name honestly if you will not restructure. A routine that computes marketing expense and also initializes shared member data is accurately called `ComputeMarketingExpenseAndInitializeMemberData`. That name is not too long — the routine is wrong, and the ugliness is the report.

## Don't
- Don't let domain knowledge carry the order. Computing monthly figures before quarterly and quarterly before annual is deducible by someone who knows accounting and invisible to everyone else, and whoever maintains this in two years may be neither.
- Don't leave a constraint expressed only in a comment when the structure could express it. That comment goes stale in silence, because nothing breaks at the moment it stops being true.
- Don't reach for housekeeping flags as a default protection. A variable recording that the data was initialized, plus its siblings for each subsequent step, means new variables, new initialization, and new checking code — each one a fresh place to be wrong. The protection has to be worth the secondary defects it invites, which is why it is the last rung and not the first.
- Don't assume an arbitrary placement will be read as arbitrary. Initialization dropped into whichever routine happened to be written first looks deliberate to everyone who arrives later, and they will preserve it.

## Checklist
- Could this dependency be designed away rather than communicated?
- From the code alone, with no knowledge of the domain, can a reader tell these must run in this order?
- Do the parameter lists say whether these calls share state?
- Is any ordering constraint carried only by a comment?
- If someone reordered these tomorrow, what in the code would tell them they were wrong?

## Notes
Order dependencies come in three grades of visibility and the middle one is the dangerous one. At the top, the names do the work — reading data, then calculating from it, then printing the result cannot be reordered and nobody would try. At the bottom, the dependency is genuinely hidden behind parameterless calls that share member data, and at least a careful reader will notice they can learn nothing from the code and go looking. In between sit dependencies that are deducible if you happen to know the domain, and those get reordered, because the code looks like a list of peers and the reader who breaks it had no reason to suspect otherwise.

The ladder is worth following in order rather than picking a rung by taste, because each rung costs more and helps less than the one above it. Removing the dependency means nobody can get it wrong. Expressing it structurally means the code states it. Expressing it in names and parameters means the code hints at it strongly. A comment means the code says nothing and a note beside it says something, for as long as the note stays true. A run-time check means the code does not communicate the constraint at all but will catch you violating it, at the price of additional state that has to be maintained correctly.

The parameter-list technique is the one most often left unused, and it is nearly free. Data flow and control flow are separate things, but a reader uses the first to infer the second, and that inference is reliable enough to build on deliberately. Passing shared data explicitly through a sequence of calls is a way of writing the ordering constraint into the code without writing a word about it — and the same mechanism working in reverse lets you state independence, which is information a maintainer can act on rather than something they have to establish for themselves.

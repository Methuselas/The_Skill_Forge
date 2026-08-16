---
object_id: PAT_name_the_problem_not_the_computation
object_type: pattern
name: Name the Problem, Not the Computation
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
- naming
- readability
- problem_domain
- constants
cross_links:
- rel: related_to
  target_object_id: PAT_use_descriptive_names
- rel: related_to
  target_object_id: AP_choose_a_name_with_feitelsons_three_steps
- rel: related_to
  target_object_id: PAT_give_each_variable_exactly_one_purpose
- rel: related_to
  target_object_id: PAT_name_unexplained_values
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Name the Problem, Not the Computation

## Pattern Rule
**IF** a candidate name has come to mind for a variable, field, or constant
**THEN** check which world it is drawn from — the problem you are solving, or the machinery you are solving it with — and take the problem word.
**ELSE** when the accurate problem-domain name comes out too long to live with, shorten it by dropping words rather than by switching worlds — `numTeamMembers` keeps the domain that `ntm` and `x` throw away.

## Do
- Run the what-against-how test on the candidate. A name pointing at some aspect of computing rather than at the problem is a how. `inputRec` names input and records, both computing ideas; `employeeData` names what is actually inside. `bitFlag` describes how a printer's readiness is stored; `printerReady` describes the readiness. In an accounting program `calcVal` reports that a calculation occurred, where `sum` reports the money.
- Generate the name by stating in words what the thing represents, then look at the sentence you just wrote. It is very often the best name available, and for a specific reason — it needs no deciphering, it cannot be confused with something else because it is a full description, and it is easy to remember because it resembles the concept.
- Name a constant for the entity rather than for the number it currently holds. `FIVE` is bad whether or not the value is 5.0, because `FIVE = 6.0` is absurd and values move; `CYCLES_NEEDED` survives the change. `BAKERS_DOZEN` fails in the same way that `DONUTS_MAX` does not.
- Reach for the ordinary word first. `currentDate` and `todaysDate` are good names precisely because they are the obvious ones, and the obvious word is the solution most often skipped past.
- Make the name as specific as the thing it holds. `date` is nearly right for the current date and still wrong, because the date in question is not just any date, and the name gives no indication which one it is.

## Don't
- Don't accept a name that would fit more than one purpose. Names general enough to serve several things are less informative than they could be, and a name that would fit anywhere is an open invitation to reuse the variable for something else.
- Don't let `x` through on the grounds that it is temporary. It traditionally stands for an unknown quantity, so it announces to every reader that nobody knows what is in there — and `x1` and `x2` are worse, because even after you work out what `x` is you still learn nothing about how the two relate.
- Don't name a value after the operation that produced it when the result already has a name in the domain.

## Checklist
- Does this name mention a computing concept — input, record, flag, value, calc, buffer — where a domain word exists?
- Said aloud to someone who knows the business and not the code, would they recognize what it refers to?
- Would this constant's name still be true if its value changed tomorrow?
- Is there an ordinary word for this that you passed over?
- Could this name be attached to a second, unrelated thing in the same program without looking wrong?

## Notes
The framing that makes this more than a preference is that a variable and its name are not two things. You can name a dog whatever you like because the dog exists independently of what you call it; a variable is very nearly constituted by its name, since the name is all a reader has. That is why the goodness of a variable is largely decided by the goodness of its name, and why a cute or arbitrary choice is a different kind of mistake here than it would be for a pet.

The demonstration is a four-line calculation. Written as `x = x - xx`, `xxx = fido + SalesTax( fido )`, and so on, it is unreadable even once you are told it computes a customer bill — you cannot say which variable holds the new purchases. Written as `balance`, `lastPayment`, `monthlyTotal`, and `newPurchases`, the same arithmetic answers the question on sight. Nothing changed but the names.

This sits underneath the naming action plan rather than beside it. That plan decides which concepts a name should carry and how to assemble them; this decides which side of the problem-solution line the concepts should be drawn from in the first place. A name can pass every step of a naming procedure and still describe the machine instead of the job.

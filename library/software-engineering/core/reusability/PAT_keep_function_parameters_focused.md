---
object_id: PAT_keep_function_parameters_focused
object_type: pattern
name: Make Functions Take Only What They Need
library_path:
- software-engineering
- core
- reusability
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- function_parameters
- reusability
- readability
- modularity
cross_links:
- rel: related_to
  target_object_id: PAT_encapsulate_related_data_together
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u09, pp. 257-259
  evidence_type: text
confidence: high
references: []
variants:
- variant_id: VAR_order_and_audit_the_parameter_list_as_an_interface
  variant_name: Order and Audit the Parameter List as an Interface
  variant_basis: emphasis
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  locator: u07, pp. 174-181
  difference_from_foundation: The foundation narrows each parameter to what the function actually needs, judged one parameter at a time. This variant treats the parameter list as an interface to be ordered and audited as a whole, on the grounds that inter-routine communication is where a large share of defects live - Basili and Perricone found 39 percent of all errors were internal interface errors. Its rules are conventions rather than judgments. Order parameters input, then input-and-output, then output-only, so the list implies the sequence of operations inside. Keep similar parameters in the same order across similar routines, since inconsistency there is pure memory tax with no compensating benefit. Put status and error variables last, being incidental and output-only. Remove unused parameters, which correlate with defects - 46 percent of routines with no unused variables were error-free against 17 to 29 percent of those with more than one.
  when_to_use: Use when designing or reviewing a family of related routines, where consistency across the family is worth more than any individual signature's local optimum. The unused-parameter audit is worth running on its own, since it is mechanical and the correlation with defects is strong.
  when_not_to_use: Do not let ordering conventions override the foundation's narrowing rule - a well-ordered list of parameters the function does not need is still the wrong interface. Language conventions may also conflict, as the C library's modified-parameter-first habit does; consistency within your own codebase matters more than which convention you pick.
  absorbed_from_object_id: none
---

# Make Functions Take Only What They Need

## Pattern Rule
**IF** a function uses only part of an object passed to it
**THEN** narrow the parameter to just what it actually needs, so the function is reusable and its calls are honest — while using judgment when it needs most of an encapsulating object.

## Do
- Pass the specific value: a `setTextColor` that reads only the color from a styling object should take a color, not the whole options object.
- Notice the call-site symptom: forcing callers to build a full options object with irrelevant made-up font, size, and line-height values just to set a color signals the parameter is too broad.
- Keep calls truthful — narrowing the parameter makes a warning-styling call simply set the color red, with no misleading extra values.

## Don't
- Don't demand a whole object when one field will do; it makes the function unreusable elsewhere and makes callers fabricate values that imply effects that never happen.
- Don't overcorrect into unencapsulating everything; if a function genuinely needs most of a grouped object, passing the object beats threading many loose values, which harms modularity.

## Checklist
- Does the function read only a fraction of the object it takes?
- Are callers inventing irrelevant values just to satisfy the parameter?
- If it needs most of an encapsulating object, is passing the whole object the cleaner choice?

## Notes
An over-broad parameter couples a function to more than it uses, blocking reuse and misleading readers. Long's `setTextColor` taking a full `TextOptions` forces a warning-styler to concoct a font, size, and line height that suggest it sets them — it does not. Taking a color instead makes the function reusable and the call self-evident. The judgment clause guards against the opposite mistake from chapter 8: when a function needs most of a cohesive object, keep it encapsulated rather than exploding it into loose arguments.

`VAR_order_and_audit_the_parameter_list_as_an_interface` widens the unit of attention from the individual parameter to the list. The foundation asks whether each parameter is narrow enough; this asks whether the list as a whole reads as an interface, and its justification is that interfaces between routines are where defects concentrate - Basili and Perricone attributed 39 percent of all errors to internal interface communication. The rules are deliberately conventions rather than judgment calls, because their value comes from being applied uniformly: input, then input-output, then output-only, so the ordering itself narrates what happens inside; the same parameters in the same order across similar routines; status and error variables last. The unused-parameter rule is the one to act on first, being mechanical and strongly evidenced, with 46 percent of routines carrying no unused variables coming back error-free against 17 to 29 percent of those carrying more than one. Note that `PAT_dont_mutate_input_parameters` already covers McConnell's related warning against using parameters as working variables, so that guidance is not duplicated here.

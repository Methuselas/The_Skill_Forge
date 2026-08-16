---
object_id: PAT_name_a_boolean_for_the_condition_it_asserts
object_type: pattern
name: Name a Boolean for the Condition It Asserts
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
- booleans
- status_variables
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_use_descriptive_names
- rel: related_to
  target_object_id: PAT_detect_linguistic_antipatterns_in_names
- rel: related_to
  target_object_id: PAT_name_unexplained_values
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Name a Boolean for the Condition It Asserts

## Pattern Rule
**IF** you are naming a boolean or a variable that carries the state of the program
**THEN** name it for a specific condition that is plainly either true or false, stated positively.
**ELSE** when the state has more than two values, stop naming a boolean and give it an enumerated type, so the name describes a category rather than pretending the world is binary.

## Do
- Test a candidate by asking what `true` would mean. `done`, `found`, `error`, `success`, and `processingComplete` answer at once. `status` cannot — everything has a status, so `true` might mean a status exists, or that things are fine, or that something went wrong, and no reader can tell which.
- Prefer the specific condition to the generic verdict. Where success means the value turned up, `found` says so; where it means the work ran to completion, `processingComplete` says so. Both beat `success`, which only says that whatever was supposed to happen did.
- State the condition positively and negate it where it is used. `if not notFound` is a phrase nobody parses correctly at speed, and the repair is not a better double negative but `found`, negated with an operator at the one site that needs it.
- Use the question form as a detector even when you do not keep it. Turning a candidate into a question exposes vagueness immediately — `isProcessingComplete?` has an answer and `isStatus?` makes no sense at all. That is a property of the check, not of the prefix.
- Give a numeric status a named constant or an enumerated type. `characterType == CONTROL_CHARACTER` and `reportType == ReportType_Annual` say what is being compared; `statusFlag & 0x0F` and `printFlag == 16` require the reader to already know both what the variable is and what the number means.

## Don't
- Don't put `flag` in the name. It announces that the variable marks something without saying what, which is the only part the reader needed, and it is why these end up as `statusFlag` and `computeFlag` rather than as conditions.
- Don't keep a name that makes you work out what a section does. Figuring things out is for murder mysteries; catching yourself deducing the meaning of a variable is the signal to rename it rather than to concentrate harder.
- Don't adopt the question prefix as a blanket convention just because it works as a test. It costs a little at every use site — `if (isFound)` reads slightly worse than `if (found)` — so it earns its keep as a check on the name more reliably than as a standing rule.

## Checklist
- What exactly does `true` mean here, stated in one clause?
- Is the condition phrased positively, with negation left to the use site?
- Would the question form of this name have an answer?
- Is any state carried as a bare number where a named constant or enumerated type would say what it means?
- Does this variable have exactly two meaningful states, or has a third been squeezed in?

## Notes
The distinction that makes this workable is between naming the *variable's subject* and naming the *condition*. `sourceFile` names a subject and tells you nothing about what `true` would assert; `sourceFileAvailable` and `sourceFileFound` name conditions and answer the question on sight. Most bad boolean names are subjects, and the repair is almost always to append the predicate rather than to find a better noun.

The known counterweight is worth carrying alongside this. `PAT_detect_linguistic_antipatterns_in_names` reports that across seven open-source projects most identifiers beginning with `is` did not in fact hold booleans, which is the same failure arriving from the other direction — a name shaped like a condition attached to something that is not one. Read together, the two say that the question form is a prompt for the author and never a guarantee to the reader, so a reader should still check and an author should still make it true.

The dispatch to enumerated types is the part people skip. A status variable that started as a boolean and grew a third case usually gets a magic number bolted on instead of a type, which is how `printFlag == 16` happens. Reaching for the enumerated type at that moment keeps the name describing a category rather than leaving it describing a condition that stopped being binary.

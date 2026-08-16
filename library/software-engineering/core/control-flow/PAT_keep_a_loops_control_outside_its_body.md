---
object_id: PAT_keep_a_loops_control_outside_its_body
object_type: pattern
name: Keep a Loop's Control Outside Its Body
library_path:
- software-engineering
- core
- control-flow
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- loops
- control_flow
- termination
- readability
cross_links:
- rel: related_to
  target_object_id: AP_build_a_loop_from_the_inside_out
- rel: related_to
  target_object_id: PAT_choose_the_loop_by_where_it_tests
- rel: related_to
  target_object_id: PAT_give_each_variable_exactly_one_purpose
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Keep a Loop's Control Outside Its Body

## Pattern Rule
**IF** you are writing or reviewing a loop
**THEN** arrange it so a reader can tell when it ends without reading inside it — every condition that decides termination belongs in the header or the test, and the body belongs to the work.
**ELSE** where an exit genuinely has to sit in the middle, accept that you have given up reading the loop from outside and pay for it deliberately, by putting every exit in one place and making the loop short enough to take in whole.

## Do
- Read the loop's opening line and ask what it tells you. A test combining end-of-file and a data-available flag says exactly what stops this loop, and it says it without your knowing anything about the contents. That property is the thing being protected.
- Reserve a counted loop's header for statements that control the loop — the initialization, the test, and the step that moves it toward finishing. Housekeeping that merely happens each pass, such as maintaining a record count, is not loop control and putting it in the header falsely implies it is.
- Group the housekeeping at one end of the body and keep it there. The variables you initialized above the loop are generally the ones you will be adjusting in that block, which makes the pairing easy to check.
- Save what you need from the index before leaving, rather than reading the index afterwards. Setting a found flag inside the loop and returning that is clearer than testing the counter against its limit afterwards, because the counter's value on exit differs between languages, between implementations, and between normal and early termination.
- Prefer the counted form when the work fits it, precisely because it collects initialization, test, and step in one place. A common modification error is changing a while loop's setup at the top and forgetting the matching advance at the bottom, and the counted form has no bottom to forget.
- Take a ceremonial control variable as the one clearly defensible break. A flag such as `done`, set in the body and tested in the header purely to mean "leave now", puts a word in the header that describes nothing; a single `break` or `return` at the point the decision is made says the same thing where a reader will look for it.

## Don't
- Don't adjust the index of a counted loop to force an early exit. Setting a counter past its bound to break out is a well-known amateur signature, and the honest version is a loop whose test can express the real exit condition.
- Don't scatter exits. A loop containing several breaks is a signal that it wants to be more than one loop, and the cost of getting it wrong is not theoretical — a misplaced break that left a switch rather than the intended conditional took New York City's phone system down for nine hours in 1990.
- Don't let a break or continue in without being able to defend it. Each one forces a reader to look inside for the exit condition, which is the property this whole discipline exists to preserve. Use them where they genuinely simplify, and treat the inability to justify one as the answer.
- Don't put the loop's work inside its test. A loop whose body is empty because the read and the end check were combined into the condition has hidden the work in the control, which is the same failure in the other direction.
- Don't count on the index being invisible outside the loop even where the language says it should be. Compilers have disagreed about this, and code that depends on a scoping rule three implementations read three ways is not portable.

## Checklist
- From the loop's first line alone, can you say what makes it stop?
- Does the header contain anything that does not affect termination?
- Is the index modified anywhere except by the loop's own step?
- Does any code after the loop read the index's final value?
- How many exits does this loop have, and can each be defended?

## Notes
The organizing image is the loop as a black box: the surrounding program knows the conditions under which the box runs and knows nothing about its contents. That is worth more than it sounds, because it makes a loop something you can reason about without reading — the same property that makes a well-named routine cheap to use. Every technique here either preserves it or is a deliberate, priced exception to it.

Two failures reliably destroy the property, and they look nothing alike. One is control leaking into the body — a break, a continue, an index quietly modified — after which the header no longer describes when the loop ends and a reader has to scan the body to find out. The other is work leaking into the header, which is the mirror image: the loop's opening line now mixes what is being done with when it stops, and neither is legible. A header stuffed with a record count and a body containing the actual read has both problems at once, and it is the shape a flexible counted-loop syntax invites.

There is an apparent conflict inside McConnell's own advice here, and resolving it sharpens the rule rather than weakening it. The refactoring material says to use `break` or `return` in place of a loop control variable; this card says a `break` needs defending. Both hold, because they are aimed at different things. What this card protects is a reader's ability to learn the exit condition from the header — and a `done` flag defeats that as thoroughly as a scattered break does, since `while (!done)` names no condition at all and the real test is somewhere in the body. Replacing that flag with one `break` moves the condition to where it is decided and costs nothing that was not already lost. The rule that survives is about the number and placement of exits, not about the keyword: one exit at the point of decision is legible, a flag standing in for it is not, and several breaks sprinkled through a body are the case the caution was written for.

The exception is real and should not be argued away. Sometimes the exit genuinely belongs in the middle, and the loop-with-exit form is a legitimate structured construct with evidence behind it. What matters is knowing what you spent: once the exit is inside, the loop can no longer be understood from outside, so it needs to be short enough to read entirely, and every exit condition needs to sit together rather than being sprinkled through the body where one will be missed during a change.

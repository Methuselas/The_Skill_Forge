---
object_id: PAT_decide_the_else_instead_of_omitting_it
object_type: pattern
name: Decide the Else Instead of Omitting It by Default
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
- control_flow
- conditionals
- completeness
- testing
cross_links:
- rel: related_to
  target_object_id: PAT_handle_enums_exhaustively
- rel: related_to
  target_object_id: PAT_order_branches_so_the_common_case_is_found_first
- rel: related_to
  target_object_id: PAT_understand_the_routine_before_the_compiler_sees_it
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Decide the Else Instead of Omitting It by Default

## Pattern Rule
**IF** you have written a conditional with no alternative branch
**THEN** treat the omission as a decision to be made rather than a default to fall into — establish what should happen when the test fails, and record that you established it.
**ELSE** where nothing should happen and the reason is not evident from the code, say so in a short comment instead of leaving a silence that reads identically to an oversight.

## Do
- Assume the alternative is more likely needed than not. An analysis of production code found that somewhere between half and four fifths of conditionals written without an alternative branch should have had one, which makes the bare conditional the suspicious shape rather than the ordinary one.
- Leave evidence that the case was considered. A brief note saying that an invalid colour is safely ignored because nothing was written to the screen tells the next reader that the silence is deliberate; an empty space tells them nothing, and they will either duplicate your reasoning or assume you forgot.
- Exercise the alternative branch when you test. The reflex is to check that the main path works and stop, so the branch that runs least often is also the one least likely to have been run at all before it ships.
- Read the two branches against each other before moving on. Swapping the contents of the branches, or inverting the test, is a common enough slip that it is worth one deliberate look — both versions compile and both look plausible.
- Collapse a conditional whose main branch is empty. A test with nothing in its body and all the work in the alternative should have its condition negated and its alternative promoted, which removes two lines and a small puzzle.

## Don't
- Don't read a missing alternative as meaning the author decided nothing was needed. It is equally consistent with the author never having considered it, and from the code the two are indistinguishable — which is the whole reason this is worth a habit.
- Don't write empty alternative branches everywhere as a ritual. Coding one purely to demonstrate that you thought about it is overkill in most code, and a file full of empty branches trains readers to skip them, including the ones that matter.
- Don't leave the reasoning in your head when it took any thought to reach. The cases worth commenting are exactly the ones where you had to work out that nothing should happen, because that is the reasoning the next person would otherwise repeat.

## Checklist
- What should happen when this test fails, and did you decide that or skip it?
- If nothing should happen, would a reader know why without asking?
- Has the alternative branch actually been executed by a test?
- Are the branches the right way round, and is the test the right way round?
- Is the main branch empty, with the real work in the alternative?

## Notes
The finding underneath this is what makes it worth a card rather than a preference: most conditionals written without an alternative turned out to need one. That is a claim about how the omission actually happens — not as a considered judgment that the failing case needs no handling, but as the natural consequence of writing the case you were thinking about and moving on. The conditional is complete as far as the author's attention went, and attention stopped at the interesting branch.

What the habit costs is small and what it catches is not. Most of the time the answer really is that nothing should happen, and the work is a few seconds of thought and occasionally one line of comment. Occasionally the question surfaces a case nobody had considered, and it surfaces it while the code is being written rather than after it has produced a wrong result quietly for a while. That asymmetry is the argument.

This is the plain-conditional counterpart to exhaustiveness on a closed set of values. Where the branch is over an enumerated type, `PAT_handle_enums_exhaustively` gives a stronger guarantee than a habit can — the compiler or a test can be made to fail when a new value appears, and that mechanical check should be preferred wherever it is available. This card is for the case that has no such closed set to check against, where a boolean test has exactly two outcomes and only one of them has been written down.

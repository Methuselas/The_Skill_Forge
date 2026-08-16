---
object_id: PAT_choose_the_control_construct_that_fits_the_data
object_type: pattern
name: Choose the Control Construct That Fits the Data
library_path:
- software-engineering
- core
- control-flow
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- control_flow
- conditionals
- case_statements
- data_shape
cross_links:
- rel: related_to
  target_object_id: PAT_handle_enums_exhaustively
- rel: related_to
  target_object_id: PAT_choose_a_problem_representation_before_solving
- rel: related_to
  target_object_id: PAT_give_each_variable_exactly_one_purpose
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Choose the Control Construct That Fits the Data

## Pattern Rule
**IF** you are choosing between a case statement and a chain of conditionals
**THEN** let the shape of the data decide — a case statement wants a value that is genuinely one of a small set of categories, and anything else wants a chain that tests the real value.
**ELSE** when the language's case statement handles ranges, strings, or enumerated values directly, prefer it over a chain for data that qualifies, because it is both easier to write and easier to read than the equivalent ladder of tests.

## Do
- Test the actual value rather than a key derived from it. Comparing a whole command string against named constants is longer to write than switching on its first character and is the only version that answers the question that was asked.
- Notice when you are manufacturing the selector. If the variable controlling the branch did not exist until you created it to enable the construct, that is the signal — the construct is driving the data representation instead of following it.
- Keep the work in each branch short, calling out to a routine when a case needs real logic, so the shape of the branch structure stays visible.
- Reach for the language's richer construct when the data qualifies. Where a case statement accepts a range of characters, a list of punctuation marks, and a pair of named bounds, expressing four categories that way is clearer than four multi-clause conditionals, and it will not silently gain a fifth path.

## Don't
- Don't peel a categorical key off non-categorical data. Taking the first character of a user-entered command routes `copy` to the copy operation and routes `cement overshoes`, `clambake`, and `cellulite` there too — and the error branch will not save you, because it now catches only a wrong first letter rather than a wrong command.
- Don't code your last real case as the default clause. It costs you the label that documented what that case was, it costs you the ability to use the default for detecting values you did not plan for, and it makes the next addition awkward — you have to add the case, decide whether it becomes the new default, and convert the old disguised one back into a real case.
- Don't reshape the data to suit the construct you had in mind. If the values do not sort into a small closed set, that is a fact about the problem, and forcing them into one produces branches that look exhaustive and are not.

## Checklist
- Is the value being switched on something the domain actually has, or something this code invented?
- Could two genuinely different inputs produce the same selector value?
- Does the error branch catch a wrong input, or only a wrong derived key?
- Is any branch label doing double duty as the catch-all?
- Would the language's case construct express this directly, without a manufactured key?

## Notes
The failure this prevents is not a syntax mistake, and that is why it survives review. The version that switches on a peeled-off first character compiles, reads tidily, handles the intended inputs correctly, and has a default branch that looks like error handling. It is wrong about a category of input nobody enumerated, and the error branch's apparent coverage is what stops anyone from looking. Manufacturing a selector converts a question about the data into a question about a projection of the data, and every input that shares a projection is now indistinguishable.

The general principle underneath is that control structures and data structures are two views of the same shape. Data that is one of several alternatives wants a selective construct; data that is a repeated series wants a loop; data that is a fixed sequence of distinct items wants statements in order. When the construct and the data disagree, one of them is wrong, and it is nearly always cheaper to change the construct.

There is a live tension with a technique this book endorses elsewhere, and it is worth naming so the two do not get confused. Assigning a complicated expression to a well-named boolean or variable to clarify a test is good practice; manufacturing a variable so that a particular construct becomes usable is not. The difference is what the new variable is for — one names something the code already computes so a reader can see it, and the other creates a stand-in that the real data does not map onto cleanly.

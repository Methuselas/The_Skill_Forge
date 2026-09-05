---
object_id: DRILL_audit_identifier_names_in_a_code_review
object_type: drill
name: Audit the Names in a Change, Away From the Code
target_skill: Judging identifier names on their own terms instead of accepting them because the surrounding code explains them
library_path:
- software-engineering
- core
- readability
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- code_review
- readability
- deliberate_practice
cross_links:
- rel: supports
  target_object_id: PAT_review_names_outside_the_coding_moment
- rel: supports
  target_object_id: PAT_design_a_name_for_both_stm_and_ltm
- rel: related_to
  target_object_id: DRILL_rename_nondescriptive_code
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Audit the Names in a Change, Away From the Code

## Practice Task
Before reviewing a change, mechanically list every identifier it introduces, move that list somewhere the code is not visible, and judge the names there.

## Target Skill
Judging identifier names on their own terms instead of accepting them because the surrounding code explains them.

## Setup
A change under review, and a whiteboard or separate document. The separation is the mechanism, not a convenience — a name read in place is judged with the context that a future reader will not have.

## Instructions
1. List every identifier name in the changed code: variables, methods, classes, parameters. Do this mechanically, before forming any opinion about the change.
2. Move the list off the code. From here on you are answering questions about names, not about logic.
3. For each name, ask whether its meaning is clear knowing nothing about the code — in particular, whether you know what the words it is built from mean.
4. Mark any name that is ambiguous or unclear, and any that uses an abbreviation which could be read more than one way. Give each flagged name a stated reason drawn from one of these checks.
5. Find the names that resemble each other. For each such group, check whether the similar names actually refer to similar things — similar names for unrelated objects is the expensive case.
6. Run the two cognitive checks separately: does the formatting let you see the parts, and do the words connect to the domain, to a programming concept, or to a convention?
7. Take the syntactic pass last, using Butler's rules as the checklist — capitalization consistency, no doubled or external underscores, words rather than truncations, roughly two to four words, no type information encoded in the name.
8. Bring the flagged names back to the change and only then decide which are worth raising. Mark any you would have accepted had you read it in place.

## Success Check
- You raised at least one name you would have accepted had you read it in place.
- Every flagged name has a stated reason drawn from one of the checks, not "I would have called it something else."
- Groups of similar names have been checked for whether the similarity is meaningful.

## Common Failures
- Reviewing names in the diff. The context supplies the meaning and the check silently passes; this is the failure the whole drill is arranged to prevent.
- Turning it into a style argument. Steps 3 to 6 are about comprehension; the syntactic pass is deliberately last and smallest.
- Flagging every short name. Conventions are real information, and `i` in a loop is doing its job.
- Running it on your own code immediately after writing it, when you still hold the context the drill is trying to strip away.

## Notes
This combines two of Hermans's exercises. One supplies the review framing and the instruction that makes it work — list the names *outside* the code, on a whiteboard or in a separate document — along with the four questions about clarity, ambiguity, abbreviation, and similar names referring to similar objects. The other supplies the cognitive pass, asking of each name whether it supports the STM through its formatting and the LTM through domain words, programming concepts, and conventions.

Butler's rules are the source of the syntactic checklist in step 7. It is placed last on purpose. Hermans notes that rules about the precise formation of names can sound petty, and defends them on the grounds that unnecessary information causes extraneous load — a real but smaller effect than a name whose words mean nothing to the reader.

The reason the drill targets review specifically is that naming comes up in only about one in four code reviews. Left to arise naturally it mostly does not, and a mechanical listing step is what converts it from a thing reviewers sometimes notice into a thing they always check.

---
object_id: PAT_review_to_detect_not_to_correct
object_type: pattern
name: Review to Detect, Not to Correct
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- reviews
- inspections
- code_review
- collaboration
cross_links:
- rel: related_to
  target_object_id: PAT_put_review_effort_into_preparation_not_the_meeting
- rel: related_to
  target_object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
- rel: related_to
  target_object_id: PAT_review_names_outside_the_coding_moment
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Review to Detect, Not to Correct

## Pattern Rule
**IF** you are running or taking part in a review of someone else's work
**THEN** keep the activity on finding defects and off fixing them, and hold the author's role to acknowledging rather than defending.
**ELSE** where the group genuinely wants to design the fixes together, open a separate session once the review has formally closed, so the two activities do not compete for the same hour.

## Do
- Stop at recognition. The moment something is identified as a defect, record its kind and severity and move on — the discussion ends there. What the session produces is a list, not a set of solutions.
- Treat confusion as a finding in its own right. Some groups forbid debate over whether an alleged defect is really a defect, reasoning that if a reviewer was confused enough to raise it then something needs clarifying regardless of who turns out to be correct.
- Have the author acknowledge each item without arguing. Acknowledging is not agreeing — the author considers each point privately afterwards and keeps the final say on how every defect gets resolved, which is what makes acknowledging cheap enough to do consistently.
- Keep the roles distinct and give the moderating job to someone other than the author. Three participants is the minimum that allows a separate moderator, author, and reviewer, and merging any two of those removes the structure that makes the rest work.
- Feed the results back into the checklist. Recording the kinds of errors found lets the checklist grow toward the mistakes this group actually makes and shed the ones it has stopped making, which is what turns a review process into one that improves itself. Keep it to a page — longer ones do not get used at the level of detail a review needs.

## Don't
- Don't let review output reach a performance appraisal. The work under review is unfinished by definition, and evaluating people on it destroys the willingness to expose rough work that the entire technique depends on.
- Don't have general management in the room. Their presence changes what people are willing to say, and the only clean exception is when the material under review is a project plan and they are its author.
- Don't criticize the author instead of the work. A remark that anyone competent would already know something is outside the purpose of the meeting, and saying so is part of the moderator's job rather than an optional intervention.
- Don't drop or merge stages to save time. Organizations that have tried it generally found the saving smaller than the cost, and the self-correcting property depends on the feedback loop staying intact.
- Don't expect the author to absorb criticism gracefully by default. Some of what gets raised will not be defects and some will be debatable, and the author needs to know in advance that acknowledging everything and sorting it out later is the expected behaviour rather than capitulation.

## Checklist
- Is anyone proposing solutions in this meeting?
- When a defect is disputed, does the discussion stop or keep going?
- Is the author defending the work, or acknowledging and moving on?
- Could anything said here plausibly reach a performance review?
- Are the moderator and the author different people?
- Did anything learned here change the checklist?

## Notes
The separation of detection from correction is what keeps a review finite. Fixing is open-ended and interesting, and a group that starts designing a solution will spend the remaining time on one defect and never reach the rest of the material. Recording and moving on feels abrupt and is the only way a two-hour session covers what it was convened to cover — the fix is not being skipped, it is being done later by the person best placed to do it.

The rule against defending is doing something subtler than keeping the peace. If the author argues each point, every disputed item costs meeting time whether or not it turns out to be real, and the reviewers learn that raising a marginal observation is expensive. Since a good share of what gets found starts as a marginal observation, that cost suppresses exactly the material worth having. Acknowledging without agreeing keeps the raising cheap while leaving the judgment where it belongs.

There is a second-order effect worth knowing about, because it does not depend on the review finding anything. When people know their work will be examined, they examine it more carefully themselves before submitting it. Part of the return therefore arrives before the review starts and would not show up in any measurement of what the review caught — which is one reason the practice tends to be undervalued by anyone assessing it purely on defects found per hour.

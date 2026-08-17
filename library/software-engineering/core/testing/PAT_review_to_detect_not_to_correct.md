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
variants:
- variant_id: written_asynchronous_review
  variant_name: Carry the Remedy When the Review Is Written
  variant_basis: context
  difference_from_foundation: Each finding carries a suggested remedy and a priority alongside the defect, instead of stopping at recognition — because the constraint the foundation protects against, a shared hour consumed by designing one fix, does not exist when reviewers comment asynchronously and the author reads later.
  when_to_use: Written review of a submitted change, where reviewer and author work at different times and a bare defect report costs the author a round trip to find out what was meant.
  when_not_to_use: Any convened session with several people in it, where proposing fixes competes for the same clock as finding the remaining defects — and wherever a suggested remedy would be read as a required one by an author who does not feel free to decline it.
  absorbed_from_object_id: none
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

The absorbed variant `written_asynchronous_review` inverts the central rule for the setting most reviews now happen in, and it does so by attacking the foundation's reason rather than ignoring it. Stopping at recognition exists to protect a shared hour — with several people in a room, designing one fix spends the time the remaining defects needed. Written comments on a submitted change have no shared hour to protect. The reviewer writes when they are free, the author reads when they are free, and the cost that dominates is the round trip: a comment saying only that there are too many dependencies between two components leaves the author guessing at what was meant, and the next exchange happens hours or days later. So in that setting each finding carries three things — what the defect is, a concrete suggestion for addressing it, and how much it matters relative to the rest — and the author still decides, exactly as in the foundation. Use it for written review of a change; do not carry it into a convened session, and do not use it where a suggestion will be received as an instruction by someone who does not feel able to decline it.

There is a second-order effect worth knowing about, because it does not depend on the review finding anything. When people know their work will be examined, they examine it more carefully themselves before submitting it. Part of the return therefore arrives before the review starts and would not show up in any measurement of what the review caught — which is one reason the practice tends to be undervalued by anyone assessing it purely on defects found per hour.

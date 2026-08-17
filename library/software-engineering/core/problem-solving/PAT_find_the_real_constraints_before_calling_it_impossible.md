---
object_id: PAT_find_the_real_constraints_before_calling_it_impossible
object_type: pattern
name: Find the Real Constraints Before Calling It Impossible
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- problem_solving
- constraints
- assumptions
- design
cross_links:
- rel: related_to
  target_object_id: PAT_separate_essential_from_accidental_complexity
- rel: related_to
  target_object_id: PAT_choose_a_problem_representation_before_solving
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Find the Real Constraints Before Calling It Impossible

## Pattern Rule
**IF** a problem is resisting every approach and starting to look impossible
**THEN** stop attacking it and audit the constraints instead — sort the ones genuinely imposed on you from the ones you assumed — because a problem that admits no solution is usually being solved inside a boundary smaller than the real one.

## Do
- Write down every avenue you can think of, including the ones that sound unusable or stupid. Then go through the list and say why each cannot be taken, and for each reason ask whether you could actually prove it. The absurd entries are the point of the exercise: the reason one of them looks absurd is often an assumption, and the reason another does is a fact.
- Honour the constraints that turn out to be real, however irritating they are. The audit is for finding which ones are real, not for arguing your way out of them.
- Order the constraints by how much they restrict you and satisfy the tightest first, then fit the rest inside. A woodworker cuts the longest pieces first and takes the smaller ones out of what remains, and starting from the loosest constraint reliably paints you into the corner the tightest one was always going to occupy.
- Look for the freedom as deliberately as the restriction. Solutions live in the degrees of freedom you did not notice you had, and a solution gets dismissed early far more often than a constraint gets challenged.
- Run the short question list when it feels harder than it should be: is there an easier way; are you solving the actual problem or a peripheral technicality that grabbed your attention; what specifically makes this hard; does it have to be done this way; does it have to be done at all.

## Don't
- Don't keep trying the obvious approach because it ought to work. Repeating an approach that has already failed, on the grounds that there must be a way to make it work, is the recognisable shape of this failure and it can absorb days.
- Don't take a constraint on trust because it arrived with the project. Constraints handed over at the start were set under conditions that may have changed, and the interpretation placed on them may never have been checked.
- Don't treat "think outside the box" as the instruction. It presumes you know where the box is, and the problem is almost always that you have drawn it too small — the work is finding the real boundary, which is usually much larger than the one you have been working inside.
- Don't confuse a reinterpretation with a cheat. Reading the requirement differently is a legitimate solution when the new reading still satisfies the actual need; what makes it cheating is dropping a need, not dropping an assumed method.

## Checklist
- Which of these constraints could you prove, and which have you only assumed?
- Which is the most restrictive, and are you satisfying it first?
- What are you free to change here that you have been treating as fixed?
- Has anything on your rejected list been rejected without a reason you can state?
- Does this have to be done this way — and does it have to be done at all?

## Notes
The reframing that does the work is that the difficulty is rarely in the problem and rarely in your ability; it is in the boundary you are searching inside. That boundary is assembled from real constraints and from preconceived notions, and the two are indistinguishable from the inside because both simply feel like facts about the situation. Which is why the audit has to be explicit and written rather than done in your head — the assumed constraints are precisely the ones that never come up for review.

The enumerate-then-disprove step is the operational core and it is worth doing literally. Listing only the plausible avenues reproduces the boundary you already have; the value comes from the entries that seem not worth writing down, because forcing yourself to say why one of them is unavailable is what exposes the difference between "that would not work" and "I have never tried that." Getting troops inside a walled city by carrying them through the front gate would have been dismissed instantly by anyone listing only sensible options.

This sits next to the essential-versus-accidental split rather than duplicating it. That one sorts the *difficulty*: some of it is inherent to the problem and some was introduced by your solution, and only the second yields. This one sorts the *boundary*: which limits are actually imposed and which you supplied. They can both be live at once, and a problem can be genuinely hard in its essence while still being attempted inside a box two sizes too small.

---
object_id: PAT_plan_the_removal_while_you_build
object_type: pattern
name: Plan the Removal While You Are Still Building
library_path:
- software-engineering
- core
- refactoring
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- deprecation
- design
- migration
- maintenance
- lifecycle
cross_links:
- rel: related_to
  target_object_id: PAT_tell_obsolete_from_merely_old
- rel: related_to
  target_object_id: PAT_a_warning_migrates_nobody
- rel: related_to
  target_object_id: PAT_state_your_compatibility_promise_and_its_span
- rel: related_to
  target_object_id: PAT_make_every_milestone_a_place_you_could_stop
- rel: related_to
  target_object_id: AP_replace_a_system_that_is_still_in_use
reference:
  source_title: 'Software Engineering at Google: Lessons Learned from Programming Over Time'
  author: Titus Winters, Tom Manshreck, and Hyrum Wright
confidence: high
references: []
variants: []
---

# Plan the Removal While You Are Still Building

## Pattern Rule
**IF** you are designing something that other code will depend on and that will one day be superseded
**THEN** decide now how a consumer would get off it and how it could be replaced in pieces, and let those two answers shape the design
**ELSE** where you are not prepared to support it for as long as it will be needed, the decision to make is not to start it.

## Do
- Answer the migration question at design time, in one sentence a stranger could act on. If somebody depends on this and a better thing arrives, what exactly do they have to change? A design with no answer is a design that will be removed by attrition or not at all.
- Build it so it can be replaced in parts rather than only whole. A boundary that lets half the work move to a successor while the other half stays put converts an all-or-nothing migration into a sequence of steps, each of which can be finished.
- Keep the surface you expose narrower than the surface you have. Everything reachable becomes something depended on, and every dependency is a thread that has to be cut later — which makes hiding an implementation detail a decision about future removability, not only about present tidiness.
- Prefer an interface that could be satisfied by something other than this implementation. If the only thing that can sit behind it is what is behind it now, the interface is a description of the implementation and offers no migration path.
- Decide the intended lifespan explicitly and let it set the effort. Something meant to last a decade earns care about its exit that a tool for this quarter does not, and the failure is applying the same level to both.
- Treat the commitment as the decision point. Once it exists and people depend on it, the remaining options are supporting it, retiring it carefully, or letting it break — and all three cost something.

## Don't
- Don't defer the question on the grounds that removal is far off. The choices that make removal feasible are made early and are expensive to retrofit, which is precisely why they get skipped.
- Don't take on something you cannot commit to for as long as it will be needed. Building it is the cheapest part, and the obligation starts on the day somebody else builds on it.
- Don't confuse a migration plan with a migration tool. You need the plan at design time; the tool comes later, and it can only exist if the design left a path for it to follow.
- Don't design as though this will be the last version. Whatever replaces it will be different enough to be worth moving to, which means the seams you leave are the ones somebody will actually use.

## Checklist
- If something better arrives, what does a consumer have to change, stated concretely?
- Can this be replaced in pieces, or only all at once?
- What have you exposed that you would rather not have to keep working?
- Could anything other than the current implementation satisfy this interface?
- How long is this expected to live, and is the exit work proportionate to that?
- Is the organisation prepared to support this for that long?

## Notes
Other engineering disciplines treat this as unremarkable. A facility with a long life and a hazardous end state has its decommissioning considered while it is being designed, and money set aside for it — the eventual removal is a named phase of the project rather than an embarrassment nobody planned for. Software rarely does the equivalent, partly because the people drawn to building new things are not the ones who will dismantle them, and partly because planning the end of something you are excited to start feels like pessimism rather than diligence.

The two design questions do most of the work because they are answerable early and expensive later. How a consumer migrates off determines whether a future retirement is a coordinated change or an indefinite negotiation with people who have no reason to move; and whether the thing can be replaced piecewise determines whether the retirement can be broken into finishable steps or has to be attempted as one enormous cutover. Both are decided by where the boundaries sit, which is a decision made once, at the beginning, and effectively frozen afterwards.

The commitment point is worth stating plainly because it is where the real choice lives. Building something is a small cost paid once. Supporting it is a larger cost paid continuously by whoever inherits it, and it begins the moment somebody else depends on it. After that, all three remaining paths — support, careful retirement, or letting it break — cost something, and none of them is free. Which means the honest version of the question at the start is not whether this is worth building, but whether it is worth keeping.

---
object_id: PAT_fix_or_board_up_a_broken_window
object_type: pattern
name: Fix a Broken Window Now, or Board It Up Where Everyone Can See
library_path:
- software-engineering
- core
- code-quality
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- entropy
- maintenance
- technical_debt
cross_links:
- rel: related_to
  target_object_id: PAT_invest_in_quality_over_hacky_shortcut
- rel: related_to
  target_object_id: PAT_move_code_across_a_named_quality_boundary
- rel: related_to
  target_object_id: PAT_improve_the_code_when_you_cannot_improve_the_process
- rel: related_to
  target_object_id: PAT_diagnose_why_the_code_degraded_before_changing_it
reference:
  source_title: 'The Pragmatic Programmer: From Journeyman to Master'
  author: Andrew Hunt and David Thomas
confidence: high
references: []
variants: []
---

# Fix a Broken Window Now, or Board It Up Where Everyone Can See

## Pattern Rule
**IF** you have found a bad design, a wrong decision, or a piece of poor code
**THEN** repair it while you are looking at it
**ELSE** where there is genuinely no time to repair it properly, board it up — comment the offending code out, replace it with an explicit "not implemented", substitute obvious dummy data — so that the damage is contained and visibly acknowledged rather than left looking like working code.

## Do
- Treat the first unrepaired defect as the expensive one. Decay is not gradual accumulation; it is a threshold effect, and what crosses the threshold is the signal that nobody is minding the code. One flaw left standing licenses the next.
- Board it up rather than leaving it silent. The point of the boarding is that it is *visible*: it says a person knows about this and is on top of it, which is the opposite message from a quiet defect sitting in code that otherwise looks maintained.
- Separate the two decay mechanisms, because they need different responses. A broken window is code where people **stopped caring**, since it appeared that nobody else did. A boiled frog is drift that nobody **noticed** — a system moving away from its specification one feature at a time, patch upon patch, until nothing of the original is left. The first needs a repair anyone can see; the second needs somebody periodically looking at the whole rather than the part.
- Bank the effect in the other direction. Code that is clean throughout recruits care from everyone who touches it, exactly as a fire crew rolls out a mat before dragging hoses across a clean carpet. The tidiness is not decoration — it is what makes the next person unwilling to be the first to make a mess.
- Watch for the specific thought that marks the threshold being crossed: *the rest of this is bad, so mine may as well be.* Once that reasoning is available, quality stops being defended by anyone.
- Confine the repair to code your team actually maintains. Outside that line the move is to raise what you found with whoever owns it — ask what the constraint was before proposing the fix — rather than to restructure it where you stand.

## Don't
- Don't tell yourself there is no time to clean up the glass. There is less time later, and the bill arrives as a section of the system nobody is willing to touch.
- Don't let boarding up become the repair. It is a holding action with a visible marker, not a resolution, and a board left in place long enough is itself a broken window.
- Don't excuse a mess by pointing at the mess around it. That is the mechanism, stated as though it were a justification.
- Don't silently rearrange a team's code because you were passing through and knew better. Whoever maintains it navigates by remembering where things are, and that memory is what they use to find a fault under incident pressure — arriving to find nothing where they left it costs them exactly when it is most expensive.

## Checklist
- Did you fix the flaw you just found, or walk past it?
- If you could not fix it, is the damage now contained and obvious to the next reader?
- Is this decay because people stopped caring, or because nobody noticed?
- What would someone conclude about how much this codebase is cared for, from the section in front of them?
- Is this code yours to repair, and if not, who did you tell?

## Notes
The observation this rests on comes from urban decay research rather than from software: one broken window left unrepaired reliably converts an intact, occupied building into a derelict one, because the unrepaired window communicates abandonment and abandonment is contagious. The experimental version is sharper still — an abandoned car sat untouched for a week, and was stripped within hours of a single window being broken. Neglect is not a slow leak; it is a signal, and it is acted on quickly.

What makes the software version worth its own card is that the countermeasure is not simply "fix things." It is that when you cannot fix something, you must still act *visibly*, because the damage the defect does is mostly to the belief that the code is maintained. Commenting out the offending section, or leaving an explicit unimplemented marker, costs almost nothing and preserves that belief; leaving a quiet flaw in code that otherwise looks fine is what spends it.

The ownership boundary is the limit on all of this, and without it the rule reads as a licence to repair anything you can see. The cost of crossing it is not offence at having one's work altered, though that happens; it is that the people responsible for a region navigate it from memory, and that memory is the instrument they reach for when something breaks at an inconvenient hour. Restructuring their code improves it by every static measure while degrading the one thing that only they possess. So the boundary is not about etiquette — the repair genuinely makes their situation worse, and the version that helps is a conversation that starts by asking what the awkward part was for. That question is also the one most likely to reveal that the awkwardness was load-bearing.

Pairing this with the boiled frog is the part most often dropped, and the two mechanisms genuinely differ. Broken windows are a *motivation* failure — the standard is visible and people stop upholding it. The frog is a *perception* failure — nothing looks wrong at any single step, and the accumulated drift is only apparent against the original intent. Fixing windows does nothing about the frog, and periodically stepping back to compare the system against what it was meant to be does nothing about windows. Both are needed, and neither substitutes for the other.

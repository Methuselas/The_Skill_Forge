---
object_id: PAT_produce_a_second_design_before_committing
object_type: pattern
name: Do Not Stop at the First Design That Would Work
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- iteration
- heuristics
- alternatives
cross_links:
- rel: related_to
  target_object_id: PAT_separate_essential_from_accidental_complexity
- rel: related_to
  target_object_id: PAT_keep_a_toolbox_instead_of_adopting_one_methodology
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Do Not Stop at the First Design That Would Work

## Pattern Rule
**IF** you have arrived at a design that looks good enough and are about to start building on it
**THEN** produce at least one more candidate first, because the second attempt is nearly always better and each attempt teaches something that improves the result.
**ELSE** when a further attempt would only re-derive what you already have, stop — the point is a genuinely different approach, not another draft of the same one.

## Do
- Change the medium when the approach stalls. If a diagram is not working, write it in English; write a short test program; sketch a brute-force version. Keep outlining and the thinking tends to follow.
- Range deliberately between the high-level and low-level views. The big picture puts the details in perspective and the details keep the high-level decisions honest; the tension between the two produces a more stable structure than working purely in one direction.
- Take the brute-force option seriously as one of the candidates. A brute-force solution that works beats an elegant one that does not, and elegance can take a long time to get right — the binary search was described in 1946 and it took another sixteen years for anyone to publish a version that handled lists of every size correctly.
- Leave an issue open when you lack the information to settle it. Recognise that a point needs deciding, note that you cannot decide it yet, and come back with more experience of the design rather than making a poor decision now.
- Walk away when stuck. Putting a problem out of mind for a while often produces a result faster than continued persistence does.
- Stop once the candidates you hold would all work. The goal at that point is a good solution and the avoidance of disaster, not the best solution — and the signal is not confidence in a winner but the moment when further comparison stops telling you anything new about any of the options.

## Don't
- Don't treat design as a process that should look tidy while you are doing it. The finished design should be clean; the process that produced it involves false steps and blind alleys, and making those mistakes is the point — a mistake in a design is far cheaper than the same mistake found after it is coded.
- Don't expect a definition of the problem before you have solved some of it. A wicked problem can be clearly defined only by solving it, which means the first pass is partly an act of discovery rather than a failed attempt at the answer.
- Don't read a single acceptable design as *the* design. Send three people to design the same program and three very different, perfectly acceptable designs come back.
- Don't stop because you are uncomfortable leaving a design cycle without closure. That discomfort fades once you have deliberately left issues unresolved a few times and watched them resolve more easily later.

## Checklist
- How many genuinely different candidates do you have — not drafts, but different approaches?
- What did the first attempt teach you that the second one should use?
- Is there a brute-force version, and have you honestly compared it rather than dismissing it?
- Which decisions are you deferring on purpose, and which are you avoiding?
- Have you looked at this from both the top-level and the detail view, or only one?

## Notes
The property that makes this pay is that design cycles are short and their effects downstream are large, so the arithmetic favours spending another cycle. That is the opposite of the intuition, which treats reaching a workable design as the finish line and further exploration as indulgence.

Underneath sit four attributes of design that together explain why one pass is not enough. It is a *wicked* problem — definable only by solving it, the way the Tacoma Narrows bridge's designers could not know aerodynamics mattered until the bridge tore itself apart. It is *nondeterministic*, with many acceptable answers rather than one right one. It is *heuristic*, so the techniques are rules of thumb that worked somewhere before rather than procedures guaranteed to work here. And it is *emergent*: designs do not arrive fully formed but improve through review, discussion, and the experience of writing and revising the code.

The hard question this raises is when the design is good enough, and the honest starting position is that the activity is open-ended and the usual answer in practice is "when you're out of time" — an admission rather than a rule. The answer is that the returns shift once alternatives exist. Generating a second genuinely different candidate pays well, because before it there was nothing to choose between; ranking three workable candidates pays much less, because all three working already bounds how wrong the outcome can be. So the stopping point is not a feeling of having found the best design, it is the moment further comparison stops producing new information. That is a stopping rule rather than only a habit, and it does not soften the card at all — stopping at the *first* idea remains the failure this exists to prevent, and none of it applies until real alternatives are in hand. It also does not apply where a merely workable choice is itself the disaster, which is the case for load-bearing decisions later work cannot escape.

---
object_id: PAT_diagnose_why_the_code_degraded_before_changing_it
object_type: pattern
name: Work Out How the Code Got This Way Before You Improve It
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- maintenance
- technical_debt
- diagnosis
- legacy_code
cross_links:
- rel: related_to
  target_object_id: PAT_fix_or_board_up_a_broken_window
- rel: related_to
  target_object_id: PAT_improve_the_code_when_you_cannot_improve_the_process
- rel: related_to
  target_object_id: PAT_look_for_the_evidence_outside_the_code
- rel: prerequisite_for
  target_object_id: PAT_make_every_milestone_a_place_you_could_stop
reference:
  source_title: 'Refactoring at Scale: Regaining Control of Your Codebase'
  author: Maude Lemaire
confidence: high
references: []
variants: []
---

# Work Out How the Code Got This Way Before You Improve It

## Pattern Rule
**IF** you have found code bad enough that you want to restructure it
**THEN** establish first whether it decayed because the demands on it moved or because it was built under pressure it could not meet, since the two have different centres and a fix aimed at the wrong one lands on the wrong part of the code
**ELSE** where the history is genuinely unrecoverable, say so and design for the behaviour you can observe, rather than inventing a story that makes the current shape look like carelessness.

## Do
- Ask what changed since it was written, before asking what is wrong with it. Demands move underneath working code in ways nobody could have priced at the time — a load assumption outgrown, a standard revised, a platform that shifted beneath a correct implementation, a dependency drifting far enough that catching up became a project. None of that is carelessness, and a rewrite that treats it as carelessness will reproduce the original design with better names.
- Use the original authors' own words as the test when you can reach them. People who say *we didn't know that* or *at the time we thought* are describing demands that moved. People who say *that was never any good* or *we were racing a deadline* are describing corners cut knowingly. The distinction arrives in one sentence and would take you days to derive from the code.
- Go to the team that inherited the code when the authors have gone. Context is usually handed over even when people are not, and someone can generally say why a strange decision was strange.
- Look for what the original solution got right, not only what it got wrong. Constraints it worked around and failure modes it avoided are the parts most easily lost in a rewrite, and losing them is how a cleaner implementation reintroduces a bug that was solved years ago.
- Treat a deliberate shortcut as a decision with a rationale rather than a defect. Shipping something scrappy is occasionally the correct call, and the record of *why* tells you whether the pressure that produced it still applies.
- Watch for the code that exists to paper over something else. A routine that quietly rewrites data after the fact, or a check that exists for no visible reason, usually encodes a constraint nobody wrote down — and history plus conversation archives will often explain it well enough to tell you whether it is still needed.

## Don't
- Don't start from the assumption that everything you dislike is debt. It is the cheaper explanation and the more flattering one, and it produces a solution weighted toward whatever is currently most irritating rather than toward whatever is actually structural.
- Don't let the reaction on first reading set the scope. The passage that provokes it is frequently a symptom sitting downstream of the real problem, and a change targeted there leaves the cause untouched while feeling productive.
- Don't rewrite a workaround before finding out what it works around. Every awkward line was solving something, and the fact that you cannot see what does not mean nothing was there.
- Don't confuse this with excusing the state of the code. The point of the reconstruction is a better repair, not a verdict on whoever wrote it.

## Checklist
- Which is this — demands that moved, or corners knowingly cut, or both in identifiable proportions?
- What did this code have to be true of the world when it was written, and is any of it still true?
- Have you spoken to anyone who was there, or read anything they wrote at the time?
- What is this implementation handling well that a clean rewrite would drop?
- Is the target of your planned change the thing that annoyed you, or the thing that caused it?

## Notes
The failure this prevents is specific and easy to walk into: reading badly-aged code, feeling the reaction it provokes, and starting immediately. What comes out is a solution shaped by the most acute irritation rather than by the underlying fault, and it usually attacks a symptom while the cause carries on producing more of them. Reconstructing the history first moves the target, and it moves it before any effort has been spent going the wrong way.

The two categories matter because they imply different work. Where the demands moved, the code was fit and the world was not stationary — so the useful question is what the demands are now and whether they will move again in the same direction, which is a design question about the next several years. Where corners were cut under pressure, the design was known to be wrong on the day it shipped, the shortcuts are usually enumerable, and the question is whether the pressure that produced them still exists. Confuse the first for the second and you rebuild for requirements that have already left; confuse the second for the first and you go looking for a sophisticated reason behind something that was simply rushed.

The authors' phrasing is worth treating as a real instrument rather than an anecdote. Someone who worked on a system will characterise it accurately in a sentence or two if asked directly, and that sentence sorts the code into the right category faster than any amount of reading. It also surfaces the constraints that never made it into a comment — the reason for the odd check, the thing that broke once and led to the strange guard — which is exactly the material a rewrite destroys silently and rediscovers expensively.

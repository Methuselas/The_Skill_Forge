---
object_id: PAT_let_name_length_signal_scope
object_type: pattern
name: Let a Name's Length Signal Its Scope
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- scope
- loops
- readability
cross_links:
- rel: related_to
  target_object_id: PAT_start_a_variable_at_the_narrowest_scope
- rel: related_to
  target_object_id: PAT_minimize_variable_span_and_live_time
- rel: related_to
  target_object_id: PAT_use_descriptive_names
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Let a Name's Length Signal Its Scope

## Pattern Rule
**IF** you are deciding how long to make a name
**THEN** treat the length itself as a message about reach — a very short name promises the reader that this value means nothing beyond the next few lines, and anything living longer than that has to pay for a longer name.
**ELSE** when you cannot honestly make that promise, lengthen the name; the promise is what the convention is made of, and a short name on a far-reaching value spends everyone's credit rather than yours.

## Do
- Read a one-character name as a claim rather than as laziness. Naming something `i` states that it is a run-of-the-mill loop counter or array index with no significance outside these few lines, and a reader is entitled to act on that without checking.
- Scale in both directions. Longer names serve rarely used and widely visible values better; shorter names genuinely do serve local and loop variables better, so this is not a one-way push toward length.
- Promote the name the moment the value outlives its loop. Something counting records that is still wanted after the loop finishes is `recordCount`, and calling it `i` misreports its reach.
- Name nested loop indices for what they index. `score[teamIndex][eventIndex]` states which subscript is which; `score[i][j]` makes the reader remember. The specific failure this prevents is index cross-talk — writing `i` in the place where `j` was meant, which the compiler cannot catch because both are in scope and both are integers.
- Keep `i`, `j`, and `k` for simple loop indices if you use them at all. The convention is established firmly enough that borrowing them for anything else is worse than picking a fresh name.

## Don't
- Don't leave a short index in a loop that has since grown. Loops lengthen as code is changed, extended, and copied between programs, and once one runs past a few lines the reader has already lost track of what the index stood for.
- Don't take this as licence to abbreviate generally. The signal works only because brevity is reserved for small scope; short names for far-reaching values do not merely fail locally, they teach readers to stop trusting the signal everywhere.
- Don't let the length rule stand in for the content rule. A short name still has to be the right short name, and short names carry enough other problems that some careful programmers refuse them entirely as a defensive policy.

## Checklist
- Does anything outside these few lines depend on this value?
- Has this loop grown past the point where a single letter is still readable at a glance?
- In a nested loop, can a reader tell which subscript belongs to which dimension without counting?
- If this name is one character, is it a simple index and nothing else?
- Would the honest name for this be long? If so, is the scope wider than you intended?

## Notes
Length as a signal is worth separating from length as a quality, because the two give opposite advice about `i`. Judged on descriptiveness alone, a single letter is always worse than a word. Judged as a message about reach, a single letter says something true and useful that `loopIndex` does not — that this value is disposable. The research points the same way: longer names suit rarely used and global variables, shorter ones suit local and loop variables, so the question is not how descriptive to be in general but how much reach the name has to account for.

What makes this fragile is that it is a shared convention rather than a local choice. It only pays while everyone honours it, and each far-reaching value given a two-letter name teaches readers that short names cannot be trusted to mean anything — at which point the convention stops working for the people who kept it. That is the argument for treating a violation as a real defect rather than a stylistic one.

The last checklist question is the useful one to carry away, because it runs the rule backwards. If the only honest name for something is long, the length is telling you the value reaches further than you meant it to, and the fix may be to narrow the scope rather than to accept the name.

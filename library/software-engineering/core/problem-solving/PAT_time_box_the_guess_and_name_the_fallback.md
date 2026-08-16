---
object_id: PAT_time_box_the_guess_and_name_the_fallback
object_type: pattern
name: Time-Box the Guess and Name the Fallback
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- debugging
- estimation
- sunk_cost
- brute_force
cross_links:
- rel: related_to
  target_object_id: AP_find_a_defect_by_hypothesis_not_by_guessing
- rel: related_to
  target_object_id: PAT_fix_the_cause_not_the_symptom
- rel: related_to
  target_object_id: PAT_produce_a_second_design_before_committing
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Time-Box the Guess and Name the Fallback

## Pattern Rule
**IF** you are about to attack a hard problem with a quick approach that might work
**THEN** first name a slower approach that is guaranteed to work, then give the quick one a time limit and switch when it expires.
**ELSE** where no guaranteed approach exists at any price, say so explicitly — that is a different situation and it changes what the time limit is for.

## Do
- Ask the question before starting rather than after getting stuck. If I do not crack this quickly, what is something I am certain would work? Having an answer in hand is what makes abandoning the quick attempt a decision rather than a defeat.
- Accept that the guaranteed option is usually tedious. Reviewing the whole broken section, rewriting it from scratch, building a harness around it and testing it in isolation, stepping a long loop by hand, instrumenting it heavily, running it under a different compiler or in a different environment — none of these are clever and all of them terminate.
- Set the limit before you begin, out loud or in writing. A limit chosen afterwards is negotiated against the effort already spent, which is precisely the judgment the limit exists to remove.
- Price the fallback against the right baseline. The reaction to a brute-force option is that it is too much work, and that is only true if it costs more than the quick approach *actually* costs — which is not the five minutes it promises but the hours it can consume.
- Take the same reading on the code itself. Two hours spent debugging something that took thirty minutes to write is a signal that rewriting it was the cheaper route from the beginning, and the ratio is worth noticing while it is still two hours.

## Don't
- Don't let the quick approach become a matter of principle. The risk is not that the five-minute attempt fails; it is that having committed to it, finding the defect *that way* turns into the goal, and the hours go by unproductively because switching would concede something.
- Don't confuse having a fallback with using it. Naming the guaranteed approach costs nothing and most of the time you never reach it — its job is to make the time limit enforceable, not to be the plan.
- Don't set a limit you have no intention of honouring. A limit that always gets extended is the same as not having one, with an added feeling of rigour.
- Don't apply this to the diagnosis and skip it for the correction. The same gambler's reasoning produces the special-case patch, for the same reason — it promises to be quicker than understanding.

## Checklist
- What is the approach here that is guaranteed to work, however tedious?
- How long is the quick attempt allowed to run?
- Has that limit already passed?
- How long did this code take to write, and how long have you now spent on it?
- Are you continuing because it is working, or because you have already spent time on it?

## Notes
The failure this prevents is a sunk-cost trap with a specific trigger. Each individual decision to keep going is defensible — you are closer than you were, one more idea is worth trying, switching now wastes what you have done — and the sequence of defensible decisions is what produces the lost afternoon. A limit set in advance is the only version of this judgment made by someone with no stake in the outcome, which is why it has to be set before rather than during.

Naming the fallback first does something the time limit alone cannot. Without it, expiry leaves you with no plan and the natural move is to keep guessing, since the alternative is undefined. With it, expiry is a switch between two known options rather than an admission that you are stuck. That is also why the fallback should be identified while you are calm at the start, not while frustrated in the middle.

The ratio between writing time and debugging time is a useful running instrument beyond this one decision. Code that consistently costs several times more to debug than it cost to write is telling you something about how it was built, and the appropriate response is upstream — in how the next piece gets designed and checked — rather than in getting better at debugging this one. Debugging skill has a ceiling; not needing it has a higher one.

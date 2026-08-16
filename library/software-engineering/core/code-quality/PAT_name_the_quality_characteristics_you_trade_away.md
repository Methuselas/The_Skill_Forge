---
object_id: PAT_name_the_quality_characteristics_you_trade_away
object_type: pattern
name: Name the Quality Characteristics You Are Trading Away
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- quality
- tradeoffs
- objectives
- design
cross_links:
- rel: related_to
  target_object_id: PAT_evaluate_code_against_quality_goals
- rel: related_to
  target_object_id: PAT_set_the_robustness_level_deliberately
- rel: related_to
  target_object_id: PAT_expect_a_design_maneuver_to_cost_another_dimension
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Name the Quality Characteristics You Are Trading Away

## Pattern Rule
**IF** you are deciding what good means for this system, or handing that decision to people who will build it
**THEN** name the two or three specific characteristics being optimized, and name what optimizing them costs the others, because they conflict in mapped and largely predictable ways.
**ELSE** where two characteristics reinforce each other rather than compete, take both — the trade only binds on the pairs that actually pull against one another.

## Do
- Separate what the user experiences from what only you do. Correctness, usability, efficiency, reliability, integrity, adaptability, accuracy, and robustness are visible from outside. Maintainability, flexibility, portability, reusability, readability, testability, and understandability are visible only to whoever works on the code. Users care about the first list exclusively, and the second list matters because it eventually reaches the first.
- State the goals out loud to whoever is building. Five teams were given one program, the same five objectives, and each told to optimize a different one — four finished first on their assigned objective and the fifth finished second, while none did well across the board. People optimize what they are asked to optimize, and in the absence of an instruction they optimize something anyway.
- Learn the two most destructive priorities, because both look virtuous. Optimizing efficiency damages correctness, reliability, integrity, adaptability, and accuracy while helping nothing but itself. Optimizing robustness damages correctness, efficiency, reliability, integrity, and accuracy, helping only usability and adaptability.
- Bank the pairs that reinforce. Correctness and reliability help each other, as do adaptability and robustness — where two goals pull the same way there is no decision to make and no cost to account for.
- Settle correctness against robustness explicitly, because they oppose each other in both directions. Correctness means never producing a wrong answer, so the right move on bad input may be to produce nothing. Robustness means continuing to run, so the right move may be to produce something approximate. Which one applies is a fact about the domain, not about the code.

## Don't
- Don't use the word quality as though it named one dimension. It covers at least fifteen characteristics that interact, and people told to improve quality without being told which one will improve whichever is cheapest to improve.
- Don't treat the interaction map as a law. It describes typical relationships, and any given project can invert one — the value is in prompting you to check each pair you actually care about rather than in memorizing the grid.
- Don't let internal characteristics be surrendered quietly on the grounds that nobody outside sees them. Nobody does, and code that cannot be maintained becomes incorrect over time while code that cannot be changed eventually becomes unusable.
- Don't expect a team to infer the priority from context. The experiment's result is that they will infer *a* priority, and it will be the one that is easiest to achieve or most recently rewarded.

## Checklist
- Which two or three characteristics is this system optimizing, and can everyone building it name them?
- For each one, which others does focusing on it damage?
- Is correctness or robustness the priority here, and is that written down anywhere?
- Which internal characteristic are you spending, and which external one will that eventually surface as?
- Have you checked the pairs you care about, rather than assuming the typical relationships hold?

## Notes
The finding that makes this more than a taxonomy is that the characteristics are mapped against each other, and the map is not symmetric or intuitive. Efficiency is the clearest example — it reads as an unambiguous good, and pursuing it degrades five of the seven other external characteristics while improving none of them. A team told to make the system fast will make it fast, and will also make it less correct, less reliable, less adaptable, less accurate, and weaker on integrity, without anyone having decided that.

The experiment behind the second point is worth holding precisely because its result is unremarkable in isolation and alarming in aggregate. That people hit the target you give them is not surprising. That they hit it *at the cost of every other target*, reliably, across five different objectives, is the part that changes what you do — because it means an unstated priority is not a neutral position. It is a decision to let whoever is closest to the code pick, and to have them pick differently in different parts of the system.

This sits underneath the four-goal evaluation rule rather than beside it. That rule asks whether a given piece of code is good, using goals that mostly reinforce each other. This asks the prior question of which kind of good this system is aiming at, on a wider list where the goals genuinely compete. The two are compatible, and the order matters — deciding what you are optimizing comes before judging whether you achieved it.

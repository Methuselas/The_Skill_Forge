---
object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
object_type: pattern
name: Combine Detection Techniques Rather Than Perfecting One
library_path:
- software-engineering
- core
- testing
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- defect_detection
- inspections
- testing
- reviews
cross_links:
- rel: related_to
  target_object_id: PAT_understand_the_routine_before_the_compiler_sees_it
- rel: related_to
  target_object_id: PAT_design_for_testability
- rel: related_to
  target_object_id: PAT_name_the_quality_characteristics_you_trade_away
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Combine Detection Techniques Rather Than Perfecting One

## Pattern Rule
**IF** you are deciding how to catch defects in a piece of work and are reaching for the technique you trust most
**THEN** use two or three different ones instead, because no single technique catches much more than half of what is there and different techniques catch different things.
**ELSE** where only one technique is available, at least apply it twice with different people, which is nearly as effective as adding a second technique.

## Do
- Calibrate against the ceiling rather than against your confidence. Typical detection rates for individual techniques cluster around forty percent, and no common technique's typical rate exceeds about seventy-five percent. Unit testing and integration testing — the two most relied upon — sit near thirty to thirty-five.
- Add a second pair of eyes before adding a second method. When experienced programmers hunted for known defects in one program, no individual technique beat any other by a statistically meaningful margin, but any combination of two — *including two independent groups using the same technique* — roughly doubled the total found. Only about a fifth of the defects found by inspection were found by more than one inspector.
- Pair a human technique with a machine one deliberately, because they find different categories. Reading code surfaces more interface defects; running it surfaces more control-flow defects. Choosing between them is choosing which category to leave in.
- Spend early where the technique finds cause as well as symptom. A review or inspection identifies the defect and its reason together; a failing test tells you a symptom exists and leaves the diagnosis to you. That single-step-against-two-step difference is why measured find-and-fix costs run around three hours per defect for inspection against roughly twelve for testing.
- Read a suspiciously good result as a property of the practice mix rather than as magic. Development styles that report unusually high defect removal generally do so because they stack several detection practices — pair review, desk checking, unit test, integration test, regression test — and the cumulative figure is what you would predict from the individual rates.

## Don't
- Don't let testing carry the whole load. A combination of unit, functional, and system testing frequently reaches under sixty percent cumulative detection, which is not enough for production work, and the gap does not close by testing harder.
- Don't assume a second reviewer is redundant because the first was competent. The overlap between two inspectors is small, which is exactly why the second one pays — competence is not the variable, and the low overlap means the marginal reviewer finds nearly new material.
- Don't conclude that informal review has covered the code. Informal approaches typically reach only half to sixty percent coverage unless something is measuring it, and the impression of thoroughness is not correlated with the number.
- Don't treat these figures as targets to hit. They are there to correct an estimate — most people substantially overestimate how much any single technique catches, and that overestimate is what makes a one-technique plan look sufficient.

## Checklist
- How many distinct detection techniques will this work pass through?
- If only one, can it at least be applied twice by different people?
- Is there both a reading technique and an executing one, or only one kind?
- Which technique here finds causes rather than only symptoms, and is it applied early?
- What cumulative detection rate do the chosen techniques actually imply?

## Notes
The number that changes behaviour is the ceiling. Most people's working assumption is that a technique they apply carefully catches most of what is there, and the measured reality is that a typical one catches about forty percent and the best common ones do not reach eighty. Once that is believed, a plan resting on one technique stops looking like diligence and starts looking like a decision to ship the majority of the defects.

The two-independent-groups result is the most useful single finding here and the least intuitive. Adding a second reviewer using the *same* method as the first roughly doubles the yield, which only makes sense once you see that the limiting factor is not the method's power but which defects a particular person happens to notice. Overlap between inspectors is around a fifth. That reframes review capacity as a coverage problem rather than a skill problem, and it means the cheapest available improvement is usually another person rather than a better technique.

The one-step-against-two-step distinction is what makes the cost comparison hold up, and it is easy to miss because it is not about detection at all. A test that fails has told you a symptom exists somewhere; the diagnosis is separate work, often the larger half. A review that finds a defect has already located it, because the reviewer was looking at the cause when they found it. That is why inspection costs less per defect end-to-end even where it is slower per hour of effort, and it is the same reason that checking a routine by reading it before running it pays.

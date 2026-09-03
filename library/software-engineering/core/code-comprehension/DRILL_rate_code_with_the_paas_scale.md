---
object_id: DRILL_rate_code_with_the_paas_scale
object_type: drill
name: Rate the Effort a Piece of Code Costs You, and Say Why
target_skill: Noticing which specific properties of code drive your own cognitive load, rather than only that some code felt hard
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- cognitive_load
- code_comprehension
- deliberate_practice
- measurement
cross_links:
- rel: supports
  target_object_id: PAT_separate_intrinsic_from_extraneous_load
- rel: supports
  target_object_id: PAT_diagnose_a_code_smell_by_the_cognitive_process_it_breaks
- rel: related_to
  target_object_id: PAT_diagnose_source_of_code_confusion
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Rate the Effort a Piece of Code Costs You, and Say Why

## Practice Task
Read an unfamiliar piece of code, rate the mental effort it cost on a nine-point scale, and write down what specifically caused that rating.

## Target Skill
Noticing which specific properties of code drive your own cognitive load, rather than only that some code felt hard.

## Setup
A piece of code you have not read before, and the nine-point scale with a second column for reasons. No instruments — the point of this drill is that you do not need any.

## Instructions
1. Pick code you have not read before, and state that it is unfamiliar. Familiar code will not produce a useful rating, since most of the load has already been paid.
2. Read it until you could explain what it does.
3. Record a rating of the mental effort on the Paas Scale's nine points, from very, very low mental effort through neither high nor low to very, very high mental effort. Write the number down before writing anything else.
4. In the second column, write *why* — the part the bare rating cannot carry. Was it a long parameter list, an unfamiliar construct, information spread across files, a name that turned out to mean something else? Where a reason names only a state of the reader rather than something about the code, mark it as such.
5. Separate the load coming from the problem from the load coming from how the code was written, and identify one case of each.
6. Repeat across several pieces of code over time and read your reasons back together, naming any driver that recurs. The individual ratings matter less than the pattern in what keeps driving them up.
7. Where a reason names a specific smell or a name-behaviour contradiction, route it to the matching diagnosis rather than leaving it as a feeling.

## Success Check
- The code was genuinely unfamiliar and this is stated. A rating on code already read measures recall, and the scale cannot tell the two apart.
- The rating is recorded before the reason is written, so the reason explains the number rather than the number drifting to fit a tidy explanation.
- Every reason names something about the code — a construct, a distance, a name that misled — and any reason naming only a state of the reader is marked as such rather than counted.
- Across entries at least one recurring driver is named and is specific enough to act on. "Complexity" recurring is the absence of a finding rather than a finding. A recurrence needs several entries and therefore several sittings, so a first run records its entry and leaves this open; a driver called recurring on the strength of one reading is a preference reported as a pattern.
- Load from the problem is separated from load from the writing, with one case of each identified. A run attributing everything to how the code was written has not made the distinction the scale exists to support.

## Common Failures
- Rating without the reason column, which produces a number that cannot be acted on.
- Rating familiar code, where the score reflects your prior exposure rather than the code.
- Treating the scale as precise. It is one question with nine points and it is not clear participants can reliably tell very high from very, very high; the value is in the reason and the trend.
- Reaching for a wearable instead. Hermans's own conclusion is that biometric methods largely correlate with this scale, so a fitness tracker adds cost rather than accuracy.

## Notes
The Paas Scale is the standard self-report instrument for cognitive load, designed by Fred Paas, and it has known limits — a single question, and unclear resolution at the extremes. Hermans presents it with those criticisms attached and recommends it anyway, which is the right posture for a tool used on yourself rather than in a study.

What makes the recommendation credible is the alternative it was compared against. The chapter surveys the instrumented options in some detail: eye tracking, where blink rate falls and pupil size rises with load, on the hypothesis that the brain is maximising visual intake on a hard task; skin temperature and sweat; EEG; and fNIRS, which infers load from oxygenated haemoglobin via infrared light. Nakagawa's fNIRS study found greater oxygenated blood flow on a deliberately complicated version of a C algorithm for 8 of 10 participants, with functionality held constant. All of it correlates with the nine-point question, which is why the drill uses the question.

Exercise 9.3 is the source of this drill. The addition here is the repetition across several pieces of code, because a single rating tells you about one file while a run of them tells you about yourself.

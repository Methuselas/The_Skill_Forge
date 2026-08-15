---
object_id: PAT_separate_essential_from_accidental_complexity
object_type: pattern
name: Ask Whether the Difficulty Is in the Problem or in Your Solution
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
- complexity
- design
- simplicity
- diagnosis
cross_links:
- rel: related_to
  target_object_id: PAT_produce_a_second_design_before_committing
- rel: related_to
  target_object_id: PAT_ask_what_should_be_hidden
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u05, pp. 77-80, 105, 124
  evidence_type: text
confidence: high
references: []
variants: []
---

# Ask Whether the Difficulty Is in the Problem or in Your Solution

## Pattern Rule
**IF** a piece of design or code is proving hard and you are about to push harder at it
**THEN** first sort the difficulty into essential — inherent to the problem being solved — and accidental — introduced by your solution, tools, or framing — and attack the accidental part, because only that part will yield to being pushed.

## Do
- Test each source of difficulty by asking whether it would survive a perfect language and perfect tools. Interfacing with a disorderly real world, identifying every dependency and exception case, and having to be exactly rather than approximately correct are essential. Awkward syntax, tools that fight each other, and a structure you imposed are not.
- Treat the recognisable symptom as a stop signal: doggedly applying a method that is clearly irrelevant is what being overloaded by complexity looks like from the inside. Notice it and step back rather than pushing through.
- Cut accidental complexity where you find it rather than routing around it. Accidental difficulty is the part you control, and it compounds — the system grows until nobody knows what it does, and once nobody can predict the effect of a change in one area on another, progress stops.
- Judge a candidate design by how much of anyone's brain it occupies at one time, and prefer the version that minimises what must be held simultaneously.

## Don't
- Don't force-fit code to a recognised pattern. Shifting code slightly to match a well-known shape can improve understandability; shifting it far to look like a standard pattern adds complexity rather than managing it.
- Don't reach for a pattern because you want to use the pattern. Wanting to try one is not evidence that it is the appropriate design solution here.
- Don't expect the essential difficulty to shrink much. Accidental difficulties were largely addressed decades ago — clumsy syntax by third-generation languages, batch-mode turnaround by time-sharing, tool friction by integrated environments — and progress on what remains is bound to be slower.
- Don't take "no technical cause" at face value on a failed project. Projects fail most often from poor requirements, planning, or management, but when the cause *is* technical it is usually uncontrolled complexity.

## Checklist
- For the thing that is hard right now: would it still be hard with perfect tools and a perfect language?
- Are you applying a method that has stopped being relevant to what you are actually looking at?
- Which part of this complexity did you introduce, and what would removing it cost?
- How much of this design must be held in mind at once to change it safely?

## Notes
The distinction is Brooks's, from *No Silver Bullets*, and it descends from Aristotle: essential properties are the ones a thing must have to be that thing, accidental properties are the ones it merely happens to have. A car needs an engine, wheels, and doors; whether the engine is a V8 or a turbocharged four is accidental. Applied to software, the essential difficulty is working out all the details of a highly intricate, interlocking set of concepts, and it grows as software addresses larger real-world problems, because the interactions among real-world entities grow with them.

The reason this earns a place ahead of any specific design technique is that McConnell makes managing complexity the primary technical imperative — not one goal among several. Dijkstra's framing of why is worth keeping: programming is the only profession where a single mind must span from a bit to hundreds of megabytes, nine orders of magnitude, and no one's skull is big enough to hold a modern program. The conclusion is not to try harder at holding it, but to organise so that you never have to.

Both halves of the imperative matter. Keeping accidental complexity from proliferating is the half you act on directly. Minimising the essential complexity anyone must deal with at one time is the half that every other design heuristic — abstraction, encapsulation, hiding, hierarchy — exists to serve.

---
object_id: PAT_prototype_to_answer_one_specific_design_question
object_type: pattern
name: Prototype the Minimum That Answers One Named Question
library_path:
- software-engineering
- core
- design
stage_binding: 1 skeleton
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- prototyping
- design
- risk_reduction
- experiment
cross_links:
- rel: related_to
  target_object_id: PAT_produce_a_second_design_before_committing
- rel: related_to
  target_object_id: AP_grow_a_system_from_a_running_skeleton
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Prototype the Minimum That Answers One Named Question

## Pattern Rule
**IF** a design decision depends on something you cannot know without trying it
**THEN** write the absolute minimum throwaway code that answers one specifically stated question, and throw it away once answered.
**ELSE** if you cannot state the question specifically enough to know when it is answered, do not start — sharpen the question first.

## Do
- State the question with numbers and conditions in it. "Will this database framework support 1,000 transactions per second under assumptions X, Y and Z?" gives you something to build against; "will this framework work?" gives you no direction and no finish line.
- Approximate the problem space instead of modelling it. You need the number of tables and roughly how many entries they hold — not the real schema. Tables called Table1 and Table2 with columns called Column1 and Column2, populated with junk, will answer a throughput question.
- Decide up front that the code is going away. People who believe the code will end up in production cannot bring themselves to write the minimum, and quietly start implementing the system instead of prototyping it.
- Make disposal structural rather than a matter of willpower. Build the prototype in a different technology from the production code — a Java design explored in Python, an interface mocked in slideware — so it cannot be absorbed.
- When you must use the production technology, mark it so extension takes a conscious act: prefix the class or package names with `prototype`, which at least makes someone think twice before building on it.
- If nothing structural stops the code being absorbed and you cannot trust the culture to throw it away, do not build a prototype at all — build a lean but *complete* end-to-end slice instead, carrying real error handling and structure, and grow it. You lose the freedom to ignore details and you gain code you are not lying about.

## Don't
- Don't let the prototype grow past its question. Every addition past the answer is production code being written under prototype rules — no tests, no error handling, no design.
- Don't prototype to explore in general. This is an instrument for resolving a specific uncertainty, not a way of starting work while undecided.
- Don't keep a prototype because it turned out well. Its value was the answer it produced; the code was never held to a standard that makes it safe to keep.
- Don't run one whose answer you have already settled on. Ask first what you would do if the result came back the other way; if the honest answer is "carry on regardless," the exercise is confirmation rather than an experiment and the time is simply spent.

## Checklist
- Can you write the question down in one sentence, with the threshold that decides it?
- Will you know from the result which way the design decision goes?
- Is anything in the prototype there for reasons other than answering that question?
- What stops this code reaching production — a different technology, a naming convention, or only your intention?

## Notes
This is the tool that makes the wickedness of design tractable at low cost. You cannot fully define a design problem until you have partly solved it, and prototyping is the cheapest available way to partly solve it — provided the exploration is bounded by a question rather than by how interesting the code becomes.

How to judge the outcome follows from what a prototype is for, and it is the opposite of how people usually judge it. A prototype that comes back "no, this framework will not hold the throughput" has succeeded exactly as much as one that comes back "yes" — it resolved the issue, which is the only thing it was built to do. Reading a negative result as a failed prototype is what produces the fourth failure mode, the one that happens before any code exists: an experiment run to confirm a decision already taken. Design is a process of planning small mistakes in order to avoid large ones, and a prototype you are unwilling to be contradicted by has been stripped of the only function it had.

The three failure modes that arise once you are building are worth holding separately because they have different fixes. Undisciplined scope is fixed by the minimum-code rule. A vague question is fixed before any code is written. And treating the output as production code is the one that cannot be fixed by intention alone, which is why the countermeasures are structural — a different technology, or a naming prefix that makes absorption deliberate rather than accidental.

Used with discipline this is the workhorse against design uncertainty. Used without it, prototyping adds uncertainty of its own: half-built code with production ambitions and no production rigour, which is worse than the unresolved question it was meant to settle.

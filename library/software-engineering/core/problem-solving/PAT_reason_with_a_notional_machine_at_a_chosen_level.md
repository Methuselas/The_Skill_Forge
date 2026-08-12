---
object_id: PAT_reason_with_a_notional_machine_at_a_chosen_level
object_type: pattern
name: Pick the Abstraction Level of Your Machine Model and Name What It Hides
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- problem_solving
- notional_machine
- abstraction
- mental_model
cross_links:
- rel: related_to
  target_object_id: PAT_check_whether_a_second_model_composes_or_conflicts
- rel: related_to
  target_object_id: PAT_guard_against_an_outdated_mental_model_under_load
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u06, pp. 102-105
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Pick the Abstraction Level of Your Machine Model and Name What It Hides

## Pattern Rule
**IF** you are reasoning about what the machine does when your code runs
**THEN** decide which level of abstraction the question actually needs, and state which details your model is hiding, so you can tell the difference between a detail safely ignored and a detail that is about to bite.

## Do
- Place your working model on the level it serves: the programming language, the compiler or interpreter, the virtual machine and bytecode, or the operating system. Figure 6.4's examples map cleanly — calculation as substitution sits at the language level, mutually exclusive operations as train switches at the VM level, threads as human collaboration at the OS level.
- Say explicitly what the model omits. "Variables as boxes" operates at the language and compiler/interpreter levels and abstracts away compiled code and the operating system entirely; knowing that is what tells you when to stop trusting it.
- Accept a model that is wrong in the right places. Predicting `(9.0/5.0) * celsius + 32` by substituting `10` for `celsius` and adding brackets for precedence is not how the machine evaluates it — the machine most likely converts to reverse Polish notation and works a stack — but the substitution model answers the question you asked.
- Move down a level when the question is about performance, memory, concurrency, or anything where the hidden mechanism is the subject.

## Don't
- Don't confuse this with a mental model you happen to hold. A notional machine is a consistent and correct abstraction offered as an explanation, whereas your mental model can be wrong or internally inconsistent; the two converge only as you learn the language better.
- Don't reason at the lowest level available on principle. Most of the time you do not care how bits are stored using electricity, and dragging that in is cost without accuracy.
- Don't let a model chosen for one level answer a question that lives at another — that is the specific failure Hermans warns about when she says some ways of thinking about code "might abstract relevant details."

## Checklist
- Which of the four levels does the question I am asking actually live at?
- What is this model hiding, and is any of it load-bearing for the answer I need?
- If my model is wrong about the mechanism, is it wrong in a way that changes the result?

## Notes
A notional machine is an abstract representation of the computer used to reason about what it is doing — the term comes from Ben du Boulay, who coined it while working on Logo in the 1970s and defined it as the idealized model of the computer implied by a language's constructs. His own teaching version was a factory worker with ears for parameters, a mouth for output, and hands to carry out the code.

The distinction Hermans draws between notional machines and mental models is the useful part: a notional machine is an explanation of how a computer works, and once you have internalized it and can use it with ease it becomes your mental model. That makes level selection a skill you can practise rather than a fact about your current understanding.

Figure 6.4 has to be looked at rather than extracted — linearized text collapses the four stacked levels and their paired examples into an unreadable run of labels, and the pairing is the whole content of the figure.

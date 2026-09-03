---
object_id: DRILL_surface_notional_machines_from_code_vocabulary
object_type: drill
name: Surface the Notional Machine Hiding in Your Team's Vocabulary
target_skill: Recognizing which model of the machine a piece of everyday programming language commits you to
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- notional_machine
- mental_model
- vocabulary
- problem_solving
cross_links:
- rel: supports
  target_object_id: PAT_reason_with_a_notional_machine_at_a_chosen_level
- rel: supports
  target_object_id: PAT_check_whether_a_second_model_composes_or_conflicts
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Surface the Notional Machine Hiding in Your Team's Vocabulary

## Practice Task
Collect the metaphorical verbs and nouns your team uses about code, and for each one name the model of the machine it implies and the false inference it licenses.

## Target Skill
Recognizing which model of the machine a piece of everyday programming language commits you to.

## Setup
A recent design discussion, code review thread, or your own codebase's documentation and identifier names. A two-column list.

## Instructions
1. Collect ten phrases from real discussion that describe code in physical or agentive terms, quoting each as it was actually written rather than recalling it. The chapter's own examples are the calibration set: a variable "holds" a value, a file is "open" or "closed," a pointer "points" to something, a function "returns" a value, and a function is "called."
2. For each phrase, write in the second column the model it implies. "Holds" implies a container with an interior. "Open" and "closed" imply a physical state of the file, where the technical meaning is only that you are permitted to read it or forbidden to. Mark any model you had never made explicit before writing it here, or state that none was new.
3. Mark which of your phrases have hardened past metaphor into the language or tooling itself — pointers exist as a language construct, and IDEs will show you where a function is "called" — and for one of them, say what the construct still hides.
4. For each implied model, write one thing that would be true if the metaphor were literal and is not true of the code. A container can hold several items; a variable cannot.
5. Find a pair of phrases implying models that cannot both be true at once, decide which one your team actually reasons with, and give the reason. If no such pair exists in your ten, say which single model all ten share.
6. Repeat on a piece of documentation written for newcomers, where the metaphors are usually denser and less examined.

## Success Check
- Ten phrases are quoted as they were actually written in real discussion or real artifacts, rather than recalled or invented. A list assembled from memory returns the metaphors already noticed, and the entries worth having are the ones that read as literal description.
- Every phrase carries both the model it implies and one concrete prediction that model would make which the code does not honour. A model named without its wrong prediction has restated the metaphor in longer words.
- At least one phrase is marked as carrying a model not previously made explicit, or the run states that none was — which is itself a claim about how examined the team's vocabulary already is, and has to be made rather than left as a blank.
- A phrase that has hardened into a language construct or a tool is named together with what the construct still hides. Naming the construct is the easy half, and stopping there reports that the metaphor won rather than what it cost.
- A pair of phrases implying incompatible models is identified and one is chosen as the team's working model, with the reason. Reporting that no such pair exists requires naming the single model all ten share, so the absence is a finding rather than an omission.

## Common Failures
- Collecting jargon rather than metaphor. "Idempotent" is vocabulary; "the queue drains" is a notional machine.
- Stopping at "it's just a figure of speech." The chapter's point is that these figures of speech shape reasoning and have already shaped the languages themselves.
- Listing only phrases you disapprove of. The useful entries are usually the ones so natural that they read as literal description.

## Notes
This is Hermans's exercise 6.5 — list examples of language used about programming that indicate a notional machine and lead to a certain mental model — expanded into a repeatable pass over real team artifacts rather than a one-time recall task.

The reason the drill has teeth is the observation it sits on: notional machines that are commonly used to explain how things work "find their way into the language we use to talk about code, and even into programming languages themselves." That makes the vocabulary a readable record of which models a team has committed to, including the ones nobody chose deliberately. Running it on newcomer documentation is the highest-yield variant in practice, because that is where metaphors are introduced and where their false inferences get installed.

---
object_id: PAT_prepare_for_interruption_before_it_arrives
object_type: pattern
name: Externalize Enough State That an Interruption Cannot Cost You the Context
library_path:
- software-engineering
- core
- working-practice
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- working_practice
- interruptions
- note_taking
- prospective_memory
cross_links:
- rel: related_to
  target_object_id: PAT_support_the_memory_system_the_activity_taxes
- rel: related_to
  target_object_id: PAT_comment_why_not_what
- rel: related_to
  target_object_id: PAT_interrupt_at_task_boundaries
- rel: related_to
  target_object_id: AP_refactor_working_code_safely
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Externalize Enough State That an Interruption Cannot Cost You the Context

## Pattern Rule
**IF** you are working on something you will not finish before you are interrupted
**THEN** write the recoverable parts of your context down as you go, because the expensive part of an interruption is rebuilding the mental model, not the interruption itself.

## Do
- **Dump the mental model into a comment** when you can hold the interruption off for a moment — a Slack message or a colleague at your desk usually can wait, a ringing phone cannot. Even a rough dump beats reconstruction.
- **Support prospective memory**, the memory for things you intend to do later. To-do comments in the code you are working on are the common form; sticky notes and emails to yourself work but sit outside the codebase, which is their weakness.
- **Consider a deliberate roadblock.** Parnin observed programmers inserting random characters to force a compile error, ensuring the code could not be left in a half-finished state unnoticed.
- **Label subgoals before you start.** Write the steps of a larger task as comments first — parse the text, receive the parse tree, filter it, flatten it back — then fill them in. There is always a plan to fall back on, and Margulieux's study found that when subgoals are provided, programmers use them to organise the solution mentally.
- Expect a warm-up. Nakagawa found load varies widely within a task and peaks in the middle, which suggests a warm-up and cool-down around the hardest work — so an interruption does not cost you a moment, it costs you the climb back.

## Don't
- Don't rely on to-do comments alone. As most programmers have experienced, they linger unresolved; a GitHub search returned 136 million code results containing the word.
- Don't trust yourself to resume quickly. Programmers interrupted mid-edit resumed in under a minute only 10% of the time, and it takes roughly a quarter of an hour to start editing again.
- Don't leave recovery to a source diff. Participants used it as a last resort and found it cumbersome to locate the actual differences.
- Don't treat interruptions as an occasional nuisance to be endured. They take 15 to 20 minutes each and consume around 20% of a developer's time, and the average programmer gets just one uninterrupted two-hour session in a day.

## Checklist
- If I were pulled away right now, what would I have to reconstruct rather than read?
- Are my next steps written somewhere the code will show me, rather than only in my head?
- Have I recorded *why* I chose this direction, not just what I was doing?

## Notes
Figure 11.2 gives the three techniques as three answers to "Can I ask you something?" — let me store my mental model, sure I have prospective memory support, sure I labelled my subgoals. That ordering is also a fallback ladder: the first buys the most and costs a moment you may not have, the third costs nothing at the time because it was done before you started.

Subgoal labelling is the one with uses beyond interruption. The labels survive as documentation, and they support delegation — a senior programmer can design the subgoals and others implement parts of the solution. It is presented here as an interruption technique but it is not only that.

Hermans defends comments here against the self-documenting-code position, and the argument is specific rather than general: code seldom explains the programmer's thought process, so it does not represent the author's mental model. Why an approach was chosen, what the goals were, and which alternatives were rejected are not expressible as code, and when they are unwritten they can at best be rediscovered. She quotes Ousterhout — the idea behind comments is to capture information that was in the designer's mind but could not be represented in the code — and Brooks, that comments matter most in comprehension because they are always present, unlike documents you must find.

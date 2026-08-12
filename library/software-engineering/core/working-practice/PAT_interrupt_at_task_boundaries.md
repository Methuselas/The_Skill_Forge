---
object_id: PAT_interrupt_at_task_boundaries
object_type: pattern
name: Interrupt People Between Tasks, Not Inside Them
library_path:
- software-engineering
- core
- working-practice
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- working_practice
- interruptions
- collaboration
- cognitive_load
cross_links:
- rel: related_to
  target_object_id: PAT_prepare_for_interruption_before_it_arrives
- rel: related_to
  target_object_id: PAT_dont_multitask_what_you_have_not_automatized
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u11, pp. 187-189
  evidence_type: text
confidence: high
references: []
variants: []
---

# Interrupt People Between Tasks, Not Inside Them

## Pattern Rule
**IF** you need something from a colleague who is working
**THEN** wait for a task boundary rather than interrupting mid-task, because the timing changes the cost — the same interruption delivered during a task produces more errors, more annoyance and more anxiety than one delivered after it.

## Do
- Treat the boundary as the variable you control. Bailey's controlled experiment gave one group interruptions during the primary task and the other the same interruptions afterwards; the during-task group was measurably worse off on every dimension measured.
- Take the error result seriously. A 2006 follow-up with a similar setup found interrupted people made **twice as many mistakes** — a cost paid by the work, not just by the person's mood.
- Make your own state legible so others can find the boundary. The FlowLight infers engagement from typing speed and mouse activity and shows red when the developer is deep in a task and green when they are available; in a field study of over 400 participants across 12 countries it reduced interruptions by 46%, and enough people kept using it afterwards that it became a product.
- Use the manual equivalent where no instrument exists — a Slack status, a headphones convention, a visible marker on the desk. The mechanism is signalling the boundary, not the hardware.

## Don't
- Don't assume a short interruption is a small one. Bailey found interrupted tasks take longer to complete than uninterrupted ones *even after excluding the time spent on the interruption itself*.
- Don't discount the subjective cost as merely subjective. People perceive interrupted tasks as harder, and report more annoyance and anxiety — and the same participants also performed worse, so the feeling tracks something real.
- Don't rely on the interrupted person to protect themselves. Recovery is expensive enough that 62% of developers in a Microsoft study regard it as a serious problem, which is not a thing they can solve on their own.

## Checklist
- Is the person I want to interrupt visibly mid-task, and can this wait for a boundary?
- Have I made my own working state visible so others do not have to guess?
- Am I about to send something that could be asynchronous instead?

## Notes
The measurement behind this is the dual-task method, which is worth knowing because it bounds the claim. A participant performs a second task — clicking a letter A whenever it appears — while working on the primary one, and how fast and accurately they handle the second task estimates the load imposed by the first. Its known weakness is that the second task adds load of its own and so interferes with what it measures.

This pattern is the counterpart to preparing for interruption, and the pair is deliberate. One is what you do as the person who will be interrupted; this one is what you do as the person doing the interrupting. Most teams have policies about the first and none about the second, which is backwards given that the timing decision belongs entirely to the interrupter.

---
object_id: PAT_support_the_memory_system_the_activity_taxes
object_type: pattern
name: Name the Activity You Are In, Then Support the Memory It Taxes
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- working_practice
- cognitive_load
- code_comprehension
- note_taking
cross_links:
- rel: related_to
  target_object_id: PAT_externalize_intermediate_state_when_tracing
- rel: related_to
  target_object_id: PAT_separate_intrinsic_from_extraneous_load
- rel: supports
  target_object_id: PAT_prepare_for_interruption_before_it_arrives
- rel: related_to
  target_object_id: AP_prepare_an_onboarding_for_all_three_memory_systems
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Name the Activity You Are In, Then Support the Memory It Taxes

## Pattern Rule
**IF** you are about to spend a stretch of time in a codebase
**THEN** name which of the five activities you are doing — searching, comprehension, transcription, incrementation, exploration — because each taxes a different memory system and the support that helps one does little for another.

## Do
- **Searching** loads short-term memory, so offload it. Write down what you are looking for, where you will look next, and what you have already ruled out. Leave breadcrumb comments recording *why* you visited a place — "I read this method because I thought it might be involved in initialising the page class" — which pays off doubly when the search will not finish in one sitting.
- **Comprehension** loads working memory, so externalise the model. Draw the code and update the drawing as you learn; retrieving from paper is cheaper than retrieving from your head, and a written model also exposes misconceptions you are holding.
- **Transcription** loads long-term memory, since what you need is recall of syntax. This is the activity the flashcard and automatization work targets.
- **Incrementation and exploration** load all three, so split them. Say out loud that you will search first, then comprehend, then transcribe — being deliberate about which subactivity you are in is what lets you apply the right support.
- Adjust for what you already know. If the language is familiar your LTM is barely working; if the codebase is familiar your STM and working memory are barely working. The same task lands differently depending on which of the two is unfamiliar.

## Don't
- Don't treat all programming time as one undifferentiated activity. Incrementation is the most common activity in professional work and it is also the one most in need of explicit support, precisely because it is a mixture.
- Don't skip notes during exploration because they break flow. Hermans acknowledges the feeling directly and argues the rough note about a design direction buys back more mental space than it costs.
- Don't look for debugging in the list. It is not a sixth activity — it is usually a sequence of exploration, searching and comprehension followed by writing code, which is why it feels harder than any single activity.

## Checklist
- Which of the five am I actually doing right now?
- Which memory system does that tax, and what am I doing to offload it?
- If this is incrementation or exploration, have I split it into named subactivities?

## Notes
The five activities come from the cognitive dimensions of notation framework of Green, Blackwell and Petre. They lay out as a grid of activity against task — executing, coding, testing, reading, refactoring — with a final column naming the memory system each activity is hard on.

The figure carries one distinction the prose never states. Its ticks come in two weights: solid for the tasks central to an activity and dashed for those that are optional. Testing and refactoring are dashed under comprehension, and refactoring is dashed under incrementation and exploration. So refactoring is available to comprehension as a tool rather than being part of it, which matches the surrounding argument that you may refactor code *in order to* understand it. Reading the grid as uniform ticks loses that.

The observation that developers spend around 58% of their time comprehending existing code is what makes the second bullet the highest-value one on the list.

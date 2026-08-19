---
object_id: AP_prepare_an_onboarding_for_all_three_memory_systems
object_type: ap
name: Prepare an Onboarding That Supports All Three Memory Systems
library_path:
- software-engineering
- core
- working-practice
stage_binding: 0 design
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
- onboarding
- teaching
- documentation
- cognitive_load
cross_links:
- rel: related_to
  target_object_id: PAT_give_a_newcomer_one_activity_at_a_time
- rel: related_to
  target_object_id: PAT_account_for_the_curse_of_expertise_when_onboarding
- rel: related_to
  target_object_id: PAT_locate_a_learner_on_the_neo_piagetian_stages
- rel: related_to
  target_object_id: PAT_support_the_memory_system_the_activity_taxes
- rel: related_to
  target_object_id: PAT_teach_along_a_semantic_wave
- rel: related_to
  target_object_id: PAT_calibrate_code_reading_scope_to_reader_knowledge
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Prepare an Onboarding That Supports All Three Memory Systems

## Objective
Do the preparation for a newcomer before they arrive, so that each of their three memory systems has support in place and none of the first weeks is spent on load you could have removed.

## Steps / Flow
1. **Build the long-term memory support with the existing team, in advance.** Write down every domain concept someone will meet in the code, with a definition. Write a second list of every library, framework, database and external tool the codebase uses, with what each one is for. A sentence like "we use Laravel for this web app, deployed on Heroku with Jenkins" costs an existing developer nothing and carries no meaning at all to someone who does not know one of those names — knowing what a web framework is in the abstract does not help when the specific names are opaque.
2. **Teach the domain separately from the code.** Going over the concepts on their own, before introducing the codebase, is a small change with a large effect, because it stops domain learning and code comprehension competing for the same capacity. A flashcard deck of domain and programming concepts is a reasonable form for this.
3. **Keep those lists afterwards.** An up-to-date list of the domain and programming concepts a project uses helps the existing developers too, which is what makes this preparation worth maintaining rather than doing once per hire.
4. **Prepare small, focused tasks for the short-term memory.** One activity each, per the single-activity pattern. Where a task must involve implementation, prepare the code beforehand so the newcomer is not also searching.
5. **Prepare working-memory support, and hold it loosely.** Diagrams and tables help, and creating them is hard for someone who does not know the codebase — so the onboarder makes them rather than asking for them. But diagrams do not help absolute beginners, who are reluctant to step away from the code, so monitor whether they are landing and drop them when they are not.
6. **Give both sides the vocabulary.** Teach the newcomer the cognitive concepts — long-term, short-term and working memory, cognitive load, chunks — so that they can report "too much load reading this" or "I lack chunks for Python" instead of "I am confused." A newcomer who can manage their own load is the goal, not just an onboarder who manages it for them.
7. **Monitor understanding continuously rather than at checkpoints.** Regularly ask for a quick recap of what was read, a definition of a domain concept, or recall of a programming concept used in the code. Guessing and conclusions that do not follow are the signal that load has been exceeded.

## Notes
The three-way split maps onto the three forms of confusion from chapter 1: lack of knowledge is a long-term memory problem, lack of information is a short-term memory problem, and lack of processing power is a working-memory problem. Preparing for each separately is what turns "be patient with newcomers" into a set of things you can actually do before they arrive.

Step 5 carries a real tension with step 4 and is deliberately conditional. Diagrams are the standard working-memory support and are counterproductive below the concrete operational stage — which means the same artefact helps or hurts depending on where the newcomer is, and the only way to know is to watch. That is why the step says monitor and abandon rather than provide.

Most of this is preparation done by the team before anyone is hired, which is the quiet claim of the whole chapter. The failure mode it replaces — introduce the people, the domain, the workflow and the codebase at once, then hand over a small task — costs nothing to set up and reliably produces a newcomer who cannot retain what they were told and a team that misreads why.

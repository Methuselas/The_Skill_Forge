---
object_id: PAT_study_worked_examples_rather_than_only_solving
object_type: pattern
name: Study Solved Problems, Don't Only Solve New Ones
library_path:
- software-engineering
- core
- deliberate-practice
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- deliberate_practice
- worked_examples
- cognitive_load
- code_reading
cross_links:
- rel: related_to
  target_object_id: PAT_match_practice_method_to_the_memory_type
- rel: related_to
  target_object_id: DRILL_read_code_with_text_comprehension_strategies
- rel: related_to
  target_object_id: PAT_use_domain_specific_cues_not_generic_problem_frames
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Study Solved Problems, Don't Only Solve New Ones

## Pattern Rule
**IF** you are trying to get better at solving programming problems
**THEN** spend a real share of the time studying other people's solutions together with an explanation of how they were reached, because solving alone leaves no capacity to store what solving taught you.

## Do
- Pair the code with its explanation. The effect comes from the worked example — a recipe describing the steps — not from the solution alone, and studies in programming specifically found more learning from reading programs plus an accompanying explanation than from programming.
- Read code in a domain you already know somewhat. Unfamiliar domain vocabulary adds extraneous load and pushes out the capacity you need for the programming itself; a library you actually use is a better target than an impressive unfamiliar codebase.
- Do it with someone. A code reading club sustains the habit better than solitary intent, and the two-step version is stronger still — write a summary of code you wrote, then swap code and summaries with a colleague so each of you studies the other's.
- Use the written sources that exist for this: blog posts explaining how a problem was solved, and the small number of books built around code and its explanation, such as *The Architecture of Open Source Applications* and *500 Lines or Less*.

## Don't
- Don't assume solving more problems is the efficient path. Sweller's ninth-graders who received worked examples solved the equations five times faster than those who did not — and the transfer result is the one that matters, since they also did better on *different* problems requiring the same underlying rules.
- Don't fear that studying recipes produces mechanical imitation. That worry is the standard objection and the evidence runs the other way; the recipe group learned the general moves, while the group deep in the problem stayed focused on that problem rather than on the rules.
- Don't take "just build side projects and you'll learn" as established. Hermans names this as the programming version of the same fallacy, and quotes Kirschner's summary — you don't become an expert by doing expert things.

## Checklist
- When did I last read someone else's solution alongside an account of why it is that way?
- Is the code I am studying in a domain familiar enough that I am learning programming rather than vocabulary?
- Am I ending sessions unable to recall what I did, and treating that as normal?

## Notes
Sweller's 1980s experiments divided 20 Australian ninth-graders into two groups solving the same algebra equations, with one group also receiving worked examples. The speed result is unsurprising; the transfer result is the finding, because it removes the usual objection that recipes only teach recipe-following. The effect has since been replicated across age groups and subjects including mathematics, music, chess, sports and programming.

The mechanism is germane load, the third type beside the two introduced earlier. Germane load is the effort of writing information back into long-term memory. When intrinsic and extraneous load fill the available capacity there is nothing left for it, and the solving simply does not get stored — which is why a heavy coding session can end with no memory of what you did. It is best pictured as an arrow from working memory into the LTM that only functions when there is capacity to spare. The worked-example group stayed under that ceiling, so they could reflect on and retain the rules; the solving group did not.

That also connects this pattern to the automatization one. Both are about freeing capacity — automatization lowers what routine work costs, worked examples exploit the headroom to actually store what you learn.

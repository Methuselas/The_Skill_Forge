---
object_id: DRILL_read_code_with_text_comprehension_strategies
object_type: drill
name: Read Unfamiliar Code With Text-Comprehension Strategies
target_skill: Deliberately applying reading strategies to code instead of stepping through it line by line
library_path:
- software-engineering
- core
- code-comprehension
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_comprehension
- reading_strategies
- onboarding
cross_links:
- rel: supports
  target_object_id: PAT_separate_text_knowledge_from_plan_knowledge
- rel: related_to
  target_object_id: DRILL_annotate_a_dependency_graph_over_code
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants:
- variant_id: VAR_hermans_run_the_seven_strategies_as_a_team_for_onboarding
  variant_name: Run the Seven Strategies Collaboratively to Onboard Someone
  variant_basis: context
  difference_from_foundation: The foundation runs the seven strategies as an individual reader, where each pass is work you do for yourself. This variant runs the same seven as a group with a newcomer present, and the team absorbs the expensive passes on their behalf — the point is to lower the newcomer's load so their working memory can go to the code rather than to orientation. Several strategies change hands entirely. Activating happens before the session, with the team reminding the newcomer of relevant concepts rather than the newcomer recalling them. Determining importance is done by team members naming what they think the key lines are, since someone with low knowledge of a system cannot separate core from peripheral. Inferring surfaces the undocumented domain rules the team holds tacitly, such as a shipment always containing at least one order.
  when_to_use: Use when bringing someone into an unfamiliar codebase, and note that the session is a comprehension activity — so the other four programming activities should be kept out of it. Pitch visualizing and questioning to the newcomer's stage, either supplying a diagram or asking them to draw one, and either asking questions they answer or inviting questions you answer.
  when_not_to_use: Do not run it with an absolute beginner who cannot yet trace code, since the strategies assume a working execution model. Also stop treating it as onboarding once the newcomer can lead the passes themselves — at that point the foundation's individual form is the cheaper tool.
  absorbed_from_object_id: none
---

# Read Unfamiliar Code With Text-Comprehension Strategies

## Practice Task
Take a piece of unfamiliar code and read it using the seven strategies people are taught for reading prose, one pass at a time, instead of stepping through it.

## Target Skill
Deliberately applying reading strategies to code instead of stepping through it line by line.

## Setup
The code printed or open as an annotatable PDF, and a timer. An IDE works if you record the annotations as comments instead.

## Instructions
1. **Activate.** Give yourself a fixed budget — five or ten minutes — to study the code before trying to understand it. Then answer: what caught your eye first, and why? What second? Are they related? Which programming, syntactic, and domain concepts appear, and do you know all of them? Look up any you do not *before* reading further.
2. **Monitor.** Read through marking each line with a tick where you understand it and a question mark where you do not. Then turn each question mark into a question naming what specifically is unknown — which value, which caller, which condition — or carry it forward as still unresolved.
3. **Determine importance.** Pick the lines with the most influence on execution — ten in a snippet, twenty-five in a program — and mark them. For each, say why you chose it in terms of what it does to execution, and how it connects to the program's goal.
4. **Infer.** List every identifier: variables, classes, methods, functions. Sort them into domain names, programming-concept names, both, and those that mean nothing without context. The last group is where to spend effort. Mark any name that turned out to mean something different from your first assumption, or state that none did.
5. **Visualize.** For anything still opaque, build an operation table: each identifier against the operations it takes part in. If `f` is applied to `as[i]` and `bs[i]` then `f` is a function and `as` and `bs` are indexable — types and roles fall out of usage.
6. **Question.** Ask what the five most central concepts are and how you identified them; what the creator decided; what those decisions assume; what they buy; what they cost; and what alternatives existed.
7. **Summarize.** Close the code and write down the program's goal from memory. Then write the summary in prose, with its most important lines, its domain concepts, its constructs, and the decisions behind it. Keep it — this is often the documentation the code was missing.
8. Check the summary against something outside your own reading — a test, a caller, the author, documentation — and record what that check changed, including when it changed nothing.

## Success Check
- The program's goal is written down with the code closed, before the summary is composed. A goal written with the file open describes what was just read, and the claim under test is that the seven passes left something behind.
- Every question mark from the monitoring pass becomes a question naming what specifically is unknown, or is carried forward as unresolved. "I don't understand this part" is the state the pass exists to convert, not an outcome it may report.
- The lines chosen in the importance pass are justified by what they do to execution rather than by their prominence on the page. The longest line, the one carrying a comment, and the import block are what a prominence-based choice returns, and it fills the quota while selecting for nothing.
- The identifier sort names at least one name that meant something different from the first assumption, or states that none did and shows the sorted list establishing it. A run reporting only the names it classified correctly has kept its hits and discarded the finding.
- The summary is checked against something outside the reading — a test, a caller, the author, documentation — and what that check changed is recorded, including when it changed nothing.

## Common Failures
- Running all seven at once. Each is a separate pass; combined they become ordinary reading with extra steps.
- Skipping activation because it feels like stalling. Reading code while simultaneously learning a concept it uses overloads you and teaches neither.
- Marking only the lines you understand, which produces a map of your confidence rather than of the code.
- Treating disagreement about important lines as error. Run step 3 with a team and people will choose differently — the heavy computation, an import, a comment — and the disagreement is the useful part.

## Notes
The seven strategies — activating, monitoring, determining importance, inferring, visualizing, questioning, summarizing — come from reading-comprehension research, not from software engineering. Applying them to code is justified by the finding that the two activities share machinery: Siegmund's fMRI work found program comprehension activating five Brodmann areas in the left hemisphere, several of them language-processing regions, and this held even though variable names in the study were deliberately obfuscated.

Prat's study points the same way from a different direction: across 36 learners, numeracy explained about 2% of the variance in programming ability and language aptitude about 17%, with working memory and reasoning the strongest predictor at roughly 34%. Programmers already do a piece of this without being taught — eye-tracking shows them viewing over 70% of the lines in the first 30% of their review time, which is the scanning behaviour readers use on prose.

`VAR_hermans_run_the_seven_strategies_as_a_team_for_onboarding` retains **Run the Seven Strategies Collaboratively to Onboard Someone**, which is the same seven passes performed by a group around a newcomer rather than by a reader alone. The purpose changes from deepening your own reading to lowering someone else's load, and several passes change hands as a result: the team activates relevant concepts *before* the session rather than the newcomer recalling them, team members name what they consider the important lines because someone new cannot yet separate core from peripheral, and inferring is where the team's undocumented domain rules get said out loud. Monitoring becomes the onboarder's main instrument — ask for a recap, a domain definition, a concept recalled — and guessing is the signal that load has been exceeded. Visualizing and questioning are pitched to the newcomer's stage in both directions. A natural closing move is committing the session's summary to the codebase as documentation, which also walks the newcomer through the project's review workflow at low cost. Keep the session to comprehension only, and stop treating it as onboarding once the newcomer can lead the passes themselves.

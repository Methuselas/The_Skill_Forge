---
object_id: PAT_match_practice_method_to_the_memory_type
object_type: pattern
name: Pick the Practice Method That Fits the Kind of Memory You Need
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
- memory
- automatization
- problem_solving
cross_links:
- rel: related_to
  target_object_id: DRILL_practice_syntax_with_flashcards
- rel: related_to
  target_object_id: PAT_study_worked_examples_rather_than_only_solving
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Pick the Practice Method That Fits the Kind of Memory You Need

## Pattern Rule
**IF** you are choosing how to practise a programming skill
**THEN** first decide which kind of memory the skill lives in, because explicit and implicit memories are laid down by different mechanisms and the wrong method will not move the one you need.

## Do
- Use flashcards and other attention-based methods for **semantic** memory — facts you know you know, such as how a Java for-loop is written. Explicit memories require your explicit attention to be stored, which is exactly what a card demands.
- Use **repetition** for implicit or procedural memory, because those are laid down by doing rather than by attending. You learned to eat with a spoon by trying repeatedly, not by studying it, and touch typing and keyboard shortcuts are the same category.
- Recognise **episodic** memory as the expert's main instrument. Research shows experts rely heavily on it when solving problems — in a real sense they recreate familiar problems rather than solve them, applying a solution that worked before rather than deriving a new one. That memory forms without deliberate effort, but its retrieval strength rises with how often you have revisited it.
- Notice when a skill has drifted out of the category you are treating it as. If you can state the rule perfectly and still do the wrong thing under your fingers, the failure is implicit and no amount of card practice will fix it.

## Don't
- Don't practise an implicit skill with a declarative method. Hermans's own case is exact: she knew Python's `for` syntax, had drilled it with flashcards, and still produced `foreach` from C# muscle memory for years.
- Don't assume more programming builds all three. Repetition of whole tasks builds implicit skill at whatever you happen to repeat, and leaves semantic gaps untouched.
- Don't treat automatization as optional polish. Every skill still costing conscious attention is consuming capacity that the larger problem needs.

## Checklist
- Is what I am practising a fact I must recall, a motion I must not have to think about, or a solution I want to be reminded of later?
- Does my chosen method match that category?
- Where the rule is known and the behaviour is wrong, am I still treating it as a knowledge problem?

## Notes
The taxonomy runs: memories divide into procedural (implicit) and declarative (explicit), and declarative divides again into episodic — things you experienced, like the three hours chasing a bug that turned out to be an error in a unit test — and semantic, meanings and facts, like a class in Java combining data and functionality. The same tree maps onto programming, with `ctrl-c`/`ctrl-v` under procedural and for-loop syntax under semantic.

The payoff for practice is the reason the taxonomy is worth carrying: the three categories are *created* differently, so the method has to match. This is also the mechanism behind automatization. Once a skill reaches the autonomous phase it adds nothing to cognitive load, which is what frees capacity for larger problems — Hermans's image is unlocking a move in a game, where learning to double-jump opens parts of a level that were unreachable before.

Logan's instance theory explains why automatized performance is fast. Each execution of a task lays down another instance memory, and automatization is complete when you are retrieving instances rather than reasoning at all. Retrieval is faster than reasoning and needs little conscious attention, and there is a diagnostic in it — a fully automatized task carries no urge to go back and check your work, which reasoning through a task does.

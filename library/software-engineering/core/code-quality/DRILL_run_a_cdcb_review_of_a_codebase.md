---
object_id: DRILL_run_a_cdcb_review_of_a_codebase
object_type: drill
name: Review a Codebase Against the Cognitive Dimensions
target_skill: Judging a codebase by what it does to the people who use it, rather than by its technical properties
library_path:
- software-engineering
- core
- code-quality
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- code_quality
- api_design
- cognitive_load
- review
cross_links:
- rel: supports
  target_object_id: PAT_evaluate_code_against_quality_goals
- rel: supports
  target_object_id: PAT_expect_a_design_maneuver_to_cost_another_dimension
- rel: supports
  target_object_id: PAT_optimize_a_codebase_for_its_likely_activities
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Review a Codebase Against the Cognitive Dimensions

## Practice Task
Walk a codebase you own through the thirteen cognitive dimensions, mark which ones matter for it, and name the ones worth improving.

## Target Skill
Judging a codebase by what it does to the people who use it, rather than by its technical properties.

## Setup
A codebase you maintain, ideally a library, framework or module that others call rather than change — that is where this pays most. A three-column table: dimension, relevant, could be improved.

## Instructions
1. Go through the dimensions one at a time and write a sentence on each for this codebase.
   - **Error proneness** — how easy is it to make a mistake here? Inconsistent conventions, missing documentation and vague names all raise it, and a codebase can inherit it from its language.
   - **Consistency** — how similar are similar things? Same name molds, same file layout across classes.
   - **Diffuseness** — how much room does a construct take? Count chunks, not only lines.
   - **Hidden dependencies** — what depends on what, invisibly? Callers of a function are harder to see than callees; config and requirements files separate from code are the classic case.
   - **Provisionality** — how easy is it to think in this system, to write something vague or incomplete?
   - **Viscosity** — how hard is it to change? Slow compiles and slow test runs add to this from outside the code.
   - **Progressive evaluation** — can a user run partial or imperfect work? Optional parameters let someone run with defaults and then vary one at a time.
   - **Role expressiveness** — can a reader see what each part is for? Brackets marking a call, syntax highlighting, `is_set` rather than `set`.
   - **Closeness of mapping** — does the code speak the problem domain? `findCustomers()` maps more closely than `executeQuery()`.
   - **Hard mental operations** — what does this force users to hold or work out? Long ordered parameter lists tax short-term memory; uninformative names like `execute()` have to be memorised.
   - **Secondary notation** — can users add meaning outside the formal language? Comments, and named arguments at a call site.
   - **Abstraction** — can users build abstractions as powerful as the built-in ones? A library allowing subclassing offers more than one allowing only API calls.
   - **Visibility** — how easy is it to see the parts? An API returning an object exposes more shape than one returning a string.
2. Mark each dimension relevant or not, writing the argument for the ones you rule irrelevant. Not all matter for every codebase, and saying why is part of the result.
3. For the relevant ones, note whether the codebase is doing well or badly, citing something in the codebase for each judgement.
4. Name any dimension that mattered here which you had not considered before, or state plainly that none did.
5. For each dimension worth improving, name the design maneuver that would improve it — adding types improves error proneness, renaming toward the domain improves closeness of mapping.
6. For each maneuver, write down which other dimensions it would help and which it would hurt, before deciding to do it. Reject at least one maneuver on that basis, and name one pair of dimensions where improving one degrades the other in this codebase specifically.
7. Re-run the review periodically. The recommendation is roughly annual; the dimensions that matter shift as a codebase ages.

## Success Check
- Every dimension has a sentence, the irrelevant ones included, and irrelevance is argued rather than assumed. A dimension skipped in silence is indistinguishable from one never considered.
- At least one dimension not previously considered turns out to matter, or the run states plainly that none did — which is itself a finding about the reviewer's habitual coverage.
- Each judgement cites something in the codebase, so a later reader can disagree with the evidence rather than only with the verdict.
- Every maneuver has its negative side effect written beside it, and at least one maneuver is rejected on that basis. A list of improvements with no rejections has not used the trade-off structure this framework exists for.
- At least one pair of dimensions is named where improving one degrades the other in this codebase specifically, rather than in general.

## Common Failures
- Reviewing the technical properties instead. Language, paradigm and runtime are not what this measures; the question is what the codebase does to a reader's brain.
- Treating every dimension as a target. Several will be irrelevant, and marking them so is a result rather than a gap.
- Proposing maneuvers without their costs, which is how a codebase acquires a type system and a viscosity problem at the same time.
- Running it once. The value is in the trend and in catching drift as the codebase's likely activities change.

## Notes
The framework is the cognitive dimensions of notation of Green, Blackwell and Petre, originally built for visualisations such as flowcharts and later applied to programming languages — notations being ways to express thoughts. Hermans generalises it from notations to codebases and calls that CDCB, which is what this drill uses. It is aimed particularly at libraries and frameworks, code that others call rather than adapt.

Two dimensions have supporting evidence worth knowing. Hanenberg's Java-versus-Groovy experiments found static type systems let programmers locate and fix errors faster, and that the advantage survived attempts to compensate on the dynamic side with better IDE support and documentation — so the error-proneness dimension is not merely intuition. And the domain-driven design movement, which asks that structure and identifiers match the business domain, is the industry's name for improving closeness of mapping.

This drill combines exercises 12.3, 12.4 and 12.5. The book presents them as three tables; they are one review, because a dimension list without maneuvers produces no change and maneuvers without their trade-offs produce regressions.

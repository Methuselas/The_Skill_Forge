---
object_id: PAT_give_knowledge_one_authoritative_home
object_type: pattern
name: Give Every Piece of Knowledge One Authoritative Home
library_path:
- software-engineering
- core
- abstraction
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- duplication
- maintenance
- knowledge
- normalization
cross_links:
- rel: related_to
  target_object_id: PAT_extract_a_routine_even_when_it_seems_too_small
- rel: related_to
  target_object_id: PAT_reuse_before_reinventing
- rel: related_to
  target_object_id: PAT_comment_why_not_what
- rel: related_to
  target_object_id: DRILL_remove_redundant_derived_data
reference:
  source_title: 'The Pragmatic Programmer: From Journeyman to Master'
  author: Andrew Hunt and David Thomas
confidence: high
references: []
variants: []
---

# Give Every Piece of Knowledge One Authoritative Home

## Pattern Rule
**IF** a fact about the system — a rule, a format, a limit, a relationship — is about to exist in a second place
**THEN** find the one place it genuinely belongs and derive or generate every other appearance from there
**ELSE** where a language or platform forces the repetition on you, generate the copies from a single source as part of the build rather than maintaining them by hand.

## Do
- Read the rule as being about *knowledge*, not about text. Two identical-looking lines that encode two independent decisions are not duplication and should not be merged; two very different-looking pieces of code that both encode the same business rule are duplication and will diverge.
- Diagnose which of four kinds you are looking at, because the repair differs. **Imposed** — the environment demands it. **Inadvertent** — the design put it there and nobody noticed. **Impatient** — copying was quicker. **Interdeveloper** — two people built the same thing without knowing.
- Against imposed duplication, generate rather than transcribe, and keep the generation *active*. A one-time conversion just relocates the problem: the copies must be regenerated every build, or they are back to being maintained by hand.
- Against inadvertent duplication, normalize the model. A value that can be derived from other values is not a field — a line holding a start point, an end point, *and* a length has three facts where two would do, and the third goes stale the moment either endpoint moves. Compute it instead.
- When performance genuinely forces you to cache a derived value, contain the violation. Keep the cached field private and reach everything through accessors, so only the methods inside the class need to keep it honest and nothing outside can observe the inconsistency.
- Against interdeveloper duplication, lower the cost of finding what exists. If reuse is harder than rewriting, people will rewrite — so a known place for shared utilities and a habit of reading each other's code do more than exhortation does.

## Don't
- Don't leave knowledge in a comment that belongs in the code. A comment restating what the code says is the same fact in two places, and it is the copy nobody updates — which is how an untrustworthy comment gets made.
- Don't treat similar-looking code as automatically duplicated. Merging two things that happen to coincide today couples decisions that were independent, and the merge has to be undone the first time they diverge.
- Don't accept "the language makes me" as the end of the analysis. Header declarations and interface specifications repeat information because the compiler needs it repeated; the compiler will at least tell you when the copies disagree, which is not true of anything you duplicate by choice.

## Checklist
- If this rule changed tomorrow, how many places would you have to edit?
- Which of the four kinds is this — imposed, inadvertent, impatient, or interdeveloper?
- Is this field storing something the object could compute?
- Where a copy is unavoidable, is it generated on every build or maintained by hand?
- Would a colleague find this before writing their own version of it?

## Notes
The formulation worth memorising is that every piece of knowledge should have a single, unambiguous, authoritative representation within a system. Stating it in terms of knowledge rather than code is what makes it usable, because the common failures are invisible under a text-matching reading: an unnormalized data model, a comment restating its code, and a specification repeated in a test suite are all duplication, and none of them looks like copy-and-paste.

The reason this outranks most style rules is arithmetic about maintenance rather than aesthetics. Maintenance is not a phase that begins at release — understanding changes daily, requirements arrive mid-build, environments shift, so a system is under maintenance from the first week. Every duplicated fact is a standing obligation to remember, at some unpredictable future moment, that the second copy exists. The question is never whether you will forget; it is when.

The four kinds are worth separating because three of them are not fixed by discipline. Impatient duplication is the one that responds to willpower, and it is the least interesting. Imposed duplication needs a generator. Inadvertent duplication needs the model corrected, and will keep coming back until it is. Interdeveloper duplication needs the cost of discovery lowered, since it arises precisely when nobody involved knows the other copy exists — the state where a governmental audit turned up ten thousand programs each carrying its own version of the same validation.

---
object_id: PAT_detect_linguistic_antipatterns_in_names
object_type: pattern
name: Hunt for Names That Contradict What the Code Does
library_path:
- software-engineering
- core
- readability
stage_binding: 4 final
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- code_review
- cognitive_load
- defects
cross_links:
- rel: related_to
  target_object_id: PAT_match_caller_mental_model
- rel: related_to
  target_object_id: PAT_diagnose_a_code_smell_by_the_cognitive_process_it_breaks
- rel: related_to
  target_object_id: DRILL_audit_identifier_names_in_a_code_review
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Hunt for Names That Contradict What the Code Does

## Pattern Rule
**IF** you are looking for the changes that will most reduce a reader's effort
**THEN** search for places where a name says something the code does not do, and fix those before fixing formatting, because the measured cognitive cost sits with the contradiction and not with the layout.

## Do
- Search the six shapes Arnaoudova defines: methods that do more than they say, that say more than they do, or that do the opposite of what they say; and identifiers whose names claim they contain more, less, or the opposite of what they hold.
- Check the high-base-rate cases first, because they are common enough to be worth a sweep. In seven open-source projects, 64% of identifiers starting with `is` turned out not to be Boolean, 11% of setters also returned a value, and in 2.5% of methods the name and its comment described opposite behaviour.
- Look at the concrete shapes these take — an `initial_element` holding an index rather than an element, an `isValid` holding an integer, a `getCustomers` returning a Boolean.
- Prioritise this over structural tidying when both are on the table. Fakhoury's study found linguistic antipatterns significantly increased oxygenated blood flow while structural inconsistencies produced no statistical evidence of raised cognitive load — even though participants complained loudly about the latter, one of them saying terrible formatting severely increases readers' burden.
- Treat the reader's eye as corroboration: eye-tracking in the same study showed the regions containing linguistic antipatterns were inspected far more than the rest of the code.

## Don't
- Don't take dislike as evidence of cost. The clearest result here is the gap between what participants complained about and what the instruments measured, and a review process driven by irritation will spend its effort in the wrong place.
- Don't dismiss a mismatch because the behaviour is defensible. A `getCustomers` that returns a Boolean may be sensibly checking whether any customers exist, and it is still a name that will mislead.
- Don't treat this as covered by having descriptive names. A name can be perfectly descriptive of something the code does not do — the failure here is disagreement, not vagueness.
- Don't over-read the load evidence. More studies using brain measurements are needed, and Hermans flags the causal account as speculation built on what is known about working memory and the LTM.

## Checklist
- Does every `is` and `has` name here actually hold a Boolean?
- Does any method do something its name does not mention, or omit something its name promises?
- If I am about to raise formatting, is there an unfixed name-behaviour contradiction I should raise first?

## Notes
Linguistic antipatterns are Arnaoudova's term for inconsistencies between the linguistic elements of code — method signatures, documentation, attribute names, types, comments — and the roles those elements actually play. The framing that makes this pair with the code-smell material is Hermans's distinction between *structural* antipatterns, where correct code is arranged badly, and *conceptual* antipatterns, where well-arranged code carries confusing names. The two frameworks are complementary, and a codebase can be clean under one and not the other.

Two mechanisms are proposed for why the contradiction costs so much. The first is misdirected retrieval: reading `retrieveElements()` pulls up what you know about functions returning collections, so you begin reasoning about sorting, filtering and slicing something that is a single element. The second is mis-chunking, the same failure clones produce — `isValid` is assumed Boolean, so the brain never looks closer, and the energy saved buys a wrong assumption that can persist.

Arnaoudova's detector, LAPD, exists as an Eclipse Checkstyle extension for Java. It is worth knowing about and is not the pattern; the six categories are checkable by hand in any language.

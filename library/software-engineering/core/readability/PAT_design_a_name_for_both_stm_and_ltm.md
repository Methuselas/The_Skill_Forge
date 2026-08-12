---
object_id: PAT_design_a_name_for_both_stm_and_ltm
object_type: pattern
name: Make a Name Serve Both the Reader's Parsing and Their Recall
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- readability
- working_memory
- code_comprehension
cross_links:
- rel: related_to
  target_object_id: PAT_use_descriptive_names
- rel: related_to
  target_object_id: PAT_read_code_as_semantic_chunks
- rel: supports
  target_object_id: AP_choose_a_name_with_feitelsons_three_steps
reference:
  source_id: programmers_brain
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u08, pp. 133-136
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Make a Name Serve Both the Reader's Parsing and Their Recall

## Pattern Rule
**IF** you are choosing an identifier name
**THEN** check it twice — once for whether its shape lets a reader split it into parts, and once for whether its words will retrieve anything useful from what the reader already knows — because those are two separate cognitive jobs and a name can pass one while failing the other.

## Do
- Make the parts visibly separable. `name_counter_average` is roughly twice the characters of `nmcntravg` and takes a fraction of the effort to read, because the reader's short-term memory can find the components instead of having to reconstruct them.
- Choose words that will retrieve something. A domain word like `customer` brings associations — buys products, has a name and an address — and a programming-concept word like `tree` brings root, traversal, flattening. That retrieval is the second job, and only the words can do it.
- Use the three categories deliberately when picking words: domain knowledge, programming concepts, and conventions. Conventions are real information too — `j` genuinely does signal the inner counter of a nested loop to most readers.
- Keep the word count within reach. Butler's cap of four words per identifier looks arbitrary but sits close to the working memory's estimated capacity of two to six chunks.

## Don't
- Don't treat a formatting rule as sufficient. Consistent casing and split words help the parsing job and do nothing for retrieval — a perfectly formatted `data_value_2` retrieves nothing.
- Don't treat vocabulary as sufficient either. The right domain word run together with three others and no separators still costs the reader the parsing work first.
- Don't count characters as the cost. The comparison of `nmcntravg` against `name_counter_average` is the direct counter-example — the longer name is cheaper to read.

## Checklist
- Can a reader see where each word in this name ends?
- Does at least one word in it connect to the domain or to a programming concept they will know?
- Is it within about four words?

## Notes
Figure 8.1 traces the split: a name is processed by sensory memory, arrives at the STM where it is broken into chunks, and goes to working memory — while in parallel the LTM is searched for information related to those parts, and whatever is found is fed into working memory alongside. The two arrows into working memory are the two jobs this pattern asks you to check separately.

Figure 8.2 supplies the three retrieval categories and the examples that make them concrete — `customer` and `shipment` for domain, `list`, `tree` and `hashmap` for programming concepts, and `i`, `j`, `n`, `m` for conventions.

The chapter arrives here by reconciling two research positions that look opposed. Butler argues for syntactic rules and Allamanis for consistency across a codebase; Hermans's table 8.3 shows both are cognitively justified but for different reasons — consistency supports chunking, and syntactic similarity lowers the load of processing each name. Neither addresses word choice, which is where the LTM half of this pattern comes from.

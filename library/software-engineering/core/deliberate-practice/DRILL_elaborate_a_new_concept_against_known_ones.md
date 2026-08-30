---
object_id: DRILL_elaborate_a_new_concept_against_known_ones
object_type: drill
name: Elaborate a New Concept Against What You Already Know
target_skill: Connecting a newly learned programming concept to existing knowledge so it can be retrieved later
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
- elaboration
- memory
- deliberate_practice
- onboarding
cross_links:
- rel: supports
  target_object_id: PAT_diagnose_weak_recall_as_storage_or_retrieval
- rel: related_to
  target_object_id: DRILL_practice_syntax_with_flashcards
reference:
  source_title: 'The Programmer''s Brain: What Every Programmer Needs to Know About Cognition'
  author: Felienne Hermans
confidence: high
references: []
variants: []
---

# Elaborate a New Concept Against What You Already Know

## Practice Task
Immediately after meeting a new programming concept, work through a fixed set of questions that force it into contact with concepts you already hold.

## Target Skill
Connecting a newly learned programming concept to existing knowledge so it can be retrieved later.

## Setup
No special setup required. A notebook or scratch file, used at the moment the concept is first encountered rather than later.

## Instructions
1. Write down the new concept and a minimal working example of it.
2. List every concept it makes you think of, without filtering.
3. For each related concept, answer in writing: why does the new one remind me of this? Does it share syntax? Is it used in a similar context? Is it an alternative to something I already use?
4. Write as many alternative ways as you can to achieve the same result — other constructs, other idioms, the longhand version.
5. Ask whether other languages you know have this concept, write an example in each, and note how they differ.
6. Name the paradigm, domain, library, or framework the concept belongs to.

## Success Check
- The related concepts are collected without filtering, and the ones later judged irrelevant stay on the page. Pruning during collection removes exactly the associations that were doing the elaborating.
- Each connection is written as a reason, and the reasons are of more than one kind — shared syntax, similar context, an alternative to something already in use. Connections all of one kind mean one dimension was explored.
- What the concept is an alternative to is stated explicitly, since that is what makes it retrievable later, when the alternative rather than the concept is the thing in hand.
- Alternative ways to reach the same result are written as code, the longhand version included, rather than named.
- The week-later check is performed and its outcome recorded. Whether the written connections reconstruct the concept is the claim being made, and it cannot be evaluated on the day it is written.

## Common Failures
- Writing a definition instead of connections. A definition stored in isolation has nothing to be reached through.
- Deferring the exercise until later, after the details that would have been worth connecting have already been dropped.
- Listing related concepts without saying *why* they are related, which skips the step that does the work.
- Treating an unfamiliar concept as elaborable when it is not yet understood at all — elaboration connects knowledge, it does not supply it.

## Notes
The mechanism is that memories are held in a network rather than a hierarchy, and retrieval strength is higher for items with more connections into that network. Hermans's figure 3.3 puts the two organizations side by side — a filesystem tree of `birds.txt` and `houses.txt` against a graph where Dove, Sparrow, Penguin, Eagle, House, Shed and Zoo all interconnect — and the point is that the right-hand structure is the one you are writing into.

Bartlett's 1930s work is the warning attached to it: participants recalling a Native American folk tale weeks later had reshaped it to fit what they already believed, dropping details they judged irrelevant and substituting a gun for a bow. Material is altered on the way in to fit existing schemata, so deliberately choosing which existing knowledge it attaches to is a way to influence what survives the first save.

---
object_id: PAT_give_every_participant_in_an_operation_a_name
object_type: pattern
name: Give Every Participant in an Operation a Name
library_path:
- software-engineering
- core
- readability
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- naming
- readability
- data_structures
- traversal
cross_links:
- rel: related_to
  target_object_id: PAT_name_unexplained_values
- rel: related_to
  target_object_id: PAT_give_each_variable_exactly_one_purpose
- rel: related_to
  target_object_id: PAT_externalize_intermediate_state_when_tracing
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Give Every Participant in an Operation a Name

## Pattern Rule
**IF** you are writing an operation that involves several distinct things
**THEN** count them, and give each one its own variable — a participant reachable only through an expression such as `current->next` is a thing the reader has to hold without help.
**ELSE** where a participant genuinely has no role of its own and appears once, leave the expression inline; the test is whether the reader has to remember what it refers to, not whether an expression appears.

## Do
- Count the participants before writing the code and check the count against the variables. Inserting into a doubly linked list involves three nodes — the one you insert after, the one that currently follows it, and the new one — and the traditional implementation declares two, leaving the third addressed only as a field of the first.
- Name the missing one and watch the chain disappear. Introducing `followingNode` for what was `currentNode->next` costs one line and removes every doubled dereference, including the one that read `currentNode->next->previous`. The extra line is the price of not making the reader reconstruct the relationship.
- Rename the others to say what role they play in this operation rather than what they were called on arrival. Once three nodes are named, `startNode`, `newMiddleNode`, and `followingNode` describe the arrangement being built, where `currentNode` and `insertNode` describe only where they came from.
- Hoist a chained access out of a loop into a named variable. A rate pulled from `rates->discounts->factors->net` inside a loop body reads as noise and re-walks the chain on each pass; assigned once to a named variable above the loop it reads as a quantity and may cost less, though the second benefit needs measuring before anyone counts on it.
- Draw the thing when the relationships resist description. Pointer and link rearrangements are notoriously hard to hold in prose, and a sketch of the before and after states is often what reveals that a participant has no name.

## Don't
- Don't economize on variables here. Reusing one traversal variable over and over, or leaving a reader to work out what a doubled dereference refers to, saves declarations and spends the reader's attention on bookkeeping that the code could have done.
- Don't assume a short expression is a clear one. Two tokens can still name a participant that the operation depends on, and brevity is not the property being tested — whether the thing has an identity is.
- Don't leave the diagram out of the codebase when it was what made the operation comprehensible. If a picture was needed to write the code, the next person will need it to read the code.

## Checklist
- How many distinct things does this operation touch?
- How many of them have names?
- Is any participant referred to only as a field or index of another?
- Do the names describe the roles in this operation, or only where the values came from?
- Would a sketch of the before and after states help, and does one exist?

## Notes
The failure this addresses is quieter than the usual naming complaints, which is why it goes unnoticed. Nothing is misnamed and nothing is obscure — every symbol in the traditional link-insertion routine is accurate. What is missing is a variable for a thing the operation depends on, so the reader has to carry that thing mentally under a description rather than a name, and then has to keep re-deriving it every time a dereference chain appears. The cost lands on comprehension rather than correctness, which is why the code looks fine to whoever wrote it and reads badly to everyone else.

The diagnostic is arithmetic, and that is what makes it usable. Comparing a count of participants against a count of variables takes seconds and does not require any judgment about whether an expression is complicated enough to deserve a name. In the insertion case the counts are three and two, which is the whole finding — and once the third variable exists, the improved names for the other two follow naturally, because they now have to describe positions in a three-way arrangement rather than just labelling their arguments.

Extra variables here are not in tension with keeping a variable's life short. Both push in the same direction: a participant named immediately above the statements that use it is live for exactly the length of the operation, whereas the same participant reached through a chain has no life at all and is instead reconstructed at each mention. Naming it once is the cheaper arrangement for the reader and for the machine.

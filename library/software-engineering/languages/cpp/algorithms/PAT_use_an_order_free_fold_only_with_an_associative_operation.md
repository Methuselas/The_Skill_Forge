---
object_id: PAT_use_an_order_free_fold_only_with_an_associative_operation
object_type: pattern
name: Use an Order-Free Fold Only With an Associative Operation
library_path:
- software-engineering
- languages
- cpp
- algorithms
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- algorithms
- concurrency
- correctness
- numerics
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_execution_policy_the_loop_body_can_survive
- rel: related_to
  target_object_id: PAT_remember_an_algorithm_cannot_change_a_containers_size
- rel: related_to
  target_object_id: PAT_bound_an_arithmetic_expression_before_trusting_it
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Use an Order-Free Fold Only With an Associative Operation

## Pattern Rule
**IF** you want a fold over a range, or a running-totals computation, to be able to run in parallel
**THEN** use the order-free counterpart of the sequential algorithm, and first confirm that your combining operation is associative — and, for the fold, commutative — because these algorithms may group and order the combinations however they like and an operation that does not satisfy that produces a result which varies between runs
**ELSE** where the operation lacks those properties and the exact left-to-right answer is what you need, the sequential algorithm is correct and its lack of a parallel form is the reason rather than an oversight.

## Do
- Learn the pairings, since the names do not make the relationship obvious. The ordered left fold has an order-free counterpart; the ordered running-totals algorithm has a family of order-free scans. Each pair computes the same thing for operations that qualify and differs entirely for operations that do not.
- Read the requirement as being on your operation rather than on your data. Associativity says the grouping does not matter; commutativity says the order does not. The algorithm needs both to be free to split the range, combine the pieces on separate threads, and merge the partial results in whatever order they finish.
- Treat floating-point addition as the case that catches people, because it is the most common combining operation there is and it is not associative. Summing the same doubles with an order-free fold can give a different total on different runs, and the difference is real rather than a rounding display artefact.
- Choose between the inclusive and exclusive scan on whether the output at each position includes the input at that position. That is the whole distinction, and getting it wrong shifts every result by one place.
- Reach for the fused transform-and-fold form where you would otherwise transform into a temporary and fold that. It applies a callable to one range, or a binary callable across two, and folds the result without materializing the intermediate.

## Don't
- Don't treat the order-free fold as a drop-in replacement for the ordered one. They have the same shape, the same arguments, and different contracts — so the substitution compiles, runs, and quietly changes the guarantee from a specified result to an unspecified one.
- Don't go looking for a parallel policy on the ordered fold. There is not one, and the reason is this card: the algorithm is specified as a left fold, and a left fold is exactly what cannot be reordered.
- Don't dismiss non-determinism because the answers look close enough. An answer that differs between runs is not reproducible, which makes every downstream comparison, test, and regression check unreliable in a way that is much more expensive than the difference itself.

## Checklist
- Is the combining operation associative? Is it commutative?
- If it is floating-point arithmetic, has the variation between runs been considered acceptable?
- Does the code need the exact ordered result, or only a correct total?
- For a scan, does the output at each position include the input there or not?
- Is there a transform feeding a fold that could be fused?

## Notes
The library's decision to introduce new names rather than add a policy argument to the existing algorithms is the informative part. A policy argument would have implied that the parallel version computes the same thing faster; a different name says correctly that it computes something under a different contract. Where the operation qualifies, the two agree; where it does not, they were never the same function.

The requirement is easy to satisfy accidentally and easy to violate accidentally, which is why it deserves an explicit check. Integer addition, multiplication, minimum, maximum, and the bitwise operations all qualify. Floating-point addition and multiplication do not, subtraction does not, and neither does anything that accumulates into external state or depends on the sequence it sees.

The connection to the missing parallel form is worth holding onto, because it converts an apparent gap in the library into a statement about the problem. The ordered fold has no parallel version not because nobody wrote one but because the thing it promises — combine these strictly left to right — has no parallel meaning.

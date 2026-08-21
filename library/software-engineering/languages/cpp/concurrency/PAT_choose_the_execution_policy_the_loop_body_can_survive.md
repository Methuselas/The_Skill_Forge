---
object_id: PAT_choose_the_execution_policy_the_loop_body_can_survive
object_type: pattern
name: Choose the Execution Policy the Loop Body Can Survive
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 4 final
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- parallelism
- algorithms
- performance
cross_links:
- rel: related_to
  target_object_id: PAT_decide_if_the_problem_is_worth_parallelizing
- rel: related_to
  target_object_id: PAT_check_for_memory_saturation_before_adding_threads
- rel: related_to
  target_object_id: PAT_do_not_create_a_thread_for_every_task
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Choose the Execution Policy the Loop Body Can Survive

## Pattern Rule
**IF** you are adding an execution policy to a standard algorithm call to make it run in parallel
**THEN** check the policy against what the callable actually does — anything holding a lock or otherwise unsafe to interleave rules out the unsequenced policy — and confirm by measurement that the sequence is long enough for parallelism to pay at all
**ELSE** where the sequence is short or the per-element work is trivial, the sequential policy is not a fallback but the correct answer, and it is what the call already does without a policy.

## Do
- Read the three policies as three different promises. The sequential policy runs the algorithm on one thread exactly as an unpolicied call would. The parallel policy permits execution across threads. The parallel-unsequenced policy additionally permits operations to be interleaved *within* one thread, which is what allows vectorization.
- Treat any lock inside the callable as disqualifying the unsequenced policy. If one thread processes several elements in an interleaved fashion, it can try to acquire a lock it already holds, and the second acquisition blocks a thread that will never reach its own release — a guaranteed deadlock. The standard names such code vectorization-unsafe and excludes it from unsequenced policies.
- Establish the crossover with a benchmark rather than a rule of thumb, because it depends on three things at once: the sequence length, the cost per element, and the implementation. Thirty-two thousand elements with substantial per-element work scaled well; a thousand elements ran slower than sequential; and thirty-two thousand elements incrementing a double gained nothing at all.
- Expect the hardest algorithms to pay best. Sorting doubles — cheap comparisons, cheap swaps, and genuinely difficult to parallelize — showed strong speedup above about a thousand elements, which is a better return than a trivially parallel loop over the same data.
- Budget for the build setup before promising anything. The parallel headers ship with recent compilers, but the threading runtime underneath is a separate library whose version must match the compiler's exactly, and it has to be on the library path at run time.
- Check the algorithm you want actually has a parallel form. The set is incomplete — accumulation notably has no parallel overload — so a policy argument is not uniformly available.

## Don't
- Don't assume the unsequenced policy is a free upgrade over the parallel one. It permits an additional transformation that changes what the callable must tolerate, and the code that violates it compiles cleanly and deadlocks at run time.
- Don't parallelize a memory-bound loop and expect a gain. Incrementing every element of a large array is limited by memory traffic, and more threads share the same path to memory rather than adding capacity.
- Don't use a policy on short sequences inside a hot loop. The implementation launches and joins threads on each call, so the setup cost is charged every time and dominates when the work is small.
- Don't expect parallel algorithms to cooperate over the machine. Each call tries to use every available processor, so two running at once compete, and there is no way to apportion them.
- Don't skip thread safety because the algorithm is standard. A policy makes the calls concurrent; whatever the callable touches is subject to the same rules as any other threaded code.

## Checklist
- Does the callable take a lock, or do anything else that breaks if interleaved within one thread?
- What is the measured crossover length for this algorithm with this per-element work?
- Is the loop limited by computation or by memory traffic?
- Is this call inside something that runs often, paying thread setup each time?
- Does the algorithm have a parallel overload at all, and is the runtime library version matched to the compiler?

## Notes
The distinction between the two parallel policies is easy to under-read because vectorization sounds like something the compiler does anyway — and it does, without any help from the source. What the unsequenced policy adds is permission to interleave the *callable's* operations, which is a statement about the code you wrote rather than about the loop. That is why the requirement lands on the body and why the failure is a deadlock rather than a wrong answer.

The setup cost that makes short sequences lose is an implementation property rather than a requirement of the standard. It comes from starting threads at the beginning of each parallel call and joining them at the end, which is how the current mainstream implementations bridge to their threading runtime. Worth knowing because it is the kind of thing that changes between library versions, and because it explains why the crossover exists at all.

Where these algorithms are strong is worth stating alongside the caveats. Given enough data, they deliver good speedups on algorithms that are awkward to parallelize by hand, with no concurrency code of your own to get wrong — which is a much better trade than it appears from a list of restrictions.

One consequence of naming a policy at all has nothing to do with which policy you name, and it is the least expected thing here: it changes what happens when the callable throws. A call without a policy propagates the exception normally, so a handler around the call catches it. A call *with* a policy does not — an exception escaping the callable calls the terminate handler, which by default aborts the program. That applies to the sequential policy too, so adding the policy that promises to change nothing about how the algorithm runs still changes how it fails. Any callable that can throw needs to catch inside itself before this is used, and code being converted to policied calls should be checked for handlers that are about to stop working.

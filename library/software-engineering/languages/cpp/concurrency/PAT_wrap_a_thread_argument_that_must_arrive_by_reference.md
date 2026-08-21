---
object_id: PAT_wrap_a_thread_argument_that_must_arrive_by_reference
object_type: pattern
name: Wrap a Thread Argument That Must Arrive by Reference
library_path:
- software-engineering
- languages
- cpp
- concurrency
stage_binding: 2 block
lane_fit: both
foundation_role: specialization
routing_class: specialized
specialization_axis: language
foundation_object_id: none
tags:
- cpp
- concurrency
- threading
- parameter_passing
- lifetime
cross_links:
- rel: related_to
  target_object_id: PAT_make_threads_unjoinable_on_every_path
- rel: related_to
  target_object_id: PAT_name_every_lambda_capture
- rel: related_to
  target_object_id: PAT_know_when_two_accesses_are_a_data_race
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Wrap a Thread Argument That Must Arrive by Reference

## Pattern Rule
**IF** you are handing an argument to a thread's callable and that callable declares the corresponding parameter as a reference
**THEN** wrap the argument in a reference wrapper at the construction site, because the thread stores its arguments by copy and the parameter will otherwise bind to that internal copy rather than to your object
**ELSE** where the callable takes the parameter by value, or the work is a lambda that captures what it needs, no wrapper belongs there and adding one only reintroduces a lifetime obligation you did not have.

## Do
- Distinguish the two routes an argument takes into a thread, because only one of them has this problem. Arguments passed to the thread's constructor are stored by the thread and then forwarded; things a lambda captures are captured by the lambda under whatever capture mode you wrote, and a capture by reference already refers to the original.
- Make the wrapping visible at the construction site rather than buried in the callable's signature. The function's declaration says it takes a reference; nothing at the call site says whether it will receive one, so the wrapper is the only thing distinguishing the two behaviours to a reader.
- Take on the lifetime obligation deliberately once you have wrapped. A reference that genuinely reaches the thread is a reference into the creator's scope, and that scope must outlive the thread — which turns this into a question about how the thread is joined rather than a question about arguments.
- Prefer passing by copy where the work does not need to write back. The copy has no lifetime obligation at all, and the cost is usually smaller than the reasoning the alternative requires.

## Don't
- Don't assume a parameter declared as a reference will be bound to your object. The mismatch produces no diagnostic in the ordinary case: the code compiles, the thread runs, the function modifies something, and the modification lands on a copy the caller cannot see.
- Don't combine a wrapped reference with a detached thread. The creator's scope ends while the thread continues to use what it referred to, and this reaches further than the obvious variables — the standard output stream's lifetime is tied to the main thread, so even printing from a detached thread can outlive what it prints to.
- Don't reach for the wrapper to avoid a copy you have not measured. Its purpose is to make write-back reach the caller, and using it as an optimization buys a lifetime problem in exchange for an unquantified saving.

## Checklist
- Does the thread's callable declare any parameter as a reference?
- Is the corresponding argument wrapped at the construction site?
- If it is, what guarantees the referred-to object outlives the thread?
- Is the thread detached, and if so does it refer to anything in the creator's scope?

## Notes
The default is a copy for a good reason, which is worth knowing so the wrapper reads as an opt-in rather than as boilerplate. A thread outlives the expression that created it, so decaying arguments to copies is the choice that is safe by construction; binding references into a scope that may already be gone is the dangerous case, and the language makes you ask for it by name.

What makes the failure hard to catch is that both halves look right in isolation. The function's signature says reference, the call passes the variable, and every reviewer reading either half sees what they expect. Only the pairing is wrong, and it is wrong silently.

The lifetime consequence is the same one that governs joining and detaching, approached from the other side. There the question is what happens to the thread when the scope ends; here it is what the thread is still pointing at when it does. A thread that owns copies of everything it needs makes both questions go away.

---
object_id: PAT_give_every_acquired_resource_one_named_owner
object_type: pattern
name: One Named Owner, Everything Else Borrows
library_path:
- software-engineering
- core
- design
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- resources
- lifetime
- ownership
- interfaces
- design
cross_links:
- rel: related_to
  target_object_id: PAT_design_shutdown_for_process_lifetime_objects
- rel: related_to
  target_object_id: PAT_pop_the_teardown_entry_before_running_it
- rel: related_to
  target_object_id: PAT_test_what_happens_when_a_resource_runs_out
- rel: related_to
  target_object_id: PAT_pass_the_cancellation_signal_through_the_call_graph
reference:
  source_title: PASS software-engineering canonical synthesis
  author: Multiple accepted sources
confidence: medium
references: []
variants: []
---

# One Named Owner, Everything Else Borrows

## Pattern Rule
**IF** something is acquired that must later be released — memory, a file, a connection, a lock, a subscription, a registration, a running task
**THEN** name exactly one place that owns it and is answerable for releasing it, treat everything else as borrowing it under the condition that no borrower outlives the owner, and put that decision somewhere a reader can see rather than in a comment
**ELSE** where the thing genuinely lives as long as the process and is reclaimed when the process ends, say so deliberately — that is a legitimate answer, and it rests on something outside the program doing the reclaiming, which is an assumption about the platform rather than a property of the code.

## Do
- Name the owner as a place, not as a stage. The answer has to be a particular component, structure, or scope that holds the thing and releases it. Answers of the form that it gets cleaned up at the end, or that the caller handles it, are the absence of an owner written in a way that sounds like one, and they survive review because nobody can point at the moment they become false.
- Default to one owner with everyone else borrowing, and make sharing argue for itself. Shared ownership is the right answer when the lifetimes genuinely do not nest, and it is reached for far more often than that, usually to avoid having to work out which of two candidates should own the thing. The test is whether you can name the second owner and say why it may outlive the first; where you cannot, you wanted one owner and a borrow.
- Make transfer visible at the boundary, and expect it to be commoner than it looks. A reader looking at an interface should be able to answer whether calling it hands the thing over, without reading the implementation: where the language can carry that in the type, let it, and where it cannot, the documentation carries it and must state it rather than implying it through the name of the function. Treat this as ordinary traffic rather than an advanced case — a substantial share of the code that releases things never acquired them, so the convention between the two sides is load-bearing, and where nothing in the type records it the cost appears as a thing released twice or never rather than as anything visible at the call site.
- Check that something actually reclaims before relying on the process ending to do it. The escape above is ordinary application reasoning and it is borrowed from an environment that happens to hold: an operating system that reclaims a process's memory, descriptors and handles when it exits. Where that reclaimer is absent or is the thing you are writing — kernel and driver code, embedded targets, a long-lived host running plugins, anything holding a resource owned by a system that outlives it — the acquisition simply persists, and it persists for the life of the machine rather than the life of the run. The rule does not change in those places; what changes is that the escape is unavailable and nothing will tell you so.
- Count the ways out before writing a release by hand. Every early return, every loop exit, and every failure that unwinds is a path the release has to be correct on, and the count is reliably larger than it looks from the top of the routine. Where the language can bind release to leaving a scope, that mechanism gets it right on paths that do not exist yet. Without such a mechanism the release sites for a single acquisition routinely reach three, and a routine with real error handling can need most of ten, every one of which has to be correct and stay correct as branches are added.
- Identify the longest-lived borrower and check it ends first. Ownership is only half the arrangement; the other half is the claim that every borrower is gone before the owner releases. The one that breaks it is usually something stored rather than something passed, because storing a borrowed thing quietly converts it from something used within a call to something held across many.
- Ask what releases the things that are not memory, in every language including the ones that collect. Automatic memory management is exactly what its name says, and files, sockets, locks, registrations, timers, watches, and running tasks are none of them memory. Those need an owner and an explicit release in a collected language on the same terms as anywhere else, and the collector will not report their absence.
- Treat a registration as an acquisition. Anything added to a list somebody else holds — a callback, an observer, a handler, a metric, a route — has been acquired by that list, and the code that added it owns removing it. This is the acquisition most often missed, because nothing was allocated and the operation reads as configuration rather than as taking something.

## Don't
- Don't accept the runtime as the owner of a scarce resource. A finalizer runs when the collector gets round to it, which may be long after the descriptors ran out, and for many runtimes may be never — so a release that matters cannot be attached to one.
- Don't reach for shared ownership as a way of postponing the decision. It does postpone it, and what arrives later is a lifetime nobody can reason about and a release that happens at whichever point the last holder happened to finish.
- Don't leave the ownership rule in a comment when the interface could carry it. A comment is checked by whoever reads it, which is not everyone, and it stays unchanged when the function's behaviour changes.
- Don't let a borrowed thing be stored without deciding what happens when the owner releases. Storing it is the moment the arrangement changed, and it is the moment that gets no attention, because the code that stores it is usually correct on the day it is written.

## Checklist
- What single place releases this, and what happens if that place goes away first?
- If the answer is that the process ends, what performs the reclaiming, and does it exist here?
- Can a reader tell from the interface whether calling it transfers ownership?
- Which borrower lives longest, and does it certainly end before the owner does?
- If this is shared, who is the second owner, and why can the lifetimes not nest?
- Does the release still happen on the paths where something failed part way through?
- If the runtime reclaims memory, what is releasing everything here that is not memory?
- Was anything registered with something else, and who removes it?

## Notes
Automatic memory management creates the blind spot this card exists for, because it solves one instance of the problem completely and leaves every other instance untouched, while removing the daily practice that would have kept the general shape in view. A codebase in a collected language still closes files, releases connections, stops timers, and unsubscribes handlers by hand, in numbers comparable to a codebase in a language without a collector — the difference is that the discipline is no longer exercised on the most common resource, so it is not reliably present when a less common one appears. The question worth carrying into any language is not whether memory is managed but which acquisitions the manager does not cover, and that list is long everywhere.

Borrowing as the default is the part that keeps ownership from spreading. Most code that uses a thing has no reason to own it: it needs the thing for the duration of a call and has no interest in when it is released. Making that the normal case leaves a small number of places holding things and a large number merely using them, which is the arrangement in which the question of who releases what stays answerable. The failure mode runs the other way — every component that needs a thing acquires its own claim on it, and the lifetime becomes the union of everything that ever touched it, at which point release happens at a moment determined by nothing in particular.

Putting the decision at the boundary is what makes it survive contact with people who did not make it. Ownership is a fact about an arrangement rather than about a line of code, so it is invisible at exactly the moment a maintainer needs it: they are looking at one call site, deciding whether they may keep the thing they were handed. An interface that answers this — by type where the language allows, by explicit statement where it does not — answers it for every such maintainer without any of them having to reconstruct the arrangement. One that does not will be guessed about, and the guesses will be reasonable, and some of them will be wrong in ways that appear as a resource exhausted under load or a release that happened while somebody was still reading.

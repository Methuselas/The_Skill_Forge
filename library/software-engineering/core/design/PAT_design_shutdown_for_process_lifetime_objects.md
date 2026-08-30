---
object_id: PAT_design_shutdown_for_process_lifetime_objects
object_type: pattern
name: Design Shutdown for Process-Lifetime Objects
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
- design
- lifetime
- shutdown
- global_state
- resource_management
cross_links:
- rel: related_to
  target_object_id: PAT_avoid_global_state_inject_shared_state
- rel: related_to
  target_object_id: PAT_pop_the_teardown_entry_before_running_it
- rel: related_to
  target_object_id: PAT_manage_resources_with_raii_objects
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Design Shutdown for Process-Lifetime Objects

## Pattern Rule
**IF** an object is created once and lives for the length of the process — a logger, a connection pool, a device handle, a cache, anything reached through a global accessor
**THEN** decide explicitly what happens to it at shutdown, because the automatic answer is an order you did not choose and cannot see.
**ELSE** where something does reclaim what it holds once the process ends, and it holds nothing that outlives the process, decide deliberately not to destroy it and record that as the decision — including what you are relying on to do the reclaiming.

## Do
- Establish whether this code owns the process before treating process exit as the boundary. A library, a plugin, a loaded module, or anything running inside a host has no exit of its own: what it gets is being unloaded while the program carries on, and possibly loaded again later. Everything it abandoned then stays held by a process that is still running, so the reasoning that exit will tidy up is not weakened here but absent, and the lifetime in this card's title belongs to the host rather than to you.
- Check that a reclaimer exists at all, rather than which resources it covers. The familiar split between memory the system takes back and handles it does not assumes a protected process boundary underneath. Without one — kernel and driver code, an embedded target, a system with no memory protection — nothing is returned when a program ends, and the memory case that is normally the safe half becomes permanent until the machine restarts.
- Separate the two questions. Whether the object must be torn down at all is about what it holds; when it is torn down relative to others is about who uses it during their own teardown.
- Ask what still uses it while the program is coming down. Anything that reports errors, flushes buffers, or writes diagnostics is used by other objects' teardown, and therefore must outlive them — which is the reverse of what creation order will usually give you.
- Where an object must survive to the end, take control rather than hoping: register teardown explicitly with an order you choose, or keep it alive deliberately and release only what the system will not.
- Make use-after-teardown detectable rather than silent. A flag set during teardown, checked by the accessor, converts a corrupt read into a diagnosable failure at the cost of one test per access.
- Where an object must be available even after it has been torn down, arrange for it to be recreated on demand and re-registered for teardown, rather than handing back the remains of the old one.

## Don't
- Don't assume "the process is exiting anyway" settles it. Memory is reclaimed by the system, and that reasoning is sound for memory alone; handles held in the kernel, locks shared between processes, sessions open on a server, and files with buffered writes are not the same case and can survive the process that abandoned them.
- Don't rely on creation order to give you a usable teardown order. Objects created lazily are created in whatever order the program first touched them, which depends on the input, and the teardown order inherits all of that.
- Don't let the object that everything reports to be an ordinary participant in that order. It will be destroyed partway through, and the failures that occur after that point are exactly the ones nobody will see reported.
- Don't answer this once for the program. Objects differ in what they hold and in who needs them late, so a single blanket policy will be wrong for the ones that matter most.

## Checklist
- What does this hold that will not be reclaimed if the process simply ends, and what performs that reclaiming?
- Does this code own the process whose exit it is relying on, or is it loaded into somebody else's?
- Which other objects use this during their own teardown, and are they guaranteed to go first?
- If something reaches this after it has been torn down, what happens — a diagnosable error, or a read of whatever is left?
- Is the chosen order written down somewhere, or does it emerge from whichever code path ran first?

## Notes
The trap is that shutdown appears to be the safest part of the program. Nothing new is being computed, the work is done, and the code that runs is short — so the ordering is rarely designed, and it ends up determined by the order of first use, which is determined by the input.

The distinction between reclaimed memory and released resources is what makes the lazy answer wrong in the cases that matter. Skipping teardown is genuinely harmless for a process holding nothing but its own memory, and genuinely harmful for one holding anything the system tracks on its behalf — and the difference is invisible in testing, because a short-lived test process that leaks a handle looks exactly like one that does not.

Both halves of that distinction rest on a process boundary that somebody else maintains, which is worth making explicit because it is the assumption that travels worst. Code written as a program can treat exit as a backstop and be right; the same code compiled into a library cannot, because it is never the thing that exits. Its ending is an unload inside a process that keeps running, so what would have been reclaimed is simply retained, and it is retained by a host that may load the module again and expect a clean start. The same reasoning fails a second way further down, where there is no protected boundary to reclaim anything: in kernel, driver, and unprotected embedded environments the memory case loses its exemption too, and an abandoned allocation lasts until the machine is restarted. Neither situation is exotic, and in both the card's rule is unchanged while its escape has quietly gone.

The object used by everyone else's teardown deserves separate treatment, and it is usually the logger. It must be constructed before anything reports to it and destroyed after everything that might, which no automatic scheme derived from construction order will produce. Either it is exempted from the ordering by hand, or it is made able to come back after it has gone.

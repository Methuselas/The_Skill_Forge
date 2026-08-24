---
object_id: PAT_pop_the_teardown_entry_before_running_it
object_type: pattern
name: Pop the Teardown Entry Before Running It
library_path:
- software-engineering
- core
- design
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- design
- shutdown
- reentrancy
- registries
- lifetime
cross_links:
- rel: related_to
  target_object_id: PAT_design_shutdown_for_process_lifetime_objects
- rel: related_to
  target_object_id: PAT_have_the_doer_record_the_undo
- rel: related_to
  target_object_id: PAT_publish_changes_and_let_consumers_register
reference:
  source_title: 'Modern C++ Design: Generic Programming and Design Patterns Applied'
  author: Andrei Alexandrescu
confidence: high
references: []
variants: []
---

# Pop the Teardown Entry Before Running It

## Pattern Rule
**IF** you are draining a registry of cleanup actions — shutdown hooks, finalizers, deferred releases, teardown callbacks
**THEN** remove each entry from the registry before running it, not after, because running one can add another and an entry still in place while it executes can be reached twice.

## Do
- Take the entry off, then execute it. The two steps are usually written as one line and the order inside that line is the whole content of this.
- Expect the registry to grow while you are draining it. Cleanup routinely constructs things — a final log message, a flush that opens a buffer, a notification that builds a payload — and anything constructed during teardown registers its own teardown.
- Drain with a loop that re-reads the registry each pass rather than iterating a snapshot taken at the start. A snapshot silently discards everything added during the drain.
- Make the drain safe to enter twice. A cleanup action that fails part-way, or a shutdown reached through two paths, should find an entry already gone rather than run it again.

## Don't
- Don't hold an index or iterator across the execution of an entry. The registry can be reallocated or reordered by something the entry did, and the position you were holding no longer means what it meant.
- Don't drain by walking the registry and clearing it at the end. Everything registered during the walk is either lost or run twice, and which one it is depends on the container.
- Don't assume a cleanup action does nothing but release. The ones that report, flush, or notify are common, and those are precisely the ones that build something new on their way out.
- Don't let a failing entry abandon the drain. The remaining entries are still registered and still holding resources, and stopping at the first failure leaves all of them.

## Checklist
- Is each entry removed before it runs, in that order?
- If an entry registers a new one, does the drain pick it up?
- If an entry throws or fails, do the remaining entries still run?
- Can the drain be entered a second time without running anything twice?

## Notes
The re-entrancy here is easy to dismiss as a corner case and is in fact the ordinary path. Teardown is when programs write their final diagnostics, and writing a diagnostic tends to construct something — which registers its own cleanup, on the very registry currently being drained. The mechanism must handle growth during its own execution because that is what its normal use looks like.

Ordering the two operations correctly costs nothing and is invisible when right, which is why it is worth stating as a rule rather than rediscovering. An entry removed before execution cannot be reached again by anything the execution triggers; an entry removed afterwards is live and reachable for the whole time the cleanup runs, and whether that causes a double release depends on details nobody wants to reason about at shutdown.

The symptom when this is wrong is unhelpful in a characteristic way. The program has finished its work and produced its output, and the failure appears after everything a user cares about has already happened — so it reads as a harmless noise at exit, gets an exclusion added to the test suite, and stays until the day the doubled release is of something the system was tracking.

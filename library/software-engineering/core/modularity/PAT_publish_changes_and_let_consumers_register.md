---
object_id: PAT_publish_changes_and_let_consumers_register
object_type: pattern
name: Publish Changes and Let the Interested Parties Register
library_path:
- software-engineering
- core
- modularity
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- coupling
- events
- model_view_separation
- modularity
cross_links:
- rel: related_to
  target_object_id: PAT_design_modular_interfaces
- rel: related_to
  target_object_id: PAT_single_source_of_truth_for_data
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Publish Changes and Let the Interested Parties Register

## Pattern Rule
**IF** several parts of a system have to react when one piece of data or state changes
**THEN** keep the thing that changes ignorant of who cares — let each interested part register for the specific changes it wants and be notified of those — instead of having the changing code call its consumers or pushing everything through one central routine.

## Do
- Keep one authoritative model and build each consumer as an interpretation of it. A spreadsheet's grid, its bar chart, and its running-total box are three readings of one set of numbers, not three copies of the numbers.
- Register per event rather than per application, so an object receives only what it asked for and never has to filter a firehose to find its own business.
- Chain it when the data is rich. A consumer that filters or summarizes what it receives becomes a model for the next consumer, so what forms is a network of models and readers rather than one flat fan-out — and one reader can draw on several models at once.
- Apply it outside user interfaces. A view is any interpretation of the model and need not be graphical; the coordinating half need not be tied to any input device. A component that watches a live feed for a condition and reports it is the same structure as a chart.
- Add a debugging view once the network is more than a layer deep — one that shows a model's internals in full, plus a trace of individual events. It is cheap to build while the design is fresh and painful to reconstruct later.

## Don't
- Don't push all events through a single routine. That routine then has to know how many objects interact and in what combinations, which is precisely the knowledge you were arranging not to need; the recognisable symptom is one huge case statement or multiway if-then dispatching on event kind.
- Don't hold three copies of the data because three things display it — the copies drift and reconciling them becomes its own subsystem.
- Don't broadcast everything to everyone as the simple version. Sending objects events they did not ask for reintroduces the coupling in a form that is harder to see, because nothing in the code names the dependency.
- Don't claim this buys full independence. Publisher and subscribers still agree on an interface and a calling convention, and a subscriber still has to hold a reference to register.

## Checklist
- Does the code that changes the data name any of the things that display it?
- Is any consumer receiving notifications it never registered for?
- If a fourth consumer were added tomorrow, which existing file would have to change?
- Is the data stored once, or once per reader?

## Notes
Splitting a program into modules with single responsibilities creates a second problem that the split itself does not solve: at runtime those modules still have to keep each other current. Answering it by having the changing module call the modules that care re-couples what was just separated, and answering it with one central dispatcher concentrates all of that knowledge in a single place — which is worse, because that place now depends on every participant.

Registration inverts who holds the knowledge. The publisher knows only that it has subscribers; it does not know what they are, how many there are, or what they do with a change. The subscriber knows what it wants and asks for that. Adding a consumer therefore touches one file — the new one.

The generalisation past the graphical case is the part that is easy to miss, because the idiom is nearly always taught with a window on the screen. A model is whatever holds the facts, a view is any interpretation of them, and the coordinating piece is any mechanism that feeds new facts in. Once that is clear, the same structure covers a scoring feed, a monitoring pipeline, or a report generator — and the chaining property matters most there, because each layer of interpretation is an abstraction the next layer gets to work in rather than reconstructing.

What this does not do is remove the last of the coupling. Both sides still agree on the shape of a notification and both still exist in each other's world well enough to connect. That residue is the reason the fully anonymous alternative exists, and it is worth knowing which of the two you actually need.

---
object_id: PAT_build_a_way_to_see_inside_the_running_system
object_type: pattern
name: Build a Way to See Inside the Running System
library_path:
- software-engineering
- core
- testing
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- testability
- diagnostics
- observability
- logging
cross_links:
- rel: related_to
  target_object_id: PAT_design_for_testability
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Build a Way to See Inside the Running System

## Pattern Rule
**IF** code will run somewhere you cannot attach a debugger — in production, on a customer's machine, on a device in the field
**THEN** build the observation points into the software itself while you are writing it, so its internal state can be read while it runs, by someone who is not you.

## Do
- Emit diagnostics in a regular, consistent format so a program can read them. That is what makes it possible to derive processing times or reconstruct the path the code actually took; output where every message was formatted however its author felt at the time is hard for a person to read and impossible for a tool to parse.
- Provide a deliberate way in that is not the debugger. An interactive application can put a diagnostic panel behind a key sequence users are never told about; a long-running server can serve its own status, counters, and recent log entries on a side channel. Neither has to be a documented feature to be worth building.
- Decide what internal state is worth exposing at the time you write the module, while you still know which values would explain a failure. That knowledge decays fast, and it is completely gone by the time someone is trying to use it.
- Plan for this in the expectation that the tests missed something. Production has conditions no test environment reproduces, and faults that never appeared under test come out there — so the channel for looking at them is designed in rather than improvised during an incident.

## Don't
- Don't assume you will be able to reproduce a production problem somewhere convenient. The reason to build the window is precisely the cases where you cannot, and those are the expensive ones.
- Don't scatter unstructured diagnostic output through the code and count it as instrumentation. Volume is not visibility; inconsistent diagnostics are noise that has to be read line by line at the worst possible moment.
- Don't confuse this with testing. It does not tell you whether the code is correct — it tells you what the code is currently doing, which is a different question and the only one available once the software has shipped.

## Checklist
- If this failed at a customer site overnight, what would somebody need to look at?
- Could a script parse these diagnostics, or does a human have to read every line?
- Is there any way to see internal state without stopping the process?
- Do you still know, right now, which values would explain a failure here?

## Notes
Hardware makes this obligation visible in a way software does not. A chip is designed to be testable not only at the factory and at installation but in the field once deployed, which is why complex parts carry built-in self-test and a mechanism for external equipment to feed in stimuli and read back responses. Software has no equivalent of a test pin, so the equivalent has to be constructed — and because it has to be constructed deliberately, it is routinely not constructed at all.

What makes this a design decision rather than a logging convention is when it has to be made. The valuable state to expose is obvious while you are writing the module and obscure afterwards, and the person who eventually needs it is usually not you and usually working under time pressure. Adding the window later means guessing which values would have mattered, from a position where you already do not know what went wrong.

The consistency requirement is the part most often dropped, and it is the part that converts diagnostics from a last resort into a tool. Regular, parseable output can be processed automatically to answer questions nobody thought to ask when writing it — how long a stage took, how often a path was taken, whether two events ever overlapped. Free-form output can only answer questions you already know to ask, by reading, one line at a time.

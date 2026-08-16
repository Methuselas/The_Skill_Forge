---
object_id: PAT_make_the_development_build_fail_louder_than_production
object_type: pattern
name: Let the Development Build Be Obnoxious and the Shipped One Graceful
library_path:
- software-engineering
- core
- error-handling
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- defensive_programming
- debugging
- error_handling
- build_configuration
cross_links:
- rel: related_to
  target_object_id: PAT_fail_fast_near_error_source
- rel: related_to
  target_object_id: PAT_barricade_dirty_data_at_a_named_boundary
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Let the Development Build Be Obnoxious and the Shipped One Graceful

## Pattern Rule
**IF** you are writing code that detects a condition which should not happen
**THEN** make it as loud as possible in the development build and as survivable as possible in the shipped one — the same detection, two behaviours, chosen by build configuration.
**ELSE** where the consequence of the undetected error is trivial, compile the check out of production entirely rather than leaving noise behind.

## Do
- Decide per area of the program what an undetected error would actually cost. A messy screen in a spreadsheet's redraw is survivable; a wrong number from its calculation engine is not, and the two deserve different amounts of checking.
- Keep the checks that let the program die well. Leaving deliberate debug code in the shipped build is what let JPL diagnose a fault on the Mars Pathfinder after landing and upload corrected code, and the mission completed.
- Downgrade rather than delete. An assertion that halts during development can log to a file in production instead of vanishing, which keeps the diagnosis available without the crash.
- Give a default case something to say. Where five kinds of event are expected, the default should shout during development that a sixth exists and fix the program — and write quietly to an error log in production.
- Refuse to inherit production's constraints in the development build. It may run slow, use resources extravagantly, and expose dangerous operations that no shipped build would; a menu item that verifies a fragile data structure, or an idle-loop integrity check, buys diagnosis cheaply.
- Build the debugging aid the *first* time a problem bites, not the third. Written early it helps for the rest of the project, and it can be carried into the next one.
- Make aids switchable without a fuss — version control, precompiler switches, or a stub whose production version returns immediately.

## Don't
- Don't ship the hard crash. During development a debugging message followed by a crash is the right response even to a minor error; in production users need the chance to save their work, and they will forgive several anomalies before they forgive lost work.
- Don't leave internal messages facing users. Someone eventually reads out the one that ended "Dog Breath!" over the phone — an "internal error" notice with a way to report it does the same job.
- Don't check everything everywhere. Validating every parameter in every conceivable way makes the program fat and slow, and defensive code is no more defect-free than any other code — more so when written casually.
- Don't confuse this with failing fast generally. The claim here is narrower and stranger: the *same* detection deliberately behaves differently in two builds, which is a decision people skip because it feels like two implementations of one thing.

## Checklist
- For this check: what does it do in the development build, and what in production?
- Which areas of this program can afford undetected errors, and which cannot?
- Would this crash cost a user their work?
- Can the aids be switched on and off without editing code?
- Is there a debugging aid you have wished for twice and still not written?

## Notes
The paradox that makes this worth stating is that the two builds want opposite things. During development you want the error to be obnoxious, because an error you can overlook is an error that ships. In production you want it unobtrusive, because the person in front of it did not write the code and cannot act on the diagnosis. Treating those as one requirement forces a compromise that serves neither, and the compromise usually lands on the production side, which is where the loud version would have paid.

Offensive programming is the name for the development half — exceptional cases made obvious while you are still in a position to fix them. The underlying claim is that a dead program does considerably less damage than a crippled one, which is true in development and false in front of a user, and that reversal is the whole pattern.

The counterweight comes from the same chapter and deserves equal weight. Too much defensive programming is its own defect: it adds bulk, costs speed, and adds complexity, and none of that code is immune from being wrong. So the decision is not how defensive to be in general but where — checks concentrated where an undetected error is expensive, and removed where it is not.

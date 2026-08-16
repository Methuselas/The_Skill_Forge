---
object_id: PAT_barricade_dirty_data_at_a_named_boundary
object_type: pattern
name: Draw a Line Where Data Becomes Trusted
library_path:
- software-engineering
- core
- error-handling
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- validation
- error_handling
- architecture
- input_handling
cross_links:
- rel: related_to
  target_object_id: PAT_settle_one_error_handling_strategy_systemwide
- rel: related_to
  target_object_id: PAT_enforce_contracts_at_runtime_with_checks
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Draw a Line Where Data Becomes Trusted

## Pattern Rule
**IF** you are deciding which parts of a system must validate their inputs
**THEN** name a boundary, put validation on it, and let everything inside assume clean data — rather than leaving every routine to guess whether its caller already checked.
**ELSE** where data crosses several trust levels, sterilize at each one; one boundary is the common case, not the only one.

## Do
- Say explicitly which code is outside the boundary, which is on it, and which is inside. That placement is an architecture-level decision, not something each author should settle privately.
- Validate everything arriving from outside: files, users, the network, and any other external interface. Check numeric values against tolerances, check string lengths, and reject strings that fall outside the range their purpose allows.
- Treat routine parameters as external data when the routine sits outside the boundary. The only difference from a file or a socket is where the bad value came from.
- Run the same pattern at class scale when it helps. Public methods assume their arguments are hostile and sanitize them; private methods, reached only through that surface, may assume the data is clean.
- Convert input to its proper type at the moment it arrives. A value that stays a string longer than necessary is a value someone can crash the program with by typing a colour named `Yes`.
- Be specific about hostile input where it applies: attempted buffer overflows, injected SQL, injected HTML or XML, integer overflows, and data forwarded into system calls.
- Draw the same line for representation, not only for trust. Where the outside world supplies a value in several forms — character encodings, units, time zones, numeric formats — pick one internal format, hold every value in the program in it, and convert as close to the input and output operations as you can get. Settle it early: validation can be added later to a boundary that already exists, but a representation policy cannot, because once the interior holds a mixture there is no single place left to convert at.

## Don't
- Don't accept "garbage in, garbage out" as the contract. Production software should do garbage in, *nothing* out, or an error message out, or refuse the garbage at the door.
- Don't leave the boundary implicit. When nobody has said where it is, every routine either checks everything — which is slow, fat, and itself a source of defects — or checks nothing, and both failures look identical from inside a single function.
- Don't put validation in the same place twice because you are unsure. Duplicate checking is the symptom of an undeclared boundary, not a safety margin.
- Don't rely on the barricade alone. It contains damage; it does not prevent defects, and iterative design, pseudocode before code, tests before code, and low-level design inspections all rank ahead of it for not inserting the error in the first place.

## Checklist
- Can you point at the classes that make up the boundary?
- For the routine you are writing: inside, outside, or on it?
- Does anything inside the boundary still validate, and if so, why?
- Is input converted to its real type at arrival, or carried as a string?
- Where data crosses more than one trust level, is there a boundary at each?

## Notes
The value of naming the boundary is that it converts a question every routine faces into a question the architecture answers once. Without it, "has this already been checked?" has no reliable answer, so the codebase drifts toward one of two failures — validation everywhere, which is expensive and adds defect-prone code of its own, or validation nowhere, because each author assumed someone upstream had done it.

The image McConnell uses is worth keeping because it carries the consequence: compartments in a ship's hull. Hitting an iceberg opens one compartment, and the rest of the ship is unaffected. The operating-room version is the same idea from the other side — data is sterilized before it enters, everything inside is assumed safe, and the design decisions are what to admit, what to keep out, and where to put the doors.

The most useful consequence is that the boundary makes a second decision mechanical. Code outside it must use error handling, because no assumption about the data is safe. Code inside it should use assertions, because the data was supposed to have been sanitized on the way in — so a bad value detected there is a defect in the program rather than a defect in the data. That classification is otherwise a judgment call made per-check; with a boundary in place it follows from where the code sits.

The same architecture carries a second property. Where the line above separates unchecked data from trusted data, it can equally separate the outside world's many representations of a value from the one representation the interior speaks. Character encoding is the worked case — a single alphabetic language can sit on an extended-ASCII standard, while anything needing multiple languages or an ideographic script needs the fuller international one — and the shape covers units, time zones, and numeric formats identically. Both decisions want the same boundary, because the place where a value is checked is the natural place to convert it, and one crossing that does both is easier to reason about than two that do one each. Two limits are worth stating. This is not licence to convert eagerly wherever two formats meet, which is how a program ends up converting the same value repeatedly; the instruction is one format inside and conversion at the edges. And it does not settle *which* format the interior should use — that is a domain question about what has to be represented, and all this requires is that a choice be made and held.

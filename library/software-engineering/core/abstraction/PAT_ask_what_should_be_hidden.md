---
object_id: PAT_ask_what_should_be_hidden
object_type: pattern
name: Ask What This Should Hide, Not What It Should Expose
library_path:
- software-engineering
- core
- abstraction
stage_binding: 0 design
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- information_hiding
- abstraction
- design
- encapsulation
cross_links:
- rel: related_to
  target_object_id: PAT_expose_clean_api_hide_implementation
- rel: related_to
  target_object_id: PAT_separate_essential_from_accidental_complexity
reference:
  source_id: code_complete_2e
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
  publish_date: 2004
  media_type: PDF
  locator: u05, pp. 92-97, 124
  evidence_type: text
confidence: high
references: []
variants: []
---

# Ask What This Should Hide, Not What It Should Expose

## Pattern Rule
**IF** you are deciding the shape of a class, routine, module, or type and are unsure which way to go
**THEN** ask what design decision this thing should keep secret from the rest of the program, and let the answer drive the shape — the question generates alternatives that asking "what should this expose?" does not.

## Do
- Name the secret explicitly. It is usually one of: an area likely to change, the format of a file, the way a data type is implemented, or an area walled off so its errors cause as little damage as possible.
- Run the question at every level, not just at class boundaries. It argues for a named constant over a literal, for a declared type over a raw one, for good parameter names inside a class, and for how subsystems are decomposed and interconnected.
- Hide the type as well as the mechanism. Replacing `id = ++g_maxId` scattered through a program with `id = NewId()` hides how IDs are made — but leaving `int id` declarations everywhere still exposes that IDs are integers, which invites callers to compare and increment them, so changing to a string ID still means hundreds of edits. A type alias or a small ID type hides the second secret.
- Apply the interface test directly: if a function or datum can go into the public interface without compromising the secret, put it there; otherwise keep it out.
- Treat a stubborn interface as a signal. Designing an interface is iterative, and if it will not stabilise after a few attempts, the approach is wrong rather than the attempt.

## Don't
- Don't let object-thinking substitute for this question. Asking "should an ID be its own object?" invites a cost calculation — constructor, destructor, copy and assignment operators, comments, configuration control — and most people answer "no, I'll just use ints," never considering the cheap alternative of hiding the type behind a declaration. The two questions approve of the same answer; only one of them generates it.
- Don't scatter a decision across the program and call it simple. A literal repeated everywhere, user interaction interleaved throughout, or a global array touched directly all publish an implementation detail to code that should not know it.
- Don't accept a performance objection to hiding without measurement. Architecting for information hiding does not conflict with architecting for performance, and at code level the worry about indirection is premature — a highly modular design is what lets you optimise the hot spots later without disturbing the rest.
- Don't build circular dependencies between the things you are hiding. When a routine in A calls B and B calls back into A, neither can be tested until part of the other exists.

## Checklist
- What is the secret here, stated in one sentence?
- If that decision changed, how far would the edit spread?
- Are you exposing a type as well as a mechanism?
- Is anything public that could be private without breaking a caller?
- Did you consider a cheap hiding option, or only the expensive one?

## Notes
The claim that makes this more than a restatement of encapsulation is that the question has *generative* power — it inspires design solutions that other framings do not surface. The ID example is the demonstration, and it is worth remembering precisely because the object-oriented framing and the hiding framing would approve of the same design; the difference is that only one of them produces it as a candidate. Information hiding is one of the few theoretical techniques whose value has been demonstrated in practice, with large programs that use it found substantially easier to modify.

Secrets fall into two camps and it is worth knowing which one you are protecting. Hiding *complexity* keeps your brain free of something until you specifically need it — complicated data types, file structures, involved algorithms. Hiding *sources of change* localises the damage when change arrives. The two often coincide but not always, and the second is the one that pays over a system's life.

Most barriers to doing this are mental rather than real. Genuine impossibility is rare; what is common is habit — the literal repeated because it was quicker, the global accessed directly because it was there, the class interface designed for the convenience of its first caller rather than for what it must not reveal.

---
object_id: PAT_know_why_it_works_before_you_move_on
object_type: pattern
name: Know Why It Works Before You Build on It
library_path:
- software-engineering
- core
- working-practice
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- assumptions
- deliberate_practice
- undocumented_behaviour
- generated_code
cross_links:
- rel: related_to
  target_object_id: PAT_beware_assumptions_avoid_or_enforce
- rel: related_to
  target_object_id: PAT_verify_code_assumptions_with_tests_and_pairing
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Know Why It Works Before You Build on It

## Pattern Rule
**IF** a piece of code you have just written, assembled, or generated now behaves correctly
**THEN** establish why it behaves correctly before building anything on top of it, treating "it works and I do not know why" as a defect you have not located rather than as a result.

## Do
- Separate what is guaranteed from what merely happens to be true. Rely on documented behaviour; where the documentation says nothing about a boundary case or an error condition, you are depending on how that code is written today, and a later release can change it without breaking any promise it made.
- Take out the calls you added while flailing. Piling on invalidate, validate, revalidate and repaint until something finally appears leaves a sequence nobody designed, and "it works now, better leave well enough alone" keeps it there permanently — at the cost of the time the extra calls take and the faults each one can introduce on its own.
- Name what the code assumes about its surroundings, not only about its inputs. A utility written inside a graphical application may quietly require a display to exist; it may also assume its users read English, or read at all. None of that is guaranteed by anything, and none of it appears in a parameter list.
- When you genuinely cannot tell whether a behaviour is guaranteed, assume it is not, and write down the assumption you are proceeding on so the next person meets it as a statement rather than as a surprise.
- Put the effort into the parts that are fundamental and hard. Refinements layered over infrastructure nobody understands are worth nothing when the infrastructure turns out to be wrong.

## Don't
- Don't accept "why take the risk of changing something that works" as the end of the discussion. It may not actually be working, only appearing to; the boundary condition it rests on may behave differently at another screen size, in another locale, or on another machine; and the undocumented behaviour it leans on can change with the next version of the library.
- Don't extend the usual exemption to generated code. Depending on a compiler, a process scheduler, or a library you could not have written yourself is reasonable, because each sits behind an interface you can hold it to. Code a generator emits into your project is not behind an interface — it is interwoven line by line with what you write, it becomes yours to maintain and debug, and producing a great deal of it quickly feels like progress right up to the first time it needs changing.
- Don't solve a problem by finding similar code and editing it into shape. Correctly modifying a program you do not fully understand is unreliable work, and the test is sharper than it sounds — not whether you did write it, but whether you *could* have. The cost also compounds: every solution you complete yourself joins the stock of worked problems you will recognise a future problem as resembling, so leaning on code you cannot account for makes you likelier to have to lean on it again.
- Don't keep building on a result you cannot explain. Every layer added on an unexplained foundation puts more distance between the eventual failure and its cause, which is why this fails weeks later as a mystery rather than immediately as a mistake.

## Checklist
- Can you say why this works, in one sentence, without the word "somehow"?
- Which behaviours here are documented promises, and which are just what it does today?
- Is every call in this sequence doing something you can name?
- What does this need from its environment that nothing actually guarantees?
- If a generator produced this, could you have produced it yourself?

## Notes
The failure this prevents has a delay built into it, and the delay is what makes it expensive. Code accumulates for weeks, each piece apparently working, and then something stops working for reasons that cannot be found — because the person who wrote it never knew why any of it worked in the first place. There is nothing to reason back from. The cost is not the original mistake; it is that the mistake was never observable at the point it was made, and by the time it surfaces, weeks of other work are resting on it.

The two shapes worth recognising separately are accidents of implementation and accidents of context. An accident of implementation is depending on how something is currently built: an error path the author never designed, a boundary the documentation does not mention, a call order that happens not to matter yet. An accident of context is depending on the world the code was first written in: that a display exists, that a filesystem is writable from wherever this runs, that only one thread will ever be inside it. The first breaks when someone else changes their code correctly. The second breaks when your code is reused correctly.

The counterargument is worth answering directly, because it sounds strong: developers rely on things they do not understand all the time, and always have. That is true and it is fine, and the reason it is fine is that those things are reached through an interface — you depend on what it promises, not on how it does it, and when it changes underneath you the promise still holds. What breaks the analogy is code that lands *inside* your program. There is no interface, no promise, and no one else maintaining it. Whatever produced it has moved on, and it is now indistinguishable from code you wrote, which is exactly the standard it now has to meet.

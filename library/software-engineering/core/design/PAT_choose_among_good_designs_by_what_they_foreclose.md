---
object_id: PAT_choose_among_good_designs_by_what_they_foreclose
object_type: pattern
name: Choose Among Good Designs by What They Foreclose
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
- performance
- architecture
- trade_offs
- premature_optimization
cross_links:
- rel: related_to
  target_object_id: PAT_name_the_performance_metric_before_you_optimize
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_produce_a_second_design_before_committing
- rel: related_to
  target_object_id: PAT_settle_load_bearing_decisions_before_finishes
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Choose Among Good Designs by What They Foreclose

## Pattern Rule
**IF** you are choosing a design for something whose performance will matter, and cannot yet measure anything
**THEN** do not try to pick the optimizations — screen the candidate designs for the ones that would make later optimization hard or impossible, and choose among the good designs accordingly
**ELSE** where the component's cost is bounded and small however the system grows, any of the good designs will do and this screening is wasted effort.

## Do
- Hold the two claims together, because each alone is wrong. Predicting which optimization will pay is nearly impossible before there is code to measure. Recognizing that a decision removes the *option* of optimizing later is quite possible, and it is a different activity.
- Answer "this design performs badly" with a different good design, not a worse one. It is common for a particular good design to perform poorly in a particular system; it is very unlikely that every good design for that system does. The work is choosing among them, not abandoning the category.
- Ask what each candidate permits rather than what it costs. A design cannot be optimized — only an implementation can. What a design does is allow or prevent efficient implementations, which is why the useful vocabulary is performance-friendly and performance-hostile rather than fast and slow.
- Trace how a decision propagates before accepting it. Exposing a collection's elements as directly addressable objects rules out ever storing them compressed, or in a different layout, or behind a proxy — not because that is slow today, but because every client will then hold references that a change would break.
- Weight the decision by how hard it is to revisit. A class used in two places can be changed with its callers. A protocol that becomes the system's standard, a data layout every component reads, a low-level interface everything is built on — those are the ones to screen carefully, because their architecture is more fundamental than any algorithm choice above them.
- Separate premature optimization from premature pessimization, and apply the test to each candidate change. Does it make the code harder to read, more complex, or harder to test? If yes, it needs a measurement to justify it. If no, and it is also faster, then declining it is not restraint — it is choosing the slower of two equally good options for no reason.

## Don't
- Don't leave performance out of the design goals on the grounds that it cannot be measured yet. It is a requirement like any other, and the reason it gets treated differently is habit: we are practised at evaluating designs by what they do and not by how fast they do it.
- Don't use "we don't guess about performance" as a licence to skip this. That rule governs tuning existing code. Applied at design time it produces exactly the decisions that make tuning impossible later.
- Don't build a back door when a good design turns out to constrain performance. An escape hatch added to work around your own interface compromises both goals at once; the honest move is to redesign the components, or to erase the boundary and make the pieces internal.
- Don't expect a rewrite to be available. Inefficiency embedded in the core architecture is rarely reachable by optimization, and systems live long enough that the people paying for the decision are usually not the ones who made it.

## Checklist
- For each candidate design: if this turns out to be the hot path, what would have to be rewritten?
- Which decisions here will be depended on by code that does not exist yet?
- Is a performance target written into the requirements alongside the functional ones?
- Where you rejected a change as premature, does it actually cost clarity — or only effort?
- Is there a second good design that does not foreclose what this one forecloses?

## Notes
The claim that design determines performance is often stated too strongly and then dismissed. The accurate version is narrower and more useful: designing for performance does not produce a fast program, it preserves the possibility of one. What the opposite produces is not merely a slow program but a program whose slowness is out of reach — the constraints live in the architecture, and the code-level work that would fix them has nowhere to stand.

Two camps overstate opposite halves of this and both have a point. The claim that a good design never costs performance is false for particular systems, and pretending otherwise leaves people unprepared for a real and expensive trap. The claim that performance therefore justifies abandoning design practice is a false choice, because the alternative to one good design is another good design rather than no design.

The asymmetry that makes this tractable is worth stating plainly, because it tells you where to spend the attention. Decisions that expose something are hard to reverse — clients come to depend on what they can see. Decisions that withhold something are easy to reverse — you can always add an interface later, and nothing breaks. So when uncertain, the direction that keeps options open is to promise less.

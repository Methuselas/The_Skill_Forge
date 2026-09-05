---
object_id: PAT_count_the_dependency_chain_not_the_operations
object_type: pattern
name: Count the Dependency Chain, Not the Operations
library_path:
- software-engineering
- core
- performance
stage_binding: 4 final
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- optimization
- hardware
- loops
- tuning
cross_links:
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
- rel: related_to
  target_object_id: PAT_ask_whether_the_hot_code_can_run_less_often
- rel: related_to
  target_object_id: PAT_keep_one_job_per_loop
- rel: prerequisite_for
  target_object_id: PAT_trade_a_branch_for_unconditional_work
reference:
  source_title: 'The Art of Writing Efficient Programs: An Advanced Programmer''s Guide to Efficient Hardware Utilization'
  author: Fedor G. Pikus
confidence: high
references: []
variants: []
---

# Count the Dependency Chain, Not the Operations

## Pattern Rule
**IF** you are judging what a hot loop or expression costs, or deciding whether to remove arithmetic from it
**THEN** ask what each step has to wait for before it can start, and treat the waiting as the cost rather than the number of operations
**ELSE** where the operation itself is one of the genuinely expensive ones — integer division, transcendental functions — the operation count is the cost and removing one is worth something.

## Do
- Add computations freely to values already sitting in registers. A loop body doing one addition, and the same body doing an addition, a multiplication, a shift and a subtraction on the same two loaded values, measured at the same time per iteration: the extra work executed in parallel on execution units that were otherwise idle. The limit is real but far away — roughly five to seven operations before that machine slowed down at all.
- Read a chain of dependent steps as the thing to attack. An expression whose second half needs the first half's result cannot collapse into one step no matter how many execution units are free; that is the shape that costs, and shortening the chain is what helps.
- Distinguish a dependency inside one iteration from one that crosses iterations. Two-stage work per iteration — add and subtract, then multiply the results — ran as fast as a single multiplication, because the hardware overlaps the second stage of one iteration with the first stage of the next. A value each iteration must have from the previous one is the dependency that actually blocks.
- Confirm the direct evidence when the timings surprise you. A machine code analyzer showing the timeline of instructions through the execution units will say plainly whether two iterations overlapped, which no amount of reading the source will.
- Look at loads before arithmetic. Getting the operands out of memory and into registers is a separate step from computing on them, and it is normally the step that decides how fast the loop can go.

## Don't
- Don't remove arithmetic from a hot loop as a first move. The instruction count is rarely the binding constraint, and the transformation costs clarity for a resource that was not scarce.
- Don't assume unused capacity means the code is fine. A single multiplication per iteration was using well under a quarter of that processor's integer capability, and a program leaving that much idle has room that only becomes visible once you look for parallel work rather than fewer operations.
- Don't reason about instruction cost from the source alone. The compiler is choosing the instructions and the hardware is choosing when to run them; the source shows neither.
- Don't extrapolate a limit you measured on one machine. How many operations issue together depends on the processor's execution units, and separate integer, floating-point, and vector hardware means the budget differs by the kind of work as well as by the chip.

## Checklist
- For each step in the hot loop, what must be finished before it can start?
- Is there a value that every iteration takes from the previous one?
- Are the operands already in registers, or is this loop actually paying for loads?
- Before removing an operation, what evidence says operation count is the constraint here?
- Does the timeline from an analyzer, or the measurement, agree that iterations are overlapping?

## Notes
The hardware behind this is worth carrying as a mental model even though none of it is under your control. A processor issues several independent operations per cycle, overlaps successive iterations so that later stages of one run beside earlier stages of the next, renames registers internally so that reusing the same register name across iterations does not serialize them, and executes out of program order. The net effect is that a modern CPU is looking for independent work to do, and the programmer's job is supplying it rather than economizing on it.

Which is why the useful question about a slow loop is where the waiting is rather than where the arithmetic is. Left to itself, the hardware fills the gaps; what it cannot do is compute something whose inputs do not exist yet.

This sits alongside, and does not overturn, the reasons for keeping separate jobs in separate loops. That decision is made on clarity with a measurement as the escape hatch. What this adds is that the extra pass costs the loads again, while extra work on values already loaded is close to free — so when a measurement does open the question, the cheap direction is usually combining work on data already in hand rather than shaving operations.

The out-of-order execution mentioned above has a consequence beyond this card's scope: when several threads are involved, the order in which one thread's writes become visible to another is not the order they appear in the source.

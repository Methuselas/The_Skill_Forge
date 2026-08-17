---
object_id: PAT_estimate_the_order_before_you_run_it
object_type: pattern
name: Estimate How the Cost Grows Before You Run It
library_path:
- software-engineering
- core
- performance
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- performance
- algorithms
- complexity
- estimation
cross_links:
- rel: related_to
  target_object_id: PAT_choose_the_level_before_tuning_the_code
- rel: related_to
  target_object_id: PAT_let_measurement_decide_what_to_tune
reference:
  source_title: The Pragmatic Programmer
  author: Andrew Hunt & David Thomas
confidence: high
references: []
variants: []
---

# Estimate How the Cost Grows Before You Run It

## Pattern Rule
**IF** you are writing or choosing code whose input size is not fixed — a loop, a recursion, or an algorithm handed a collection from outside
**THEN** work out from the shape of the code how its time and memory grow as that input grows, before running it, and then confirm the estimate by running it at several sizes and looking at the curve.

## Do
- Read the growth off the structure. A loop running once per item grows linearly. A loop nested inside another grows as the product of the two limits, which for two passes over the same collection is the square. Halving the candidates each time around is logarithmic. Partitioning the input, working the halves independently, and combining the results lands between linear and square. Anything that enumerates permutations grows factorially — time it for five items and six will take six times as long, seven forty-two times as long.
- Ask what bounds the input. Where the count is bounded you already know the runtime; where it comes from outside — records in an overnight batch, names in a list of people — that is where a value nobody anticipated changes the answer.
- Check the estimate rather than trusting it. Run the code across a range of input sizes and plot the results; three or four points are enough to show whether the curve bends upward, runs straight, or flattens. Where accurate timings are hard to get, profile how many times each step executes and plot that against input size instead.
- Model memory with the same reasoning, since the growth question applies to any resource. A recursion that holds a sizeable local buffer at every level is the case where memory growth matters more than time growth, and it is invisible if you only ever look at the loop structure.
- Where a square-law step sits on the critical path, look for a restatement that splits the input and recombines the halves, which is the standard route down to something close to linear.

## Don't
- Don't read the notation as a ranking of implementations. It deliberately discards constant factors and low-order terms, so one square-law routine can be a thousand times faster than another with the identical classification, and nothing in the notation says so.
- Don't assume the better growth rate is the better choice. On a small input a straightforward insertion sort matches a quicksort and costs far less to write and debug, a sophisticated algorithm with an expensive inner loop loses to a naive one, and an algorithm with a high setup cost can be dwarfed by its own setup before it processes anything.
- Don't trust a curve measured only on small inputs. Runtime can look convincingly linear right until the working set stops fitting in memory, at which point the system starts swapping and the times degrade sharply — and nothing about the code predicted the cliff.
- Don't measure with random data alone. A sort fed random keys can behave completely differently the first time it meets input that is already ordered, which is precisely where the average-case guarantee of a partitioning sort stops applying.

## Checklist
- What is the varying quantity here, and what sets its upper bound?
- Does the loop and recursion structure give a growth rate you can name out loud?
- Have you run it at three or four sizes and looked at the shape of the plot?
- Would constant factors or setup cost reverse the ranking at the sizes you actually see?
- Does the test data include the ordered and degenerate cases, or only random ones?

## Notes
This is a daily estimate rather than a formal analysis. Most of the time the check is subconscious — you write a loop, you notice it runs once per item, you satisfy yourself that is sensible here — and the notation only comes out when the answer is not obvious. Treating it as a piece of computer science reserved for people who write sort routines is what causes it to be skipped, because almost nobody writes sort routines and the library version will beat anything you produce without serious effort. The shapes still turn up constantly in ordinary code, which is where the estimate pays.

The difference between a linear and a square-law routine is invisible at the size you develop against and decisive at the size you deploy against. An algorithm that takes a minute on ten items can take a lifetime on a hundred, and the code looks the same either way. That asymmetry is the whole argument for doing the estimate up front: it is nearly free, and the alternative is finding out from a production dataset.

The estimate and the measurement do different jobs and neither replaces the other. The estimate tells you the shape of the curve, which is what lets you answer "it handles a thousand records, what about a million" without having a million records. The measurement tells you the constants, the setup costs, and the point where the machine's own limits take over — none of which the analysis knows about. The honest summary is that the only timing that finally counts is the code running in production against real data, and the estimate is what stops you from discovering that too late to change the design.

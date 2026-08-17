---
object_id: AP_choose_test_cases_systematically
object_type: ap
name: Choose Test Cases Systematically
library_path:
- software-engineering
- core
- testing
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- test_design
- coverage
- boundary_analysis
- defect_detection
cross_links:
- rel: related_to
  target_object_id: PAT_count_a_routines_decision_points
- rel: related_to
  target_object_id: PAT_combine_detection_techniques_rather_than_perfecting_one
- rel: related_to
  target_object_id: AP_write_a_unit_test_suite
- rel: related_to
  target_object_id: PAT_bound_an_arithmetic_expression_before_trusting_it
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Choose Test Cases Systematically

## Objective

Build a set of test cases for a routine by working through named techniques in an order where each one adds cases the previous ones could not produce — rather than writing tests until you feel finished, which reliably stops at about half the code while feeling like ninety-five percent of it.

Exhaustive testing is not available and never was. A trivial routine taking a twenty-character name, a twenty-character address, and a ten-digit phone number has around ten-to-the-sixty-six possible inputs, so the entire craft is choosing the few cases that tell you different things.

## Steps / Flow

1. **Write cases from the requirements and the design first, before the code exists.** One case per relevant requirement and per relevant design concern, planned at those stages rather than after. The earlier detection is the obvious benefit; the better one is that it is hard to write a test case against a poor requirement, so the attempt exposes bad requirements while they are still cheap to fix.

2. **Compute the minimum case count from the decision points.** Start at one for the straight path through the routine and add one for each `if`, `while`, `for`, `and`, and `or`. This is the same count that measures a routine's complexity, used here as a floor instead of a warning. Then make sure each of those keywords gets at least one case that makes it true and one that makes it false — the number tells you how many cases are needed and nothing about which ones, and any six arbitrary cases will not cover a routine that needs six.

3. **Check the variables for state sequences that are wrong on sight.** Every variable moves through being defined, used, and killed. A variable defined twice before use, defined and then killed without use, defined and then exited, killed twice, or used after being killed is suspect before any test runs — finding these by reading is cheaper than testing for their consequences.

4. **Add the defined-used pairs that step 2 missed.** Exercising every line guarantees only that every definition was reached, not that every definition was reached by every use. Where two conditions each select a value, the cases that set both the same way fall out of basis testing free and the cross combinations do not, so those are the ones to add.

5. **Add three cases at every boundary.** Just below, exactly on, and just above. Boundaries are where off-by-one errors live, and the exactly-on case is specifically the one that basis testing does not generate for you.

6. **Add compound boundary cases where values interact.** Two large numbers multiplied together, two large negatives, both at zero, every string at maximum length, or a large collection in which every member also carries a large value. These are the boundaries nobody writes down because they belong to no single variable.

7. **Work through the classes of bad data.** Too little or none at all, too much, the wrong kind, the wrong size, and uninitialized. Some will already be covered; the value is in the list being fixed so you do not have to think of the categories under pressure.

8. **Work through the classes of good data, which is the step people skip.** The nominal case, the minimum normal configuration, the maximum normal configuration, and compatibility with data from the previous version. It is easy to forget that the ordinary path can be wrong too.

9. **Add cases from your own error history.** Guessing where the errors are is respectable when the guesses come from a record of what this team actually gets wrong, which is the same record a review checklist is built from.

10. **Generate rather than enumerate where the input space is large.** A random-data generator produces combinations you would not think of and exercises the code far more thoroughly than you can by hand. Weight its distribution toward realistic sizes rather than spreading it uniformly across the legal range, so that the effort concentrates where users will actually be.

11. **Pick values that make hand-checking easy.** A salary of twenty thousand is exactly as likely to reveal an error as an arbitrary ugly number drawn from the same equivalence class, and it does not make your hand calculation as error-prone as the code you are checking it against.

12. **Work through what the code will run out of, not just what it is passed.** Memory and disk space are the two everybody checks; the ones that go untested are CPU and disk and network bandwidth, wall-clock time, screen resolution, and colour depth. Ask whether the batch job finishes before the archive starts, and whether the interface survives both the smallest and the largest display it will meet. Some of these can be detected and adapted to; some cannot be recovered from at all, and for those the case to test is whether the failure is graceful — state saved, work preserved — or a crash in the user's face.

13. **Measure the coverage instead of estimating it.** Programmers put their own coverage at about ninety-five percent and typically achieve fifty to sixty. Aim past statement coverage at branch coverage, with every predicate term exercised both ways, and let a tool tell you rather than your impression.

14. **Read the coverage figure as a floor and never as a score.** What matters is the number of states the program can be in, and states are not lines. A three-line function taking two integers from zero to nine hundred and ninety-nine has a million logical states, of which exactly one — the pair that sums to zero before a division — is fatal; a tool reporting that the line executed says nothing whatever about that. Full branch coverage with data that never approaches the fatal combination is a complete pass over a program you have not tested, and the order in which the code is traversed can matter more than either figure.

## Notes

The order matters because each technique is defined by what the previous ones leave out. Basis testing guarantees every line runs and says nothing about data. Data-flow testing covers the definition-to-use paths that line coverage misses. Boundary analysis covers the specific values that both of those step over. The bad-data and good-data classes cover the shapes of input that no amount of path reasoning suggests. Running them in this order means each pass is short, because most of what it would generate is already present.

The most useful number in this area is about what gets tested rather than how. Immature testing groups write roughly five clean tests — does it work — for every dirty one that tries to break the code, and mature groups run five dirty for every clean. The reversal is not achieved by writing fewer clean tests; it comes from writing something like twenty-five times as many dirty ones. Most of the steps above exist to generate dirty cases, which is why working through them feels unnatural compared with confirming the code does what it was written to do.

The last step is where the whole procedure is most often misread, because a coverage tool produces the only number in the process and numbers attract confidence. Coverage answers one narrow question — was this line or branch ever reached — and the thing you actually want to know is which of the program's states have been visited. Those diverge fast: a handful of integer parameters puts the state count into the millions while the line count stays in single figures, and the states that break are frequently a specific combination rather than a specific path. This is why the earlier steps are ordered the way they are. Boundary cases, compound boundaries, and the bad-data classes are all attempts to reach dangerous *states*, and the coverage measurement at the end is there to catch code the attempt never reached at all — not to certify the ones it did.

Step 2 is worth connecting to its other use deliberately. The identical count that flags a routine as too complex also sets the floor on how many cases it needs, which means a routine scoring above ten is simultaneously telling you to simplify it and telling you that testing it properly costs at least eleven cases. Those two readings reinforce each other, and a routine that is expensive on both counts is the clearest possible candidate for being broken up before it is tested.

---
object_id: PAT_reduce_the_problem_until_you_can_already_solve_it
object_type: pattern
name: Reduce the Problem Until You Can Already Solve It
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- problem_solving
- decomposition
- constraints
- getting_unstuck
cross_links:
- rel: related_to
  target_object_id: PAT_find_the_real_constraints_before_calling_it_impossible
- rel: related_to
  target_object_id: PAT_use_domain_specific_cues_not_generic_problem_frames
reference:
  source_title: 'Think Like a Programmer: An Introduction to Creative Problem Solving'
  author: V. Anton Spraul
confidence: high
references: []
variants: []
---

# Reduce the Problem Until You Can Already Solve It

## Pattern Rule
**IF** you cannot see a route to a solution and are about to attack the full problem anyway
**THEN** change its terms on purpose — drop a dimension, fix a quantity, delete a requirement — until you reach a version you already know how to write, build that, and read what is missing as an exact statement of the difficulty that remains.

## Do
- Suspend a constraint you know is real, which is what separates this from wishful thinking. Finding the closest pair among points in three dimensions gets tractable if you first solve it in two dimensions, or along a single line where the coordinates are just numbers, or for exactly three points rather than an arbitrary series.
- Choose the reduction by what it isolates. Collapsing to one dimension removes the distance computation and leaves the search; fixing the count at three removes the search and leaves the distance computation. Two reductions of one problem hand back two different residues, and a hard problem usually needs you to have solved both.
- Work outward from what you can already write rather than inward from the full statement. Code the pieces you know how to code first; a running partial solution regularly suggests the rest, and it costs nothing you were not going to spend.
- Read the residue as a precise request. "Here is code that computes the distance between two points and compares two distances, and I cannot find a general way to get the minimum-distance pair" is a question someone can answer in a sentence. "Here is my program, it doesn't work, why not?" is not, and it is what being stuck sounds like when the reduction has not been done.
- Put the constraint back. A reduced solution is a stepping stone and its value is what it taught you; the requirement you suspended still has to be met before the work is finished.

## Don't
- Don't confuse this with checking whether a constraint is genuine. That question asks whether a limit exists at all and removes the ones that turn out to be imaginary. This one takes a limit that is unquestionably real and suspends it anyway, on purpose and temporarily, to get moving.
- Don't reduce so far that the small version shares nothing with the original. It has to keep enough of the structure that solving it transfers something back, or you have simply written a different program.
- Don't let the reduced version ship. It solves a problem nobody asked about, and the gap between it and the real requirement is invisible to everyone who did not watch you make it.

## Checklist
- What is the simplest version of this that you could sit down and write right now?
- Which specific difficulty does that version remove, and which does it leave behind?
- Is there a second reduction that removes the difficulty this one left?
- Can you state what remains as a question another person could answer?
- Has every suspended constraint been restored?

## Notes
The move has two payoffs and the second one is the one people miss. The first is momentum: a solvable version exists, you can write it today, and a partial result is worth more than an afternoon of staring at the full problem. The second is diagnostic — after the reduction, the difference between what you built and what was asked is precisely the thing you do not know how to do. That difference is usually much smaller and much more specific than "this problem is hard," and it is the form in which a difficulty can actually be looked up, asked about, or recognised as something you have solved before in another guise.

The pairing with constraint auditing is worth keeping straight because the two look similar and pull in opposite directions. Auditing asks which of the limits around you were ever imposed, and its result is that some of them evaporate. Reduction assumes the limits are all real and deliberately breaks one anyway, knowing it will have to be restored. Running the audit first is usually right — there is no sense reducing away a constraint that was never there — but the two are separate operations and a problem can need both.

The failure this guards against has a recognisable shape from outside: someone who cannot describe what help they need. Being unable to say more than "it doesn't work" is not a communication problem, it is evidence that the problem has never been decomposed at all, because anyone who had built a reduced version would be able to name the piece that defeated them. That makes the ability to state the residue a decent test of whether the reduction was done properly.

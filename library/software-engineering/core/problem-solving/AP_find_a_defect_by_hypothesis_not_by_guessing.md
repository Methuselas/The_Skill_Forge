---
object_id: AP_find_a_defect_by_hypothesis_not_by_guessing
object_type: ap
name: Find a Defect by Hypothesis, Not by Guessing
library_path:
- software-engineering
- core
- problem-solving
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- debugging
- diagnosis
- hypothesis
- defects
cross_links:
- rel: related_to
  target_object_id: AP_build_a_mental_model_of_unfamiliar_code
- rel: related_to
  target_object_id: PAT_fix_the_cause_not_the_symptom
- rel: related_to
  target_object_id: PAT_time_box_the_guess_and_name_the_fallback
- rel: related_to
  target_object_id: PAT_externalize_intermediate_state_when_tracing
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Find a Defect by Hypothesis, Not by Guessing

## Objective

Locate the cause of a defect by running the scientific method over it — stabilize, hypothesize, design a test that could disprove the hypothesis, and act on the result — rather than changing things until the symptom disappears. Finding and understanding the defect is roughly ninety percent of the work; the correction is usually small.

The alternative is not a slower method, it is a different activity. Adjusting code until the symptom goes away terminates whether or not anyone understands what happened, which is how a correction gets made that leaves the defect in place.

## Steps / Flow

1. **Get the reproduction from the reporter, not from the report.** Bug reports are a lossy channel and worse through a third party, so where the symptom will not reproduce, watch the person who saw it actually do it. A painting tool that crashed for the testers and never for its author differed only in the direction the stroke was drawn — the author had tried it one way, and no amount of argument across a ticket was going to surface that.

2. **Stabilize the error before trying to locate it.** A defect that does not occur reliably is nearly impossible to diagnose. If it is intermittent, the cause is usually one of three things — an uninitialized variable that mostly happens to start at zero, a timing issue, or a pointer used after the memory it referenced was released. *Shortcut:* where the program stops itself — a memory-access fault, an unhandled exception, an abort — reproduce it under a debugger and take the call chain before anything else. An involuntary stop hands you a location and the sequence of calls that reached it, which is most of steps 3 through 6 for free. A program that only hangs gives you the same thing on demand: let it reach the suspect state, interrupt it, and read the stack.

3. **Narrow the reproducing case until it is minimal.** Finding *a* test case that triggers the defect is not enough; simplify until changing any aspect of the case changes the behaviour. Do this by hypothesis too — guess which of the contributing factors are irrelevant, vary those, and rerun. Still failing means those factors are eliminated. No longer failing means you have disproved that guess and learned something narrower.

4. **Gather data, then form a hypothesis from it — plural.** Rather than pursuing the first explanation that occurs to you, list several without analyzing them, then work out what test would distinguish them. Concentrating on a single line of reasoning is the most common way to get stuck, and generating alternatives is what breaks the jam.

5. **Design each test so it can disprove, not merely confirm.** A test that fails to support your hypothesis is not a wasted cycle — it tells you the defect is not where you thought, which shrinks the remaining search space. Treat a negative result as information rather than as a setback.

6. **Narrow the region by bisection when reasoning stalls.** Remove or bypass roughly half the suspect code and see whether the symptom survives; that tells you which half holds it. Repeat. A debugger's breakpoints and step-over do the same job without editing anything. Bisect the call hierarchy the same way rather than descending into it: step *over* each call and check whether the values that depend on it are right, and only step into the one whose results are wrong. Stepping into a function that turns out to be correct is the most common way to spend an hour reading code that was never the problem. And bisect in time as well as in space — a value that has gone bad by the thousandth iteration can be checked at the five hundredth.

7. **Suspect your own code before the layers under it.** The operating system is probably not broken, the database is probably fine, and the library call probably works — it is far more likely that your code is calling into it wrongly. An engineer once spent weeks writing workarounds for a system call he was certain was broken, on a machine where every other application using it worked, and found his own error minutes after being made to read the documentation. Even when the fault does turn out to be a third party's, you have to eliminate your own code before the bug report is worth filing.

8. **Bias the search toward code that is new or has a history.** Recently changed code is the first place to look for a newly appeared defect — compare against a version that worked and read the difference. Code that has produced defects before is more likely than average to hold this one too.

9. **Widen the region when the narrow one is exhausted.** The confident feeling that the defect *must* be in this section is exactly what keeps a search inside a region that does not contain it. When bisection inside the region finds nothing, the region was wrong.

10. **Explain the problem out loud to someone.** Describing the symptom, what you have ruled out, and why, frequently produces the answer mid-sentence and before the listener has spoken. It costs one interruption of one colleague.

11. **Stop and step away when the anxiety starts.** Once you are no longer generating new hypotheses, more time at the screen produces guesses rather than diagnosis. The onset of frustration is a reliable signal that the productive phase has ended.

12. **Confirm the diagnosis before touching anything.** Run cases that should reproduce the error and cases that should not. You are done when you can predict the defect's occurrence correctly every time — not when you have one explanation that fits.

13. **Fix the cause, check the fix, and add a test that would have caught it.** The correction itself has its own discipline, since more than half of defect corrections are wrong on the first attempt.

14. **Look for the same defect elsewhere.** Defects arrive in groups, and the understanding you just paid for is at its most valuable now. If you cannot work out how to search for siblings, that is a warning that you do not yet understand the defect as well as you think.

## Notes

The reason this deserves a procedure is that debugging ability varies more than almost any other programming skill. In one study of professionals with at least four years of experience, the fastest three found the defects in about a third of the time the slowest three took, and — the more telling number — introduced about two-fifths as many new defects while correcting them. The best found all twelve defects and added none; the worst missed four and added eleven. That spread is not explained by knowledge of the language.

Step 2 is the one most often skipped, and it is where the leverage is. A reproducing case that still has ten contributing factors leaves ten hypotheses live. Stripping it to the point where any change alters the behaviour is what converts a vague symptom into a statement about the program, and it is done by the same hypothesize-and-test loop as the diagnosis itself — which is why the method appears twice, at two scales.

Surprise is a locating device and is usually wasted. The amount of surprise you feel at a defect is proportional to how much you trusted the code it turned out to be in — so the feeling of *that's impossible* is not an obstacle to reasoning, it is a pointer at the assumption you never examined. When it arrives, the useful question is which belief just failed, and the answer is nearly always whatever you were most certain of: the routine that has worked for years, the library everyone uses, the boundary case you are sure was tested. Prove it in this context, with this data.

The distinction that organizes everything here is between the *symptom* and the *fault*. The symptom is what you observed; the fault is the code that produced it, and in this class of work the two are often far apart. Every step above is a way of shortening the distance between them — stabilizing makes the symptom repeatable, bisection moves the boundary inward, negative results remove territory. Guessing skips the shortening and jumps to a change, which is why it terminates on a green result rather than on an understanding.

---
object_id: PAT_block_with_a_deadline_before_polling_on_an_interval
object_type: pattern
name: Block With a Deadline Before Polling on an Interval
library_path:
- software-engineering
- core
- concurrency
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
tags:
- concurrency
- latency
- waiting
- timeouts
- design
foundation_object_id: none
cross_links:
- rel: related_to
  target_object_id: PAT_match_the_problem_to_a_known_coordination_shape
- rel: related_to
  target_object_id: PAT_match_the_lock_to_the_length_of_the_critical_section
- rel: related_to
  target_object_id: PAT_wait_on_a_predicate_not_on_a_notification
reference:
  source_title: 'Concurrency with Modern C++: What every professional C++ programmer should know about concurrency'
  author: Rainer Grimm
confidence: high
references: []
variants: []
---

# Block With a Deadline Before Polling on an Interval

## Pattern Rule
**IF** a thread has nothing to do until something another thread produces becomes available, and you are choosing how it waits
**THEN** block on the thing itself with a deadline, so the waiter is woken when the result appears and burns nothing until then, and reach for repeated checking only where there is nothing to block on — accepting, when you do, that your checking interval is added to how late the result is noticed
**ELSE** where the waiter has useful work to do between checks, it is not waiting at all, and the question becomes how often to interrupt that work rather than how to sleep.

## Do
- Separate the two costs every waiting strategy has, because they trade against each other and only one of them is visible in a profile. One is what the waiter burns while nothing has happened; the other is how late it learns that something has. Blocking pays almost nothing on either. Repeated checking pays on both, and the interval is the single knob moving cost from one to the other.
- Set a deadline generous enough for the result to actually arrive, and treat it as protection against waiting forever rather than as an estimate of how long the work takes. Against a result published after five seconds, a waiter bounded at four seconds timed out and never saw it at all, while one bounded at twenty returned about three tenths of a millisecond after publication. A bound set as though it were a prediction converts a slow result into no result.
- Expect a fixed-interval checker to be late by up to one interval and on average by half of one. Checking every seven hundred milliseconds for that same five-second result returned it at about 5.6 seconds — correct, six tenths of a second behind the blocking waiter, and eight wakeups spent getting there.
- Know what growing the interval buys and what it charges. Doubling the wait after each failed check drives the number of wakeups down logarithmically, which is the whole point where a check is expensive, contended, or crosses a network. What it costs is worst-case lateness proportional to the total wait, because the interval you happen to be sleeping through at the end is as long as everything before it put together: the doubling checker found the same five-second result at about 8.2 seconds, more than three seconds late.
- Cap the growth and keep checking at the cap. That keeps almost all of the reduction in wakeups while bounding the overshoot to something you chose, and it is what most retry loops actually want rather than unbounded doubling.
- Time every deadline with a clock that cannot be adjusted. A clock the system may move — forward when it synchronizes, backward when it corrects — makes a deadline mean something different depending on what happened to the system time while you waited, and the failure appears only when the adjustment does.
- Check what the highest-resolution clock actually is on each target before timing anything with it. It is permitted to be an alias for another clock, and which one it aliases differs by platform: on one Linux build it followed the adjustable system-wide clock, and on one Windows build the steady one. Choosing it for its name can hand you an adjustable clock on half your targets.
- Say whether an interface takes a length of time or a point in time, and prefer the point when the wait may be retried. A wait expressed as a duration restarts its full interval on every retry, so a loop around a two-second wait can run far longer than two seconds; a deadline is unaffected by how many times it is re-entered.

## Don't
- Don't check repeatedly where you could block. Every cycle of a checking loop is a guess about when the result will arrive, and it is wrong in one of two directions each time — too early and it burns a wakeup for nothing, too late and the result sat ready while nobody looked.
- Don't shorten the interval to reduce lateness without pricing it. Halving it halves the average lateness and doubles the wakeups, forever, including the overwhelming majority that find nothing.
- Don't apply growing intervals to something that arrives once and arrives soon. Backoff is built for contention and for checks that cost something; against a single result a few seconds away it adds latency and saves almost nothing.
- Don't treat a timed wait that returned as proof the deadline expired. It can return for other reasons, so what the waiter does next depends on re-examining the thing it was waiting for rather than on which call returned.
- Don't leave the strategy unstated at the interface. Whether a caller will be woken promptly or discover the result on some future sweep is part of what the operation promises, and a caller cannot infer it from a signature that just says it waits.

## Checklist
- Is there something the waiter could block on directly, and if not, why not?
- Is the deadline set to bound waiting forever, or was it set from a guess at how long the work takes?
- What is the worst-case lateness of this strategy, and is that acceptable to whoever is waiting?
- If the interval grows, what caps it?
- How many wakeups does this cost over a typical wait, and how many of them find nothing?
- Is the clock behind this deadline one the system can adjust?

## Notes
The reason blocking wins so consistently is that it is the only one of these strategies that is not guessing. A waiter that has registered its interest is told the moment the result exists; every checking loop is instead sampling a state it cannot predict, and sampling has an irreducible cost in both directions. That is why the interesting question is rarely which interval to check at — it is whether there is anything to block on, and the answer is more often yes than the reach for a sleep-and-retry loop suggests.

Growing intervals deserve their reputation and also their limits. They exist because a check can be expensive — a query, a request across a network, a lock that other threads want — and reducing a linear number of those to a logarithmic one is a large win. What gets forgotten is that the saving comes entirely out of latency, and specifically out of the worst case: the longer you have already waited, the longer you will now go without looking. A strategy whose lateness grows with how long the thing took is a poor fit for anything a person is waiting on, which is why the capped form is usually the right one and the uncapped form is usually an oversight.

The clock question looks like a detail and behaves like a portability bug. Every deadline is a comparison against a clock, and a clock that can be adjusted turns a bounded wait into an unbounded one, or fires it immediately, depending on which way the adjustment went. The trap is that the clock advertising the best resolution is not required to be a distinct clock at all, so the choice that reads as the most careful one is the choice that varies most between platforms.

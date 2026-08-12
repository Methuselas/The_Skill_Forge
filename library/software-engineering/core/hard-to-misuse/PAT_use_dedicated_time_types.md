---
object_id: PAT_use_dedicated_time_types
object_type: pattern
name: Represent Time With Dedicated Types, Not Integers
library_path:
- software-engineering
- core
- hard-to-misuse
stage_binding: 2 block
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- time
- types
- hard_to_misuse
- units
cross_links:
- rel: related_to
  target_object_id: PAT_use_dedicated_types_over_general_ones
reference:
  source_id: gcbc_think_like_swe
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u07, pp. 193-198
  evidence_type: text
confidence: high
references: []
variants: []
---

# Represent Time With Dedicated Types, Not Integers

## Pattern Rule
**IF** you need to represent a time-based concept — an instant, an amount of time, or a date
**THEN** use a dedicated time type from a robust library rather than a bare integer of seconds or milliseconds, so the type states which concept it is and encapsulates its units.

## Do
- Distinguish instant from amount with the type: a `Duration` parameter says unmistakably that a deadline is an amount of time, ending the ambiguity of an integer that could be seconds-since-epoch or a countdown.
- Encapsulate units in the type: a `Duration` created by one part of the code with a seconds factory and read elsewhere as milliseconds cannot mismatch, unlike an integer where passing a seconds value to a milliseconds parameter silently shows a message for five milliseconds.
- Use a date type that is not tied to an instant (a local date-time) for calendar concepts like a birthday, so a stored date is not shifted a day by a time-zone conversion.

## Don't
- Don't represent time as an integer and paper over the ambiguity with documentation; that piles more onto unreliable small print for something a type could make explicit.
- Don't hand-roll time handling — units, time zones, daylight saving, leap years — when a vetted library provides instant, duration, and local-date types built for exactly these traps.

## Checklist
- Does the type make clear whether a value is an instant, an amount, or a date?
- Are units carried by the type so two pieces of code cannot mismatch seconds and milliseconds?
- For calendar dates, is the value kept free of an implied time zone that could shift it?

## Notes
Time is the archetypal overly-general-type problem: an integer conveys neither which time concept it holds nor its units, producing the three failures Long walks through — instant-versus-amount ambiguity, a seconds/milliseconds mismatch that flashes a warning for 5 ms, and a birthday that renders a day earlier across time zones. Dedicated types from java.time, Noda Time, chrono, or js-joda encode the concept and units in the type, turning runtime confusion into compile-time clarity. It is a specialization of the dedicated-type rule for the domain that most often tempts a bare integer.

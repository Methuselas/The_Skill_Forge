---
object_id: PAT_choose_the_tables_access_scheme_by_the_key
object_type: pattern
name: Choose a Table's Access Scheme by the Shape of Its Key
library_path:
- software-engineering
- core
- control-flow
stage_binding: 2 block
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- table_driven
- lookup
- indexes
- boundaries
cross_links:
- rel: related_to
  target_object_id: PAT_put_the_variation_in_data_rather_than_logic
- rel: related_to
  target_object_id: PAT_bound_an_arithmetic_expression_before_trusting_it
- rel: related_to
  target_object_id: PAT_extract_a_routine_even_when_it_seems_too_small
reference:
  source_title: 'Code Complete: A Practical Handbook of Software Construction, Second Edition'
  author: Steve McConnell
confidence: high
references: []
variants: []
---

# Choose a Table's Access Scheme by the Shape of Its Key

## Pattern Rule
**IF** you have decided to drive behaviour from a table and now have to decide how an entry gets found
**THEN** pick the scheme from what the key looks like — direct where the data indexes the table as it stands, indexed where the key space is far larger than the population, stair-step where entries cover ranges rather than points.
**ELSE** where none of the three fits without contorting something, transform the key inside a routine of its own rather than reshaping the table to accommodate an awkward key.

## Do
- Try for direct access first and check whether a small adjustment buys it. Month numbers index a twelve-entry array as they stand. Ages needing one rate below eighteen and another above sixty-five can be made to key directly by duplicating those two rates across the out-of-range ages — which spends table space to buy the simplest possible access, and is a legitimate move rather than a hack.
- Reach for an index table when the key space dwarfs the population and entries are large. A hundred stocked items with four-digit part numbers means either a ten-thousand-entry main table or a ten-thousand-entry index pointing into a hundred-entry one, and where each main entry runs to a hundred bytes that is thirty thousand bytes against a million.
- Take the index table's second benefit deliberately, because it is easy to miss. Several indexes can address one table through different fields, so the same employee records are reachable by name, by hiring date, and by salary without any of them being duplicated.
- Use stair-step where the boundaries are ranges and the numbers resist arithmetic. Grade cut-offs at fifty, sixty-five, seventy-five and ninety have no transformation that maps them to positions, and probabilities running to six decimal places defeat any attempt to invent one.
- Put the key calculation in a routine of its own whatever scheme you choose. That is the single thing that keeps the scheme changeable — an access approach spread through the program in the form of duplicated arithmetic is one you will not replace.

## Don't
- Don't let the stair-step boundaries go unexamined, because this is where the scheme's defects concentrate. Arrange the search so anything failing to match a lower range falls into the uppermost one, invent an artificial top bound where you need one to make that work, and check every comparison for the difference between less-than and less-than-or-equal.
- Don't scan a long stair-step table sequentially without pricing it. A binary search works, with one wrinkle worth knowing — it is looking for the category a value belongs to rather than for a matching entry, so the decision about where a value *should* go carries the endpoint handling and needs its own attention.
- Don't choose stair-step by default when an index would serve. Where the values are discrete and few enough to enumerate, an index trades memory for directness and removes the search entirely; where they are continuous or arbitrarily precise, it is not available at all.
- Don't spend long comparing schemes that would all work. More than one is often viable, and the effort is better spent on getting the boundaries right than on ranking the candidates.

## Checklist
- Does the data index the table as it stands, or after a transformation you can state in one line?
- How sparse is the key space, and how large is each main entry?
- Do entries correspond to points or to ranges?
- Is every boundary covered, including everything above the highest range?
- Is the key calculation in one routine, or repeated at each access site?

## Notes
The three schemes are points on one trade between space and directness. Direct access is the fastest to read and to execute and demands that the key already be an index or become one cheaply. An index table buys a compact main table at the cost of one extra hop and a second structure to maintain. Stair-step gives up direct addressing altogether in exchange for handling data that no transformation reaches, and pays for it with a search. Nothing here is a fallback for a failed attempt at the previous one; each fits a different shape of key.

Key-fudging deserves rehabilitating, because duplicating information to make a key work directly looks like the sort of thing you should be ashamed of. It is not. Repeating one rate across eighteen out-of-range ages turns an awkward lookup into an array index, and the duplication lives in a table where it is visible and easy to regenerate rather than in logic where it would be scattered. The judgment is about how much space the duplication costs against how much complexity it removes.

The endpoint warning is the one to act on rather than merely note. Stair-step tables concentrate their defects at the boundaries — the top range that nothing falls into because the search never reaches it, the comparison that should have been inclusive, the artificial upper bound nobody added. These are off-by-one errors with a table wrapped around them, and they behave like off-by-one errors do, which is to say they work for every case anyone tried by hand.

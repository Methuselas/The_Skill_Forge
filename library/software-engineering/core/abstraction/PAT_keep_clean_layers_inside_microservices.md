---
object_id: PAT_keep_clean_layers_inside_microservices
object_type: pattern
name: Keep Clean Layers of Abstraction Inside Microservices
library_path:
- software-engineering
- core
- abstraction
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
- microservices
- abstraction
- architecture
- reuse
cross_links:
- rel: related_to
  target_object_id: PAT_decompose_into_layers_of_abstraction
reference:
  source_title: 'Good Code, Bad Code: Think Like a Software Engineer'
  author: Tom Long
confidence: medium
references: []
variants: []
---

# Keep Clean Layers of Abstraction Inside Microservices

## Pattern Rule
**IF** you are working inside a microservices architecture and are tempted to conclude that internal code structure no longer matters because the service boundary already provides a clean layer
**THEN** still break the service's problem into subproblems with clean internal layers, because a service nominally doing "one thing" still solves many subproblems and other teams may need to reuse its logic.

## Do
- Enumerate the subproblems hiding inside the "one thing": a stock-level service must handle items, multiple warehouses and locations, per-country availability by delivery range, talking to the datastore, and interpreting its returned data.
- Trace a single operation to expose its internal layers: answering "is this item in stock for this customer" means finding warehouses in range, querying the datastore, interpreting the format, and returning an answer.
- Design internal layers so reusable logic (interpreting the database's data format) can be shared with other teams, even those that bypass the service and scan the database directly for latency.

## Don't
- Don't treat the microservice boundary as a substitute for thinking about the layers of abstraction within it.
- Don't bundle a service's several subproblems into one undivided lump on the theory that the service is already small.

## Checklist
- Can you list the distinct subproblems this service solves internally?
- Would another team be able to reuse a piece of this service's logic without calling the whole service?
- Are the service's internal layers as clean as you would demand of a library?

## Notes
Long counters a common argument — that microservices make internal structure irrelevant because the service is the abstraction — by showing a stock-management service is still of a size and scope that hides multiple subproblems. The retailer example makes it concrete: analytics teams scanning the stock database directly still want to reuse the data-interpretation logic, which is only possible if that logic sits in a clean internal layer. The whole decomposition argument applies unchanged one level down.

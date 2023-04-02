# Slot: street
_The street component of a physical mailing address. Unabbreviated by default (Street, not St.) Multi-line values are represented by multivalues. See examples._


URI: [mug:street](https://w3id.org/caufieldjh-in-space/mug_schemas/street)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Address](Address.md) | A mailing address for a physical location
[ResidentialAddress](ResidentialAddress.md) | Address of a residential location
[WorkingAddress](WorkingAddress.md) | Address of a workplace location






## Properties

* Range: [String](String.md)
* Multivalued: True









## Examples

| Value |
| --- |
| Sandstone Street |
| Colonial Highway |
| Stevens Q. Puddleton Trail |

## TODOs

* convert to a GeneratedThing, at least to make street type enum

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: street
description: The street component of a physical mailing address. Unabbreviated by
  default (Street, not St.) Multi-line values are represented by multivalues. See
  examples.
todos:
- convert to a GeneratedThing, at least to make street type enum
examples:
- value: Sandstone Street
- value: Colonial Highway
- value: Stevens Q. Puddleton Trail
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
multivalued: true
alias: street
domain_of:
- Address
range: string

```
</details>
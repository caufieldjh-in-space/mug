# Slot: locality
_The broadest component of a physical mailing address. Should include postal code._


URI: [mug:locality](https://w3id.org/caufieldjh-in-space/mug_schemas/locality)



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
| Kansas City, Missouri 64102, United States |
| Staples, Ontario N0P 2J0, Canada |
| 14612 Falkensee, Germany |

## TODOs

* evaluate whether this really needs to be multivalued
* convert to a GeneratedThing
* but note that city, broader location, and postal code are all related
* define a regex pattern (or patterns)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: locality
description: The broadest component of a physical mailing address. Should include
  postal code.
todos:
- evaluate whether this really needs to be multivalued
- convert to a GeneratedThing
- but note that city, broader location, and postal code are all related
- define a regex pattern (or patterns)
examples:
- value: Kansas City, Missouri 64102, United States
- value: Staples, Ontario N0P 2J0, Canada
- value: 14612 Falkensee, Germany
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
multivalued: true
alias: locality
domain_of:
- Address
range: string

```
</details>
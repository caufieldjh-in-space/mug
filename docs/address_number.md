# Slot: address_number
_The most specific component of a physical mailing address. Multi-line values are  represented by multivalues._


URI: [mug:address_number](https://w3id.org/caufieldjh-in-space/mug_schemas/address_number)



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
| 30 |
| 40B |
| Room 581 |
| Floor 12 |
| Bamberg Building |

## TODOs

* add an enum for corporate departments

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: address_number
description: The most specific component of a physical mailing address. Multi-line
  values are  represented by multivalues.
todos:
- add an enum for corporate departments
examples:
- value: '30'
- value: 40B
- value: Room 581
- value: Floor 12
- value: Bamberg Building
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
multivalued: true
alias: address_number
domain_of:
- Address
range: string

```
</details>
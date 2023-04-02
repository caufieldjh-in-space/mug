# Slot: preferred_name
_Any name used to refer to a specific Person. Often presented in quotes, but that doesn't have to be the case here._


URI: [mug:preferred_name](https://w3id.org/caufieldjh-in-space/mug_schemas/preferred_name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[FullName](FullName.md) | All parts of a name






## Properties

* Range: [String](String.md)
* Multivalued: True






## Aliases


* nickname
* pet name
* pseudonym




## Examples

| Value |
| --- |
| Jimmy |
| The Brick |
| xXDarksoul920Xx |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: preferred_name
description: Any name used to refer to a specific Person. Often presented in quotes,
  but that doesn't have to be the case here.
examples:
- value: Jimmy
- value: The Brick
- value: xXDarksoul920Xx
from_schema: https://w3id.org/my-org/mug_schemas
aliases:
- nickname
- pet name
- pseudonym
rank: 1000
multivalued: true
alias: preferred_name
domain_of:
- FullName
range: string

```
</details>
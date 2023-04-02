# Slot: family_name
_A family name. Optional, so mononyms should go in given_name. For multvalued names like  "Duarte de Perón", the "de" particle should be part of the second name, not its own value._


URI: [mug:family_name](https://w3id.org/caufieldjh-in-space/mug_schemas/family_name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[FullName](FullName.md) | All parts of a name






## Properties

* Range: [String](String.md)
* Multivalued: True






## Aliases


* last name
* surname




## Examples

| Value |
| --- |
| Quigley |
| Branson-Danforth |
| de Souza |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: family_name
description: A family name. Optional, so mononyms should go in given_name. For multvalued
  names like  "Duarte de Perón", the "de" particle should be part of the second name,
  not its own value.
examples:
- value: Quigley
- value: Branson-Danforth
- value: de Souza
from_schema: https://w3id.org/my-org/mug_schemas
aliases:
- last name
- surname
rank: 1000
multivalued: true
alias: family_name
domain_of:
- FullName
range: string

```
</details>
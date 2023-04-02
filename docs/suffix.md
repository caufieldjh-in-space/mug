# Slot: suffix
_A formal or informal postfix for a name. Use the full version, not an abbreviation. These can get messy about commas and such, but that's not a problem to be solved here._


URI: [mug:suffix](https://w3id.org/caufieldjh-in-space/mug_schemas/suffix)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[FullName](FullName.md) | All parts of a name






## Properties

* Range: [String](String.md)
* Multivalued: True






## Aliases


* postnominative




## Examples

| Value |
| --- |
| Jr |
| IV |
| CEO |
| Professor Emeritus |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: suffix
description: A formal or informal postfix for a name. Use the full version, not an
  abbreviation. These can get messy about commas and such, but that's not a problem
  to be solved here.
examples:
- value: Jr
- value: IV
- value: CEO
- value: Professor Emeritus
from_schema: https://w3id.org/my-org/mug_schemas
aliases:
- postnominative
rank: 1000
multivalued: true
alias: suffix
domain_of:
- FullName
range: string

```
</details>
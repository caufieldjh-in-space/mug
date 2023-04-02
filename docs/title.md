# Slot: title
_A formal or informal prefix for a name. Use the full version, not an abbreviation._


URI: [mug:title](https://w3id.org/caufieldjh-in-space/mug_schemas/title)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[FullName](FullName.md) | All parts of a name






## Properties

* Range: [String](String.md)
* Multivalued: True






## Aliases


* prenominative




## Examples

| Value |
| --- |
| Lady |
| Captain |
| His Holiness |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: title
description: A formal or informal prefix for a name. Use the full version, not an
  abbreviation.
examples:
- value: Lady
- value: Captain
- value: His Holiness
from_schema: https://w3id.org/my-org/mug_schemas
aliases:
- prenominative
rank: 1000
multivalued: true
alias: title
domain_of:
- FullName
range: string

```
</details>
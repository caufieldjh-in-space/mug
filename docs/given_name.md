# Slot: given_name
_A given name. May be a mononym (i.e., the only name). When multivalued, implies spaces in between names._


URI: [mug:given_name](https://w3id.org/caufieldjh-in-space/mug_schemas/given_name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[FullName](FullName.md) | All parts of a name






## Properties

* Range: [String](String.md)
* Multivalued: True






## Aliases


* first name
* forename




## Examples

| Value |
| --- |
| Frances |
| Mary Kate |
| Sinbad |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: given_name
description: A given name. May be a mononym (i.e., the only name). When multivalued,
  implies spaces in between names.
examples:
- value: Frances
- value: Mary Kate
- value: Sinbad
from_schema: https://w3id.org/my-org/mug_schemas
aliases:
- first name
- forename
rank: 1000
multivalued: true
alias: given_name
domain_of:
- FullName
range: string

```
</details>
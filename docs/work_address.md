# Slot: work_address
_One or more addresses where a person may work._


URI: [mug:work_address](https://w3id.org/caufieldjh-in-space/mug_schemas/work_address)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Person](Person.md) | General class for people
[Company](Company.md) | A corporate entity






## Properties

* Range: [WorkingAddress](WorkingAddress.md)
* Multivalued: True








## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: work_address
description: One or more addresses where a person may work.
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
multivalued: true
alias: work_address
domain_of:
- Person
- Company
range: WorkingAddress

```
</details>
# Slot: id
_A unique identifier for a thing_


URI: [schema:identifier](http://schema.org/identifier)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[NamedThing](NamedThing.md) | A generic grouping for any identifiable entity
[GeneratedThing](GeneratedThing.md) | Any set of data representing a single generated object
[Address](Address.md) | A mailing address for a physical location
[ResidentialAddress](ResidentialAddress.md) | Address of a residential location
[WorkingAddress](WorkingAddress.md) | Address of a workplace location
[Person](Person.md) | General class for people
[FullName](FullName.md) | All parts of a name
[Company](Company.md) | A corporate entity






## Properties

* Range: [Uriorcurie](Uriorcurie.md)







## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: id
description: A unique identifier for a thing
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
slot_uri: schema:identifier
identifier: true
alias: id
domain_of:
- NamedThing
range: uriorcurie

```
</details>
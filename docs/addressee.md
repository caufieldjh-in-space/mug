# Slot: addressee
_The recipient of mail. May be a person or a company - the name is the most relevant part._


URI: [mug:addressee](https://w3id.org/caufieldjh-in-space/mug_schemas/addressee)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Address](Address.md) | A mailing address for a physical location
[ResidentialAddress](ResidentialAddress.md) | Address of a residential location
[WorkingAddress](WorkingAddress.md) | Address of a workplace location






## Properties

* Range: [String](String.md)







## TODOs

* Unions can be tricky, so test this

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas




## LinkML Source

<details>
```yaml
name: addressee
description: The recipient of mail. May be a person or a company - the name is the
  most relevant part.
todos:
- Unions can be tricky, so test this
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
alias: addressee
domain_of:
- Address
range: string
any_of:
- range: Person
- range: Company

```
</details>
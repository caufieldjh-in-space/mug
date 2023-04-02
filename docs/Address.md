# Class: Address
_A mailing address for a physical location. This is the general class - it includes an addressee, but that isn't required._




URI: [mug:Address](https://w3id.org/caufieldjh-in-space/mug_schemas/Address)



```mermaid
 classDiagram
    class Address
      GeneratedThing <|-- Address
      

      Address <|-- ResidentialAddress
      Address <|-- WorkingAddress
      
      
      Address : address_number
        
      Address : addressee
        
      Address : description
        
      Address : id
        
      Address : locality
        
      Address : name
        
      Address : street
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [GeneratedThing](GeneratedThing.md)
        * **Address**
            * [ResidentialAddress](ResidentialAddress.md)
            * [WorkingAddress](WorkingAddress.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [addressee](addressee.md) | 0..1 <br/> [String](String.md) | The recipient of mail | direct |
| [address_number](address_number.md) | 0..* <br/> [String](String.md) | The most specific component of a physical mailing address | direct |
| [street](street.md) | 0..* <br/> [String](String.md) | The street component of a physical mailing address | direct |
| [locality](locality.md) | 0..* <br/> [String](String.md) | The broadest component of a physical mailing address | direct |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [NamedThing](NamedThing.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mug:Address |
| native | mug:Address |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Address
description: A mailing address for a physical location. This is the general class
  - it includes an addressee, but that isn't required.
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
is_a: GeneratedThing
slots:
- addressee
- address_number
- street
- locality

```
</details>

### Induced

<details>
```yaml
name: Address
description: A mailing address for a physical location. This is the general class
  - it includes an addressee, but that isn't required.
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
is_a: GeneratedThing
attributes:
  addressee:
    name: addressee
    description: The recipient of mail. May be a person or a company - the name is
      the most relevant part.
    todos:
    - Unions can be tricky, so test this
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    alias: addressee
    owner: Address
    domain_of:
    - Address
    range: string
    any_of:
    - range: Person
    - range: Company
  address_number:
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
    owner: Address
    domain_of:
    - Address
    range: string
  street:
    name: street
    description: The street component of a physical mailing address. Unabbreviated
      by default (Street, not St.) Multi-line values are represented by multivalues.
      See examples.
    todos:
    - convert to a GeneratedThing, at least to make street type enum
    examples:
    - value: Sandstone Street
    - value: Colonial Highway
    - value: Stevens Q. Puddleton Trail
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    multivalued: true
    alias: street
    owner: Address
    domain_of:
    - Address
    range: string
  locality:
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
    owner: Address
    domain_of:
    - Address
    range: string
  id:
    name: id
    description: A unique identifier for a thing
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: Address
    domain_of:
    - NamedThing
    range: uriorcurie
  name:
    name: name
    description: A human-readable name for a thing
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: Address
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A human-readable description for a thing. For a GeneratedThing, this
      will be one potential string representation of the object.
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: Address
    domain_of:
    - NamedThing
    range: string

```
</details>
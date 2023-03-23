# Class: GeneratedThing
_Represents a GeneratedThing_




URI: [mug_schemas:GeneratedThing](https://w3id.org/my-org/mug_schemas/GeneratedThing)



```mermaid
 classDiagram
    class GeneratedThing
      NamedThing <|-- GeneratedThing
      
      GeneratedThing : age_in_years
        
      GeneratedThing : birth_date
        
      GeneratedThing : description
        
      GeneratedThing : id
        
      GeneratedThing : name
        
      GeneratedThing : primary_email
        
      GeneratedThing : vital_status
        
          GeneratedThing ..> PersonStatus : vital_status
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **GeneratedThing**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [primary_email](primary_email.md) | 0..1 <br/> [String](String.md) | The main email address of a person | direct |
| [birth_date](birth_date.md) | 0..1 <br/> [Date](Date.md) | Date on which a person is born | direct |
| [age_in_years](age_in_years.md) | 0..1 <br/> [Integer](Integer.md) | Number of years since birth | direct |
| [vital_status](vital_status.md) | 0..1 <br/> [PersonStatus](PersonStatus.md) | living or dead status | direct |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | A unique identifier for a thing | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human-readable name for a thing | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A human-readable description for a thing | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneratedThingCollection](GeneratedThingCollection.md) | [entries](entries.md) | range | [GeneratedThing](GeneratedThing.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mug_schemas:GeneratedThing |
| native | mug_schemas:GeneratedThing |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneratedThing
description: Represents a GeneratedThing
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
is_a: NamedThing
slots:
- primary_email
- birth_date
- age_in_years
- vital_status
slot_usage:
  primary_email:
    name: primary_email
    domain_of:
    - GeneratedThing
    pattern: ^\S+@[\S+\.]+\S+

```
</details>

### Induced

<details>
```yaml
name: GeneratedThing
description: Represents a GeneratedThing
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
is_a: NamedThing
slot_usage:
  primary_email:
    name: primary_email
    domain_of:
    - GeneratedThing
    pattern: ^\S+@[\S+\.]+\S+
attributes:
  primary_email:
    name: primary_email
    description: The main email address of a person
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    slot_uri: schema:email
    alias: primary_email
    owner: GeneratedThing
    domain_of:
    - GeneratedThing
    range: string
    pattern: ^\S+@[\S+\.]+\S+
  birth_date:
    name: birth_date
    description: Date on which a person is born
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    slot_uri: schema:birthDate
    alias: birth_date
    owner: GeneratedThing
    domain_of:
    - GeneratedThing
    range: date
  age_in_years:
    name: age_in_years
    description: Number of years since birth
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    alias: age_in_years
    owner: GeneratedThing
    domain_of:
    - GeneratedThing
    range: integer
  vital_status:
    name: vital_status
    description: living or dead status
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    alias: vital_status
    owner: GeneratedThing
    domain_of:
    - GeneratedThing
    range: PersonStatus
  id:
    name: id
    description: A unique identifier for a thing
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: GeneratedThing
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
    owner: GeneratedThing
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A human-readable description for a thing
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: GeneratedThing
    domain_of:
    - NamedThing
    range: string

```
</details>
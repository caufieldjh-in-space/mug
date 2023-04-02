# Class: GeneratedThingCollection
_A holder for GeneratedThing objects_




URI: [mug:GeneratedThingCollection](https://w3id.org/caufieldjh-in-space/mug_schemas/GeneratedThingCollection)



```mermaid
 classDiagram
    class GeneratedThingCollection
      GeneratedThingCollection : entries
        
          GeneratedThingCollection ..> GeneratedThing : entries
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [entries](entries.md) | 0..* <br/> [GeneratedThing](GeneratedThing.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/my-org/mug_schemas





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mug:GeneratedThingCollection |
| native | mug:GeneratedThingCollection |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneratedThingCollection
description: A holder for GeneratedThing objects
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
attributes:
  entries:
    name: entries
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    multivalued: true
    range: GeneratedThing
    inlined: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: GeneratedThingCollection
description: A holder for GeneratedThing objects
from_schema: https://w3id.org/my-org/mug_schemas
rank: 1000
attributes:
  entries:
    name: entries
    from_schema: https://w3id.org/my-org/mug_schemas
    rank: 1000
    multivalued: true
    alias: entries
    owner: GeneratedThingCollection
    domain_of:
    - GeneratedThingCollection
    range: GeneratedThing
    inlined: true
tree_root: true

```
</details>
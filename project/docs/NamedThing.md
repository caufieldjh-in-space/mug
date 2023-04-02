
# Class: NamedThing


A generic grouping for any identifiable entity

URI: [mug:NamedThing](https://w3id.org/caufieldjh-in-space/mug_schemas/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F]^-[GeneratedThing],[GeneratedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F]^-[GeneratedThing],[GeneratedThing])

## Children

 * [GeneratedThing](GeneratedThing.md) - Any set of data representing a single generated object. In MUG, this does not include the object's string representation, but rather all components used in generating that representation. Think of this like the ingredients list rather than the finished meal.

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing. For a GeneratedThing, this will be one potential string representation of the object.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Thing |


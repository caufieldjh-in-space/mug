
# Class: GeneratedThing


Any set of data representing a single generated object. In MUG, this does not include the object's string representation, but rather all components used in generating that representation. Think of this like the ingredients list rather than the finished meal.

URI: [mug:GeneratedThing](https://w3id.org/caufieldjh-in-space/mug_schemas/GeneratedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Person],[NamedThing],[GeneratedThingCollection]++-%20entries%200..*>[GeneratedThing&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[GeneratedThing]^-[Person],[GeneratedThing]^-[FullName],[GeneratedThing]^-[Company],[GeneratedThing]^-[Address],[NamedThing]^-[GeneratedThing],[GeneratedThingCollection],[FullName],[Company],[Address])](https://yuml.me/diagram/nofunky;dir:TB/class/[Person],[NamedThing],[GeneratedThingCollection]++-%20entries%200..*>[GeneratedThing&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[GeneratedThing]^-[Person],[GeneratedThing]^-[FullName],[GeneratedThing]^-[Company],[GeneratedThing]^-[Address],[NamedThing]^-[GeneratedThing],[GeneratedThingCollection],[FullName],[Company],[Address])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Children

 * [Address](Address.md) - A mailing address for a physical location. This is the general class - it includes an addressee, but that isn't required.
 * [Company](Company.md) - A corporate entity.
 * [FullName](FullName.md) - All parts of a name.
 * [Person](Person.md) - General class for people.

## Referenced by Class

 *  **None** *[➞entries](generatedThingCollection__entries.md)*  <sub>0..\*</sub>  **[GeneratedThing](GeneratedThing.md)**

## Attributes


### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing. For a GeneratedThing, this will be one potential string representation of the object.
     * Range: [String](types/String.md)

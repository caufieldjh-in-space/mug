
# Class: Person


General class for people.

URI: [mug:Person](https://w3id.org/caufieldjh-in-space/mug_schemas/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkingAddress],[ResidentialAddress],[WorkingAddress]<work_address%200..*-%20[Person&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[ResidentialAddress]<home_address%200..*-%20[Person],[FullName]<full_name%200..1-%20[Person],[ResidentialAddress]-%20addressee%201..1>[Person],[GeneratedThing]^-[Person],[GeneratedThing],[FullName])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkingAddress],[ResidentialAddress],[WorkingAddress]<work_address%200..*-%20[Person&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[ResidentialAddress]<home_address%200..*-%20[Person],[FullName]<full_name%200..1-%20[Person],[ResidentialAddress]-%20addressee%201..1>[Person],[GeneratedThing]^-[Person],[GeneratedThing],[FullName])

## Parents

 *  is_a: [GeneratedThing](GeneratedThing.md) - Any set of data representing a single generated object. In MUG, this does not include the object's string representation, but rather all components used in generating that representation. Think of this like the ingredients list rather than the finished meal.

## Referenced by Class

 *  **[ResidentialAddress](ResidentialAddress.md)** *[ResidentialAddress➞addressee](ResidentialAddress_addressee.md)*  <sub>1..1</sub>  **[Person](Person.md)**

## Attributes


### Own

 * [full_name](full_name.md)  <sub>0..1</sub>
     * Description: Slot for all name parts.
     * Range: [FullName](FullName.md)
 * [home_address](home_address.md)  <sub>0..\*</sub>
     * Description: One or more addresses where a person may live.
     * Range: [ResidentialAddress](ResidentialAddress.md)
 * [work_address](work_address.md)  <sub>0..\*</sub>
     * Description: One or more addresses where a person may work.
     * Range: [WorkingAddress](WorkingAddress.md)

### Inherited from GeneratedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing. For a GeneratedThing, this will be one potential string representation of the object.
     * Range: [String](types/String.md)

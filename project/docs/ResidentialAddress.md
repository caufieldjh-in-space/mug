
# Class: ResidentialAddress


Address of a residential location.

URI: [mug:ResidentialAddress](https://w3id.org/caufieldjh-in-space/mug_schemas/ResidentialAddress)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Person]<addressee%201..1-%20[ResidentialAddress&#124;address_number(i):string%20*;street(i):string%20*;locality(i):string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Person]-%20home_address%200..*>[ResidentialAddress],[Address]^-[ResidentialAddress],[Person],[Address])](https://yuml.me/diagram/nofunky;dir:TB/class/[Person]<addressee%201..1-%20[ResidentialAddress&#124;address_number(i):string%20*;street(i):string%20*;locality(i):string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Person]-%20home_address%200..*>[ResidentialAddress],[Address]^-[ResidentialAddress],[Person],[Address])

## Parents

 *  is_a: [Address](Address.md) - A mailing address for a physical location. This is the general class - it includes an addressee, but that isn't required.

## Referenced by Class

 *  **None** *[home_address](home_address.md)*  <sub>0..\*</sub>  **[ResidentialAddress](ResidentialAddress.md)**

## Attributes


### Own

 * [ResidentialAddress➞addressee](ResidentialAddress_addressee.md)  <sub>1..1</sub>
     * Description: The recipient of mail. May be a person or a company - the name is the most relevant part.
     * Range: [Person](Person.md)

### Inherited from Address:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing. For a GeneratedThing, this will be one potential string representation of the object.
     * Range: [String](types/String.md)
 * [address_number](address_number.md)  <sub>0..\*</sub>
     * Description: The most specific component of a physical mailing address. Multi-line values are  represented by multivalues.
     * Range: [String](types/String.md)
     * Example: 30 None
     * Example: 40B None
     * Example: Room 581 None
     * Example: Floor 12 None
     * Example: Bamberg Building None
 * [street](street.md)  <sub>0..\*</sub>
     * Description: The street component of a physical mailing address. Unabbreviated by default (Street, not St.) Multi-line values are represented by multivalues. See examples.
     * Range: [String](types/String.md)
     * Example: Sandstone Street None
     * Example: Colonial Highway None
     * Example: Stevens Q. Puddleton Trail None
 * [locality](locality.md)  <sub>0..\*</sub>
     * Description: The broadest component of a physical mailing address. Should include postal code.
     * Range: [String](types/String.md)
     * Example: Kansas City, Missouri 64102, United States None
     * Example: Staples, Ontario N0P 2J0, Canada None
     * Example: 14612 Falkensee, Germany None

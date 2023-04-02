
# Class: WorkingAddress


Address of a workplace location. Technically this is a commercial address since it's specific to Company, but for now that can cover things like government agencies, too.

URI: [mug:WorkingAddress](https://w3id.org/caufieldjh-in-space/mug_schemas/WorkingAddress)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Company]<addressee%201..1-%20[WorkingAddress&#124;address_number(i):string%20*;street(i):string%20*;locality(i):string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Person]-%20work_address%200..*>[WorkingAddress],[Company]-%20work_address%200..*>[WorkingAddress],[Address]^-[WorkingAddress],[Person],[Company],[Address])](https://yuml.me/diagram/nofunky;dir:TB/class/[Company]<addressee%201..1-%20[WorkingAddress&#124;address_number(i):string%20*;street(i):string%20*;locality(i):string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Person]-%20work_address%200..*>[WorkingAddress],[Company]-%20work_address%200..*>[WorkingAddress],[Address]^-[WorkingAddress],[Person],[Company],[Address])

## Parents

 *  is_a: [Address](Address.md) - A mailing address for a physical location. This is the general class - it includes an addressee, but that isn't required.

## Referenced by Class

 *  **None** *[work_address](work_address.md)*  <sub>0..\*</sub>  **[WorkingAddress](WorkingAddress.md)**

## Attributes


### Own

 * [WorkingAddress➞addressee](WorkingAddress_addressee.md)  <sub>1..1</sub>
     * Description: The recipient of mail. May be a person or a company - the name is the most relevant part.
     * Range: [Company](Company.md)

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

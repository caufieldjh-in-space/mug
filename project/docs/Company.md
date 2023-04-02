
# Class: Company


A corporate entity.

URI: [mug:Company](https://w3id.org/caufieldjh-in-space/mug_schemas/Company)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkingAddress],[GeneratedThing],[WorkingAddress]<work_address%200..*-%20[Company&#124;company_name:string%20%3F;industry:string%20%3F;slogan:string%20%3F;logo_description:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[WorkingAddress]-%20addressee%201..1>[Company],[GeneratedThing]^-[Company])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkingAddress],[GeneratedThing],[WorkingAddress]<work_address%200..*-%20[Company&#124;company_name:string%20%3F;industry:string%20%3F;slogan:string%20%3F;logo_description:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[WorkingAddress]-%20addressee%201..1>[Company],[GeneratedThing]^-[Company])

## Parents

 *  is_a: [GeneratedThing](GeneratedThing.md) - Any set of data representing a single generated object. In MUG, this does not include the object's string representation, but rather all components used in generating that representation. Think of this like the ingredients list rather than the finished meal.

## Referenced by Class

 *  **[WorkingAddress](WorkingAddress.md)** *[WorkingAddress➞addressee](WorkingAddress_addressee.md)*  <sub>1..1</sub>  **[Company](Company.md)**

## Attributes


### Own

 * [company_name](company_name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [work_address](work_address.md)  <sub>0..\*</sub>
     * Description: One or more addresses where a person may work.
     * Range: [WorkingAddress](WorkingAddress.md)
 * [industry](industry.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [slogan](slogan.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [logo_description](logo_description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

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

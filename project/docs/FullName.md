
# Class: FullName


All parts of a name.

URI: [mug:FullName](https://w3id.org/caufieldjh-in-space/mug_schemas/FullName)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneratedThing],[Person]-%20full_name%200..1>[FullName&#124;given_name:string%20*;family_name:string%20*;other_name:string%20*;preferred_name:string%20*;title:string%20*;suffix:string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[GeneratedThing]^-[FullName],[Person])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneratedThing],[Person]-%20full_name%200..1>[FullName&#124;given_name:string%20*;family_name:string%20*;other_name:string%20*;preferred_name:string%20*;title:string%20*;suffix:string%20*;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[GeneratedThing]^-[FullName],[Person])

## Parents

 *  is_a: [GeneratedThing](GeneratedThing.md) - Any set of data representing a single generated object. In MUG, this does not include the object's string representation, but rather all components used in generating that representation. Think of this like the ingredients list rather than the finished meal.

## Referenced by Class

 *  **None** *[full_name](full_name.md)*  <sub>0..1</sub>  **[FullName](FullName.md)**

## Attributes


### Own

 * [given_name](given_name.md)  <sub>0..\*</sub>
     * Description: A given name. May be a mononym (i.e., the only name). When multivalued, implies spaces in between names.
     * Range: [String](types/String.md)
     * Example: Frances None
     * Example: Mary Kate None
     * Example: Sinbad None
 * [family_name](family_name.md)  <sub>0..\*</sub>
     * Description: A family name. Optional, so mononyms should go in given_name. For multvalued names like  "Duarte de Perón", the "de" particle should be part of the second name, not its own value.
     * Range: [String](types/String.md)
     * Example: Quigley None
     * Example: Branson-Danforth None
     * Example: de Souza None
 * [other_name](other_name.md)  <sub>0..\*</sub>
     * Description: A middle name or names, usually, or at least a name usually presented in between a given_name and a family_name.
     * Range: [String](types/String.md)
 * [preferred_name](preferred_name.md)  <sub>0..\*</sub>
     * Description: Any name used to refer to a specific Person. Often presented in quotes, but that doesn't have to be the case here.
     * Range: [String](types/String.md)
     * Example: Jimmy None
     * Example: The Brick None
     * Example: xXDarksoul920Xx None
 * [title](title.md)  <sub>0..\*</sub>
     * Description: A formal or informal prefix for a name. Use the full version, not an abbreviation.
     * Range: [String](types/String.md)
     * Example: Lady None
     * Example: Captain None
     * Example: His Holiness None
 * [suffix](suffix.md)  <sub>0..\*</sub>
     * Description: A formal or informal postfix for a name. Use the full version, not an abbreviation. These can get messy about commas and such, but that's not a problem to be solved here.
     * Range: [String](types/String.md)
     * Example: Jr None
     * Example: IV None
     * Example: CEO None
     * Example: Professor Emeritus None

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

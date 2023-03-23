
# Class: GeneratedThing


Represents a GeneratedThing

URI: [mug_schemas:GeneratedThing](https://w3id.org/my-org/mug_schemas/GeneratedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[GeneratedThingCollection]++-%20entries%200..*>[GeneratedThing&#124;primary_email:string%20%3F;birth_date:date%20%3F;age_in_years:integer%20%3F;vital_status:PersonStatus%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[GeneratedThing],[GeneratedThingCollection])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[GeneratedThingCollection]++-%20entries%200..*>[GeneratedThing&#124;primary_email:string%20%3F;birth_date:date%20%3F;age_in_years:integer%20%3F;vital_status:PersonStatus%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[NamedThing]^-[GeneratedThing],[GeneratedThingCollection])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Referenced by Class

 *  **None** *[➞entries](generatedThingCollection__entries.md)*  <sub>0..\*</sub>  **[GeneratedThing](GeneratedThing.md)**

## Attributes


### Own

 * [GeneratedThing➞primary_email](GeneratedThing_primary_email.md)  <sub>0..1</sub>
     * Description: The main email address of a person
     * Range: [String](types/String.md)
 * [birth_date](birth_date.md)  <sub>0..1</sub>
     * Description: Date on which a person is born
     * Range: [Date](types/Date.md)
 * [age_in_years](age_in_years.md)  <sub>0..1</sub>
     * Description: Number of years since birth
     * Range: [Integer](types/Integer.md)
 * [vital_status](vital_status.md)  <sub>0..1</sub>
     * Description: living or dead status
     * Range: [PersonStatus](PersonStatus.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing
     * Range: [String](types/String.md)

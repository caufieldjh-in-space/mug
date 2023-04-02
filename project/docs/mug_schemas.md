
# mug_schemas


**metamodel version:** 1.7.0

**version:** None


Schemas for Modular Universal Generators.


### Classes

 * [GeneratedThingCollection](GeneratedThingCollection.md) - A holder for GeneratedThing objects
 * [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity
     * [GeneratedThing](GeneratedThing.md) - Any set of data representing a single generated object. In MUG, this does not include the object's string representation, but rather all components used in generating that representation. Think of this like the ingredients list rather than the finished meal.
         * [Address](Address.md) - A mailing address for a physical location. This is the general class - it includes an addressee, but that isn't required.
             * [ResidentialAddress](ResidentialAddress.md) - Address of a residential location.
             * [WorkingAddress](WorkingAddress.md) - Address of a workplace location. Technically this is a commercial address since it's specific to Company, but for now that can cover things like government agencies, too.
         * [Company](Company.md) - A corporate entity.
         * [FullName](FullName.md) - All parts of a name.
         * [Person](Person.md) - General class for people.

### Mixins


### Slots

 * [address_number](address_number.md) - The most specific component of a physical mailing address. Multi-line values are  represented by multivalues.
 * [addressee](addressee.md) - The recipient of mail. May be a person or a company - the name is the most relevant part.
     * [ResidentialAddress➞addressee](ResidentialAddress_addressee.md)
     * [WorkingAddress➞addressee](WorkingAddress_addressee.md)
 * [company_name](company_name.md)
 * [description](description.md) - A human-readable description for a thing. For a GeneratedThing, this will be one potential string representation of the object.
 * [family_name](family_name.md) - A family name. Optional, so mononyms should go in given_name. For multvalued names like  "Duarte de Perón", the "de" particle should be part of the second name, not its own value.
 * [full_name](full_name.md) - Slot for all name parts.
 * [➞entries](generatedThingCollection__entries.md)
 * [given_name](given_name.md) - A given name. May be a mononym (i.e., the only name). When multivalued, implies spaces in between names.
 * [home_address](home_address.md) - One or more addresses where a person may live.
 * [id](id.md) - A unique identifier for a thing
 * [industry](industry.md)
 * [locality](locality.md) - The broadest component of a physical mailing address. Should include postal code.
 * [logo_description](logo_description.md)
 * [name](name.md) - A human-readable name for a thing
 * [other_name](other_name.md) - A middle name or names, usually, or at least a name usually presented in between a given_name and a family_name.
 * [preferred_name](preferred_name.md) - Any name used to refer to a specific Person. Often presented in quotes, but that doesn't have to be the case here.
 * [slogan](slogan.md)
 * [street](street.md) - The street component of a physical mailing address. Unabbreviated by default (Street, not St.) Multi-line values are represented by multivalues. See examples.
 * [suffix](suffix.md) - A formal or informal postfix for a name. Use the full version, not an abbreviation. These can get messy about commas and such, but that's not a problem to be solved here.
 * [title](title.md) - A formal or informal prefix for a name. Use the full version, not an abbreviation.
 * [work_address](work_address.md) - One or more addresses where a person may work.

### Enums


### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE

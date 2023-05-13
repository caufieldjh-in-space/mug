# Auto generated from mug_schemas.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-05-13T15:16:26
# Schema: mug_schemas
#
# id: https://w3id.org/my-org/mug_schemas
# description: Schemas for Modular Universal Generators.
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MUG = CurieNamespace('mug', 'https://w3id.org/caufieldjh-in-space/mug_schemas/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MUG


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class GeneratedThingId(NamedThingId):
    pass


class AddressId(GeneratedThingId):
    pass


class ResidentialAddressId(AddressId):
    pass


class WorkingAddressId(AddressId):
    pass


class PersonId(GeneratedThingId):
    pass


class FullNameId(GeneratedThingId):
    pass


class CompanyId(GeneratedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MUG.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class GeneratedThing(NamedThing):
    """
    Any set of data representing a single generated object. In MUG, this does not include the object's string
    representation, but rather all components used in generating that representation. Think of this like the
    ingredients list rather than the finished meal.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MUG.GeneratedThing
    class_class_curie: ClassVar[str] = "mug:GeneratedThing"
    class_name: ClassVar[str] = "GeneratedThing"
    class_model_uri: ClassVar[URIRef] = MUG.GeneratedThing

    id: Union[str, GeneratedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneratedThingId):
            self.id = GeneratedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Address(GeneratedThing):
    """
    A mailing address for a physical location. This is the general class. Does not include the addressee (a Person has
    a home_address, but the Address alone does not have a Person)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MUG.Address
    class_class_curie: ClassVar[str] = "mug:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = MUG.Address

    id: Union[str, AddressId] = None
    address_number: Optional[Union[str, List[str]]] = empty_list()
    street: Optional[Union[str, List[str]]] = empty_list()
    locality: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AddressId):
            self.id = AddressId(self.id)

        if not isinstance(self.address_number, list):
            self.address_number = [self.address_number] if self.address_number is not None else []
        self.address_number = [v if isinstance(v, str) else str(v) for v in self.address_number]

        if not isinstance(self.street, list):
            self.street = [self.street] if self.street is not None else []
        self.street = [v if isinstance(v, str) else str(v) for v in self.street]

        if not isinstance(self.locality, list):
            self.locality = [self.locality] if self.locality is not None else []
        self.locality = [v if isinstance(v, str) else str(v) for v in self.locality]

        super().__post_init__(**kwargs)


@dataclass
class ResidentialAddress(Address):
    """
    Address of a residential location.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MUG.ResidentialAddress
    class_class_curie: ClassVar[str] = "mug:ResidentialAddress"
    class_name: ClassVar[str] = "ResidentialAddress"
    class_model_uri: ClassVar[URIRef] = MUG.ResidentialAddress

    id: Union[str, ResidentialAddressId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResidentialAddressId):
            self.id = ResidentialAddressId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class WorkingAddress(Address):
    """
    Address of a workplace location. Technically this is a commercial address since it's specific to Company, but for
    now that can cover things like government agencies, too.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MUG.WorkingAddress
    class_class_curie: ClassVar[str] = "mug:WorkingAddress"
    class_name: ClassVar[str] = "WorkingAddress"
    class_model_uri: ClassVar[URIRef] = MUG.WorkingAddress

    id: Union[str, WorkingAddressId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkingAddressId):
            self.id = WorkingAddressId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Person(GeneratedThing):
    """
    General class for people.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MUG.Person
    class_class_curie: ClassVar[str] = "mug:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = MUG.Person

    id: Union[str, PersonId] = None
    full_name: Optional[Union[str, FullNameId]] = None
    home_address: Optional[Union[Union[str, ResidentialAddressId], List[Union[str, ResidentialAddressId]]]] = empty_list()
    work_address: Optional[Union[Union[str, WorkingAddressId], List[Union[str, WorkingAddressId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.full_name is not None and not isinstance(self.full_name, FullNameId):
            self.full_name = FullNameId(self.full_name)

        if not isinstance(self.home_address, list):
            self.home_address = [self.home_address] if self.home_address is not None else []
        self.home_address = [v if isinstance(v, ResidentialAddressId) else ResidentialAddressId(v) for v in self.home_address]

        if not isinstance(self.work_address, list):
            self.work_address = [self.work_address] if self.work_address is not None else []
        self.work_address = [v if isinstance(v, WorkingAddressId) else WorkingAddressId(v) for v in self.work_address]

        super().__post_init__(**kwargs)


@dataclass
class FullName(GeneratedThing):
    """
    All parts of a name.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MUG.FullName
    class_class_curie: ClassVar[str] = "mug:FullName"
    class_name: ClassVar[str] = "FullName"
    class_model_uri: ClassVar[URIRef] = MUG.FullName

    id: Union[str, FullNameId] = None
    given_name: Optional[Union[str, List[str]]] = empty_list()
    family_name: Optional[Union[str, List[str]]] = empty_list()
    other_name: Optional[Union[str, List[str]]] = empty_list()
    preferred_name: Optional[Union[str, List[str]]] = empty_list()
    title: Optional[Union[str, List[str]]] = empty_list()
    suffix: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FullNameId):
            self.id = FullNameId(self.id)

        if not isinstance(self.given_name, list):
            self.given_name = [self.given_name] if self.given_name is not None else []
        self.given_name = [v if isinstance(v, str) else str(v) for v in self.given_name]

        if not isinstance(self.family_name, list):
            self.family_name = [self.family_name] if self.family_name is not None else []
        self.family_name = [v if isinstance(v, str) else str(v) for v in self.family_name]

        if not isinstance(self.other_name, list):
            self.other_name = [self.other_name] if self.other_name is not None else []
        self.other_name = [v if isinstance(v, str) else str(v) for v in self.other_name]

        if not isinstance(self.preferred_name, list):
            self.preferred_name = [self.preferred_name] if self.preferred_name is not None else []
        self.preferred_name = [v if isinstance(v, str) else str(v) for v in self.preferred_name]

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if not isinstance(self.suffix, list):
            self.suffix = [self.suffix] if self.suffix is not None else []
        self.suffix = [v if isinstance(v, str) else str(v) for v in self.suffix]

        super().__post_init__(**kwargs)


@dataclass
class Company(GeneratedThing):
    """
    A corporate entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MUG.Company
    class_class_curie: ClassVar[str] = "mug:Company"
    class_name: ClassVar[str] = "Company"
    class_model_uri: ClassVar[URIRef] = MUG.Company

    id: Union[str, CompanyId] = None
    company_name: Optional[str] = None
    work_address: Optional[Union[Union[str, WorkingAddressId], List[Union[str, WorkingAddressId]]]] = empty_list()
    industry: Optional[str] = None
    slogan: Optional[str] = None
    logo_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompanyId):
            self.id = CompanyId(self.id)

        if self.company_name is not None and not isinstance(self.company_name, str):
            self.company_name = str(self.company_name)

        if not isinstance(self.work_address, list):
            self.work_address = [self.work_address] if self.work_address is not None else []
        self.work_address = [v if isinstance(v, WorkingAddressId) else WorkingAddressId(v) for v in self.work_address]

        if self.industry is not None and not isinstance(self.industry, str):
            self.industry = str(self.industry)

        if self.slogan is not None and not isinstance(self.slogan, str):
            self.slogan = str(self.slogan)

        if self.logo_description is not None and not isinstance(self.logo_description, str):
            self.logo_description = str(self.logo_description)

        super().__post_init__(**kwargs)


@dataclass
class GeneratedThingCollection(YAMLRoot):
    """
    A holder for GeneratedThing objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MUG.GeneratedThingCollection
    class_class_curie: ClassVar[str] = "mug:GeneratedThingCollection"
    class_name: ClassVar[str] = "GeneratedThingCollection"
    class_model_uri: ClassVar[URIRef] = MUG.GeneratedThingCollection

    entries: Optional[Union[Dict[Union[str, GeneratedThingId], Union[dict, GeneratedThing]], List[Union[dict, GeneratedThing]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=GeneratedThing, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MUG.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MUG.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MUG.description, domain=None, range=Optional[str])

slots.addressee = Slot(uri=MUG.addressee, name="addressee", curie=MUG.curie('addressee'),
                   model_uri=MUG.addressee, domain=None, range=Optional[str])

slots.address_number = Slot(uri=MUG.address_number, name="address_number", curie=MUG.curie('address_number'),
                   model_uri=MUG.address_number, domain=None, range=Optional[Union[str, List[str]]])

slots.street = Slot(uri=MUG.street, name="street", curie=MUG.curie('street'),
                   model_uri=MUG.street, domain=None, range=Optional[Union[str, List[str]]])

slots.locality = Slot(uri=MUG.locality, name="locality", curie=MUG.curie('locality'),
                   model_uri=MUG.locality, domain=None, range=Optional[Union[str, List[str]]])

slots.full_name = Slot(uri=MUG.full_name, name="full_name", curie=MUG.curie('full_name'),
                   model_uri=MUG.full_name, domain=None, range=Optional[Union[str, FullNameId]])

slots.given_name = Slot(uri=MUG.given_name, name="given_name", curie=MUG.curie('given_name'),
                   model_uri=MUG.given_name, domain=None, range=Optional[Union[str, List[str]]])

slots.family_name = Slot(uri=MUG.family_name, name="family_name", curie=MUG.curie('family_name'),
                   model_uri=MUG.family_name, domain=None, range=Optional[Union[str, List[str]]])

slots.other_name = Slot(uri=MUG.other_name, name="other_name", curie=MUG.curie('other_name'),
                   model_uri=MUG.other_name, domain=None, range=Optional[Union[str, List[str]]])

slots.preferred_name = Slot(uri=MUG.preferred_name, name="preferred_name", curie=MUG.curie('preferred_name'),
                   model_uri=MUG.preferred_name, domain=None, range=Optional[Union[str, List[str]]])

slots.title = Slot(uri=MUG.title, name="title", curie=MUG.curie('title'),
                   model_uri=MUG.title, domain=None, range=Optional[Union[str, List[str]]])

slots.suffix = Slot(uri=MUG.suffix, name="suffix", curie=MUG.curie('suffix'),
                   model_uri=MUG.suffix, domain=None, range=Optional[Union[str, List[str]]])

slots.home_address = Slot(uri=MUG.home_address, name="home_address", curie=MUG.curie('home_address'),
                   model_uri=MUG.home_address, domain=None, range=Optional[Union[Union[str, ResidentialAddressId], List[Union[str, ResidentialAddressId]]]])

slots.work_address = Slot(uri=MUG.work_address, name="work_address", curie=MUG.curie('work_address'),
                   model_uri=MUG.work_address, domain=None, range=Optional[Union[Union[str, WorkingAddressId], List[Union[str, WorkingAddressId]]]])

slots.company_name = Slot(uri=MUG.company_name, name="company_name", curie=MUG.curie('company_name'),
                   model_uri=MUG.company_name, domain=None, range=Optional[str])

slots.industry = Slot(uri=MUG.industry, name="industry", curie=MUG.curie('industry'),
                   model_uri=MUG.industry, domain=None, range=Optional[str])

slots.slogan = Slot(uri=MUG.slogan, name="slogan", curie=MUG.curie('slogan'),
                   model_uri=MUG.slogan, domain=None, range=Optional[str])

slots.logo_description = Slot(uri=MUG.logo_description, name="logo_description", curie=MUG.curie('logo_description'),
                   model_uri=MUG.logo_description, domain=None, range=Optional[str])

slots.generatedThingCollection__entries = Slot(uri=MUG.entries, name="generatedThingCollection__entries", curie=MUG.curie('entries'),
                   model_uri=MUG.generatedThingCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, GeneratedThingId], Union[dict, GeneratedThing]], List[Union[dict, GeneratedThing]]]])
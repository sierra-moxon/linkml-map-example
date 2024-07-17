# Auto generated from linkml_map_example.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-07-17T11:02:45
# Schema: linkml-map-example
#
# id: https://w3id.org/sierra-moxon/linkml-map-example
# description: An example repo showing the usage and application of linkml-map
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
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
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_MAP_EXAMPLE = CurieNamespace('linkml_map_example', 'https://w3id.org/sierra-moxon/linkml-map-example/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LINKML_MAP_EXAMPLE


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class PersonId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = LINKML_MAP_EXAMPLE.NamedThing

    id: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    Represents a Sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_MAP_EXAMPLE["Person"]
    class_class_curie: ClassVar[str] = "linkml_map_example:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = LINKML_MAP_EXAMPLE.Person

    id: Union[str, PersonId] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        super().__post_init__(**kwargs)


@dataclass
class PersonCollection(YAMLRoot):
    """
    A holder for Sample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_MAP_EXAMPLE["PersonCollection"]
    class_class_curie: ClassVar[str] = "linkml_map_example:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = LINKML_MAP_EXAMPLE.PersonCollection

    entries: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Person, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=LINKML_MAP_EXAMPLE.id, domain=None, range=URIRef)

slots.first_name = Slot(uri=LINKML_MAP_EXAMPLE.first_name, name="first_name", curie=LINKML_MAP_EXAMPLE.curie('first_name'),
                   model_uri=LINKML_MAP_EXAMPLE.first_name, domain=Person, range=Optional[str])

slots.last_name = Slot(uri=LINKML_MAP_EXAMPLE.last_name, name="last_name", curie=LINKML_MAP_EXAMPLE.curie('last_name'),
                   model_uri=LINKML_MAP_EXAMPLE.last_name, domain=Person, range=Optional[str])

slots.entries = Slot(uri=LINKML_MAP_EXAMPLE.entries, name="entries", curie=LINKML_MAP_EXAMPLE.curie('entries'),
                   model_uri=LINKML_MAP_EXAMPLE.entries, domain=PersonCollection, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.personCollection__entries = Slot(uri=LINKML_MAP_EXAMPLE.entries, name="personCollection__entries", curie=LINKML_MAP_EXAMPLE.curie('entries'),
                   model_uri=LINKML_MAP_EXAMPLE.personCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])
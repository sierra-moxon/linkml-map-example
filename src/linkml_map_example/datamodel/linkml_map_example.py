# Auto generated from linkml_map_example.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-07-29T17:24:11
# Schema: cmdr
#
# id: https://w3id.org/linkml/cmdr
# description: Core Model for Data Research (Tentative)
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
from linkml_runtime.linkml_model.types import Boolean, Datetime, Decimal, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
OBI = CurieNamespace('OBI', 'http://example.org/UNKNOWN/OBI/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BDCHM = CurieNamespace('bdchm', 'https://w3id.org/nhlbidatastage/bdchm/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
CMDR = CurieNamespace('cmdr', 'https://w3id.org/linkml/cmdr/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CMDR


# Types

# Class references
class InvestigationId(URIorCURIE):
    pass


class MaterialEntityId(URIorCURIE):
    pass


class ParticipationId(URIorCURIE):
    pass


class ProcessId(URIorCURIE):
    pass


class MaterialProcessingId(ProcessId):
    pass


class SpecimenCollectionProcessId(ProcessId):
    pass


class SubjectId(URIorCURIE):
    pass


class PersonId(SubjectId):
    pass


class ResearchStudyId(InvestigationId):
    pass


@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMDR["Container"]
    class_class_curie: ClassVar[str] = "cmdr:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = CMDR.Container

    materials: Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]] = empty_dict()
    participations: Optional[Union[Dict[Union[str, ParticipationId], Union[dict, "Participation"]], List[Union[dict, "Participation"]]]] = empty_dict()
    material_processings: Optional[Union[Dict[Union[str, MaterialProcessingId], Union[dict, "MaterialProcessing"]], List[Union[dict, "MaterialProcessing"]]]] = empty_dict()
    specimen_collection_processes: Optional[Union[Dict[Union[str, SpecimenCollectionProcessId], Union[dict, "SpecimenCollectionProcess"]], List[Union[dict, "SpecimenCollectionProcess"]]]] = empty_dict()
    investigations: Optional[Union[Dict[Union[str, InvestigationId], Union[dict, "Investigation"]], List[Union[dict, "Investigation"]]]] = empty_dict()
    subjects: Optional[Union[Dict[Union[str, SubjectId], Union[dict, "Subject"]], List[Union[dict, "Subject"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="materials", slot_type=MaterialEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="participations", slot_type=Participation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="material_processings", slot_type=MaterialProcessing, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="specimen_collection_processes", slot_type=SpecimenCollectionProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="investigations", slot_type=Investigation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="subjects", slot_type=Subject, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


class DataObject(YAMLRoot):
    """
    A DataFile Associated with a Subject or Investigation or MaterialEntity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMDR["DataObject"]
    class_class_curie: ClassVar[str] = "cmdr:DataObject"
    class_name: ClassVar[str] = "DataObject"
    class_model_uri: ClassVar[URIRef] = CMDR.DataObject


@dataclass
class Investigation(YAMLRoot):
    """
    General information about the Investigation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMDR["Investigation"]
    class_class_curie: ClassVar[str] = "cmdr:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = CMDR.Investigation

    id: Union[str, InvestigationId] = None
    name: Optional[str] = None
    part_of: Optional[Union[str, InvestigationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigationId):
            self.id = InvestigationId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.part_of is not None and not isinstance(self.part_of, InvestigationId):
            self.part_of = InvestigationId(self.part_of)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(YAMLRoot):
    """
    Physical entity that is an input our output of a process from a Subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMDR["MaterialEntity"]
    class_class_curie: ClassVar[str] = "cmdr:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = CMDR.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    name: Optional[str] = None
    used_in: Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]] = empty_list()
    source: Optional[Union[str, SubjectId]] = None
    volume: Optional[Union[dict, "Quantity"]] = None
    concentration: Optional[Union[dict, "Quantity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.used_in, list):
            self.used_in = [self.used_in] if self.used_in is not None else []
        self.used_in = [v if isinstance(v, InvestigationId) else InvestigationId(v) for v in self.used_in]

        if self.source is not None and not isinstance(self.source, SubjectId):
            self.source = SubjectId(self.source)

        if self.volume is not None and not isinstance(self.volume, Quantity):
            self.volume = Quantity(**as_dict(self.volume))

        if self.concentration is not None and not isinstance(self.concentration, Quantity):
            self.concentration = Quantity(**as_dict(self.concentration))

        super().__post_init__(**kwargs)


@dataclass
class Participation(YAMLRoot):
    """
    Subject/Study participation information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMDR["Participation"]
    class_class_curie: ClassVar[str] = "cmdr:Participation"
    class_name: ClassVar[str] = "Participation"
    class_model_uri: ClassVar[URIRef] = CMDR.Participation

    id: Union[str, ParticipationId] = None
    name: Optional[str] = None
    involved_in: Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]] = empty_list()
    includes: Optional[Union[str, SubjectId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParticipationId):
            self.id = ParticipationId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.involved_in, list):
            self.involved_in = [self.involved_in] if self.involved_in is not None else []
        self.involved_in = [v if isinstance(v, InvestigationId) else InvestigationId(v) for v in self.involved_in]

        if self.includes is not None and not isinstance(self.includes, SubjectId):
            self.includes = SubjectId(self.includes)

        super().__post_init__(**kwargs)


@dataclass
class Process(YAMLRoot):
    """
    A planned process resulting in a material or data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMDR["Process"]
    class_class_curie: ClassVar[str] = "cmdr:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = CMDR.Process

    id: Union[str, ProcessId] = None
    name: Optional[str] = None
    has_input: Optional[Union[str, List[str]]] = empty_list()
    has_output: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessId):
            self.id = ProcessId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, str) else str(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, str) else str(v) for v in self.has_output]

        super().__post_init__(**kwargs)


@dataclass
class MaterialProcessing(Process):
    """
    A planned process which results in physical changes in a specified input material
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000094"]
    class_class_curie: ClassVar[str] = "OBI:0000094"
    class_name: ClassVar[str] = "MaterialProcessing"
    class_model_uri: ClassVar[URIRef] = CMDR.MaterialProcessing

    id: Union[str, MaterialProcessingId] = None
    has_input: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()
    has_output: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingId):
            self.id = MaterialProcessingId(self.id)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_output]

        super().__post_init__(**kwargs)


@dataclass
class Quantity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMDR["Quantity"]
    class_class_curie: ClassVar[str] = "cmdr:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = CMDR.Quantity

    has_raw_value: Optional[str] = None
    has_numeric_value: Optional[float] = None
    has_unit: Optional[str] = None
    comparator: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        if self.has_numeric_value is not None and not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        if self.has_unit is not None and not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self.comparator is not None and not isinstance(self.comparator, str):
            self.comparator = str(self.comparator)

        super().__post_init__(**kwargs)


@dataclass
class SpecimenCollectionProcess(Process):
    """
    A planned process with the objective of collecting a specimen
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000659"]
    class_class_curie: ClassVar[str] = "OBI:0000659"
    class_name: ClassVar[str] = "SpecimenCollectionProcess"
    class_model_uri: ClassVar[URIRef] = CMDR.SpecimenCollectionProcess

    id: Union[str, SpecimenCollectionProcessId] = None
    has_input: Optional[str] = None
    has_output: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecimenCollectionProcessId):
            self.id = SpecimenCollectionProcessId(self.id)

        if self.has_input is not None and not isinstance(self.has_input, str):
            self.has_input = str(self.has_input)

        if self.has_output is not None and not isinstance(self.has_output, str):
            self.has_output = str(self.has_output)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, SubjectId) else SubjectId(v) for v in self.has_input]

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_output]

        super().__post_init__(**kwargs)


@dataclass
class Subject(YAMLRoot):
    """
    Demographic and clinical information about the subject
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CMDR["Subject"]
    class_class_curie: ClassVar[str] = "cmdr:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = CMDR.Subject

    id: Union[str, SubjectId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubjectId):
            self.id = SubjectId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    """
    Any resource that has its own identifier
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = CMDR.Entity

    id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Person(Subject):
    """
    Demographics and other administrative information about an individual or animal receiving care or other
    health-related services.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Person"]
    class_class_curie: ClassVar[str] = "bdchm:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = CMDR.Person

    id: Union[str, PersonId] = None
    identity: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    species: Optional[Union[str, "CellularOrganismSpeciesEnum"]] = None
    breed: Optional[Union[str, "VertebrateBreedEnum"]] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    ethnicity: Optional[Union[str, "EthnicityEnum"]] = None
    race: Optional[Union[str, "RaceEnum"]] = None
    year_of_birth: Optional[int] = None
    vital_status: Optional[Union[str, "VitalStatusEnum"]] = None
    age_at_death: Optional[int] = None
    year_of_death: Optional[int] = None
    cause_of_death: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        self._normalize_inlined_as_dict(slot_name="identity", slot_type=Identifier, key_name="value", keyed=False)

        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.ethnicity is not None and not isinstance(self.ethnicity, EthnicityEnum):
            self.ethnicity = EthnicityEnum(self.ethnicity)

        if self.race is not None and not isinstance(self.race, RaceEnum):
            self.race = RaceEnum(self.race)

        if self.year_of_birth is not None and not isinstance(self.year_of_birth, int):
            self.year_of_birth = int(self.year_of_birth)

        if self.vital_status is not None and not isinstance(self.vital_status, VitalStatusEnum):
            self.vital_status = VitalStatusEnum(self.vital_status)

        if self.age_at_death is not None and not isinstance(self.age_at_death, int):
            self.age_at_death = int(self.age_at_death)

        if self.year_of_death is not None and not isinstance(self.year_of_death, int):
            self.year_of_death = int(self.year_of_death)

        if self.cause_of_death is not None and not isinstance(self.cause_of_death, str):
            self.cause_of_death = str(self.cause_of_death)

        super().__post_init__(**kwargs)


@dataclass
class Participant(Entity):
    """
    A Participant is the entity of interest in a research study, typically a human being or an animal, but can also be
    a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a
    particular person to protect the subject’s privacy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Participant"]
    class_class_curie: ClassVar[str] = "bdchm:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = CMDR.Participant

    associated_person: Optional[Union[str, PersonId]] = None
    identity: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    description: Optional[str] = None
    member_of_research_study: Optional[Union[str, ResearchStudyId]] = None
    age_at_enrollment: Optional[int] = None
    index_timepoint: Optional[str] = None
    originating_site: Optional[Union[dict, "Organization"]] = None
    study_arm: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.associated_person is not None and not isinstance(self.associated_person, PersonId):
            self.associated_person = PersonId(self.associated_person)

        self._normalize_inlined_as_dict(slot_name="identity", slot_type=Identifier, key_name="value", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.member_of_research_study is not None and not isinstance(self.member_of_research_study, ResearchStudyId):
            self.member_of_research_study = ResearchStudyId(self.member_of_research_study)

        if self.age_at_enrollment is not None and not isinstance(self.age_at_enrollment, int):
            self.age_at_enrollment = int(self.age_at_enrollment)

        if self.index_timepoint is not None and not isinstance(self.index_timepoint, str):
            self.index_timepoint = str(self.index_timepoint)

        if self.originating_site is not None and not isinstance(self.originating_site, Organization):
            self.originating_site = Organization(**as_dict(self.originating_site))

        if not isinstance(self.study_arm, list):
            self.study_arm = [self.study_arm] if self.study_arm is not None else []
        self.study_arm = [v if isinstance(v, str) else str(v) for v in self.study_arm]

        super().__post_init__(**kwargs)


@dataclass
class ResearchStudy(Investigation):
    """
    A process where a researcher or organization plans and then executes a series of steps intended to increase the
    field of healthcare-related knowledge. This includes studies of safety, efficacy, comparative effectiveness and
    other information about medications, devices, therapies and other interventional and investigative techniques. A
    ResearchStudy involves the gathering of information about human or animal subjects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["ResearchStudy"]
    class_class_curie: ClassVar[str] = "bdchm:ResearchStudy"
    class_name: ClassVar[str] = "ResearchStudy"
    class_model_uri: ClassVar[URIRef] = CMDR.ResearchStudy

    id: Union[str, ResearchStudyId] = None
    identity: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    name: Optional[str] = None
    name_shortened: Optional[str] = None
    description: Optional[str] = None
    description_shortened: Optional[str] = None
    sponsor: Optional[str] = None
    date_started: Optional[Union[dict, "TimePoint"]] = None
    date_ended: Optional[Union[dict, "TimePoint"]] = None
    url: Optional[Union[str, URIorCURIE]] = None
    part_of: Optional[Union[str, ResearchStudyId]] = None
    research_project_type: Optional[str] = None
    associated_timepoint: Optional[Union[Union[dict, "TimePoint"], List[Union[dict, "TimePoint"]]]] = empty_list()
    principal_investigator: Optional[Union[str, List[str]]] = empty_list()
    consent_code: Optional[Union[Union[str, "DataUseEnum"], List[Union[str, "DataUseEnum"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResearchStudyId):
            self.id = ResearchStudyId(self.id)

        self._normalize_inlined_as_dict(slot_name="identity", slot_type=Identifier, key_name="value", keyed=False)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.name_shortened is not None and not isinstance(self.name_shortened, str):
            self.name_shortened = str(self.name_shortened)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.description_shortened is not None and not isinstance(self.description_shortened, str):
            self.description_shortened = str(self.description_shortened)

        if self.sponsor is not None and not isinstance(self.sponsor, str):
            self.sponsor = str(self.sponsor)

        if self.date_started is not None and not isinstance(self.date_started, TimePoint):
            self.date_started = TimePoint(**as_dict(self.date_started))

        if self.date_ended is not None and not isinstance(self.date_ended, TimePoint):
            self.date_ended = TimePoint(**as_dict(self.date_ended))

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.part_of is not None and not isinstance(self.part_of, ResearchStudyId):
            self.part_of = ResearchStudyId(self.part_of)

        if self.research_project_type is not None and not isinstance(self.research_project_type, str):
            self.research_project_type = str(self.research_project_type)

        if not isinstance(self.associated_timepoint, list):
            self.associated_timepoint = [self.associated_timepoint] if self.associated_timepoint is not None else []
        self.associated_timepoint = [v if isinstance(v, TimePoint) else TimePoint(**as_dict(v)) for v in self.associated_timepoint]

        if not isinstance(self.principal_investigator, list):
            self.principal_investigator = [self.principal_investigator] if self.principal_investigator is not None else []
        self.principal_investigator = [v if isinstance(v, str) else str(v) for v in self.principal_investigator]

        if not isinstance(self.consent_code, list):
            self.consent_code = [self.consent_code] if self.consent_code is not None else []
        self.consent_code = [v if isinstance(v, DataUseEnum) else DataUseEnum(v) for v in self.consent_code]

        super().__post_init__(**kwargs)


@dataclass
class Visit(Entity):
    """
    Events where Persons engage with the healthcare system for a duration of time. They are often also called
    “Encounters”. Visits are defined by a configuration of circumstances under which they occur, such as (i) whether
    the patient comes to a healthcare institution, the other way around, or the interaction is remote, (ii) whether
    and what kind of trained medical staff is delivering the service during the Visit, and (iii) whether the Visit is
    transient or for a longer period involving a stay in bed. (OMOP)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Visit"]
    class_class_curie: ClassVar[str] = "bdchm:Visit"
    class_name: ClassVar[str] = "Visit"
    class_model_uri: ClassVar[URIRef] = CMDR.Visit

    visit_category: Optional[Union[str, "VisitCategoryEnum"]] = None
    age_at_visit_start: Optional[int] = None
    age_at_visit_end: Optional[int] = None
    visit_provenance: Optional[Union[str, "VisitProvenanceEnum"]] = None
    associated_participant: Optional[Union[dict, Participant]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.visit_category is not None and not isinstance(self.visit_category, VisitCategoryEnum):
            self.visit_category = VisitCategoryEnum(self.visit_category)

        if self.age_at_visit_start is not None and not isinstance(self.age_at_visit_start, int):
            self.age_at_visit_start = int(self.age_at_visit_start)

        if self.age_at_visit_end is not None and not isinstance(self.age_at_visit_end, int):
            self.age_at_visit_end = int(self.age_at_visit_end)

        if self.visit_provenance is not None and not isinstance(self.visit_provenance, VisitProvenanceEnum):
            self.visit_provenance = VisitProvenanceEnum(self.visit_provenance)

        if self.associated_participant is not None and not isinstance(self.associated_participant, Participant):
            self.associated_participant = Participant(**as_dict(self.associated_participant))

        super().__post_init__(**kwargs)


@dataclass
class Organization(Entity):
    """
    A grouping of people or organizations with a common purpose such as a data coordinating center, an university, or
    an institute within a university.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Organization"]
    class_class_curie: ClassVar[str] = "bdchm:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = CMDR.Organization

    identity: Optional[Union[Union[dict, "Identifier"], List[Union[dict, "Identifier"]]]] = empty_list()
    name: Optional[str] = None
    alias: Optional[str] = None
    organization_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="identity", slot_type=Identifier, key_name="value", keyed=False)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.alias is not None and not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.organization_type is not None and not isinstance(self.organization_type, str):
            self.organization_type = str(self.organization_type)

        super().__post_init__(**kwargs)


@dataclass
class TimePoint(Entity):
    """
    A structured representation of a single point in time that allows direct/explicit declaration as a dateTime,
    specification in terms of offset from a defined index, or description of an event type as a proxy for the time
    point when it occurred.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["TimePoint"]
    class_class_curie: ClassVar[str] = "bdchm:TimePoint"
    class_name: ClassVar[str] = "TimePoint"
    class_model_uri: ClassVar[URIRef] = CMDR.TimePoint

    date_time: Optional[Union[str, XSDDateTime]] = None
    index_time_point: Optional[Union[dict, "TimePoint"]] = None
    offset_from_index: Optional[int] = None
    event_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.date_time is not None and not isinstance(self.date_time, XSDDateTime):
            self.date_time = XSDDateTime(self.date_time)

        if self.index_time_point is not None and not isinstance(self.index_time_point, TimePoint):
            self.index_time_point = TimePoint(**as_dict(self.index_time_point))

        if self.offset_from_index is not None and not isinstance(self.offset_from_index, int):
            self.offset_from_index = int(self.offset_from_index)

        if self.event_type is not None and not isinstance(self.event_type, str):
            self.event_type = str(self.event_type)

        super().__post_init__(**kwargs)


@dataclass
class TimePeriod(YAMLRoot):
    """
    A period of time between a start and end time point.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["TimePeriod"]
    class_class_curie: ClassVar[str] = "bdchm:TimePeriod"
    class_name: ClassVar[str] = "TimePeriod"
    class_model_uri: ClassVar[URIRef] = CMDR.TimePeriod

    period_start: Optional[Union[dict, TimePoint]] = None
    period_end: Optional[Union[dict, TimePoint]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.period_start is not None and not isinstance(self.period_start, TimePoint):
            self.period_start = TimePoint(**as_dict(self.period_start))

        if self.period_end is not None and not isinstance(self.period_end, TimePoint):
            self.period_end = TimePoint(**as_dict(self.period_end))

        super().__post_init__(**kwargs)


@dataclass
class Identifier(YAMLRoot):
    """
    An Identifier is associated with a unique object or entity within a given system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Identifier"]
    class_class_curie: ClassVar[str] = "bdchm:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = CMDR.Identifier

    value: str = None
    system: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.system is not None and not isinstance(self.system, str):
            self.system = str(self.system)

        super().__post_init__(**kwargs)


@dataclass
class ResearchStudyCollection(YAMLRoot):
    """
    A holder for ResearchStudy objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["ResearchStudyCollection"]
    class_class_curie: ClassVar[str] = "bdchm:ResearchStudyCollection"
    class_name: ClassVar[str] = "ResearchStudyCollection"
    class_model_uri: ClassVar[URIRef] = CMDR.ResearchStudyCollection

    entries: Optional[Union[Dict[Union[str, ResearchStudyId], Union[dict, ResearchStudy]], List[Union[dict, ResearchStudy]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=ResearchStudy, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Questionnaire(Entity):
    """
    A Questionnaire is an organized collection of questions intended to solicit information from patients, providers
    or other individuals involved in the healthcare domain. They may be simple flat lists of questions or can be
    hierarchically organized in groups and sub-groups, each containing questions. The Questionnaire defines the
    questions to be asked, how they are ordered and grouped, any intervening instructional text and what the
    constraints are on the allowed answers. The results of a Questionnaire can be communicated using the
    QuestionnaireResponse. (FHIR)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Questionnaire"]
    class_class_curie: ClassVar[str] = "bdchm:Questionnaire"
    class_name: ClassVar[str] = "Questionnaire"
    class_model_uri: ClassVar[URIRef] = CMDR.Questionnaire

    items: Union[Union[dict, "QuestionnaireItem"], List[Union[dict, "QuestionnaireItem"]]] = None
    identity: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[Union[str, URIorCURIE]] = None
    version: Optional[str] = None
    publisher: Optional[str] = None
    copyright: Optional[str] = None
    copyright_label: Optional[str] = None
    language: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.items):
            self.MissingRequiredField("items")
        if not isinstance(self.items, list):
            self.items = [self.items] if self.items is not None else []
        self.items = [v if isinstance(v, QuestionnaireItem) else QuestionnaireItem(**as_dict(v)) for v in self.items]

        self._normalize_inlined_as_dict(slot_name="identity", slot_type=Identifier, key_name="value", keyed=False)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.copyright is not None and not isinstance(self.copyright, str):
            self.copyright = str(self.copyright)

        if self.copyright_label is not None and not isinstance(self.copyright_label, str):
            self.copyright_label = str(self.copyright_label)

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, str) else str(v) for v in self.language]

        super().__post_init__(**kwargs)


@dataclass
class QuestionnaireItem(Entity):
    """
    QuestionnaireItem defines a question or section within the Questionnaire
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["QuestionnaireItem"]
    class_class_curie: ClassVar[str] = "bdchm:QuestionnaireItem"
    class_name: ClassVar[str] = "QuestionnaireItem"
    class_model_uri: ClassVar[URIRef] = CMDR.QuestionnaireItem

    identity: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    text: Optional[str] = None
    code: Optional[str] = None
    part_of: Optional[Union[dict, "QuestionnaireItem"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="identity", slot_type=Identifier, key_name="value", keyed=False)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.part_of is not None and not isinstance(self.part_of, QuestionnaireItem):
            self.part_of = QuestionnaireItem(**as_dict(self.part_of))

        super().__post_init__(**kwargs)


@dataclass
class QuestionnaireResponse(Entity):
    """
    QuestionnaireResponse provides a complete or partial list of answers to a set of questions filled when responding
    to a questionnaire. (FHIR)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["QuestionnaireResponse"]
    class_class_curie: ClassVar[str] = "bdchm:QuestionnaireResponse"
    class_name: ClassVar[str] = "QuestionnaireResponse"
    class_model_uri: ClassVar[URIRef] = CMDR.QuestionnaireResponse

    items: Union[Union[dict, "QuestionnaireResponseItem"], List[Union[dict, "QuestionnaireResponseItem"]]] = None
    age_at_response: Optional[int] = None
    associated_visit: Optional[Union[dict, Visit]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.items):
            self.MissingRequiredField("items")
        self._normalize_inlined_as_dict(slot_name="items", slot_type=QuestionnaireResponseItem, key_name="response_value", keyed=False)

        if self.age_at_response is not None and not isinstance(self.age_at_response, int):
            self.age_at_response = int(self.age_at_response)

        if self.associated_visit is not None and not isinstance(self.associated_visit, Visit):
            self.associated_visit = Visit(**as_dict(self.associated_visit))

        super().__post_init__(**kwargs)


@dataclass
class QuestionnaireResponseItem(YAMLRoot):
    """
    QuestionnaireResponseItem provides a complete or partial list of answers to a set of questions filled when
    responding to a questionnaire. (FHIR)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["QuestionnaireResponseItem"]
    class_class_curie: ClassVar[str] = "bdchm:QuestionnaireResponseItem"
    class_name: ClassVar[str] = "QuestionnaireResponseItem"
    class_model_uri: ClassVar[URIRef] = CMDR.QuestionnaireResponseItem

    response_value: Union[dict, "QuestionnaireResponseValue"] = None
    has_questionnaire_item: Optional[Union[dict, QuestionnaireItem]] = None
    text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.response_value):
            self.MissingRequiredField("response_value")
        if not isinstance(self.response_value, QuestionnaireResponseValue):
            self.response_value = QuestionnaireResponseValue(**as_dict(self.response_value))

        if self.has_questionnaire_item is not None and not isinstance(self.has_questionnaire_item, QuestionnaireItem):
            self.has_questionnaire_item = QuestionnaireItem(**as_dict(self.has_questionnaire_item))

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass
class QuestionnaireResponseValue(YAMLRoot):
    """
    Single-valued answer to the question. (FHIR)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["QuestionnaireResponseValue"]
    class_class_curie: ClassVar[str] = "bdchm:QuestionnaireResponseValue"
    class_name: ClassVar[str] = "QuestionnaireResponseValue"
    class_model_uri: ClassVar[URIRef] = CMDR.QuestionnaireResponseValue

    value: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        self.type = str(self.class_name)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)
        self.unknown_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class QuestionnaireResponseValueDecimal(QuestionnaireResponseValue):
    """
    Single-valued decimal answer to the question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["QuestionnaireResponseValueDecimal"]
    class_class_curie: ClassVar[str] = "bdchm:QuestionnaireResponseValueDecimal"
    class_name: ClassVar[str] = "QuestionnaireResponseValueDecimal"
    class_model_uri: ClassVar[URIRef] = CMDR.QuestionnaireResponseValueDecimal

    value: Decimal = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Decimal):
            self.value = Decimal(self.value)

        super().__post_init__(**kwargs)
        self.unknown_type = str(self.class_name)


@dataclass
class QuestionnaireResponseValueBoolean(QuestionnaireResponseValue):
    """
    Single-valued boolean answer to the question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["QuestionnaireResponseValueBoolean"]
    class_class_curie: ClassVar[str] = "bdchm:QuestionnaireResponseValueBoolean"
    class_name: ClassVar[str] = "QuestionnaireResponseValueBoolean"
    class_model_uri: ClassVar[URIRef] = CMDR.QuestionnaireResponseValueBoolean

    value: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Bool):
            self.value = Bool(self.value)

        super().__post_init__(**kwargs)
        self.unknown_type = str(self.class_name)


@dataclass
class QuestionnaireResponseValueString(QuestionnaireResponseValue):
    """
    Single-valued string answer to the question
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["QuestionnaireResponseValueString"]
    class_class_curie: ClassVar[str] = "bdchm:QuestionnaireResponseValueString"
    class_name: ClassVar[str] = "QuestionnaireResponseValueString"
    class_model_uri: ClassVar[URIRef] = CMDR.QuestionnaireResponseValueString

    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)
        self.unknown_type = str(self.class_name)


@dataclass
class Condition(Entity):
    """
    Conditions are records of a Person suggesting the presence of a disease or medical condition stated as a
    diagnosis, a sign or a symptom, which is either observed by a Provider or reported by the patient. Conditions are
    recorded in different sources and levels of standardization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BDCHM["Condition"]
    class_class_curie: ClassVar[str] = "bdchm:Condition"
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = CMDR.Condition

    identity: Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]] = empty_list()
    condition_concept: Optional[Union[str, "ConditionConceptEnum"]] = None
    age_at_condition_start: Optional[int] = None
    age_at_condition_end: Optional[int] = None
    condition_provenance: Optional[Union[str, "ConditionProvenanceEnum"]] = None
    relationship_to_participant: Optional[str] = None
    associated_participant: Optional[Union[dict, Participant]] = None
    associated_visit: Optional[Union[dict, Visit]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="identity", slot_type=Identifier, key_name="value", keyed=False)

        if self.age_at_condition_start is not None and not isinstance(self.age_at_condition_start, int):
            self.age_at_condition_start = int(self.age_at_condition_start)

        if self.age_at_condition_end is not None and not isinstance(self.age_at_condition_end, int):
            self.age_at_condition_end = int(self.age_at_condition_end)

        if self.condition_provenance is not None and not isinstance(self.condition_provenance, ConditionProvenanceEnum):
            self.condition_provenance = ConditionProvenanceEnum(self.condition_provenance)

        if self.relationship_to_participant is not None and not isinstance(self.relationship_to_participant, str):
            self.relationship_to_participant = str(self.relationship_to_participant)

        if self.associated_participant is not None and not isinstance(self.associated_participant, Participant):
            self.associated_participant = Participant(**as_dict(self.associated_participant))

        if self.associated_visit is not None and not isinstance(self.associated_visit, Visit):
            self.associated_visit = Visit(**as_dict(self.associated_visit))

        super().__post_init__(**kwargs)


# Enumerations
class DataUseEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values drawn from the Data Use Ontology (DUO). The DUO is an ontology which
    represent data use conditions.
    """
    GRU = PermissibleValue(
        text="GRU",
        description="""This data use permission indicates that use is allowed for general research use for any research purpose. This includes but is not limited to: health/medical/biomedical purposes, fundamental biology research, the study of population origins or ancestry, statistical methods and algorithms development, and social-sciences research.""",
        meaning=DUO["0000042"])
    HMB = PermissibleValue(
        text="HMB",
        description="""This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry.""",
        meaning=DUO["0000006"])
    DS = PermissibleValue(
        text="DS",
        description="""This data use permission indicates that use is allowed provided it is related to the specified disease. This term should be coupled with a term describing a disease from an ontology to specify the disease the restriction applies to. DUO recommends MONDO be used, to provide the basis for automated evaluation. For more information see https://github.com/EBISPOT/DUO/blob/master/MONDO_Overview.md Other resources, such as the Disease Ontology, HPO, SNOMED-CT or others, can also be used. When those other resources are being used, this may require an extra mapping step to leverage automated matching algorithms.""",
        meaning=DUO["0000007"])
    NPUNCU = PermissibleValue(
        text="NPUNCU",
        description="""This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use.""",
        meaning=DUO["0000018"])
    IRB = PermissibleValue(
        text="IRB",
        description="""This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval.""",
        meaning=DUO["0000021"])

    _defn = EnumDefinition(
        name="DataUseEnum",
        description="""A constrained set of enumerative values drawn from the Data Use Ontology (DUO). The DUO is an ontology which represent data use conditions.""",
    )

class EthnicityEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the United States Office of Management and Budget (OMB) values
    for ethnicity.
    """
    HISPANIC_OR_LATINO = PermissibleValue(
        text="HISPANIC_OR_LATINO",
        description="""A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race. The term, \"Spanish origin\" can be used in addition to \"Hispanic or Latino\". (OMB)""",
        meaning=OMOP["38003563"])
    NOT_HISPANIC_OR_LATINO = PermissibleValue(
        text="NOT_HISPANIC_OR_LATINO",
        description="""A person not of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race.""",
        meaning=OMOP["38003564"])

    _defn = EnumDefinition(
        name="EthnicityEnum",
        description="""A constrained set of enumerative values containing the United States Office of Management and Budget (OMB) values for ethnicity.""",
    )

class RaceEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the United States Office of Management and Budget (OMB) values
    for race.
    """
    AMERICAN_INDIAN_OR_ALASKA_NATIVE = PermissibleValue(
        text="AMERICAN_INDIAN_OR_ALASKA_NATIVE",
        description="""A person having origins in any of the original peoples of North and South America (including Central America) and who maintains tribal affiliation or community attachment. (OMB)""",
        meaning=OMOP["8657"])
    ASIAN = PermissibleValue(
        text="ASIAN",
        description="""A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent, including for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam. (OMB)""",
        meaning=OMOP["8515"])
    BLACK_OR_AFRICAN_AMERICAN = PermissibleValue(
        text="BLACK_OR_AFRICAN_AMERICAN",
        description="""A person having origins in any of the Black racial groups of Africa. Terms such as \"Haitian\" or \"Negro\" can be used in addition to \"Black or African American\". (OMB)""",
        meaning=OMOP["8516"])
    NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER = PermissibleValue(
        text="NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER",
        description="""Denotes a person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands. The term covers particularly people who identify themselves as part-Hawaiian, Native Hawaiian, Guamanian or Chamorro, Carolinian, Samoan, Chuukese (Trukese), Fijian, Kosraean, Melanesian, Micronesian, Northern Mariana Islander, Palauan, Papua New Guinean, Pohnpeian, Polynesian, Solomon Islander, Tahitian, Tokelauan, Tongan, Yapese, or Pacific Islander, not specified.""",
        meaning=OMOP["8557"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Not known, not observed, not recorded, or refused.",
        meaning=OMOP["8552"])
    WHITE = PermissibleValue(
        text="WHITE",
        description="""Denotes person with European, Middle Eastern, or North African ancestral origin who identifies, or is identified, as White.""",
        meaning=OMOP["8527"])

    _defn = EnumDefinition(
        name="RaceEnum",
        description="""A constrained set of enumerative values containing the United States Office of Management and Budget (OMB) values for race.""",
    )

class SexEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the OMOP values for sex.
    """
    MALE = PermissibleValue(
        text="MALE",
        description="A person who belongs to the sex that normally produces sperm.",
        meaning=OMOP["8507"])
    FEMALE = PermissibleValue(
        text="FEMALE",
        description="A person who belongs to the sex that normally produces ova.",
        meaning=OMOP["8532"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Not known, not observed, not recorded, or refused.",
        meaning=OMOP["8552"])

    _defn = EnumDefinition(
        name="SexEnum",
        description="A constrained set of enumerative values containing the OMOP values for sex.",
    )

class CellularOrganismSpeciesEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the NCBITaxon values for cellular organisms.
    """
    _defn = EnumDefinition(
        name="CellularOrganismSpeciesEnum",
        description="A constrained set of enumerative values containing the NCBITaxon values for cellular organisms.",
    )

class VitalStatusEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the OMOP values for vital status.
    """
    ALIVE = PermissibleValue(
        text="ALIVE",
        description="Showing characteristics of life; displaying signs of life. (NCIt)",
        meaning=OMOP["4230556"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="The cessation of life. (NCIt)",
        meaning=OMOP["434489"])

    _defn = EnumDefinition(
        name="VitalStatusEnum",
        description="A constrained set of enumerative values containing the OMOP values for vital status.",
    )

class VertebrateBreedEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the VBO values for vertebrate breeds.
    """
    _defn = EnumDefinition(
        name="VertebrateBreedEnum",
        description="A constrained set of enumerative values containing the VBO values for vertebrate breeds.",
    )

class VisitCategoryEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the OMOP values for visit categories.
    """
    INPATIENT = PermissibleValue(
        text="INPATIENT",
        description="""Person visiting hospital, at a care stie, in bed, for duration of more than one day, with physicians and other Providers permanently available to deliver service around the clock""",
        meaning=OMOP["9201"])
    EMERGENCY_ROOM = PermissibleValue(
        text="EMERGENCY_ROOM",
        description="""Person visiting dedicated healthcare institution for treating emergencies, at a Care Site, within one day, with physicians and Providers permanently available to deliver service around the clock""",
        meaning=OMOP["9203"])
    EMERGENCY_ROOM_AND_INPATIENT = PermissibleValue(
        text="EMERGENCY_ROOM_AND_INPATIENT",
        description="""Person visiting ER followed by a subsequent Inpatient Visit, where Emergency department is part of hospital, and transition from the ER to other hospital departments is undefined""",
        meaning=OMOP["262"])
    NON_HOSPITAL_INSTITUTION = PermissibleValue(
        text="NON_HOSPITAL_INSTITUTION",
        description="""Person visiting dedicated institution for reasons of poor health, at a Care Site, long-term or permanently, with no physician but possibly other Providers permanently available to deliver service around the clock""",
        meaning=OMOP["42898160"])
    OUTPATIENT = PermissibleValue(
        text="OUTPATIENT",
        description="""Person visiting dedicated ambulatory healthcare institution, at a Care Site, within one day, without bed, with physicians or medical Providers delivering service during Visit""",
        meaning=OMOP["9202"])
    HOME = PermissibleValue(
        text="HOME",
        description="Provider visiting Person, without a Care Site, within one day, delivering service",
        meaning=OMOP["581476"])
    TELEHEALTH = PermissibleValue(
        text="TELEHEALTH",
        description="Patient engages with Provider through communication media",
        meaning=OMOP["5083"])
    PHARMACY = PermissibleValue(
        text="PHARMACY",
        description="Person visiting pharmacy for dispensing of Drug, at a Care Site, within one day",
        meaning=OMOP["581458"])
    LABORATORY = PermissibleValue(
        text="LABORATORY",
        description="""Patient visiting dedicated institution, at a Care Site, within one day, for the purpose of a Measurement.""",
        meaning=OMOP["32036"])
    AMBULANCE = PermissibleValue(
        text="AMBULANCE",
        description="""Person using transportation service for the purpose of initiating one of the other Visits, without a Care Site, within one day, potentially with Providers accompanying the Visit and delivering service""",
        meaning=OMOP["581478"])
    CASE_MANAGEMENT = PermissibleValue(
        text="CASE_MANAGEMENT",
        description="""Person interacting with healthcare system, without a Care Site, within a day, with no Providers involved, for administrative purposes""",
        meaning=OMOP["38004193"])

    _defn = EnumDefinition(
        name="VisitCategoryEnum",
        description="A constrained set of enumerative values containing the OMOP values for visit categories.",
    )

class VisitProvenanceEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the OMOP values for visit provenance.
    """
    CASE_REPORT_FORM = PermissibleValue(
        text="CASE_REPORT_FORM",
        description="Case Report Form",
        meaning=OMOP["32809"])
    CLAIM = PermissibleValue(
        text="CLAIM",
        description="Claim",
        meaning=OMOP["32810"])
    CLAIM_AUTHORIZATION = PermissibleValue(
        text="CLAIM_AUTHORIZATION",
        description="Claim authorization",
        meaning=OMOP["32811"])
    CLAIM_DISCHARGE_RECORD = PermissibleValue(
        text="CLAIM_DISCHARGE_RECORD",
        description="Claim discharge record",
        meaning=OMOP["32812"])
    CLAIM_ENROLMENT_RECORD = PermissibleValue(
        text="CLAIM_ENROLMENT_RECORD",
        description="Claim enrolment record",
        meaning=OMOP["32813"])
    COST_RECORD = PermissibleValue(
        text="COST_RECORD",
        description="Cost record",
        meaning=OMOP["32814"])
    DEATH_CERTIFICATE = PermissibleValue(
        text="DEATH_CERTIFICATE",
        description="Death Certificate",
        meaning=OMOP["32815"])
    DENTAL_CLAIM = PermissibleValue(
        text="DENTAL_CLAIM",
        description="Dental claim",
        meaning=OMOP["32816"])
    EHR = PermissibleValue(
        text="EHR",
        description="EHR",
        meaning=OMOP["32817"])
    EHR_PATHOLOGY_REPORT = PermissibleValue(
        text="EHR_PATHOLOGY_REPORT",
        description="EHR Pathology report",
        meaning=OMOP["32835"])
    EHR_ADMINISTRATION_RECORD = PermissibleValue(
        text="EHR_ADMINISTRATION_RECORD",
        description="EHR administration record",
        meaning=OMOP["32818"])
    EHR_ADMISSION_NOTE = PermissibleValue(
        text="EHR_ADMISSION_NOTE",
        description="EHR admission note",
        meaning=OMOP["32819"])
    EHR_ANCILLARY_REPORT = PermissibleValue(
        text="EHR_ANCILLARY_REPORT",
        description="EHR ancillary report",
        meaning=OMOP["32820"])
    EHR_BILLING_RECORD = PermissibleValue(
        text="EHR_BILLING_RECORD",
        description="EHR billing record",
        meaning=OMOP["32821"])
    EHR_CHIEF_COMPLAINT = PermissibleValue(
        text="EHR_CHIEF_COMPLAINT",
        description="EHR chief complaint",
        meaning=OMOP["32822"])
    EHR_DISCHARGE_RECORD = PermissibleValue(
        text="EHR_DISCHARGE_RECORD",
        description="EHR discharge record",
        meaning=OMOP["32823"])
    EHR_DISCHARGE_SUMMARY = PermissibleValue(
        text="EHR_DISCHARGE_SUMMARY",
        description="EHR discharge summary",
        meaning=OMOP["32824"])
    EHR_DISPENSING_RECORD = PermissibleValue(
        text="EHR_DISPENSING_RECORD",
        description="EHR dispensing record",
        meaning=OMOP["32825"])
    EHR_EMERGENCY_ROOM_NOTE = PermissibleValue(
        text="EHR_EMERGENCY_ROOM_NOTE",
        description="EHR emergency room note",
        meaning=OMOP["32826"])
    EHR_ENCOUNTER_RECORD = PermissibleValue(
        text="EHR_ENCOUNTER_RECORD",
        description="EHR encounter record",
        meaning=OMOP["32827"])
    EHR_EPISODE_RECORD = PermissibleValue(
        text="EHR_EPISODE_RECORD",
        description="EHR episode record",
        meaning=OMOP["32828"])
    EHR_INPATIENT_NOTE = PermissibleValue(
        text="EHR_INPATIENT_NOTE",
        description="EHR inpatient note",
        meaning=OMOP["32829"])
    EHR_MEDICATION_LIST = PermissibleValue(
        text="EHR_MEDICATION_LIST",
        description="EHR medication list",
        meaning=OMOP["32830"])
    EHR_NOTE = PermissibleValue(
        text="EHR_NOTE",
        description="EHR note",
        meaning=OMOP["32831"])
    EHR_NURSING_REPORT = PermissibleValue(
        text="EHR_NURSING_REPORT",
        description="EHR nursing report",
        meaning=OMOP["32832"])
    EHR_ORDER = PermissibleValue(
        text="EHR_ORDER",
        description="EHR order",
        meaning=OMOP["32833"])
    EHR_OUTPATIENT_NOTE = PermissibleValue(
        text="EHR_OUTPATIENT_NOTE",
        description="EHR outpatient note",
        meaning=OMOP["32834"])
    EHR_PHYSICAL_EXAMINATION = PermissibleValue(
        text="EHR_PHYSICAL_EXAMINATION",
        description="EHR physical examination",
        meaning=OMOP["32836"])
    EHR_PLANNED_DISPENSING_RECORD = PermissibleValue(
        text="EHR_PLANNED_DISPENSING_RECORD",
        description="EHR planned dispensing record",
        meaning=OMOP["32837"])
    EHR_PRESCRIPTION = PermissibleValue(
        text="EHR_PRESCRIPTION",
        description="EHR prescription",
        meaning=OMOP["32838"])
    EHR_PRESCRIPTION_ISSUE_RECORD = PermissibleValue(
        text="EHR_PRESCRIPTION_ISSUE_RECORD",
        description="EHR prescription issue record",
        meaning=OMOP["32839"])
    EHR_PROBLEM_LIST = PermissibleValue(
        text="EHR_PROBLEM_LIST",
        description="EHR problem list",
        meaning=OMOP["32840"])
    EHR_RADIOLOGY_REPORT = PermissibleValue(
        text="EHR_RADIOLOGY_REPORT",
        description="EHR radiology report",
        meaning=OMOP["32841"])
    EHR_REFERRAL_RECORD = PermissibleValue(
        text="EHR_REFERRAL_RECORD",
        description="EHR referral record",
        meaning=OMOP["32842"])
    EXTERNAL_CDM_INSTANCE = PermissibleValue(
        text="EXTERNAL_CDM_INSTANCE",
        description="External CDM instance",
        meaning=OMOP["32843"])
    FACILITY_CLAIM = PermissibleValue(
        text="FACILITY_CLAIM",
        description="Facility claim",
        meaning=OMOP["32844"])
    FACILITY_CLAIM_DETAIL = PermissibleValue(
        text="FACILITY_CLAIM_DETAIL",
        description="Facility claim detail",
        meaning=OMOP["32845"])
    FACILITY_CLAIM_HEADER = PermissibleValue(
        text="FACILITY_CLAIM_HEADER",
        description="Facility claim header",
        meaning=OMOP["32846"])
    GEOGRAPHIC_ISOLATION_RECORD = PermissibleValue(
        text="GEOGRAPHIC_ISOLATION_RECORD",
        description="Geographic isolation record",
        meaning=OMOP["32847"])
    GOVERNMENT_REPORT = PermissibleValue(
        text="GOVERNMENT_REPORT",
        description="Government report",
        meaning=OMOP["32848"])
    HEALTH_INFORMATION_EXCHANGE_RECORD = PermissibleValue(
        text="HEALTH_INFORMATION_EXCHANGE_RECORD",
        description="Health Information Exchange record",
        meaning=OMOP["32849"])
    HEALTH_RISK_ASSESSMENT = PermissibleValue(
        text="HEALTH_RISK_ASSESSMENT",
        description="Health Risk Assessment",
        meaning=OMOP["32850"])
    HEALTHCARE_PROFESSIONAL_FILLED_SURVEY = PermissibleValue(
        text="HEALTHCARE_PROFESSIONAL_FILLED_SURVEY",
        description="Healthcare professional filled survey",
        meaning=OMOP["32851"])
    HOSPITAL_COST = PermissibleValue(
        text="HOSPITAL_COST",
        description="Hospital cost",
        meaning=OMOP["32852"])
    INPATIENT_CLAIM = PermissibleValue(
        text="INPATIENT_CLAIM",
        description="Inpatient claim",
        meaning=OMOP["32853"])
    INPATIENT_CLAIM_DETAIL = PermissibleValue(
        text="INPATIENT_CLAIM_DETAIL",
        description="Inpatient claim detail",
        meaning=OMOP["32854"])
    INPATIENT_CLAIM_HEADER = PermissibleValue(
        text="INPATIENT_CLAIM_HEADER",
        description="Inpatient claim header",
        meaning=OMOP["32855"])
    LAB = PermissibleValue(
        text="LAB",
        description="Lab",
        meaning=OMOP["32856"])
    MAIL_ORDER_RECORD = PermissibleValue(
        text="MAIL_ORDER_RECORD",
        description="Mail order record",
        meaning=OMOP["32857"])
    NLP = PermissibleValue(
        text="NLP",
        description="NLP",
        meaning=OMOP["32858"])
    OUTPATIENT_CLAIM = PermissibleValue(
        text="OUTPATIENT_CLAIM",
        description="Outpatient claim",
        meaning=OMOP["32859"])
    OUTPATIENT_CLAIM_DETAIL = PermissibleValue(
        text="OUTPATIENT_CLAIM_DETAIL",
        description="Outpatient claim detail",
        meaning=OMOP["32860"])
    OUTPATIENT_CLAIM_HEADER = PermissibleValue(
        text="OUTPATIENT_CLAIM_HEADER",
        description="Outpatient claim header",
        meaning=OMOP["32861"])
    PATIENT_FILLED_SURVEY = PermissibleValue(
        text="PATIENT_FILLED_SURVEY",
        description="Patient filled survey",
        meaning=OMOP["32862"])
    PATIENT_OR_PAYER_PAID_RECORD = PermissibleValue(
        text="PATIENT_OR_PAYER_PAID_RECORD",
        description="Patient or payer paid record",
        meaning=OMOP["32863"])
    PATIENT_REPORTED_COST = PermissibleValue(
        text="PATIENT_REPORTED_COST",
        description="Patient reported cost",
        meaning=OMOP["32864"])
    PHARMACY_CLAIM = PermissibleValue(
        text="PHARMACY_CLAIM",
        description="Pharmacy claim",
        meaning=OMOP["32869"])
    PROFESSIONAL_CLAIM = PermissibleValue(
        text="PROFESSIONAL_CLAIM",
        description="Professional claim",
        meaning=OMOP["32871"])
    PROFESSIONAL_CLAIM_DETAIL = PermissibleValue(
        text="PROFESSIONAL_CLAIM_DETAIL",
        description="Professional claim detail",
        meaning=OMOP["32872"])
    PROFESSIONAL_CLAIM_HEADER = PermissibleValue(
        text="PROFESSIONAL_CLAIM_HEADER",
        description="Professional claim header",
        meaning=OMOP["32873"])
    PROVIDER_CHARGE_LIST_PRICE = PermissibleValue(
        text="PROVIDER_CHARGE_LIST_PRICE",
        description="Provider charge list price",
        meaning=OMOP["32874"])
    PROVIDER_FINANCIAL_SYSTEM = PermissibleValue(
        text="PROVIDER_FINANCIAL_SYSTEM",
        description="Provider financial system",
        meaning=OMOP["32875"])
    PROVIDER_INCURRED_COST_RECORD = PermissibleValue(
        text="PROVIDER_INCURRED_COST_RECORD",
        description="Provider incurred cost record",
        meaning=OMOP["32876"])
    RANDOMIZATION_RECORD = PermissibleValue(
        text="RANDOMIZATION_RECORD",
        description="Randomization record",
        meaning=OMOP["32877"])
    REFERENCE_LAB = PermissibleValue(
        text="REFERENCE_LAB",
        description="Reference lab",
        meaning=OMOP["32878"])
    REGISTRY = PermissibleValue(
        text="REGISTRY",
        description="Registry",
        meaning=OMOP["32879"])
    STANDARD_ALGORITHM = PermissibleValue(
        text="STANDARD_ALGORITHM",
        description="Standard algorithm",
        meaning=OMOP["32880"])
    STANDARD_ALGORITHM_FROM_EHR = PermissibleValue(
        text="STANDARD_ALGORITHM_FROM_EHR",
        description="Standard algorithm from EHR",
        meaning=OMOP["32882"])
    STANDARD_ALGORITHM_FROM_CLAIMS = PermissibleValue(
        text="STANDARD_ALGORITHM_FROM_CLAIMS",
        description="Standard algorithm from claims",
        meaning=OMOP["32881"])
    SURVEY = PermissibleValue(
        text="SURVEY",
        description="Survey",
        meaning=OMOP["32883"])
    US_SOCIAL_SECURITY_DEATH_MASTER_FILE = PermissibleValue(
        text="US_SOCIAL_SECURITY_DEATH_MASTER_FILE",
        description="US Social Security Death Master File",
        meaning=OMOP["32885"])
    URGENT_LAB = PermissibleValue(
        text="URGENT_LAB",
        description="Urgent lab",
        meaning=OMOP["32884"])
    VISION_CLAIM = PermissibleValue(
        text="VISION_CLAIM",
        description="Vision claim",
        meaning=OMOP["32886"])

    _defn = EnumDefinition(
        name="VisitProvenanceEnum",
        description="A constrained set of enumerative values containing the OMOP values for visit provenance.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "PATIENT_SELF-REPORT",
            PermissibleValue(
                text="PATIENT_SELF-REPORT",
                description="Patient self-report",
                meaning=OMOP["32865"]))
        setattr(cls, "PATIENT_SELF-TESTED",
            PermissibleValue(
                text="PATIENT_SELF-TESTED",
                description="Patient self-tested",
                meaning=OMOP["705183"]))
        setattr(cls, "PAYER_SYSTEM_RECORD_(PAID_PREMIUM)",
            PermissibleValue(
                text="PAYER_SYSTEM_RECORD_(PAID_PREMIUM)",
                description="Payer system record (paid premium)",
                meaning=OMOP["32866"]))
        setattr(cls, "PAYER_SYSTEM_RECORD_(PRIMARY_PAYER)",
            PermissibleValue(
                text="PAYER_SYSTEM_RECORD_(PRIMARY_PAYER)",
                description="Payer system record (primary payer)",
                meaning=OMOP["32867"]))
        setattr(cls, "PAYER_SYSTEM_RECORD_(SECONDARY_PAYER)",
            PermissibleValue(
                text="PAYER_SYSTEM_RECORD_(SECONDARY_PAYER)",
                description="Payer system record (secondary payer)",
                meaning=OMOP["32868"]))
        setattr(cls, "POINT_OF_CARE/EXPRESS_LAB",
            PermissibleValue(
                text="POINT_OF_CARE/EXPRESS_LAB",
                description="Point of care/express lab",
                meaning=OMOP["703249"]))
        setattr(cls, "PRE-QUALIFICATION_TIME_PERIOD",
            PermissibleValue(
                text="PRE-QUALIFICATION_TIME_PERIOD",
                description="Pre-qualification time period",
                meaning=OMOP["32870"]))

class MondoHumanDiseaseEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the MONDO values for human diseases.
    """
    _defn = EnumDefinition(
        name="MondoHumanDiseaseEnum",
        description="A constrained set of enumerative values containing the MONDO values for human diseases.",
    )

class HpoPhenotypicAbnormalityEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the HPO values for phenotypic abnormalities.
    """
    _defn = EnumDefinition(
        name="HpoPhenotypicAbnormalityEnum",
        description="A constrained set of enumerative values containing the HPO values for phenotypic abnormalities.",
    )

class ConditionConceptEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing both the MONDO values for human diseases and the HPO values for
    phenotypic abnormalities.
    """
    _defn = EnumDefinition(
        name="ConditionConceptEnum",
        description="""A constrained set of enumerative values containing both the MONDO values for human diseases and the HPO values for phenotypic abnormalities.""",
    )

class ConditionProvenanceEnum(EnumDefinitionImpl):
    """
    A constrained set of enumerative values containing the OMOP values for visit provenance.
    """
    EHR_BILLING_DIAGNOSIS = PermissibleValue(
        text="EHR_BILLING_DIAGNOSIS",
        meaning=OMOP["4822159"])
    EHR_CHIEF_COMPLAINT = PermissibleValue(
        text="EHR_CHIEF_COMPLAINT",
        meaning=OMOP["4822124"])
    EHR_ENCOUNTER_DIAGNOSIS = PermissibleValue(
        text="EHR_ENCOUNTER_DIAGNOSIS",
        meaning=OMOP["4822160"])
    EHR_EPISODE_ENTRY = PermissibleValue(
        text="EHR_EPISODE_ENTRY",
        meaning=OMOP["4822135"])
    EHR_PROBLEM_LIST_ENTRY = PermissibleValue(
        text="EHR_PROBLEM_LIST_ENTRY",
        meaning=OMOP["4822121"])
    FIRST_POSITION_CONDITION = PermissibleValue(
        text="FIRST_POSITION_CONDITION",
        meaning=OMOP["4822128"])
    NLP_DERIVED = PermissibleValue(
        text="NLP_DERIVED",
        meaning=OMOP["4822058"])
    OBSERVATION_RECORDED_FROM_EHR = PermissibleValue(
        text="OBSERVATION_RECORDED_FROM_EHR",
        meaning=OMOP["4822126"])
    PRIMARY_CONDITION = PermissibleValue(
        text="PRIMARY_CONDITION",
        meaning=OMOP["4822127"])
    REFERRAL_RECORD = PermissibleValue(
        text="REFERRAL_RECORD",
        meaning=OMOP["4822125"])
    SECONDARY_CONDITION = PermissibleValue(
        text="SECONDARY_CONDITION",
        meaning=OMOP["4822129"])
    TUMOR_REGISTRY = PermissibleValue(
        text="TUMOR_REGISTRY",
        meaning=OMOP["4822266"])

    _defn = EnumDefinition(
        name="ConditionProvenanceEnum",
        description="A constrained set of enumerative values containing the OMOP values for visit provenance.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "PATIENT_SELF-REPORTED_CONDITION",
            PermissibleValue(
                text="PATIENT_SELF-REPORTED_CONDITION",
                meaning=OMOP["4822157"]))

# Slots
class slots:
    pass

slots.comparator = Slot(uri=CMDR.comparator, name="comparator", curie=CMDR.curie('comparator'),
                   model_uri=CMDR.comparator, domain=None, range=Optional[str])

slots.concentration = Slot(uri=CMDR.concentration, name="concentration", curie=CMDR.curie('concentration'),
                   model_uri=CMDR.concentration, domain=None, range=Optional[str])

slots.has_input = Slot(uri=CMDR.has_input, name="has_input", curie=CMDR.curie('has_input'),
                   model_uri=CMDR.has_input, domain=None, range=Optional[str])

slots.has_numeric_value = Slot(uri=CMDR.has_numeric_value, name="has_numeric_value", curie=CMDR.curie('has_numeric_value'),
                   model_uri=CMDR.has_numeric_value, domain=None, range=Optional[str])

slots.has_output = Slot(uri=CMDR.has_output, name="has_output", curie=CMDR.curie('has_output'),
                   model_uri=CMDR.has_output, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=CMDR.has_raw_value, name="has_raw_value", curie=CMDR.curie('has_raw_value'),
                   model_uri=CMDR.has_raw_value, domain=None, range=Optional[str])

slots.has_unit = Slot(uri=CMDR.has_unit, name="has_unit", curie=CMDR.curie('has_unit'),
                   model_uri=CMDR.has_unit, domain=None, range=Optional[str])

slots.id = Slot(uri=CMDR.id, name="id", curie=CMDR.curie('id'),
                   model_uri=CMDR.id, domain=None, range=Optional[str])

slots.includes = Slot(uri=CMDR.includes, name="includes", curie=CMDR.curie('includes'),
                   model_uri=CMDR.includes, domain=None, range=Optional[str])

slots.investigations = Slot(uri=CMDR.investigations, name="investigations", curie=CMDR.curie('investigations'),
                   model_uri=CMDR.investigations, domain=None, range=Optional[str])

slots.involved_in = Slot(uri=CMDR.involved_in, name="involved_in", curie=CMDR.curie('involved_in'),
                   model_uri=CMDR.involved_in, domain=None, range=Optional[str])

slots.material_processings = Slot(uri=CMDR.material_processings, name="material_processings", curie=CMDR.curie('material_processings'),
                   model_uri=CMDR.material_processings, domain=None, range=Optional[str])

slots.materials = Slot(uri=CMDR.materials, name="materials", curie=CMDR.curie('materials'),
                   model_uri=CMDR.materials, domain=None, range=Optional[str])

slots.name = Slot(uri=CMDR.name, name="name", curie=CMDR.curie('name'),
                   model_uri=CMDR.name, domain=None, range=Optional[str])

slots.part_of = Slot(uri=CMDR.part_of, name="part_of", curie=CMDR.curie('part_of'),
                   model_uri=CMDR.part_of, domain=None, range=Optional[str])

slots.participations = Slot(uri=CMDR.participations, name="participations", curie=CMDR.curie('participations'),
                   model_uri=CMDR.participations, domain=None, range=Optional[str])

slots.source = Slot(uri=CMDR.source, name="source", curie=CMDR.curie('source'),
                   model_uri=CMDR.source, domain=None, range=Optional[str])

slots.specimen_collection_processes = Slot(uri=CMDR.specimen_collection_processes, name="specimen_collection_processes", curie=CMDR.curie('specimen_collection_processes'),
                   model_uri=CMDR.specimen_collection_processes, domain=None, range=Optional[str])

slots.subjects = Slot(uri=CMDR.subjects, name="subjects", curie=CMDR.curie('subjects'),
                   model_uri=CMDR.subjects, domain=None, range=Optional[str])

slots.used_in = Slot(uri=CMDR.used_in, name="used_in", curie=CMDR.curie('used_in'),
                   model_uri=CMDR.used_in, domain=None, range=Optional[str])

slots.volume = Slot(uri=CMDR.volume, name="volume", curie=CMDR.curie('volume'),
                   model_uri=CMDR.volume, domain=None, range=Optional[str])

slots.identity = Slot(uri=SCHEMA.identifier, name="identity", curie=SCHEMA.curie('identifier'),
                   model_uri=CMDR.identity, domain=None, range=Optional[Union[Union[dict, Identifier], List[Union[dict, Identifier]]]])

slots.associated_person = Slot(uri=BDCHM.associated_person, name="associated_person", curie=BDCHM.curie('associated_person'),
                   model_uri=CMDR.associated_person, domain=None, range=Optional[Union[str, PersonId]])

slots.value = Slot(uri=BDCHM.value, name="value", curie=BDCHM.curie('value'),
                   model_uri=CMDR.value, domain=None, range=Optional[str])

slots.person__species = Slot(uri=BDCHM.species, name="person__species", curie=BDCHM.curie('species'),
                   model_uri=CMDR.person__species, domain=None, range=Optional[Union[str, "CellularOrganismSpeciesEnum"]])

slots.person__breed = Slot(uri=BDCHM.breed, name="person__breed", curie=BDCHM.curie('breed'),
                   model_uri=CMDR.person__breed, domain=None, range=Optional[Union[str, "VertebrateBreedEnum"]])

slots.person__sex = Slot(uri=BDCHM.sex, name="person__sex", curie=BDCHM.curie('sex'),
                   model_uri=CMDR.person__sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.person__ethnicity = Slot(uri=BDCHM.ethnicity, name="person__ethnicity", curie=BDCHM.curie('ethnicity'),
                   model_uri=CMDR.person__ethnicity, domain=None, range=Optional[Union[str, "EthnicityEnum"]])

slots.person__race = Slot(uri=BDCHM.race, name="person__race", curie=BDCHM.curie('race'),
                   model_uri=CMDR.person__race, domain=None, range=Optional[Union[str, "RaceEnum"]])

slots.person__year_of_birth = Slot(uri=BDCHM.year_of_birth, name="person__year_of_birth", curie=BDCHM.curie('year_of_birth'),
                   model_uri=CMDR.person__year_of_birth, domain=None, range=Optional[int])

slots.person__vital_status = Slot(uri=BDCHM.vital_status, name="person__vital_status", curie=BDCHM.curie('vital_status'),
                   model_uri=CMDR.person__vital_status, domain=None, range=Optional[Union[str, "VitalStatusEnum"]])

slots.person__age_at_death = Slot(uri=BDCHM.age_at_death, name="person__age_at_death", curie=BDCHM.curie('age_at_death'),
                   model_uri=CMDR.person__age_at_death, domain=None, range=Optional[int])

slots.person__year_of_death = Slot(uri=BDCHM.year_of_death, name="person__year_of_death", curie=BDCHM.curie('year_of_death'),
                   model_uri=CMDR.person__year_of_death, domain=None, range=Optional[int])

slots.person__cause_of_death = Slot(uri=BDCHM.cause_of_death, name="person__cause_of_death", curie=BDCHM.curie('cause_of_death'),
                   model_uri=CMDR.person__cause_of_death, domain=None, range=Optional[str])

slots.participant__description = Slot(uri=BDCHM.description, name="participant__description", curie=BDCHM.curie('description'),
                   model_uri=CMDR.participant__description, domain=None, range=Optional[str])

slots.participant__member_of_research_study = Slot(uri=BDCHM.member_of_research_study, name="participant__member_of_research_study", curie=BDCHM.curie('member_of_research_study'),
                   model_uri=CMDR.participant__member_of_research_study, domain=None, range=Optional[Union[str, ResearchStudyId]])

slots.participant__age_at_enrollment = Slot(uri=BDCHM.age_at_enrollment, name="participant__age_at_enrollment", curie=BDCHM.curie('age_at_enrollment'),
                   model_uri=CMDR.participant__age_at_enrollment, domain=None, range=Optional[int])

slots.participant__index_timepoint = Slot(uri=BDCHM.index_timepoint, name="participant__index_timepoint", curie=BDCHM.curie('index_timepoint'),
                   model_uri=CMDR.participant__index_timepoint, domain=None, range=Optional[str])

slots.participant__originating_site = Slot(uri=BDCHM.originating_site, name="participant__originating_site", curie=BDCHM.curie('originating_site'),
                   model_uri=CMDR.participant__originating_site, domain=None, range=Optional[Union[dict, Organization]])

slots.participant__study_arm = Slot(uri=BDCHM.study_arm, name="participant__study_arm", curie=BDCHM.curie('study_arm'),
                   model_uri=CMDR.participant__study_arm, domain=None, range=Optional[Union[str, List[str]]])

slots.researchStudy__name = Slot(uri=BDCHM.name, name="researchStudy__name", curie=BDCHM.curie('name'),
                   model_uri=CMDR.researchStudy__name, domain=None, range=Optional[str])

slots.researchStudy__name_shortened = Slot(uri=BDCHM.name_shortened, name="researchStudy__name_shortened", curie=BDCHM.curie('name_shortened'),
                   model_uri=CMDR.researchStudy__name_shortened, domain=None, range=Optional[str])

slots.researchStudy__description = Slot(uri=BDCHM.description, name="researchStudy__description", curie=BDCHM.curie('description'),
                   model_uri=CMDR.researchStudy__description, domain=None, range=Optional[str])

slots.researchStudy__description_shortened = Slot(uri=BDCHM.description_shortened, name="researchStudy__description_shortened", curie=BDCHM.curie('description_shortened'),
                   model_uri=CMDR.researchStudy__description_shortened, domain=None, range=Optional[str])

slots.researchStudy__sponsor = Slot(uri=BDCHM.sponsor, name="researchStudy__sponsor", curie=BDCHM.curie('sponsor'),
                   model_uri=CMDR.researchStudy__sponsor, domain=None, range=Optional[str])

slots.researchStudy__date_started = Slot(uri=BDCHM.date_started, name="researchStudy__date_started", curie=BDCHM.curie('date_started'),
                   model_uri=CMDR.researchStudy__date_started, domain=None, range=Optional[Union[dict, TimePoint]])

slots.researchStudy__date_ended = Slot(uri=BDCHM.date_ended, name="researchStudy__date_ended", curie=BDCHM.curie('date_ended'),
                   model_uri=CMDR.researchStudy__date_ended, domain=None, range=Optional[Union[dict, TimePoint]])

slots.researchStudy__url = Slot(uri=BDCHM.url, name="researchStudy__url", curie=BDCHM.curie('url'),
                   model_uri=CMDR.researchStudy__url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.researchStudy__part_of = Slot(uri=BDCHM.part_of, name="researchStudy__part_of", curie=BDCHM.curie('part_of'),
                   model_uri=CMDR.researchStudy__part_of, domain=None, range=Optional[Union[str, ResearchStudyId]])

slots.researchStudy__research_project_type = Slot(uri=BDCHM.research_project_type, name="researchStudy__research_project_type", curie=BDCHM.curie('research_project_type'),
                   model_uri=CMDR.researchStudy__research_project_type, domain=None, range=Optional[str])

slots.researchStudy__associated_timepoint = Slot(uri=BDCHM.associated_timepoint, name="researchStudy__associated_timepoint", curie=BDCHM.curie('associated_timepoint'),
                   model_uri=CMDR.researchStudy__associated_timepoint, domain=None, range=Optional[Union[Union[dict, TimePoint], List[Union[dict, TimePoint]]]])

slots.researchStudy__principal_investigator = Slot(uri=BDCHM.principal_investigator, name="researchStudy__principal_investigator", curie=BDCHM.curie('principal_investigator'),
                   model_uri=CMDR.researchStudy__principal_investigator, domain=None, range=Optional[Union[str, List[str]]])

slots.researchStudy__consent_code = Slot(uri=BDCHM.consent_code, name="researchStudy__consent_code", curie=BDCHM.curie('consent_code'),
                   model_uri=CMDR.researchStudy__consent_code, domain=None, range=Optional[Union[Union[str, "DataUseEnum"], List[Union[str, "DataUseEnum"]]]])

slots.visit__visit_category = Slot(uri=BDCHM.visit_category, name="visit__visit_category", curie=BDCHM.curie('visit_category'),
                   model_uri=CMDR.visit__visit_category, domain=None, range=Optional[Union[str, "VisitCategoryEnum"]])

slots.visit__age_at_visit_start = Slot(uri=BDCHM.age_at_visit_start, name="visit__age_at_visit_start", curie=BDCHM.curie('age_at_visit_start'),
                   model_uri=CMDR.visit__age_at_visit_start, domain=None, range=Optional[int])

slots.visit__age_at_visit_end = Slot(uri=BDCHM.age_at_visit_end, name="visit__age_at_visit_end", curie=BDCHM.curie('age_at_visit_end'),
                   model_uri=CMDR.visit__age_at_visit_end, domain=None, range=Optional[int])

slots.visit__visit_provenance = Slot(uri=BDCHM.visit_provenance, name="visit__visit_provenance", curie=BDCHM.curie('visit_provenance'),
                   model_uri=CMDR.visit__visit_provenance, domain=None, range=Optional[Union[str, "VisitProvenanceEnum"]])

slots.visit__associated_participant = Slot(uri=BDCHM.associated_participant, name="visit__associated_participant", curie=BDCHM.curie('associated_participant'),
                   model_uri=CMDR.visit__associated_participant, domain=None, range=Optional[Union[dict, Participant]])

slots.organization__name = Slot(uri=BDCHM.name, name="organization__name", curie=BDCHM.curie('name'),
                   model_uri=CMDR.organization__name, domain=None, range=Optional[str])

slots.organization__alias = Slot(uri=BDCHM.alias, name="organization__alias", curie=BDCHM.curie('alias'),
                   model_uri=CMDR.organization__alias, domain=None, range=Optional[str])

slots.organization__organization_type = Slot(uri=BDCHM.organization_type, name="organization__organization_type", curie=BDCHM.curie('organization_type'),
                   model_uri=CMDR.organization__organization_type, domain=None, range=Optional[str])

slots.timePoint__date_time = Slot(uri=BDCHM.date_time, name="timePoint__date_time", curie=BDCHM.curie('date_time'),
                   model_uri=CMDR.timePoint__date_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.timePoint__index_time_point = Slot(uri=BDCHM.index_time_point, name="timePoint__index_time_point", curie=BDCHM.curie('index_time_point'),
                   model_uri=CMDR.timePoint__index_time_point, domain=None, range=Optional[Union[dict, TimePoint]])

slots.timePoint__offset_from_index = Slot(uri=BDCHM.offset_from_index, name="timePoint__offset_from_index", curie=BDCHM.curie('offset_from_index'),
                   model_uri=CMDR.timePoint__offset_from_index, domain=None, range=Optional[int])

slots.timePoint__event_type = Slot(uri=BDCHM.event_type, name="timePoint__event_type", curie=BDCHM.curie('event_type'),
                   model_uri=CMDR.timePoint__event_type, domain=None, range=Optional[str])

slots.timePeriod__period_start = Slot(uri=BDCHM.period_start, name="timePeriod__period_start", curie=BDCHM.curie('period_start'),
                   model_uri=CMDR.timePeriod__period_start, domain=None, range=Optional[Union[dict, TimePoint]])

slots.timePeriod__period_end = Slot(uri=BDCHM.period_end, name="timePeriod__period_end", curie=BDCHM.curie('period_end'),
                   model_uri=CMDR.timePeriod__period_end, domain=None, range=Optional[Union[dict, TimePoint]])

slots.identifier__value = Slot(uri=BDCHM.value, name="identifier__value", curie=BDCHM.curie('value'),
                   model_uri=CMDR.identifier__value, domain=None, range=str)

slots.identifier__system = Slot(uri=BDCHM.system, name="identifier__system", curie=BDCHM.curie('system'),
                   model_uri=CMDR.identifier__system, domain=None, range=Optional[str])

slots.researchStudyCollection__entries = Slot(uri=BDCHM.entries, name="researchStudyCollection__entries", curie=BDCHM.curie('entries'),
                   model_uri=CMDR.researchStudyCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ResearchStudyId], Union[dict, ResearchStudy]], List[Union[dict, ResearchStudy]]]])

slots.questionnaire__name = Slot(uri=BDCHM.name, name="questionnaire__name", curie=BDCHM.curie('name'),
                   model_uri=CMDR.questionnaire__name, domain=None, range=Optional[str])

slots.questionnaire__title = Slot(uri=BDCHM.title, name="questionnaire__title", curie=BDCHM.curie('title'),
                   model_uri=CMDR.questionnaire__title, domain=None, range=Optional[str])

slots.questionnaire__description = Slot(uri=BDCHM.description, name="questionnaire__description", curie=BDCHM.curie('description'),
                   model_uri=CMDR.questionnaire__description, domain=None, range=Optional[str])

slots.questionnaire__url = Slot(uri=BDCHM.url, name="questionnaire__url", curie=BDCHM.curie('url'),
                   model_uri=CMDR.questionnaire__url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.questionnaire__version = Slot(uri=BDCHM.version, name="questionnaire__version", curie=BDCHM.curie('version'),
                   model_uri=CMDR.questionnaire__version, domain=None, range=Optional[str])

slots.questionnaire__publisher = Slot(uri=BDCHM.publisher, name="questionnaire__publisher", curie=BDCHM.curie('publisher'),
                   model_uri=CMDR.questionnaire__publisher, domain=None, range=Optional[str])

slots.questionnaire__copyright = Slot(uri=BDCHM.copyright, name="questionnaire__copyright", curie=BDCHM.curie('copyright'),
                   model_uri=CMDR.questionnaire__copyright, domain=None, range=Optional[str])

slots.questionnaire__copyright_label = Slot(uri=BDCHM.copyright_label, name="questionnaire__copyright_label", curie=BDCHM.curie('copyright_label'),
                   model_uri=CMDR.questionnaire__copyright_label, domain=None, range=Optional[str])

slots.questionnaire__language = Slot(uri=BDCHM.language, name="questionnaire__language", curie=BDCHM.curie('language'),
                   model_uri=CMDR.questionnaire__language, domain=None, range=Optional[Union[str, List[str]]])

slots.questionnaire__items = Slot(uri=BDCHM.items, name="questionnaire__items", curie=BDCHM.curie('items'),
                   model_uri=CMDR.questionnaire__items, domain=None, range=Union[Union[dict, QuestionnaireItem], List[Union[dict, QuestionnaireItem]]])

slots.questionnaireItem__text = Slot(uri=BDCHM.text, name="questionnaireItem__text", curie=BDCHM.curie('text'),
                   model_uri=CMDR.questionnaireItem__text, domain=None, range=Optional[str])

slots.questionnaireItem__code = Slot(uri=BDCHM.code, name="questionnaireItem__code", curie=BDCHM.curie('code'),
                   model_uri=CMDR.questionnaireItem__code, domain=None, range=Optional[str])

slots.questionnaireItem__part_of = Slot(uri=BDCHM.part_of, name="questionnaireItem__part_of", curie=BDCHM.curie('part_of'),
                   model_uri=CMDR.questionnaireItem__part_of, domain=None, range=Optional[Union[dict, QuestionnaireItem]])

slots.questionnaireResponse__age_at_response = Slot(uri=BDCHM.age_at_response, name="questionnaireResponse__age_at_response", curie=BDCHM.curie('age_at_response'),
                   model_uri=CMDR.questionnaireResponse__age_at_response, domain=None, range=Optional[int])

slots.questionnaireResponse__items = Slot(uri=BDCHM.items, name="questionnaireResponse__items", curie=BDCHM.curie('items'),
                   model_uri=CMDR.questionnaireResponse__items, domain=None, range=Union[Union[dict, QuestionnaireResponseItem], List[Union[dict, QuestionnaireResponseItem]]])

slots.questionnaireResponse__associated_visit = Slot(uri=BDCHM.associated_visit, name="questionnaireResponse__associated_visit", curie=BDCHM.curie('associated_visit'),
                   model_uri=CMDR.questionnaireResponse__associated_visit, domain=None, range=Optional[Union[dict, Visit]])

slots.questionnaireResponseItem__has_questionnaire_item = Slot(uri=BDCHM.has_questionnaire_item, name="questionnaireResponseItem__has_questionnaire_item", curie=BDCHM.curie('has_questionnaire_item'),
                   model_uri=CMDR.questionnaireResponseItem__has_questionnaire_item, domain=None, range=Optional[Union[dict, QuestionnaireItem]])

slots.questionnaireResponseItem__text = Slot(uri=BDCHM.text, name="questionnaireResponseItem__text", curie=BDCHM.curie('text'),
                   model_uri=CMDR.questionnaireResponseItem__text, domain=None, range=Optional[str])

slots.questionnaireResponseItem__response_value = Slot(uri=BDCHM.response_value, name="questionnaireResponseItem__response_value", curie=BDCHM.curie('response_value'),
                   model_uri=CMDR.questionnaireResponseItem__response_value, domain=None, range=Union[dict, QuestionnaireResponseValue])

slots.questionnaireResponseValue__type = Slot(uri=BDCHM.type, name="questionnaireResponseValue__type", curie=BDCHM.curie('type'),
                   model_uri=CMDR.questionnaireResponseValue__type, domain=None, range=Optional[str])

slots.questionnaireResponseValue__name = Slot(uri=BDCHM.name, name="questionnaireResponseValue__name", curie=BDCHM.curie('name'),
                   model_uri=CMDR.questionnaireResponseValue__name, domain=None, range=Optional[str])

slots.condition__condition_concept = Slot(uri=BDCHM.condition_concept, name="condition__condition_concept", curie=BDCHM.curie('condition_concept'),
                   model_uri=CMDR.condition__condition_concept, domain=None, range=Optional[Union[str, "ConditionConceptEnum"]])

slots.condition__age_at_condition_start = Slot(uri=BDCHM.age_at_condition_start, name="condition__age_at_condition_start", curie=BDCHM.curie('age_at_condition_start'),
                   model_uri=CMDR.condition__age_at_condition_start, domain=None, range=Optional[int])

slots.condition__age_at_condition_end = Slot(uri=BDCHM.age_at_condition_end, name="condition__age_at_condition_end", curie=BDCHM.curie('age_at_condition_end'),
                   model_uri=CMDR.condition__age_at_condition_end, domain=None, range=Optional[int])

slots.condition__condition_provenance = Slot(uri=BDCHM.condition_provenance, name="condition__condition_provenance", curie=BDCHM.curie('condition_provenance'),
                   model_uri=CMDR.condition__condition_provenance, domain=None, range=Optional[Union[str, "ConditionProvenanceEnum"]])

slots.condition__relationship_to_participant = Slot(uri=BDCHM.relationship_to_participant, name="condition__relationship_to_participant", curie=BDCHM.curie('relationship_to_participant'),
                   model_uri=CMDR.condition__relationship_to_participant, domain=None, range=Optional[str])

slots.condition__associated_participant = Slot(uri=BDCHM.associated_participant, name="condition__associated_participant", curie=BDCHM.curie('associated_participant'),
                   model_uri=CMDR.condition__associated_participant, domain=None, range=Optional[Union[dict, Participant]])

slots.condition__associated_visit = Slot(uri=BDCHM.associated_visit, name="condition__associated_visit", curie=BDCHM.curie('associated_visit'),
                   model_uri=CMDR.condition__associated_visit, domain=None, range=Optional[Union[dict, Visit]])

slots.Container_investigations = Slot(uri=CMDR.investigations, name="Container_investigations", curie=CMDR.curie('investigations'),
                   model_uri=CMDR.Container_investigations, domain=Container, range=Optional[Union[Dict[Union[str, InvestigationId], Union[dict, "Investigation"]], List[Union[dict, "Investigation"]]]])

slots.Container_material_processings = Slot(uri=CMDR.material_processings, name="Container_material_processings", curie=CMDR.curie('material_processings'),
                   model_uri=CMDR.Container_material_processings, domain=Container, range=Optional[Union[Dict[Union[str, MaterialProcessingId], Union[dict, "MaterialProcessing"]], List[Union[dict, "MaterialProcessing"]]]])

slots.Container_materials = Slot(uri=CMDR.materials, name="Container_materials", curie=CMDR.curie('materials'),
                   model_uri=CMDR.Container_materials, domain=Container, range=Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]])

slots.Container_participations = Slot(uri=CMDR.participations, name="Container_participations", curie=CMDR.curie('participations'),
                   model_uri=CMDR.Container_participations, domain=Container, range=Optional[Union[Dict[Union[str, ParticipationId], Union[dict, "Participation"]], List[Union[dict, "Participation"]]]])

slots.Container_specimen_collection_processes = Slot(uri=CMDR.specimen_collection_processes, name="Container_specimen_collection_processes", curie=CMDR.curie('specimen_collection_processes'),
                   model_uri=CMDR.Container_specimen_collection_processes, domain=Container, range=Optional[Union[Dict[Union[str, SpecimenCollectionProcessId], Union[dict, "SpecimenCollectionProcess"]], List[Union[dict, "SpecimenCollectionProcess"]]]])

slots.Container_subjects = Slot(uri=CMDR.subjects, name="Container_subjects", curie=CMDR.curie('subjects'),
                   model_uri=CMDR.Container_subjects, domain=Container, range=Optional[Union[Dict[Union[str, SubjectId], Union[dict, "Subject"]], List[Union[dict, "Subject"]]]])

slots.Investigation_id = Slot(uri=CMDR.id, name="Investigation_id", curie=CMDR.curie('id'),
                   model_uri=CMDR.Investigation_id, domain=Investigation, range=Union[str, InvestigationId])

slots.Investigation_part_of = Slot(uri=CMDR.part_of, name="Investigation_part_of", curie=CMDR.curie('part_of'),
                   model_uri=CMDR.Investigation_part_of, domain=Investigation, range=Optional[Union[str, InvestigationId]])

slots.MaterialEntity_concentration = Slot(uri=CMDR.concentration, name="MaterialEntity_concentration", curie=CMDR.curie('concentration'),
                   model_uri=CMDR.MaterialEntity_concentration, domain=MaterialEntity, range=Optional[Union[dict, "Quantity"]])

slots.MaterialEntity_id = Slot(uri=CMDR.id, name="MaterialEntity_id", curie=CMDR.curie('id'),
                   model_uri=CMDR.MaterialEntity_id, domain=MaterialEntity, range=Union[str, MaterialEntityId])

slots.MaterialEntity_source = Slot(uri=CMDR.source, name="MaterialEntity_source", curie=CMDR.curie('source'),
                   model_uri=CMDR.MaterialEntity_source, domain=MaterialEntity, range=Optional[Union[str, SubjectId]])

slots.MaterialEntity_used_in = Slot(uri=CMDR.used_in, name="MaterialEntity_used_in", curie=CMDR.curie('used_in'),
                   model_uri=CMDR.MaterialEntity_used_in, domain=MaterialEntity, range=Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]])

slots.MaterialEntity_volume = Slot(uri=CMDR.volume, name="MaterialEntity_volume", curie=CMDR.curie('volume'),
                   model_uri=CMDR.MaterialEntity_volume, domain=MaterialEntity, range=Optional[Union[dict, "Quantity"]])

slots.MaterialProcessing_has_input = Slot(uri=CMDR.has_input, name="MaterialProcessing_has_input", curie=CMDR.curie('has_input'),
                   model_uri=CMDR.MaterialProcessing_has_input, domain=MaterialProcessing, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.MaterialProcessing_has_output = Slot(uri=CMDR.has_output, name="MaterialProcessing_has_output", curie=CMDR.curie('has_output'),
                   model_uri=CMDR.MaterialProcessing_has_output, domain=MaterialProcessing, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.Participation_id = Slot(uri=CMDR.id, name="Participation_id", curie=CMDR.curie('id'),
                   model_uri=CMDR.Participation_id, domain=Participation, range=Union[str, ParticipationId])

slots.Participation_includes = Slot(uri=CMDR.includes, name="Participation_includes", curie=CMDR.curie('includes'),
                   model_uri=CMDR.Participation_includes, domain=Participation, range=Optional[Union[str, SubjectId]])

slots.Participation_involved_in = Slot(uri=CMDR.involved_in, name="Participation_involved_in", curie=CMDR.curie('involved_in'),
                   model_uri=CMDR.Participation_involved_in, domain=Participation, range=Optional[Union[Union[str, InvestigationId], List[Union[str, InvestigationId]]]])

slots.Process_has_input = Slot(uri=CMDR.has_input, name="Process_has_input", curie=CMDR.curie('has_input'),
                   model_uri=CMDR.Process_has_input, domain=Process, range=Optional[Union[str, List[str]]])

slots.Process_has_output = Slot(uri=CMDR.has_output, name="Process_has_output", curie=CMDR.curie('has_output'),
                   model_uri=CMDR.Process_has_output, domain=Process, range=Optional[Union[str, List[str]]])

slots.Process_id = Slot(uri=CMDR.id, name="Process_id", curie=CMDR.curie('id'),
                   model_uri=CMDR.Process_id, domain=Process, range=Union[str, ProcessId])

slots.Quantity_comparator = Slot(uri=CMDR.comparator, name="Quantity_comparator", curie=CMDR.curie('comparator'),
                   model_uri=CMDR.Quantity_comparator, domain=Quantity, range=Optional[str])

slots.Quantity_has_numeric_value = Slot(uri=CMDR.has_numeric_value, name="Quantity_has_numeric_value", curie=CMDR.curie('has_numeric_value'),
                   model_uri=CMDR.Quantity_has_numeric_value, domain=Quantity, range=Optional[float])

slots.Quantity_has_raw_value = Slot(uri=CMDR.has_raw_value, name="Quantity_has_raw_value", curie=CMDR.curie('has_raw_value'),
                   model_uri=CMDR.Quantity_has_raw_value, domain=Quantity, range=Optional[str])

slots.Quantity_has_unit = Slot(uri=CMDR.has_unit, name="Quantity_has_unit", curie=CMDR.curie('has_unit'),
                   model_uri=CMDR.Quantity_has_unit, domain=Quantity, range=Optional[str])

slots.SpecimenCollectionProcess_has_input = Slot(uri=CMDR.has_input, name="SpecimenCollectionProcess_has_input", curie=CMDR.curie('has_input'),
                   model_uri=CMDR.SpecimenCollectionProcess_has_input, domain=SpecimenCollectionProcess, range=Optional[Union[Union[str, SubjectId], List[Union[str, SubjectId]]]])

slots.SpecimenCollectionProcess_has_output = Slot(uri=CMDR.has_output, name="SpecimenCollectionProcess_has_output", curie=CMDR.curie('has_output'),
                   model_uri=CMDR.SpecimenCollectionProcess_has_output, domain=SpecimenCollectionProcess, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.Subject_id = Slot(uri=CMDR.id, name="Subject_id", curie=CMDR.curie('id'),
                   model_uri=CMDR.Subject_id, domain=Subject, range=Union[str, SubjectId])

slots.QuestionnaireResponseValueDecimal_value = Slot(uri=BDCHM.value, name="QuestionnaireResponseValueDecimal_value", curie=BDCHM.curie('value'),
                   model_uri=CMDR.QuestionnaireResponseValueDecimal_value, domain=QuestionnaireResponseValueDecimal, range=Decimal)

slots.QuestionnaireResponseValueBoolean_value = Slot(uri=BDCHM.value, name="QuestionnaireResponseValueBoolean_value", curie=BDCHM.curie('value'),
                   model_uri=CMDR.QuestionnaireResponseValueBoolean_value, domain=QuestionnaireResponseValueBoolean, range=Union[bool, Bool])

slots.QuestionnaireResponseValueString_value = Slot(uri=BDCHM.value, name="QuestionnaireResponseValueString_value", curie=BDCHM.curie('value'),
                   model_uri=CMDR.QuestionnaireResponseValueString_value, domain=QuestionnaireResponseValueString, range=str)
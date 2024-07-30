from linkml_map.session import Session
import graphviz
from linkml_runtime.utils.schemaview import SchemaView
from pprint import pprint
from linkml_runtime.dumpers import yaml_dumper

# Load the schema
schema_path = "src/linkml_map_example/schema/linkml_map_example.yaml"
sv = SchemaView(schema_path)

# Initialize Session and SchemaBuilder
session = Session()

# Set the source schema in the session
session.set_source_schema(sv)


# Transformer specification (in YAML)
session.set_object_transformer("""
class_derivations:
    Entity:
        populated_from: MaterialEntity
        description: >-
            Any resource that has its own identifier
    Person:
        populated_from: Subject
        is_a: Entity
        slot_derivations:
            id:
                populated_from: id
            species:
                range: CellularOrganismSpeciesEnum
                description: The scientific binomial name for the species of the Person (e.g. Homo sapiens, Mus musculus, etc.). Values should be derived from the NCBI organismal taxonomy (http://purl.obolibrary.org/obo/ncbitaxon.owl).
            breed:
                range: VertebrateBreedEnum
                description: A label given to a group of animals homogeneous in appearance and other characteristics that distinguish it from other animals of the same species. Values should be derived from the Vertebrate Breed Ontology (http://purl.obolibrary.org/obo/vbo.owl).
            sex:
                range: SexEnum
                description: The biologic character or quality that distinguishes male and female from one another as expressed by analysis of the person's gonadal, morphologic (internal and external), chromosomal, and hormonal characteristics.
            ethnicity:
                range: EthnicityEnum
                description: An individual's self-described social and cultural grouping, specifically whether an individual describes themselves as Hispanic or Latino. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau
            race:
                range: RaceEnum
                description: An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.
            year_of_birth:
                range: integer
                description: Numeric value to represent the calendar year in which an individual was born.
            vital_status:
                range: VitalStatusEnum
                description: Coded value indicating the state or condition of being living or deceased; also includes the case where the vital status is unknown.
            age_at_death:
                range: integer
                description: The age of an individual at the time of death, expressed in days since birth
            year_of_death:
                range: integer
                description: Numeric value to represent the calendar year in which an individual died.
            cause_of_death:
                range: string
                description: Coded value indicating the circumstance or condition that results in the death of the individual.
    Participant:
        populated_from: Participation
        is_a: Entity
        description: >-
            A Participant is the entity of interest in a research study, typically a human being or an animal, but can also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy.
        slot_derivations:
            member_of_research_study:
                range: ResearchStudy
                description: A reference to the Study(s) of which this Participant is a member
            age_at_enrollment:
                range: integer
                description: The age in days when the Participant enrolled on the ResearchStudy
            index_timepoint:
                range: string
                description: The text term used to describe the reference or anchor date used for date obfuscation, where a single date is obscured by creating one or more date ranges in relation to this date.
            originating_site:
                range: Organization
                description: The Organization through which a subject was enrolled on a ResearchStudy.
            study_arm:
                range: string
                description: The arm(s) of the study on which the Participant is enrolled
            associated_person:
                range: Person
                description: A reference to the Person entity that is associated with the Participant
            identity:
                populated_from: id
                range: string
                description: A unique identifier for a Participant
    ResearchStudy:
        populated_from: Investigation
        slot_derivations:
            identity:
                populated_from: id
            name:
                range: string
                description: An unabridged name of a research program, project, or study.
            name_shortened:
                range: string
                description: An abbreviated name of a research program, project, or study.
            description:
                range: string
                description: An unabridged description of a research program, project, or study.
            description_shortened:
                range: string
                description: An abbreviated description of a research program, project, or study.
            sponsor:
                range: string
                description: An entity that is responsible for the initiation, management, and/or financing of a research project.
            date_started:
                range: TimePoint
                description: The date when the research project began.
            date_ended:
                range: TimePoint
                description: The date when the research project ended.
            url:
                range: uriorcurie
                description: A URL address for a resource that provides information about a research program, project, or study.
            part_of:
                populated_from: part_of
                range: ResearchStudy
                description: A reference to a parent ResearchStudy (e.g. a link to the overarching CPTAC ResearchStudy from a substudy of CPTAC)
            research_project_type:
                range: string
                description: The 'type' of ResearchStudy represented (e.g. a broad-based Program like 'CPTAC' or a more focused Project like 'CPTAC PDAC Discovery Study')
            associated_timepoint:
                range: TimePoint
                description: A collection of timepoint observations that are relevant to research projects (e.g. date of IACUC approval, date of IRB approval, date of embargo end, etc.)
            principal_investigator:
                range: string
                description: The investigator or investigators leading a project.
            consent_code:
                range: DataUseEnum
                description: 'Data Use Restrictions that are used to indicate permissions/restrictions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. Based on the Data Use Ontology : see http://www.obofoundry.org/ontology/duo.html'
    Visit:
        is_a: Entity
        description: >-
            Events where Persons engage with the healthcare system for a duration of time. They are often also called “Encounters”. Visits are defined by a configuration of circumstances under which they occur, such as (i) whether the patient comes to a healthcare institution, the other way around, or the interaction is remote, (ii) whether and what kind of trained medical staff is delivering the service during the Visit, and (iii) whether the Visit is transient or for a longer period involving a stay in bed. (OMOP)
        slot_derivations:
            visit_category:
                range: VisitCategoryEnum
                description: A value representing the kind (or category) of visit, like inpatient or outpatient.
            age_at_visit_start:
                range: integer
                description: The age of the Participant (in days) at the start of the Visit.
            age_at_visit_end:
                range: integer
                description: The age of the Participant (in days) at the end of the Visit.
            visit_provenance:
                range: VisitProvenanceEnum
                description: A value representing the provenance of the visit record, or where the record comes from.
            associated_participant:
                range: Participant
                description: A reference to the Participant for whom this Visit occurred.
    Organization:
        is_a: Entity
        description: >-
            A grouping of people or organizations with a common purpose such as a data coordinating center, an university, or an institute within a university.
        slot_derivations:
            name:
                range: string
                description: The full legal name by which the organization is known (e.g. 'National Cancer Institute')
            alias:
                range: string
                description: A secondary name for the organization such as a short name or abbreviation (e.g. 'NCI')
            organization_type:
                range: string
                description: The type of the organization (e.g. 'Cancer Genome Characterization Center')
            identity:
                populated_from: id  
    TimePoint:
        is_a: Entity
        description: >-
              A structured representation of a single point in time that allows direct/explicit declaration as a dateTime, specification in terms of offset from a defined index, or description of an event type as a proxy for the time point when it occurred.
        slot_derivations:
            date_time:
                range: datetime
                description: An explicitly specified timepoint described in terms of a date and optionally a time on that date.
            index_time_point:
                range: TimePoint
                description: Another TimePoint from which this point is offset.
            offset_from_index:
                range: integer
                description: A quantity of time that, together with the index date or event, can be used to derive a specific timepoint.
            event_type:
                range: string
                description: An event that occurred at the point in time specified by this TimePoint.
    TimePeriod:
        description: >-
            A period of time between a start and end time point.
        slot_derivations:
            period_start:
                range: TimePoint
                description: When a period of time started.
            period_end:
                range: TimePoint
                description: When a period of time ended.
    ResearchStudyCollection:
        description: >-
            A holder for ResearchStudy objects
        slot_derivations:
            entries:
                range: ResearchStudy
    Questionnaire:
        is_a: Entity
        description: A Questionnaire is an organized collection of questions intended to solicit information from patients, providers or other individuals involved in the healthcare domain. They may be simple flat lists of questions or can be hierarchically organized in groups and sub-groups, each containing questions. The Questionnaire defines the questions to be asked, how they are ordered and grouped, any intervening instructional text and what the constraints are on the allowed answers. The results of a Questionnaire can be communicated using the QuestionnaireResponse. (FHIR)
        slot_derivations:
            name:
                description: Name for this Questionnaire (computer friendly)
                range: string
            title:
                description: Name for this Questionnaire (human friendly)
                range: string
            description:
                description: Natural language description of the Questionnaire
                range: string
            url:
                description: Canonical identifier for this Questionnaire, represented as an absolute URI (globally unique)
                range: uriorcurie
            version:
                description: The identifier that is used to identify this version of the questionnaire when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the questionnaire author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.
                range: string
            publisher:
                description: Name of the publisher/steward (organization or individual) of this Questionnaire
                range: string
            copyright:
                description: Textual description of any use and/or publishing restrictions
                range: string
            copyright_label:
                description: Copyright holder and year(s)
                range: string
            language:
                description: The language(s) in which questions are presented.
                range: string
            items:
                description: A collection of QuestionnaireItem objects which encapsulate the question being asked.
                range: QuestionnaireItem
    QuestionnaireItem:
        is_a: Entity
        description: QuestionnaireItem defines a question or section within the Questionnaire
        slot_derivations:
          text:
            range: string
            description: Name for group or question text
          code:
            range: string
            description: Corresponding concept for this item in a terminology
          part_of:
            range: QuestionnaireItem
            description: A reference to a parent QuestionnaireItem.
          identity:
            populated_from: id
    QuestionnaireResponse:
        is_a: Entity
        description: QuestionnaireResponse provides a complete or partial list of answers to a set of questions filled when responding to a questionnaire. (FHIR)
        slot_derivations:
          age_at_response:
            description: The age (in days) of the Participant when the QuestionnaireResponse was captured.
            range: integer
          items:
            description: A collection of QuestionnaireResponseItem objects which encapsulate the question being asked and the response.
            range: QuestionnaireResponseItem
          associated_visit:
            description: A reference to the Visit during which this QuestionnaireResponse was captured.
            range: Visit
    QuestionnaireResponseItem:
        description: QuestionnaireResponseItem provides a complete or partial list of answers to a set of questions filled when responding to a questionnaire. (FHIR)
        slot_derivations:
          has_questionnaire_item:
            range: QuestionnaireItem
            description: A reference to the QuestionnaireItem that this QuestionnaireResponseItem responds to.
          text:
            range: string
            description: Name for group or question text
          response_value:
            range: QuestionnaireResponseValue
    QuestionnaireResponseValue:
        description: Single-valued answer to the question. (FHIR)
        slot_derivations:
          type:
            range: string
          name:
            range: string
          value:
    QuestionnaireResponseValueDecimal:
        is_a: QuestionnaireResponseValue
        description: Single-valued decimal answer to the question
    QuestionnaireResponseValueBoolean:
        is_a: QuestionnaireResponseValue
        description: Single-valued boolean answer to the question
    QuestionnaireResponseValueString:
        is_a: QuestionnaireResponseValue
        description: Single-valued string answer to the question
    Condition:
        is_a: Entity
        description: >-
            Conditions are records of a Person suggesting the presence of a disease or medical condition stated as a diagnosis, a sign or a symptom, which is either observed by a Provider or reported by the patient. Conditions are recorded in different sources and levels of standardization.
        slot_derivations:
          condition_concept:
            range: ConditionConceptEnum
            description: The coded value for the presence of a disease or medical condition stated as a diagnosis, a sign or a symptom, coded to the Human Phenotype Ontology or MONDO.
          age_at_condition_start:
            range: integer
            description: The Participant's age (expressed in days) when the condition was first recorded.
          age_at_condition_end:
            range: integer
            description: The Participant's age (expressed in days) when the condition was recorded as having been resolved.
          condition_provenance:
            range: ConditionProvenanceEnum
            description: A value representing the provenance of the Condition record
          relationship_to_participant:
            range: string
            description: A value indicating the relationship between the Participant to which the Condition is attributed and the individual who had the reported Condition.  If the Condition is affecting the participant themselves, then 'Self' is the appropriate relationship.  If the Condition is affecting a family member (e.g. a parent of the Participant) then an appropriate relationship should be provided (e.g. 'Parent')
          associated_participant:
            range: Participant
            description: A reference to the Participant to which the Condition is attributed.
          associated_visit:
            description: A reference to the Visit during which this QuestionnaireResponse was captured.
            range: Visit
          identity:
            populated_from: id


""")

obj = {
    "id": "Person:1",
    "species": "Homo sapiens",
    "sex": "female",
    "age_at_death": 42,
    "vital_status": "dead"
}

# print(session.transform(obj))
print(yaml_dumper.dumps(session.target_schema))

dot = session.graphviz()
if isinstance(dot, graphviz.Digraph):
    dot.render('session_graph', format='png', cleanup=True)
    dot.view()
else:
    print("graphviz() did not return a Digraph object.")
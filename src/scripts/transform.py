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
-- # Class: "Container" Description: ""
--     * Slot: id Description: 
-- # Class: "DataObject" Description: "A DataFile Associated with a Subject or Investigation or MaterialEntity"
--     * Slot: id Description: 
-- # Class: "Investigation" Description: "General information about the Investigation"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: part_of Description: 
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "MaterialEntity" Description: "Physical entity that is an input our output of a process from a Subject"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: source Description: 
--     * Slot: Container_id Description: Autocreated FK slot
--     * Slot: volume_id Description: 
--     * Slot: concentration_id Description: 
-- # Class: "MaterialProcessing" Description: "A planned process which results in physical changes in a specified input material"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Participation" Description: "Subject/Study participation information"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: includes Description: 
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Process" Description: "A planned process resulting in a material or data"
--     * Slot: id Description: 
--     * Slot: name Description: 
-- # Class: "Quantity" Description: ""
--     * Slot: id Description: 
--     * Slot: has_raw_value Description: 
--     * Slot: has_numeric_value Description: 
--     * Slot: has_unit Description: 
--     * Slot: comparator Description: 
-- # Class: "SpecimenCollectionProcess" Description: "A planned process with the objective of collecting a specimen"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Subject" Description: "Demographic and clinical information about the subject"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Entity" Description: "Any resource that has its own identifier"
--     * Slot: uid Description: 
--     * Slot: id Description: 
-- # Class: "Person" Description: "Demographics and other administrative information about an individual or animal receiving care or other health-related services."
--     * Slot: uid Description: 
--     * Slot: species Description: The scientific binomial name for the species of the Person (e.g. Homo sapiens, Mus musculus, etc.). Values should be derived from the NCBI organismal taxonomy (http://purl.obolibrary.org/obo/ncbitaxon.owl).
--     * Slot: breed Description: A label given to a group of animals homogeneous in appearance and other characteristics that distinguish it from other animals of the same species. Values should be derived from the Vertebrate Breed Ontology (http://purl.obolibrary.org/obo/vbo.owl).
--     * Slot: sex Description: The biologic character or quality that distinguishes male and female from one another as expressed by analysis of the person's gonadal, morphologic (internal and external), chromosomal, and hormonal characteristics.
--     * Slot: ethnicity Description: An individual's self-described social and cultural grouping, specifically whether an individual describes themselves as Hispanic or Latino. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau
--     * Slot: race Description: An arbitrary classification of a taxonomic group that is a division of a species. It usually arises as a consequence of geographical isolation within a species and is characterized by shared heredity, physical attributes and behavior, and in the case of humans, by common history, nationality, or geographic distribution. The provided values are based on the categories defined by the U.S. Office of Management and Business and used by the U.S. Census Bureau.
--     * Slot: year_of_birth Description: Numeric value to represent the calendar year in which an individual was born.
--     * Slot: vital_status Description: Coded value indicating the state or condition of being living or deceased; also includes the case where the vital status is unknown.
--     * Slot: age_at_death Description: The age of an individual at the time of death, expressed in days since birth
--     * Slot: year_of_death Description: Numeric value to represent the calendar year in which an individual died.
--     * Slot: cause_of_death Description: Coded value indicating the circumstance or condition that results in the death of the individual.
--     * Slot: id Description: 
-- # Class: "Participant" Description: "A Participant is the entity of interest in a research study, typically a human being or an animal, but can also be a device, group of humans or animals, or a tissue sample. Human research subjects are usually not traceable to a particular person to protect the subject’s privacy."
--     * Slot: uid Description: 
--     * Slot: description Description: A free text field to capture additional info/explanation about the research subject.
--     * Slot: age_at_enrollment Description: The age in days when the Participant enrolled on the ResearchStudy
--     * Slot: index_timepoint Description: The text term used to describe the reference or anchor date used for date obfuscation, where a single date is obscured by creating one or more date ranges in relation to this date.
--     * Slot: id Description: 
--     * Slot: associated_person_uid Description: A reference to the Person that is associated with this record.
--     * Slot: member_of_research_study_uid Description: A reference to the Study(s) of which this Participant is a member
--     * Slot: originating_site_uid Description: The Organization through which a subject was enrolled on a ResearchStudy.
-- # Class: "ResearchStudy" Description: "A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge. This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques. A ResearchStudy involves the gathering of information about human or animal subjects."
--     * Slot: uid Description: 
--     * Slot: name Description: An unabridged name of a research program, project, or study.
--     * Slot: name_shortened Description: An abbreviated name of a research program, project, or study.
--     * Slot: description Description: An unabridged description of a research program, project, or study.
--     * Slot: description_shortened Description: An abbreviated description of a research program, project, or study.
--     * Slot: sponsor Description: An entity that is responsible for the initiation, management, and/or financing of a research project.
--     * Slot: url Description: A URL address for a resource that provides information about a research program, project, or study.
--     * Slot: research_project_type Description: The 'type' of ResearchStudy represented (e.g. a broad-based Program like 'CPTAC' or a more focused Project like 'CPTAC PDAC Discovery Study')
--     * Slot: id Description: 
--     * Slot: ResearchStudyCollection_id Description: Autocreated FK slot
--     * Slot: date_started_uid Description: The date when the research project began.
--     * Slot: date_ended_uid Description: The date when the research project ended.
--     * Slot: part_of_uid Description: A reference to a parent ResearchStudy (e.g. a link to the overarching CPTAC ResearchStudy from a substudy of CPTAC)
-- # Class: "Visit" Description: "Events where Persons engage with the healthcare system for a duration of time. They are often also called “Encounters”. Visits are defined by a configuration of circumstances under which they occur, such as (i) whether the patient comes to a healthcare institution, the other way around, or the interaction is remote, (ii) whether and what kind of trained medical staff is delivering the service during the Visit, and (iii) whether the Visit is transient or for a longer period involving a stay in bed. (OMOP)"
--     * Slot: uid Description: 
--     * Slot: visit_category Description: A value representing the kind (or category) of visit, like inpatient or outpatient.
--     * Slot: age_at_visit_start Description: The age of the Participant (in days) at the start of the Visit.
--     * Slot: age_at_visit_end Description: The age of the Participant (in days) at the end of the Visit.
--     * Slot: visit_provenance Description: A value representing the provenance of the visit record, or where the record comes from.
--     * Slot: id Description: 
--     * Slot: associated_participant_uid Description: A reference to the Participant for whom this Visit occurred.
-- # Class: "Organization" Description: "A grouping of people or organizations with a common purpose such as a data coordinating center, an university, or an institute within a university."
--     * Slot: uid Description: 
--     * Slot: name Description: The full legal name by which the organization is known (e.g. 'National Cancer Institute')
--     * Slot: alias Description: A secondary name for the organization such as a short name or abbreviation (e.g. 'NCI')
--     * Slot: organization_type Description: The type of the organization (e.g. 'Cancer Genome Characterization Center')
--     * Slot: id Description: 
-- # Class: "TimePoint" Description: "A structured representation of a single point in time that allows direct/explicit declaration as a dateTime, specification in terms of offset from a defined index, or description of an event type as a proxy for the time point when it occurred."
--     * Slot: uid Description: 
--     * Slot: date_time Description: An explicitly specified timepoint described in terms of a date and optionally a time on that date.
--     * Slot: offset_from_index Description: A quantity of time that, together with the index date or event, can be used to derive a specific timepoint.
--     * Slot: event_type Description: An event that occurred at the point in time specified by this TimePoint.
--     * Slot: id Description: 
--     * Slot: index_time_point_uid Description: Another TimePoint from which this point is offset.
-- # Class: "TimePeriod" Description: "A period of time between a start and end time point."
--     * Slot: id Description: 
--     * Slot: period_start_uid Description: When a period of time started.
--     * Slot: period_end_uid Description: When a period of time ended.
-- # Class: "Identifier" Description: "An Identifier is associated with a unique object or entity within a given system."
--     * Slot: id Description: 
--     * Slot: value Description: The value of the identifier, as defined by the system.
--     * Slot: system Description: The system or namespace that defines the identifier.
-- # Class: "ResearchStudyCollection" Description: "A holder for ResearchStudy objects"
--     * Slot: id Description: 
-- # Class: "Questionnaire" Description: "A Questionnaire is an organized collection of questions intended to solicit information from patients, providers or other individuals involved in the healthcare domain. They may be simple flat lists of questions or can be hierarchically organized in groups and sub-groups, each containing questions. The Questionnaire defines the questions to be asked, how they are ordered and grouped, any intervening instructional text and what the constraints are on the allowed answers. The results of a Questionnaire can be communicated using the QuestionnaireResponse. (FHIR)"
--     * Slot: uid Description: 
--     * Slot: name Description: Name for this Questionnaire (computer friendly)
--     * Slot: title Description: Name for this Questionnaire (human friendly)
--     * Slot: description Description: Natural language description of the Questionnaire
--     * Slot: url Description: Canonical identifier for this Questionnaire, represented as an absolute URI (globally unique)
--     * Slot: version Description: The identifier that is used to identify this version of the questionnaire when it is referenced in a specification, model, design or instance. This is an arbitrary value managed by the questionnaire author and is not expected to be globally unique. For example, it might be a timestamp (e.g. yyyymmdd) if a managed version is not available. There is also no expectation that versions can be placed in a lexicographical sequence.
--     * Slot: publisher Description: Name of the publisher/steward (organization or individual) of this Questionnaire
--     * Slot: copyright Description: Textual description of any use and/or publishing restrictions
--     * Slot: copyright_label Description: Copyright holder and year(s)
--     * Slot: id Description: 
-- # Class: "QuestionnaireItem" Description: "QuestionnaireItem defines a question or section within the Questionnaire"
--     * Slot: uid Description: 
--     * Slot: text Description: Name for group or question text
--     * Slot: code Description: Corresponding concept for this item in a terminology
--     * Slot: id Description: 
--     * Slot: part_of_uid Description: A reference to a parent QuestionnaireItem.
-- # Class: "QuestionnaireResponse" Description: "QuestionnaireResponse provides a complete or partial list of answers to a set of questions filled when responding to a questionnaire. (FHIR)"
--     * Slot: uid Description: 
--     * Slot: age_at_response Description: The age (in days) of the Participant when the QuestionnaireResponse was captured.
--     * Slot: id Description: 
--     * Slot: associated_visit_uid Description: A reference to the Visit during which this QuestionnaireResponse was captured.
-- # Class: "QuestionnaireResponseItem" Description: "QuestionnaireResponseItem provides a complete or partial list of answers to a set of questions filled when responding to a questionnaire. (FHIR)"
--     * Slot: id Description: 
--     * Slot: text Description: Name for group or question text
--     * Slot: has_questionnaire_item_uid Description: A reference to the QuestionnaireItem that this QuestionnaireResponseItem responds to.
--     * Slot: response_value_id Description: 
-- # Class: "QuestionnaireResponseValue" Description: "Single-valued answer to the question. (FHIR)"
--     * Slot: id Description: 
--     * Slot: value Description: A general slot to hold a value.
--     * Slot: type Description: 
--     * Slot: name Description: 
-- # Class: "QuestionnaireResponseValueDecimal" Description: "Single-valued decimal answer to the question"
--     * Slot: id Description: 
--     * Slot: value Description: A general slot to hold a value.
--     * Slot: type Description: 
--     * Slot: name Description: 
-- # Class: "QuestionnaireResponseValueBoolean" Description: "Single-valued boolean answer to the question"
--     * Slot: id Description: 
--     * Slot: value Description: A general slot to hold a value.
--     * Slot: type Description: 
--     * Slot: name Description: 
-- # Class: "QuestionnaireResponseValueString" Description: "Single-valued string answer to the question"
--     * Slot: id Description: 
--     * Slot: value Description: A general slot to hold a value.
--     * Slot: type Description: 
--     * Slot: name Description: 
-- # Class: "Condition" Description: "Conditions are records of a Person suggesting the presence of a disease or medical condition stated as a diagnosis, a sign or a symptom, which is either observed by a Provider or reported by the patient. Conditions are recorded in different sources and levels of standardization."
--     * Slot: uid Description: 
--     * Slot: condition_concept Description: The coded value for the presence of a disease or medical condition stated as a diagnosis, a sign or a symptom, coded to the Human Phenotype Ontology or MONDO.
--     * Slot: age_at_condition_start Description: The Participant's age (expressed in days) when the condition was first recorded.
--     * Slot: age_at_condition_end Description: The Participant's age (expressed in days) when the condition was recorded as having been resolved.
--     * Slot: condition_provenance Description: A value representing the provenance of the Condition record
--     * Slot: relationship_to_participant Description: A value indicating the relationship between the Participant to which the Condition is attributed and the individual who had the reported Condition.  If the Condition is affecting the participant themselves, then 'Self' is the appropriate relationship.  If the Condition is affecting a family member (e.g. a parent of the Participant) then an appropriate relationship should be provided (e.g. 'Parent')
--     * Slot: id Description: 
--     * Slot: associated_participant_uid Description: A reference to the Participant to which the Condition is attributed.
--     * Slot: associated_visit_uid Description: A reference to the Visit during which this QuestionnaireResponse was captured.
-- # Class: "MaterialEntity_used_in" Description: ""
--     * Slot: MaterialEntity_id Description: Autocreated FK slot
--     * Slot: used_in_id Description: 
-- # Class: "MaterialProcessing_has_input" Description: ""
--     * Slot: MaterialProcessing_id Description: Autocreated FK slot
--     * Slot: has_input_id Description: 
-- # Class: "MaterialProcessing_has_output" Description: ""
--     * Slot: MaterialProcessing_id Description: Autocreated FK slot
--     * Slot: has_output_id Description: 
-- # Class: "Participation_involved_in" Description: ""
--     * Slot: Participation_id Description: Autocreated FK slot
--     * Slot: involved_in_id Description: 
-- # Class: "Process_has_input" Description: ""
--     * Slot: Process_id Description: Autocreated FK slot
--     * Slot: has_input Description: 
-- # Class: "Process_has_output" Description: ""
--     * Slot: Process_id Description: Autocreated FK slot
--     * Slot: has_output Description: 
-- # Class: "SpecimenCollectionProcess_has_input" Description: ""
--     * Slot: SpecimenCollectionProcess_id Description: Autocreated FK slot
--     * Slot: has_input_id Description: 
-- # Class: "SpecimenCollectionProcess_has_output" Description: ""
--     * Slot: SpecimenCollectionProcess_id Description: Autocreated FK slot
--     * Slot: has_output_id Description: 
-- # Class: "Person_identity" Description: ""
--     * Slot: Person_uid Description: Autocreated FK slot
--     * Slot: identity_id Description: A 'business' identifier or accession number for the entity, typically as provided by an external system or authority, that are globally unique and persist across implementing systems. Also, since these identifiers are created outside the information system through a specific business process, the Identifier type has additional attributes to capture this additional metadata so the actual identifier values are qualified by the context that created those values. This additional context allows "identifier" instances to be transmitted as business data across systems while still being able to trace them back to the system of origin.
-- # Class: "Participant_identity" Description: ""
--     * Slot: Participant_uid Description: Autocreated FK slot
--     * Slot: identity_id Description: A 'business' identifier or accession number for the entity, typically as provided by an external system or authority, that are globally unique and persist across implementing systems. Also, since these identifiers are created outside the information system through a specific business process, the Identifier type has additional attributes to capture this additional metadata so the actual identifier values are qualified by the context that created those values. This additional context allows "identifier" instances to be transmitted as business data across systems while still being able to trace them back to the system of origin.
-- # Class: "Participant_study_arm" Description: ""
--     * Slot: Participant_uid Description: Autocreated FK slot
--     * Slot: study_arm Description: The arm(s) of the study on which the Participant is enrolled
-- # Class: "ResearchStudy_identity" Description: ""
--     * Slot: ResearchStudy_uid Description: Autocreated FK slot
--     * Slot: identity_id Description: A 'business' identifier or accession number for the entity, typically as provided by an external system or authority, that are globally unique and persist across implementing systems. Also, since these identifiers are created outside the information system through a specific business process, the Identifier type has additional attributes to capture this additional metadata so the actual identifier values are qualified by the context that created those values. This additional context allows "identifier" instances to be transmitted as business data across systems while still being able to trace them back to the system of origin.
-- # Class: "ResearchStudy_associated_timepoint" Description: ""
--     * Slot: ResearchStudy_uid Description: Autocreated FK slot
--     * Slot: associated_timepoint_uid Description: A collection of timepoint observations that are relevant to research projects (e.g. date of IACUC approval, date of IRB approval, date of embargo end, etc.)
-- # Class: "ResearchStudy_principal_investigator" Description: ""
--     * Slot: ResearchStudy_uid Description: Autocreated FK slot
--     * Slot: principal_investigator Description: The investigator or investigators leading a project.
-- # Class: "ResearchStudy_consent_code" Description: ""
--     * Slot: ResearchStudy_uid Description: Autocreated FK slot
--     * Slot: consent_code Description: Data Use Restrictions that are used to indicate permissions/restrictions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. Based on the Data Use Ontology : see http://www.obofoundry.org/ontology/duo.html
-- # Class: "Organization_identity" Description: ""
--     * Slot: Organization_uid Description: Autocreated FK slot
--     * Slot: identity_id Description: A 'business' identifier or accession number for the entity, typically as provided by an external system or authority, that are globally unique and persist across implementing systems. Also, since these identifiers are created outside the information system through a specific business process, the Identifier type has additional attributes to capture this additional metadata so the actual identifier values are qualified by the context that created those values. This additional context allows "identifier" instances to be transmitted as business data across systems while still being able to trace them back to the system of origin.
-- # Class: "Questionnaire_identity" Description: ""
--     * Slot: Questionnaire_uid Description: Autocreated FK slot
--     * Slot: identity_id Description: A 'business' identifier or accession number for the entity, typically as provided by an external system or authority, that are globally unique and persist across implementing systems. Also, since these identifiers are created outside the information system through a specific business process, the Identifier type has additional attributes to capture this additional metadata so the actual identifier values are qualified by the context that created those values. This additional context allows "identifier" instances to be transmitted as business data across systems while still being able to trace them back to the system of origin.
-- # Class: "Questionnaire_language" Description: ""
--     * Slot: Questionnaire_uid Description: Autocreated FK slot
--     * Slot: language Description: The language(s) in which questions are presented.
-- # Class: "Questionnaire_items" Description: ""
--     * Slot: Questionnaire_uid Description: Autocreated FK slot
--     * Slot: items_uid Description: A collection of QuestionnaireItem objects which encapsulate the question being asked.
-- # Class: "QuestionnaireItem_identity" Description: ""
--     * Slot: QuestionnaireItem_uid Description: Autocreated FK slot
--     * Slot: identity_id Description: A 'business' identifier or accession number for the entity, typically as provided by an external system or authority, that are globally unique and persist across implementing systems. Also, since these identifiers are created outside the information system through a specific business process, the Identifier type has additional attributes to capture this additional metadata so the actual identifier values are qualified by the context that created those values. This additional context allows "identifier" instances to be transmitted as business data across systems while still being able to trace them back to the system of origin.
-- # Class: "QuestionnaireResponse_items" Description: ""
--     * Slot: QuestionnaireResponse_uid Description: Autocreated FK slot
--     * Slot: items_id Description: A collection of QuestionnaireResponseItem objects which encapsulate the question being asked and the response.
-- # Class: "Condition_identity" Description: ""
--     * Slot: Condition_uid Description: Autocreated FK slot
--     * Slot: identity_id Description: A 'business' identifier or accession number for the entity, typically as provided by an external system or authority, that are globally unique and persist across implementing systems. Also, since these identifiers are created outside the information system through a specific business process, the Identifier type has additional attributes to capture this additional metadata so the actual identifier values are qualified by the context that created those values. This additional context allows "identifier" instances to be transmitted as business data across systems while still being able to trace them back to the system of origin.

CREATE TABLE "Container" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataObject" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Process" (
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Quantity" (
	id INTEGER NOT NULL, 
	has_raw_value TEXT, 
	has_numeric_value FLOAT, 
	has_unit TEXT, 
	comparator TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Entity" (
	uid INTEGER NOT NULL, 
	id TEXT, 
	PRIMARY KEY (uid)
);
CREATE TABLE "Person" (
	uid INTEGER NOT NULL, 
	species VARCHAR, 
	breed VARCHAR, 
	sex VARCHAR(7), 
	ethnicity VARCHAR(22), 
	race VARCHAR(41), 
	year_of_birth INTEGER, 
	vital_status VARCHAR(5), 
	age_at_death INTEGER, 
	year_of_death INTEGER, 
	cause_of_death TEXT, 
	id TEXT, 
	PRIMARY KEY (uid)
);
CREATE TABLE "Organization" (
	uid INTEGER NOT NULL, 
	name TEXT, 
	alias TEXT, 
	organization_type TEXT, 
	id TEXT, 
	PRIMARY KEY (uid)
);
CREATE TABLE "TimePoint" (
	uid INTEGER NOT NULL, 
	date_time DATETIME, 
	offset_from_index INTEGER, 
	event_type TEXT, 
	id TEXT, 
	index_time_point_uid INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(index_time_point_uid) REFERENCES "TimePoint" (uid)
);
CREATE TABLE "Identifier" (
	id INTEGER NOT NULL, 
	value TEXT NOT NULL, 
	system TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ResearchStudyCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Questionnaire" (
	uid INTEGER NOT NULL, 
	name TEXT, 
	title TEXT, 
	description TEXT, 
	url TEXT, 
	version TEXT, 
	publisher TEXT, 
	copyright TEXT, 
	copyright_label TEXT, 
	id TEXT, 
	PRIMARY KEY (uid)
);
CREATE TABLE "QuestionnaireItem" (
	uid INTEGER NOT NULL, 
	text TEXT, 
	code TEXT, 
	id TEXT, 
	part_of_uid INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(part_of_uid) REFERENCES "QuestionnaireItem" (uid)
);
CREATE TABLE "QuestionnaireResponseValue" (
	id INTEGER NOT NULL, 
	value TEXT, 
	type TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "QuestionnaireResponseValueDecimal" (
	id INTEGER NOT NULL, 
	value INTEGER NOT NULL, 
	type TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "QuestionnaireResponseValueBoolean" (
	id INTEGER NOT NULL, 
	value BOOLEAN NOT NULL, 
	type TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "QuestionnaireResponseValueString" (
	id INTEGER NOT NULL, 
	value TEXT NOT NULL, 
	type TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Investigation" (
	id TEXT NOT NULL, 
	name TEXT, 
	part_of TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(part_of) REFERENCES "Investigation" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "MaterialProcessing" (
	id TEXT NOT NULL, 
	name TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "SpecimenCollectionProcess" (
	id TEXT NOT NULL, 
	name TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Subject" (
	id TEXT NOT NULL, 
	name TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "ResearchStudy" (
	uid INTEGER NOT NULL, 
	name TEXT, 
	name_shortened TEXT, 
	description TEXT, 
	description_shortened TEXT, 
	sponsor TEXT, 
	url TEXT, 
	research_project_type TEXT, 
	id TEXT, 
	"ResearchStudyCollection_id" INTEGER, 
	date_started_uid INTEGER, 
	date_ended_uid INTEGER, 
	part_of_uid INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY("ResearchStudyCollection_id") REFERENCES "ResearchStudyCollection" (id), 
	FOREIGN KEY(date_started_uid) REFERENCES "TimePoint" (uid), 
	FOREIGN KEY(date_ended_uid) REFERENCES "TimePoint" (uid), 
	FOREIGN KEY(part_of_uid) REFERENCES "ResearchStudy" (uid)
);
CREATE TABLE "TimePeriod" (
	id INTEGER NOT NULL, 
	period_start_uid INTEGER, 
	period_end_uid INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(period_start_uid) REFERENCES "TimePoint" (uid), 
	FOREIGN KEY(period_end_uid) REFERENCES "TimePoint" (uid)
);
CREATE TABLE "QuestionnaireResponseItem" (
	id INTEGER NOT NULL, 
	text TEXT, 
	has_questionnaire_item_uid INTEGER, 
	response_value_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_questionnaire_item_uid) REFERENCES "QuestionnaireItem" (uid), 
	FOREIGN KEY(response_value_id) REFERENCES "QuestionnaireResponseValue" (id)
);
CREATE TABLE "Process_has_input" (
	"Process_id" TEXT, 
	has_input TEXT, 
	PRIMARY KEY ("Process_id", has_input), 
	FOREIGN KEY("Process_id") REFERENCES "Process" (id)
);
CREATE TABLE "Process_has_output" (
	"Process_id" TEXT, 
	has_output TEXT, 
	PRIMARY KEY ("Process_id", has_output), 
	FOREIGN KEY("Process_id") REFERENCES "Process" (id)
);
CREATE TABLE "Person_identity" (
	"Person_uid" INTEGER, 
	identity_id INTEGER, 
	PRIMARY KEY ("Person_uid", identity_id), 
	FOREIGN KEY("Person_uid") REFERENCES "Person" (uid), 
	FOREIGN KEY(identity_id) REFERENCES "Identifier" (id)
);
CREATE TABLE "Organization_identity" (
	"Organization_uid" INTEGER, 
	identity_id INTEGER, 
	PRIMARY KEY ("Organization_uid", identity_id), 
	FOREIGN KEY("Organization_uid") REFERENCES "Organization" (uid), 
	FOREIGN KEY(identity_id) REFERENCES "Identifier" (id)
);
CREATE TABLE "Questionnaire_identity" (
	"Questionnaire_uid" INTEGER, 
	identity_id INTEGER, 
	PRIMARY KEY ("Questionnaire_uid", identity_id), 
	FOREIGN KEY("Questionnaire_uid") REFERENCES "Questionnaire" (uid), 
	FOREIGN KEY(identity_id) REFERENCES "Identifier" (id)
);
CREATE TABLE "Questionnaire_language" (
	"Questionnaire_uid" INTEGER, 
	language TEXT, 
	PRIMARY KEY ("Questionnaire_uid", language), 
	FOREIGN KEY("Questionnaire_uid") REFERENCES "Questionnaire" (uid)
);
CREATE TABLE "Questionnaire_items" (
	"Questionnaire_uid" INTEGER, 
	items_uid INTEGER NOT NULL, 
	PRIMARY KEY ("Questionnaire_uid", items_uid), 
	FOREIGN KEY("Questionnaire_uid") REFERENCES "Questionnaire" (uid), 
	FOREIGN KEY(items_uid) REFERENCES "QuestionnaireItem" (uid)
);
CREATE TABLE "QuestionnaireItem_identity" (
	"QuestionnaireItem_uid" INTEGER, 
	identity_id INTEGER, 
	PRIMARY KEY ("QuestionnaireItem_uid", identity_id), 
	FOREIGN KEY("QuestionnaireItem_uid") REFERENCES "QuestionnaireItem" (uid), 
	FOREIGN KEY(identity_id) REFERENCES "Identifier" (id)
);
CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	source TEXT, 
	"Container_id" INTEGER, 
	volume_id INTEGER, 
	concentration_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(source) REFERENCES "Subject" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id), 
	FOREIGN KEY(volume_id) REFERENCES "Quantity" (id), 
	FOREIGN KEY(concentration_id) REFERENCES "Quantity" (id)
);
CREATE TABLE "Participation" (
	id TEXT NOT NULL, 
	name TEXT, 
	includes TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(includes) REFERENCES "Subject" (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Participant" (
	uid INTEGER NOT NULL, 
	description TEXT, 
	age_at_enrollment INTEGER, 
	index_timepoint TEXT, 
	id TEXT, 
	associated_person_uid INTEGER, 
	member_of_research_study_uid INTEGER, 
	originating_site_uid INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(associated_person_uid) REFERENCES "Person" (uid), 
	FOREIGN KEY(member_of_research_study_uid) REFERENCES "ResearchStudy" (uid), 
	FOREIGN KEY(originating_site_uid) REFERENCES "Organization" (uid)
);
CREATE TABLE "SpecimenCollectionProcess_has_input" (
	"SpecimenCollectionProcess_id" TEXT, 
	has_input_id TEXT, 
	PRIMARY KEY ("SpecimenCollectionProcess_id", has_input_id), 
	FOREIGN KEY("SpecimenCollectionProcess_id") REFERENCES "SpecimenCollectionProcess" (id), 
	FOREIGN KEY(has_input_id) REFERENCES "Subject" (id)
);
CREATE TABLE "ResearchStudy_identity" (
	"ResearchStudy_uid" INTEGER, 
	identity_id INTEGER, 
	PRIMARY KEY ("ResearchStudy_uid", identity_id), 
	FOREIGN KEY("ResearchStudy_uid") REFERENCES "ResearchStudy" (uid), 
	FOREIGN KEY(identity_id) REFERENCES "Identifier" (id)
);
CREATE TABLE "ResearchStudy_associated_timepoint" (
	"ResearchStudy_uid" INTEGER, 
	associated_timepoint_uid INTEGER, 
	PRIMARY KEY ("ResearchStudy_uid", associated_timepoint_uid), 
	FOREIGN KEY("ResearchStudy_uid") REFERENCES "ResearchStudy" (uid), 
	FOREIGN KEY(associated_timepoint_uid) REFERENCES "TimePoint" (uid)
);
CREATE TABLE "ResearchStudy_principal_investigator" (
	"ResearchStudy_uid" INTEGER, 
	principal_investigator TEXT, 
	PRIMARY KEY ("ResearchStudy_uid", principal_investigator), 
	FOREIGN KEY("ResearchStudy_uid") REFERENCES "ResearchStudy" (uid)
);
CREATE TABLE "ResearchStudy_consent_code" (
	"ResearchStudy_uid" INTEGER, 
	consent_code VARCHAR(6), 
	PRIMARY KEY ("ResearchStudy_uid", consent_code), 
	FOREIGN KEY("ResearchStudy_uid") REFERENCES "ResearchStudy" (uid)
);
CREATE TABLE "Visit" (
	uid INTEGER NOT NULL, 
	visit_category VARCHAR(28), 
	age_at_visit_start INTEGER, 
	age_at_visit_end INTEGER, 
	visit_provenance VARCHAR(37), 
	id TEXT, 
	associated_participant_uid INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(associated_participant_uid) REFERENCES "Participant" (uid)
);
CREATE TABLE "MaterialEntity_used_in" (
	"MaterialEntity_id" TEXT, 
	used_in_id TEXT, 
	PRIMARY KEY ("MaterialEntity_id", used_in_id), 
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id), 
	FOREIGN KEY(used_in_id) REFERENCES "Investigation" (id)
);
CREATE TABLE "MaterialProcessing_has_input" (
	"MaterialProcessing_id" TEXT, 
	has_input_id TEXT, 
	PRIMARY KEY ("MaterialProcessing_id", has_input_id), 
	FOREIGN KEY("MaterialProcessing_id") REFERENCES "MaterialProcessing" (id), 
	FOREIGN KEY(has_input_id) REFERENCES "MaterialEntity" (id)
);
CREATE TABLE "MaterialProcessing_has_output" (
	"MaterialProcessing_id" TEXT, 
	has_output_id TEXT, 
	PRIMARY KEY ("MaterialProcessing_id", has_output_id), 
	FOREIGN KEY("MaterialProcessing_id") REFERENCES "MaterialProcessing" (id), 
	FOREIGN KEY(has_output_id) REFERENCES "MaterialEntity" (id)
);
CREATE TABLE "Participation_involved_in" (
	"Participation_id" TEXT, 
	involved_in_id TEXT, 
	PRIMARY KEY ("Participation_id", involved_in_id), 
	FOREIGN KEY("Participation_id") REFERENCES "Participation" (id), 
	FOREIGN KEY(involved_in_id) REFERENCES "Investigation" (id)
);
CREATE TABLE "SpecimenCollectionProcess_has_output" (
	"SpecimenCollectionProcess_id" TEXT, 
	has_output_id TEXT, 
	PRIMARY KEY ("SpecimenCollectionProcess_id", has_output_id), 
	FOREIGN KEY("SpecimenCollectionProcess_id") REFERENCES "SpecimenCollectionProcess" (id), 
	FOREIGN KEY(has_output_id) REFERENCES "MaterialEntity" (id)
);
CREATE TABLE "Participant_identity" (
	"Participant_uid" INTEGER, 
	identity_id INTEGER, 
	PRIMARY KEY ("Participant_uid", identity_id), 
	FOREIGN KEY("Participant_uid") REFERENCES "Participant" (uid), 
	FOREIGN KEY(identity_id) REFERENCES "Identifier" (id)
);
CREATE TABLE "Participant_study_arm" (
	"Participant_uid" INTEGER, 
	study_arm TEXT, 
	PRIMARY KEY ("Participant_uid", study_arm), 
	FOREIGN KEY("Participant_uid") REFERENCES "Participant" (uid)
);
CREATE TABLE "QuestionnaireResponse" (
	uid INTEGER NOT NULL, 
	age_at_response INTEGER, 
	id TEXT, 
	associated_visit_uid INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(associated_visit_uid) REFERENCES "Visit" (uid)
);
CREATE TABLE "Condition" (
	uid INTEGER NOT NULL, 
	condition_concept VARCHAR, 
	age_at_condition_start INTEGER, 
	age_at_condition_end INTEGER, 
	condition_provenance VARCHAR(31), 
	relationship_to_participant TEXT, 
	id TEXT, 
	associated_participant_uid INTEGER, 
	associated_visit_uid INTEGER, 
	PRIMARY KEY (uid), 
	FOREIGN KEY(associated_participant_uid) REFERENCES "Participant" (uid), 
	FOREIGN KEY(associated_visit_uid) REFERENCES "Visit" (uid)
);
CREATE TABLE "QuestionnaireResponse_items" (
	"QuestionnaireResponse_uid" INTEGER, 
	items_id INTEGER NOT NULL, 
	PRIMARY KEY ("QuestionnaireResponse_uid", items_id), 
	FOREIGN KEY("QuestionnaireResponse_uid") REFERENCES "QuestionnaireResponse" (uid), 
	FOREIGN KEY(items_id) REFERENCES "QuestionnaireResponseItem" (id)
);
CREATE TABLE "Condition_identity" (
	"Condition_uid" INTEGER, 
	identity_id INTEGER, 
	PRIMARY KEY ("Condition_uid", identity_id), 
	FOREIGN KEY("Condition_uid") REFERENCES "Condition" (uid), 
	FOREIGN KEY(identity_id) REFERENCES "Identifier" (id)
);
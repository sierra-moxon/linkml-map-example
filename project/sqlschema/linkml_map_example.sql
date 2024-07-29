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
CREATE TABLE "SpecimenCollectionProcess_has_input" (
	"SpecimenCollectionProcess_id" TEXT, 
	has_input_id TEXT, 
	PRIMARY KEY ("SpecimenCollectionProcess_id", has_input_id), 
	FOREIGN KEY("SpecimenCollectionProcess_id") REFERENCES "SpecimenCollectionProcess" (id), 
	FOREIGN KEY(has_input_id) REFERENCES "Subject" (id)
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
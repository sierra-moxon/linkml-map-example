-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: id Description: A unique identifier for a thing
-- # Class: "Person" Description: "Represents a Sample"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: first_name Description: A human-readable first name for a Person
--     * Slot: last_name Description: A human-readable last name for a Person
--     * Slot: PersonCollection_id Description: Autocreated FK slot
-- # Class: "PersonCollection" Description: "A holder for Sample objects"
--     * Slot: id Description: 

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PersonCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	first_name TEXT, 
	last_name TEXT, 
	"PersonCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("PersonCollection_id") REFERENCES "PersonCollection" (id)
);
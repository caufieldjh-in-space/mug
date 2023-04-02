

CREATE TABLE "Address" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	addressee TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Company" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	company_name TEXT, 
	work_address TEXT, 
	industry TEXT, 
	slogan TEXT, 
	logo_description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "FullName" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "GeneratedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "GeneratedThingCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	full_name TEXT, 
	work_address TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(full_name) REFERENCES "FullName" (id)
);

CREATE TABLE "WorkingAddress" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	addressee TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(addressee) REFERENCES "Company" (id)
);

CREATE TABLE "Address_address_number" (
	backref_id TEXT, 
	address_number TEXT, 
	PRIMARY KEY (backref_id, address_number), 
	FOREIGN KEY(backref_id) REFERENCES "Address" (id)
);

CREATE TABLE "Address_street" (
	backref_id TEXT, 
	street TEXT, 
	PRIMARY KEY (backref_id, street), 
	FOREIGN KEY(backref_id) REFERENCES "Address" (id)
);

CREATE TABLE "Address_locality" (
	backref_id TEXT, 
	locality TEXT, 
	PRIMARY KEY (backref_id, locality), 
	FOREIGN KEY(backref_id) REFERENCES "Address" (id)
);

CREATE TABLE "FullName_given_name" (
	backref_id TEXT, 
	given_name TEXT, 
	PRIMARY KEY (backref_id, given_name), 
	FOREIGN KEY(backref_id) REFERENCES "FullName" (id)
);

CREATE TABLE "FullName_family_name" (
	backref_id TEXT, 
	family_name TEXT, 
	PRIMARY KEY (backref_id, family_name), 
	FOREIGN KEY(backref_id) REFERENCES "FullName" (id)
);

CREATE TABLE "FullName_other_name" (
	backref_id TEXT, 
	other_name TEXT, 
	PRIMARY KEY (backref_id, other_name), 
	FOREIGN KEY(backref_id) REFERENCES "FullName" (id)
);

CREATE TABLE "FullName_preferred_name" (
	backref_id TEXT, 
	preferred_name TEXT, 
	PRIMARY KEY (backref_id, preferred_name), 
	FOREIGN KEY(backref_id) REFERENCES "FullName" (id)
);

CREATE TABLE "FullName_title" (
	backref_id TEXT, 
	title TEXT, 
	PRIMARY KEY (backref_id, title), 
	FOREIGN KEY(backref_id) REFERENCES "FullName" (id)
);

CREATE TABLE "FullName_suffix" (
	backref_id TEXT, 
	suffix TEXT, 
	PRIMARY KEY (backref_id, suffix), 
	FOREIGN KEY(backref_id) REFERENCES "FullName" (id)
);

CREATE TABLE "ResidentialAddress" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	addressee TEXT NOT NULL, 
	"Person_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(addressee) REFERENCES "Person" (id), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);

CREATE TABLE "WorkingAddress_address_number" (
	backref_id TEXT, 
	address_number TEXT, 
	PRIMARY KEY (backref_id, address_number), 
	FOREIGN KEY(backref_id) REFERENCES "WorkingAddress" (id)
);

CREATE TABLE "WorkingAddress_street" (
	backref_id TEXT, 
	street TEXT, 
	PRIMARY KEY (backref_id, street), 
	FOREIGN KEY(backref_id) REFERENCES "WorkingAddress" (id)
);

CREATE TABLE "WorkingAddress_locality" (
	backref_id TEXT, 
	locality TEXT, 
	PRIMARY KEY (backref_id, locality), 
	FOREIGN KEY(backref_id) REFERENCES "WorkingAddress" (id)
);

CREATE TABLE "ResidentialAddress_address_number" (
	backref_id TEXT, 
	address_number TEXT, 
	PRIMARY KEY (backref_id, address_number), 
	FOREIGN KEY(backref_id) REFERENCES "ResidentialAddress" (id)
);

CREATE TABLE "ResidentialAddress_street" (
	backref_id TEXT, 
	street TEXT, 
	PRIMARY KEY (backref_id, street), 
	FOREIGN KEY(backref_id) REFERENCES "ResidentialAddress" (id)
);

CREATE TABLE "ResidentialAddress_locality" (
	backref_id TEXT, 
	locality TEXT, 
	PRIMARY KEY (backref_id, locality), 
	FOREIGN KEY(backref_id) REFERENCES "ResidentialAddress" (id)
);

/*
 * Data Modeling
 * 
 * OLTP rendszerek - Normal Forms - Normál formákat - 3rd normal format
 * 
 * OLAP rendszerek - Kimball EDW - Dimenzionális modellezést 
 * 							- Csillagséma - Starschema
 * 							- Hópehelyséma - Snowflake
 *
 * 				   - Inmon CIF - lesz olyan rétege a megoldásodnak, amely 3rd normal form
 * 							   - lesz olyan rétege, amely dimenzionálisat
 * 				
 * 				   - Data Vault 2.0
 * 
 *                 - Data Lake  - denormalizáltan tárolod az adatokat
 *  
 * 
 * Data modelling
 * 
 * 3 lépése:
 * 
 * Conceptual data model
 * Nem tartalmazza a részletes struktúrát a mezőkre vonatkozóan, 
 * maximum a kapcsolatot a táblák között jelzi.
 *
 * 
 * Logikai adatmodell
 * A tábla szerkezetét pontosan definiálja
 * oszlopok adattipusa, constraintek
 * Kapcsolat a táblák között
 * 
 * Fizikai adatmodell:
 * Maga a create és egyéb scriptek, az adatbázisban létrehozva.
 * 
	Employee table	
	pk	Employee_id	100
		Employee_Name	Mekk Odüsszeus
		Salary	10
		Start_date	2023.10.11
	foreign_key	Job_Id	1

 * 
 * 	Jobs	
	pk	Job_id	1
		Job_name	Cloud Engineer
foreign_key	Department_ID	1

 * 		Department	
	pk	Department_id	1
		Department_name	IT

 * 
 * Primary key constraint:
 * Not null és az értéknek egyedinek kell lennie
 * Ezt úgy oldja meg az adatbázisok többsége,
 * hogy egy unique indexet hoz létre a mezőn
 * 
 * */

select now();

create table departments (
	department_id serial primary key,
	department_name varchar(25) not null, --not null constraint - nem kaphat az oszlop null / üres értéket
	created_date date default now(),
	last_updated_date date
);

create table jobs (
	job_id serial primary key,
	job_name varchar(50),
	department_id integer,
    CONSTRAINT fk_department FOREIGN KEY (department_id)
    REFERENCES departments(department_id)	
);

create table employee (
	employee_id serial primary key,
	employee_name varchar(100),
	salary integer,
	start_date date,
	job_id integer,
	CONSTRAINT fk_jobs FOREIGN KEY (job_id)
    REFERENCES jobs(job_id)
);

INSERT INTO public.departments
(department_name)
VALUES('IT'),
	  ('HR'),
	  ('CEO');

select *from departments;
-------------------------------------------------------------

INSERT INTO public.jobs
(job_name, department_id)
VALUES('Cloud Engineer', 1),
	  ('Data Engineer', 1),
	  ('HR Generalista', 2),
	  ('CEO', 3);

select * from jobs;
-------------------------------------------

INSERT INTO public.employee
(employee_name, salary, job_id)
VALUES('Fekete Péter', 40, 4),
		('Józska Pista', 5, 3);

select * from employee;

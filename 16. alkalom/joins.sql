/*
 * Táblák összekapcsolása
 * 
 * JOIN műveletek
 * 
 * 
 * 
 * */

-- Melyik employee-nak mi a munkaköre?

explain analyze select * from employee e where e.job_id > 1;
select * from jobs;
explain analyze select * from departments;

select
e.*,
j.job_name
from 
employee e,
jobs j
where e.job_id = j.job_id;


INSERT INTO departments (department_name, created_date, last_updated_date) VALUES
('Legal', '2025-01-23', NULL),
('Research', '2025-01-23', NULL),
('Security', '2025-01-23', NULL),
('Facility', '2025-01-23', NULL);

INSERT INTO jobs (job_name, department_id) VALUES
('Legal Advisor', 6),  -- A department_id = 6 nem szerepelt eddig
('Scientist', 7); 


/*
 * -- Melyik employee-nak mi a munkaköre és melyik departmentben dolgozik?
 * INNER JOIN
 * közös metszet 2 tábla között
 * 
 * */
explain analyse select
e.employee_id, e.employee_name, j.job_name, d.department_name 
from
employee e
inner join jobs j on e.job_id = j.job_id
inner join departments d on j.department_id = d.department_id
where e.employee_name = 'Alice Johnson' 
;

explain analyse select
e.employee_id, e.employee_name, j.job_name, d.department_name 
from
employee e
inner join jobs j on e.job_id = j.job_id and e.employee_name = 'Alice Johnson' 
inner join departments d on j.department_id = d.department_id
;

explain analyse select
e.employee_id, e.employee_name, j.job_name, d.department_name 
from
(select * from employee where employee_name ='Alice Johnson') e
inner join jobs j on e.job_id = j.job_id 
inner join departments d on j.department_id = d.department_id


/*
 * LEFT JOIN
 * balról mindent, jobbról meg a közös
 * 
 * */


select * from employee;
select * from ;
select * from jobs;


select * from departments d left join jobs j on d.department_id = j.department_id
where j.job_id is not null;


/*
 * RIGHT JOIN
 * 
 * jobbról mindent, balról csak a közös
 * 
 * */

select * from jobs j right join departments d on d.department_id = j.department_id

select * from employee e right join jobs j on e.job_id = j.job_id
where e.employee_id is null;

/*
 * FULL OUTER JOIN
 * mindenből mindent
 * 
 * 
 * */

select * from
employee e
full outer join jobs j on e.job_id = j.job_id
full outer join departments d on j.department_id = d.department_id;

select * from employee e
cross join departments; -- Descartes szorzat




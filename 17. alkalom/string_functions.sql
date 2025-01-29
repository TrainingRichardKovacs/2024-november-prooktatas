/*
 * CTE - Common Table Expression 
 * 
 * with
 * 
 * 
		 WITH cte_name AS (
		    SELECT column1, column2, ...
		    FROM table_name
		    WHERE conditions
		)
		SELECT * 
		FROM cte_name;
 * 
 * 
 * */

select * from ( 
select sum(base.salary) from 
 (select e.* from employee e
 where employee_name like '%ll%') base) a;

with base_data as (
	select * from employee e
	where employee_name like '%ll%'
), sum_salary as (
	select sum(b.salary) from base_data b
), cnt_employee as (
	select count(*) from base_data b
), list_jobs as (
	select * from jobs
)
select * from list_jobs

;


/*
 * string functions
 * 
 * concatenation
 * 
 * || vs concat()
 * 
 * */

select e.employee_id || '-' || e.employee_name || ' ? ' || e.job_id,
concat(e.employee_id, e.employee_name),
concat_ws('-', e.employee_id, e.employee_name, ' ? ', e.job_id)
from employee e;


/*
 * substring
 * 
 * */

select e.employee_name,
substring(e.employee_name, 1, 3) from employee e;

/*
 * instr
 * 
 * */
select e.employee_name,
position('J' in e.employee_name),
substring(e.employee_name, position('J' in e.employee_name))
from employee e
where e.employee_name like '% J%';


/**
 * Szedjük ketté az employee_name mezőt firstname és lastname-re
 * /
select e.employee_name,
substring(e.employee_name, 1, 3) from employee e;
*/
with base_data as (
	select
		e.employee_name,
		position(' ' in e.employee_name) as space_cnt
	from employee e
), name_modification as (
	select
		b.employee_name,
		substring(b.employee_name, 1, b.space_cnt -1) as firstname,
		substring(b.employee_name, b.space_cnt + 1) as lastname
	from base_data b
)
select * from name_modification;


select
e.employee_name,
bit_length(e.employee_name),
char_length(e.employee_name ),
substring(e.employee_name, 1, position(' ' in e.employee_name) -1) as firstname,
substring(e.employee_name, position(' ' in e.employee_name) + 1) as lastname
from employee e;

select char_length('aaalmafa'), length('aaalmafa');


--- replace function

select
e.employee_name,
replace(e.employee_name, 'J', 'K')
from employee e;



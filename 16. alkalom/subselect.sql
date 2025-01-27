/*
 * Subquery
 * 
 * select * from 
 * (select * from employee e
 * where employee_name like '%ll%') base
 * 
 * Egy select-et zárójelekbe téve, "táblaként" tudunk használni
 * 
 * with
 * 
 * */


select * from ( 
select base.* from 
 (select e.employee_id from employee e
 where employee_name like '%ll%') base) a;
 
 
 
 
 select * from
 (select
sum(e.salary)over(partition by e.job_id) as sum_salary_by_job,
count(e.employee_id)over(partition by e.job_id) as cnt_employee,
min(e.salary)over(partition by e.job_id) as min_salary,
max(e.salary)over(partition by e.job_id) as max_salary,
avg(e.salary)over(partition by e.job_id) as avg_salary,
e.*
from employee e
order by sum_salary_by_job desc) base_record;

explain analyse select
*
from
employee e
right join jobs j on e.job_id = j.job_id
where e.job_id is null;

explain analyze select * from jobs j
where j.job_id not in (select distinct e.job_id d from employee e);

-- EXISTS
explain analyze select * from jobs j
where not exists (select distinct e.job_id d from employee e where j.job_id = e.job_id);

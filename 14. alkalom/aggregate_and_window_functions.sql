/*
 * SQL nyelv
 * 
 * DDL, DML, TCL, DQL
 * 
 * 
 * Data Query Language
 * select utasitás
 * 
 * from tábla_neve -> melyik táblából szeretnéd az adatokat lekérdezni
 * 
 * select from -> a select és from közötti rész szolgál arra
 * hogy megadjuk a lekérdezésnek, hogy az adott adatset-ből mely oszlopokat
 * akarom megjeleniteni illetve adott esetben
 * mely oszlopokon szeretnék valamilyen sql műveletet elvégezni
 * 
 * */

--- select * -> minden mezőt adj vissza a megadott lekérdezésből
select * from employee;

-- alias -> column_name as new_column_name -> az alias nem nevezi át a táblában
-- a mezők neveit, és a táblát sem
-- stg_new_customer_orders -> snco
--select e.employee_name as full_name, e.employee_id from employee as e;
select e.employee_name as full_name, e.employee_id from employee e;
select employee.employee_name, employee.employee_id from employee;

--- A dolgozó neve
-- ne használjátok
select e.employee_name as "A dolgozó neve" from employee e;

-----------------------------------------------------------------------------------

-- filtering - where utasitás
select e.* from employee e
where 1 = 1 and
--e.employee_id = 2;
--e.employee_id in (2, 3)
e.employee_id not in (2, 3)
and e.salary > 10
;


select e.* from employee e
where 1 = 1 and
--e.employee_name = 'Mekk Elek'
--e.employee_name in ('Mekk Elek', 'Lapos Elemér')
--e.employee_name not in ('Mekk Elek', 'Lapos Elemér')
-- wildcard utasitások: %, _ 
--e.employee_name like '%Elemér' -- tudom, hogy az Elemér szó a string végén van
e.employee_name like '%Elemér%' -- nem tudom, hogy hol lehet az Elemér
e.employee_name like ''
;

select * from (
select 'kever' as valami
union all
select 'kavar' as valami
union all
select 'kövér' as valami) t
where --t.valami like 'k_v_r' -- k_v_r -> k és a v után 1 akármilyen karakter állhat,
t.valami like '%vér%'
;

---------------------------------------------------------------------------
-- group by clause -> csoportositás -> aggregate függvények használata miatt
-- aggregate functions: sum, count, avg, min, max
/*
 * count - megszámolja, hogy hány darab record tartozik egy csoporthoz
 * sum   - a csoporton belüli adatokat összeadja
 * avg   - a csoporton belüli adatokat átlagolja
 * min	 - a csoporton belüli adatok közzül adja vissza a legkisebbet
 * max   - a csoporton belüli adatok közzül adja vissza a legnagyobbat
 * 
 * */
-- ANSI SQL-t 

select
--count(e.employee_id),
sum(e.salary) as sum_salary,
min(e.salary) as min_salary,
max(e.salary) as max_salary,
count(e.employee_id) as cnt_employee,
avg(e.salary) as avg_salary,
e.employee_name
from employee e
--where 1 = 1
group by e.start_date, e.employee_name
;
------------------------------------------------------------------
--- ha van group by a having mindig a group by után van
--- ha nincs group by, de van where, akkor a where feltétel után van a having
--- ha nincs group by és nincs where akkor a from után a having a következő

select
sum(e.salary) as sum_salary,
e.employee_id
from employee e
where 1 = 1
group by e.employee_id
having sum(e.salary) > 10
;
-----------------------------------------
-- sorrendbe rakás - order by, alapvetőne növekvő sorrend -> asc
-- csökkenő sorrend order by col_name desc


select
e.employee_id,
sum(e.salary) as sum_salary
from employee e
where 1 = 1
group by e.employee_id
having sum(e.salary) > 10
order by sum_salary desc 
--order by 1 desc
;


---
select * from employee e
order by e.salary asc, e.job_id desc;
----------------------------------------------
-- Add vissza, ki kereste a legtöbb pénzt

select max(e.salary) from employee e;

select e.employee_name from employee e
order by e.salary desc
limit 3;
----------------------------------------------------------------------------
--- Analitikus függvények - window function
---
--- rangsor: row_number, rank, dense_rank
--  row_number()over(partition by col_names order by col_names)
--  lead(), lag()


select
--row_number()over(order by e.salary desc) as rb_by_salary,
--rank()over(order by e.salary desc) as rnk_by_salary,
--dense_rank()over(order by e.salary desc) as drnk_by_salary,
distinct -- duplikáció szűr
sum(e.salary)over(partition by e.job_id) as sum_salary_by_job,
count(e.employee_id)over(partition by e.job_id) as cnt_employee,
min(e.salary)over(partition by e.job_id) as min_salary,
max(e.salary)over(partition by e.job_id) as max_salary,
avg(e.salary)over(partition by e.job_id) as avg_salary,
e.job_id
from employee e
order by sum_salary_by_job desc;


select * from jobs;
select * from employee where job_id = 1 order by salary;
select *from departments;
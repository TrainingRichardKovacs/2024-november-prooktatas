/*
 * case when
 * 
 * SQL -ben az if-else
 * 
 * */

-- 63000 alattiak 20%, 70-63 ezer között 5%, mindenki más 3.7-et kap
select
e.*,
case 
	when 63000 > e.salary then e.salary * 1.2
	when e.salary > 63000 and 70000 >= e.salary then e.salary * 1.05
	when e.salary > 70000 and 73000 > e.salary then
		case 
			when e.job_id in (1, 2, 3, 4) then e.salary * 1.1
			else e.salary * 1.04
		end		
	else e.salary * 1.037
end as new_salary,
case job_id
	when 1 then 'Mit tudom én'
	when 2 then 'Nem tudom'
	when 6 then 'fogalma sincs'
	else 'honnan kéne tudnom'
end as job_id_desc
from employee e;
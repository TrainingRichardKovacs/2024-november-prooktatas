-- EXISTS
select * from jobs j
where not exists 
(select distinct e.job_id d from employee e where j.job_id = e.job_id);


/*
 * jobs táblának minden rekordjánál egyesével meghivja a subselect-et
 * */
select * from jobs j
where j.job_id not in (select distinct e.job_id d from employee e);

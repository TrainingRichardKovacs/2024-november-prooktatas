/*
 * Date functions
 * 
 * */

--now() - 2025-01-29 18  :34:43.962 +0100
--now() - YYYY-MM-DD HH24:MI:SS.MS    +timezone beállitás
select now(), current_timestamp, localtime, current_time;

select
e.start_date,
trim(to_char(1.8, '999G999D99S'))
from employee e;


select
e.start_date,
to_char(e.start_date, '-Mon-D- Almafa          YYYY')
from employee e;


select to_char(now(), 'Day');

select to_date('2025/01/29', 'YYYY/MM/DD');

--union all - halmazművelet - 

with base_data as (
	select 
		'2025/01/29' as my_date
	union all
	select 
		'2023-feb-21' as my_date
), converted_data as (
	select to_date(b.my_date, 'YYYY-MM-DD') from base_data b
)
select * from base_data
;

/*
 * union vs union all
 * 
 * union deduplikál, az union all meg nem
 * 
 * */

select 
'2025/01/29' as my_date
union
select 
'2025/01/29' as my_date;


SELECT
  TO_CHAR(
    CASE
      WHEN my_date LIKE '%/%'
        THEN TO_DATE(my_date, 'YYYY/MM/DD')
      ELSE
        TO_DATE(my_date, 'YYYY-mon-DD')
    END,
    'YYYY-MM-DD'
  ) AS my_date
FROM
(
  SELECT '2025/01/29' AS my_date
  UNION ALL
  SELECT '2023-feb-21' AS my_date
) t;

/*
 * extract
 * 
 * */

SELECT EXTRACT(CENTURY FROM TIMESTAMP '2000-12-16 12:21:13');

SELECT EXTRACT(DAY FROM TIMESTAMP '2001-02-16 20:38:40');

SELECT EXTRACT(Month FROM now());

-- interval - ha növelni vagy csökkenteni akarod a dátumodat
select now() - interval '4 year'




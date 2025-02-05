/*
 * Reguláris kifejezések 
 * 
 * test@email.hu
 * 
 * ez az en emailem: test@email.hu
 * ez az en emailem: kovacs.richard90@gmail.hu
 * 
 * */


with base_data as (
	select 'ez az en emailem: test@email.hu' as str
	union all
	select 'ez az en emailem: kovacs.richard90@gmail.hu'
	union all
	select 'ez'
), regexp_data as (
select 
	b.str,
	regexp_matches(b.str, '([a-zA-Z0-9.-\_]+)(@[a-z0-9-]+(\.[a-z]{2,3}))') as groupped,
	regexp_matches(b.str, '[a-zA-Z0-9.-\_]+@[a-z0-9-]+\.[a-z]{2,3}') as not_groupped
from base_data b)
select
r.groupped,
(r.groupped)[1] as first_group,
(r.groupped)[2] as second_group,
(r.groupped)[3] as second_group
from regexp_data r


select regexp_count('ez az 235en emailem: te523st@email.hu', '\d+')   


SELECT REGEXP_MATCHES(
  'abc123def',
  '(?:[a-zA-Z]+)([0-9]+)(?:[a-zA-Z]+)'
);




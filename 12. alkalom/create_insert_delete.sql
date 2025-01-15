/*
 * CREATE utasitás
 * Az objektum nevének egyedinek kell lennie schémánként !!!!
 * 
 * CREATE OBJEKTUM_TIPUS OBJEKTUM_NEVE BEÁLLITÁSOK, PARAMETEREK
 * 
 * Tábla létrehozása
 * Egy táblában minden oszlopnak egyedi névvel kell rendelkeznie 
 * 
 * CREATE TABLE TEST_TABLE (
 * oszlopok_nevei oszlopok_adattipusa, :null vagy not null, egyéb constraintek:
 * oszlopok_nevei2 oszlopok_adattipusa,
 * oszlopok_nevei3 oszlopok_adattipusa
 * )
 * 
 * */

drop table test_table;

create table test_table (
id integer,
name varchar(10)
);

select * from test_table;

-- adat létrehozása INSERT utasitással
-- szintaxisok

-- minden oszlophoz akarok egy rekordot létrehozni
insert into test_table values(1, 'Karcsi');
insert into test_table (name, id) values('Pista', 10);

-- megadott oszlophoz akarok rekordot létrehozni
-- csak abban az esetben lehet megcsinálni, ha NINCS AZ OSZLOPON, AMIT KIHAGYOK
-- NOT NULL CONSTRAINT

insert into test_table (id) values(2);

-- több érték egyidejű létrehozása

insert into test_table 
values 
(11, 'István'),
(12, 'Józsi'),
(13, 'Attila'),
(14, 'Ildikó');

-------------------------------------------------------------------
-- az adatok törlése - DELETE művelet, TRUNCATE művelettel

select * from test_table;

delete from test_table;

--truncate table test_table;
commit;

rollback;

/*
 * Session:
 * Egy adatbázis connection-ből nyitott önálló kapcsolat. Valójában
 * a sessin-ön keresztül futtatjuk az SQL utasitásokat
 * 
 * Tranzakció kezelés 
 * 
 * SQL utasitás érvénybe léptetése globálisan.
 * 2 fajtája van: jóváhagyás - commit utasitás
 * 				  tranzakció visszavonás - rollback utasitás
 * 
 * 
 * 
 * Session és Tranzakció kapcsolat
 * 
 * A session-ben inditott sql utasitás - tranzakció 
 * addig nem lép globálisan érvénybe, amig a tranzakciót le nem zártuk 
 * egy commit vagy egy rollback utasitással.
 * 
 * 
 * ACID
 * 
 * */

rollback;
select * from test_table;

insert into test_table (id) values(2);
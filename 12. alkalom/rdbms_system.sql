/*
 * RDBMS - Relational DataBase Management System
 * 
 * Az adatok tárolása relációk segitségével van megvalósitva.
 * Reláció fogalma: táblák közötti kapcsolatok - szülő - gyermek
 * 					illetve, maga a tábla is egy reláció.
 * 
 * Strukturáltan tároljuk az adatokat
 * Az adatok fő tárolására használt objektumok az adatbázis táblák.
 * Ezek fizikailag tartalmazzák az adatot.
 * 
 * A legtöbb RDBMS rendszer SQL nyelvet használ
 * az adatok létrehozására, módositására, törlésére
 * és az adatbázis objektumainak létrehozására,
 * módositására, megszüntetésére.
 * 
 * -------------------------------------------
 * OLTP - OnLine Transactional Processing
 * 
 * Kis rekordmennyiség módositására, létrehozására
 * ügyfelek szolgáltatáshoz való használatának adatbázis oldali megoldása
 * 
 * Technikai: nagyon gyorsan tudd a módositást végrehajtani: létrehozás, módositás, törlés
 * Itt sokkal több a felhasználó
 * Backend fejlesztők, Adatbázis fejlesztők, Full Stack fejlesztők
 * 
 * ---------------------------------------------------
 * OLAP - OnLine Analytical Processing
 * 
 * Riporting célre, adatvagyon gazdálkodás megvalósitására
 * Business Intellingece célokra történő felhasználást valósit meg.
 * Historikus adatokat elemzel (statisztikailag) -> nagy mennyiségű adatot
 * 
 * Technikai: gyorsan tudj nagy adatmennyiséget olvasni -> read műveletre fogsz optimalizálni
 * Sokkal kevesebb user -> statisztikailag vizsgálnak adatot: Reporting, Data Scientistek, Data Analystok, BI fejlesztők, Data Engineer
 * 
 * Adattárház - DWH
 * 	 - CIF, MIS, EDW
 * , Data Lake, Data Lakehouse
 * -------------------------------------------
 * */
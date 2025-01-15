/*
 * Constraintek - Megszoritások
 * 
 * NOT NULL - az az oszlop nem kaphat null értéket -> nem lehet üres
 * Unique - az oszlop értékeinek egyedinek kell lennie -> nem lehet duplikáció az adatban
 * Foreign-key
 * Primary Key - Unique + Not NULL constraint együttese
 * Check constraints - a mezőre logikai vizsgálatot tudunk beállitani -> ha ez nem teljesül, 
 * akkor az új adat nem insertálható
 * Exclusion constraints
 * 
 * */

drop table  test_table;

create table test_table (
id integer not null,
name varchar(10)
);

CREATE TABLE products (
    product_no integer,
    name text,
    price numeric CHECK (price > 0)
);

insert into test_table (name)
values ('Piroska')
;

select * from products;
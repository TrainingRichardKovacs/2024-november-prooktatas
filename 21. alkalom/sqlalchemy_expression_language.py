"""
SQLAlchemy - 

Core
ORM

Python objektumokat fogunk definiálni -> ezek segítségével fogjuk tudni az SQL műveleteket
                                            elvégezni

"""
import random
import string
import time
from sqlalchemy import create_engine, text, MetaData, Table, Column, String, Integer, and_, select, insert

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

meta = MetaData(schema="from_python")

customer_table = Table("customer",
                        meta,
                        Column('id', Integer, primary_key=True),
                        Column('customer_name', String(100)))

meta.create_all(bind=engine, checkfirst=True)

customer_insert = customer_table.insert()

customer_insert_2 = insert(customer_table)

print(customer_insert_2)


def generate_random_name():
    length = random.randint(5, 15)  # Nevek hossza 5 és 15 karakter között
    return ''.join(random.choices(string.ascii_letters, k=length)).capitalize()

# Függvény, ami 150 000 rekordot generál
def generate_multiple_data():
    return [
        {'customer_name': generate_random_name()} for _ in range(150_000)
    ]

# start_dt = time.time()

# with engine.connect() as connection:
#     for item in generate_multiple_data():
#         connection.execute(customer_table.insert(), item)
#         connection.commit()

# print(f"Sequential insert took - {time.time() - start_dt} sec")


# start_dt = time.time()

with engine.connect() as connection:
    #connection.execute(customer_table.insert(), generate_multiple_data())
    connection.commit()

# print(f"Bulk insert took - {time.time() - start_dt} sec")

"""
Sequencial vs Bulk insert

Sequencial - Soronként, iterálva insertálom az adatot -> 1 insert során 1 sor adatot insertálok
Bulk insert - Kötegelve insertálom -> 1 insert során egyszerre több adatot insertálok

Roundtrip: az az út, amit a pythonból kiadott sql utasítás 
                -> db-ben lefut az utasítás 
                -> visszatér a pythonba a válasszal

"""
# table.update().where(table.c.id == 7).values(name="foo")
customer_update = customer_table.update().where(customer_table.c.id > 188_000).values(customer_name="ricsi voltam")
print(customer_update)

with engine.connect() as connection:
    connection.execute(customer_update)
    connection.commit()

customer_delete = customer_table.delete().where(customer_table.c.customer_name=='ricsi voltam')

# DELETE FROM from_python.customer WHERE from_python.customer.customer_name = :customer_name_1
# :customer_name_1 -> bind variable -> 
# insert into customer (customer_name) values ('asgagaag')
# insert into customer (customer_name) values ('fhdydfhydhydh')
# insert into customer (customer_name) values (:customer_name)
print(customer_delete)

with engine.connect() as connection:
    connection.execute(customer_delete)
    connection.commit()


customer_select = customer_table.select() # select * from customer;
customer_select = customer_table.select().where(customer_table.c.id >185_000 ) # select * from customer where id > 185000;
customer_select = customer_table.select().where(customer_table.c.customer_name.not_like("K%") ) # select * from customer where customer_name not like 'K%';
customer_select = customer_table.select().where(and_(customer_table.c.customer_name.like("K%"), customer_table.c.id > 186_000) ) # select * from customer customer_name like 'K%' and id > 186000;

customer_select_without_table_object = select(customer_table).where(and_(customer_table.c.customer_name.like("K%"), customer_table.c.id > 186_000) ) # select * from customer customer_name like 'K%' and id > 186000;


with engine.connect() as connection:
    results = connection.execute(customer_select_without_table_object)

    for item in results:
        print(item)
    connection.commit()
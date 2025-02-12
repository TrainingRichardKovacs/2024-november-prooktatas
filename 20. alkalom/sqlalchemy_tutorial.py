"""
SQLALCHEMY

Általános, adatbázis kezeléshez használt library.

3 féle megközelítése van az SQLALCHEMY-nek

1. nativ SQL - CORE
2. expression language
3. ORM

Round trip - A backendről kiadott sql utasítás lefuttatása és az adatbázisból a backend számára
visszaküldött válasz ideje / száma

pl. insert-nél - 1 insert utasítás kb. 0.02 sec * 16 millióval

16 milliót - 1000 -> 16 000 -1 másodperc

"""
import time
from sqlalchemy import create_engine, text

# sqlite:///example.db - URL - connection string
# engine = create_engine('sqlite:///example.db')

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

my_list = []

start_dt = time.time()
with engine.connect() as conn:
     with conn.execution_options(stream_results=True, max_row_buffer=150000).execute(
        text("select * from big_sales")
    ) as result:
        my_list.extend(list(result))
        print("valami")

print(f"áthoztam az adatokat python memóriába: {time.time() - start_dt} sec")

start_dt = time.time()
with open("test.txt", "w") as f:
    f.write(str(my_list))

print(f"file kiírás: { time.time() - start_dt} sec")
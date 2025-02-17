"""
ORM - Object Relational Mapping

Az adatbázis objektum Python oldali reprezentációja
a Python class-ok segítségével

Az ORM a CRUD-os - OLTP - fejlesztéshez nagyon jó
analitikához kevésbé

"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, String, Integer, select, update, delete
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
meta = MetaData(schema="python_orm")
base = declarative_base(metadata=meta)

# model
class FilmTable(base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    director = Column(String(100))

    def __str__(self):
        return f"{self.id} - {self.title}"
    
    def __repr__(self):
        return self.__str__()

Session = sessionmaker(engine)
session = Session()

base.metadata.create_all(engine)
# insert
alien = FilmTable(title="Alien", director="Ridley Scott")
print(alien)
alien3 = FilmTable(title="Alien", director="Ridley Scott")
alien2 = FilmTable(title="Aliens", director="James Cameron")

print(alien == alien3)

# bulk insert
# session.add_all([alien, alien, alien, alien, alien, alien, alien, alien3, alien2])
#session.add_all([alien, alien2])

# session.add_all([alien, alien2])

# select 
movies = session.execute(select(FilmTable))

# for item in movies:
#     print(item[0].id, item[0].title, item[0].director)

# egyfajta update
for item in movies:
    if item[0].director == 'Ridley Scott':
        item[0].title = 'Gladiator'

movies = session.query(FilmTable)

print(list(movies))

# egy fajta update
# for item in movies:
#     if item.director == 'James Cameron':
#         item.title = "Avatar"

session.commit()
session.close()
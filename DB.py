#config

from sqlalchemy import *

engine = create_engine('mysql://root:azerty@localhost:3306/madb')
connection = engine.connect()

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Sequence,
    Float
)



#Map la table lien pour pouvoir utiliser du python directement.

Base = declarative_base()

class lien(Base):  #<-------------------------
    __tablename__  = "lien"
    id             = Column(Integer,primary_key=True, autoincrement=True) # plays nice with all major database engines
    URL           = Column(VARCHAR(400))                                    # string column need lengths
    date = Column(DateTime)

    def __init__(self, URL, date):
        self.URL = URL
        self.date = date

    def get_id(self):
        return self.id
    def get_URL(self):
        return self.URL
    def get_date(self):
        return self.date

    def __str__(self):
        self.id = id
        self.date = date
        return id

#Creer la table dans la DB

Base.metadata.create_all(engine)

#insert new row

'''newToner = lien(URL="test.com")

session.add(newToner)
session.commit()'''

  #read

'''result = engine.execute("select id, URL from lien")
for row in result:
    print row['id'], row['URL']
result.close()'''

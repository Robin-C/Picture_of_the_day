#config

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://user:pwd@localhost:3306/yourdb')
connection = engine.connect()

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

import datetime

#Map the table "lien" so you can interact with it directly in Python

Base = declarative_base()

class lien(Base):  #
    __tablename__  = "lien"
    id             = Column(Integer,primary_key=True, autoincrement=True) # plays nice with all major database engines
    URL           = Column(VARCHAR(400))                                    # string column need lengths
    date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, URL, date):
        self.URL = URL
        self.date = date

#Create the table in the database

Base.metadata.create_all(engine)

#insert new row

'''newrow = lien(URL="test.com")

session.add(newrow)
session.commit()'''

  #read

'''result = engine.execute("select id, URL from lien")
for row in result:
    print row['id'], row['URL']
result.close()'''


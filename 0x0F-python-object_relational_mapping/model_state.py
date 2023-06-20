#!/usr/bin/python3

"""A module that uses mysqlAlchemy module to abstract and
manage the instances of mysql database relations
"""


from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import sys

user = "root"
pwd = "root"
db = "hbtn_0e_6_usa"

query = "mysql+mysqldb://{}:{}@localhost:3306/{}"
engine = create_engine(query.format(user, pwd, db), pool_pre_ping=True)
Base = declarative_base()


class State(Base):
    """A class that models the object for the table relation
    Attributes:
        id: the table id
        name: the name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)

#!/usr/bin/python3

"""A module that uses mysqlAlchemy module to abstract and
manage the instances of mysql database relations
"""


from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import sys

user = sys.argv[1]
pwd = sys.argv[2]
db = sys.argv[3]

query = "mysql+mysqldb://{}:{}@localhost:3306/{}"
engine = create_engine(query.format(user, pwd, db), pool_pre_ping=True)
Base = declarative_base()

class State(Base):
	__tablename__ = 'states'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(128), nullable=False)

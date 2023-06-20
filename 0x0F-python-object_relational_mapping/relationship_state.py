#!/usr/bin/python3

"""A module that uses mysqlAlchemy module to abstract and
manage the instances of mysql database relations
"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """A class that models the object for the table relation
    Attributes:
        id: the table id
        name: the name
        cities: the cities relationship
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = \
        relationship('City', cascade='all, delete', back_populates='states')

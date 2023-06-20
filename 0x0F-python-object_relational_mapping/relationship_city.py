#!/usr/bin/python3

"""A module that creates a city class using sql alchemy
"""

from sqlalchemy import String, Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """A class that creates a city object for the relational
    database
    ATTRIBUTES:
        id: Auto_generated, Integer, primary key, not null
        name: City name, 128 string characters
        state_id: foreign key, not null
        states: relationship state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    states = relationship('State', back_populates='cities')

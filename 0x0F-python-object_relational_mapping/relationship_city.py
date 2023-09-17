#!/usr/bin/python3
""" defines a class 'City' that represents the 'City' table """

from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base, State


class City(Base):
    """ represents City table """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))

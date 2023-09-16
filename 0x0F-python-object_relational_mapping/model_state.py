#!/usr/bin/python3
""" defines a class 'State' that represents the 'states' table """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ represents states table """
    __tablename__ = "states"
    id = Column(Integer, Primary_key=True)
    name = Column(String(128), nullable=False)

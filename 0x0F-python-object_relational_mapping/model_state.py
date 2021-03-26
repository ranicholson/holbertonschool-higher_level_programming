#!/usr/bin/python3

""" Class State that inherits from Base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
      tablename (str): Name of table to link to
      id (int): state id
      name (str): name of state
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3

""" Class City that inherits from Base"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """State class
      tablename (str): Name of table to link to
      id (int): state id
      name (str): name of state
      state_id (int): ID of state in which city is located
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

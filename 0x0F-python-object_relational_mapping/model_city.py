#!/usr/bin/python3
"""Class definition of a state and an instance Base = declarative_base()"""
from model_state import Base
from sqlalchemy import Integer, Column, String, ForeignKey


class City(Base):
    """
    __tablename__ (str): --- table name of the class.
    id (int): -------------- id of the class.
    name (str): ------------ name of the class.
    state_id (int): -------- identifier number.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

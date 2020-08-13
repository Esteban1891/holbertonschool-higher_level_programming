#!/usr/bin/python3
"""Class definition of a state and an instance Base = declarative_base()"""
from model_state import Base
from sqlalchemy import Integer, Column, String, ForeignKey


class City(Base):
    """class city inherits Base"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_keys('states.id'))

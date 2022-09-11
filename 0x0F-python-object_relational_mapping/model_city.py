#!/usr/bin/python3
"""Base class for alchemy"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from model_state import Base, State


class City(Base):
    """State table class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")


State.cities = relationship("City", order_by=City.id,
                            back_populates="state")

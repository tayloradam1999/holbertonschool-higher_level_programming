#!/usr/bin/python3

"""
Class definition of a State and instance <Base = declarative_base()>
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):
    """links to the MySQL table <states>"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

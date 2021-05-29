#!/usr/bin/python3

"""
Class definition of a State and instance <Base = declarative_base()>
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa',
                       echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class State(Base):
    """links to the MySQL table <states>"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

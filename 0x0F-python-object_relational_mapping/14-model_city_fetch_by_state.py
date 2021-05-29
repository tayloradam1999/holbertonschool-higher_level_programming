#!/usr/bin/python3

"""
List all <State> objects from the database <hbtn_0e_6_usa>
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City)\
                              .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

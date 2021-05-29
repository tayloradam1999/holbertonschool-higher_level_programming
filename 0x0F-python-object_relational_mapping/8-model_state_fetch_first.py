#!/usr/bin/python3

"""
List the first <State> object from the database <hbtn_0e_6_usa>
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).first()
    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing\n")

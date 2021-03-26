#!/usr/bin/python3
""" Script that adds state object Louisiana to database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    nstate = State(name="Louisiana")
    session.add(nstate)
    session.commit()
    print(nstate.id)
    session.close()

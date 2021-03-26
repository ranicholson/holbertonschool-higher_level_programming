#!/usr/bin/python3
""" Script that lists all state objects from specified database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            session.delete(state)
    session.commit()
    session.close()

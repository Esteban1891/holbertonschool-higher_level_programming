#!/usr/bin/python3
"""cript that lists all State objects
   from the database hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from model_state import State, Base
from sys import argv
from sqlalchemy.orm import sessionmaker


def model_state():
    """initializate function model_state for db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # associate it with our custom Session class
    Session = sessionmaker()

    # associate it with our custom Session class
    Session.configure(bind=engine)

    session = Session()

    rows = session.query(State).order_by(State.id).all()

    for state in rows:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == '__main__':
    model_state()

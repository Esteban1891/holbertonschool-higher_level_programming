#!/usr/bin/python3
"""script that prints the first State
object from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def model_state_first():
    """create function"""
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

    rows = session.query(State).order_by(State.id).first()

    if rows:
        print('{}: {}'.format(rows.id, rows.name))
    else:
        print("Nothing")

    session.close()


if __name__ == '__main__':
    model_state_first()

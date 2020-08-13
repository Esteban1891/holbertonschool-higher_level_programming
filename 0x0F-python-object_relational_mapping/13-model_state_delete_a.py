#!/usr/bin/python3
"""script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


def model_state_delete():
    """function that delete the letter a"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id).all()

    for state in rows:
        if 'a' in state.name:
            session.delete(state)

    session.commit()
    session.close()


if __name__ == '__main__':
    model_state_delete()

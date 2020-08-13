#!/usr/bin/python3
"""script that changes the name of a State
   object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


def model_state_update():
    """functio that changes name of
    state object of my db"""
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

    update_state = session.query(State).filter_by(id=2).first()

    update_state.name = 'New Mexico'
    session.commit()
    session.close


if __name__ == '__main__':
    model_state_update()

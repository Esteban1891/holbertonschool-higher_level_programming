#!/usr/bin/python3
"""script that prints the State object with the name
   passed as argument from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


def model_state_my_get():
    """my function that print state"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # associate it with our custom Session class
    Session = sessionmaker()

    Session.configure(bind=engine)

    session = Session()

    rows = session.query(State)

    unk = ""

    for state in rows:
        if state.name == argv[4]:
            unk = state.id
    if unk is not "":
        print(unk)
    else:
        print("Not Found")

    session.close


if __name__ == '__main__':
    model_state_my_get()

#!/usr/bin/python3
"""file similar to model_state.py named model_city.p
    y that contains the class definition of a City
"""
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


def model_city_fetch_by_state():
    """function file similar to
    model_state.py named model_city.py
    """
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

    rows = session.query(City, State)\
                  .filter(City.state_id == State.id)\
                  .order_by(City.id).all()

    for state, city in rows:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    model_city_fetch_by_state()

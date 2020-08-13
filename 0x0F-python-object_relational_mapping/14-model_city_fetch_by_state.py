#!/usr/bin/python3
"""file similar to model_state.py named model_city.p
    y that contains the class definition of a City
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmake


def model_city_fetch_by_state():
    """function file similar to
    model_state.py named model_city.py
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        .argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(City, State) \
                   .filter(City.state_id == State.id) \
                   .order_by(City.id)

    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    model_city_fetch_by_state()

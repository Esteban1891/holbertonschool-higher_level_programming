#!/usr/bin/python3
"""Script that adds the State object Louisiana
to the database 'hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def model_city_fetch_by_state():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

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

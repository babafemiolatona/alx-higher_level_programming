#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        for city, state in session.query(City, State).filter(
                City.state_id == State.id).order_by(City.id).all():
            print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.close()
    else:
        print("Usage: ./14-model_city_fetch_by_state.py <username> <password> \
            <database name>")

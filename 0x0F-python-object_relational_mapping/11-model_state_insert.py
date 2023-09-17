#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
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
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        print("{}".format(new_state.id))
        session.close()
    else:
        print("Usage: ./11-model_state_insert.py <username> <password> \
            <database name>")

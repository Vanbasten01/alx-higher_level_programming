#!/usr/bin/python3
""" a script that lists all State objects that contain
    the letter 'a' from the database hbtn_0e_6_us.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(username, password, db_name),
                       pool_pre_ping=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
states_name_a = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id).all()
)

for state in states_name_a:
    print(state.id, state.name, sep=': ')
session.close()

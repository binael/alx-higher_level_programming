#!/usr/bin/python3

"""A script that uses the sqlalchemy module to abstract and
manipulate objects in a relational database
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    state_name = 'New Mexico'

    query = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(query.format(user, pwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    id = 2
    state = session.get(State, id)
    state.name = state_name
    session.commit()

    session.close()

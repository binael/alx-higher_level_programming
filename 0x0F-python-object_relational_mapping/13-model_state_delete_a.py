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

    query = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(query.format(user, pwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id)

    for state in states:
        session.delete(state)

    session.commit()

    session.close()

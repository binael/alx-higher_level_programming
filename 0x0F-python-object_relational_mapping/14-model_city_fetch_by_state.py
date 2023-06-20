#!/usr/bin/python3

"""A script that uses sqlalchemy module to abstract and
manipulates a relational database
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import Base, State
    import sys

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    conn = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    engine = create_engine(conn.format(user, pwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id).order_by(City.id).all()

    for city, id, state in data:
        print("{}: ({}) {}".format(city, id, state))

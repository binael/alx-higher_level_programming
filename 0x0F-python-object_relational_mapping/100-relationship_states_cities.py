#!/usr/bin/python3

"""A script that uses the sqlalchemy module to abstract and
manipulate objects in a relational database
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from relationship_city import City
    from relationship_state import State, Base

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    query = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(query.format(user, pwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", states=new_state)
    session.add(new_state)
    session.add(new_city)

    session.commit()

    session.close()

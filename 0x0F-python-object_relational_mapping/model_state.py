#!/usr/bin/python3

"""A module that uses mysqlAlchemy module to abstract and
manage the instances of mysql database relations
"""

if __name__ == '__main__':
    from mysqlalchemy import create_engine, Column, String, Integer
    from mysqlalchemy.ext.declarative import declarative_base
    import sys

    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    query = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, pwd, db)
    engine = create_engine(query, pool_pre_ping=True)
    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)

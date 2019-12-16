#!/usr/bin/python3


def getAllStates(user2, passward2, db2):
    """ script that gets all the states when called on """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user2, passward2, db2), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    pp = session.query(State).order_by(State.id).first()
    if pp:
        print("{}: {}".format(pp.id, pp.name))
    else:
        print("Nothing")
    session.close()

if __name__ == "__main__":
    import sys
    """ protected from executing when imported """
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3])

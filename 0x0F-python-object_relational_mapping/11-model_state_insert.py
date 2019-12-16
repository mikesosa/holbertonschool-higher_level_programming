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
    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()
    for state in session.query(State).order_by(State.id).all():
        if "Louisiana" == state.name:
            print("{}".format(state.id))
    session.close()
    # engine = sqlalchemy.create_engine()
    # db = MySQLdb.connect(host=MY_HOST, user=MY_USER, db=MY_DB)
    # cur = db.cursor()

if __name__ == "__main__":
    import sys
    """ protected from executing when imported """
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3])

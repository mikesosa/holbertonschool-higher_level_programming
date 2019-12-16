#!/usr/bin/python3


def getAllStates(user2, passward2, db2, name):
    """ script that gets all the states when called on """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user2, passward2, db2), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    counter = 0
    for state in session.query(State).order_by(State.id).all():
        if name == state.name:
            print("{}".format(state.id))
            counter = 1
            break
    if counter is 0:
        print("Not found")
    session.close()
    # engine = sqlalchemy.create_engine()
    # db = MySQLdb.connect(host=MY_HOST, user=MY_USER, db=MY_DB)
    # cur = db.cursor()

if __name__ == "__main__":
    import sys
    """ protected from executing when imported """
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

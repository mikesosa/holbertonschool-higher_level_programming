#!/usr/bin/python3


def getAllCities(user2, passward2, db2):
    """ script that gets all the states when called on """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import Base, City
    from model_state import State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                user2, passward2, db2), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for k in session.query(City, State).filter(
                State.id == City.state_id).order_by(City.id).all():
            print("{}: ({}) {}".format(k.State.name, k.City.id, k.City.name))
    session.close()
    # engine = sqlalchemy.create_engine()
    # db = MySQLdb.connect(host=MY_HOST, user=MY_USER, db=MY_DB)
    # cur = db.cursor()

if __name__ == "__main__":
    import sys
    """ protected from executing when imported """
    getAllCities(sys.argv[1], sys.argv[2], sys.argv[3])

#!/usr/bin/python3
import MySQLdb
import sys


def getAllStates(username, password, db_name):
    """ script that gets all the cities """
    # Creating connection
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=db_name, port=3306)
    # Creating a cursor
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY id ASC""")

    states = cur.fetchall()
    # Printing resutls
    for state in states:
        print(state)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()


if __name__ == "__main__":
    """ Protected from executing """
    # Calling the function taking 3 arguments
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3])

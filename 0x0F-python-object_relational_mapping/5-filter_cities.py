#!/usr/bin/python3
import MySQLdb
import sys


def getAllStates(username, password, db_name, query):
    """ script that gets states queried by the user
        and safe from query injections"""
    # Creating connection
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=db_name, port=3306)
    # Creating a cursor
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
                WHERE states.name=%s
                ORDER BY cities.id ASC""", (query,))

    states = cur.fetchall()
    # Printing resutls
    myList = []
    for state in states:
        myList.append(state[0])
    print(", ".join(myList))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()


if __name__ == "__main__":
    """ Protected from executing """
    # Calling the function taking 3 arguments
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

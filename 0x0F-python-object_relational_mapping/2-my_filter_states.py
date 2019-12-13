#!/usr/bin/python3
import MySQLdb
import sys


def getAllStates(username, password, db_name, query):
    """ script that gets states queried by the user"""
    # Creating connection
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=db_name, port=3306)
    # Creating a cursor
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(query))

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
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

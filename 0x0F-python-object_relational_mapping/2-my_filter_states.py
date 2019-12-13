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
    cur.execute('SELECT * FROM states')
    states = cur.fetchall()
    # Printing all states
    for id, name in states:
        if name == query:
            print("({}, '{}')".format(id, name))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()


if __name__ == "__main__":
    """ Protected from executing """
    # Calling the function taking 3 arguments
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

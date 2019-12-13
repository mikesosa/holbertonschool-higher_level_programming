#!/usr/bin/python3
import MySQLdb
import sys


def getAllStates(username, password, db_name):
    """ script that gets all the states when called on """
    # Creating connection
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=db_name, port=3306)
    # Creating a cursor
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    states = cur.fetchall()
    # Printing all states
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

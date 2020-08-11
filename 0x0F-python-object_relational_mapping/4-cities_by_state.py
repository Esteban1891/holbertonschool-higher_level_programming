#!/usr/bin/python3
"""Display cities"""
import MySQLdb
from sys import argv


def filter__list():
    """Takes arguments argv to list from database
    Only lists with states that matches name argument

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8",
                         )

    # Getting a cursor in MySQLdb python
    cur = db.cursor()

    # Executing db queries
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    # fetches all the rows of a query result
    query_rows = cur.fetchall()

    # Printing the result one in one
    for row in query_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    filter__list()

#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


def list__cities():
    """Takes arguments argv to list from database
    Only lists with states that matches name argument

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8"
                         )

    # Getting a cursor in MySQLdb python
    cur = db.cursor()

    # Executing db queries
    cur.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name = '{:s}'\
                    ORDER BY cities.id ASC".format(argv[4]))

    # fetches all the rows of a query result
    query_rows = cur.fetchall()

    res = []
    # Printing the result one in one
    for row in query_rows:
        res.append(row[0])

    # Printing DATABASE of states name
    print(", ".join(res))

    cur.close()
    db.close()


if __name__ == '__main__':
    list__cities()

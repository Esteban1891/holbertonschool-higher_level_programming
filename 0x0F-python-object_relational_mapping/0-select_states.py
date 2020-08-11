#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


def get__db():
    """Takes arguments argv to list from database

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
                         charset="utf8"
                         )

    # Getting a cursor in MySQLdb python
    cur = db.cursor()

    # Executing db queries
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # fetches all the rows of a query result
    query_rows = cur.fetchall()

    # Printing the result one in one
    for row in query_rows:
        print(row)

    cur.close()
    db.close()

if __name__ == '__main__':
    get__db()

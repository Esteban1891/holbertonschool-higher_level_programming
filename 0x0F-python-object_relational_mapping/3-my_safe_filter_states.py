#!/usr/bin/python3
"""Display name argument of states table"""
import MySQLdb
from sys import argv


def attack__sql_injection():
    """Takes arguments argv to list from database
    Only lists with states that matches name argument

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """

    # Build safety string for make query and avoid sql injection
    if len(argv) == 5:
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
        cur.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                ORDER BY id ASC".format(argv[4]))

        # fetches all the rows of a query result
        query_rows = cur.fetchall()

        # Printing the result one in one
        for row in query_rows:
            print(row)

        cur.close()
        db.close()
    else:
        return


if __name__ == '__main__':
    attack__sql_injection()

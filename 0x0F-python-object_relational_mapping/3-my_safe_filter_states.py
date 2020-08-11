#!/usr/bin/python3
'''
This script select an state that matchs with a user input,
but avoiding SQL injection.
'''

from sys import argv
import MySQLdb

if __name__ == '__main__':

    # declaring arguments passed, with query.
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]

    # creating connection to the database.
    db_connection = MySQLdb.connect(host="localhost", port=3306, user=user,
                                    passwd=passwd, db=db, charset="utf8")

    # Making a cursor Object for query execution.
    cursor = db_connection.cursor()

    # Executing query.
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                   (name,))
    query_rows = cursor.fetchall()

    # Printing DATABASE
    for row in query_rows:
        if row[1] == name:
            print(row)

    cursor.close()
    db_connection.close()

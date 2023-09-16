#!/usr/bin/python3

""" a script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches
    the argumenti.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    statement = """
    SELECT *
    FROM states
    WHERE BINARY name = '{}'
    ORDER BY id
    """.format(state_name)

    db = MySQLdb.connect("localhost", username, password, db_name, 3306)
    cur = db.cursor()
    cur.execute(statement)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

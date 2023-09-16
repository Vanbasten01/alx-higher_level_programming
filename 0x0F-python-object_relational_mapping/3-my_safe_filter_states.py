#!/usr/bin/python3
"""
    a script that takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
    But this time, it is safe from MySQL injections.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    statement = "SELECT * FROM states WHERE name = %s ORDER BY id"

    db = MySQLdb.connect("localhost", username, password, db_name, 3306)
    cur = db.cursor()
    cur.execute(statement, (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

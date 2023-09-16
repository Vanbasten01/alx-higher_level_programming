#!/usr/bin/python3
""" lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, db_name, 3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

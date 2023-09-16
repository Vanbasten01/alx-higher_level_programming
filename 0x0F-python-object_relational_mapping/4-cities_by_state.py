#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, db_name, 3360)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

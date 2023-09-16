#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    statement = """
    SELECT cities.id, cities.name, states.name FROM
    cities INNER JOIN states ON cities.state_id = states.id ORDER BY id"""

    db = MySQLdb.connect("localhost", username, password, db_name, 3360)
    cur = db.cursor()
    cur.execute(statement)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

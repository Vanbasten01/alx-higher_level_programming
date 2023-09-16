#!/usr/bin/python3
"""  a script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usai. """

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    statement = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') AS city_list FROM cities
    INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s"""

    db = MySQLdb.connect("localhost", username, password, db_name, 3360)
    cur = db.cursor()
    cur.execute(statement, [state_name])
    rows = cur.fetchall()

    if rows:
        city_list = rows[0][0]
        print(city_list)

    cur.close()
    db.close()

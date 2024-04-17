#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    sql_cmd = "SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    rows = cursor.execute(sql_cmd)
    for i in range(rows):
        print(cursor.fetchone())
    cursor.close()
    db.close()

#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Lists all cities from the database hbtn_0e_4_usa """
    my_db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], password=argv[2], db=argv[3])
    cur = my_db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    my_db.close()

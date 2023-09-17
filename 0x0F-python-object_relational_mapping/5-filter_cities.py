#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Lists all cities from the database hbtn_0e_4_usa """
    my_db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], password=argv[2], db=argv[3])
    cur = my_db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON \
    cities.state_id=states.id WHERE states.name = %s ORDER BY cities.id ASC""",
                (argv[4],))
    rows = cur.fetchall()
    print(", ".join([i[0] for i in rows]))
    cur.close()
    my_db.close()

#!/usr/bin/python3
""" Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa """
    my_db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], password=argv[2], db=argv[3])
    cur = my_db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}' \
    ORDER BY id ASC""".format(argv[4]))
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    my_db.close()

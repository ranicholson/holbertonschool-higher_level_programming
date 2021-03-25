#!/usr/bin/python3
""" Script that lists all states from specified database"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    states = cursor.execute("""SELECT * FROM states ORDER BY id ASC""")
    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()

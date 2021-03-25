#!/usr/bin/python3
""" Script that lists cities from specified database"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities JOIN states ON\
                cities.state_id=states.id WHERE states.name\
                = %(name)s ORDER BY cities.id ASC""", {'name': argv[4]})
    result = cursor.fetchall()
    rows = []
    rows = [i[0] for i in result]
    print(*rows, sep=", ")

    cursor.close()
    db.close()

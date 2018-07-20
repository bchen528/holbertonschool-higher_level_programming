#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name=%s\
    ORDER BY cities.id"
    num_rows = cur.execute(sql, (argv[4],))
    for i in range(num_rows):
        res = cur.fetchone()
        if i != num_rows - 1:
            for item in res:
                print("{}, ".format(res[0]), end="")
        else:
            for item in res:
                print("{}".format(res[0]))
    cur.close()
    db.close()

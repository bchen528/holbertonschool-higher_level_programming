#!/usr/bin/python3
"""
takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument,
safe from MySQL injections
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name=%s ORDER BY states.id"
    num_rows = cur.execute(sql, (argv[4], ))
    for i in range(num_rows):
        print(cur.fetchone())

#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name='{:s}'\
    ORDER BY states.id".format(argv[4])
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()

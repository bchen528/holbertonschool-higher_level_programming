#!/usr/bin/python3
"""lists all states from the database"""
import MySQLdb


db = MySQLdb.connect(host="localhost", port=3306,
                     user="root", passwd="", db="hbtn_0e_0_usa")
cur = db.cursor()
num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
for i in range(num_rows):
    print(cur.fetchone())

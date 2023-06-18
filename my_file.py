#!/usr/bin/env python3

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="bina", db="hbtn_0d_usa")
cur = db.cursor()
cur.execute("SELECT * FROM cities ORDER BY name")
query = cur.fetchall()

for city in query:
    my_city = city[2]
    print(my_city)

cur.close()
db.close()

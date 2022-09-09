#!/usr/bin/python3
"""Reading a database table"""

import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', port=3306,
        user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
r = cur.execute('SELECT * FROM states')
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()

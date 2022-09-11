#!/usr/bin/python3
"""Reading a database table with filter"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    if (len(sys.argv) != 4):
        quit()
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    r = cur.execute('SELECT * FROM states ' +
                    'WHERE name LIKE \'N%\' ' +
                    'ORDER BY states.id')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
